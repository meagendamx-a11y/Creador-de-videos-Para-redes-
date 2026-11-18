import json,re,pandas as pd,numpy as np
D='/tmp/claude-0/-home-user-Creador-de-videos-Para-redes-/f6e80049-54f1-5e5b-b0dd-1d5ea884d7d2/scratchpad/research/apify/'
NOW=pd.Timestamp('2026-11-18',tz='UTC')
rows=[]
for f,src in [('tt_test.json','hashtag'),('tt_hashtags.json','hashtag'),('tt_search.json','search'),('tt_profiles.json','profile')]:
    for x in json.load(open(D+f)):
        a=x['authorMeta']; t=x.get('text') or ''
        sh=x.get('searchHashtag'); sh=sh.get('name') if isinstance(sh,dict) else sh
        rows.append(dict(id=x['id'],src=src,query=sh or (x.get('input') if isinstance(x.get('input'),str) else ''),author=a['name'],nick=a.get('nickName'),fans=a.get('fans'),
            lang=x.get('textLanguage'),date=x['createTimeISO'],views=x.get('playCount') or 0,likes=x.get('diggCount') or 0,comments=x.get('commentCount') or 0,
            shares=x.get('shareCount') or 0,saves=x.get('collectCount') or 0,duration=(x.get('videoMeta') or {}).get('duration'),
            slideshow=bool(x.get('isSlideshow')),pinned=bool(x.get('isPinned')),sponsored=bool(x.get('isSponsored')),
            hashtags=' '.join('#'+h.get('name','') for h in (x.get('hashtags') or []) if h.get('name')),
            music_original=(x.get('musicMeta') or {}).get('musicOriginal'),cover=(x.get('videoMeta') or {}).get('coverUrl'),url=x.get('webVideoUrl'),text=t))
df=pd.DataFrame(rows)
df['date']=pd.to_datetime(df['date'])
df['age_days']=(NOW-df['date']).dt.days
df['save_rate']=df.saves/df.views.replace(0,np.nan)
df['share_rate']=df.shares/df.views.replace(0,np.nan)
df['like_rate']=df.likes/df.views.replace(0,np.nan)
df['comment_rate']=df.comments/df.views.replace(0,np.nan)
df['series']=df.text.str.contains(r'parte\s*\d|part\s*\d|pt\.?\s*\d|\d\s*/\s*\d|cap[ií]tulo|episodio',case=False,regex=True)
df['hook']=df.text.str.split('\n').str[0].str.replace(r'#\S+','',regex=True).str.strip().str[:120]
df['question_hook']=df.hook.str.contains(r'\?|¿')
df['list_hook']=df.hook.str.contains(r'^\s*\d+\s|\b\d+\s+(señales|cosas|formas|tips|razones|hábitos|frases|maneras|errores|técnicas)',case=False,regex=True)
df['you_hook']=df.hook.str.contains(r'\b(tú|tu|te|eres|estás|sientes|sabes|tienes)\b',case=False,regex=True)
# format classification
animated={'lapsicologiainvisible':'animación/ilustración','teayudo_aayudarte':'animación/ilustración','itslennnie':'personaje animado (ref. EN)','psicologiacruda_':'faceless (texto/stock)','influencia.mental':'faceless (texto/stock)'}
df['formato_cuenta']=df.author.map(animated).fillna('persona a cámara')
anim_re=r'animaci|animad|animation|#animac|ilustraci|dibuj|alightmotion|#art\b|cartoon|caricatura'
df.loc[(df.src!='profile')&df.text.str.contains(anim_re,case=False,regex=True),'formato_cuenta']='animación/ilustración'
df.loc[(df.src!='profile')&(df.formato_cuenta=='persona a cámara'),'formato_cuenta']='sin clasificar (hashtag)'
df=df.drop_duplicates('id')
df.to_csv(D+'tiktok_videos.csv',index=False)
print(len(df)); print(df.groupby('src').size())
