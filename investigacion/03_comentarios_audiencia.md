# 03. Qué quiere y qué rechaza la audiencia hispana: análisis de comentarios de YouTube

**Fecha:** 18 de noviembre de 2026 · **Para:** Agenda PSI, canal de divulgación con personaje animado
**Muestra:** 15,627 comentarios (14,109 comentarios principales y 1,518 respuestas) de **121 videos** de **24 canales**. De ellos, 12,961 son comentarios principales en español, y esa es la base de casi todos los porcentajes.
**Leyenda:** [V] = dato medido en la muestra · [I] = inferencia o interpretación.
**Privacidad:** no se guardaron ni se citan nombres de usuario. Los comentarios aparecen parafraseados o en fragmentos breves.

---

## 0. Resumen ejecutivo

1. [V] **El comentario típico en español es de gratitud y vínculo, no de crítica.** El 30% agradece o dice que el video le sirvió. Las críticas explícitas suman menos del 2%: exactitud 0.6%, IA 0.1–0.2%, patologización 0.1%, horóscopo menos de 0.1%. La gente que no está de acuerdo casi no comenta: se va.
2. [V] **Las pocas críticas que aparecen reciben muchos likes.** La queja de que un guion "suena a ChatGPT", por la muletilla "no es esto, sino aquello", es **el comentario #1** del video de La Psicología Invisible sobre la casa limpia (1.7M vistas, 1,300 likes). "Por fin un narrador humano" suma 223 likes. Otra queja contra los guiones redundantes hechos con IA suma 242. Que haya pocas críticas no significa que no haya rechazo: el rechazo es silencioso y, cuando alguien lo pone por escrito, la gente lo respalda.
3. [V] **Lo que más likes acumula no es la psicología, sino lo que la gente hace con ella.** De los 50 comentarios con más likes, unos 19 son humor, memes o citas de cultura pop (Kung Fu Panda, Rick y Morty, Franco de Vita), unos 6 son aforismos sobre el amor, 8 son relatos de infancia o vida, 5 dan ánimo a otros y 4 bromean sobre la miniatura. Además, **45 de los 50 vienen de canales animados o de divulgación** (Sprouts, Psych2Go Español, CuriosaMente, La Psicología Invisible, Sapiencia práctica).
4. [V] **La terapia aparece en el 6% de los comentarios, casi siempre en positivo**, pero con barreras claras: el costo ("no tenemos para una terapia", 834 likes), la familia que no toma en serio el malestar (245 likes), el estigma de que el psicólogo es "para locos" (100 likes), las malas experiencias con terapeutas y no saber qué enfoque elegir. Muchos dicen que un video les ayudó "más que diez años de terapia": el video funciona como **puerta de entrada** y, en algunos casos, como sustituto.
5. [V] **El 5.3% confiesa malestar propio y el 0.67% (87 comentarios) contiene señales de riesgo** (ideación suicida o autolesión). Llegan también menores de edad: "tengo 11 años", "tengo 15", "tengo miedo de contarle a mis papás". Un canal de Agenda PSI necesita un **protocolo de moderación y derivación** antes de publicar el primer video.
6. [V] **Los videos virales y los de bajo rendimiento no generan comentarios muy distintos en contenido** (comparando el promedio por video). Lo que cambia es el **volumen y el tipo de público**. Los videos de bajo rendimiento reciben 10 veces más comentarios por cada mil vistas: es la audiencia núcleo, que pregunta, pide temas y corrige con argumentos técnicos. En los virales, la sección de comentarios se vuelve un muro de confesiones, humor y aforismos que se dirigen más a otros comentaristas que al creador.
7. [V] **Sobre el estilo visual se comenta poco, pero de forma reveladora.** Se elogia el dibujo hecho a mano ("algo difícil de encontrar ahora con la inteligencia artificial"). Se detecta el reciclaje de ilustraciones ajenas: varios comentarios notan que Sapiencia práctica usa dibujos de Psych2Go. Las miniaturas sexualizadas atraen bromas, no confianza. Y la gente siente empatía por el personaje ("me sentí mal por José", 6,500 likes; "pobre muñequita").

---

## 1. Muestra

### 1.1 Diseño
- **Selección por canal, comparando dentro del mismo canal.** Para cada canal se descargó el catálogo de videos largos y Shorts (hasta 200 por pestaña), con 3,851 videos largos con vistas. Se descartaron los 8 videos más recientes, que todavía no maduran, y se filtró por títulos de psicología o salud mental. De lo que quedó se eligieron:
  - **"Viral":** los 2 videos largos y el Short con más vistas del canal.
  - **"Bajo":** 2 videos largos y 1 Short cerca del percentil 10 de vistas del mismo canal. Se evitó el mínimo absoluto para no incluir subidas muertas.
- Se integraron también los 23 videos del análisis previo, todos de nuevo con un tope de 300 comentarios. Los 6 que no encajaban en viral ni bajo quedaron como "medio".
- **Descarga:** `yt-dlp --js-runtimes node --skip-download --write-comments --ignore-no-formats-error --extractor-args "youtube:max_comments=300,all,30,3;comment_sort=top" --sleep-requests 1`, con 2 a 3 flujos secuenciales y reintentos con espera. YouTube devolvió errores 429 y "confirm you're not a bot". Se resolvió con `--ignore-no-formats-error`, porque los comentarios salen igual aunque falle la lectura de formatos.
- Se excluyeron los comentarios del propio creador. 11 videos tenían los comentarios desactivados, entre ellos los 2 más vistos de Chris Núñez (4.6M y 2.4M vistas).

### 1.2 Composición

| Tipo de canal | Videos | Canales |
|---|---|---|
| Animado o divulgación en español | 41 (19 virales, 20 bajos, 2 medios) | La Psicología Invisible, Psych2Go Español, Psicología Animada, Escéptico, Sapiencia práctica, Sprouts Español, CuriosaMente (MX) |
| Psicólogos y psiquiatras hispanos reales | 64 (35 virales, 29 bajos) | Psi Mammoliti, Guillermo Orozco, Fanny Psiquiatra, Psic. Hannah Anda, Mario Guzmán Sescosse, Desansiedad, Píldoras de Psicología, Fernando Leiva, DOCTORA FLOREZ, R&A Psicólogos (CDMX), Psicóloga María Paula, Psiconociendo (Isaac Toiz) |
| Entrevista o charla | 11 | AprendemosJuntos, César Lozano (MX) |
| Animado en inglés (control, solo del análisis previo) | 5 | Psych2Go, The School of Life, Sprouts |

- **Formatos:** 93 videos largos y 28 Shorts.
- **Volumen por grupo:** 13,284 comentarios descargados de videos virales y 1,836 de videos de bajo rendimiento. Los videos de bajo rendimiento tienen pocos comentarios: la mediana es 18 por video, frente a 300 (el tope) en los virales.
- **Idioma de los comentarios:** español 14,246, inglés 554, emojis u otros 826.
- **Mediana de vistas:** 718,692 en los virales y 4,183 en los de bajo rendimiento.

