# 07 · Qué ha funcionado y qué no en psicología en español: TikTok e Instagram con datos reales (Apify)

**Proyecto:** canal de divulgación con personaje animado de Agenda PSI (agendapsi.mx)
**Fecha de extracción:** 18-nov-2026
**Fuente:** Apify (cuenta FREE), con los actores `clockworks/tiktok-scraper`, `clockworks/tiktok-comments-scraper`, `apify/instagram-scraper` y `apify/instagram-comment-scraper`.
**Datos crudos (JSON/CSV):** `/tmp/claude-0/-home-user-Creador-de-videos-Para-redes-/f6e80049-54f1-5e5b-b0dd-1d5ea884d7d2/scratchpad/research/apify/`. Esa carpeta es temporal: si hay que conservar los datos, conviene copiarla al repo.
**Portadas analizadas (hojas de contacto):** `investigacion/referencias_visuales/apify_tiktok/` (top 30, bottom 30 y top 30 de hashtags).

> Leyenda: [D] dato medido en esta muestra · [I] inferencia o interpretación · [!] advertencia metodológica.
> No se incluyen nombres de usuario de comentaristas. Los comentarios citados son textuales, pero anónimos.

---

## 0. Resumen ejecutivo

1. **[D] El tema concreto y cotidiano gana por goleada al tema abstracto.** En La Psicología Invisible (animación, mismo personaje y mismo formato), los títulos sobre una conducta concreta tienen una mediana de **1.6 M de vistas**: "personas que lloran cuando se enfadan", "que abrazan la almohada", "los perros que duermen contigo", "arreglar en vez de reemplazar". Los títulos de autoayuda abstracta tienen una mediana de **15.5 K**: autoestima, resiliencia, carisma, liderazgo. Es una diferencia de unas **100 veces**.
2. **[D] Las "Parte 2" se desploman en TikTok.** "Lloran cuando se enfadan" tuvo 2.7 M de vistas en la parte 1 y 58 K en la parte 2 (−98 %). "Arreglar en vez de reemplazar" tuvo 713 K y 36 K (−95 %). En Instagram, en cambio, las series en carrusel sí funcionan: la 3ª parte de "duelos que no tienen nada que ver con la muerte" de @psicologiaconb sacó **698 K likes y 5,860 comentarios**.
3. **[D] Lo que más se comparte es lo enviable y cálido.** @itslennnie (personaje animado en inglés, referencia) tiene una tasa de compartidos mediana del **7.6 %** de las vistas, unas 16 veces más que el resto de cuentas (0.49 %). Sus piezas son de unos 39 s, con texto afectivo directo ("hey. things get better. i love you") y la llamada "tag someone / send this to".
4. **[D] En las cuentas con persona a cámara funcionan las escenas, no el monólogo.** Rosi y Víctor (psicólogos y pareja) tienen sus 2 mayores outliers (×192 y ×73 sobre su mediana; 3.7 M y 1.4 M de vistas) en escenas de pareja dramatizadas. Sus bottom son monólogos a cámara de 0.8 K a 5 K vistas.
5. **[D] Las simulaciones de sesión ("así es una primera sesión") son las que más demanda de terapia generan.** El **53 %** de sus comentarios menciona terapia o psicólogo y el **17 %** pide precio, cita o modalidad en línea. En el resto de videos esas menciones son solo el 2.9 %. Es el hallazgo más accionable para Agenda PSI.
6. **[D] Un personaje 3D con aspecto de IA no basta.** Psicología Cruda (muñeco 3D con bufanda) tiene una mediana de 11 K vistas, y su producción reciente (octubre de 2026) cayó a 440-4,000 vistas. Ocupa 5 de los 10 peores videos de la muestra.
7. **[D] Instagram y TikTok premian cosas distintas.** @psicologiaconb tiene **1.2 M de seguidores en IG** con carruseles de texto (mediana de 49.9 K likes por post). Su TikTok replica esas mismas diapositivas y saca una mediana de **1.5 K vistas**.
8. **[D] Qué escribe la audiencia en TikTok (1,112 comentarios):** elogios (17 %), identificación ("me pasa", 15 %), anécdotas y debate sobre el caso (9 %), menciones a terapia (9 %), confesiones de malestar (7 %) y fe/religión (4 %). La crítica es mínima (0.5 %). Casi nadie pide temas de forma explícita (0.3 %); la demanda aparece como "¿y ahora qué hago?".

---

## 1. Muestra y método

