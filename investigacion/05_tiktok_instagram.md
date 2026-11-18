# 05 · Qué funciona en TikTok e Instagram (psicología en español, México/Latam)

**Para:** Agenda PSI (agendapsi.mx), canal de divulgación con personaje animado (TikTok, Instagram Reels/carruseles, YouTube Shorts)
**Fecha de captura de datos:** 18 de noviembre de 2026
**Datos crudos:** `/tmp/claude-0/-home-user-Creador-de-videos-Para-redes-/f6e80049-54f1-5e5b-b0dd-1d5ea884d7d2/scratchpad/research/social/` (el scratchpad puede borrarse; conviene copiar a un lugar durable lo que se quiera conservar)

> **Cómo leer este informe.** Cada afirmación lleva una etiqueta:
> **[V]** = dato verificado directamente hoy en una fuente pública (perfil, video o listado de TikTok, YouTube o Instagram), con el número tal como lo devuelve la plataforma.
> **[F]** = dato tomado de una fuente secundaria (artículo, blog o documento de política) que **no** pude contrastar con la plataforma.
> **[I]** = inferencia o recomendación mía a partir de los datos.

---

## 0. Resumen ejecutivo

1. **En el nicho hispano el que gana es el formato largo y con subtítulos, no el clip de 15 s.** En 50 videos virales de psicología en español, la duración mediana es de **85 s**. Solo 9 de los 50 duran 30 s o menos, y 29 pasan del minuto [V]. Con 1,665 videos de 28 cuentas hispanas, los videos de más de 3 min rinden un 12 % más que la mediana de su propia cuenta, y los de 0–15 s rinden un 6 % menos [V/I].
2. **Las cuentas animadas comparten muchísimo más.** Lennnie (blob animado, en inglés) tiene un **share rate del 8.3 %** en sus últimos 30 videos [V], contra una mediana de **0.42 %** en los videos hispanos de psicología con más de 5K vistas [V]. Sus videos "whoever sent you this…" llegan a **462K compartidos con 3.8M de vistas** (12 %) [V]. Su mecánica es una afirmación afectiva dirigida a "tú", pensada para mandársela a alguien.
3. **Lo que más se guarda es lo práctico**: técnicas, ejercicios, guías de primeros auxilios psicológicos, libros recomendados y "X señales". **Lo que más se comparte** es humor de autoironía del terapeuta, el formato "mándaselo a tu hermana/pareja" y los consejos de pareja del tipo "no le hables así" [V].
4. **El hook dominante (alrededor de la mitad de la muestra) es una tesis o una lista fija en una caja de texto desde el fotograma 0**, más subtítulos palabra por palabra. Ejemplos: "4 cosas que tienes derecho a esperar de tu pareja" (8.3M) y "La persona narcisista te pide PAZ…" (715K) [V]. 44 de 50 videos llevan texto en pantalla en el primer segundo [V/I].
5. **Los temas con más rendimiento** relativo a la cuenta son familia, infancia y crianza (×1.33), diagnósticos como TLP, TDAH o autismo (×1.37), listas numeradas (×2.4, n=23) y la actualidad o cultura pop mexicana: Komanche, el Chavo, chismes de TV (×1.29) [V/I].
6. **Las series "Parte 1/2" rinden menos de lo que se cree**: ×0.84 en las cuentas hispanas. "La Psicología de las Personas que Lloran Cuando se Enfadan" hizo 2.7M en la PARTE 1 y 58K en la PARTE 2 [V]. Funcionan cuando son **episodios autocontenidos** con personajes recurrentes: el episodio 2 de *Haunted House Husband* (Alec With Pen) hizo 11.1M [V].
7. **Ya hay animación con IA en español y en este nicho que funciona con la etiqueta de IA visible.** @lapsicologiainvisible muestra "Creator labeled as AI-generated", tiene 55K seguidores y logró 2.7M de vistas en un video [V]. **Pero desde el 16 de julio de 2026 YouTube no monetiza "AI personas" que hablen de salud** [F], así que el personaje debe ser **un personaje ficticio estilizado, no un avatar realista de un psicólogo**.
8. **Un riesgo competitivo directo**: Paola Lavín (746K en TikTok) es cofundadora de **@holaelo.mx**, una plataforma para psicólogos en México. La cuenta de marca solo tiene 19.9K seguidores y una mediana de 675 vistas [V]. **Las marcas-plataforma rinden poco y las personas o personajes rinden mucho** [I].

---

## 1. Metodología, fuentes y qué NO se pudo acceder

### 1.1 Lo que sí funcionó (todo sin credenciales y sin evadir protecciones)

| Fuente | Qué obtuve | Volumen |
|---|---|---|
| Páginas públicas de perfil de TikTok (`tiktok.com/@usuario`, el JSON de rehidratación que trae la propia página) | Seguidores, likes totales, número de videos, bio, verificación | ~110 handles probados, 45 válidos y relevantes |
| `yt-dlp` sobre perfiles públicos de TikTok (extractor `tiktok:user`, listado plano) | Por video: vistas, likes, **guardados**, compartidos, comentarios, duración, audio, fecha y caption | **2,229 videos** de 38 cuentas (últimos ~60 por cuenta) |
| Reproductor **embed público** de TikTok (`tiktok.com/embed/v2/ID`) con Playwright | Fotogramas en 0 (portada), 1, 2.5, 4.5 y 10 s para leer el hook visual y el texto en pantalla | **63 videos** (50 en español y orgánicos) |
| `yt-dlp` sobre las pestañas `/shorts` de YouTube | Títulos y vistas (redondeadas) de 150 Shorts por canal | 17 canales, ~2,000 Shorts |
| Subtítulos automáticos de YouTube Shorts | Transcripción del hook hablado | 8 Shorts (luego bloqueó, ver abajo) |
| Perfiles públicos de Instagram con Playwright (la vista sin sesión muestra el contador y la cuadrícula) | Seguidores, número de publicaciones, mezcla de formatos (carrusel/reel/foto) en las últimas 12 publicaciones, portadas | 44 perfiles intentados, ~33 con dato |
| Búsqueda web y artículos | Listas de cuentas, políticas y benchmarks | Ver las fuentes al final |

### 1.2 Lo que NO pude acceder (documentado; no intenté forzarlo)

- **TikTok Creative Center**: no carga en headless (confirmado por el usuario). No lo reintenté.
- **Páginas de hashtag y "discover" de TikTok** (`/tag/psicologia`, `/discover/...`): el HTML llega sin datos y con Playwright muestra "Hubo un problema… Inténtalo más tarde". El extractor `tiktok:tag` de yt-dlp figura como *CURRENTLY BROKEN*. **Por eso no hay un ranking por hashtag; la muestra viral sale de los top de cada cuenta.**
- **oEmbed de TikTok para perfiles**: devuelve `400 Something went wrong`. Para videos no fue necesario.
- **Descarga individual de un video de TikTok con yt-dlp**: pide *impersonation* (curl_cffi). No lo instalé para no evadir medidas anti-bot y usé el embed público en su lugar.
- **YouTube (detalle por video)**: después de ~10 peticiones apareció "Sign in to confirm you're not a bot". Detuve la descarga; solo conseguí 8 transcripciones. Los listados planos de `/shorts` sí funcionaron, pero **las vistas vienen redondeadas** (p. ej. "80K") y **sin duración**.
- **Instagram**: el endpoint `web_profile_info` devuelve 404. Curl simple redirige al login. Playwright funciona con intermitencias (~70 % de éxito) y **no muestra likes ni guardados de carruseles**. Tampoco abrí carruseles slide por slide por el modal de login. **No hay métricas de guardados en IG; los patrones de carrusel combinan las portadas observadas, los benchmarks [F] y los guardados de TikTok como proxy.**
- **Agregadores**: Social Blade (TikTok) → 403. Exolyt → 404 o requiere app. HypeAuditor (ranking MX) → 404. Favikon → 404. CreatorDB → solo YouTube de Psych2Go. **No tengo series históricas de crecimiento.** El "crecimiento" de este informe compara el dato de hoy [V] con cifras publicadas antes en artículos [F].
- **Reddit**: 403 (confirmado por el usuario). No reintenté.