---

## 2. Método de codificación

### 2.1 Libro de códigos
El libro de códigos se definió antes de codificar y se ajustó después de revisar 25 comentarios al azar por código. Funciona con expresiones regulares sobre el texto normalizado (minúsculas y sin acentos). Un comentario puede tener varios códigos. El código completo está en `.../research/comments/scripts/codebook.py`.

| Código | Definición | Precisión estimada* |
|---|---|---|
| IDENT | Se ve reflejado: "me describió", "soy yo", "pensé que era la única" | ~85% |
| CONFESION | Relata un malestar propio: ansiedad, depresión, trauma, duelo, abuso, soledad | ~95% |
| CRISIS | Subconjunto de CONFESION con ideación suicida o autolesión | ~75% (incluye relatos pasados) |
| AYUDA | Pide ayuda o consejo directo para sí o para un familiar | ~90% |
| PIDE_TEMA | Pide un video, tema o segunda parte | ~60% (la lista de temas de la §5 se depuró a mano) |
| GRATITUD | Agradece o dice que le sirvió | ~95% |
| CLARIDAD | Elogia que el tema se explique claro, sencillo o didáctico | ~90% |
| VOZ / VOZ_POS | Menciona la voz o la narración / la elogia | ~70% / ~95% |
| VISUAL | Menciona la animación, el dibujo, la ilustración o los "monitos" | ~85% |
| MINIATURA | Menciona la miniatura | ~100% |
| CRIT_IA | Critica o sospecha uso de IA | Revisado a mano (§6) |
| CRIT_EXACT | Cuestiona el rigor, las fuentes o la evidencia, o señala errores | ~40% automático; revisado a mano (§6) |
| CRIT_PATOLOG | Rechaza la patologización, el autodiagnóstico o la romantización | ~50%; revisado a mano |
| HOROSCOPO | Señala efecto horóscopo o Barnum ("aplica a cualquiera") | Revisado a mano |
| TERAPIA (+ subcódigos POS, NEG, COSTO, MIEDO) | Menciona terapia, psicólogo o psiquiatra | ~85%; subcódigos completados con codificación manual de 120 casos (§4) |
| HUMOR | Risas, memes, emojis de risa | ~75% |
| COMUNIDAD | Se dirige a otros comentaristas ("no estás solo", "a quien lea esto") | ~60% |
| FE | Menciona a Dios, la oración, Jesús | ~85% |
| FAMILIA / PAREJA | Menciona infancia, padres o hijos / pareja, ex o amor | ~90% |
| ELOGIO_GEN | Elogio genérico ("excelente video") | ~95% |
| CRIT_FORMA, HUMANO, VIDEO_COMO_TERAPIA, MUSICA | Duración o clickbait, autenticidad, "video = terapia", música | **Poco fiables** (menos de 40%): no se usan como cifra; se usaron solo para encontrar casos y leerlos a mano |

\*La precisión es el porcentaje de comentarios marcados que de verdad pertenecen al código, estimado leyendo muestras al azar de 25 por código. No se midió la sensibilidad (cuántos casos reales se escapan), así que **los conteos son pisos, no techos**, sobre todo en las críticas, que suelen escribirse con ironía.

### 2.2 Ponderaciones
- **% de comentarios:** cada comentario cuenta 1.
- **% de likes:** la parte de los likes totales que reúnen los comentarios con ese código. Unos pocos comentarios con más de 10,000 likes dominan esta cifra.
- **% ponderado log:** cada comentario pesa log(1 + likes) + 1. Atenúa los valores extremos y es la cifra más estable para medir "lo que la audiencia respalda".
- **Comparación viral vs. bajo:** además de juntar todos los comentarios, se promedió el porcentaje **por video** (videos con 10 o más comentarios en español). Así se evita que los virales, con 300 comentarios cada uno, dominen el resultado.

---

## 3. Resultados generales

### 3.1 Códigos en el total de comentarios principales en español (n = 12,961)

| Código | n | % de comentarios | % de likes | % ponderado log |
|---|---|---|---|---|
| GRATITUD | 3,879 | **29.9** | 7.4 | 26.4 |
| FE | 958 | 7.4 | 6.8 | 8.9 |
| ELOGIO_GEN | 800 | 6.2 | 1.0 | 5.3 |
| TERAPIA | 778 | 6.0 | 4.3 | 6.5 |
| FAMILIA (infancia o padres) | 729 | 5.6 | **10.2** | 7.2 |
| PAREJA | 682 | 5.3 | **11.9** | 6.7 |
| CONFESION | 681 | 5.3 | 5.0 | 6.5 |
| IDENT | 548 | 4.2 | 3.1 | 4.3 |
| HUMOR | 454 | 3.5 | 4.8 | 3.8 |
| COMUNIDAD | 196 | 1.5 | 3.4 | 2.1 |
| CLARIDAD | 171 | 1.3 | 0.2 | 1.1 |
| PIDE_TEMA | 93 | 0.7 | 0.4 | 0.7 |
| CRISIS | 87 | 0.67 | 0.4 | 0.8 |
| VOZ (VOZ_POS) | 79 (43) | 0.6 (0.3) | 0.9 (0.5) | 0.6 (0.3) |
| MINIATURA | 71 | 0.55 | 4.0 | 0.8 |
| VISUAL | 58 | 0.45 | 0.3 | 0.4 |
| AYUDA | 49 | 0.4 | 0.05 | 0.3 |
| CRIT_EXACT (automático) | 79 | 0.6 | 0.2 | 0.6 |
| CRIT_PATOLOG (automático) | 18 | 0.14 | 0.01 | 0.1 |
| CRIT_IA (automático) | 15 | 0.12 | 0.2 | 0.1 |
| HOROSCOPO (automático) | 9 | 0.07 | 0.04 | 0.07 |

**Lectura [I]:**
- La gratitud es el comentario más frecuente, pero tiene pocos likes: la gente la escribe pero no la respalda.
- Lo que **sí respaldan con likes** son las historias de **infancia o padres** (5.6% de los comentarios, 10.2% de los likes) y de **pareja** (5.3% y 11.9%), además del humor, la comunidad y las miniaturas.
- Los temas que mueven a la audiencia son relacionales y biográficos, no clínicos.

### 3.2 Por tipo de canal (% de comentarios principales en español)

