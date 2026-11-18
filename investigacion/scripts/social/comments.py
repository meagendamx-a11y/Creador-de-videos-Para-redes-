import json,re,pandas as pd,numpy as np
pd.set_option('display.width',250); pd.set_option('display.max_colwidth',160)
D='/tmp/claude-0/-home-user-Creador-de-videos-Para-redes-/f6e80049-54f1-5e5b-b0dd-1d5ea884d7d2/scratchpad/research/apify/'
tg=pd.read_csv(D+'tt_comment_targets.csv',dtype={'id':str}).set_index('id')
rows=[]
for x in json.load(open(D+'tt_comments.json')):
    vid=x['submittedVideoUrl'].rstrip('/').split('/')[-1]
    rows.append(dict(plat='TikTok',post=vid,author=tg.loc[vid,'author'],grupo=tg.loc[vid,'grupo'],text=str(x.get('text') or ''),likes=x.get('diggCount') or 0,has_mention=bool(x.get('mentions'))))
ig=pd.read_csv(D+'instagram_posts.csv')
seen=set()
for x in json.load(open(D+'ig_comments.json')):
    seen.add(x['id']); acct=ig[ig.url==x['postUrl']].acct.iloc[0]
    rows.append(dict(plat='Instagram',post=x['postUrl'],author=acct,grupo='destacado (scraper)',text=str(x.get('text') or ''),likes=x.get('likesCount') or 0,has_mention='@' in (x.get('text') or '')))
for p in json.load(open(D+'ig_posts.json')):
    acct=p['inputUrl'].rstrip('/').split('/')[-1]
    for c in p.get('latestComments') or []:
        if c.get('id') in seen: continue
        seen.add(c.get('id'))
        rows.append(dict(plat='Instagram',post=p.get('url'),author=acct,grupo='últimos comentarios (gratis)',text=str(c.get('text') or ''),likes=c.get('likesCount') or 0,has_mention='@' in (c.get('text') or '')))
