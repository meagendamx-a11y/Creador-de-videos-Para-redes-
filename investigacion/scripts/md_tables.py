import csv, sys, os
D = sys.argv[1]
rows = list(csv.DictReader(open(os.path.join(D, "outliers_coded.csv"), encoding="utf-8")))
def fmt_v(v):
    v = int(float(v)); return f"{v/1e6:.1f}M" if v >= 1e6 else f"{v/1e3:.0f}K"
def dur(s):
    try: s = int(float(s)); return f"{s//60}:{s%60:02d}"
    except: return ""
def date(r):
    d = r["upload_date_exact"]
    if d: return f"{d[:4]}-{d[4:6]}-{d[6:]}"
    a = r["approx_date"]
    if not a: return "s/f"
    return ("~" + a[:7]) if a >= "2025-12" else ("≥" + a[:4] if a.startswith("2025-11") else "~" + a[:4])
for lst, cols in (("es_long", True), ("en_long", True)):
    print(f"\n### {lst}\n")
    print("| # | Canal | Score (×mediana) | Score local | Vistas | Fecha | Dur. | Tema | Plantilla | Título |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    for r in rows:
        if r["list"] != lst: continue
        t = r["title"].replace("|", "/")
        print(f"| {r['rank']} | {r['channel']} | {float(r['outlier_score']):.0f} | {float(r['local_score'] or 0):.0f} | {fmt_v(r['views'])} | {date(r)} | {dur(r['duration_s'])} | {r['tema_manual']} | {r['plantilla_manual']} | [{t[:90]}]({r['url']}) |")
for lst in ("es_short", "en_short"):
    print(f"\n### {lst}\n")
    print("| # | Canal | Score | Vistas | Título |"); print("|---|---|---|---|---|")
    for r in rows:
        if r["list"] != lst: continue
        t = r["title"].replace("|", "/")
        print(f"| {r['rank']} | {r['channel']} | {float(r['outlier_score']):.0f} | {fmt_v(r['views'])} | [{t[:90]}]({r['url']}) |")