| Bloque | Qué se extrajo | n |
|---|---|---|
| TikTok, hashtags | 8 hashtags × 12 videos (psicologia, saludmental, ansiedad, psicologiamexico, terapiapsicologica, psicologa, autoestima, relacionessanas) + 3 de prueba | 97 (87 en español) |
| TikTok, búsqueda | "psicología animada", "animación salud mental ansiedad" (12 c/u), para descubrir cuentas animadas | 24 |
| TikTok, perfiles | 15 cuentas × 17 videos recientes (sin fijados) | 252 (189 con ≥7 días de antigüedad) |
| TikTok, comentarios | 27 videos (21 de alto rendimiento, 6 de bajo) × hasta 48 | 1,112 |
| Instagram, perfiles | 13 perfiles consultados en modo "details" (8 válidos, 5 inexistentes con ese handle) | 15 resultados |
| Instagram, posts | 10 cuentas × 17 posts (Reels, carruseles e imágenes) | 170 |
| Instagram, comentarios | 165 vía scraper (11 posts destacados, máximo 15 por post sin login) + 825 "últimos comentarios" que trae cada post gratis | 990 |

**Cuentas de TikTok analizadas (verificadas en tiktok.com antes de gastar):**

| Cuenta | Seguidores | Formato | Mediana de vistas (17 videos) | Video máx. | Guardados/vistas (med) | Compartidos/vistas (med) | Duración med. |
|---|---|---|---|---|---|---|---|
| influencia.mental | 296 K | faceless: clips de caricatura + titular | 756 K | 7.4 M | 1.17 % | 0.79 % | 108 s |
| itslennnie (ref. EN) | 3.0 M | personaje animado | 65 K | 3.7 M | 2.05 % | **7.64 %** | 39 s |
| lapsicologiainvisible | 55 K | animación/ilustración (personaje verde) | 58 K | 2.7 M | 1.63 % | 0.70 % | 313 s |
| fabiana.psicologa1 | 516 K | persona a cámara | 38 K | 461 K | 1.00 % | 0.76 % | 53 s |
| rosiyvictor_psicologos | 106 K | persona/escenas de pareja | 19 K | 3.7 M | 1.25 % | 0.64 % | 42 s |
| patoopsicologo | 129 K | persona a cámara | 17 K | 1.2 M | **4.10 %** | 1.13 % | 131 s |
| psic_noreliamorales | 158 K | persona a cámara | 12 K | 465 K | 1.18 % | 0.54 % | 13 s |
| psicologiacruda_ | 48 K | faceless: personaje 3D con aspecto de IA | 11 K | 132 K | 1.16 % | 1.34 % | 70 s |
| ernesto.torres.psicologo | 142 K | persona/simulación de sesión | 8.3 K | 34 K | 1.36 % | 0.43 % | 97 s |
| centrosoma (MX) | 352 K | persona (clínica interdisciplinaria) | 8.0 K | 51 K | 2.69 % | 0.69 % | 99 s |
| ceciliaayonpsicologa (MX) | 183 K | persona a cámara | 1.7 K | 16 K | 0.40 % | 0.07 % | 36 s |
| psicologiaconb (MX) | 41 K | slideshows de texto (espejo de IG) | 1.5 K | 299 K* | 1.15 % | 0.31 % | — |
| 1minutodepsicologia | 1.3 M | persona + reacción a series/cuentos | 1.2 K | 90 K | 0.75 % | 0.44 % | 66 s |
| octaviasol.psi | 166 K | persona a cámara | 964 | 3.2 K | 1.13 % | 0.28 % | 81 s |
| teayudo_aayudarte | 13 K | animación amateur/memes | 640 | 1.8 K | 0.41 % | 0.28 % | 10 s |

\* El pico de 299 K en psicologiaconb es una promo de su grupo de escritura con un 0.05 % de guardados: muy probablemente pauta pagada. [I]

**Outlier score:** vistas del video ÷ mediana de la cuenta (calculada solo con videos de ≥7 días, para no castigar a los recién publicados). Top 30 y bottom 30 sobre esos 189 videos.

**Codificación de comentarios:** reglas por palabras clave en español (multietiqueta), calibradas leyendo ~250 comentarios a mano. Precisión estimada de ~80-90 % por categoría; queda un ~35-40 % sin código (emojis, frases sueltas, comentarios fuera de tema). [!]

---

## 2. TikTok: qué funcionó y qué no

### 2.1 Top 30 vs. bottom 30 (outlier score)

| Grupo | n | Duración med. | Guardados/vistas | Compartidos/vistas | Likes/vistas | Comentarios/vistas | Hook en pregunta | Hook "tú/te" | Serie ("parte") |
|---|---|---|---|---|---|---|---|---|---|
| Top 30 | 30 | 62 s | **1.78 %** | **1.33 %** | 8.7 % | 0.07 % | 7 % | 13 % | 0 % |
| Bottom 30 | 30 | 70 s | 0.99 % | 0.31 % | 6.0 % | 0.04 % | 10 % | 23 % | 3 % (+2 "parte 2" en portada) |
| Todos | 189 | 57 s | 1.17 % | 0.57 % | 7.2 % | 0.07 % | 12 % | 20 % | 2 % |

