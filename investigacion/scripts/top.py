import json,sys,statistics
for f in sys.argv[1:]:
    try: d=json.load(open(f))
    except Exception: continue
    if not d or 'entries' not in d: continue
    E=[e for e in d['entries'] if e]
    vs=[e.get('view_count') or 0 for e in E]
    print(f"\n### {f} | {d.get('channel')} subs={d.get('channel_follower_count')} n={len(E)} median={statistics.median(vs) if vs else 0}")
    print("keys:", sorted(E[0].keys())[:40] if E else '')
    print("-- newest 12:")
    for e in E[:12]: print(f"  {e.get('view_count')}\t{e.get('duration')}\t{e.get('title')}\t{e.get('id')}")
    print("-- top 15:")
    for e in sorted(E,key=lambda e:-(e.get('view_count') or 0))[:15]: print(f"  {e.get('view_count')}\t{e.get('duration')}\t{e.get('title')}\t{e.get('id')}")
