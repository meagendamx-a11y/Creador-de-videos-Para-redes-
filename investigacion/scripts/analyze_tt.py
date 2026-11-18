import json,glob,statistics as st,csv,datetime as dt
prof={}
for f in glob.glob('tt_batch*.json')+['tt_test.json']:
    for r in json.load(open(f)): 
        if r.get('status')==0: prof[r['handle']]=r
rows=[];allv=[]
for f in sorted(glob.glob('tt_videos/*.json')):
    h=f.split('/')[-1][:-5]
    try: d=json.load(open(f))
    except: continue
    E=[e for e in d.get('entries',[]) if e.get('view_count') is not None]
    if not E: continue
    ts=sorted([e['timestamp'] for e in E if e.get('timestamp')])
    # exclude first 3 (possible pinned) for cadence: use median gap of sorted timestamps
    span_days=(ts[-1]-ts[0])/86400 if len(ts)>1 else 0
    # recent 30: last 30 by timestamp
    Es=sorted(E,key=lambda e:-e.get('timestamp',0))
    rec=Es[:30]
    v=[e['view_count'] for e in rec]
    def rate(k): 
        tv=sum(e['view_count'] for e in rec) or 1
        return round(100*sum((e.get(k) or 0) for e in rec)/tv,2)
    durs=[e.get('duration') or 0 for e in rec]
    music=sum(1 for e in rec if e.get('track') and not str(e.get('track')).lower().startswith(('original sound','sonido original','som original','son original')))
    gaps=[(Es[i]['timestamp']-Es[i+1]['timestamp'])/86400 for i in range(min(29,len(Es)-1))]
    p=prof.get(h,{})
    row=dict(handle=h,followers=p.get('followers'),likes_total=p.get('likes'),videos_total=p.get('videos'),verified=p.get('verified'),
        n=len(rec),posts_per_week=round(7/st.median(gaps),1) if gaps and st.median(gaps)>0 else None,
        median_views=int(st.median(v)),mean_views=int(st.mean(v)),max_views=max(v),
        like_rate=rate('like_count'),save_rate=rate('save_count'),share_rate=rate('repost_count'),comment_rate=rate('comment_count'),
        median_dur=st.median(durs),pct_le30=round(100*sum(1 for x in durs if x<=30)/len(durs)),pct_gt60=round(100*sum(1 for x in durs if x>60)/len(durs)),
        pct_music_track=round(100*music/len(rec)),
        last_post=dt.datetime.utcfromtimestamp(Es[0]['timestamp']).strftime('%Y-%m-%d'),
        views_per_follower=round(st.median(v)/int(p['followers']),3) if p.get('followers') and int(p['followers'])>0 else None)
    rows.append(row)
    for e in E:
        allv.append(dict(handle=h,id=e['id'],url=e['url'],views=e['view_count'],likes=e.get('like_count'),saves=e.get('save_count'),shares=e.get('repost_count'),comments=e.get('comment_count'),duration=e.get('duration'),track=e.get('track'),date=dt.datetime.utcfromtimestamp(e.get('timestamp',0)).strftime('%Y-%m-%d'),desc=(e.get('description') or '').replace('\n',' ')))
with open('tt_account_metrics.csv','w') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
with open('tt_all_videos.csv','w') as f:
    w=csv.DictWriter(f,fieldnames=list(allv[0].keys())); w.writeheader(); w.writerows(allv)
for r in sorted(rows,key=lambda r:-int(r['followers'] or 0)):
    print(f"{r['handle'][:24]:24} f={int(r['followers'] or 0)/1e6:6.2f}M ppw={r['posts_per_week']} medV={r['median_views']:>8} maxV={r['max_views']:>9} like%={r['like_rate']} save%={r['save_rate']} share%={r['share_rate']} dur={r['median_dur']} <=30s:{r['pct_le30']}% >60s:{r['pct_gt60']}% music:{r['pct_music_track']}% last={r['last_post']} vpf={r['views_per_follower']}")
print(len(allv))