- [D] La correlación de Spearman entre el outlier score y la tasa de **compartidos es 0.32**; con guardados, 0.25; con likes, 0.22; con duración, **−0.03** (nula). La duración no explica el rendimiento: el contenido sí.
- [D] Los compartidos de los top son 4 veces los de los bottom. Lo que se comparte (a la pareja, a una amiga) es lo que escala.

**Top 10 (outlier):**

| # | Cuenta | ×Mediana | Vistas | Qué es (caption + portada) |
|---|---|---|---|---|
| 1 | rosiyvictor | ×192 | 3.7 M | Escena de pareja: "Una foto, un mensaje sin responder… rara vez son el verdadero problema" (los celos detrás del detonante) |
| 2 | rosiyvictor | ×73 | 1.4 M | Escena: "un rechazo s3xual se interpreta como rechazo personal" |
| 3 | psicologiaconb | ×68 | 100 K | Slideshow de frase: "cuando uno sobrepiensa, no está viendo la realidad…" |
| 4 | 1minutodepsicologia | ×65 | 90 K | Recomienda un cuento infantil a partir de la serie "Carrie" (cultura pop) |
| 5 | 1minutodepsicologia | ×63 | 86 K | Análisis de una escena de Ted Lasso ("se sienta a su lado y le da espacio") |
| 6 | itslennnie | ×53 | 3.7 M | "hey. things get better. i love you" (39 s) |
| 7 | lapsicologiainvisible | ×46 | 2.7 M | "La psicología de las personas que lloran cuando se enfadan" (240 s) |
| 8 | lapsicologiainvisible | ×36 | 2.1 M | "…personas que abrazan la almohada para dormir" (586 s) |
| 9 | patoopsicologo | ×31 | 1.2 M | "3 actividades con tu pareja… intenta la número 3" (listado + gancho a un número) |
| 10 | 1minutodepsicologia | ×28 | 38 K | Lectura de cuento ("Había una vez… y fin") |

**Bottom (patrones):**
- 5 de los 10 peores son del **personaje 3D con aspecto de IA** de Psicología Cruda, con títulos genéricos ("3 señales de control que disfrazan de amor", "¿El amor tiene que doler?"): de 440 a 830 vistas.
- **Promos de taller/curso o seminario** ("Entra al link de la biografía…", "Seminario psicoanálisis"): de 0.11× a 0.29×.
- **"Parte 2"** y **autoayuda abstracta** en La Psicología Invisible (resiliencia, autoestima): de 0.08× a 0.30×.
- **Monólogos sobre relaciones sin escena** (Rosi y Víctor solo a cámara): de 0.04× a 0.26×.
- Animación amateur sin tema claro (teayudo_aayudarte): de 130 a 260 vistas.

### 2.2 Temas (videos de perfil ≥7 días; un video puede tener varios temas)

| Tema | n | Outlier med. | Lectura |
|---|---|---|---|
| Autoestima/autocuidado | 17 | **1.87** | Funciona cuando se ata a una situación ("disfrutar tu propia compañía"); falla como concepto ("psicología de la autoestima") |
| Trauma/infancia/familia | 14 | 1.62 | Validar emociones de niños, crianza |
| Ansiedad/estrés | 14 | 1.54 | Mejor el "así se siente" que el "qué es" |
| TLP/diagnósticos | 14 | 1.44 | Centro Soma: "Green flags en TLP" (4.6×, 355 comentarios) |
| Depresión/tristeza | 40 | 1.39 | — |
| Motivación/frases | 29 | 1.27 | Altísimo en compartidos (2.2 %) |
| Pareja/relaciones | 48 | 1.19 | El tema más producido: gran techo (escenas virales), pero mucha saturación |
| Terapia/sesión/psicólogo | 35 | 1.00 | Rinde en vistas lo normal, pero es el que **más conversación de servicio** genera (ver §3) |
| Manipulación/"psicología oscura" | 20 | **0.67** | Satura; en hashtags sí aparecen outliers, pero mezclados con venta de libros |

En los hashtags en español (87 videos, sesgados hacia lo popular), la mediana es de 672 K vistas. Encabezan cultura/libros/películas, motivación, manipulación e infancia (de 1.1 M a 1.3 M de mediana). "Terapia/sesión" es el tema más bajo (395 K).

