#!/bin/bash
# date pass (english locale so approximate_date parses), videos + shorts tabs, spanish channels only
OUT="$2"; mkdir -p "$OUT"
while IFS=$'\t' read -r name cid lang kind; do
  [ "$lang" != "es" ] && continue
  if [[ "$cid" == @* ]]; then base="https://www.youtube.com/$cid"; else base="https://www.youtube.com/channel/$cid"; fi
  for tab in videos shorts; do
  f="$OUT/${name}_${tab}.tsv"
  [ -s "$f" ] && continue
  for attempt in 1 2 3; do
    yt-dlp --js-runtimes node --flat-playlist --sleep-requests 1 --extractor-args "youtubetab:approximate_date" \
      --print "%(id)s	%(timestamp)s	%(view_count)s" "$base/$tab" > "$f" 2> "$OUT/${name}_${tab}.err"
    if grep -q "not a bot" "$OUT/${name}_${tab}.err"; then sleep $((120*attempt)); else break; fi
  done
  echo "$(date +%T) $name $tab $(wc -l < "$f")"; sleep 3
  done
done < "$1"
echo DONE