### 1.3 Métricas calculadas

- **Lift** = vistas del video ÷ mediana de vistas de los ~60 videos recientes de **su propia cuenta**. Neutraliza el tamaño de la cuenta (>1 = rinde más que lo habitual).
- **Tasas (like, save, share, comment)** = suma de la interacción ÷ suma de las vistas en los **30 videos más recientes** de la cuenta.
- **Posts/semana** = 7 ÷ mediana de días entre publicaciones (30 más recientes).
- **Vistas/seguidor (vpf)** = mediana de vistas recientes ÷ seguidores. Es un indicador de si la cuenta sigue viva para el algoritmo o vive del pasado.
- **Advertencia**: el listado puede incluir 1–3 videos fijados antiguos. También detecté **videos pautados** (Pictoline × Nubank: 3.4M de vistas con 0.27 % de likes; Gato Aurelio: 2.5M con 0.04 %). Los excluí de las conclusiones orgánicas.

---

## 2. Mapa de cuentas hispanas (psicología, salud mental e ilustración emocional)

Los datos de TikTok se capturaron el 18/11/2026 [V], salvo que se indique otra cosa. "IG" = seguidores de Instagram leídos hoy en el perfil público [V]; IG redondea ("2M"). "—" = no capturado o handle distinto.

### 2.1 Psicólogos y psiquiatras con cara (talking head)

| # | Cuenta (país) | TikTok seg. | IG | Posts/sem | Mediana vistas (30 rec.) | Save % / Share % | Duración mediana | Formato y tono | Credencial visible |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **Farid Dieck** @faridieck (MX) | 30.46M | 11M | 10.8 | 1,150,000 | 1.91 / 0.64 | **914 s** | Relato e interpretación de películas e historias reales; narrativo y largo | "Psicólogo." en la bio; verificado |
| 2 | **Machy Guerrero** @machyguerrero (MX) | 3.99M | — | 1.2 | 20,950 | 1.29 / 0.80 | 86 s | Selfie (coche/casa), crianza y buen trato a la infancia; firme | "Psic." en la bio |
| 3 | **Carlos Alanis** @psicologocarlosalanis (MX) | 3.42M | 970K | 11.9 | 5,482 | 0.62 / 0.27 | 85 s | Ansiedad y pánico; respuestas a comentarios, citas de pacientes en caja blanca; vende "Método Lux" | "Psicólogo" en el nombre |
| 4 | **César Lozano** @drcesarlozano (MX) | 2.35M | — | 3.6 | 97,600 | 0.78 / 1.12 | 52 s | Motivacional, clips de LIVE y podcast; cálido | "Conferencista, autor" (no se presenta como psicólogo) |
| 5 | **Victoria Olavarrieta** (MX) | 2.09M | — | 7.3 | 1,095 | 0.68 / 0.19 | 41 s | Giró a poemas y moda; **cuenta "zombie"** (vpf 0.001) | "Psicología" en la bio |
| 6 | **Massiel Martel** @psicologamassiel (PE) | 1.98M | 149K | 2.4 | 18,500 | 1.00 / 0.58 | 90 s | Pareja; greenscreen sobre chismes de TV y noticias | "Psicóloga – Psicoterapeuta"; verificada |
| 7 | **Adrián Salama** @adriansalama (MX) | 1.97M | 638K | **35.4** | 4,612 | 0.59 / 0.27 | 30 s | Clips de stream en pantalla dividida, newsjacking (Komanche); "El psicólogo de TikTok" | Verificado; "Dr." en YT |
| 8 | **Carrot Adventure** @carrotadventure (ES) | 1.72M | — | 1.0 | 101,650 | **2.03** / 0.61 | **164 s** | Divulgación crítica ("psicobasura"), análisis de virales; marca visual (pelirrojo, franja amarilla) | Psicólogo (en prensa) [F] |
| 9 | **Martín Jardon** @psicologia_instantanea (AR) | 1.38M | — | 3.8 | 48,050 | 1.68 / 0.54 | 171 s | **Monotema narcisismo**; caja con tesis + subtítulos | Verificado; "Psicólogo" |
| 10 | **Adály López** @1minutodepsicologia (MX) | 1.31M | 426K | 1.8 | 1,780 | **2.28 / 1.67** | 48 s | Crianza, recursos y cuentos; subtítulos karaoke amarillos | "Psicóloga Clínica", autora; verificada |
| 11 | **Manuel Arango** @manuel.arango (CO) | 1.20M | — | 0.8 | 3,569 | 0.91 / 0.42 | 40 s | "X señales según ciencia", test visual con fuente académica | "Psicólogo" |
| 12 | **Paola Lavín** @paola.lavin.lps (MX) | 746K | 179K | 9.7 | 1,424 | 0.84 / 0.72 | 37 s | Humor, lifestyle y psicología; **cofundadora de @holaelo** | "Tu psicóloga fav" |
| 13 | **Cristy de la Torre** (MX) | 656K | 351K | 12.3 | 3,801 | 1.24 / 0.70 | 60 s | Desarrollo personal con toques espirituales ("el universo te escucha") | "Psicóloga" |
| 14 | **Karime Fajer** @kay.psicologiapop (MX) | 490K | — | 5.4 | 5,120 | 0.39 / 0.47 | 15 s | Psicología + cultura pop + comedia; sketches | "M.S. CBT" |
| 15 | **Alejandra de Pedro** @adp.psicologa (ES) | 489K | — | inactiva (último: ene-2025) | 125,650 | **2.80** / 0.79 | 163 s | Pareja; título rojo fijo + lista numerada | "Psicóloga y terapeuta de parejas" |
| 16 | **Marian Rojas Estapé** (ES) | 409K | **5M** | 0.4 | 51,700 | 0.76 / 0.86 | 56 s | Clips de conferencias y entrevistas; marca autora | "Psiquiatra" |
| 17 | **Juan Luis Tigo** @psicjuanluistigo (MX) | 367K | — | 8.0 | 1,343 | 1.86 / 0.76 | 56 s | Pareja y sexualidad; "Pregúntale al psicólogo" | "Psicólogo – Sexólogo" |
| 18 | **Centro Soma** @centrosoma (MX, SLP) | 352K | — | 6.3 | 8,226 | **3.68** / 1.06 | 118 s | TLP y "persona favorita"; caja serif + imagen tierna; disclaimer fijo | Equipo interdisciplinario |
| 19 | **Somos Estupendas** (ES) | 304K | 891K | 3.7 | 7,225 | 0.39 / 0.20 | 93 s | Testimonios y entrevistas (duelo, abuso, familia) | Centro de psicoterapia |
| 20 | **Alicia González** @aliciagonzalezpsicologia (ES) | 289K | — | 1.6 | 28,250 | 0.85 / 0.62 | 70 s | **Confesional**: "acabo de poner un límite a mis padres y siento culpa" | "Psicología online" |
| 21 | **Silvia Congost** (ES) | 255K | 601K | 2.3 | 9,806 | 0.63 / 0.37 | 53 s | Clips de radio y podcast; dependencia emocional | "Psicóloga experta en autoestima" |
| 22 | **Fanny Psiquiatra** @fannypsiquiatra (MX) | 217K | — | 8.0 | 4,473 | 0.46 / 0.16 | 37 s | Fármacos y diagnósticos; plantilla tipo miniatura de YouTube | "Psiquiatra" |
| 23 | **Desirée Llamas** (ES) | 124K | — | 1.2 | 3,221 | 1.39 / 0.91 | 88 s | Psicología científica, desmentidos ("te contaron mal el marshmallow test"), sketches | "Dra." |
| 24 | **JessForense** (MX) | 59K | — | 1.8 | 2,419 | 1.33 / 0.35 | 136 s | Psicología forense, Q&A | "Psicóloga Forense" |
| 25 | **hijademabel** (AR) | 41K | — | 6.9 | 6,448 | 0.71 / 0.31 | 68 s | Memes de terapeuta ("cosas que no le puedo decir a un paciente"); **vpf 0.157, cuenta pequeña en ascenso** | "Tu psico conductual" |
| 26 | **holaelo.mx** (MX, competidor) | 19.9K | — | 8.6 | 675 | 0.55 / 0.54 | 25 s | Marca SaaS para psicólogos | — |

