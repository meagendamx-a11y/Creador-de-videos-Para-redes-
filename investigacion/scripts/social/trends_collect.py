import json, os, time, random, sys, traceback
import pandas as pd
from pytrends.request import TrendReq

OUT = "/tmp/claude-0/-home-user-Creador-de-videos-Para-redes-/f6e80049-54f1-5e5b-b0dd-1d5ea884d7d2/scratchpad/research/trends"
os.makedirs(OUT + "/raw", exist_ok=True)
ANCHOR = "psicólogo"

GROUPS = {
    "emociones": ["ansiedad", "depresión", "estrés", "soledad", "ira", "ataque de pánico", "tristeza", "insomnio"],
    "relaciones": ["apego", "narcisista", "dependencia emocional", "ruptura", "infidelidad", "relación tóxica", "celos", "duelo"],
    "familia": ["padres tóxicos", "crianza", "adolescentes", "divorcio"],
    "trabajo": ["burnout", "estrés laboral", "síndrome del impostor", "jefe tóxico"],
    "neurodivergencia": ["tdah", "autismo adultos", "tdah adultos", "autismo"],
    "autoconocimiento": ["autoestima", "personalidad", "introvertido", "inteligencia emocional", "trauma", "test de personalidad"],
    "terapia": ["terapia en línea", "psicólogo cerca de mí", "cuánto cuesta un psicólogo", "terapia psicológica", "salud mental", "psiquiatra"],
}
TERMS = [(g, t) for g, ts in GROUPS.items() for t in ts]
BATCHES = [TERMS[i:i + 4] for i in range(0, len(TERMS), 4)]

pt = TrendReq(hl="es-MX", tz=360, timeout=(10, 30))


def call(fn, label):
    for attempt in range(7):
        try:
            r = fn()
            time.sleep(random.uniform(6, 10))
            return r
        except Exception as e:
            msg = str(e)
            wait = 30 * (attempt + 1) + random.uniform(0, 10)
            print(f"[{label}] error {msg[:120]} -> wait {wait:.0f}s", flush=True)
            time.sleep(wait)
    print(f"[{label}] GAVE UP", flush=True)
    return None


def save_df(df, name):
    if df is not None:
        df.to_csv(f"{OUT}/raw/{name}.csv")


def done(name):
    return os.path.exists(f"{OUT}/raw/{name}.done")


def mark(name):
    open(f"{OUT}/raw/{name}.done", "w").close()


for bi, batch in enumerate(BATCHES):
    kws = [ANCHOR] + [t for _, t in batch]
    for prop in ["", "youtube"]:
        pname = "google" if prop == "" else "youtube"
        for tf, tfn in [("today 5-y", "5y"), ("today 12-m", "12m")]:
            name = f"b{bi:02d}_{pname}_{tfn}"
            if done(name):
                continue
            print("==>", name, kws, flush=True)
            ok = call(lambda: pt.build_payload(kws, geo="MX", timeframe=tf, gprop=prop) or True, name + ":payload")
            if not ok:
                continue
            iot = call(pt.interest_over_time, name + ":iot")
            save_df(iot, name + "_iot")
            if tfn == "12m":
                rq = call(pt.related_queries, name + ":rq")
                if rq is not None:
                    js = {}
                    for k, v in rq.items():
                        js[k] = {kk: (vv.to_dict(orient="records") if vv is not None else []) for kk, vv in (v or {}).items()}
                    json.dump(js, open(f"{OUT}/raw/{name}_related.json", "w"), ensure_ascii=False, indent=1)
                if prop == "":
                    reg = call(lambda: pt.interest_by_region(resolution="REGION", inc_low_vol=True), name + ":reg")
                    save_df(reg, name + "_region")
            mark(name)
print("ALL DONE", flush=True)