| Código | Animado o divulgación (n=5,682) | Psicólogo real (n=6,631) | Entrevista (n=645) |
|---|---|---|---|
| GRATITUD | 14.3 | **42.5** | 38.1 |
| IDENT | **6.1** | 3.0 | 1.2 |
| CONFESION | 4.3 | **6.5** | 0.8 |
| CRISIS | 0.4 | **0.95** | 0 |
| HUMOR | **5.5** | 1.9 | 2.5 |
| FAMILIA | **8.1** | 3.7 | 3.4 |
| PAREJA | 6.2 | 4.6 | 4.2 |
| TERAPIA | 4.1 | **8.1** | 1.2 |
| FE | 5.2 | **9.4** | 6.8 |
| VISUAL + MINIATURA | **2.2** | 0.1 | 0 |
| CRIT_EXACT (automático) | 0.9 | 0.4 | 0.8 |
| CRIT_IA (automático) | 0.23 | 0.03 | 0 |

**Lectura [I]:** son dos tipos de vínculo distintos.
- **Animados:** la gente se identifica, bromea y cuenta su infancia. El video es un espejo y el comentario va hacia otros comentaristas.
- **Psicólogos reales:** la gente agradece, confiesa, pide ayuda y menciona a Dios. El comentario va hacia una persona que siente como "mi psicólogo" ("el mejor psicólogo que he escuchado", "usted es mi psicóloga favorita").

Un personaje animado de Agenda PSI tendrá por defecto la dinámica del espejo. Para generar confianza clínica le hace falta un respaldo humano visible (ver §8).

### 3.3 Shorts vs. videos largos

| Código | Shorts (n=1,366) | Largos (n=11,595) |
|---|---|---|
| GRATITUD | 17.1 | 31.4 |
| IDENT | 2.0 | 4.5 |
| CONFESION | 1.5 | 5.7 |
| HUMOR | **7.8** | 3.0 |
| TERAPIA | 1.5 | 6.5 |
| VISUAL | 1.5 | 0.3 |

[I] Los Shorts reciben reacción rápida (humor, visual); los largos, profundidad (confesión, gratitud, terapia). Las confesiones y las señales de riesgo se concentran en los videos largos: ahí es donde la moderación importa más.

### 3.4 Por canal (% de comentarios principales en español)

| Canal | Tipo | Videos | n | IDENT | CONFES. | GRATIT. | HUMOR | COMUN. | TERAPIA | PIDE | C_EXACT | C_IA | FE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| La Psicología Invisible | animado | 12 | 1,781 | **10.6** | 1.4 | 16.1 | 4.3 | 1.6 | 2.0 | 0.6 | 0.6 | **0.6** | 2.8 |
| CuriosaMente | animado | 5 | 907 | 3.9 | 5.6 | 12.7 | **9.9** | 0.7 | 13.2 | 1.5 | **2.3** | 0.3 | 1.1 |
| Sapiencia práctica | animado | 6 | 802 | 3.4 | 0.8 | 5.7 | 9.0 | 0.6 | 0.5 | 0.8 | 0.4 | 0 | 1.0 |
| Escéptico | animado | 6 | 752 | 3.3 | 2.1 | 21.0 | 2.0 | 2.7 | 1.6 | 0.5 | 0.7 | 0 | 7.3 |
| Sprouts Español | animado | 4 | 558 | 3.9 | 5.9 | 10.6 | 4.5 | 1.2 | 4.5 | 0.2 | 1.1 | 0 | 3.9 |
| Psicología Animada | animado | 6 | 545 | 5.3 | **19.8** | 23.9 | 0.6 | 4.0 | 6.6 | 0.6 | 0 | 0 | **26.6** |
| Psych2Go Español | animado | 2 | 337 | 5.3 | 2.1 | 5.3 | 10.1 | 2.4 | 0.3 | 0.6 | 1.2 | 0 | 0.9 |
| Fernando Leiva | psicólogo | 6 | 791 | 1.9 | 2.0 | 53.1 | 1.1 | 0.4 | 11.8 | 0 | 0.1 | 0 | **24.9** |
| Guillermo Orozco | psicólogo | 6 | 762 | 0.8 | 3.0 | 50.0 | 2.8 | 0.7 | 1.7 | 0.5 | 0.1 | 0 | 3.8 |
| Desansiedad | psicóloga | 6 | 672 | 0.5 | 6.8 | **62.8** | 0.6 | 1.9 | 4.6 | 0.1 | 0 | 0 | 15.8 |
| Fanny Psiquiatra | psiquiatra | 5 | 661 | 0.5 | 4.5 | 18.8 | 1.8 | 0.3 | 9.1 | **3.8** | 0.9 | 0 | 3.5 |
| Psi Mammoliti | psicóloga | 6 | 621 | **10.6** | 6.9 | 35.8 | 3.1 | 1.1 | **19.6** | 0.6 | 0.5 | 0 | 2.1 |
| DOCTORA FLOREZ | psicóloga | 6 | 615 | 4.5 | 4.1 | 53.8 | 0.5 | 1.5 | 4.2 | 0.5 | 0.3 | 0.2 | 12.8 |
| Píldoras de Psicología | psicólogo | 5 | 571 | 2.6 | **16.1** | 28.7 | 1.8 | **6.5** | 8.1 | 0.9 | 0.3 | 0 | 11.0 |
| Psic. Hannah Anda | psicóloga | 5 | 557 | 3.8 | 2.1 | 46.5 | 2.9 | 0.7 | 3.8 | 0.5 | 0 | 0 | 3.2 |
| Mario Guzmán Sescosse | psicólogo | 6 | 534 | 1.1 | 2.8 | **63.9** | 0.4 | 0.6 | 13.1 | 0.9 | 0.8 | 0 | 5.8 |
| R&A Psicólogos (CDMX) | clínica | 3 | 529 | 5.1 | **23.8** | 21.7 | 0.8 | 2.5 | 7.8 | 0 | 0.6 | 0 | 10.2 |
| Psiconociendo | psicólogo | 5 | 234 | 1.7 | 0.4 | 11.1 | 9.0 | 0.4 | 0.8 | 0 | 0.8 | 0.4 | 3.0 |
| Psicóloga María Paula | psicóloga | 5 | 84 | 2.4 | 1.2 | 19.1 | 2.4 | 0 | 14.3 | 0 | 1.2 | 0 | 1.2 |
| AprendemosJuntos | entrevista | 5 | 446 | 0.9 | 0 | 42.6 | 1.4 | 0.5 | 1.6 | 0.5 | 0.7 | 0 | 3.4 |
| César Lozano | entrevista | 6 | 199 | 2.0 | 2.5 | 28.1 | 5.0 | 0 | 0.5 | 0 | 1.0 | 0 | 14.6 |

**Patrones [I]:**
- **Identificación:** La Psicología Invisible y Psi Mammoliti la disparan. En los dos casos se describe un rasgo o una herida concreta ("personas que…", "la herida del rechazo").
- **Confesión:** Psicología Animada (síntomas de ansiedad y depresión), R&A (síntomas de depresión) y Píldoras la disparan. **Los listados de síntomas atraen a personas que sufren.**
- **Peticiones:** Fanny Psiquiatra recibe muchas (suplementos, análisis de famosos de *reality*). La audiencia pide justo lo que es riesgoso: remedios "naturales" y diagnósticos a distancia.
- **Críticas de rigor:** CuriosaMente las concentra, sobre todo en su video de bajo rendimiento "¿Cuál es la mejor terapia para ti?", donde varios psicólogos corrigen la clasificación de las terapias. Las audiencias de divulgación científica **sí** auditan.
- **Fe:** aparece en 1 de cada 4 comentarios en Fernando Leiva y Psicología Animada. Es parte central del marco con el que la audiencia latinoamericana entiende su malestar.