### 2.2 Cuentas faceless, animadas o ilustradas en español

| # | Cuenta | Plataforma: seguidores | Mediana vistas | Formato | Personaje | Nota |
|---|---|---|---|---|---|---|
| 27 | **La Psicología Invisible** @lapsicologiainvisible | TT 55K [V]; canal YT con videos de 0.4–2.8M [V] | 37,550 (TT) | **Animación con IA etiquetada**, personajes tipo "blob" verde, narración en off, letterbox con título fijo, 240–600 s | Sí (blobs genéricos) | **vpf 0.68**: el algoritmo lo empuja mucho para su tamaño |
| 28 | **Psych2Go Español** (YouTube) | Shorts: mediana ~9.2K, top 165K [V, redondeado] | — | Animación 2D, voz en off, "Señales de…", "Por qué los inteligentes…" | Personajes genéricos | Versión doblada del canal en inglés (13.2M en YT [F, CreatorDB]) |
| 29 | **Psicología Animada** (YouTube) | Shorts: mediana ~1.6K, top 25K [V] | — | Explainers animados de trastornos (DSM-5) | No | En TikTok el handle @psicologiaanimada es otra cuenta (curiosidades con IA, 1.2M en un carrusel del Chavo del 8) |
| 30 | **Desansiedad** (YouTube; @desansiedad en TT está vacío) | Shorts: mediana ~10K, top **508K** ("Ejercicios para el nervio vago") [V] | — | Ejercicios guiados para la ansiedad | No | Lo práctico y corporal arrasa |
| 31 | **Pictoline** (MX) | TT 1.24M, IG **2.4M** [V] | 23,750 | Infografía e ilustración animada; personaje **"Gato Aurelio"** (libro *Meditaciones de Gato Aurelio*) | **Sí** | Gato Aurelio da consejos (finanzas, filosofía estoica); 4.1 % de guardados en uno de sus videos |
| 32 | **Moderna de Pueblo** (ES) | TT 152K, IG **2M** [V] | 18,300 | Cómic animado limitado + clips de su programa | Sí (alter ego) | "¿Team rancia o team fiesta?" 2M |
| 33 | **72kilos** (ES) | IG **2M** [V] | — | Viñeta minimalista emocional | Sí (monigote) | En TikTok solo tiene 1K: el cómic estático vive en IG |
| 34 | **Mr. Wonderful** (ES) | IG 2M [V] | — | Frases positivas ilustradas (marca) | No | Referente "frase + ilustración" |
| 35 | **Flavita Banana** (ES) | IG 648K [V] | — | Viñeta B/N a mano, ironía social; 6 de 12 publicaciones recientes son carruseles [V] | Sí | — |
| 36 | **Lola Vendetta** (ES) | IG 616K [V] | — | Cómic con personaje feminista | Sí | Tiras de salud mental con MSF [F] |
| 37 | **Alfonso Casas** (ES) | IG 553K [V] | — | "Experto en autosabotaje", metáforas visuales | Sí | — |
| 38 | **Alberto Montt** (CL) | IG 365K [V] | — | Viñeta; libro con el personaje "Ansiedad" | Sí | — |
| 39 | **Javirroyo** (ES) | IG 356K [V] | — | Dibujo minimalista sobre salud mental y suicidio (rompe tabú) | No | — |
| 40 | **Pedrita Parker** (ES) | IG 309K [V] | — | Avatar que fue incorporando ansiedad, presión e insomnio [F] | Sí | — |
| 41 | **Monstruo Espagueti** (ES) | IG 243K [V] | — | Humor gráfico, salud mental | Sí | — |
| 42 | **Iglús** @iglus_ (ES) | IG 134K [V] | — | Ilustración con perspectiva de género | — | — |
| 43 | **Domm Cobb** (ES) | IG 90K [V] | — | Cartoon B/N, presiones cotidianas | — | — |
| 44 | **museodesam** (MX) | TT 13K [V] | 1,162 | Ilustración emocional; save 1.97 % | Sí (conejo) | Pequeña |
| — | Medios: **Psicología y Mente** IG 409K, **La Mente es Maravillosa** IG 459K [V] | | | Artículos y carruseles de texto; en TikTok son casi inexistentes (155 y 15.9K seguidores) [V] | | Los medios-texto no migraron a video |

### 2.3 "Crecimiento": comparación de hoy [V] contra cifras publicadas [F]

| Cuenta | Antes [F] | Hoy [V] | Lectura [I] |
|---|---|---|---|
| Carlos Alanis | 2.5M sumando plataformas (Saludiario, ene-2024) | 3.42M solo en TT + 970K en IG | Creció fuerte con volumen alto (~12 posts/sem) |
| Machy Guerrero | 5M sumando plataformas (ene-2024) | 3.99M en TT | Estable |
| Adály López | 1.8M sumando plataformas (ene-2024) | 1.31M en TT + 426K en IG | Estable; alcance reciente bajo (mediana 1.8K) pero gran tasa de guardados y compartidos |
| Carrot Adventure | ~1.8–2M en TT (BioBioChile, feb-2024) | 1.72M | Estancado o leve caída, pero mediana de 100K vistas: audiencia fiel |
| Elsa Gómez @psicologatiktokera | ">1M" (BrandMe) | **16K y 0 videos** | **Cuenta perdida o reiniciada**: riesgo real de baneo o abandono en el nicho |
| Alejandra de Pedro | 517K (COMSalud, 2025) | 488.6K; sin publicar desde ene-2025 | Pierde seguidores al dejar de publicar |
| Leandro Olszanski (EN/ES) | ">1M" | 2.55M; último video jun-2024 | Inactivo |
| Marmaremoto (ilustradora MX) | "casi 200K" en IG (Domestika) | El handle hoy da 76 seguidores (otra cuenta o renombrada) | No localizable |

**Hallazgo [V/I]: el tamaño de la cuenta predice mal las vistas actuales.** Victoria Olavarrieta (2.09M) tiene una mediana de 1,095 vistas. Hijademabel (41K) tiene 6,448. La Psicología Invisible (55K) tiene 37,550. **TikTok premia el video, no la base de seguidores**, y eso es una buena noticia para un canal nuevo.

---

## 3. Patrones cuantitativos (1,665 videos hispanos + 433 animados o ilustrados)

### 3.1 Duración (lift mediano frente a la propia cuenta) [V]

