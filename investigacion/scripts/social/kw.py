import json,sys,re,glob,collections
K={
'identificado':r'identific|me describ|describi[oó]|soy yo|soy así|me proyect|me sent[ií] (descrit|identif)|mi tribu|no soy (el|la) [uú]nic|pens[eé] que era (el|la) [uú]nic|relat|called (us|me) out|this is me',
'voz/narrador':r'\bvoz\b|narrador|narraci|voice|narrat',
'IA':r'\bIA\b|\bAI\b|inteligencia artificial|chatgpt|generado|robot',
'dibujo/animación':r'animaci|dibuj|ilustrac|grafismo|animation|art style|personaje|mu[ñn]equit',
'música':r'm[uú]sica|music',
'terapia/psicólogo':r'terapia|psic[oó]log[oa]\b|terapeuta|therap|psiquiatr|psychiatr',
'Dios/fe':r'\bdios\b|jes[uú]s|cristo|\bgod\b|am[eé]n',
'crítica gen./superficial':r'superficial|gen[eé]rico|horoscop|hor[oó]scopo|barnum|pseudo|sin fuentes|fuente|estudio[s]? (dice|cient)|evidencia|clickbait|repetitiv|todos se sienten identificados|cualquiera',
'pide video/tema':r'(haz|hagan|podr[ií]as hacer|necesito) (un )?v[ií]deo|video (de|sobre)|please make|make a video|next video|parte 2|part 2',
'duración':r'duraci|muy largo|muy corto|demasiado largo|resum',
'infancia/padres':r'infancia|ni[ñn]ez|padres|madre|padre|childhood|parents',
'gracias':r'gracias|thank',
}
files=sys.argv[1:]
cnt=collections.Counter(); ex=collections.defaultdict(list); N=0; Nroot=0
for f in files:
    d=json.load(open(f))
    for c in d.get('comments') or []:
        N+=1; Nroot+= c.get('parent')=='root'
        t=c['text']
        for k,p in K.items():
            if re.search(p,t,re.I):
                cnt[k]+=1; ex[k].append((c.get('like_count') or 0, d['id'], t.replace('\n',' ')[:220]))
print("comments total",N,"top-level",Nroot)
for k,v in cnt.most_common(): print(f"{k}: {v}")
for k in sys.argv[0:0] or ['voz/narrador','IA','crítica gen./superficial','pide video/tema','dibujo/animación','duración','terapia/psicólogo']:
    print("\n==",k)
    for l,i,t in sorted(ex[k],reverse=True)[:14]: print(f"  [{l}] {i}: {t}")