### 2.3 Duración

| Duración (perfiles) | n | Outlier med. | Guardados/vistas |
|---|---|---|---|
| ≤15 s | 13 | 0.81 | 0.37 % |
| 15-30 s | 13 | **1.19** | 0.79 % |
| 30-45 s | 32 | 1.00 | 1.00 % |
| 45-60 s | 15 | 1.00 | 1.13 % |
| 60-90 s | 33 | 0.80 | 1.14 % |
| 90-180 s | 42 | **1.07** | **1.81 %** |
| >180 s | 16 | 0.81 | 1.53 % |

- [D] Hay dos zonas que funcionan: **15-45 s** (alcance y compartidos, estilo Lennnie) y **90-180 s** (guardados altos; mini-explicación con valor). Los videos de ≤15 s rinden poco y casi no se guardan.
- [D] Los videos largos (4-10 min) de La Psicología Invisible pueden ser virales (2.7 M con 240 s y 2.1 M con 586 s), pero solo cuando el tema es concreto. Con temas abstractos, los mismos minutos generan 5-17 K. Lo que sostiene un video largo es el tema, no la duración.
- En hashtags, el rango 15-30 s tiene la mediana más alta (3.0 M, n=6).

### 2.4 Formato

| Formato (perfiles, ≥7 días) | n | Vistas med. | Guardados | Compartidos |
|---|---|---|---|---|
| Persona a cámara | 168 | 6.0 K | — | 0.47 % |
| Animación/ilustración (ES) | 34 | 3.4 K* | — | 0.45 % |
| Faceless texto/stock/IA | 33 | 132 K** | — | 1.07 % |
| Personaje animado (Lennnie, EN) | 17 | 65 K | 2.05 % | **7.64 %** |

\* La mediana de animación mezcla La Psicología Invisible (58 K) con teayudo_aayudarte (640). \*\* Está dominada por influencia.mental, que usa clips de caricaturas ajenas para vender un libro: no es un comparable sano. [!]

**Formato de los 30 videos más vistos en hashtags en español (codificado a mano viendo las portadas):** persona a cámara 10, clips de podcast/entrevista 7, **animación 4** (gatopan "Overthinker" 4.4 M; soygrafy "La ansiedad llega así" 981 K; tonycontreras "Ansiedad" 974 K; influencia.mental 2.3 M), faceless b-roll/IA 4, canciones con "ansiedad" en el título 4 (ruido), meme/sketch 1.

**Lo que muestran las portadas (hojas en `referencias_visuales/apify_tiktok/`):**
- **Top:** el titular grande en la portada es la promesa exacta ("La PSICOLOGÍA de las personas que ABRAZAN la almohada", "Cómo superar el MIEDO a que a tu pareja le guste alguien más"). Hay escenas con dos personas, fotogramas de series conocidas (Carrie, Ted Lasso) y fondos lisos con una sola frase manuscrita (Lennnie).
- **Bottom:** "PARTE 2" en la portada, conceptos abstractos ("Resiliencia", "Autoestima"), flyers de seminarios, persona sola sin texto o con un texto a medias ("Muy estable") y el muñeco 3D con escenas genéricas.
- **Animaciones de hashtags que funcionan:** representan la **sensación física** ("Así llega la ansiedad": persona en la cama con el pecho en rojo; "Cuando llega la ansiedad:" en estilo cartoon), sin explicación clínica.

### 2.5 Hooks: patrones observados

| Funciona [D/I] | No funciona [D/I] |
|---|---|
| "La psicología de las personas que + **conducta cotidiana específica**" (lloran al enojarse, abrazan la almohada, duermen con su perro) | "Psicología de + concepto" (autoestima, resiliencia, carisma, liderazgo) |
| Escena reconocible de pareja: "Me hace daño que comentes fotos de chicas" | Monólogo explicativo ("Poner un límite no significa…") |
| Número con intriga: "intenta con tu pareja la número 3" | Listas genéricas sin intriga ("3 señales de control…") |
| Cultura pop: "¿Carrie y un cuento infantil?" | "PARTE 2" / continuaciones |
| Afecto directo de 2ª persona: "hey. things get better. i love you" | CTA de venta como caption ("Entra al link…") |
| "Así se siente la ansiedad" (visual, corporal) | Preguntas retóricas genéricas ("¿El amor tiene que doler?") |

- [D] Los hooks en forma de pregunta no rinden mejor (outlier med. 0.98 frente a 1.00). Usar "tú/te" en el caption tampoco garantiza nada: es más frecuente en los bottom (23 %) que en los top (13 %).

---

## 3. TikTok: qué dice la audiencia (1,112 comentarios de 27 videos)