| Duración | Cuentas hispanas (n) | Lift | Animadas/ilustradas (n) | Lift |
|---|---|---|---|---|
| 0–15 s | 166 | 0.94 | 49 | **0.58** |
| 16–30 s | 170 | 1.00 | 79 | 0.99 |
| 31–60 s | 456 | 0.97 | 193 | 1.04 |
| 61–90 s | 325 | 1.00 | 96 | **1.72** |
| 91–180 s | 367 | 1.03 | 10 | 1.09 |
| >180 s | 181 | **1.12** | 6 | 1.01 |

- **[I]** Para la animación, la ventana óptima es de **60–90 s** (≥61 s también deja el video dentro de lo que TikTok exige para monetizar en su programa de recompensas, que pide más de 1 min [F, conocido públicamente]). Los micro-clips animados de menos de 15 s rinden la mitad.
- En la muestra viral hispana (50 videos), la mediana es de 85 s: ≤30 s = 9, 31–60 s = 11, 61–180 s = 21, >180 s = 8 [V].

### 3.2 Temas y recursos del caption (lift; solo cuentas hispanas) [V]

| Rasgo del caption | n | Lift con / sin |
|---|---|---|
| Lista numerada ("4 señales", "3 cosas"…) | 23 | **2.44** / 1.00 |
| Disclaimer "no te autodiagnostiques" | 49 | 1.72 / 1.00 (efecto Centro Soma: lo usan en todos sus videos, que tratan de TLP) |
| Diagnósticos (TLP, TDAH, autismo, depresión, bipolar) | 111 | **1.37** / 0.99 |
| Familia, infancia, crianza | 89 | **1.33** / 0.99 |
| Famosos o actualidad (cultura pop) | 31 | 1.29 / 1.00 |
| Pareja o relación | 376 | 1.04 |
| Pregunta en el caption | 436 | 1.03 |
| Respuesta a comentario | 52 | 1.02 |
| "Parte N" / serie | 62 | **0.84** |
| Greenscreen, dúo o stitch | 12 | 0.60 |
| Audio musical con nombre (frente a sonido original o voz) | 316 | 0.92 frente a 1.01 |

**[I]** En el nicho hispano **la voz y el sonido original superan a la música de tendencia**. En las cuentas animadas da igual (1.03 frente a 0.97). En las animadas, "mándale / etiqueta a alguien" tiene lift **2.06** (n=11).

### 3.3 Tasas de referencia para fijar KPIs [V]

- Videos hispanos de psicología con ≥5K vistas: **guardados/vistas mediana 0.80 % (p90 2.29 %)**; **compartidos/vistas mediana 0.42 % (p90 1.36 %)**.
- Like rate habitual: 5–12 % en cuentas sanas. Por debajo de ~2 % suele indicar contenido pautado o una cuenta en declive (Pictoline 1.5 % por su mezcla con anuncios; Fanny 2.4 %).
- Referentes animados: Lennnie like 16 %, share **8.3 %**, save 1.9 %. Mycanimations like 17 %, share 1.25 %. Alec With Pen like 14 %, share 1.8 %.
- **KPI propuesto [I]** para el personaje de Agenda PSI: share ≥1.5 % (por encima del p90 hispano) y save ≥1.5 %. Con eso el contenido se mantendría por encima del ~85 % del nicho.

### 3.4 Cadencia [V]

- La cadencia **no explica el alcance**. Salama publica 35/semana y tiene una mediana de 4.6K. Carrot publica 1/semana y tiene una mediana de 100K. Lennnie publica ~1/semana y tiene 83K.
- **[I]** Para una producción animada, **3 piezas/semana** de calidad más 2 reciclajes (carrusel o foto) son suficientes. Más volumen no compensa.

---

## 4. Cuentas animadas o con personaje: qué hacen distinto

| Cuenta | Seguidores | Duración típica | Estructura | Texto / voz | Mecánica de distribución |
|---|---|---|---|---|---|
| **Lennnie** @itslennnie (EN) | TT 3.02M, IG 2M [V] | 22–71 s (mediana 44.5 s) | **Saludo "HIIII" (0–1 s)** → frase puente ("I just wanted to remind you that…" / "Whoever sent you this video wanted me to remind you that…") → afirmación en 3–6 planos de 1 frase c/u → metáfora visual (olas, luz en lo oscuro) → cierre "I love you" | Letras manuscritas negras sobre fondo plano (un color por video) + voz suave del creador que dice exactamente lo mismo; blob con ojos grandes en primer plano | **"Mándaselo a alguien"**: share 8.3 %, en picos 12 % de las vistas. Caption con #lennnie #mentalhealth #animation. Colabs de marca (Tatcha) [F] |
| **mycanimations** (EN) | TT 2.42M [V] | 15–61 s | "POV: You have a big sister/older brother" desde el fotograma 0 → recorrido de vida en viñetas → remate tierno | Sin voz; música emotiva; personajes blob de colores planos | Mediana de **2.1M** de vistas (vpf 0.87). Etiquetar al hermano o hermana: 587K compartidos en un video |
| **Alec With Pen** (EN) | TT 148K [V] | 26–58 s | **Serie con episodios** ("Haunted House Husband Ep. 1/2"); imagen intrigante en el fotograma 0 (monstruo sobre la cama); giro final | Voces actuadas + subtítulos grandes palabra por palabra | vpf **1.9** (mediana 283K con 148K seguidores); el Ep. 2 hizo 11.1M |
| **Haley Drew This** (EN) | TT 24K, IG [F] | Carrusel de fotos | Portada manuscrita "Reasons I have FaceTimed my mom" → una razón ilustrada por slide | Texto manuscrito; música | 3.2M en photo mode con la fecha del Día de las Madres |
| **La Psicología Invisible** (ES) | TT 55K [V] | 240–600 s | Título fijo en letterbox ("La psicología de las personas que…") + PARTE N → narración en off con personajes IA | Voz en off; etiqueta IA visible | 2.7M en Parte 1, 58K en Parte 2 |
| **Psych2Go** (EN/ES) | YT 13.2M [F]; Shorts EN mediana ~55K, ES ~9K [V] | Shorts ~30–60 s | Pregunta o afirmación halagadora ("Por qué los inteligentes quieren estar solos") → 3–6 señales → cierre | Voz en off + animación 2D genérica | El título-gancho de identidad ("¿eres de los que…?") funciona en EN; en ES rinde 6× menos |
| **Pictoline – Gato Aurelio** (MX) | IG 2.4M [V] | 45–81 s | Personaje sabio que "deja sus meditaciones" para dar un consejo práctico | Texto en mayúsculas por plano + voz | 4.1 % de guardados en el orgánico de finanzas: **un personaje-mentor que enseña algo útil = guardados** |

**Lo que hacen distinto frente a los psicólogos con cara [I]:**
1. **Hablan en segunda persona afectiva** ("you are", "estoy orgulloso de ti") en vez de explicar en tercera persona ("el narcisista…"). Generan **compartidos**; los psicólogos generan **guardados**.
2. **Una idea por plano**, planos de 1.5–2.5 s, texto en pantalla idéntico a la voz. Accesible sin audio.
3. **Paleta y diseño de personaje ultrasimples** (blob, 2–3 colores, fondo plano). Se reconocen en 0.5 s en el feed, y la producción es barata y serializable.
4. **Ritual de apertura constante** ("HIIII"): la audiencia reconoce la marca antes de leer.
5. **Cuando hay serie, cada episodio es autocontenido** (Alec). La "Parte 2" de un mismo tema (La Psicología Invisible) se desploma.
6. **Las cuentas de cómic estático (72kilos, Flavita, Lola Vendetta) viven en IG (cientos de miles a millones) y casi no existen en TikTok** [V]. El carrusel es su formato natural.

---

## 5. Análisis de 50 TikToks virales en español (y 13 de referencia)

