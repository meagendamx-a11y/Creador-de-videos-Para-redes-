#!/usr/bin/env python3
"""Aggregate tables: theme/template lift, duration, trends, new-channel growth, cross-language topic lag."""
import csv, sys, os, statistics, collections, re, json
D = sys.argv[1]
OUT = open(os.path.join(D, "aggregates.txt"), "w", encoding="utf-8")
def p(*a):
    print(*a); print(*a, file=OUT)
GENERAL = {"TeLoPinto", "CuriosaMente"}
rows = [r for r in csv.DictReader(open(os.path.join(D, "videos_all.csv"), encoding="utf-8"))]
for r in rows:
    r["views"] = int(r["views"]); r["os"] = float(r["outlier_score"] or 0)
    r["ls"] = float(r["local_score"] or 0); r["age"] = int(r["age_days"]) if r["age_days"] else None
    r["dur"] = float(r["duration_s"]) if r["duration_s"] not in ("", "None") else None
rows = [r for r in rows if not (r["channel"] in GENERAL and r["theme_primary"] == "otro") and int(r["channel_n"]) >= 15]
json_out = {}

def lift_table(sel, key, label, thr_q=0.9, min_n=15):
    """lift = share of key among top-decile (by local score) / share among all."""
    if not sel: return
    scores = sorted(r["ls"] for r in sel)
    thr = scores[int(thr_q * (len(scores) - 1))]
    top = [r for r in sel if r["ls"] >= thr]
    c_all = collections.Counter(); c_top = collections.Counter(); meds = collections.defaultdict(list)
    for r in sel:
        ks = r[key].split("|") if key == "themes_all" else [r[key]]
        for k in ks or ["otro"]:
            if not k: k = "otro"
            c_all[k] += 1; meds[k].append(r["ls"])
            if r["ls"] >= thr: c_top[k] += 1
    p(f"\n== {label}: n={len(sel)} top-decile n={len(top)} (local_score >= {thr:.2f})")
    p(f"{'cat':28s} {'n':>5s} {'share':>6s} {'topshr':>6s} {'lift':>5s} {'med_ls':>6s} {'p90_ls':>6s}")
    res = []
    for k, n in c_all.most_common():
        if n < min_n: continue
        sh = n / len(sel); tsh = c_top[k] / len(top)
        m = sorted(meds[k]); res.append((k, n, sh, tsh, tsh / sh if sh else 0, statistics.median(m), m[int(0.9 * (len(m) - 1))]))
    for k, n, sh, tsh, lf, md, p9 in sorted(res, key=lambda x: -x[4]):
        p(f"{k:28s} {n:5d} {sh:6.1%} {tsh:6.1%} {lf:5.2f} {md:6.2f} {p9:6.2f}")
    json_out[label] = res

for lang in ("es", "en"):
    for fmt in ("long",):
        sel = [r for r in rows if r["lang"] == lang and r["format"] == fmt]
        lift_table(sel, "theme_primary", f"THEME primary {lang} {fmt}")
        lift_table(sel, "themes_all", f"THEME any-tag {lang} {fmt}")
        lift_table(sel, "template", f"TEMPLATE {lang} {fmt}")
        # recent only (last ~12 months) to reflect current algorithm/audience
        rec = [r for r in sel if r["age"] is not None and 14 <= r["age"] <= 380]
        lift_table(rec, "theme_primary", f"THEME primary {lang} {fmt} ULTIMOS 12M", min_n=10)
        lift_table(rec, "template", f"TEMPLATE {lang} {fmt} ULTIMOS 12M", min_n=10)
    sel = [r for r in rows if r["lang"] == lang and r["format"] == "short"]
    lift_table(sel, "theme_primary", f"THEME primary {lang} short", min_n=10)
    lift_table(sel, "template", f"TEMPLATE {lang} short", min_n=10)

# title flags
p("\n== TITLE FLAGS (es long, last 12M): median local score with vs without")
for lang in ("es", "en"):
    sel = [r for r in rows if r["lang"] == lang and r["format"] == "long" and r["age"] is not None and 14 <= r["age"] <= 380]
    for fl in ("caps_emphasis", "all_caps_title", "question", "parenthetical", "number", "second_person", "emoji"):
        a = [r["ls"] for r in sel if r[fl] == "1"]; b = [r["ls"] for r in sel if r[fl] == "0"]
        if len(a) >= 10 and len(b) >= 10:
            p(f"{lang} {fl:16s} with n={len(a):4d} med={statistics.median(a):.2f} | without n={len(b):4d} med={statistics.median(b):.2f}")

# duration
p("\n== DURATION buckets (long, last 12M): median local score / median views")
def dbucket(s):
    if s is None: return "NA"
    m = s / 60
    for lim, lab in ((3, "<3m"), (5, "3-5m"), (8, "5-8m"), (12, "8-12m"), (20, "12-20m"), (40, "20-40m")):
        if m < lim: return lab
    return "40m+"
