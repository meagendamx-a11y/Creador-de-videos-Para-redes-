#!/usr/bin/env python3
"""Merge final_outliers.csv with manual coding (tema macro, plantilla, serie, reencuadre) and per-video details if present."""
import csv, json, os, sys
D = sys.argv[1]
# manual coding by (list, rank): (tema_macro, plantilla_manual, serie/franquicia, gancho)
ES = {
1:("rasgos/inteligencia","Psicología de [rasgo] (Por qué algunas personas…)","franquicia 'Psicología de' (traducción de PsychToons 21-oct-2026)","validación de habilidad"),
2:("rasgos cotidianos","La psicología de las personas que [hábito]","franquicia PDP","identificación"),
3:("rasgos cotidianos","La psicología de las personas que [hábito] (Y por qué molestan)","franquicia PDP","identificación + conflicto"),
4:("trastornos (detección)","COMPORTAMIENTOS extraños que son señales de [X]","no","alarma/curiosidad"),
5:("rasgos cotidianos (sueño)","La PSICOLOGÍA de las personas que [hábito]","franquicia PDP (mismo tema que LPI)","identificación"),
6:("relaciones/rasgo","La psicología de las personas que [conducta]","franquicia PDP","identificación"),
7:("amor/atracción","N señales psicológicas de que le gustas (la ciencia no miente)","lista señales","detección en otro"),
8:("social/autopercepción","N señales de que [defecto] sin darte cuenta (la psicología lo explica)","lista señales","miedo social"),
9:("rasgos cotidianos (redes)","La PSICOLOGÍA de las personas que NO [hábito]","franquicia PDP","identificación"),
10:("inteligencia","N señales de [bajo IQ] (lo que nadie te dice)","lista señales","autoevaluación"),
11:("rasgos cotidianos","Si [no te gusta X], tu cerebro es diferente","no","validación"),
12:("inteligencia emocional","¿Tienes ESTAS actitudes? Señales de [X]","lista señales","autoevaluación"),
13:("trastornos (ansiedad)","TODOS LOS [síntomas de X] EXPLICADOS","explicado/compendio","compendio"),
14:("social","N señales psicológicas de que le CAES MAL a alguien","lista señales","detección en otro"),
15:("rasgos cotidianos","La psicología de las personas que [gusto]","franquicia PDP","identificación"),
16:("trastornos/autoayuda práctica","¿Cómo combatir [X]? (N pasos)","psicólogo con cara","solución"),
17:("rasgos (introversión)","La PSICOLOGÍA de las personas que prefieren estar SOLAS","franquicia PDP","validación"),
18:("social","N señales de que te envidian","lista señales","detección en otro"),
19:("test/psicología oscura","N preguntas revelan tu [lado oscuro]","test","autoevaluación"),
20:("rasgos cotidianos","Psicología de personas que NO [hábito] (y no es casualidad)","franquicia PDP","identificación"),
21:("trastornos (depresión)","N síntomas de [depresión oculta]","lista señales","detección"),
22:("amor/apego","Psicología de las personas que se ILUSIONAN rápido","franquicia PDP","identificación"),
23:("amor","N señales de que nunca estuviste enamorado","lista señales","reencuadre de experiencia"),
24:("test","\"Si respondiste esto en N segundos, no eres normal\"","test","reto"),
25:("trastornos (TDAH)","N señales de que es [X], y NO [Y]","reencuadre 'no es X, es Y'","reencuadre/alivio de culpa"),
26:("trastornos (neurodivergencia)","Todas las [X] explicadas en N minutos","compendio 'explicado en N min'","compendio"),
27:("rasgos (introversión)","Psicología de personas que NO disfrutan [X]","franquicia PDP","validación"),
28:("filosofía/pseudo","[Afirmación] – [autor clásico]","franquicia 'autor clásico'","misterio"),
29:("filosofía/autoayuda","[Consejo] – La filosofía de [autor]","franquicia 'autor clásico'","consejo"),
30:("emociones/autoayuda práctica","Cómo dejar de [X] (técnica de N pasos)","psicólogo con cara","solución"),
31:("relaciones tóxicas","[Trastorno]: N frases habituales","lista","detección en otro"),
32:("adicciones/Jung","La psicología de [X] – Carl Jung","franquicia 'autor clásico'","autoridad"),
33:("trastornos (autismo)","[X] vs [Y] ¿Qué diferencia hay?","comparativa","aclaración"),
34:("relaciones tóxicas","N señales de que tu PAREJA es [X]","lista señales","detección en otro"),
35:("filosofía/autoayuda","[Frase inspiracional]","franquicia 'autor clásico'","consuelo"),
36:("autoayuda/reencuadre","No eres [X], solo estás [Y]","reencuadre","alivio de culpa"),
37:("social","N cosas que te hacen [defecto] sin que te des cuenta","lista","miedo social"),
38:("atracción","N señales de que eres ATRACTIVO (y no lo sabes)","lista señales","validación"),
39:("atracción/personalidad","N señales de que tienes una personalidad ATRACTIVA (y nadie te lo ha dicho)","lista señales","validación"),
40:("amor/espiritualidad","Por qué el universo te envía a alguien… | Psicología de Carl Jung","franquicia 'autor clásico'","misterio romántico"),
41:("autoconocimiento","La psicología de [X]","franquicia 'autor clásico'","autoconocimiento"),
42:("relaciones tóxicas","N preguntas para saber si tu pareja es [X]","test","detección en otro"),
43:("trauma","N señales de que arrastras HERIDAS EMOCIONALES","lista señales","autoevaluación"),
44:("trastornos (fobias)","Todas las [X] explicadas en N minutos","compendio 'explicado en N min'","compendio"),
45:("trastornos (burnout)","N señales de que NO es [X], sino [Y]","reencuadre 'no es X, es Y'","alivio de culpa"),
46:("social/lenguaje","¿Por qué [hábito] – y qué dice eso sobre ti?","no","autoconocimiento"),
47:("rasgos cotidianos","La psicología de las personas a las que no les importa [X]","franquicia PDP","identificación"),
48:("rasgos cotidianos (redes)","¿Por qué algunas personas [hábito]? (Psicología)","no","identificación"),
49:("trastornos (personalidad)","Cada [X] explicado en N minutos","compendio 'explicado en N min'","compendio"),
50:("emociones (depresión oculta)","N señales de que NO \"estoy bien\"","lista señales","identificación"),
}
EN = {
1:("inteligencia","Psychology of People With [rasgo]","franquicia PDP","validación"),
2:("autoayuda (virtud)","Psychology of [virtud] (And How to [truco])","franquicia 'Psychology of [virtud]' PsychToons","promesa"),
3:("inteligencia/rasgos","Psychology of [rasgo]: Why [X] Is an Unfair Advantage","franquicia PsychToons","validación + promesa"),
4:("inteligencia/autoayuda","Psychology of [X]: [promesa hiperbólica] So Fast It's Almost Unfair","franquicia PsychToons","promesa hiperbólica"),
5:("rasgos cotidianos","Psychology of People Who [hábito]","franquicia PDP","identificación"),
6:("emociones/rasgo","Psychology of People Who [reacción emocional]","franquicia PDP","identificación"),
7:("rasgos cotidianos","People Who [rasgo] | Psychology explained","franquicia PDP","identificación"),
8:("inteligencia/autoayuda","Psychology of [tipo de inteligencia]: How To…","franquicia PsychToons","promesa"),
9:("inteligencia/trauma","N Signs You Have [inteligencia rara]","lista señales","validación"),
10:("generaciones","Psychology of [generación]","franquicia generaciones","nostalgia/identidad"),
11:("inteligencia/rasgos","Psychology of [tipo de inteligencia] (Why Some People…)","franquicia PsychToons","validación"),
12:("autoayuda (virtud)","Psychology of [virtud]: Build a Mind So Strong It Scares People","franquicia PsychToons","promesa hiperbólica"),
13:("generaciones","Psychology of People Who Grew Up in the [década]","franquicia generaciones","nostalgia/identidad"),
14:("rasgos (introversión)","The Psychology of People Who Love [hábito]","franquicia PDP","validación"),
15:("rasgos cotidianos","Psychology of People Who Don't [hábito]","franquicia PDP","identificación"),
16:("rasgos (hiperconciencia)","The Psychology of People Who Are Too [rasgo]","franquicia PDP","validación"),
17:("rasgos (soledad)","Why Some People Are Meant to [X] (Psychology Explains)","franquicia PsychToons","validación"),
18:("generaciones","Psychology of [generación] (años)","franquicia generaciones","nostalgia/identidad"),
19:("autoayuda (adicción)","Psychology of [problema] (And How to Beat It Without [X])","franquicia PsychToons","promesa"),
20:("autoayuda (virtud)","Psychology of [virtud]: Be So [X] It Makes People Nervous","franquicia PsychToons","promesa hiperbólica"),
21:("autoayuda (virtud)","Psychology of [virtud]: [X] So Well It Makes You Dangerous","franquicia PsychToons","promesa hiperbólica"),
22:("autoayuda (social)","Psychology of [virtud]: How To Actually…","franquicia PsychToons","promesa"),
23:("autoayuda","The Psychology of Not Giving A F*ck","franquicia PsychToons","irreverencia"),
24:("concepto/efecto","The [efecto psicológico]","no (catálogo Sprouts)","concepto"),
25:("rasgos cotidianos","Psychology of People Who Don't [hábito]","franquicia PDP","identificación"),
26:("familia/infancia","N Toxic Things Parents Say To Their Children","lista","identificación/herida"),
27:("rasgos cotidianos (redes)","Psychology of People Who Don't [hábito]","franquicia PDP","identificación"),
28:("rasgos (introversión)","Psychology of People Who Love [hábito]","franquicia PDP","validación"),
29:("social","N Things Only Fake Friends Do","lista","detección en otro"),
30:("autoayuda (virtud)","Psychology of [virtud] (And How To Stop [X])","franquicia PsychToons","promesa"),
}
rows = list(csv.DictReader(open(os.path.join(D, "final_outliers.csv"), encoding="utf-8")))
out = []
for r in rows:
    rk = int(r["rank"]); m = None
    if r["list"] == "es_long": m = ES.get(rk)
    elif r["list"] == "en_long": m = EN.get(rk)
    det = {}
    pth = os.path.join(D, "details", r["id"] + ".json")
    if os.path.exists(pth) and os.path.getsize(pth) > 10:
        try: det = json.load(open(pth, encoding="utf-8"))
        except Exception: det = {}
    o = {k: r[k] for k in ("list", "rank", "channel", "kind", "id", "title", "views", "channel_median", "outlier_score", "local_score", "duration_s", "approx_date", "theme_primary", "template")}
    o.update({
        "upload_date_exact": det.get("upload_date") or "", "views_exact": det.get("view_count") or "",
        "likes": det.get("like_count") or "", "comments": det.get("comment_count") or "",
        "channel_subs": det.get("channel_follower_count") or "",
        "tema_manual": m[0] if m else "", "plantilla_manual": m[1] if m else "",
        "serie_franquicia": m[2] if m else "", "gancho": m[3] if m else "",
        "url": f"https://www.youtube.com/watch?v={r['id']}",
    })
    out.append(o)
with open(os.path.join(D, "outliers_coded.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)
print("coded", len(out), "with details", sum(1 for o in out if o["upload_date_exact"]))
