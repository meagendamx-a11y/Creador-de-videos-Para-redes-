import re, sys, subprocess
rep, D = sys.argv[1], sys.argv[2]
subprocess.run([sys.executable, "-I", "scripts/code_outliers.py", D], check=True)
tables = subprocess.run([sys.executable, "-I", "scripts/md_tables.py", D], capture_output=True, text=True, check=True).stdout
tables = tables.replace("### es_long", "### Top-50 outliers · español · videos largos").replace("### en_long", "### Top-30 outliers · inglés · videos largos (referencia)")
tables = tables.replace("### es_short", "### Top-25 outliers · español · Shorts").replace("### en_short", "### Top-15 outliers · inglés · Shorts")
block = "<!-- TABLAS_INICIO -->\n" + tables + "\n<!-- TABLAS_FIN -->"
s = open(rep, encoding="utf-8").read()
if "<<TABLAS>>" in s: s = s.replace("<<TABLAS>>", block)
else: s = re.sub(r"<!-- TABLAS_INICIO -->.*?<!-- TABLAS_FIN -->", lambda m: block, s, flags=re.S)
open(rep, "w", encoding="utf-8").write(s)
print("ok")
