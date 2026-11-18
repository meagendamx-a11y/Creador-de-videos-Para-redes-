#!/bin/bash
# usage: fetch_details.sh ids.tsv outdir thumbdir
mkdir -p "$2" "$3"
while IFS=$'\t' read -r id lang thumb; do
  f="$2/$id.json"; [ -s "$f" ] && continue
  extra=(); [ "$thumb" = "1" ] && extra=(--write-thumbnail --convert-thumbnails jpg -o "$3/%(id)s.%(ext)s")
  for attempt in 1 2 3; do
    yt-dlp --js-runtimes node --skip-download -j --sleep-requests 1 --ignore-no-formats-error --extractor-args "youtube:lang=$lang;player_client=mweb" "${extra[@]}" \
      "https://www.youtube.com/watch?v=$id" 2> "$2/$id.err" | python3 -c "
import json,sys
d=json.load(sys.stdin)
keep=['id','title','upload_date','view_count','like_count','comment_count','duration','channel','channel_id','channel_follower_count','tags','categories','description','language','playlist']
o={k:d.get(k) for k in keep}; o['description']=(o['description'] or '')[:1500]
print(json.dumps(o,ensure_ascii=False))" > "$f"
    if grep -qi "bot" "$2/$id.err"; then rm -f "$f"; sleep $((300*attempt)); else break; fi
  done
  sleep 12
done < "$1"
echo DONE