| Categoría | n | % TikTok | % videos alto rend. | % videos bajo rend. |
|---|---|---|---|---|
| Elogio/agradecimiento | 190 | 17.1 | 16.3 | 25.0 |
| Identificación/validación ("me pasa", "tal cual", "yo también") | 169 | 15.2 | 15.7 | 10.6 |
| Humor/comunidad/etiquetar a alguien | 121 | 10.9 | 11.4 | 5.8 |
| Pregunta/debate sobre el caso ("¿y si…?", "pero…") | 105 | 9.4 | 10.2 | 1.9 |
| Menciones a terapia/psicólogo | 104 | 9.4 | 10.3 | 0.0 |
| Confesión de malestar | 75 | 6.7 | 7.4 | 0.0 |
| Religión/espiritualidad ("Dios", "amén") | 42 | 3.8 | 4.1 | 1.0 |
| Solicitud de servicio (precio, cita, "¿atiendes en línea?") | 41 | 3.7 | 4.0 | 1.0 |
| Respuesta a CTA de palabra clave ("elijo", "mente") | 27 | 2.4 | 0.4 | 22.1 |
| Pedido de ayuda ("¿qué hago?", "¿cómo se resuelve?") | 26 | 2.3 | 2.5 | 1.0 |
| Crítica/escepticismo (IA, exactitud, patologización, publicidad) | 6 | 0.5 | 0.3 | 2.9 |
| Petición explícita de tema | 3 | 0.3 | 0.3 | 0.0 |
| Sin código | 442 | 39.7 | — | — |

(Multietiqueta: los % no suman 100. El grupo de bajo rendimiento tiene solo 104 comentarios porque esos videos casi no tienen comentarios; casi la mitad viene de un post con CTA "¿elegir o ser elegido?".) [!]

**Hallazgos:**
1. **[D] Las simulaciones de sesión son una mina de intención de compra.** En 144 comentarios de 3 videos de este tipo (Ernesto Torres, Cecilia Ayón, Susurros Mentales), el **52.8 %** menciona terapia y el **17.4 %** pide servicio. En los otros 24 videos, solo el 2.9 % menciona terapia. Ejemplos textuales:
   - "De tan bonito que habló hasta ganas me dieron de ir a terapia y contarle todo a él." (2,256 likes)
   - "¿En donde te encuentras? Necesito a alguien que me aporte esa confianza para comenzar a platicarle todo." (624 likes)
   - "y si ni siquiera sé por qué me quiero consultar pero sé que lo necesito?" (687 likes)
   - "He tenido 5 psicólogas y con ninguna he sentido esa confianza…"
   - "dónde encuentro psicólogos como los que aparecen aquí?… cuando me animé a ir con uno salí peor que como entré"
   - "No puedo hablar sin llorar, me da miedo pagar una terapia y no poder expresarme…"
   - "Precio por favor quiero tomar terapia" / "¿Das sesiones online y qué precio tienen?"
2. **[D] Menciones a terapia por subtema (n=104):** experiencias negativas o de desajuste con el terapeuta (13 explícitas: "mi psicóloga solo me deja hablar", "me volví la psicóloga de mi psicóloga", "abandoné el proceso"); costo o "¿es gratis?" (6); deseo o necesidad de ir y búsqueda de dónde (6); miedo o nervios ante la primera cita (1-2, con mucho engagement). [I] **El dolor más repetido no es "no creo en la terapia", sino "no encontré al psicólogo adecuado" y "no sé qué esperar ni cuánto cuesta".** Es justo el problema que resuelve un servicio que conecta pacientes con psicólogos.
3. **[D] La confesión de malestar se concentra en piezas de "así se siente"**: soygrafy, animación de ansiedad (25 % de sus comentarios); el remedio casero para la ansiedad de drsergioperea (23 %); La Psicología Invisible (12 %). Son síntomas físicos ("me duele el pecho", "no puedo respirar", "palpitaciones") y antigüedad del malestar ("más de 5 años con ansiedad y depresión"). [I] Un personaje que pone en escena la sensación genera esa apertura, y obliga a tener un **protocolo de respuesta** (recursos de crisis, Línea de la Vida 800 911 2000 en México).
4. **[D] La identificación nace de lo concreto.** Los comentarios con más likes de toda la muestra son relatos propios sobre la conducta del video: "Lloro de rabia y decepción y eso me enfada más…" (16,257 likes); "Odio cuando me pasa, siento que no me toman en serio" (7,991); "Desde niña he dormido abrazando la almohada…" (6,284). En los temas abstractos no aparece ese efecto.
5. **[D] La comunidad de pareja comenta etiquetando y bromeando**: "pero que le salga a mi esposo, no a mí" (5,106 likes); "Nosotros hicimos el FODA de nuestra relación jajaja" (4,638). Ese es el mecanismo de compartir.
6. **[D] La demanda de temas se expresa como "¿y ahora qué hago?"** ("Gracias por la explicación, y ahora qué hacemos?", 634 likes; "¿Cómo se puede evitar llorar en esas situaciones?"). Las peticiones explícitas son pocas: "podrías hablar de las personas que sentimos con mucha más intensidad?", "¿cuál es la serie?", "¿cómo se llama el libro?". [I] Cada video debería cerrar con **una herramienta concreta**, y la parte de "qué hacer" puede ser el gancho del siguiente video, sin numerarlo como "parte 2".
7. **[D] La fe aparece como recurso de afrontamiento** (3.8 %: "oremos, la biblia dice que Dios quita toda ansiedad", "el mejor psicólogo se llama Jesús"). [I] No hay que confrontarla: conviene un tono respetuoso que no la ridiculice.
8. **[D] Casi no hay crítica** (0.5 %). No aparece queja por uso de IA en los videos de psicología; la única mención es en influencia.mental ("ahora todo lo hacen ver como si fuera una IA"). Hay un caso de corrección técnica ("las constelaciones familiares no son terapia"). [I] La baja crítica no significa que haya permiso: el algoritmo simplemente no premia al personaje 3D genérico (§2.1).

