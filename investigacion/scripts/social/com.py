import json,sys,os
tot=0
for f in sys.argv[1:]:
    d=json.load(open(f))
    C=[c for c in (d.get('comments') or []) if c.get('parent')=='root']
    tot+=len(C)
    print(f"\n##### {d.get('channel')} | {d.get('title')} | {d.get('upload_date')} | views={d.get('view_count')} likes={d.get('like_count')} comments_total={d.get('comment_count')} dur={d.get('duration')} fetched={len(C)}")
    for c in sorted(C,key=lambda c:-(c.get('like_count') or 0))[:int(os.environ.get('N','25'))]:
        t=c['text'].replace('\n',' ')[:260]
        print(f"  [{c.get('like_count')}] {t}")
print("TOTAL top-level fetched:",tot)
