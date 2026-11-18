# Scripts de la investigación

Referencia de método (nov-2026). Muchos apuntan a rutas temporales de la sesión original (`/tmp/claude-0/.../scratchpad/...`): ajústalas a `investigacion/datos/` o a una carpeta nueva antes de re-ejecutar.

- `fetch_*.sh`, `analyze_outliers.py`, `topics.py`, `topic_lag.py` → informe 02 (outliers YouTube, yt-dlp).
- `comentarios/`, `codebook.py`, `comments.py` → informe 03 (comentarios YouTube).
- `suggest_*.py`, `trends_analyze.py`, `region_analyze.py` → informe 04 (Google Trends + autocompletado).
- `social/`, `pw_*.js`, `an_tt.py`, `an_ig.py` → informe 05 (TikTok/IG públicos).
- `build_tt.py`, `analyze_tt.py`, `com.py` → informe 07 (Apify; la autenticación la inyecta el proxy, no hay claves en código).
