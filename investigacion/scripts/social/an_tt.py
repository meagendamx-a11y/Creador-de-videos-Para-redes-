import pandas as pd,numpy as np
pd.set_option('display.width',250); pd.set_option('display.max_colwidth',90); pd.set_option('display.max_rows',200)
D='/tmp/claude-0/-home-user-Creador-de-videos-Para-redes-/f6e80049-54f1-5e5b-b0dd-1d5ea884d7d2/scratchpad/research/apify/'
df=pd.read_csv(D+'tiktok_videos.csv')
p=df[df.src=='profile'].copy()
p['mature']=p.age_days>=7
med=p[p.mature].groupby('author').views.median()
p['acct_median']=p.author.map(med)
p['outlier']=p.views/p.acct_median
acc=p.groupby('author').agg(fans=('fans','first'),formato=('formato_cuenta','first'),n=('id','size'),mediana_vistas=('views','median'),max_vistas=('views','max'),
  save_rate=('save_rate','median'),share_rate=('share_rate','median'),comment_rate=('comment_rate','median'),dur_med=('duration','median'),
  slides=('slideshow','sum'),primera=('date','min'),ultima=('date','max'))
acc['views_per_fan']=acc.mediana_vistas/acc.fans
acc['dias_cubiertos']=(pd.to_datetime(acc.ultima)-pd.to_datetime(acc.primera)).dt.days
print(acc.sort_values('mediana_vistas',ascending=False).round(4).to_string())
p.to_csv(D+'tiktok_profile_videos_scored.csv',index=False)
print('\nFORMATO (perfil):'); print(p.groupby('formato_cuenta').agg(n=('id','size'),med_views=('views','median'),med_outlier=('outlier','median'),save=('save_rate','median'),share=('share_rate','median'),comm=('comment_rate','median'),dur=('duration','median')).round(4))
m=p[p.mature]
top=m.sort_values('outlier',ascending=False).head(30); bot=m.sort_values('outlier').head(30)
cols=['author','outlier','views','save_rate','share_rate','comment_rate','duration','slideshow','series','age_days','hook']
print('\nTOP30'); print(top[cols].round(4).to_string())
print('\nBOTTOM30'); print(bot[cols].round(4).to_string())
def summ(x,n):
    return dict(grupo=n,n=len(x),med_dur=x.duration.median(),pct_slideshow=x.slideshow.mean(),pct_series=x.series.mean(),pct_pregunta=x.question_hook.mean(),pct_lista=x.list_hook.mean(),pct_tu=x.you_hook.mean(),save=x.save_rate.median(),share=x.share_rate.median(),comm=x.comment_rate.median(),like=x.like_rate.median(),hook_len=x.hook.fillna('').str.len().median())
print(pd.DataFrame([summ(top,'top30'),summ(bot,'bottom30'),summ(m,'todos')]).round(4).to_string())
# duration buckets
m=m.assign(dbin=pd.cut(m.duration,[0,15,30,45,60,90,180,2000]))
print(m.groupby('dbin',observed=True).agg(n=('id','size'),med_outlier=('outlier','median'),save=('save_rate','median'),share=('share_rate','median')).round(4))
print(m.groupby('slideshow').agg(n=('id','size'),med_outlier=('outlier','median'),save=('save_rate','median'),share=('share_rate','median')).round(4))
print(m.groupby('question_hook').agg(n=('id','size'),med_outlier=('outlier','median')).round(3))
print(m.groupby('series').agg(n=('id','size'),med_outlier=('outlier','median')).round(3))
# correlation outlier vs rates
print(m[['outlier','save_rate','share_rate','comment_rate','like_rate','duration']].corr(method='spearman').round(2)['outlier'])
top.to_csv(D+'tiktok_top30_outliers.csv',index=False); bot.to_csv(D+'tiktok_bottom30.csv',index=False)
