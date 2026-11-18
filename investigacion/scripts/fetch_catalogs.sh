#!/bin/bash
# usage: fetch_catalogs.sh channels.tsv outdir
OUT="$2"; mkdir -p "$OUT"
while IFS=$'\t' read -r name cid lang kind; do
  [ -z "$name" ] && continue
  if [[ "$cid" == @* ]]; then base="https://www.youtube.com/$cid"; else base="https://www.youtube.com/channel/$cid"; fi
  for tab in videos shorts; do
    f="$OUT/${name}_${tab}.json"
    if [ -s "$f" ] && [ "$(stat -c%s "$f")" -gt 100 ]; then continue; fi
    for attempt in 1 2 3; do
      yt-dlp --js-runtimes node --flat-playlist -J --sleep-requests 1 \
        --extractor-args "youtubetab:approximate_date" --extractor-args "youtube:lang=$lang" \
        "$base/$tab" > "$f" 2> "$OUT/${name}_${tab}.err"
      if grep -q "not a bot" "$OUT/${name}_${tab}.err"; then echo "BOT block $name $tab, sleeping"; sleep $((120*attempt)); else break; fi
    done
    echo "$(date +%T) $name $tab $(stat -c%s "$f")"
    sleep 3
  done
done < "$1"
echo DONE
