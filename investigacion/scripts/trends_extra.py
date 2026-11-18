import json, os, time, random
import pandas as pd
from pytrends.request import TrendReq

OUT = "/tmp/claude-0/-home-user-Creador-de-videos-Para-redes-/f6e80049-54f1-5e5b-b0dd-1d5ea884d7d2/scratchpad/research/trends/raw_extra"
os.makedirs(OUT, exist_ok=True)
pt = TrendReq(hl="es-MX", tz=360, timeout=(10, 30))

# Variantes sin acento / formulaciones reales (ancla común "psicólogo")
BATCHES = {
    "x0": ["psicólogo", "psicologo", "psicologo cerca de mi", "depresion", "depresión"],
    "x1": ["psicólogo", "terapia online", "terapia en linea", "psicologo en linea", "cuanto cobra un psicologo"],
    "x2": ["psicólogo", "relacion toxica", "padres toxicos", "ataque de panico", "estres laboral"],
    "x3": ["psicólogo", "psicologo gratis", "terapia de pareja", "sindrome del impostor", "jefe toxico"],
    "x4": ["psicólogo", "ansiedad", "apego ansioso", "sobrepensar", "salud mental"],
}
REGION_TERMS = ["ansiedad", "depresion", "psicologo", "tdah", "autismo", "divorcio", "narcisista",
                "apego", "burnout", "autoestima", "terapia de pareja"]


def call(fn, label):
    for attempt in range(7):
        try:
            r = fn()
            time.sleep(random.uniform(6, 10))
            return r
        except Exception as e:
            wait = 30 * (attempt + 1) + random.uniform(0, 10)
            print(f"[{label}] {str(e)[:100]} -> {wait:.0f}s", flush=True)
            time.sleep(wait)
    print(f"[{label}] GAVE UP", flush=True)
    return None


for name, kws in BATCHES.items():
    for prop in ["", "youtube"]:
        pn = "google" if prop == "" else "youtube"
        for tf, tfn in [("today 5-y", "5y"), ("today 12-m", "12m")]:
            fn = f"{OUT}/{name}_{pn}_{tfn}"
            if prop == "youtube" and tfn == "5y":
                continue
            if os.path.exists(fn + ".done"):
                continue
            print("==>", fn, flush=True)
            if not call(lambda: pt.build_payload(kws, geo="MX", timeframe=tf, gprop=prop) or True, fn):
                continue
            iot = call(pt.interest_over_time, fn + ":iot")
            if iot is not None:
                iot.to_csv(fn + "_iot.csv")
            if tfn == "12m":
                rq = call(pt.related_queries, fn + ":rq")
                if rq is not None:
                    js = {k: {kk: (vv.to_dict(orient="records") if vv is not None else []) for kk, vv in (v or {}).items()} for k, v in rq.items()}
                    json.dump(js, open(fn + "_related.json", "w"), ensure_ascii=False, indent=1)
            open(fn + ".done", "w").close()

for t in REGION_TERMS:
    fn = f"{OUT}/region_{t.replace(' ', '_')}"
    if os.path.exists(fn + ".done"):
        continue
    print("==>", fn, flush=True)
    if not call(lambda: pt.build_payload([t], geo="MX", timeframe="today 12-m") or True, fn):
        continue
    reg = call(lambda: pt.interest_by_region(resolution="REGION", inc_low_vol=True), fn + ":reg")
    if reg is not None:
        reg.to_csv(fn + ".csv")
    open(fn + ".done", "w").close()
print("EXTRA DONE", flush=True)