Método: fotogramas en 0/1/2.5/4.5/10 s del embed público, más los metadatos de yt-dlp. Las notas completas, video por video, están en `video_notes.md` (datos crudos). Tabla resumida, ordenada por vistas [V para métricas, observación directa para lo visual]:

| # | Cuenta | Vistas | Dur. | Hook 0–3 s (visual + texto) | Visual | Ritmo | CTA / mecánica |
|---|---|---|---|---|---|---|---|
| 1 | adp.psicologa | 8.3M | 123 s | Caja roja fija "4 cosas que tienes derecho a esperar de tu pareja" + subtítulos | Talking head, estudio en casa | Lista numerada con rótulos de color por punto | Respuesta a comentario; 92K compartidos |
| 2 | marianrojasestape | 7.2M | 432 s | Clip de conferencia en escenario, sin texto | Escenario, luz teatral | Lento, oratoria | Autoridad/marca personal |
| 3 | adp.psicologa | 5.2M | 119 s | Caja roja en 1ª persona "Cuando me elogiaron por mi intelecto en lugar de por mi esfuerzo" + "Hace tiempo os hablé de…" | Talking head | Narrativo | Continuidad con un video previo |
| 4 | lapsicologiainvisible | 2.7M | 240 s | Letterbox con título "La psicología de las personas que lloran cuando se enfadan PARTE 1" | **Animación IA etiquetada**, blobs verdes | Planos de ~2–3 s, narración | Serie (la Parte 2 se cae a 58K) |
| 5 | modernadepueblo | 2.0M | 15 s | Cómic animado, bocadillo "¿Ya te vas?" | Cut-out 2D | Rápido; remate "RANCIAAAA" | Pregunta binaria en el caption |
| 6 | carrotadventure | 1.5M | 207 s | Primer plano extremo, expresión exagerada, franja amarilla | Talking head con estética propia | Monólogo | Tema polémico (hombres y compromiso) |
| 7 | carrotadventure | 1.2M | 598 s | Abre con el clip viral de otra creadora | Reacción/análisis | Corte a él a los ~4 s | Cultura de internet |
| 8 | drcesarlozano | 1.2M | 37 s | Selfie con el mar de fondo, frase reflexiva | Exterior, luz natural | Una idea | Cita para compartir (30.9K compartidos) |
| 9 | modernadepueblo | 1.2M | 25 s | Rótulo amarillo "SOY MENSTRUADORA LIBRE" | Clip de programa | Reacción cómica | Humor |
| 10 | psicologiaanimada | 1.2M | carrusel | "Así llaman al Chavo del 8 fuera de México" | Render IA estilo plastilina | Slides | Nostalgia MX (no es psicología) |
| 11 | marianrojasestape | 1.1M | 41 s | Subtítulos con palabra clave en caja azul | Entrevista en estudio | Frase-sentencia | "Personas que suman" |
| 12 | somosestupendas | 1.1M | 516 s | "Yo me he despedido de Paula…" (duelo) | Entrevista en set cálido | Testimonio largo | Emoción cruda |
| 13 | manuel.arango | 987K | 70 s | "4 Señales Que Eres Físicamente Atractivo" + sello "Según Ciencia" | Talking head + b-roll de stock | Lista con rótulo amarillo por punto | Vanidad + ciencia |
| 14 | desireellamas | 782K | 27 s | Texto "Límites en 2025:" + actuación en contrapicado | Sketch | Parodia | Crítica del mal uso de "límites" |
| 15 | drcesarlozano | 778K | 60 s | Highlight de LIVE, gesto enfático | Casa | Rápido | Lives como cantera de clips |
| 16 | psicologia_instantanea | 715K | 162 s | Caja blanca "La persona narcisista te pide PAZ, pero su paz implica que vos pierdas PAZ" | Selfie | Explicativo | Monotema narcisismo |
| 17 | manuel.arango | 696K | 32 s | Rótulo "Test Psicológico" + imagen de peces (¿lidera o lo persiguen?) | Talking head + gráfico | Interactivo | Fuente académica citada |
| 18 | aliciagonzalez | 666K | 85 s | Selfie en el coche: "es la primera vez que le pongo límites a mi madre" | Confesional | Íntimo | "Por si te sirve" |
| 19 | psicologia_instantanea | 603K | 170 s | Caja roja "El narcisista dice que quiere una relación que le dé PaZ" | Selfie | Explicativo | El mismo insight reciclado |
| 20 | 1minutodepsicologia | 591K | 99 s | Selfie + karaoke amarillo; recomienda una canción para bebés | Selfie + inserto de portada | Ágil | Recomendación útil (16.5K compartidos) |
| 21 | adriansalama | 479K | 32 s | Split-screen: titular "KOMANCHE DESCRIBIÓ SU FUNERAL ANTES DE MORIR" | Clip de famoso arriba, psicólogo-streamer abajo | Subtítulos en mayúsculas | Newsjacking MX |
| 22 | aliciagonzalez | 476K | 71 s | "acabo de poner un límite a mis padres y siento tanta culpa" | Confesional en la cama | Íntimo | — |
| 23 | adriansalama | 472K | 32 s | "PSICÓLOGO ANALIZA A LA CHICA QUE ACUSÓ A KOMANCHE" | Split-screen | — | Serie sobre el mismo caso |
| 24 | paola.lavin | 368K | 86 s | "Cómo la gente cree que se ve una psicóloga 'poco profesional'" | Selfie sonriendo | Humor | Rompe el estereotipo |
| 25 | psicologamassiel | 359K | 130 s | Greenscreen sobre Magaly TV: "¡ESPOSA SACA CARA POR MÚSICO…!" | Chisme de TV + psicóloga en la esquina | — | Pareja a partir del chisme |
| 26 | somosestupendas | 350K | 272 s | Cita en pantalla "¡Madre solo hay una!" + "O SU FELICIDAD O LA MÍA" | Entrevista | — | Familia |
| 27 | 1minutodepsicologia | 315K | 28 s | Selfie + karaoke; recurso gratuito (cuento para niños tras un terremoto) | Selfie | — | Link en la bio |
| 28 | hijademabel | 307K | 35 s | "COSAS QUE NO LE PUEDO DECIR [a un paciente] PERO COMO NO SOS MI PACIENTE…" | Selfie íntimo, subtítulos sobre fondo rojo | Palabra a palabra | Lo que tu psicóloga piensa |
| 29 | centrosoma | 290K | 133 s | Caja serif "Superpoderes del TLP" | Estudio con libros | Explicativo | Disclaimer; 3.3K compartidos |
| 30 | paola.lavin | 281K | 16 s | Meme de texto: "…enséñales el contenido de la cuenta de PROFECO" | Plano fijo | Meme | Humor de nicho MX |
| 31 | cristydelatorre | 275K | 50 s | Caja negra "¿Quieres una prueba de que el universo te está escuchando?" | Selfie en sala | Lento | Espiritualidad (riesgo de pseudociencia) |
| 32 | machyguerrero | 271K | 88 s | "Y si tú me cuentas que le pegaste a tu hijo… Muy mal." | Selfie en el coche | Confrontativo | Crianza |
| 33 | machyguerrero | 265K | 129 s | Karaoke amarillo; cómo explicar la reproducción a los niños | Selfie | — | Pregunta en el caption (607 comentarios) |
| 34 | centrosoma | 191K | 118 s | "TLP y Persona Favorita" + imagen de gatitos con corazones | Estudio | — | Ternura + tema clínico |
| 35 | silviacongost | 168K | 38 s | Subtítulos: "¿cómo saber si estás preparado para una nueva relación?" | Clip de podcast | — | Regla concreta |
| 36 | psicologamassiel | 156K | 112 s | Opinión sobre una noticia política peruana + inserto de noticiero | Consultorio | — | Actualidad local |
| 37 | desireellamas | 144K | 166 s | Caja negra "Te contaron mal el Marshmallow test" + dulces en la mano | Prop físico | — | Desmentido |
| 38 | carlosalanis | 142K | 85 s | Sticker de respuesta a comentario "¿Por qué me siento mejor apenas llego al hospital?" + título | Selfie | — | Comentario como guion |
| 39 | carlosalanis | 117K | 76 s | Cita del paciente: "Me dio ansiedad cuando estaba dormido 😢" | Selfie | — | Síntoma reconocible |
| 40 | fannypsiquiatra | 109K | 514 s | "NO TOMES SERTRALINA SIN ANTES VER ESTO" (plantilla tipo miniatura) | Set con luces | — | Advertencia (solo apto para psiquiatras) |
| 41 | hijademabel | 95K | 6 s | Meme: "Yo (con 11 h de pantalla) cuando mi paciente usa el celu antes de dormir" | Cara de sorpresa | 6 s | Autoironía: 3.5 % de compartidos |
| 42 | silviacongost | 84K | 21 s | Subtítulos grandes de un clip de radio | Radio | — | Frase-sentencia |
| 43 | fannypsiquiatra | 67K | 133 s | Título bicolor "¿Cuándo el PSIQUIATRA pide un perfil TIROIDEO?" | Set + inserto de laboratorio | — | — |
| 44 | kay.psicologiapop | 67K | 11 s | Baile + "Día 1 haciendo de todo pa salir del shadow ban" | Sketch | — | Indicio de restricción de alcance |
| 45 | psicjuanluistigo | 57K | 58 s | Subtítulos con palabra clave en caja roja; se presenta a los ~4 s | Selfie | — | — |
| 46 | jessforense | 39K | 179 s | Sticker "¿qué se necesita para ser psicólogo forense?" | Charla con café | — | Q&A |
| 47 | kay.psicologiapop | 37K | 14 s | Sketch con lápiz (respuesta religiosa) | — | — | Humor |
| 48 | psicjuanluistigo | 29K | 56 s | Sticker de "Preguntas" sobre sexualidad en pareja | Plano reflexivo | — | Serie de Q&A |
| 49 | cristydelatorre | 24.5K | 80 s | Producción de cine (velas, b-roll), rótulos condensados | Alta producción | — | **Rinde 11× menos que su selfie (275K)** |
| 50 | jessforense | 18K | 313 s | Selfie leyendo documentos, sin texto | — | — | Sin hook → bajo |

