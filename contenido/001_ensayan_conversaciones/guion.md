# 001 · La psicología de las personas que ensayan conversaciones en su cabeza

## ⭐ VERSIÓN 2 · ~30 s (vigente, 20-nov-2026)
Usa las escenas ya aprobadas **E1 (regadera), E2 (cama), E3 (espejo)** y **una escena nueva, E4**.

### Texto para ElevenLabs (copiar y pegar)
```
[curious] ¿Alguna vez ganaste una discusión… en la regadera?

[calm] Ensayar conversaciones en tu cabeza es muy común: lo que le dirías a tu jefe, a tu ex… o lo que debiste contestar hace años.

[thoughtful] Y sirve: tu mente practica… para que la conversación real dé menos miedo.

[gently] Pero si se vuelve un círculo que no te deja dormir… escríbelo una vez, y dile a tu mente: "ya quedó guardado".

[warmly] Y si te pasa seguido, hablarlo con alguien ayuda.
```

| Escena | Voz | Título en pantalla | Clip |
|---|---|---|---|
| E1 · regadera | "¿Alguna vez ganaste una discusión… en la regadera?" | — | ✅ |
| E2 · cama | "Ensayar conversaciones… hace años." | Ensayar conversaciones | ✅ |
| E3 · espejo | "Y sirve: tu mente practica…" | Te prepara | ✅ |
| E4 · nota en la noche | "Pero si se vuelve un círculo… hablarlo con alguien ayuda." | Escríbelo una vez | ⏳ Pedir a Gemini |

---

## VERSIÓN 1 · ~57 s (archivada; audio en `assets/voz_v1_57s.mp3`)

| Campo | Valor |
|---|---|
| Formato | Short vertical 9:16 · **~60 s** · TikTok, Reels y YouTube Shorts |
| Tipo de pieza | "La psicología de las personas que…" (pieza para guardar y compartir) |
| Personaje | El Observador |
| Por qué este tema | Rasgo cotidiano con el que la gente se identifica. Formato con hueco en Shorts en español (informe 02). Conecta con "sobrepensar", que es la búsqueda #1 de ansiedad en México (informe 04). No convierte una conducta normal en enfermedad |
| Revisión clínica | ⏳ Pendiente: firma del psicólogo responsable |
| Estado | 🟡 Borrador para aprobación del fundador |

## Guion (voz en off con tu voz clonada)

| # | Tiempo | Voz | Texto en pantalla | Escena |
|---|---|---|---|---|
| 1 | 0–4 s | ¿Alguna vez ganaste una discusión… en la regadera? | **¿GANASTE UNA DISCUSIÓN EN LA REGADERA?** | E1 |
| 2 | 4–12 s | Hay personas que ensayan conversaciones en su cabeza. Lo que le van a decir a su jefe, a su ex, o lo que debieron contestar hace tres años. | Ensayar conversaciones 🧠 | E2 |
| 3 | 12–22 s | En psicología esto se estudia como "interacciones imaginadas". Y casi siempre tiene una función: prepararte. Tu mente practica para que la conversación real dé menos miedo. | **1. Te prepara** | E3 |
| 4 | 22–32 s | También sirve para entender lo que sentiste. Repasar lo que pasó ayuda a ordenar emociones que en el momento no supiste nombrar. | **2. Ordena lo que sentiste** | E4 |
| 5 | 32–42 s | Y muchas veces es cuidado: piensas cómo decir algo difícil sin lastimar a nadie. | **3. Cuida tus vínculos** | E5 |
| 6 | 42–52 s | Ahora, si el ensayo se vuelve un círculo, la misma escena una y otra vez, y te quita el sueño o la calma, ya no te está preparando: te está desgastando. | ⚠️ Cuando se vuelve un círculo | E6 |
| 7 | 52–60 s | Un truco: escríbelo en una nota, una sola vez, y dile a tu mente: "ya quedó guardado". Y si te pasa seguido, hablarlo con alguien ayuda. | **Escríbelo una vez ✍️** | E7 |

**Palabras:** ~150, unos 60 s a ritmo pausado.
**Revisión de estilo:** sin "no es esto, sino aquello", sin diagnosticar y sin "debes ir a terapia".

## Texto para ElevenLabs (copiar y pegar)
Modelo con etiquetas de audio (v3). Las etiquetas van en minúsculas y entre corchetes. Los puntos suspensivos marcan pausas y las MAYÚSCULAS dan énfasis. Si una etiqueta suena rara con tu voz, quítala: los signos de puntuación hacen la mitad del trabajo.