---

## 4. Terapia y psicólogos: qué dicen y qué barreras mencionan

[V] 778 comentarios principales en español (6.0%) y 857 contando respuestas mencionan terapia, psicólogo o psiquiatra. En una muestra aleatoria de 120 se codificó a mano lo siguiente (las categorías se superponen):

| Qué hace el comentario | % aprox. (n=120) |
|---|---|
| Debate sobre tipos de terapia o evidencia (concentrado en CuriosaMente) | ~10% |
| Cuenta que está o estuvo en terapia y le ayuda o le ayudó | ~12% |
| Llama "psicólogo" al creador como trato o en agradecimiento ("gracias, psicólogo") | ~7% |
| Mala experiencia: no le sirvió, cambió de terapeuta, terapeuta "frío" | ~7.5% |
| Compara el video con la terapia o lo usa como sustituto ("gracias por la terapia") | ~7.5% |
| Es un profesional de la salud mental que comenta ("soy psicóloga…") | ~7% |
| Recomienda terapia o psiquiatra a otros | ~5% |
| Pide atención al creador ("¿das terapia por Zoom?", "¿dónde me inscribo?") | ~4% |
| Duda sobre límites con el terapeuta (escribirle, seguirlo en redes) | ~3% |
| Costo o acceso | ~3% |
| Miedo, estigma o familia que no apoya | ~3% |
| Dudas de medicación o suplementos | ~3% |
| Uso metafórico ("mi terapia es limpiar", "mi terapia es Dios") | ~8% |

### Barreras, con los ejemplos más respaldados (parafraseados)
- **Costo:**
  - "Gracias por ayudar a quienes no tenemos para una terapia" (834 likes, video de meditación de Guillermo Orozco).
  - "Todos dicen 'busca terapia'… ¿consultas de 20,000 pesos? ¿Quién puede pagar eso durante años?" (35).
  - "Gasté 2,400 € en un año de psicólogo y estoy igual."
  - "Dejé la terapia por problemas económicos."
  - "Gracias a los que no tenemos recursos para una sesión."
- **Familia:**
  - "Le pedí a mi mamá que me llevara al psicólogo, no me tomó en serio y ahora me da vergüenza insistir" (245).
  - "Mi madre dice que solo soy de mente débil y que me quite la flojera."
  - Menores que dicen tener "todos los síntomas" y miedo de contarles a sus papás.
- **Estigma:**
  - "Todavía hay gente que teme ir al psicólogo porque dicen que es para locos" (100).
  - Comentarios que lo refuerzan: "deben ir a terapia, están mal de la cabeza".
- **Mal ajuste o mala experiencia:**
  - "He probado con dos psicólogos y dos psiquiatras y salgo peor."
  - "Tres psicólogas, tres diagnósticos distintos."
  - "Hablar con un psicólogo es como hablarle a una pared."
  - "Pasé 3 años con una terapeuta que se decía cognitivo-conductual, pero nunca me dejó tareas" (46).
  - "Me siento como un signo de pesos con mis terapias" (45).
- **No saber qué enfoque elegir:** el video de CuriosaMente sobre "la mejor terapia" generó debate y confusión (TCC, ACT, psicoanálisis, EMDR).

### Lo que la gente valora (la oportunidad)
- **La terapia funciona cuando se encuentra:**
  - "Estuve 3 años en cognitivo-conductual y hoy me siento otra persona" (261).
  - "La terapia sí funciona, solo hay que encontrar el tipo correcto" (140).
  - "Si se sienten identificados y les hace llorar, les recomiendo terapia" (1,500, Sprouts).
- **El video como complemento o puerta de entrada:**
  - "Estos videos no sustituyen la terapia, pero los puedes ver las veces que quieras" (561).
  - "Hablaba con mi psicólogo de tus videos."
  - "Mi psicóloga me recomendó mindfulness y probé tu meditación" (292).
- **El video como sustituto (riesgo y señal de demanda insatisfecha):**
  - "Este video me ayudó más que diez años de terapia" (95).
  - "Ni dos meses de terapia me abrieron tanto los ojos" (101).
  - "Haga de cuenta que estuve en terapia" (74).
- **La evidencia se aprecia en los canales técnicos:** "Esto es psicología basada en la evidencia" (401, Mario Guzmán).

**Implicación para Agenda PSI [I]:** el producto de Agenda PSI responde justo a estas barreras: precio, encontrar al terapeuta adecuado y perderle el miedo a la primera sesión. Los videos deberían **nombrar las barreras de forma explícita**: qué pasa en una primera sesión, cómo saber si un psicólogo es bueno o no te queda, cuánto cuesta y qué opciones hay en México (IMSS, universidades, opciones de bajo costo), cómo hablarlo con tus papás. Conviene hacerlo sin un llamado comercial agresivo: la audiencia castiga la sensación de "vender" ("me siento un signo de pesos").

---

## 5. Temas que la gente pide de forma explícita

Lista depurada a mano a partir de 98 candidatos. Entre paréntesis, los likes más altos o la frecuencia.

**Salud mental y clínica**
- TDAH: diferencias con el autismo (16), TDAH en adultos (13).
- Autismo en mujeres adultas; Asperger en adultos.
- TOC y esquizofrenia "a profundidad" (12); cómo ser pareja de alguien con TOC.
- Segunda parte sobre depresión (16); ansiedad crónica por trauma; estrés ("estoy en una situación límite").
- Trastorno límite de la personalidad y trastorno de personalidad evitativa.
- Rumiación, mal humor, pensamiento negativo; sentirse estancado; indecisión crónica; procrastinación.
- Prosopagnosia; alta sensibilidad (PAS).

**Relaciones**
- Apego evitativo (cómo se forma, qué heridas se relacionan).
- Abandono o "descarte" abrupto; aprender a estar solo.
- Las víctimas del narcisista, no solo el narcisista.
- Cómo actúa una persona que **no** tiene la herida (un modelo sano, no solo el patológico).
- Poner límites (17).

**Familia y ciclo de vida**
- No repetir a los padres.
- Efectos psicológicos de cuidar a un padre o madre mayor.
- Divorcio con hijos.

**Herramientas prácticas**
- Respiración: "dicen que respiramos mal pero no dicen cómo" (9).
- Técnicas concretas de TCC; segunda parte de la meditación guiada.

**Sociedad y tecnología**
- Redes sociales y atención (18).