**Referencia no hispana o pautada (13):** mycanimations ×3 (26.1M, 23.6M, 16.2M), Alec With Pen ×3 (11.1M, 5.2M, 4.6M), Lennnie ×3 (3.8M, 3.7M, 2.0M), Haley Drew This (3.2M en carrusel de fotos), Dr. Julie (1.9M: "I'm a Psychologist and… a little secret" con un cráneo como prop), Pictoline ×2 (pautados).

**Hooks hablados (YouTube Shorts, transcripción automática) [V]:** Desansiedad (508K) arranca **en plena instrucción** ("dentro de nuestro oído vamos a meter el dedo, solo hacer presión…"). Carlos Alanis abre con un prop ("esto es hielo y créeme que no solo sirve para enfriar tu bebida…"). Martín Jardon entra directo a la lista ("principales características del psicópata: la falta de empatía…"). Somos Estupendas abre con un testimonio crudo ("me acuerdo de ver a mi madre sentada en el sofá… no quiero llorar"). **Ninguno empieza con "Hola, soy…".** Cuando hay presentación, va después del hook (Juan Luis Tigo, ~4 s).

### 5.1 Síntesis de la muestra de 50 [V conteo / I interpretación]

- **Texto en pantalla en el primer segundo:** ~44/50. Sin texto: clips de conferencia o LIVE (Marian, Lozano, Carrot, JessForense).
- **Tipos de hook** (un video puede tener más de uno): tesis o lista en caja fija ~24; humor o meme o sketch ~9; newsjacking o cultura pop ~8; clip de autoridad sin texto ~8; confesional o testimonio ~5; respuesta a comentario ~5; prop físico (cráneo, hielo, dulces, gráfico) ~5.
- **Las cajas de texto más usadas**: roja con letra blanca (adp, Jardon), blanca con letra negra (Alanis, Jardon), negra con serif (Centro Soma, Desirée). Siempre en el **tercio superior o medio**, y siempre fijas durante todo el video.
- **Subtítulos**: karaoke palabra a palabra con la **palabra clave resaltada** en amarillo, rojo o morado (1minuto, Juan Luis, Fanny, Marian).
- **Producción**: selfie o celular en ~80 % de los casos. La alta producción no garantiza nada (Cristy: 24.5K frente a 275K).
- **CTA**: casi nunca es "sígueme". Los que funcionan son **implícitos**: pregunta en el caption (comentarios), "por si te sirve" / "envíaselo a…" (compartidos), recurso gratuito en la bio (guardados y clics).

---

## 6. Carruseles de Instagram (y photo mode de TikTok)

### 6.1 Evidencia disponible

- **Benchmarks [F, Socialinsider 2026]**: el carrusel es el formato de IG con mayor engagement (0.50 % en el T3 de 2026 frente a 0.48 % de los Reels). Mediana por publicación: carrusel con 37 guardados contra 35 del Reel; el Reel gana en compartidos (5 frente a 3) y comentarios. Metricool 2026: los carruseles reciben ~9× más guardados que la foto simple [F].
- **Algoritmo IG [F, Adam Mosseri, ene-2025]**: las tres señales principales son tiempo de visualización, likes por alcance y **envíos (sends) por alcance**; los envíos pesan "un poco más" para llegar a no seguidores.
- **TikTok photo mode [F, Buffer 2026]**: el video tiene más engagement mediano (3.39 % frente a 1.92 %), pero el photo mode crece un 140 % en volumen [F, Metricool]. **[V]** Haley Drew This hizo 3.2M y el carrusel IA del Chavo hizo 1.2M en photo mode.
- **Mezcla de formatos observada en IG** (últimas 12 publicaciones, perfil público) [V]: Somos Estupendas 5 carruseles / 5 reels; 1minutodepsicologia 6 carruseles / 3 reels / 3 fotos; Flavita Banana 6 carruseles / 6 fotos / 0 reels; La Mente es Maravillosa 8 reels / 4 fotos / 0 carruseles. **Las cuentas de psicólogos e ilustradores mantienen alrededor de un 50 % de carruseles; los medios se pasaron a reels.**

### 6.2 Estructuras de portada observadas [V, captura de la cuadrícula pública]

- **Somos Estupendas**: frase-testimonio grande en serif sobre un color pleno apagado ("Lo que viene después del Abuso Sexual Infantil duele. (y mucho)"), o foto de la entrevistada con la cita superpuesta y un rótulo con su nombre y "Psicóloga especializada".
- **1minutodepsicologia**: (a) **check-in emocional con cultura pop**, "¿Cuál Robert Pattinson te representa el día de hoy?", una cuadrícula de 9 imágenes numeradas que invita a comentar el número; (b) cita de famosa ("¡ME ENCANTA EL ENOJO!" – Alanis Morissette); (c) "Juego para trabajar la frustración y resiliencia" (recurso práctico para guardar); (d) slide de texto largo tipo nota ("Regresar al trabajo después de un mes…"); (e) ilustración de bebé con título "HABILIDAD FÍSICA" (serie de desarrollo infantil).
- **Flavita Banana / 72kilos / Lola Vendetta**: viñeta única dibujada a mano, texto manuscrito y una idea irónica. En carrusel, tira de 2–6 viñetas.