```
[curious] ¿Alguna vez ganaste una discusión… [laughs] en la regadera?

Hay personas que ensayan conversaciones en su cabeza. Lo que le van a decir a su jefe… a su ex… o lo que debieron contestar [sighs] hace TRES años.

[thoughtful] En psicología, esto se estudia como "interacciones imaginadas". Y casi siempre tiene una función: prepararte. Tu mente practica… para que la conversación real dé menos miedo.

También sirve para entender lo que sentiste. Repasar lo que pasó ayuda a ordenar emociones que, en el momento, no supiste nombrar.

[warmly] Y muchas veces… es cuidado: piensas cómo decir algo difícil sin lastimar a nadie.

[serious] Ahora… si el ensayo se vuelve un círculo, la misma escena una y otra vez, y te quita el sueño o la calma… ya no te está preparando. Te está desgastando.

[calm] Un truco: escríbelo en una nota. Una sola vez. Y dile a tu mente: "ya quedó guardado".

[softly] Y si te pasa seguido… hablarlo con alguien ayuda.
```

Ajustes sugeridos: Stability ~50 (en v3, "Natural"). Genera 2 o 3 tomas y quédate con la mejor. Si una frase falla, regenera solo esa.

## Escenas para Gemini
Usa siempre la referencia `personaje/observer/referencia_gemini_conceptos_observer.jpg` y la ficha (sección 0 de `PROMPTS_GEMINI.md`).
**Paso 1:** pide la imagen fija vertical 9:16 y revísala. **Paso 2:** conviértela en un clip de 6 a 8 s con cámara fija.
Deja libre el tercio superior del encuadre para el texto.

| Escena | Imagen fija (descripción para el prompt) | Movimiento del clip |
|---|---|---|
| **E1** | The Observer in a shower with a shower curtain, steam, gesturing confidently with one finger raised, mid-argument, proud expression | Gestures as if winning an argument, then nods proudly |
| **E2** | The Observer lying in bed at night, eyes open, three small thought bubbles above: a boss figure, a heart, a clock | Thought bubbles appear one by one; blinks |
| **E3** | The Observer standing in front of a mirror, practicing, hand on chest, calm | Rehearses with small hand gestures, takes a breath |
| **E4** | The Observer sitting on a stool with a notebook, a small thought bubble with tangled lines turning into a straight line | Tangled lines untangle in the bubble; slight smile |
| **E5** | The Observer holding a phone, thinking carefully before typing, gentle expression, small heart icon | Types, deletes, types again, then smiles softly |
| **E6** | The Observer sitting on the floor, looping arrow circling above its head, tired expression | The arrow keeps looping; slumps shoulders |
| **E7** | The Observer writing on a sticky note, then sticking it on a wall, relieved expression | Writes, sticks the note, exhales and relaxes |

## Música
Piano suave o ambient, tranquilo y sin voz. En la biblioteca de audio de YouTube busca *Calma* / *Ambient* / *Piano* sin atribución, o en la biblioteca de TikTok/Instagram "piano calm". Volumen bajo, debajo de la voz.

## Publicación
**Título / primer texto:** La psicología de las personas que ensayan conversaciones en su cabeza 🚿🧠
**Descripción:**
> ¿Tú también ganas discusiones en la regadera? Ensayar conversaciones es una forma de prepararte, ordenar lo que sientes y cuidar tus vínculos. Si se vuelve un círculo que no te deja descansar, hablarlo con alguien ayuda.
> Guion revisado por [Nombre], psicólogo/a · Cédula [XXXX]. Contenido de divulgación, no sustituye una consulta.

**Hashtags:** #psicologia #sobrepensar #ansiedad #saludmental #psicologiamexico
**Comentario fijado:** ¿Con quién fue tu última discusión imaginaria? 👀
**Cierre (para compartir):** "Mándaselo a quien siempre tiene la respuesta perfecta… tres días después."

## Fuente (para el psicólogo revisor)
- Teoría de las *imagined interactions* (Honeycutt): describe sus funciones de **ensayo**, **catarsis** y **mantenimiento de relaciones**, que son la base de los puntos 1–3.
- Rumiación (punto 6): distinguir el repaso útil de la rumiación repetitiva, que se asocia con malestar.
- ✅ El revisor debe confirmar la redacción y la cita antes de publicar.

## Videos derivados de este tema (episodios independientes, sin "Parte 2")
1. **"Por qué siempre se te ocurre la respuesta perfecta… cuando ya te fuiste"** (el *esprit de l'escalier*).
2. **"Qué hacer cuando no puedes dejar de repasar una conversación"** (pieza de técnica, para guardar).
3. **Carrusel de IG:** "3 razones por las que ensayas conversaciones" (los puntos 1–3 en slides).
