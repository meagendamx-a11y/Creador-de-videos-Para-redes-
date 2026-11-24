#!/usr/bin/env python3
"""Edición automática de un video vertical 9:16 a partir de una config JSON.

Uso:  python3 produccion/editar.py contenido/001_xxx/edicion.json

Pasos:
 1) Transcribe la voz (faster-whisper, local) para tener los tiempos de cada palabra.
 2) Arma cada escena (clip de Gemini recortado a 4:5, o un marcador de posición si falta).
 3) Compone el fondo de marca, títulos por sección y subtítulos palabra a palabra (ASS/libass).
 4) Mezcla la voz con música de fondo que baja sola cuando hay voz (sidechain).
Todo es local y gratuito (ffmpeg + faster-whisper).
"""
import json, os, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FONT_DIR = ROOT / "produccion" / "fuentes"
W, H = 1080, 1920
MEDIA_Y, MEDIA_H = 0, 1920  # video a pantalla completa 9:16 (títulos y subtítulos van encima)
BG = "0xFBF8F3"


def run(cmd):
    subprocess.run(cmd, check=True)


def transcribir(voz, cache):
    if cache.exists():
        return json.loads(cache.read_text())
    import numpy as np
    from faster_whisper import WhisperModel
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(voz), "-ac", "1", "-ar", "16000", "-f", "f32le", "-"],
                         check=True, capture_output=True).stdout
    audio = np.frombuffer(raw, dtype=np.float32)
    model = WhisperModel("small", device="cpu", compute_type="int8")
    segs, _ = model.transcribe(audio, language="es", word_timestamps=True)
    words = [{"w": w.word.strip(), "s": round(w.start, 2), "e": round(w.end, 2)} for s in segs for w in s.words]
    cache.write_text(json.dumps(words, ensure_ascii=False, indent=0))
    return words


def ts(t):
    t = max(t, 0)
    return f"{int(t // 3600)}:{int(t % 3600 // 60):02d}:{t % 60:05.2f}"


def ass_color(hexrgb):  # "#RRGGBB" -> &H00BBGGRR
    r, g, b = hexrgb[1:3], hexrgb[3:5], hexrgb[5:7]
    return f"&H00{b}{g}{r}".upper()


def construir_ass(cfg, words, dur, out):
    hl = {k.lower() for k in cfg.get("resaltar", [])}
    yellow = ass_color("#FFD84A")
    head = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Titulo,Nunito,62,&H002E2E2E,&H00000000,{yellow},&H00000000,-1,0,0,0,100,100,0,0,3,14,0,8,80,80,120,1
Style: Sub,Nunito,78,&H00FFFFFF,&H00000000,&H00202028,&H64000000,-1,0,0,0,100,100,0,0,1,7,2,2,70,70,170,1
Style: Firma,Nunito,30,&H00808080,&H00000000,&H00000000,&H00000000,-1,0,0,0,100,100,0,0,1,0,0,2,40,40,70,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    ev = []
    # títulos por sección (zona superior libre)
    secs = cfg["secciones"]
    for i, s in enumerate(secs):
        end = secs[i + 1]["inicio"] if i + 1 < len(secs) else dur
        if s.get("titulo"):
            ev.append(f"Dialogue: 1,{ts(s['inicio'])},{ts(end)},Titulo,,0,0,0,,{s['titulo']}")
    # subtítulos: bloques de hasta 3 palabras, cortando en puntuación
    chunks, cur = [], []
    for w in words:
        cur.append(w)
        if len(cur) == 3 or w["w"][-1:] in ".,?!:;":
            chunks.append(cur)
            cur = []
    if cur:
        chunks.append(cur)
    for i, c in enumerate(chunks):
        start = c[0]["s"]
        end = chunks[i + 1][0]["s"] if i + 1 < len(chunks) else c[-1]["e"] + 0.4
        end = min(end, c[-1]["e"] + 0.6)
        txt = []
        for w in c:
            clean = w["w"].strip(".,?!¿¡:;\"").lower()
            word = w["w"].strip(".,;:").upper()
            txt.append(f"{{\\c{yellow}}}{word}{{\\c&H00FFFFFF&}}" if clean in hl else word)
        ev.append(f"Dialogue: 2,{ts(start)},{ts(end)},Sub,,0,0,0,,{' '.join(txt)}")
    if cfg.get("firma"):
        ev.append(f"Dialogue: 0,{ts(0)},{ts(dur)},Firma,,0,0,0,,{cfg['firma']}")
    out.write_text(head + "\n".join(ev) + "\n", encoding="utf-8")