### 6.3 Plantilla de carrusel recomendada [I, a partir de lo anterior y de los guardados de TikTok]

1. **Slide 1 (portada):** promesa concreta o identificación en ≤8 palabras ("5 señales de que no es flojera, es agotamiento"). El personaje expresa la emoción y no hay logo grande.
2. **Slide 2:** validación ("Si te pasa, no estás roto/a") con el personaje en la escena cotidiana.
3. **Slides 3–7:** un punto por slide (número grande, frase de ≤20 palabras, mini-ilustración). **Las listas numeradas tienen lift de 2.4 en TikTok.**
4. **Slide 8:** **herramienta guardable** (ejercicio de 3 pasos, frase para decir, mini check-list). Es lo que más se guarda.
5. **Slide 9:** "¿Cuál te pasa más? Comenta el número" (comentarios) **o** "Mándaselo a quien necesite leer esto" (envíos).
6. **Slide 10:** cierre suave de marca ("Si esto se siente pesado, hablar con un psicólogo ayuda · agendapsi.mx") + fuente o credencial del revisor clínico + línea de ayuda cuando el tema lo requiera.
- **Estilo:** fondo de color pleno (un color por serie), tipografía redonda grande, personaje en todas las slides y alto contraste. Formato 4:5 (1080×1350). La misma pieza se reutiliza en photo mode de TikTok.

---

## 7. Riesgos y políticas

### 7.1 Etiquetado de IA

| Plataforma | Regla | Implicación para un personaje animado |
|---|---|---|
| **TikTok** | Las Community Guidelines (Integridad y autenticidad) exigen etiquetar "AI-generated or significantly edited content that shows **realistic-looking** scenes or people". El contenido sin etiqueta "may be removed, restricted, or labeled" [V, página oficial leída hoy]. Detección automática por C2PA [F]. Las etiquetas automáticas no se pueden quitar [F] | Una animación **estilizada y no realista** no cae en la obligación literal [I]. **Recomendación:** si usamos IA generativa en imagen o voz, activar el toggle "AI-generated" de todos modos. @lapsicologiainvisible lleva la etiqueta visible y aun así hizo 2.7M [V] |
| **Instagram/Meta** | Divulgación obligatoria para **video fotorrealista o audio realista** creado o alterado con IA (herramienta "AI info"). Las imágenes fijas no son obligatorias. Meta autoetiqueta por C2PA/IPTC [F, varias fuentes secundarias; no pude abrir la página de Meta, que dio 404]. Perfiles con una "persona generada por IA" → etiqueta de perfil [F] | Una **voz sintética realista** probablemente sí requiere la etiqueta [I]. Si la voz es humana (actor o actriz), no hace falta |
| **YouTube** | Desde el 16/07/2026, el apartado de "inauthentic content" del YPP no monetiza: (1) contenido genérico, repetitivo o de plantilla; (2) contenido angustiante o manipulador; (3) **"AI personas" que hablan de temas sensibles: salud, medicina, finanzas, legal**. TechCrunch define AI persona como "representaciones de personas reales hechas con IA" [F, TechCrunch 20/07/2026] | **Riesgo alto si el personaje parece un "psicólogo IA".** Mitigación [I]: un personaje claramente ficticio (no humano realista), un **guion escrito y revisado por psicólogos con cédula**, un psicólogo real que aparezca o se cite ("revisado por Psic. X, céd. ####"), y **variación real entre episodios** para no caer en el criterio de plantilla repetitiva |

### 7.2 Autolesión, suicidio y TCA

- **TikTok [V, oficial]**: "We don't allow showing, promoting, or sharing plans for suicide or self-harm". Tampoco contenido que promueva TCA o el control de peso riesgoso. TikTok puede contactar a servicios de emergencia y redirige a líneas de ayuda. El contenido de desinformación de "daño moderado" no es elegible para el feed Para Ti [V].
- **Meta [F, AP, ene-2024]**: oculta a los adolescentes contenido de suicidio, autolesión y TCA **aunque lo publique una cuenta que siguen**, incluidos testimonios de recuperación. **[I]** Un video sobre autolesión, aunque sea preventivo, perderá alcance entre menores en IG.
- **Indicio de restricción [V]**: Karime Fajer publica "Día 1 haciendo de todo pa salir del shadow ban", y la cuenta de Elsa Gómez (>1M antes) hoy tiene 0 videos.
- **Buenas prácticas [I]**: no mostrar métodos, heridas ni cifras de peso; usar lenguaje no sensacionalista; siempre incluir un recurso de ayuda en pantalla y en el caption en México, la **Línea de la Vida 800 911 2000** (24/7, gratuita; CONASAMA [F]) y el **911** en emergencia. Tratar el tema desde las señales de alerta y cómo acompañar a alguien, no desde la experiencia gráfica. Evitar las palabras gancho que activan moderación ("suicidio" en el texto de portada) y preferir "pensamientos de no querer estar aquí", siempre que el mensaje siga siendo claro.

### 7.3 Otros riesgos

- **Publicidad de servicios de salud en México [F]**: COFEPRIS publicó en sept-2024 la "Guía de roles y responsabilidades de publicidad por influencia" (GRRUPI) y retira miles de anuncios irregulares. Fuentes de divulgación legal dicen que promocionar servicios de salud requiere aviso de publicidad. **[I]** Si el canal promociona la reserva de citas con psicólogos, conviene revisarlo con un abogado sanitario. El contenido puramente divulgativo tiene menos riesgo.
- **Pseudociencia**: varias cuentas grandes mezclan psicología con "el universo te escucha" o astrología (la "Itziar Psicóloga" de YouTube publica eclipses y lunas). **[I]** Diferenciarse con evidencia y citas (Manuel Arango cita a Morris, Nisbett & Peng, 1995).
- **Medicamentos**: lo hacen los psiquiatras (Fanny: "NO TOMES SERTRALINA…"). **[I]** Agenda PSI conecta con psicólogos, así que debe evitar consejos farmacológicos.
- **Autodiagnóstico**: hay críticas en prensa (Maldita.es, BioBioChile) [F]. Centro Soma pone un disclaimer fijo y rinde bien (lift 1.72). **[I]** Incluir "esto no es un diagnóstico" en los temas clínicos.

---

## 8. Recomendaciones accionables para el personaje de Agenda PSI [I]

### 8.1 Formato base: "60–90 s, una idea, personaje + texto + voz"

**Estructura de guion (≈75 s):**
| Tiempo | Bloque | Qué hacer |
|---|---|---|
| 0–1 s | **Ritual + tesis visible** | Saludo corto del personaje (marca sonora) y **caja de texto fija** con la tesis o la lista ("3 señales de que tu cansancio es emocional") en el tercio superior, presente todo el video |
| 1–3 s | **Identificación** | Escena cotidiana mexicana reconocible (metro, oficina, WhatsApp de la mamá) y una frase en 2ª persona |
| 3–60 s | **Desarrollo numerado** | 3–5 puntos, una frase por plano (1.5–2.5 s), voz humana cálida + subtítulos karaoke con la palabra clave resaltada |
| 60–70 s | **Herramienta** | Un ejercicio o frase concreta para guardar ("dile esto: …") |
| 70–75 s | **Cierre afectivo + CTA implícito** | "Mándaselo a quien necesite oírlo" o "¿Cuál te pasa más? 1, 2 o 3". Firma suave: "Hablarlo con un psicólogo ayuda · Agenda PSI" |

