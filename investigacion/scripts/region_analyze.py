import glob, os
import pandas as pd

D = "/tmp/claude-0/-home-user-Creador-de-videos-Para-redes-/f6e80049-54f1-5e5b-b0dd-1d5ea884d7d2/scratchpad/research/trends"
cols = {}
for f in sorted(glob.glob(f"{D}/raw_extra/region_*.csv")):
    t = os.path.basename(f)[7:-4].replace("_", " ")
    s = pd.read_csv(f, index_col=0).iloc[:, 0]
    cols[t] = s
df = pd.DataFrame(cols)
df.to_csv(f"{D}/estados_interes_por_termino.csv")
pd.set_option("display.width", 250); pd.set_option("display.max_columns", 30)
print(df.sort_values(df.columns[0], ascending=False))
print()
for t in df.columns:
    s = df[t].sort_values(ascending=False)
    print(f"{t:18} TOP5: {', '.join(f'{i} {v}' for i, v in s.head(5).items())} | BOTTOM3: {', '.join(f'{i} {v}' for i, v in s.tail(3).items())}")
# relative over-index: each term vs mean across terms per state (z within state)
rel = df.div(df.mean(axis=1), axis=0)
rel = rel.div(rel.mean(axis=0), axis=1)
rel.round(2).to_csv(f"{D}/estados_sobreindice.csv")
print()
for st in rel.index:
    r = rel.loc[st].sort_values(ascending=False)
    print(f"{st:22} sobre-índice: {', '.join(f'{i} {v:.2f}' for i, v in r.head(3).items())}")