def foco_personaje(clip):
    """Centro horizontal (0–1) del personaje: píxeles casi blancos de la mitad inferior, en varios fotogramas."""
    import numpy as np
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(clip), "-vf", "fps=1,scale=320:-2", "-f", "rawvideo",
                          "-pix_fmt", "rgb24", "-"], check=True, capture_output=True).stdout
    probe = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height",
                            "-of", "csv=p=0", str(clip)], check=True, capture_output=True, text=True).stdout.strip().split(",")
    w, h = 320, round(320 * int(probe[1]) / int(probe[0]) / 2) * 2
    f = np.frombuffer(raw, dtype=np.uint8).reshape(-1, h, w, 3).astype(int)
    blanco = (f.min(axis=3) > 215) & ((f.max(axis=3) - f.min(axis=3)) < 25)
    # solo la mitad inferior: ahí está el cuerpo; arriba suelen ir burbujas/objetos que desvían el encuadre
    blanco[:, : int(h * 0.45), :] = False
    cols = blanco.sum(axis=(0, 1))
    if cols.sum() == 0:
        return 0.5
    return float((cols * np.arange(w)).sum() / cols.sum() / w)


def escena(base, s, d, out, tmp):
    clip = base / s["clip"] if s.get("clip") else None
    vf_fit = f"scale={W}:{MEDIA_H}:force_original_aspect_ratio=increase,crop={W}:{MEDIA_H}"
    if clip and clip.exists():
        wh = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height",
                             "-of", "csv=p=0", str(clip)], check=True, capture_output=True, text=True).stdout.strip().split(",")
        iw, ih = int(wh[0]), int(wh[1])
        pre = ""
        if s.get("recorte"):
            # usar solo una zona del clip (p. ej. la escena nítida cuando la IA la entrega dentro de un relleno desenfocado)
            rx, ry, rw, rh = s["recorte"]
            pre = f"crop={rw}:{rh}:{rx}:{ry},"
            iw, ih = rw, rh
        if s.get("cortar_abajo"):
            # algunos clips de IA traen una franja inferior copiada de la referencia (p. ej. subtítulos): se recorta
            nh = int(ih * (1 - s["cortar_abajo"])) // 2 * 2
            pre += f"crop={iw}:{nh}:0:0,"
            ih = nh
        if s.get("ajustar"):
            # personaje grande sobre fondo liso: se aleja el encuadre (ancho = fracción "ajustar" del original)
            # y se rellena arriba/abajo con el color del fondo del propio clip, sin costura visible
            cw = int(iw * s["ajustar"]) // 2 * 2
            fx = s.get("foco_x", foco_personaje(clip))
            x = int(min(max(fx * iw - cw / 2, 0), iw - cw))
            px = subprocess.run(["ffmpeg", "-v", "error", "-i", str(clip), "-vf", "crop=4:4:2:2,scale=1:1", "-frames:v", "1",
                                 "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], check=True, capture_output=True).stdout
            col = "0x%02X%02X%02X" % tuple(px[:3])
            vf_fit = f"crop={cw}:{ih}:{x}:0,scale={W}:-2,pad={W}:{MEDIA_H}:0:(oh-ih)/2-{s.get('subir_fondo', 120)}:color={col}"
        elif iw * MEDIA_H > ih * W:
            # clip más ancho que 9:16: recorte inteligente centrado en el personaje (o en "foco_x" si se fija a mano)
            cw = round(ih * W / MEDIA_H) // 2 * 2
            fx = s.get("foco_x", foco_personaje(clip))
            x = int(min(max(fx * iw - cw / 2, 0), iw - cw))
            print(f"  {s['id']}: recorte {cw}x{ih} en x={x} (foco {fx:.2f})")
            vf_fit = f"crop={cw}:{ih}:{x}:0,scale={W}:{MEDIA_H}:flags=lanczos"
        # leve corrección de color: quita el tinte sepia típico de los generadores
        tp = ",tpad=stop_mode=clone:stop_duration=30" if s.get("desde") is not None else ""  # si el tramo excede el video, congela el último cuadro
        vel = f",setpts={s['velocidad']}*PTS" if s.get("velocidad") else ""  # >1 = cámara lenta para sincronizar con la voz
        vf = f"{pre}{vf_fit}{vel}{tp},colorbalance=rm=-0.06:bm=0.06:rh=-0.04:bh=0.04,eq=saturation=0.9,fps=30,setpts=PTS-STARTPTS"
        desde = ["-ss", str(s["desde"])] if s.get("desde") is not None else ["-stream_loop", "-1"]  # usar un tramo de un video largo
        run(["ffmpeg", "-v", "error", "-y", *desde, "-i", str(clip), "-t", f"{d:.3f}", "-an",
             "-vf", vf, "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", "30", str(out)])
    else:
        # marcador de posición mientras llega el clip de Gemini
        label = f"Escena {s['id']} · pendiente de Gemini"
        font = FONT_DIR / "Nunito.ttf"
        run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", f"color=c=0xECE7DF:s={W}x{MEDIA_H}:r=30:d={d:.3f}",
             "-vf", f"drawtext=fontfile={font}:text='{label}':fontsize=48:fontcolor=0x8A8578:x=(w-tw)/2:y=(h-th)/2",
             "-c:v", "libx264", "-pix_fmt", "yuv420p", str(out)])