df=pd.DataFrame(rows)
C={
'identificación/validación':r'\bme pasa|me pas[oó]|soy yo|literal(mente)? yo|\byo\b.*(tal cual|exacto)|me identifico|identificad|así me siento|asi me siento|tal cual|exacto|justo lo que|lo necesitaba|necesitaba (leer|escuchar|ver)|qu[eé] cierto|muy cierto|es verdad|totalmente|me lleg[oó]|me describe|me vi |me vi$|me sent[ií] identific|así soy|asi soy|me representa|yo cuando|same|this is me|\bfacts\b|needed this|\ba m[ií] (tambi[eé]n |me )?(pas|suced|ocurr)|yo tambi[eé]n|me too|^yo\b|\byo (soy|hago|siempre|igual|me|lo)\b|as[ií] es|tal cu[aá]l|me sucede|me ocurre|igualit|en mi caso|mi caso|siempre (duermo|lloro|hago)|el m[ií]o|la m[ií]a|mi (novi[oa]|pareja|esposo|esposa|ex|mam[aá]|pap[aá]) (me|es|siempre|hace|dice)|relatable|so true|it does get better',
'confesión de malestar':r'tengo ansiedad|mi ansiedad|con ansiedad|ataque|depresi[oó]n|deprimid|me siento (mal|sol|vac|triste|perdid|agotad|cansad)|estoy (mal|sol|triste|cansad|agotad|perdid)|llor(o|ando|é|e)\b|no puedo (m[aá]s|respirar|salir)|me duele|sufr|me lastim|me quiero morir|ganas de morir|autolesi|trauma|abandon|insomnio|no duermo|crisis|p[aá]nico',
'pedido de ayuda':r'\bayuda(me)?\b|ay[uú]denme|ay[uú]dame|alludame|qu[eé] (hago|puedo hacer|debo hacer)|c[oó]mo (hago|le hago|puedo|se supera|salgo|dejo|se quita|se resuelve|se puede evitar)|alg[uú]n consejo|un consejo\?|necesito hablar|necesito (a )?alguien|cu[aá]l es el bot[oó]n|qu[eé] hacer cuando',
'petición de tema/contenido':r'podr[ií]as (hablar|hacer)|puedes hablar|hablen? (de|sobre).*\?|haz(me)? (un )?video|has (un )?video|m[aá]s videos|parte \d|part \d|segunda parte|cu[aá]l es el (libro|nombre)|nombre del (libro|cuento|video|canci)|qu[eé] libro|c[oó]mo se llama (el|la) (libro|cuento|serie|pel|canci)|cu[aá]l es (la|el) (serie|pel[ií]cula|cuento|canci)',
'terapia/psicólogo (mención)':r'terapia|terapeut|psic[oó]log|psiquiatr|sesi[oó]n|consulta|tratamiento|medicamento|pastilla|antidepresiv|therapy|therapist|consultorio|tu contacto|agendar|agenda|tu n[uú]mero|whats',
'crítica/escepticismo':r'\bia\b|\bi\.a\b|inteligencia artificial|chat ?gpt|generad[oa] con|hecho con ia|\bai\b|falso|mentira|no es as[ií]|desinforma|eso no es|fuente|estudio(s)? (dice|demuestr)|no todo es|ahora todo es|todo es (trauma|ansiedad|t[oó]xico)|romantiz|autodiagn|pseudo|charlat|no eres psic|no es psic|vend(e|iendo)|publicidad|spam|estafa|clickbait|no estoy de acuerdo|discrepo|no aplica|generaliz',
'elogio/agradecimiento':r'gracias|thank|hermos|bonit|excelente|me encant|\bamo\b|i love|incre[ií]ble|genial|muy bien|buen(a|ísim[oa])? (video|contenido|explicaci|consejo|dato|informaci)|qu[eé] buen|bendici|aplaus|👏|❤|🥰|😍|🤍|💕|🙏',
'religión/espiritualidad':r'\bdios\b|biblia|\bor(emos|ar|en)\b|\bjes[uú]s\b|\bfe\b|\bgod\b|\bseñor\b|\bam[eé]n\b|bendig',
'respuesta a CTA (palabra clave)':r'^\W*(grupo|care kit|info|informaci[oó]n|elijo|ego|mente)\W*$|^\W*(grupo|care kit)\b',
'solicitud de servicio (precio/info/cita)':r'precio|cu[aá]nto cobra|cu[aá]nto cuesta|informaci[oó]n|\binfo\b|en l[ií]nea\s*\?|d[oó]nde atiende|atiendes|haces en l|consulta(s)? (en|online)|tu contacto|agendar|cita',
'pregunta/debate sobre el tema':r'\?\s*$|^\W*y si\b|^\W*pero\b|no estoy de acuerdo|depende|para m[ií] ',
'humor/comunidad/etiquetar':r'jaj|jej|xd\b|😂|🤣|😹|lol\b|@|mira esto|te etiqueto|para ti|etiqueta|mi (novi[oa]|pareja|esposo|esposa|mam[aá]|amig[oa]|hij[oa])'}
for k,v in C.items(): df[k]=df.text.str.contains(v,case=False,regex=True)|((k=='humor/comunidad/etiquetar')&df.has_mention)
T={'costo':r'caro|car[ií]sim|dinero|pagar|cobr|precio|gratis|econ[oó]mic|no me alcanza|lujo|privilegio|\$|pesos|accesible',
'miedo/estigma':r'miedo (a|de) (ir|la terapia|al psic)|verg[uü]enza|loc[oa]s?\b|estigma|no me atrevo|me da pena',
'experiencia propia en terapia':r'mi (psic[oó]log|terapeut|psiquiatr)|en (mi )?terapia|fui (a|al) (terapia|psic)|voy (a|al) (terapia|psic)|llevo .* terapia|estoy en terapia|mi sesi[oó]n',
'busca/necesita terapia':r'necesito (terapia|un psic|una psic|ir)|quiero (ir a terapia|un psic|una psic)|d[oó]nde (encuentro|busco)|recomiend.*psic|atiende|consulta.*(precio|costo|cu[aá]nto)|cu[aá]nto cuesta|citas?\b'}
for k,v in T.items(): df['T_'+k]=df['terapia/psicólogo (mención)']&df.text.str.contains(v,case=False,regex=True)
cat=list(C)
df['sin_codigo']=~df[cat].any(axis=1)
df['emoji_o_corto']=df.text.str.replace(r'[\W_]+','',regex=True).str.len()<4
df.to_csv(D+'comentarios_codificados.csv',index=False,columns=[c for c in df.columns if c!='has_mention'])
def tab(sub,name):
    r={k:(sub[k].mean()*100) for k in cat+['sin_codigo','emoji_o_corto']}; r['n']=len(sub); r['grupo']=name; return r
out=[tab(df[df.plat=='TikTok'],'TikTok total'),tab(df[(df.plat=='TikTok')&(df.grupo=='alto')],'TikTok alto rend.'),tab(df[(df.plat=='TikTok')&(df.grupo=='bajo')],'TikTok bajo rend.'),
     tab(df[df.plat=='Instagram'],'Instagram total'),tab(df[(df.plat=='Instagram')&(df.grupo=='destacado (scraper)')],'IG posts destacados'),tab(df[(df.plat=='Instagram')&(df.grupo!='destacado (scraper)')],'IG últimos com.')]
R=pd.DataFrame(out).set_index('grupo'); print(R.round(1).T.to_string())
print('\nCounts TikTok:'); print(df[df.plat=='TikTok'][cat].sum())
print('\nCounts IG:'); print(df[df.plat=='Instagram'][cat].sum())
th=df[df['terapia/psicólogo (mención)']]
print('\nTerapia subcodes:'); print(th.groupby('plat')[[c for c in df if c.startswith('T_')]].sum(), th.groupby('plat').size())
# by video
print(df[df.plat=='TikTok'].groupby('author')[cat].mean().mul(100).round(0).to_string())
R.round(1).to_csv(D+'comentarios_resumen_pct.csv')
