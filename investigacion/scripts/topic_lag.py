import csv, sys, os, re
D = sys.argv[1]
rows = list(csv.DictReader(open(os.path.join(D, "videos_all.csv"), encoding="utf-8")))
TOPICS = {
 "cumpleaños": (r"birthday", r"cumplea"),
 "no publican fotos": (r"post (their )?photos|don.t post", r"publican (sus )?fotos"),
 "quedarse en casa / solos en casa": (r"staying at home|stay(ing)? home", r"(en|quedarse en) casa"),
 "no ven deportes/fútbol": (r"sports|football", r"f[uú]tbol|deporte"),
 "arreglarlo todo / int. mecánica": (r"fix anything|mechanical", r"arreglar|mec[aá]nica"),
 "generación X / xennials / 70s-80s": (r"gen x|xennial|1970s|1980s|70s|80s", r"xennial|generaci[oó]n x|a[nñ]os 70|a[nñ]os 80|70s|80s"),
 "plantas": (r"plants", r"plantas"),
 "IQ alto": (r"high iq", r"(iq|ci) (alto|extremadamente)|alto (iq|ci)|bajo iq"),
 "resiliencia (mente fuerte)": (r"resilience", r"resiliencia"),
 "carisma": (r"charisma", r"carisma"),
 "autoestima/validación": (r"self.worth|self.esteem|validation", r"autoestima|validaci"),
 "tatuajes": (r"tattoo", r"tatuaj"),
 "abrazar almohada": (r"pillow", r"almohada"),
 "guardar objetos": (r"keep (things|stuff)|hoard|might need", r"guardan objetos|por si alg"),
 "cortar a todos": (r"cut (everyone|people) off", r"cortan a todos"),
 "vida simple": (r"simple life", r"vida simple"),
 "callados cuando les duele": (r"quiet when", r"callad|silencio cuando"),
 "piensan demasiado": (r"think too much|overthink", r"piensan demasiado|sobrepiens"),
 "lloran al enojarse": (r"cry when (they.re )?angry", r"lloran cuando se enfad|lloran cuando se enoj"),
 "disciplina": (r"discipline", r"disciplina"),
 "polímatas/multipotencial": (r"polymath|multiple interests", r"pol[ií]mat|muchos intereses"),
 "no les importa / not giving a f": (r"not giving a f|don.t care", r"no les importa|que no les importa"),
}
out=[]
print(f"{'topic':36s} {'EN first':10s} {'EN n':>4s} {'EN max':>9s} | {'ES first':10s} {'ES n':>4s} {'ES max':>9s}  ES best (channel)")
for t,(en,es) in TOPICS.items():
    E=[r for r in rows if r['lang']=='en' and r['format']=='long' and r['template'].startswith('psicologia_de') and re.search(en, r['title'].lower())]
    S=[r for r in rows if r['lang']=='es' and r['format']=='long' and r['template'].startswith('psicologia_de') and re.search(es, r['title'].lower())]
    def first(xs):
        ds=[r['approx_date'] for r in xs if r['approx_date']]; return min(ds) if ds else ''
    eb=max(E,key=lambda r:int(r['views'])) if E else None; sb=max(S,key=lambda r:int(r['views'])) if S else None
    print(f"{t:36s} {first(E):10s} {len(E):4d} {(eb['views'] if eb else 0):>9} | {first(S):10s} {len(S):4d} {(sb['views'] if sb else 0):>9}  {(sb['channel']+': '+sb['title'][:60]) if sb else ''}")
    for r in E+S: out.append({'topic':t,'lang':r['lang'],'channel':r['channel'],'approx_date':r['approx_date'],'views':r['views'],'outlier_score':r['outlier_score'],'title':r['title']})
with open(os.path.join(D,'topic_lag.csv'),'w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(sorted(out,key=lambda r:(r['topic'],r['approx_date'])))
