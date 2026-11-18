import sys, json, re, subprocess, time, html as H
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"
out=[]
for h in sys.argv[2:]:
    r=subprocess.run(["curl","-sS","-m","30","-A",UA,"-w","\n%{http_code}",f"https://www.instagram.com/{h}/"],capture_output=True,text=True).stdout
    code=r.rsplit("\n",1)[-1]
    m=re.search(r'<meta property="og:description" content="([^"]*)"',r)
    t=re.search(r'<meta property="og:title" content="([^"]*)"',r)
    rec={"handle":h,"http":code,"og_desc":H.unescape(m.group(1)) if m else None,"og_title":H.unescape(t.group(1)) if t else None}
    if m:
        mm=re.match(r'([\d.,KMmk]+) Followers, ([\d.,KMmk]+) Following, ([\d.,KMmk]+) Posts',rec["og_desc"])
        if mm: rec.update(followers=mm.group(1),following=mm.group(2),posts=mm.group(3))
    out.append(rec); print(json.dumps(rec,ensure_ascii=False)); sys.stdout.flush(); time.sleep(3)
json.dump(out,open(sys.argv[1],"w"),ensure_ascii=False,indent=1)