**Pseudociencia y criterio**
- Segunda parte sobre pseudoterapias como las constelaciones familiares (62, el pedido más respaldado).
- ¿Funciona el *coaching* de vida?
- Terapia ocupacional.

**Pedidos riesgosos (atender con cuidado o no atender)**
- Análisis de personalidad de participantes de *reality* (La Casa de los Famosos: Adrián Marcelo, Arath, Gala, Ricardo) e *influencers*.
- Suplementos y plantas "naturales" (GABA, ashwagandha, rodiola, maca, magnesio, sacha inchi, cannabis medicinal), incluso combinados con antidepresivos o levotiroxina.

[I] Hay demanda de contenido **práctico ("¿cómo, paso a paso?")** y de **criterio contra la pseudociencia**. Esto encaja con el respaldo a lo basado en evidencia y con la sorpresa ante terapeutas sin método. En cambio, los análisis de famosos generan alcance (el video de Fanny sobre Adrián Marcelo tuvo 135K vistas) pero también rechazo ético: "que los profesionales de la salud mental hagan esto ya debería ser cancelado". Para una marca de salud no conviene diagnosticar a personas reales a distancia.

---

## 6. Críticas: IA, exactitud, patologización y efecto horóscopo (revisión manual)

### 6.1 IA (revisión manual de todas las menciones, 35 candidatos)
- [V] **10 comentarios en español critican el uso de IA**. Suman unos **1,570 likes** y casi todos están en videos virales de La Psicología Invisible:
  - #1 del video de la casa limpia (1,300 likes): la información está bien, pero ¿por qué los guiones de IA repiten todo el tiempo "no es esto, sino aquello"?
  - "Estoy agotada de los guiones hechos con IA en todas las plataformas, son taaan redundantes" (242).
  - "¿Usas IA en el guion? Es muy 'chatgpt coded' decir tanto 'no es X, es Y'" (15).
  - Acusación de copiar el guion de un canal en inglés, relocutarlo con un micrófono barato y rellenar con animaciones de IA (6).
  - "Qué lástima, el video está hecho con IA" (4).
  - "Odio poder identificar cuando sacan un texto de ChatGPT" (3).
  - "Cuidado con la animación IA" (1), y otros.
- [V] **5 comentarios valoran que el contenido NO sea IA:**
  - "De los pocos canales que no usan la IA mal" (32, CuriosaMente).
  - "Por fin un narrador humano" (223, contado en VOZ).
  - "Qué bella animación, me encanta ver un video real, no IA."
  - "Los dibujos son excelentes, algo difícil de encontrar ahora con la IA."
  - "Qué placer que la voz no sea IA."
- [V] En el control en inglés (Psych2Go) aparece el mismo patrón: "ojalá no sea una de esas locuciones con IA".
- [I] **El detector de la audiencia es lingüístico antes que visual:** muletillas ("no es X, es Y"), redundancia, frases vacías. Para Agenda PSI, el guion debe pasar un filtro anti-muletillas de IA, aunque se use IA para producir.

### 6.2 Exactitud y rigor (revisión manual de 79 candidatos automáticos más búsqueda amplia)
- [V] Unas **20 críticas genuinas de rigor**. El 60% está en el video de bajo rendimiento de CuriosaMente "¿Cuál es la mejor terapia para ti?", con psicólogos que corrigen:
  - "Otro error: ACT y DBT no se desprenden de la TCC, son terapias contextuales" (22).
  - "Es el video más irresponsable del canal: presenta las terapias como ropa que te queda o no."
  - "Recomendar la psicodinámica hoy es como recomendar horóscopos."
- [V] Otras críticas:
  - Fechas generacionales mal (La Psicología Invisible, Xennials).
  - "Se basan en una sola persona cuando hay otros estudios" (Psych2Go Español).
  - Pedido de fuentes (Fanny).
  - "No estoy de acuerdo con que tengamos el control en los genes" (César Lozano).
- [V] También se **elogia el rigor:** "psicología basada en la evidencia seria" (401), "gracias por ser un contrapeso contra miles de canales desinformativos" (8).
- [I] El público que audita es pequeño, pero tiene autoridad: hay muchos psicólogos y estudiantes comentando (~7% de las menciones a terapia). Un error técnico en un canal de Agenda PSI no lo marcaría la masa; lo marcarían colegas, justo el público de profesionales que la plataforma necesita atraer.

### 6.3 Patologización y efecto horóscopo
- [V] **Unas 10 críticas de patologización o romantización:**
  - "Hoy se romantizan estas cosas, incluida la depresión" (5).
  - "Con esas características todo el mundo es narcisista; aquí todos se victimizan de que su ex es narcisista" (5).
  - "Ahora resulta que nunca he estado enamorada y llevo 45 años casada" (2).
  - "Estos videos son súper romantizados."
- [V] **Celebran el mensaje de no autodiagnosticarse:** "¡POR FIN alguien que dice que no se autodiagnostiquen!" y "Me encantó el último mensaje: no se autodiagnostiquen" (18). Varios comentaristas se protegen solos: "no quiero autodiagnosticarme, pero…".
- [V] **Unos 6 comentarios señalan efecto horóscopo o Barnum:**
  - El #44 del top 50 (2,900 likes, La Psicología Invisible): "Muchos se sienten identificados, pero la mayoría no es así: solo son introvertidos o buscan atención."
  - "Cambien 'inteligente' por cualquier adjetivo, es solo un gancho para que nos sintamos identificados."
  - "Esto es el efecto Forer."
  - "Aquí está tu horóscopo de cabecera."
  - Humor que desmiente el video: "los esconde tan bien que no coincide con nada del video" (4,100).
- [I] **Las dos caras de la identificación.** La identificación es el motor de La Psicología Invisible (10.6% de sus comentarios) y también su punto débil: cuando la descripción es tan amplia que le queda a cualquiera, la parte más crítica de la audiencia lo nota y recibe mucho respaldo. La fórmula que funciona es la identificación con un rasgo específico y no clínico, y nunca un "si haces X tienes Y".

---

## 7. Personaje, estilo visual, voz y música

- [V] **Las menciones visuales son pocas:** 0.45% de VISUAL y 0.55% de MINIATURA. Casi todas están en canales animados (2.2% de sus comentarios).
- **Lo que se elogia:**
  - Dibujos a mano y estilo propio: "me encanta el estilo de los dibujos", "¿cómo se llama ese estilo?", "están padrísimos los monitos", "qué buen montaje: acompaña al tema como un guante".
  - Expresividad: "las animaciones son muy expresivas".
  - Que lo visual ayude a entender: "los dibujos fueron geniales para comprender mejor", "muy didáctico con dibujos".
  - Preguntas de "¿con qué app lo haces?".
