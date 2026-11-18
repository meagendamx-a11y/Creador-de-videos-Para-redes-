import pandas as pd,urllib.request,os,sys
from PIL import Image,ImageDraw
D='/tmp/claude-0/-home-user-Creador-de-videos-Para-redes-/f6e80049-54f1-5e5b-b0dd-1d5ea884d7d2/scratchpad/research/apify/'
O='/tmp/claude-0/-home-user-Creador-de-videos-Para-redes-/f6e80049-54f1-5e5b-b0dd-1d5ea884d7d2/scratchpad/covers_dl/'
sets={'top':pd.read_csv(D+'tiktok_top30_outliers.csv'),'bot':pd.read_csv(D+'tiktok_bottom30.csv')}
h=pd.read_csv(D+'tiktok_videos.csv'); h=h[(h.src!='profile')&(h.lang=='es')].sort_values('views',ascending=False).head(30); sets['hash']=h
for name,df in sets.items():
    ims=[]
    for i,r in enumerate(df.itertuples()):
        fn=f'{O}{name}_{i:02d}.jpg'
        if not os.path.exists(fn):
            try:
                req=urllib.request.Request(r.cover,headers={'User-Agent':'Mozilla/5.0'})
                open(fn,'wb').write(urllib.request.urlopen(req,timeout=30).read())
            except Exception as e: print('fail',i,e); continue
        try: im=Image.open(fn).convert('RGB').resize((240,427))
        except Exception as e: print('bad',fn,e); continue
        d=ImageDraw.Draw(im); d.rectangle([0,0,240,22],fill=(0,0,0)); d.text((3,4),f'{i} {r.author[:18]}',fill=(255,255,0))
        ims.append(im)
    for k in range(0,len(ims),15):
        sheet=Image.new('RGB',(240*5,427*3),'white')
        for j,im in enumerate(ims[k:k+15]): sheet.paste(im,((j%5)*240,(j//5)*427))
        sheet.save(f'{O}sheet_{name}_{k//15}.jpg',quality=80)
print('ok')
