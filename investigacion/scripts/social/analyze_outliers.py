#!/usr/bin/env python3
"""Outlier analysis over yt-dlp flat catalogs.
usage: analyze_outliers.py <outliers_dir>
reads channels.tsv, raw/*.json (titles, views, duration), dates/*.tsv (timestamps for es channels)
writes videos_all.csv, channels_summary.csv, top_outliers_es_long.csv, ... into outliers_dir
"""
import csv, json, os, re, sys, statistics, datetime, collections, unicodedata

D = sys.argv[1]
NOW = datetime.datetime(2026, 11, 18)

THEMES = [  # (code, regex) evaluated in priority order for primary theme
    ("psicologia_oscura", r"oscur|dark psych|maquiavel|machiavel|manipula|persuasi"),
    ("toxico_narcisismo", r"t[oó]xic|narcis|psic[oó]pata|psychopath|sociopat|soci[oó]pata|gaslight|red flag|abus|maltrat"),
    ("apego", r"apego|attach|evitativ|avoidant|ansios[oa] en|abandono"),
    ("trauma_heridas", r"trauma|herida|wound"),
    ("trastornos_salud_mental", r"depresi|depress|ansiedad|anxiety|tdah|adhd|autis|bipolar|esquizo|schizo|\btoc\b|\bocd\b|trastorno|disorder|\btlp\b|borderline|l[ií]mite de la person|adicci|addict|p[aá]nico|panic|burnout|estr[eé]s|stress|suicid|demencia|alzheimer|ptsd|tept|fobia|phobia|insomni"),
    ("generaciones_nostalgia", r"generaci|xennial|millennial|gen z|boomer|a[nñ]os ?[6789]0|[6789]0s\b|d[eé]cada|nost[aá]lgi|crecieron en los|grew up in the"),
    ("familia_infancia", r"infancia|ni[nñ]ez|ni[nñ]o|childhood|child|kid|padre|madre|pap[aá]|mam[aá]|parent|mother|father|crianza|hij[oa]|herman|sibling|famil|primog[eé]nit|mayor de|oldest|youngest"),
    ("amor_pareja", r"amor|pareja|enamor|love|crush|atracci|attract|relaci[oó]n|relationship|partner|ruptura|breakup|\bex\b|celos|jealous|infiel|cheat|beso|kiss|coquet|flirt|cita|dating|le gustas|likes you|soltero|single|casad|marri|sexo|sex"),
    ("inteligencia", r"inteligen|intelligen|\biq\b|\bci\b|genio|genius|superdotad|gifted|smart|listo"),
    ("personalidad_tipos", r"personalidad|personality|jung|arquetip|archetyp|temperament|mbti|infj|intj|introvert|extrovert|eneagram|sigma|tipos de person"),
    ("social_comunicacion", r"lenguaje corporal|body language|leer a|read people|caes mal|respet|amig|friend|social|conversaci|hablar|habla|talk|carisma|charism|soledad|solo\b|solos|sola\b|alone|loner|lonely|antisocial"),
    ("emociones", r"emoci|emotion|llor|cry|enoj|enfad|ira\b|anger|angry|miedo|fear|culpa|guilt|verg[uü]enza|shame|trist|sad|feliz|happy|felicidad|happiness|empat"),
    ("cerebro_cuerpo_sueno", r"cerebro|brain|dorm|sleep|sue[nñ]o|dream|memoria|memory|recuerd|neuro|cuerpo|body"),
    ("autoayuda_desarrollo", r"c[oó]mo (ser|dejar|superar|lograr|mejorar|tener|vencer|controlar|hacer|desarroll|construir|sanar|aprender)|how to|autoestima|self.esteem|confianza|confidence|liderazgo|leader|resilien|motivaci|disciplin|h[aá]bito|habit|productiv|[eé]xito|success|mentalidad|mindset|estoic|stoic|validaci"),
    ("rasgos_cotidianos", r"personas que|people who|gente que|los que|quienes|qu[eé] dice de ti|says about you|si (t[uú] )?(siempre|nunca|eres|te|haces)|if you"),
]

