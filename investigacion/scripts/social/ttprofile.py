import sys, json, re, subprocess, time
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"
out=[]
for h in sys.argv[2:]:
    h=h.lstrip('@')
    html=subprocess.run(["curl","-sS","-m","30","-A",UA,f"https://www.tiktok.com/@{h}"],capture_output=True,text=True).stdout
    m=re.search(r'<script id="__UNIVERSAL_DATA_FOR_REHYDRATION__"[^>]*>(.*?)</script>',html,re.S)
    rec={"handle":h}
    if m:
        try:
            d=json.loads(m.group(1))["__DEFAULT_SCOPE__"].get("webapp.user-detail",{})
            rec["status"]=d.get("statusCode")
            ui=d.get("userInfo",{})
            u=ui.get("user",{}); s=ui.get("statsV2") or ui.get("stats",{})
            rec.update(nickname=u.get("nickname"),verified=u.get("verified"),bio=u.get("signature"),
                followers=s.get("followerCount"),likes=s.get("heartCount") or s.get("heart"),videos=s.get("videoCount"),
                created=u.get("createTime"),region=u.get("region"),language=u.get("language"),link=(u.get("bioLink") or {}).get("link"))
        except Exception as e: rec["err"]=str(e)
    else: rec["err"]="no data"
    out.append(rec); print(json.dumps(rec,ensure_ascii=False)); sys.stdout.flush()
    time.sleep(2)
json.dump(out,open(sys.argv[1],"w"),ensure_ascii=False,indent=1)
