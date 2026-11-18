import json,pandas as pd,numpy as np
pd.set_option('display.width',250); pd.set_option('display.max_colwidth',70)
D='/tmp/claude-0/-home-user-Creador-de-videos-Para-redes-/f6e80049-54f1-5e5b-b0dd-1d5ea884d7d2/scratchpad/research/apify/'
det={x['username']:x for x in json.load(open(D+'ig_details.json'))+json.load(open(D+'ig_details_test.json')) if x.get('username')}
rows=[]
for p in json.load(open(D+'ig_posts.json')):
    acct=p['inputUrl'].rstrip('/').split('/')[-1]
    t={'clips':'Reel','carousel_container':'Carrusel','feed':'Imagen'}.get(p.get('productType'),p.get('type'))
    rows.append(dict(acct=acct,owner=p.get('ownerUsername'),collab=p.get('ownerUsername')!=acct,tipo=t,date=p['timestamp'],likes=p.get('likesCount'),comments=p.get('commentsCount'),
        plays=p.get('videoPlayCount'),views=p.get('videoViewCount'),dur=p.get('videoDuration'),n_slides=len(p.get('childPosts') or []) or len(p.get('images') or []),pinned=p.get('isPinned'),paid=p.get('paidPartnership'),
        url=p.get('url'),shortcode=p.get('shortCode'),caption=(p.get('caption') or '').replace('\n',' ')[:300],n_latest=len(p.get('latestComments') or [])))
df=pd.DataFrame(rows); df['date']=pd.to_datetime(df.date); df['age']=(pd.Timestamp('2026-11-18',tz='UTC')-df.date).dt.days
df['followers']=df.acct.map(lambda a: det.get(a,{}).get('followersCount'))
df.loc[df.likes<0,'likes']=np.nan
df['eng']=(df.likes.fillna(0)+df.comments)/df.followers
med=df[~df.pinned.fillna(False)].groupby('acct').likes.median(); df['out_likes']=df.likes/df.acct.map(med)
df.to_csv(D+'instagram_posts.csv',index=False)
print(df.groupby('acct').agg(followers=('followers','first'),n=('url','size'),reels=('tipo',lambda s:(s=='Reel').sum()),carr=('tipo',lambda s:(s=='Carrusel').sum()),img=('tipo',lambda s:(s=='Imagen').sum()),med_likes=('likes','median'),med_com=('comments','median'),med_plays=('plays','median'),desde=('date','min')).sort_values('followers',ascending=False).to_string())
g=df[~df.pinned.fillna(False)]
print('\nPor tipo (todas cuentas, sin fijados):'); print(g.groupby('tipo').agg(n=('url','size'),med_likes=('likes','median'),med_com=('comments','median'),med_out=('out_likes','median'),med_eng=('eng','median'),med_plays=('plays','median')).round(4))
print('\nPor cuenta x tipo (mediana likes / out):'); print(g.pivot_table(index='acct',columns='tipo',values='out_likes',aggfunc='median').round(2))
print(g.pivot_table(index='acct',columns='tipo',values='comments',aggfunc='median').round(1))
r=g[g.tipo=='Reel']; print('\nReels: plays/followers median', (r.plays/r.followers).median(), ' likes/plays', (r.likes/r.plays).median(), ' com/plays', (r.comments/r.plays).median(), 'dur med', r.dur.median())
print(r.assign(dbin=pd.cut(r.dur,[0,15,30,60,90,600])).groupby('dbin',observed=True).agg(n=('url','size'),out=('out_likes','median'),pf=('plays',lambda s: np.nan)).round(2))
print('\nTOP 20 por out_likes'); print(g.sort_values('out_likes',ascending=False).head(20)[['acct','tipo','likes','comments','plays','out_likes','n_slides','caption']].to_string())
print('\nBOTTOM 12'); print(g[g.age>=5].sort_values('out_likes').head(12)[['acct','tipo','likes','comments','plays','out_likes','caption']].to_string())
print('\nTOP comentarios'); print(g.sort_values('comments',ascending=False).head(20)[['acct','tipo','likes','comments','url','caption']].to_string())
print('free latest comments total', df.n_latest.sum())