---

## 4. Instagram: Reels vs. carruseles

**Cuentas (17 posts recientes c/u):**

| Cuenta | Seguidores | Reels/Carr./Img. | Likes med. | Comentarios med. | Plays med. (Reels) | Plays/seguidor |
|---|---|---|---|---|---|---|
| itslennnie (ref.) | 2.34 M | 13/4/0 | 62.7 K | 367 | 1.06 M | 0.45 |
| psicologiaconb (MX) | 1.21 M | 0/17/0 | **49.9 K** | 266 | — | — |
| influencia.mental | 543 K | 17/0/0 | 21.6 K | 226 | 404 K | 0.75 |
| 1minutodepsicologia | 427 K | 4/8/5 | 1.6 K | 15 | 21 K | 0.05 |
| rosiyvictor_psicologos | 184 K | 10/7/0 | 713 | 6 | 27 K | 0.15 |
| centrosomaslp (MX) | 47 K | 6/6/5 | 470 | 15 | 12 K | 0.25 |
| octaviasol.psi | 9.7 K | 14/3/0 | 19 | 0 | 1.1 K | 0.11 |
| lapsicologiainvisible | 3.8 K | 12/5/0 | 39 | 0 | 2.1 K | 0.54 |
| ernestotorres.psicologo | n/d | 17/0/0 | 261 | 3 | 5.7 K | — |
| psic_noreliamorales | n/d | 3/8/6 | likes ocultos | 0 | 14.5 K | — |

**Por tipo (sin fijados; outlier = likes ÷ mediana de la cuenta):**

| Tipo | n | Likes med. | Comentarios med. | Outlier med. | (Likes+com)/seguidores |
|---|---|---|---|---|---|
| Carrusel | 58 | 3,631 | 19 | 1.00 | 1.14 % |
| Reel | 96 | 403 | 7.5 | 1.00 | 1.24 % |
| Imagen | 16 | 552 | 1 | 1.01 | 0.84 % |

Dentro de cada cuenta, el carrusel supera al Reel en likes en 3 de las 4 cuentas que publican ambos: 1minutodepsicologia (1.51× frente a 0.43×), rosiyvictor (1.91× frente a 0.77×) y centrosomaslp (1.52× frente a 1.05×). La excepción es La Psicología Invisible, cuyos carruseles rinden 0.33×. Comentarios por cada 1,000 likes: carrusel 6.6, Reel 6.9.

