import csv,os,sys
from PIL import Image,ImageDraw
base=sys.argv[1]; os.makedirs(base+'/sheets',exist_ok=True)
sel=[r for r in csv.DictReader(open(base+'/selected_videos.csv')) if r['handle']!='faridieck']
marks=['0','1','2.5','4.5','10']
def row(r):
    ims=[]
    for m in marks:
        p=f"{base}/frames/{r['id']}_{m}.png"
        if os.path.exists(p): ims.append(Image.open(p).crop((38,40,363,520)).resize((217,320)))
    if not ims: return None
    W=sum(i.width for i in ims); s=Image.new('RGB',(W,345),'white'); x=0
    for i in ims: s.paste(i,(x,25)); x+=i.width
    ImageDraw.Draw(s).text((4,4),f"{r['handle']} | {r['id']} | {r['views']} views | {r['duration']}s | frames: poster,1,2.5,4.5,10s",fill='black')
    return s
rows=[x for x in (row(r) for r in sel) if x]
for i in range(0,len(rows),2):
    pair=rows[i:i+2]; W=max(p.width for p in pair); H=sum(p.height for p in pair)
    s=Image.new('RGB',(W,H),'white'); y=0
    for p in pair: s.paste(p,(0,y)); y+=p.height
    s.save(f"{base}/sheets/sheet_{i//2:02d}.png")
print(len(rows))
