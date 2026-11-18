#!/bin/bash
# Usage: dl_comments.sh <idlist.txt> <outdir>
# Sequential download of comments with backoff on bot/429 blocks.
LIST="$1"; OUT="$2"; mkdir -p "$OUT"
while read -r id; do
  [ -z "$id" ] && continue
  if [ -s "$OUT/$id.info.json" ] && python3 -c "import json,sys;d=json.load(open('$OUT/$id.info.json'));sys.exit(0 if (d.get('comments') or d.get('comment_count')==0) else 1)" 2>/dev/null; then
    echo "skip $id"; continue
  fi
  for attempt in 1 2 3 4; do
    timeout 400 yt-dlp --js-runtimes node --skip-download --write-comments --write-info-json --ignore-no-formats-error \
      --extractor-args "youtube:max_comments=300,all,30,3;comment_sort=top" \
      --sleep-requests 1 --no-progress -o "$OUT/%(id)s.%(ext)s" "https://www.youtube.com/watch?v=$id" \
      > "$OUT/$id.log" 2> "$OUT/$id.err"
    n=$(python3 -c "import json;d=json.load(open('$OUT/$id.info.json'));print(len(d.get('comments') or []))" 2>/dev/null || echo 0)
    if [ "$n" -gt 0 ]; then echo "ok $id $n (attempt $attempt)"; break; fi
    if python3 -c "import json,sys;d=json.load(open('$OUT/$id.info.json'));sys.exit(0 if not d.get('comment_count') else 1)" 2>/dev/null; then echo "nocomments $id"; break; fi
    w=$((attempt*90)); echo "retry $id in ${w}s ($(grep -o 'not a bot\|429\|ERROR.*' "$OUT/$id.err" | head -1))"; sleep $w
  done
  sleep 6
done < "$LIST"
echo DONE
