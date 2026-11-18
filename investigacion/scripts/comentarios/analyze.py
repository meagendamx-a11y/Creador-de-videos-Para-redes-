import json, glob, os, csv, sys, collections, math, re, random
sys.path.insert(0, os.path.dirname(__file__))
from codebook import CODES, code, lang, norm

BASE = '/tmp/claude-0/-home-user-Creador-de-videos-Para-redes-/f6e80049-54f1-5e5b-b0dd-1d5ea884d7d2/scratchpad'
OUT = BASE + '/research/comments'
TAB = OUT + '/tablas'; os.makedirs(TAB, exist_ok=True)

# Channel typology
TIPO = {
 'La Psicología Invisible': 'animado_es', 'Psych2Go Español - Psicología Para Llevar': 'animado_es',
 'Psicología Animada': 'animado_es', 'Escéptico': 'animado_es', 'Sapiencia práctica': 'animado_es',
 'Sprouts Español': 'animado_es', 'CuriosaMente': 'animado_es',
 'Psych2Go': 'animado_en', 'The School of Life': 'animado_en', 'Sprouts': 'animado_en',
 'AprendemosJuntos': 'entrevista_es', 'César Lozano': 'entrevista_es',
}
sel = {r['id']: r for r in csv.DictReader(open(OUT + '/seleccion_videos.tsv'), delimiter='\t')}

files = {}
for f in glob.glob(BASE + '/yt/comments/*.json'):
    files[os.path.basename(f)[:-5]] = f
for f in glob.glob(OUT + '/raw/*.info.json'):
    vid = os.path.basename(f)[:-10]
    try:
        d = json.load(open(f))
        if d.get('comments'): files[vid] = f
    except Exception: pass

videos = []; comments = []
for vid, f in files.items():
    d = json.load(open(f))
    C = d.get('comments') or []
    if not C: continue
    ch = d.get('channel') or ''
    dur = d.get('duration') or 0
    s = sel.get(vid, {})
    fmt = s.get('formato') or ('shorts' if (dur and dur <= 180 and '/shorts/' in (d.get('webpage_url') or '')) or (dur and dur <= 61) else 'videos')
    views = d.get('view_count') or (int(s['vistas']) if s.get('vistas') else None)
    med = float(s['mediana_canal']) if s.get('mediana_canal') else None
    grupo = s.get('grupo')
    if not grupo:
        grupo = 'previo'
    tipo = TIPO.get(ch, 'psicologo_es')
    v = dict(id=vid, canal=ch, tipo=tipo, formato=fmt, grupo=grupo, vistas=views, mediana=med,
             titulo=(d.get('title') or '')[:100], fecha=d.get('upload_date'), likes=d.get('like_count'),
             n_coment_total=d.get('comment_count'), n_desc=len(C),
             n_top=sum(1 for c in C if c.get('parent') == 'root'))
    # performance tier for prior (unselected) videos: relative to 25k / 250k absolute thresholds
    if grupo == 'previo' and views:
        v['grupo'] = 'viral' if views >= 500000 else ('bajo' if views < 100000 else 'medio')
    videos.append(v)
    for c in C:
        t = c.get('text') or ''
        cs = code(t)
        if 'CRISIS' in cs and 'CONFESION' not in cs: cs.append('CONFESION')
        comments.append(dict(video=vid, canal=ch, tipo=tipo, formato=fmt, grupo=v['grupo'],
            top=c.get('parent') == 'root', likes=c.get('like_count') or 0, by_uploader=bool(c.get('author_is_uploader')),
            hearted=bool(c.get('is_favorited')), lang=lang(t), len=len(t), text=t, codes=cs))

# drop creator's own comments
comments = [c for c in comments if not c['by_uploader']]
json.dump(videos, open(OUT + '/videos_meta.json', 'w'), ensure_ascii=False, indent=1)
with open(OUT + '/comentarios_codificados.csv', 'w', newline='') as o:
    w = csv.writer(o); w.writerow(['video', 'canal', 'tipo', 'formato', 'grupo', 'es_raiz', 'likes', 'idioma', 'codigos', 'texto'])
    for c in comments: w.writerow([c['video'], c['canal'], c['tipo'], c['formato'], c['grupo'], int(c['top']), c['likes'], c['lang'], '|'.join(c['codes']), c['text'].replace('\n', ' ')])

