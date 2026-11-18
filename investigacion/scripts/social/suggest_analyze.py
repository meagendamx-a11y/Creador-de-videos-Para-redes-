import json, re, collections, csv, unicodedata

D = "/tmp/claude-0/-home-user-Creador-de-videos-Para-redes-/f6e80049-54f1-5e5b-b0dd-1d5ea884d7d2/scratchpad/research/trends"
r = json.load(open(f"{D}/autocomplete_raw.json"))


def norm(s):
    s = s.lower().strip()
    s = "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn" or c == "̃")
    s = unicodedata.normalize("NFC", s)
    return re.sub(r"\s+", " ", s)


NOISE = r"letra|cancion|acordes|karaoke|bukis|fuerza regida|grupo |remix|manhwa|capitulo|dailymotion|temporada|pelicula|novela|rosa de guadalupe|battle cats|granny|hollow knight|zelda|minecraft|free fire|gta|xbox|whatsapp|tiktok|instagram|facebook|telcel|netflix|spotify|iphone|xiaomi|windows|cumbia|banda |los charros|marco antonio|vicente fernandez|cuisillos|gloria trevi|mp3|en vivo|lyrics|kpop|anime|drama chino|principe elfo|rey alfa|euro truck|candy crush|xenoverse|vampire|god of war|puppy playtime|saw \d"

THEMES = [
    ("Ansiedad, pánico y sobrepensar", r"ansiedad|ansios|panico|sobrepens|pensar demasiado|pensar tanto|preocup|nervios|angusti|falta el aire|me voy a morir|me ahogo|escenarios (falsos|ficticios)|ataque"),
    ("Tristeza, depresión y vacío", r"depres|triste|vacio|vacia|llorar|lloran|llora |ganas de nada|sin ganas|desanim|bajonead|decaid|cansada de existir|no me siento real|como si no fuera yo|desganad|suicid"),
    ("Soledad y aislamiento", r"\bsol[oa]s?\b|soledad|aislad|pocos amigos|no tienen amigos|se alejan de mi|me evitan|me ignoran|quedarse en casa|estar en casa|desaparecen"),
    ("Enojo, ira y gritos", r"enoj|ira\b|gritar|grito|irritab|coraje|agresiv|violent"),
    ("Estrés, burnout y agotamiento", r"estres|burnout|agotad|cansancio emocional|modo supervivencia|quemad"),
    ("Pareja: ruptura, ex y desamor", r"\bex\b|ruptura|separacion|divorcio|desamor|me dejaron|te dejen|te deje|casi algo|olvidar a|olvidarte|superar a|amar a alguien|dejar de amar|dejar de querer|no te quiere|no me quiere|correspondid|ghosting|amor de mi vida"),
    ("Pareja: celos, infidelidad y confianza", r"celos|celosa|celoso|infiel|infidelidad|engan|traicion|desconfian|me miente|mentir a mi pareja"),
    ("Apego, dependencia y narcisismo", r"apego|dependencia|depender|codependen|narcis|toxic|manipul|gaslighting|migaje|mendigar|idealizar|obsesion|red flag|castigan con silencio|maltrat|violencia|abuso"),
    ("Atracción y señales (le gusto)", r"le gustas|gustarle|te ama|me ama|enamor|crush|atractiv|coquet|me quiere\b"),
    ("Familia: madre, padre y hermanos", r"mi mama|mi papa|mis papas|mi madre|mi padre|padres|familia|hermano|suegr|nido vacio|hijo preferido"),
    ("Crianza e hijos", r"mi hijo|mi hija|hijos|ninos|nino |bebe|berrinch|adolescen|crianza|bullying|no me hace caso"),
    ("Autoestima, inseguridad y validación", r"autoestima|insegur|validacion|aprobacion|comparar|me siento fea|feo|gorda|insuficiente|inferior|atencion|importarme lo que digan|culpable|culpa\b|autosabotaje|perfeccion|timid|verguenza"),
    ("Hábitos y adicciones", r"fumar|alcohol|tomar\b|beber|drog|vape|vapear|apost|casino|tragamonedas|procrastin|celular|scroll|redes sociales|videojuegos|morder.* unas|comer por ansiedad|comer mucho|gastar dinero|adiccion|pornograf|mota"),
    ("Trauma, heridas y duelo", r"trauma|herida|infancia|duelo|muerte|perdida|fallec|luto|abandono|rechazo"),
    ("Miedos, fobias y TOC", r"miedo|fobia|toc\b|intrusiv|obsesiv|hipocondr|claustrofob|agorafob|panico escenico|hablar en publico"),
    ("Neurodivergencia (TDAH, autismo)", r"tdah|deficit de atencion|hiperactiv|autis|asperger|neurodiverg|altas capacidades|superdotad|iq|coeficiente"),
    ("Personalidad y rasgos (\"la psicología de...\")", r"personalidad|introvert|extrovert|psicologia de las personas|psicologia dice|eneagrama|mbti|16 personalidades|inteligentes|carl jung|signos? |zurd|perezos|ordenad|impuntual|llegan tarde"),
    ("Sueño", r"dormir|insomnio|pesadilla|sueno|duermen|desvelo"),
    ("Terapia y acceso al psicólogo", r"psicolog[oa]s? (gratis|gratuito|en linea|cerca|cdmx|infantil|para|online|precio|privado|imss|de pareja)|terapia|terapeuta|psiquiatr|cuanto cobra|cuanto cuesta|consulta|van al psicologo|ir al psicologo|test de (depresion|ansiedad|autismo|tdah|personalidad|autoestima|apego)"),
    ("Síntomas físicos que la gente atribuye a algo (somatización)", r"marea|cansad|debil|nudo en la garganta|presion en el pecho|oprimido el pecho|temblor|zumb|sin energia|fatiga"),
]
THEMES = [(n, re.compile(p)) for n, p in THEMES]
noise = re.compile(NOISE)