### 8.2 Tres líneas editoriales (mezcla semanal sugerida)

1. **"Te lo explico" (guardables, 2/sem):** señales, técnicas de ansiedad (respiración, grounding, nervio vago), límites con la familia, apego. Lista numerada.
2. **"Para ti" (compartibles, 1/sem):** afirmación afectiva estilo Lennnie, adaptada a México ("Si alguien te mandó esto es porque te quiere y quiere recordarte que…"), 30–45 s.
3. **"Lo que tu psicólogo no te dice" / humor (1/sem):** autoironía y situaciones de terapia con cariño (hijademabel, Paola Lavín). Opcionalmente, **cultura pop o actualidad MX** comentada con cuidado (Komanche, telenovelas, el Chavo), que suma ×1.29.
- **Carrusel IG / photo mode:** el mismo tema de la línea 1 cada semana, reconvertido en 8–10 slides (plantilla del §6.3).
- **Series:** episodios **autocontenidos** con personajes recurrentes (la mamá, el ex, el jefe), no "Parte 1/2" de un mismo tema.

### 8.3 Temas con mejor evidencia en el nicho hispano

Familia y crianza (culpa al poner límites a los padres, heridas de la infancia), narcisismo y relaciones, ansiedad física (síntomas, técnicas), TLP/TDAH/autismo explicados sin estigmatizar (con disclaimer), autoestima y "X señales según la ciencia".

### 8.4 Credencial y confianza

- Mostrar **"Guion revisado por Psic. [Nombre], Céd. Prof. ####"** en la portada del carrusel y en el caption. En los videos, un *lower third* breve al final. Todos los psicólogos top lo ponen en la bio (§2.1).
- Ocasionalmente, **"el psicólogo real responde al personaje"** (dúo): combina la ventaja de compartibilidad del personaje con la autoridad humana.

### 8.5 KPIs iniciales (TikTok, por video, a los 7 días)

- Retención ≥40 % al segundo 3 (en analytics). **Share ≥1.5 %**, **save ≥1.5 %**, like ≥8 %.
- Los referentes hispanos están en save 0.8 % y share 0.42 % de mediana. Superar el p90 (2.3 % / 1.4 %) es una señal de producto-mercado.

---

## 9. Limitaciones

- La muestra viral es **"top por cuenta"**, no un ranking global por hashtag (TikTok bloqueó hashtags y Creative Center). Sesgo hacia cuentas ya conocidas.
- Los últimos ~60 videos por cuenta cubren periodos distintos (de semanas a años, según la cadencia).
- Los fotogramas son del embed sin audio. La presencia de voz se infiere por los subtítulos, el campo de audio ("sonido original") y 8 transcripciones de YouTube.
- Los datos de IG son solo seguidores y mezcla de formatos; **no hay guardados ni likes de IG**.
- El crecimiento se compara contra cifras de prensa, no contra series históricas.
- Políticas: TikTok se leyó en la página oficial. Meta y YouTube se tomaron de prensa y blogs, porque la página de Meta dio 404 y no abrí la de YouTube. **Conviene verificarlas antes del lanzamiento.**

---

## 10. Archivos de datos crudos (scratchpad)

Ruta base: `/tmp/claude-0/-home-user-Creador-de-videos-Para-redes-/f6e80049-54f1-5e5b-b0dd-1d5ea884d7d2/scratchpad/research/social/`
- `tt_account_metrics.csv`: métricas por cuenta de TikTok (seguidores, cadencia, medianas, tasas, duraciones).
- `account_map_merged.csv`: lo mismo más los seguidores de IG.
- `tt_all_videos.csv`: 2,229 videos con vistas, likes, guardados, compartidos, comentarios, duración, audio, fecha y caption.
- `tt_videos/*.json`: salida cruda de yt-dlp por cuenta.
- `tt_batch*.json`: perfiles de TikTok (bio, verificación, totales).
- `selected_videos.csv`: los 64 videos analizados; `frames/` y `sheets/`: sus fotogramas y hojas de contacto.
- `video_notes.md`: notas cualitativas video por video y transcripciones de hooks.
- `caption_feature_lift.txt`, `top_save_share.txt`: análisis de lift y rankings por guardados y compartidos.
- `ig_profiles_raw*.jsonl`, `ig_followers_snapshot.json`, `ig_posts_grid.jsonl`, `ig_grids/`: Instagram.
- `yt/`: listados de Shorts por canal, búsquedas y subtítulos.
- `scripts_usados/`: scripts de extracción (Python y Playwright).

## Fuentes secundarias consultadas

- Saludiario, "Los psicólogos influencers más famosos de México" (ene-2024): https://www.saludiario.com/psicologos-mas-famosos-de-mexico/
- BrandMe, "Top 10 psicólogos en TikTok": https://brandme.la/top-10-psicologos-en-tiktok-que-promueven-la-salud-mental-con-su-contenido/
- Domestika, "21 influencers de Instagram que hablan de salud mental": https://www.domestika.org/es/blog/9362-21-influencers-de-instagram-que-hablan-de-salud-mental
- COMSalud, "15 divulgadores sanitarios más influyentes de TikTok 2025": https://comsalud.es/los-15-divulgadores-sanitarios-mas-influyentes-de-tiktok-en-2025/
- BioBioChile sobre Carrot Adventure y autodiagnóstico (feb-2024): https://www.biobiochile.cl/noticias/servicios/explicado/2024/02/03/tiktok-me-diagnostico-los-peligros-de-trivializar-y-promover-los-trastornos-mentales-en-rr-ss.shtml
- El Español, viñetas de salud mental (2022): https://www.elespanol.com/enclave-ods/historias/20220121/salud-mental-instagram-vinetas-empujon-personas-terapia/643935640_0.html
- CreatorDB, Psych2Go: https://creatordb.app/creatorstats/psych2go/
- TikTok Community Guidelines, Integridad y autenticidad: https://www.tiktok.com/community-guidelines/en/integrity-authenticity
- TikTok Community Guidelines, Salud mental y conductual: https://www.tiktok.com/community-guidelines/en/mental-behavioral-health
- TechCrunch, "YouTube clarifies policies around AI slop and upsetting videos" (20/07/2026): https://techcrunch.com/2026/07/20/youtube-clarifies-policies-around-ai-slop-and-upsetting-videos/
- Storrito, reglas de etiquetado IA de TikTok 2026: https://storrito.com/resources/tiktoks-2026-ai-labeling-rules-and-what-they-signal-for-platform-governance/
- Hootsuite, política de divulgación de IA en Instagram: https://blog.hootsuite.com/ai-disclosure-policy-for-instagram/
- AP vía KUTV, Meta oculta contenido de suicidio y TCA a adolescentes (ene-2024): https://kutv.com/news/nation-world/meta-to-hide-suicide-eating-disorder-posts-from-teens-instagram-facebook-feeds-social-media-self-harm-restrictions-settings-search-terms
- Socialinsider, benchmarks de Instagram 2026: https://www.socialinsider.io/social-media-benchmarks/instagram
- Social Media Today, señales de Mosseri 2025: https://www.socialmediatoday.com/news/instagram-shares-algorithm-2025/738034/
- Buffer, mejor formato 2026: https://buffer.com/resources/data-best-content-format-social-media/
- Metricool, tendencias de TikTok 2026: https://metricool.com/tiktok-trends-going-viral/
- Expansión, guía COFEPRIS para influencers (sept-2024): https://expansion.mx/mercadotecnia/2024/09/05/nueva-guia-de-influencers-pero-ahora-de-la-cofepris
- Línea de la Vida (referencias): https://www.therapyroute.com/article/suicide-hotlines-and-crisis-lines-in-mexico