for lang in ("es", "en"):
    sel = [r for r in rows if r["lang"] == lang and r["format"] == "long" and r["age"] is not None and 14 <= r["age"] <= 380]
    g = collections.defaultdict(list)
    for r in sel: g[dbucket(r["dur"])].append(r)
    for lab in ("<3m", "3-5m", "5-8m", "8-12m", "12-20m", "20-40m", "40m+"):
        if g[lab]:
            p(f"{lang} {lab:7s} n={len(g[lab]):4d} med_ls={statistics.median([x['ls'] for x in g[lab]]):.2f} med_os={statistics.median([x['os'] for x in g[lab]]):.2f} share_top10x={sum(1 for x in g[lab] if x['os']>=10)/len(g[lab]):.1%}")

# trends by period
def period(age):
    if age is None: return None
    if age < 183: return "P0_0-6m"
    if age < 365: return "P1_6-12m"
    if age < 730: return "P2_12-24m"
    if age < 1095: return "P3_24-36m"
    return "P4_36m+"
p("\n== TRENDS es long: upload share and median local score by theme and period")
for lang in ("es", "en"):
    sel = [r for r in rows if r["lang"] == lang and r["format"] == "long" and r["age"] is not None and r["age"] >= 14]
    per = collections.defaultdict(list)
    for r in sel: per[period(r["age"])].append(r)
    pers = sorted(per)
    themes = sorted({r["theme_primary"] for r in sel})
    p(f"\n-- {lang}: n per period " + " ".join(f"{k}={len(per[k])}" for k in pers))
    p(f"{'theme':26s} " + " ".join(f"{k[:9]:>17s}" for k in pers))
    for t in themes:
        cells = []
        for k in pers:
            xs = [r for r in per[k] if r["theme_primary"] == t]
            cells.append(f"{len(xs)/max(1,len(per[k])):5.1%} ls{(statistics.median([x['ls'] for x in xs]) if len(xs)>=5 else float('nan')):5.2f}")
        p(f"{t:26s} " + " ".join(f"{c:>17s}" for c in cells))
    p(f"{'TEMPLATE':26s}")
    for t in sorted({r["template"] for r in sel}):
        cells = []
        for k in pers:
            xs = [r for r in per[k] if r["template"] == t]
            cells.append(f"{len(xs)/max(1,len(per[k])):5.1%} ls{(statistics.median([x['ls'] for x in xs]) if len(xs)>=5 else float('nan')):5.2f}")
        p(f"{t:26s} " + " ".join(f"{c:>17s}" for c in cells))

# supply of the "psicologia de las personas que" template across ALL es channels by month (last 18m)
p("\n== SUPPLY/DEMAND of 'psicologia_de_personas_que' template by approx month (es long, all channels)")
for lang in ("es", "en"):
    sel = [r for r in rows if r["lang"] == lang and r["format"] == "long" and r["approx_date"] >= "2025-05"]
    g = collections.defaultdict(list)
    for r in sel: g[r["approx_date"][:7]].append(r)
    for m in sorted(g):
        xs = [r for r in g[m] if r["template"] == "psicologia_de_personas_que"]
        p(f"{lang} {m} uploads={len(g[m]):4d} PDP_que={len(xs):3d} ({len(xs)/len(g[m]):.0%}) med_views_PDP={statistics.median([x['views'] for x in xs]) if xs else 0:>9} med_views_other={statistics.median([x['views'] for x in g[m] if x['template']!='psicologia_de_personas_que'] or [0]):>9}")

# new channel growth
p("\n== NEW CHANNELS growth (videos tab): views of videos uploaded per approx month, cumulative")
for ch in ("LaPsicologiaInvisible", "LaMenteOculta", "PsicologiaClara", "PsicologiaSinFiltro", "LoDescomun", "IdealMente",
           "MenteConsciente", "ClaridadMental", "ManualDeVida", "PsicologiaCotidiana", "DatoVisual", "PsicologiaOscura",
           "ReversHub", "PsychologySimplified", "PsychToons", "PsychologyInsight", "ApexPsychology"):
    xs = [r for r in rows if r["channel"] == ch and r["format"] == "long" and r["approx_date"]]
    if not xs: continue
    g = collections.defaultdict(lambda: [0, 0, 0])
    for r in xs:
        m = r["approx_date"][:7]; g[m][0] += 1; g[m][1] += r["views"]; g[m][2] = max(g[m][2], r["views"])
    p(f"\n{ch}: total_videos={len(xs)} total_views={sum(r['views'] for r in xs):,} first={min(g)}")
    for m in sorted(g):
        p(f"   {m} uploads={g[m][0]:3d} views={g[m][1]:>11,} max={g[m][2]:>10,}")

json.dump({k: v for k, v in json_out.items()}, open(os.path.join(D, "lift_tables.json"), "w"), ensure_ascii=False, indent=1)
