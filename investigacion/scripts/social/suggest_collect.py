import json, time, random, urllib.parse, urllib.request, os

OUT = "/tmp/claude-0/-home-user-Creador-de-videos-Para-redes-/f6e80049-54f1-5e5b-b0dd-1d5ea884d7d2/scratchpad/research/trends"
ROOTS = ["la psicología de las personas que", "por qué me siento", "cómo dejar de", "cómo saber si",
         "señales de que", "por qué las personas", "psicólogo", "terapia", "ansiedad", "mi pareja",
         "mi mamá", "mi hijo",
         # extras útiles
         "qué hacer si", "es normal", "por qué no puedo", "cómo superar", "cómo manejar", "test de"]
LETTERS = [""] + list("abcdefghijklmnopqrstuvwxyzñ")


def fetch(q, yt):
    url = "https://suggestqueries.google.com/complete/search?client=firefox&hl=es&gl=mx&q=" + urllib.parse.quote(q)
    if yt:
        url += "&ds=yt"
    for a in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=15) as r:
                raw = r.read()
                try:
                    txt = raw.decode("utf-8")
                except UnicodeDecodeError:
                    txt = raw.decode("latin-1")
                return json.loads(txt)[1]
        except Exception as e:
            time.sleep(3 * (a + 1))
    return None


res = []
for src, yt in [("google", False), ("youtube", True)]:
    for root in ROOTS:
        for L in LETTERS:
            q = f"{root} {L}".rstrip() if L else root + " "
            s = fetch(q, yt)
            res.append({"source": src, "root": root, "letter": L, "query": q, "suggestions": s or [], "ok": s is not None})
            time.sleep(random.uniform(0.25, 0.6))
        print(src, root, flush=True)
json.dump(res, open(f"{OUT}/autocomplete_raw.json", "w"), ensure_ascii=False, indent=1)
print("done", sum(len(r["suggestions"]) for r in res))
