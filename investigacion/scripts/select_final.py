import csv, sys, os
D = sys.argv[1]
GENERAL = {"TeLoPinto", "CuriosaMente"}
rows = list(csv.DictReader(open(os.path.join(D, "videos_all.csv"), encoding="utf-8")))
def ok(r, minv):
    if r["channel"] in GENERAL and (r["theme_primary"] == "otro" or r["format"] == "short"): return False
    if r["channel"] == "MentesExpertas" and r["format"] == "long": return False  # clips channel, off-topic long uploads
    if int(r["channel_n"]) < 20: return False
    if r["age_days"] and int(r["age_days"]) < 14: return False
    return int(r["views"]) >= minv
out = []
for lang, fmt, k, minv in (("es","long",50,100000),("en","long",30,500000),("es","short",25,100000),("en","short",15,500000)):
    sel = [r for r in rows if r["lang"]==lang and r["format"]==fmt and ok(r, minv)]
    sel.sort(key=lambda r: -float(r["outlier_score"]))
    for i, r in enumerate(sel[:k]):
        r = dict(r); r["list"] = f"{lang}_{fmt}"; r["rank"] = i+1; out.append(r)
with open(os.path.join(D, "final_outliers.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)
for r in out:
    print(r["list"], r["rank"], r["channel"][:14], r["outlier_score"], r["local_score"], r["views"], r["approx_date"], r["duration_s"], r["title"][:85])