def main(cfg_path):
    cfg_path = Path(cfg_path).resolve()
    base = cfg_path.parent
    cfg = json.loads(cfg_path.read_text())
    voz, musica = base / cfg["voz"], base / cfg["musica"]
    words = transcribir(voz, base / "palabras.json")
    for idx, rep in cfg.get("correcciones", {}).items():  # arreglos de transcripción por índice
        words[int(idx)]["w"] = rep
    dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(voz)],
                               check=True, capture_output=True, text=True).stdout) + 0.8
    # Pausa inicial: quien llega haciendo scroll ve primero la imagen y el título; la voz entra después.
    # Se desplazan la voz, los subtítulos y los cortes de escena (la primera escena se alarga).
    pausa = float(cfg.get("pausa_inicial", 0.6))  # regla del canal desde el 006
    if pausa > 0:
        words = [dict(w, s=w["s"] + pausa, e=w["e"] + pausa) for w in words]
        cfg["secciones"] = [dict(s, inicio=s["inicio"] + pausa) if i else s for i, s in enumerate(cfg["secciones"])]
        dur += pausa
    out_dir = base / "render"
    out_dir.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        partes = []
        secs = cfg["secciones"]
        for i, s in enumerate(secs):
            end = secs[i + 1]["inicio"] if i + 1 < len(secs) else dur
            p = tmp / f"s{i:02d}.mp4"
            escena(base, s, end - s["inicio"], p, tmp)
            partes.append(p)
        lista = tmp / "lista.txt"
        lista.write_text("".join(f"file '{p}'\n" for p in partes))
        media = tmp / "media.mp4"
        run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(lista), "-c", "copy", str(media)])
        ass = tmp / "subs.ass"
        construir_ass(cfg, words, dur, ass)
        final = out_dir / f"{base.name}_vertical.mp4"
        mv = cfg.get("volumen_musica_db", -20)
        # El personaje suele quedar muy abajo en los clips: se sube la imagen nítida "subir_px"
        # (se recorta el cielo/pared vacíos de arriba) y abajo queda una copia desenfocada donde van los subtítulos.
        up = cfg.get("subir_px", 340)
        fc = (f"[0:v]setpts=PTS-STARTPTS,split=2[m][b];"
              f"[b]boxblur=40:2,eq=brightness=-0.08[bg];"
              f"[bg][m]overlay=0:{-up}:shortest=1,"
              f"subtitles={ass}:fontsdir={FONT_DIR}[v];"
              f"[2:a]volume={mv}dB,afade=t=out:st={dur - 2:.2f}:d=2[mus];"
              f"[1:a]adelay={int(pausa * 1000)}:all=1,asplit=2[voz][sc];"
              f"[mus][sc]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=400[duck];"
              f"[voz][duck]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[a]")
        run(["ffmpeg", "-v", "error", "-y", "-i", str(media), "-i", str(voz), "-stream_loop", "-1", "-i", str(musica),
             "-filter_complex", fc, "-map", "[v]", "-map", "[a]", "-t", f"{dur:.3f}",
             "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p",
             "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", str(final)])
        print("OK ->", final)


if __name__ == "__main__":
    main(sys.argv[1])
