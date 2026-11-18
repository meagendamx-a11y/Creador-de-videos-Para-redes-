import pandas as pd,numpy as np,re
pd.set_option('display.width',250)
D='/tmp/claude-0/-home-user-Creador-de-videos-Para-redes-/f6e80049-54f1-5e5b-b0dd-1d5ea884d7d2/scratchpad/research/apify/'
T={'pareja/relaciones':r'pareja|relaci[oó]n|novi[oa]|amor|ex\b|apego|infidel|celos|discusi|ruptura|dependencia emocional|s3xual|sexual|matrimonio|couple|relationship',
 'ansiedad/estrés':r'ansiedad|ansios|estr[eé]s|p[aá]nico|anxiety|nervios|sobrepens|overthink|rumia|preocupa',
 'autoestima/autocuidado':r'autoestima|amor propio|suficiente|validaci|confianza en ti|self|autocuidado|valórate|compañía',
 'depresión/tristeza':r'depresi|triste|vac[ií]o|llorar|lloran|soledad|solo\b|sola\b|sad\b',
 'trauma/infancia/familia':r'trauma|infancia|niñ|hij[oa]s|padres|madre|padre|familia|crianza|adolescen|childhood|inner ?child',
 'TLP/diagnósticos':r'\btlp\b|bipolar|tdah|toc\b|ocd|autis|narcis|trastorno|diagn',
 'manipulación/psicología oscura':r'manipul|influir|persuas|oscura|control|narcis|gaslight|t[eé]cnica psicol',
 '"psicología de las personas que…"':r'psicolog[ií]a de (las|los|la)',
 'terapia/sesión/psicólogo':r'terapia|sesi[oó]n|psic[oó]log[oa]s? (te|me)|consulta|terapeuta|taller|atenci[oó]n psicol',
 'motivación/frases':r'motivaci|frase|reflexi|i love you|things get better|tag someone|prioridad',
 'cuentos/películas/cultura':r'cuento|pel[ií]cula|escena|libro|serie|lectura|canci[oó]n|podcast',
 'sueño/cuerpo/hábitos':r'dormir|sueño|almohada|h[aá]bito|cerebro|brain|cuerpo|perros'}
def tag(t):
    t=str(t).lower(); return [k for k,v in T.items() if re.search(v,t)] or ['otro']
for f in ['tiktok_profile_videos_scored.csv','tiktok_videos.csv']:
    df=pd.read_csv(D+f); df['topics']=df.text.apply(tag)
    e=df.explode('topics')
    if 'outlier' in df:
        e=e[e.mature]
        r=e.groupby('topics').agg(n=('id','size'),med_outlier=('outlier','median'),mean_log_out=('outlier',lambda s: np.exp(np.log(s.clip(lower=1e-3)).mean())),save=('save_rate','median'),share=('share_rate','median'),comm=('comment_rate','median')).sort_values('med_outlier',ascending=False)
        print('PERFILES (videos >=7 días):'); print(r.round(4))
        df.to_csv(D+f,index=False)
    else:
        e=e[(e.src!='profile')&(e.lang=='es')]
        r=e.groupby('topics').agg(n=('id','size'),med_views=('views','median'),save=('save_rate','median'),share=('share_rate','median'),comm=('comment_rate','median')).sort_values('med_views',ascending=False)
        print('HASHTAG+BÚSQUEDA (es):'); print(r.round(4))
        h=df[(df.src!='profile')&(df.lang=='es')]
        print('hashtag es: n',len(h),'mediana vistas',h.views.median(),'dur med',h.duration.median(),'save',h.save_rate.median(),'share',h.share_rate.median())
        h=h.assign(dbin=pd.cut(h.duration,[-1,15,30,60,90,180,2000]))
        print(h.groupby('dbin',observed=True).agg(n=('id','size'),med_views=('views','median'),save=('save_rate','median')).round(4))
        print(h.groupby('slideshow').agg(n=('id','size'),med_views=('views','median'),save=('save_rate','median'),share=('share_rate','median')).round(4))
        print('autores psic en hashtags: ', h.text.str.contains('psic',case=False).mean())
        df.to_csv(D+f,index=False)