def theme_of(title):
    t = title.lower()
    tags = [c for c, rx in THEMES if re.search(rx, t)]
    return tags

TEMPLATES = [
    ("psicologia_de_personas_que", r"^(la )?psicolog[ií]a (de|detr[aá]s de) (las |los )?(personas|gente|hombres|mujeres|ni[nñ]os|hijos)|^(the )?psychology (of|behind) (people|men|women|those|kids|children)"),
    ("lista_senales", r"\b\d+\s*(se[nñ]ales|signos|signs|indicios|red flags|banderas)"),
    ("lista_numerada", r"^\s*\d+\s|\b\d+\s*(cosas|h[aá]bitos|things|habits|razones|reasons|tipos|types|datos|facts|formas|ways|secretos|frases|errores|mistakes|comportamientos|behaviors|tecnicas|t[eé]cnicas|trucos|tricks|preguntas|curiosidades|hechos)"),
    ("explicado_en_N_min", r"explicad[oa]s? en|explained in|en \d+ minutos|in \d+ minutes|cada .* explicad|every .* explained|todos los .* explicad"),
    ("psicologia_de_X", r"^(la |el )?psicolog[ií]a (de|del|detr[aá]s)|^(the )?psychology (of|behind)"),
    ("por_que", r"^¿?\s*por qu[eé]|^why\b|¿por qu[eé]"),
    ("que_dice_de_ti", r"dice de ti|says about you|revela|reveals|significa|means"),
    ("si_tu_condicional", r"^¿?\s*si (t[uú]|te|eres|siempre|nunca|haces|alguien)|^if (you|someone)"),
    ("crecieron_hijos_de", r"crecieron|crec[ií]|grew up|hijos de|hijo mayor|hija mayor|ni[nñ]os que|children of|oldest|eldest|raised"),
    ("como_hacer", r"^¿?\s*c[oó]mo\b|^how (to|do|can)"),
    ("que_es", r"^¿?\s*qu[eé] (es|son|pasa|sucede|hace)\b|^what (is|are|happens)"),
    ("test_quiz", r"\btest\b|quiz|examen|prueba|cu[aá]l eres|which .* are you"),
]

def template_of(title):
    t = title.lower().strip()
    for c, rx in TEMPLATES:
        if re.search(rx, t):
            return c
    return "otro"

def flags(title):
    words = re.findall(r"[A-Za-zÁÉÍÓÚÑÜáéíóúñü]{4,}", title)
    caps = [w for w in words if w.isupper()]
    return {
        "caps_emphasis": int(bool(caps) and len(caps) < len(words)),
        "all_caps_title": int(bool(words) and len(caps) == len(words)),
        "question": int("?" in title),
        "parenthetical": int("(" in title),
        "number": int(bool(re.search(r"\d", title))),
        "second_person": int(bool(re.search(r"\b(t[uú]|te|tu|tus|ti|you|your)\b", title.lower()))),
        "emoji": int(bool(re.search(r"[\U0001F300-\U0001FAFF☀-➿]", title))),
        "title_len": len(title),
    }

def load_dates(name, tab):
    p = os.path.join(D, "dates", f"{name}_{tab}.tsv")
    out = {}
    if os.path.exists(p):
        for line in open(p, encoding="utf-8"):
            parts = line.rstrip("\n").split("\t")
            if len(parts) >= 2 and parts[1] not in ("NA", "None", ""):
                try:
                    out[parts[0]] = int(float(parts[1]))
                except ValueError:
                    pass
    return out

def local_median(views, i, k=10):
    lo, hi = max(0, i - k), min(len(views), i + k + 1)
    neigh = [v for j, v in enumerate(views[lo:hi], start=lo) if j != i and v is not None]
    return statistics.median(neigh) if neigh else None