def table(rows, name, keyf=None):
    """Per-code counts, % and like-weighted % (weight = log(1+likes)+1 to temper outliers; also raw-like share)."""
    groups = collections.defaultdict(list)
    for c in rows: groups[keyf(c) if keyf else 'TOTAL'].append(c)
    res = []
    for g, R in sorted(groups.items()):
        n = len(R); L = sum(c['likes'] for c in R) or 1
        W = sum(math.log1p(c['likes']) + 1 for c in R)
        for k in CODES:
            m = [c for c in R if k in c['codes']]
            res.append(dict(grupo=g, codigo=k, n_grupo=n, n=len(m), pct=round(100 * len(m) / n, 2) if n else 0,
                            pct_likes=round(100 * sum(c['likes'] for c in m) / L, 2),
                            pct_logw=round(100 * sum(math.log1p(c['likes']) + 1 for c in m) / W, 2) if W else 0))
    if not res: return res
    with open(f'{TAB}/{name}.csv', 'w', newline='') as o:
        w = csv.DictWriter(o, fieldnames=list(res[0].keys())); w.writeheader(); w.writerows(res)
    return res

top = [c for c in comments if c['top']]
es_top = [c for c in top if c['lang'] == 'es']
tot = table(top, 'codigos_total_raiz')
table(es_top, 'codigos_es_raiz')
table(es_top, 'codigos_por_tipo', lambda c: c['tipo'])
table([c for c in top if c['tipo'] == 'animado_en'], 'codigos_animado_en')
table(es_top, 'codigos_por_canal', lambda c: c['canal'])
table(es_top, 'codigos_viral_vs_bajo', lambda c: c['grupo'])
table(es_top, 'codigos_por_formato', lambda c: c['formato'])
table([c for c in comments if not c['top'] and c['lang'] == 'es'], 'codigos_respuestas_es')
table([c for c in es_top if c['tipo'] != 'animado_en'], 'codigos_tipo_x_grupo', lambda c: c['tipo'] + '|' + c['grupo'])

# Summary print
print('videos', len(videos), 'comentarios', len(comments), 'raiz', len(top), 'raiz_es', len(es_top))
print('idiomas', collections.Counter(c['lang'] for c in comments))
print('canales', len(set(v['canal'] for v in videos)))
print('grupos', collections.Counter(v['grupo'] for v in videos), collections.Counter(v['tipo'] for v in videos), collections.Counter(v['formato'] for v in videos))
for r in table(es_top, '_tmp'):
    print(f"{r['codigo']:20s} n={r['n']:5d} {r['pct']:6.2f}%  likes%={r['pct_likes']:6.2f}  logw%={r['pct_logw']:6.2f}")
os.remove(f'{TAB}/_tmp.csv')

# Samples for manual validation (precision check): 25 random per code
random.seed(7)
with open(OUT + '/muestras_validacion.txt', 'w') as o:
    for k in CODES:
        m = [c for c in es_top if k in c['codes']]
        o.write(f'\n===== {k} (n={len(m)})\n')
        for c in random.sample(m, min(25, len(m))):
            o.write(f"  - [{c['likes']}] {c['text'][:230].replace(chr(10), ' ')}\n")
# Top 50 by likes (Spanish, top-level)
with open(OUT + '/top50_likes.txt', 'w') as o:
    for c in sorted(es_top, key=lambda c: -c['likes'])[:50]:
        o.write(f"[{c['likes']}] ({c['canal']} | {c['grupo']} | {','.join(c['codes'])}) {c['text'][:400].replace(chr(10), ' ')}\n")
# Topic requests, therapy, visual: full dumps sorted by likes
for k, fn in [('PIDE_TEMA', 'pedidos_tema.txt'), ('TERAPIA', 'menciones_terapia.txt'), ('VISUAL', 'menciones_visual.txt'),
              ('VOZ', 'menciones_voz.txt'), ('CRIT_IA', 'criticas_ia.txt'), ('CRIT_EXACT', 'criticas_exactitud.txt'),
              ('CRIT_PATOLOG', 'criticas_patologizacion.txt'), ('HOROSCOPO', 'horoscopo.txt'), ('VIDEO_COMO_TERAPIA', 'video_como_terapia.txt'),
              ('CRISIS', 'crisis.txt'), ('AYUDA', 'pedidos_ayuda.txt'), ('CRIT_FORMA', 'criticas_forma.txt'), ('HUMANO', 'humano.txt')]:
    m = [c for c in comments if k in c['codes'] and c['lang'] in ('es', 'otro')]
    with open(f'{OUT}/{fn}', 'w') as o:
        for c in sorted(m, key=lambda c: -c['likes']):
            o.write(f"[{c['likes']}] ({c['canal']} | {c['tipo']} | {c['grupo']} | {'raiz' if c['top'] else 'resp'}) {c['text'][:500].replace(chr(10), ' ')}\n")
# per-video table
with open(TAB + '/videos.csv', 'w', newline='') as o:
    w = csv.DictWriter(o, fieldnames=list(videos[0].keys())); w.writeheader(); w.writerows(sorted(videos, key=lambda v: (v['canal'], v['grupo'])))
