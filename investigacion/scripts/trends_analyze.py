import json, glob, os, re
import pandas as pd
import numpy as np

D = "/tmp/claude-0/-home-user-Creador-de-videos-Para-redes-/f6e80049-54f1-5e5b-b0dd-1d5ea884d7d2/scratchpad/research/trends"
R = D + "/raw"
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
G_OF = {t: g for g, ts in GROUPS.items() for t in ts}
G_OF[ANCHOR] = "terapia (ancla)"


def load(prop, tf):
    out = {}
    for f in sorted(glob.glob(f"{R}/b*_{prop}_{tf}_iot.csv")):
        df = pd.read_csv(f, index_col=0, parse_dates=True)
        if "isPartial" in df:
            df = df[df["isPartial"].astype(str) != "True"].drop(columns="isPartial")
        out[os.path.basename(f)[:3]] = df
    return out


rows = []
norm_series = {}
for prop in ["google", "youtube"]:
    for tf in ["5y", "12m"]:
        batches = load(prop, tf)
        for b, df in batches.items():
            a = df[ANCHOR].astype(float)
            asum = a.sum()
            for t in df.columns:
                if t == ANCHOR and b != "b00":
                    continue
                s = df[t].astype(float)
                idx = 100 * s.sum() / asum if asum > 0 else np.nan
                rec = {"fuente": prop, "periodo": tf, "termino": t, "grupo": G_OF.get(t, "?"), "lote": b,
                       "media_lote": round(s.mean(), 1), "indice_vs_psicologo": round(idx, 1),
                       "ancla_media_lote": round(a.mean(), 2)}
                if tf == "5y":
                    # weekly series; YoY: last 52 weeks vs previous 52
                    last = s.iloc[-52:].mean(); prev = s.iloc[-104:-52].mean(); first = s.iloc[:52].mean()
                    rec["cambio_anual_%"] = round(100 * (last - prev) / prev, 0) if prev > 0 else np.nan
                    rec["cambio_5a_%"] = round(100 * (last - first) / first, 0) if first > 0 else np.nan
                    # normalized series (anchor units)
                    norm_series[(prop, t)] = 100 * s / a.mean()
                if tf == "12m":
                    last = s.iloc[-13:].mean(); prev = s.iloc[:13].mean()
                    rec["cambio_12m_trim_%"] = round(100 * (last - prev) / prev, 0) if prev > 0 else np.nan
                rows.append(rec)
df = pd.DataFrame(rows)
df.to_csv(f"{D}/interes_normalizado_largo.csv", index=False)

# wide summary
def pick(prop, tf, col):
    x = df[(df.fuente == prop) & (df.periodo == tf)].set_index("termino")[col]
    return x[~x.index.duplicated()]

summ = pd.DataFrame({
    "grupo": df.drop_duplicates("termino").set_index("termino")["grupo"],
    "G_12m_idx": pick("google", "12m", "indice_vs_psicologo"),
    "G_5y_idx": pick("google", "5y", "indice_vs_psicologo"),
    "G_yoy_%": pick("google", "5y", "cambio_anual_%"),
    "G_5a_%": pick("google", "5y", "cambio_5a_%"),
    "YT_12m_idx": pick("youtube", "12m", "indice_vs_psicologo"),
    "YT_5y_idx": pick("youtube", "5y", "indice_vs_psicologo"),
    "YT_yoy_%": pick("youtube", "5y", "cambio_anual_%"),
    "YT_5a_%": pick("youtube", "5y", "cambio_5a_%"),
})
summ = summ.sort_values("G_12m_idx", ascending=False)
summ.to_csv(f"{D}/resumen_terminos.csv")
pd.set_option("display.width", 200); pd.set_option("display.max_rows", 100)
print(summ)

# Seasonality from Google 5y weekly
seas = {}
for (prop, t), s in norm_series.items():
    if prop != "google":
        continue
    s = s.copy()
    if s.mean() <= 0 or (s > 0).mean() < 0.8:
        continue
    yr = s.rolling(52, center=True, min_periods=26).mean()
    ratio = (s / yr).dropna()
    m = ratio.groupby(ratio.index.month).mean()
    seas[t] = (100 * m / m.mean()).round(0)
seas = pd.DataFrame(seas).T
seas.columns = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"]
seas["pico"] = seas.iloc[:, :12].idxmax(axis=1)
seas["valle"] = seas.iloc[:, :12].idxmin(axis=1)
seas["amplitud"] = seas.iloc[:, :12].max(axis=1) - seas.iloc[:, :12].min(axis=1)
seas.to_csv(f"{D}/estacionalidad_google.csv")
print(seas.sort_values("amplitud", ascending=False))

# Related queries consolidated
rel = []
for f in sorted(glob.glob(f"{R}/b*_*_12m_related.json")):
    prop = "google" if "_google_" in f else "youtube"
    js = json.load(open(f))
    for t, v in js.items():
        for kind in ["top", "rising"]:
            for x in v.get(kind, []) or []:
                rel.append({"fuente": prop, "termino": t, "tipo": "principal" if kind == "top" else "en_aumento",
                            "consulta": x["query"], "valor": x["value"]})
rel = pd.DataFrame(rel).drop_duplicates(["fuente", "termino", "tipo", "consulta"])
rel.to_csv(f"{D}/consultas_relacionadas.csv", index=False)
print(len(rel), "related rows")