- **Empatía con el personaje:**
  - "Me sentí mal por José" (6,500 likes, Sprouts, efecto Pigmalión).
  - "Pobre muñequita" (Psicología Animada).
  - "Sufrí solo de ver a la muñequita" (alguien con ansiedad que se vio reflejada).
  - [I] **Un personaje con nombre y una historia que la audiencia puede seguir genera más apego que un ícono genérico.**
- **Lo que se detecta y castiga:**
  - Ilustraciones recicladas: en Sapiencia práctica varios notan que "los dibujos son de Psych2Go".
  - Miniaturas sexualizadas en Sapiencia práctica (4 de los 50 comentarios con más likes). Generan bromas y alcance, no confianza.
  - Animación de IA con errores ("le nació la confianza en el pecho, cuidado con la animación IA").
  - Edición recargada: "lástima de los efectos de edición, que distraen y cansan".
- **Voz:**
  - Es el atributo **más elogiado** en relación con la forma: VOZ_POS se dirige a la calma ("su voz es tan relajante", 2,700; "tu voz transmite calma"; "su voz transmite paz y confianza para que un paciente se abra", 58).
  - Se pide un ritmo pausado: "me pareció acelerada la narración, me gustaría más pausada".
  - Se valora que sea humana ("por fin un narrador humano", 223).
  - Hay detección de clonación: un comentario avisa que circulan videos con la voz de una divulgadora clonada.
- **Música:** casi no se menciona (2 comentarios específicos). [I] No es un factor de diferenciación; basta con que no estorbe.

---

## 8. Virales vs. bajo rendimiento: qué cambia

### 8.1 Volumen y relación con el público
| Métrica (mediana por video) | Viral (n=60) | Bajo (n=55) |
|---|---|---|
| Vistas | 718,692 | 4,183 |
| Comentarios por cada 1,000 vistas | 0.26 | **2.47** |
| Likes por cada 1,000 vistas | 35.4 | **57.7** |
| Largo del comentario (caracteres) | 97 | 86 |

[V] Los videos de bajo rendimiento los ve sobre todo la **audiencia núcleo**, que comenta e interactúa 10 veces más por vista. Los virales llegan a un público de paso.

### 8.2 Contenido (promedio por video, videos con 10 o más comentarios en español; 58 virales y 28 bajos)
| Código | Viral | Bajo | Diferencia |
|---|---|---|---|
| GRATITUD | 29.9% | 22.6% | ↑ viral |
| FE | 7.4% | 3.9% | ↑ viral |
| FAMILIA | 5.0% | 3.3% | ↑ viral |
| IDENT | 3.5% | 2.6% | ↑ viral |
| CLARIDAD | 1.4% | 0.7% | ↑ viral |
| TERAPIA | 4.9% | **10.3%** | ↑ bajo (temas técnicos) |
| PIDE_TEMA | 0.5% | **1.2%** | ↑ bajo |
| AYUDA | 0.4% | 0.7% | ↑ bajo |
| HUMOR | 3.8% | 4.9% | ≈ |
| CONFESION | 4.3% | 4.7% | ≈ |
| CRIT_EXACT | 0.55% | 0.74% | ≈ (en animados, 3.4% en bajos frente a 0.55% en virales) |

### 8.3 Patrones cualitativos
1. **Los videos de bajo rendimiento son técnicos o "de nicho de profesión":**
   - Temas: "¿seguir a tu psicólogo en Instagram?", "escribir al psicólogo de urgencia", estoicismo, SPES escolares, efectos de las pantallas, valores.
   - Reacción: preguntas, debate entre colegas y peticiones de temas.
   - En los animados, los videos de bajo rendimiento sobre **la propia psicología** ("pseudoterapias", "mejor terapia") atraen correcciones técnicas.
2. **Los virales tocan una vivencia universal con un ángulo de identidad:**
   - Amor ("nunca estuviste enamorado"), infancia y crianza (apego, Pigmalión), rasgos cotidianos (cumpleaños, casa limpia, arreglarlo todo), procrastinación (Da Vinci) y síntomas de ansiedad o depresión.
   - Reacción: humor, aforismos, confesiones dirigidas a otros y fe.
   - La sección de comentarios se convierte en comunidad: "leyendo los comentarios me di cuenta de que todos estamos rotos" (3,600).
3. **Las miniaturas y los títulos llevan el alcance:**
   - En Sapiencia práctica, el video más visto se comenta sobre todo por la miniatura.
   - En los catálogos (3,851 videos, vistas en relación con la mediana del canal), los títulos con "narcisista" rinden **1.41 veces** la mediana; con ansiedad o depresión, 1.29; con "señales" o "síntomas", 1.23; con emoji, 1.18.
   - Los títulos "La psicología de las personas que…" rinden **0.68 veces**: el formato está saturado dentro de los canales que lo usan.
   - Los títulos de infancia o padres rinden 0.70 dentro de su canal, aunque Sprouts haga viral el apego. [I] El efecto depende de la ejecución.
   - **Advertencia:** muchos títulos venían traducidos automáticamente al inglés. Es una correlación descriptiva, no causal.
4. **La crítica se mueve con el nivel de exposición.** En los virales de La Psicología Invisible, la crítica a la IA llega al #1. En los de bajo rendimiento de CuriosaMente aparece la crítica técnica de colegas. [I] Con poca audiencia te audita el núcleo experto; con mucha, te audita la masa sensible al "olor a IA".

---

## 9. Los 50 comentarios con más likes (comentarios principales en español, parafraseados)

