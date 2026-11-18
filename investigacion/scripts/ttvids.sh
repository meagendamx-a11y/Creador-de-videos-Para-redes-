#!/bin/bash
cd /tmp/claude-0/-home-user-Creador-de-videos-Para-redes-/f6e80049-54f1-5e5b-b0dd-1d5ea884d7d2/scratchpad/research/social
for h in "$@"; do
  timeout 300 yt-dlp --js-runtimes node --flat-playlist --playlist-end 60 -J "https://www.tiktok.com/@$h" 2>/dev/null > tt_videos/$h.json
  python3 -c "
import json
try:
  d=json.load(open('tt_videos/$h.json')); print('$h',len(d.get('entries',[])))
except Exception as e: print('$h','ERR',e)"
  sleep 3
done
