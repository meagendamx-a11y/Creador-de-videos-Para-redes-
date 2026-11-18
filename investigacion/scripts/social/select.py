import json, glob, os, statistics, sys, re
# Per channel: top-2 and ~p10 low-2 long videos (skipping newest), top-1/low-1 shorts,
# restricted to psychology/mental-health titles (titles may come auto-translated to English).
base = sys.argv[1]
chdir = os.path.join(base, 'channels')
prior = '/tmp/claude-0/-home-user-Creador-de-videos-Para-redes-/f6e80049-54f1-5e5b-b0dd-1d5ea884d7d2/scratchpad/yt'
DROP = {'EvaMariaBeristain', 'MenteOn'}
PSY = re.compile(r"psic|psych|ansie|anxi|depres|emoci|emotion|apego|attach|trauma|autoestima|self.?esteem|narcis|amor|love|pareja|relationship|duelo|grief|miedo|fear|afraid|estr[eé]s|stress|tdah|adhd|autis|terapi|therap|mente\b|mind|cerebro|brain|soledad|lonel|felic|happi|sentim|feel|celos|jealous|t[oó]xic|infancia|childhood|personalidad|personality|introvert|\bira\b|anger|culpa|guilt|shame|p[aá]nico|panic|dopamin|sesgo|bias|pensamiento|thought|confianza|confidence|rechazo|rejection|dependencia|hijos|crianza|parent|ruptura|let go|soltar|perdon|forgiv|personas que|people who|hipervigil|distimia|dysthym|sueño|sleep|burnout|agotad|tired|cansad|insegur|procrastin|motivac|h[aá]bito|habit|vagus|vago|mindful|medita|conducta|behavior|pygmalion|sibling|emp[aá]t|empath|deseo|desire|depress|suicid|amig|friend|loco|crazy")
BAD = re.compile(r"open english|taller|en vivo|\blive\b|curso|course|exam|parrot|tacos|viaje|trip\b|gestaci|regalos|christmas|navid|ispe|carl lewis|atleta|deportista|athlete|birth|anesthes|nuevo video:|pregabal|fluox|toynbee|civilizac|lama|stoic|karma")
sources = {}
for f in glob.glob(chdir + '/*_videos.json') + glob.glob(chdir + '/*_shorts.json'):
    sources[f] = os.path.basename(f)[:-5].rsplit('_', 1)
for n in ['LaPsicologiaInvisible', 'PsicologiaAnimada', 'Psych2GoEspanol', 'EscepticoYT']:
    for t in ['videos', 'shorts']:
        f = f'{prior}/{n}_{t}.json'
        if os.path.exists(f): sources[f] = [n, t]
sel = []
for f, (name, tab) in sorted(sources.items()):
    if name in DROP: continue
    try: d = json.load(open(f)) or {}
    except Exception: continue
    E = [e for e in d.get('entries', []) if e.get('view_count')]
    E = E[8:] if len(E) > 30 else E[3:]
    E = [e for e in E if PSY.search((e.get('title') or '').lower()) and not BAD.search((e.get('title') or '').lower())]
    if len(E) < 6: continue
    E.sort(key=lambda e: e['view_count'])
    med = statistics.median(e['view_count'] for e in E)
    k = 2 if tab == 'videos' else 1
    top = E[-k:]
    i = max(0, int(len(E) * 0.10) - 1)
    low = E[i:i + k]
    for e in top: sel.append((name, tab, 'viral', e['id'], e['view_count'], med, (e.get('title') or '')[:80]))
    for e in low: sel.append((name, tab, 'bajo', e['id'], e['view_count'], med, (e.get('title') or '')[:80]))
with open(os.path.join(base, 'seleccion_videos.tsv'), 'w') as o:
    o.write('canal\tformato\tgrupo\tid\tvistas\tmediana_canal\ttitulo\n')
    for r in sel: o.write('\t'.join(map(str, r)) + '\n')
for r in sel: print(r[0], r[1], r[2], r[3], r[4], r[6], sep=' | ')
print(len(sel))