**Hallazgos de Instagram:**
1. **[D] El carrusel es el formato de profundidad y de series.** Los posts más fuertes son carruseles largos (8-17 diapositivas): "No todas las infidelidades empiezan con un beso" (rosiyvictor, 34× su mediana, 24 K likes); "Nunca fue sólo una mascota" (1minutodepsicologia, 16×, 25.7 K likes); los "duelos que no tienen nada que ver con la muerte", partes 3 y 4 (psicologiaconb, 698 K y 106 K likes). Al revés que en TikTok, **la serie numerada funciona en carrusel.**
2. **[D] Los "posts que provocan" generan conversación.** "¿Tienes la madurez para leer esto sin sentirte ofendido?" (3,065 comentarios) y "Frases brutalmente honestas que necesitas leer hoy" (794 y 655 comentarios).
3. **[D] El Reel da alcance, pero solo con personaje o gancho.** Lennnie obtiene 0.45 plays por seguidor (un Reel de 5.9 M plays: "whoever sent you this wanted to remind you that you are STRONG BRAVE…"). influencia.mental, 0.75. Los psicólogos a cámara se quedan entre 0.05 y 0.25.
4. **[D] El éxito en TikTok no se traslada solo a Instagram.** La Psicología Invisible tiene 2.7 M de vistas en un video de TikTok y apenas 3.8 K seguidores en IG (Reels con una mediana de 39 likes). @psicologiaconb, al revés: 1.2 M de seguidores en IG y 41 K en TikTok. [I] Hay que diseñar cada plataforma por separado.
5. **[D] Comentarios en IG (990):** domina la respuesta a CTA de palabra clave (17 %: "Grupo" para el grupo de psicologiaconb, "care kit" para el kit gratis de Lennnie), seguida de elogio/emoji (27 %) y etiquetar o bromear (15 %). Hay mucha menos confesión (0.8 %) y menos mención a terapia (1.8 %) que en TikTok. Sí aparecen solicitudes de "info/precio" (4.1 %), concentradas en Ernesto Torres y Centro Soma. [I] **Instagram sirve para convertir: CTA de palabra clave hacia DM, lead magnet o grupo. TikTok es donde la gente se abre y cuenta lo que siente.** Lennnie usa en IG el mismo patrón que funcionaría para Agenda PSI: "comenta 'care kit' y te envío un kit gratis".
6. **[D]** Las promos (seminarios, cursos, eventos) son los peores posts en IG, igual que en TikTok (0.08×-0.24×).

---

## 5. Implicaciones para el personaje de Agenda PSI [I]

1. **Fórmula de tema:** "Lo que significa cuando [conducta cotidiana muy específica que el público hace]". Hay que evitar el "Psicología de [concepto]". Antes de producir un guion, conviene comprobar si alguien comentaría "¡yo hago eso!".
2. **Dos duraciones en TikTok:**
   (a) **20-40 s**, pieza afectiva y enviable (estilo Lennnie, en español y con humor mexicano), que busca compartidos;
   (b) **90-180 s**, mini-explicación de una conducta concreta con un "qué hacer" al final, que busca guardados.
   Mejor evitar los ≤15 s sin idea clara y los >3 min, salvo que el tema sea muy fuerte.
3. **Personaje con escenas, no muñeco que da una clase.** Las escenas de pareja y de "así se siente" (un cuerpo en la cama con el pecho en rojo) superan al monólogo. El personaje 3D genérico con aspecto de IA es la variante que peor funcionó de la muestra.
4. **Nada de "Parte 2" en TikTok.** Cada video debe valer por sí mismo. En Instagram, en cambio, conviene hacer series en carrusel ("duelos que no son por muerte, parte 3").
5. **Línea de "así es la terapia por dentro"** (qué pasa en la primera sesión, cómo saber si tu psicólogo te queda, qué preguntar del precio, qué hacer si no conectas). Es la conversación de mayor intención: 53 % de menciones a terapia y 17 % de solicitudes de servicio. Encaja de forma natural con el servicio de Agenda PSI sin parecer anuncio.
6. **Responder a "¿y ahora qué hago?":** cerrar siempre con una micro-herramienta. En los comentarios, la demanda casi nunca es "habla de X"; es "dime qué hacer".
7. **Ganchos culturales:** series, películas y cuentos (Ted Lasso, Carrie) son el mejor recurso de 1minutodepsicologia y encabezan la tabla de temas en hashtags.
8. **Conversión:** en IG, usar CTA de palabra clave ("comenta 'PRIMERA CITA'") hacia una guía o un match con un psicólogo. Nunca hacer posts promocionales "secos" (seminario, taller): son sistemáticamente los peores.
9. **Seguridad:** el 6.7 % de los comentarios de TikTok son confesiones de malestar, algunas graves (duelo por suicidio, "me quiero morir", síntomas de pánico). Hace falta un protocolo de moderación y respuesta con recursos de crisis antes del lanzamiento.

---

## 6. Gasto (verificado por run y por `/users/me/usage/monthly`)