| # | Likes | Canal (video) | Paráfrasis | Tipo |
|---|---|---|---|---|
| 1 | 31,000 | Psych2Go Español (nunca estuviste enamorado) | Se da cuenta de que nunca estuvo enamorada y aun así lloró por esa persona (con emojis de payaso) | Humor autoirónico |
| 2 | 27,000 | Sprouts (efecto Pigmalión) | Cita al papá de Po en *Kung Fu Panda*: para que algo sea especial hay que creer que lo es | Cultura pop |
| 3 | 20,000 | Psych2Go Español | Aforismo: si te gusta una flor la arrancas; si la amas, la riegas | Aforismo |
| 4 | 20,000 | CuriosaMente (Da Vinci, procrastinación) | Meme: "Nadie: / Yo explicándole al profe por qué entregué la tarea un mes tarde" | Humor |
| 5 | 15,000 | Sprouts (apego) | De niño era alegre y sociable; en la adolescencia se volvió callado y no se reconoce | Relato personal |
| 6 | 9,200 | La Psicología Invisible (cumpleaños) | Lo único que le cambia el ánimo es el día de pago | Humor |
| 7 | 9,200 | CuriosaMente | Da Vinci, el inventor del "ahorita" | Humor mexicano |
| 8 | 7,700 | Sapiencia práctica | Elogio pícaro a la miniatura | Miniatura |
| 9 | 7,100 | Psych2Go Español | El amor es como un gas: si lo fuerzas, sale mal (escatológico) | Humor o aforismo |
| 10 | 7,100 | Psych2Go Español | A veces confundimos el amor con la costumbre | Aforismo |
| 11 | 6,800 | Sprouts (apego) | Prepárense antes de ser padres o solo crearán gente ansiosa como yo, jaja | Crianza y autoironía |
| 12 | 6,700 | Psych2Go Español | El amor no se encuentra, se construye | Aforismo |
| 13 | 6,500 | Psych2Go Español | Editó el comentario para que nadie sepa qué pasó (meta-broma) | Humor |
| 14 | 6,500 | Sprouts (Pigmalión) | Se sintió mal por José, el personaje | Empatía con el personaje |
| 15 | 6,400 | La Psicología Invisible (cumpleaños) | A algunos simplemente nos da igual, sin drama | Identificación |
| 16 | 6,100 | Sprouts | Cita de anime: el esfuerzo es inútil si no crees en ti | Cultura pop |
| 17 | 6,000 | Sprouts (apego) | Lo crió una tía frustrada y su madre lo golpeaba por todo | Confesión de infancia |
| 18 | 5,900 | Hannah Anda (procrastinación) | ¿Soy la única dudando entre verlo ahora o dejarlo para después? | Humor e identificación |
| 19 | 5,800 | Sprouts | Tener un hijo no es bendición ni castigo: es responsabilidad | Opinión sobre crianza |
| 20 | 5,700 | Sprouts (Pigmalión) | Los profesores encasillan a los alumnos por su apariencia | Experiencia escolar |
| 21 | 5,600 | CuriosaMente (TDAH) | Buena alumna sin esfuerzo que se desmoronó en la universidad; diagnóstico y psiquiatra | Relato de diagnóstico |
| 22 | 5,300 | Sapiencia práctica | Meme sobre la miniatura | Miniatura |
| 23 | 5,200 | Sprouts | Cita de Kamina (*Gurren Lagann*): cree en mí, que creo en ti | Cultura pop |
| 24 | 5,200 | Píldoras de Psicología (ansiedad) | Superó los ataques de pánico viendo videos; ánimo a quien sufre (con fe) | Testimonio de esperanza |
| 25 | 5,000 | CuriosaMente | Hasta este Short debió subirse hace dos semanas | Humor |
| 26 | 4,500 | Sprouts | Nunca digan a un niño que es tonto o feo | Crianza |
| 27 | 4,200 | Sprouts | Una docente dejó de interesarse en él cuando bajó su rendimiento | Experiencia |
| 28 | 4,100 | Sapiencia práctica (señales de que esconde sentimientos) | "Los esconde tan bien que no coincide con nada del video" | Humor anti-horóscopo |
| 29 | 3,900 | Desansiedad | Superó la ansiedad; tú también puedes | Testimonio de esperanza |
| 30 | 3,800 | Sapiencia práctica | Top 3 razones por las que el video es el mejor: la #1 es la miniatura | Miniatura |
| 31 | 3,600 | Psych2Go Español | No fue enamoramiento, fue dependencia emocional | Re-etiquetado |
| 32 | 3,600 | Psych2Go Español | Cita de *Rick y Morty* sobre el amor incondicional | Cultura pop |
| 33 | 3,600 | Sapiencia práctica | Broma sobre la miniatura | Miniatura |
| 34 | 3,600 | Sprouts | Leyendo los comentarios: todos estamos rotos; vendrán días mejores | Comunidad |
| 35 | 3,500 | CuriosaMente | Tengo algo en común con Leonardo da Vinci | Humor |
| 36 | 3,500 | Sprouts | Cita de Franco de Vita: "no basta con traerlos al mundo" | Cultura pop (canción) |
| 37 | 3,400 | Psych2Go Español | YouTube me lo recomienda meses después de haber llorado | Humor (algoritmo) |
| 38 | 3,400 | Psicología Animada (ansiedad) | En las crisis alaba a Dios y le ha servido | Fe |
| 39 | 3,300 | Psych2Go Español | Yo, sin pareja: "lo voy a ver" | Humor |
| 40 | 3,300 | La Psicología Invisible (cumpleaños) | No lo celebra, odia ser el centro, cree que es protección | Identificación |
| 41 | 3,200 | CuriosaMente | "Da Vinci, hermano mío" | Humor |
| 42 | 3,000 | Psych2Go Español | El enamoramiento vive de la ilusión; el amor sobrevive a la realidad | Aforismo |
| 43 | 3,000 | Sprouts | Le duele pensar en cómo se está criando a los niños | Crianza |
| 44 | 2,900 | La Psicología Invisible (muy conscientes) | Muchos se identifican, pero la mayoría no es así: son introvertidos o buscan atención | **Crítica Barnum** |
| 45 | 2,900 | Píldoras de Psicología | Fuerza para todos los que nos sentimos así | Comunidad |
| 46 | 2,700 | Psych2Go Español | Todos hablando de que nunca los amaron… pero qué voz tan relajante | **Voz** |
| 47 | 2,500 | Psych2Go Español | Sus padres peleaban y hoy, tras 20 años, son inseparables | Relato familiar |
| 48 | 2,500 | Desansiedad | Tiene pánico y TAG, 3 años con psiquiatra y psicóloga, los ejercicios le ayudan y confía en que Dios la libere | **Terapia y fe** |
| 49 | 2,400 | Psych2Go Español | No ilusionen a alguien para luego romperle el corazón | Moraleja |
| 50 | 2,400 | La Psicología Invisible (Xennials) | ¿Recuerdan calcar mapas? Mis hijos no conocen el papel calca | Nostalgia y humor |

