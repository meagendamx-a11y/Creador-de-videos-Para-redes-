# 001 · Prompts de video para Gemini (uno por escena)

**Antes de cada escena:** adjunta `personaje/observer/referencia_gemini_conceptos_observer.jpg` y pega primero el **BLOQUE BASE** y luego el bloque de la escena.
Los tiempos salen de tu audio (57 s). Si Gemini da clips de 8 s, yo los ajusto en la edición.

## BLOQUE BASE (pegar siempre)
```
Create a VERTICAL 9:16 video (portrait, 1080x1920), {DURACIÓN} seconds, 24 fps.
CHARACTER: "The Observer" exactly as in the attached reference — warm white soft body (#FBF8F3), subtle cool-grey shading, thin soft charcoal outline, round head separate from a pear-shaped body, two small SEPARATE dot eyes, short eyebrows, tiny mouth, long soft arms. Never connect the eyes with a line. Same proportions in every frame.
STYLE: flat 2D hand-drawn illustration, like a clean animated explainer. Simple FLAT background drawn in the same 2D style, NOT photographic, NOT realistic, NOT 3D. Soft neutral palette (off-white, light grey, pale blue). No sepia, no yellow/brown tint, no film grain, no depth-of-field blur.
CAMERA: static, no zoom, no cuts. Character centered in the lower two-thirds; leave the TOP THIRD of the frame empty (plain background) for captions.
MOTION: gentle, slow and readable; one main action. Natural blinks.
NO text, NO letters, NO subtitles, NO logos, NO audio/music/voices.
```

## E1 · 0–4 s · "¿Alguna vez ganaste una discusión… en la regadera?"
```
{BASE con DURACIÓN = 6}
SCENE: The Observer stands inside a simple flat 2D shower (light blue tiles drawn as a simple grid, a pale shower curtain pulled to one side, a few soft steam swirls drawn as simple white curls).
ACTION: 0–2 s it frowns slightly and gestures like arguing, one finger raised. 2–4 s it makes a small victorious fist. 4–6 s it closes its eyes with a proud little smile and nods once.
```

## E2 · 4–13 s · Ensaya conversaciones (jefe, ex, "hace tres años")
```
{BASE con DURACIÓN = 8}
SCENE: Night bedroom in flat 2D: simple bed with a pale blue blanket, small window with a moon, soft dark-blue background. The Observer lies in bed on its back, eyes open, looking up.
ACTION: 0–2 s it blinks, awake. 2–4 s a small thought bubble pops up above it with a simple faceless figure in a tie (the boss). 4–6 s a second bubble pops up with a small heart. 6–8 s a third bubble with a simple clock; The Observer slowly turns its head toward the camera with a tired, knowing look.
```

## E3 · 13–25 s · Interacciones imaginadas: te prepara
```
{BASE con DURACIÓN = 8}
SCENE: Simple flat 2D bathroom/bedroom wall with a plain oval mirror. The Observer stands in front of the mirror; its reflection is visible.
ACTION: 0–3 s it practices talking to its reflection with small hand gestures. 3–5 s it pauses, puts a hand on its chest and takes a slow deep breath (shoulders rise and fall). 5–8 s it nods to itself, calmer, with a small confident smile.
```

## E4 · 25–32 s · Ordenar lo que sentiste
```
{BASE con DURACIÓN = 8}
SCENE: The Observer sits on a simple wooden stool holding an open notebook, plain light background.
ACTION: 0–3 s a thought bubble above its head shows a tangled scribble line. 3–6 s the tangled line slowly untangles into a smooth straight line. 6–8 s The Observer looks up from the notebook with a soft, relieved smile.
```

## E5 · 32–38 s · Cuidar tus vínculos
```
{BASE con DURACIÓN = 6}
SCENE: The Observer sits on a simple couch holding a phone with both hands, plain warm-white background.
ACTION: 0–2 s it types carefully, concentrated. 2–3 s it stops and erases (small frown). 3–5 s it types again, slower. 5–6 s it looks at the screen and smiles gently; a tiny heart floats up from the phone.
```

## E6 · 38–48 s · Cuando se vuelve un círculo
```
{BASE con DURACIÓN = 8}
SCENE: The Observer sits on the floor hugging its knees, plain light-grey background.
ACTION: 0–8 s a simple circular arrow drawn in charcoal loops continuously above its head. The Observer's shoulders slowly slump, it looks tired; at 6–8 s it sighs (shoulders drop) and rests its chin on its knees.
```

## E7 · 48–57 s · Escríbelo una vez + hablarlo con alguien
```
{BASE con DURACIÓN = 8}
SCENE: Plain light wall. The Observer stands holding a small yellow sticky note and a pencil.
ACTION: 0–3 s it writes on the sticky note. 3–5 s it sticks the note on the wall and pats it once. 5–8 s it exhales, shoulders relax, turns to the camera and gives a small warm smile and a tiny wave.
```

## Revisión de cada clip (descártalo si falla algo)
- [ ] Vertical 9:16
- [ ] Los ojos están separados y el personaje es igual a la referencia
- [ ] Fondo 2D plano, sin foto, sin sepia
- [ ] Tercio superior libre
- [ ] Sin texto ni letras dentro del video

---