agg = {}
for x in r:
    for pos, s in enumerate(x["suggestions"]):
        n = norm(s)
        w = (1 + (10 - pos) / 10) * (3 if x["letter"] == "" else 1)
        key = (x["source"], n)
        if key not in agg:
            agg[key] = {"source": x["source"], "suggestion": n, "roots": set(), "score": 0.0, "hits": 0}
        agg[key]["roots"].add(x["root"])
        agg[key]["score"] += w
        agg[key]["hits"] += 1

rows = []
for (src, n), a in agg.items():
    themes = [] if noise.search(n) else [t for t, p in THEMES if p.search(n)]
    a["themes"] = themes
    rows.append(a)

with open(f"{D}/autocomplete_clasificado.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["fuente", "sugerencia", "raices", "score", "apariciones", "temas"])
    for a in sorted(rows, key=lambda a: -a["score"]):
        w.writerow([a["source"], a["suggestion"], "|".join(sorted(a["roots"])), round(a["score"], 2), a["hits"], "|".join(a["themes"])])

summ = collections.defaultdict(lambda: {"google": [0, 0.0], "youtube": [0, 0.0]})
ex = collections.defaultdict(list)
for a in rows:
    for t in a["themes"]:
        summ[t][a["source"]][0] += 1
        summ[t][a["source"]][1] += a["score"]
        ex[t].append(a)
out = []
for t, _ in THEMES:
    s = summ[t]
    top = sorted(ex[t], key=lambda a: -a["score"])
    out.append({"tema": t, "google_n": s["google"][0], "google_score": round(s["google"][1], 1),
                "youtube_n": s["youtube"][0], "youtube_score": round(s["youtube"][1], 1),
                "top_google": [a["suggestion"] for a in top if a["source"] == "google"][:25],
                "top_youtube": [a["suggestion"] for a in top if a["source"] == "youtube"][:25]})
out.sort(key=lambda o: -(o["google_score"] + o["youtube_score"]))
json.dump(out, open(f"{D}/autocomplete_temas.json", "w"), ensure_ascii=False, indent=1)
tot = len(rows); cl = sum(1 for a in rows if a["themes"])
print("unique", tot, "classified", cl)
for o in out:
    print(f'{o["tema"][:45]:45} G {o["google_n"]:4} {o["google_score"]:7}  Y {o["youtube_n"]:4} {o["youtube_score"]:7}')