**Qué revelan [I]:**
1. **La audiencia premia al que resume o reinterpreta el video con gracia.** El "comentario estrella" es una frase memorable, un meme o una cita pop. Un video que entrega una frase citable y un momento de humor le da a la audiencia el material para que el video circule.
2. **El amor y la crianza dominan:** Psych2Go Español con "nunca estuviste enamorado" y Sprouts con apego y Pigmalión suman 28 de los 50.
3. **La vulnerabilidad recibe respaldo cuando se comparte en clave de esperanza** ("lo superé, tú también puedes"), no de desesperación.
4. **Los 5 comentarios de canales de psicólogos reales** son testimonios o comunidad. Ninguno es humor ni cultura pop: ahí el registro es más serio.
5. **Las críticas (#44) y la voz (#46) también llegan al top.**

---

## 10. Señales de riesgo y moderación

- [V] **87 comentarios (0.67%)** mencionan ideación suicida, intentos o autolesión. La mayoría están en canales de psicólogos y en videos sobre depresión y síntomas. Hay que sumar los pedidos de ayuda directos ("ayúdenme por favor", "¿a qué correo puedo contactar?", "necesito ayuda pero nadie me entiende").
- [V] Hay menores que se autodiagnostican ("tengo 11 años y tengo todos los síntomas") y personas que preguntan por combinar medicamentos con suplementos.
- [V] En los comentarios virales, la comunidad responde con contención ("no estás solo", "vendrán días mejores"). En los de bajo rendimiento, muchas veces nadie responde.
- **Recomendación [I]:**
  - Tener un **protocolo** antes del lanzamiento: palabras clave de alerta, una respuesta fijada con la Línea de la Vida (800 911 2000) y el 911, un horario de revisión y quién escala cada caso.
  - Mantener un comentario fijado con recursos en los videos sobre depresión, ansiedad o duelo.
  - No responder con diagnósticos.
  - Ofrecer un siguiente paso concreto: cómo agendar en Agenda PSI y opciones de bajo costo.

---

## 11. Implicaciones accionables para el canal de Agenda PSI

1. **Identificación específica, no horóscopo.** Hay que describir rasgos cotidianos y concretos (cumpleaños, casa limpia, arreglarlo todo) y explicar el porqué con un mecanismo. Conviene incluir siempre una línea de "esto no es un diagnóstico" o de "si esto te afecta en X áreas, vale la pena hablarlo con alguien". La audiencia celebra ese mensaje.
2. **Guion humano y sin muletillas de IA.** Hay que prohibir el "no es X, es Y" repetido, los listados vacíos y las conclusiones genéricas. Una prueba de lectura con personas reales antes de publicar ayuda a detectarlos. La voz debe ser humana, cálida y pausada, porque es el atributo formal más elogiado.
3. **Un personaje con nombre e historia.** "Me sentí mal por José" demuestra que un personaje con historia genera empatía. El dibujo debe ser propio y coherente (nunca reciclado), con expresividad y sin efectos recargados. Las miniaturas deben ser sugerentes por la emoción, no por lo sexual.
4. **Dejarle a la audiencia una frase citable y un momento de humor** por video. Es lo que convierte comentarios en likes y alcance.
5. **Ejes temáticos con demanda demostrada:**
   - Amor y apego (incluido "no fue amor, fue dependencia").
   - Infancia y crianza ("no repetir a mis padres").
   - Procrastinación con humor mexicano ("el ahorita").
   - Narcisismo desde la víctima, no desde la caricatura.
   - TDAH y autismo en adultos y en mujeres.
   - Herramientas prácticas paso a paso (respiración, rumiación, límites).
   - Pseudoterapias y "cómo elegir terapeuta".
   - **Desmitificar la terapia:** qué pasa en la primera sesión, cuánto cuesta en México, cómo saber si tu psicólogo te sirve, cómo decírselo a tus papás. Es el puente natural hacia el producto de Agenda PSI.
6. **Respaldo profesional visible** (psicólogo o psicóloga revisora con nombre, citas breves). Da la confianza clínica que el personaje animado por sí solo no genera (§3.2) y protege frente al público de colegas que audita (§6.2).
7. **Respetar la fe** sin promoverla ni burlarse. Hasta 1 de cada 4 comentarios en algunos canales la menciona como recurso de afrontamiento.
8. **No hacer** análisis de famosos a distancia ni recomendaciones de suplementos o medicamentos.
9. **Medir el éxito con dos tableros.** Uno para lo viral: alcance, humor, identificación, comunidad. Otro para el núcleo: preguntas, pedidos, correcciones técnicas. Los videos de "bajo rendimiento" son donde se gana la credibilidad con colegas y donde la audiencia pide los próximos temas.

---

## 12. Limitaciones

- **Sesgo de orden en la descarga.** En los virales se descargaron los 300 comentarios "top" (los más votados de miles); en los de bajo rendimiento, prácticamente todos. Comparar los porcentajes juntando todos los comentarios mezcla ese efecto, por eso se agregó el promedio por video (§8.2). Aun así, los virales describen "lo que la audiencia respalda" y los de bajo rendimiento, "lo que la audiencia escribe".
- **Se ve solo a quien comenta.** Quien rechaza un video casi no comenta: se va. Las tasas de crítica subestiman el rechazo real, y la retención y las vistas son mejores medidas del rechazo.
- **Codificación automática con validación limitada.** Las regex se validaron leyendo unos 25 comentarios por código y con revisión manual completa de las críticas (IA, exactitud, patologización, horóscopo), de las peticiones de temas y de 120 menciones a terapia. No hubo doble codificador ni medición de sensibilidad. Los códigos CRIT_FORMA, HUMANO, VIDEO_COMO_TERAPIA y MUSICA se descartaron como cifra por su baja precisión.
- **Composición de la muestra.**
  - Hay más psicólogos de Argentina, España y Colombia que de México. De México están CuriosaMente, R&A Psicólogos, César Lozano y quizá otros sin verificar. No se identificó el país de los comentaristas, aunque hay huellas mexicanas frecuentes ("ahorita", "padrísimo", "monitos", menciones a Monterrey y CDMX) junto a argentinas, chilenas y españolas.
  - Algunos videos "bajo" de canales de psicólogos tratan temas laterales, y 11 videos tenían los comentarios desactivados.
  - El control en inglés es pequeño (5 videos).
- **Fechas mezcladas.** Los videos van de 2019 a 2026. Los de bajo rendimiento suelen ser más recientes o más de nicho, y las normas sobre la IA cambiaron mucho en 2025–2026: la crítica a la IA solo aparece en los videos de 2026.
- **Títulos traducidos.** Muchos títulos de los catálogos venían traducidos automáticamente al inglés, lo que introduce ruido en el análisis de títulos (§8.3).
- **Likes.** Los likes son acumulativos y dependen de la antigüedad y de la exposición del comentario. Las cifras "k" de YouTube son aproximadas.

---

## 13. Archivos

Todo está en `/tmp/claude-0/-home-user-Creador-de-videos-Para-redes-/f6e80049-54f1-5e5b-b0dd-1d5ea884d7d2/scratchpad/research/comments/`.

| Archivo o carpeta | Contenido |
|---|---|
| `raw/` | JSON crudos de yt-dlp por video (`<id>.info.json`) |
| `channels/` | Catálogos de cada canal |
| `seleccion_videos.tsv` | Diseño de la muestra viral vs. bajo |
| `videos_meta.json` | Metadatos de cada video |
| `comentarios_codificados.csv` | 15,627 comentarios con sus códigos, **sin autores** |
| `tablas/` | `codigos_*.csv`: totales, por tipo, por canal, por formato, viral vs. bajo, respuestas; `viral_vs_bajo_promedio_por_video.csv`; `videos.csv` |
| `top50_likes.txt`, `pedidos_tema.txt`, `menciones_terapia.txt`, `menciones_visual.txt`, `menciones_voz.txt`, `criticas_*.txt`, `horoscopo.txt`, `crisis.txt`, `pedidos_ayuda.txt` | Listados ordenados por likes para revisar a mano |
| `muestras_validacion.txt` | Muestras de validación del libro de códigos |
| `scripts/` | `codebook.py`, `analyze.py`, `select.py`, `dl_comments.sh` (reproducibles) |