rows, chan_rows = [], []
for line in open(os.path.join(D, "channels.tsv"), encoding="utf-8"):
    name, cid, lang, kind = line.rstrip("\n").split("\t")
    for tab in ("videos", "shorts"):
        p = os.path.join(D, "raw", f"{name}_{tab}.json")
        if not os.path.exists(p) or os.path.getsize(p) < 100:
            continue
        try:
            d = json.load(open(p, encoding="utf-8"))
        except Exception:
            continue
        ents = [e for e in d.get("entries", []) if e and e.get("view_count") is not None]
        if not ents:
            continue
        dates = load_dates(name, tab)
        views = [e["view_count"] for e in ents]
        med = statistics.median(views)
        n = len(ents)
        # timestamps: es channels from dates pass, en channels from the catalog itself
        for i, e in enumerate(ents):
            ts = dates.get(e["id"]) or e.get("timestamp")
            dt = datetime.datetime.fromtimestamp(ts) if ts else None
            lm = local_median(views, i)
            r = {
                "channel": name, "lang": lang, "kind": kind, "format": "long" if tab == "videos" else "short",
                "id": e["id"], "title": unicodedata.normalize("NFC", e.get("title") or ""), "views": e["view_count"],
                "duration_s": e.get("duration"), "approx_date": dt.strftime("%Y-%m-%d") if dt else "",
                "year_q": f"{dt.year}Q{(dt.month-1)//3+1}" if dt else "",
                "age_days": (NOW - dt).days if dt else "",
                "channel_median": med, "outlier_score": round(e["view_count"] / med, 2) if med else "",
                "local_median": lm, "local_score": round(e["view_count"] / lm, 2) if lm else "",
                "upload_rank": i + 1, "channel_n": n,
            }
            tags = theme_of(r["title"])
            r["theme_primary"] = tags[0] if tags else "otro"
            r["themes_all"] = "|".join(tags)
            r["template"] = template_of(r["title"])
            r.update(flags(r["title"]))
            rows.append(r)
        top = max(ents, key=lambda e: e["view_count"])
        dts = [dates.get(e["id"]) or e.get("timestamp") for e in ents]
        dts = [x for x in dts if x]
        chan_rows.append({
            "channel": name, "lang": lang, "kind": kind, "format": "long" if tab == "videos" else "short",
            "n": n, "median_views": med, "mean_views": round(statistics.mean(views)),
            "p90_views": sorted(views)[int(0.9 * (n - 1))], "max_views": top["view_count"],
            "total_views": sum(views),
            "top10_share": round(sum(sorted(views, reverse=True)[:10]) / sum(views), 3) if sum(views) else "",
            "n_ge_3x": sum(1 for v in views if med and v >= 3 * med),
            "n_ge_10x": sum(1 for v in views if med and v >= 10 * med),
            "first_upload": datetime.datetime.fromtimestamp(min(dts)).strftime("%Y-%m") if dts else "",
            "last_upload": datetime.datetime.fromtimestamp(max(dts)).strftime("%Y-%m-%d") if dts else "",
            "top_title": top.get("title"),
        })

def write(path, data):
    if not data:
        return
    with open(os.path.join(D, path), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(data[0].keys()))
        w.writeheader(); w.writerows(data)

write("videos_all.csv", rows)
write("channels_summary.csv", chan_rows)

GENERAL = {"TeLoPinto", "CuriosaMente"}  # general-topic channels: keep only psych-themed videos in rankings

def eligible(r, min_n=20):
    if r["channel"] in GENERAL and r["theme_primary"] == "otro":
        return False
    if r["channel_n"] < min_n:
        return False
    if r["age_days"] != "" and r["age_days"] < 14:
        return False
    return True

for lang, fmt, k in (("es", "long", 80), ("en", "long", 50), ("es", "short", 50), ("en", "short", 30)):
    sel = [r for r in rows if r["lang"] == lang and r["format"] == fmt and eligible(r)]
    sel.sort(key=lambda r: -r["outlier_score"])
    write(f"top_outliers_{lang}_{fmt}.csv", sel[:k])
    sel2 = sorted(sel, key=lambda r: -(r["local_score"] or 0))
    write(f"top_local_outliers_{lang}_{fmt}.csv", sel2[:k])
print("rows", len(rows), "channel-tabs", len(chan_rows))