## PROMPT ÚNICO · Escenas E3 a E7 en un solo video (~44 s)
Adjunta `personaje/observer/referencia_gemini_conceptos_observer.jpg` y la imagen de la E1 aprobada como referencia de estilo.
Si la herramienta solo genera 8–10 s por video, usa este mismo prompt y pide **"Generate only SCENE 3"**, luego **"SCENE 4"**, etc., o usa **"Extend"** en Flow para encadenar.

```
Create ONE continuous VERTICAL 9:16 animated video, about 44 seconds long, 24 fps, made of 5 scenes in this exact order. It will be edited later over an existing Spanish voice-over (do NOT add any audio).

CONTEXT: a short psychology explainer called "The psychology of people who rehearse conversations in their head". The voice-over explains that rehearsing conversations helps you prepare, sort out your feelings and take care of your relationships — but if it becomes a loop it wears you out, and a tip is to write it down once.

CHARACTER: "The Observer" exactly as in the attached reference — warm white soft body, thin soft charcoal outline, round head separate from a pear-shaped body, two small SEPARATE dot eyes, short eyebrows, tiny mouth, long soft arms. Never connect the eyes with a line. Same proportions and design in every scene.
STYLE: same as the attached approved shower scene — flat 2D hand-drawn illustration, simple flat backgrounds in pale blue / off-white / light grey, NOT photographic, NOT 3D, no sepia or yellow tint. Gentle, slow, readable motion, natural blinks.
CAMERA: static in each scene (no zoom). Full body visible, character medium-small and centered; keep the TOP THIRD of the frame empty for captions. Use a soft quick fade between scenes.
NO text, NO letters, NO subtitles, NO audio.

SCENE 3 (0–11 s) — voice: "In psychology this is called 'imagined interactions'… it helps you prepare, so the real conversation feels less scary."
Simple bathroom/bedroom wall with a plain oval mirror. The Observer practices talking to its reflection with small hand gestures (0–5 s), pauses, puts a hand on its chest and takes a slow deep breath (5–8 s), then nods to itself with a small confident smile (8–11 s).

SCENE 4 (11–19 s) — voice: "It also helps you understand what you felt and put your emotions in order."
The Observer sits on a simple wooden stool holding an open notebook. A thought bubble above its head shows a tangled scribble (0–3 s) that slowly untangles into a smooth straight line (3–6 s); it looks up with a soft relieved smile (6–8 s).

SCENE 5 (19–25 s) — voice: "And often it's care: you think about how to say something difficult without hurting anyone."
The Observer sits on a simple couch holding a phone with both hands. It types carefully (0–2 s), stops and erases with a small frown (2–3 s), types again slowly (3–5 s), then smiles gently as a tiny heart floats up from the phone (5–6 s).

SCENE 6 (25–35 s) — voice: "But if the rehearsal becomes a loop, the same scene again and again, and it steals your sleep… it's wearing you out."
Plain light-grey background. The Observer sits on the floor hugging its knees. A simple circular charcoal arrow keeps looping above its head the whole time; its shoulders slowly slump, it looks tired, and near the end it sighs and rests its chin on its knees.

SCENE 7 (35–44 s) — voice: "A tip: write it down once and tell your mind 'it's saved'. And if it happens often, talking to someone helps."
Plain light wall. The Observer writes on a small yellow sticky note with a pencil (0–3 s), sticks it on the wall and pats it once (3–5 s), exhales and relaxes its shoulders (5–7 s), then turns to the camera with a small warm smile and a tiny wave (7–9 s).
```

| Escena | Va en el video final | Duración |
|---|---|---|
| E3 | 13.4–24.7 s | ~11 s |
| E4 | 24.7–32.5 s | ~8 s |
| E5 | 32.5–38.0 s | ~6 s |
| E6 | 38.0–47.9 s | ~10 s |
| E7 | 47.9–57.8 s | ~10 s |

---

## ⭐ VERSIÓN 2 (30 s) · solo falta la E4
Adjunta `referencia/E1_fotograma.png` (o `referencia/E1_recorte_3s.mp4`) como referencia de estilo.
```
Create a VERTICAL 9:16 video, 10 seconds, 24 fps.
STYLE REFERENCE: match the attached clip/image EXACTLY — same character, same flat 2D hand-drawn style, same soft pale blue / off-white palette, same thin soft charcoal outline. This is the final scene of the same short video.
CHARACTER: "The Observer" — warm white soft body, round head separate from a pear-shaped body, two small SEPARATE dot eyes, short eyebrows, tiny mouth, long soft arms. Never connect the eyes with a line.
SCENE: night bedroom in flat 2D (pale blue bed and blanket, small nightstand with a lamp, a window with the moon), same style as the reference. The Observer sits up in bed, a simple charcoal circular arrow looping above its head, tired expression.
ACTION: 0–3 s the looping arrow spins above its head; it looks tired. 3–6 s it takes a small yellow sticky note and a pencil from the nightstand and writes on it. 6–8 s it sticks the note on the lamp and the looping arrow fades away. 8–10 s it exhales, lies down calmly and smiles softly, eyes closing.
CAMERA: static, no zoom, no cuts. Full body visible, character medium-small and centered; leave the TOP THIRD of the frame empty.
NO text, NO letters, NO subtitles, NO audio. No sepia, no 3D, no photographic background.
```