| Bloque | Run | Resultados | USD |
|---|---|---|---|
| TikTok videos | prueba hashtag (3) | 3 | 0.0121 |
| TikTok videos | 8 hashtags × 12 | 96 | 0.3562 |
| TikTok videos | búsqueda "psicología animada" (2 × 12) | 24 | 0.0898 |
| TikTok videos | 15 perfiles × 17 | 255 | 0.9445 |
| **Subtotal TikTok videos** (tope 1.50) | | **378** | **1.4026** |
| TikTok comentarios | prueba (5) | 5 | 0.0063 |
| TikTok comentarios | 27 videos × ≤48 | 1,112 | 1.3900 |
| **Subtotal TikTok comentarios** (tope 1.50) | | **1,117** | **1.3963** |
| Instagram | details (prueba 2 + 13 perfiles) | 15 | 0.0405 |
| Instagram | posts (prueba 2 + 10 cuentas × 17) | 172 | 0.4644 |
| Instagram | comentarios (prueba 3 + 11 posts × 15) | 168 | 0.4368 |
| **Subtotal Instagram** (tope 1.30) | | **355** (+825 comentarios gratis incluidos en los posts) | **0.9417** |
| **TOTAL** (tope 4.30) | 12 runs | | **3.7406 USD** |

- El endpoint de uso mensual marcaba **3.7432 USD** (la diferencia de 0.0026 corresponde a transferencia de datos). Quedan unos **1.26 USD** de los 5 de crédito.
- Todos los runs usaron `maxItems` y `maxTotalChargeUsd`. No se activaron add-ons (descarga de video, transcripción, filtros de fecha/país/popularidad, IA) ni se descargaron videos; solo portadas públicas, que no tienen costo en Apify.
- Ahorros: el modo "details" de Instagram trae los 12 últimos posts por 0.0027 USD, y el modo "posts" incluye hasta 10 "latestComments" por post. Por eso hay 990 comentarios de IG pagando solo 168.

---

## 7. Limitaciones [!]

1. **Muestra pequeña y de conveniencia:** 15 cuentas de TikTok × 17 videos recientes y 10 de IG × 17 posts. Los resultados son indicativos, no estadísticamente generalizables. Las diferencias por tema dentro de una misma cuenta (La Psicología Invisible) son la evidencia más limpia.
2. **Sesgo de recencia:** los perfiles cubren días o semanas (de 7 a 654 días según la cuenta). Los videos de menos de 7 días se excluyeron del outlier score; dos cuentas (octaviasol, noreliamorales) tenían toda su muestra por debajo de ese umbral.
3. **Hashtags:** el scraper devuelve una mezcla sesgada hacia lo popular y de varios años. Incluye ruido (canciones llamadas "Ansiedad", contenido italiano/portugués en #psicologia). En español quedan 87 videos.
4. **Clasificación de formato** a partir del caption, el autor y una revisión visual de unas 90 portadas, no del video completo. El hook se infiere del caption y del texto de la portada, no de los primeros segundos de audio.
5. **Codificación de comentarios por reglas de palabras clave** (precisión estimada de ~80-90 %; ~35-40 % sin código). Los comentarios mostrados son los "top/recientes" que devuelve la plataforma, no una muestra aleatoria. En IG, el scraper sin login se limita a 15 comentarios por post.
6. **Comparables imperfectos:** influencia.mental usa caricaturas ajenas para vender un libro, y su engagement no es replicable de forma ética. Lennnie está en inglés. No se encontró ninguna cuenta hispana con un **personaje animado propio** de escala (La Psicología Invisible es la más cercana, con 55 K seguidores en TikTok), lo que confirma el hueco detectado en la Ronda 1.
7. **Instagram:** no hay vistas para carruseles; la comparación entre Reels y carruseles se hace en likes y comentarios. Faltan seguidores de 2 cuentas (handles sin "details"). Varios handles probados no existen en IG con ese nombre (fabiana.psicologa1, patoopsicologo, ceciliaayonpsicologa).
8. **Guardados y compartidos** solo están disponibles en TikTok.

---

## 8. Archivos

**En la carpeta temporal de la sesión** (`/tmp/claude-0/-home-user-Creador-de-videos-Para-redes-/f6e80049-54f1-5e5b-b0dd-1d5ea884d7d2/scratchpad/research/apify/`, conviene copiarla al repo si hay que conservarla):
- `tiktok_videos.csv`: 373 videos únicos con métricas, temas, hook y formato.
- `tiktok_profile_videos_scored.csv`: videos de perfil con mediana de la cuenta y outlier score.
- `tiktok_top30_outliers.csv` y `tiktok_bottom30.csv`.
- `instagram_posts.csv`: 170 posts.
- `comentarios_codificados.csv` (sin usuarios) y `comentarios_resumen_pct.csv`.
- `tt_*.json`, `ig_*.json`: respuestas crudas de Apify. Contienen datos de usuarios: no publicar.
- `ledger.jsonl`: registro de gasto por run.

**En el repo:**
- `investigacion/referencias_visuales/apify_tiktok/sheet_*.jpg`: hojas de portadas.
