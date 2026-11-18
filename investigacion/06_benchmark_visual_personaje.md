# 06 · Benchmark visual de personajes y direcciones para Agenda PSI

Fecha: 18-nov-2026. Ronda 2 de investigación.

**Leyenda.** [V] = dato verificado: medido con yt-dlp, visto en un fotograma o citado de una fuente. [I] = inferencia o juicio de diseño.

**Material de estudio** (en `investigacion/referencias_visuales/`, solo para uso interno):

| Archivo | Contenido |
|---|---|
| `00_panel_benchmark_personajes.jpg` | Un fotograma de cada uno de los 22 referentes |
| `01_panel_miniaturas_top_vs_low.jpg` | Miniaturas de los videos con más y menos vistas, por canal |
| `02_direcciones_bocetos.png` + `.html` | Bocetos esquemáticos de las 6 direcciones, con prueba de silueta y de avatar de 48 px |
| `miniaturas/` | 120 miniaturas de 320×180: top 3 y bottom 4 de cada canal |
| `fotogramas/` | 174 fotogramas de 480 px tomados a mitad de video |
| `datos/` | Listas de los últimos ≤150 videos de cada canal, con vistas, y `datos_vistas_canales.json` |

---

## 0. Resumen ejecutivo

1. **El personaje recurrente explica cuánta gente reconoce y vuelve al canal. El tema explica qué video concreto explota.**
   - En los canales que tienen un personaje fijo, la diferencia entre el video más visto y el menos visto la marca el tema o concepto, no el dibujo. Pasa en La Psicología Invisible, TheOdd1sOut, Jaiden y Casi Creativo. [V]
   - En las marcas que alternan miniaturas con mascota y sin ella, las miniaturas con mascota dominan el top:
     - Duolingo: 3 de 3 en el top con Duo, frente a 0 de 4 en el fondo.
     - Headspace: 3 de 3 en el top con su carita, frente a 1 de 4 en el fondo.
     - Psych2Go: 2 de 3 en el top con su mascota de protagonista, frente a 0 de 4 en el fondo. [V]
2. **La consistencia de estilo pesa más que el pulido.** [V/I]
   - Escéptico usa imágenes de IA sin personaje y con un estilo distinto en cada video. Su mediana es de 1,450 vistas por video. [V]
   - Psych2Go tiene 13.2M de suscriptores, pero su mediana es de 65K vistas (0.5% de sus suscriptores). Su mascota cambia de estilo entre un video y otro, porque la dibujan animadores distintos (se ve en `fotogramas/psych2go_*`). [V] Que esa inconsistencia contribuya a la caída es una hipótesis. [I]
3. **Ya hay territorio ocupado que conviene evitar:**
   - cabeza blanca redonda: TheOdd1sOut y Casi Creativo;
   - figura humanoide alargada color salvia sobre fondo crema: La Psicología Invisible;
   - ser azul con cabeza de gota: Strange Planet;
   - **cerebro con cara: Pictoline/Cartoon Network en México** ("La vida secreta de tu mente");
   - **brote o hoja en la cabeza: la mascota de Psych2Go**. Esto afecta directamente al concepto "C · Brote" de `personaje/exploracion/REFERENCIAS_Y_PROMPTS.md`;
   - blob rosa malva: Lennnie.
4. **Lo que hoy suena a "IA genérica":**
   - en la imagen: tinte amarillo o sepia, acabado liso y "plástico", fondos sobredetallados que cambian de un plano a otro, personaje que muta entre escenas, manos y texto raros, estética de óleo antiguo o de "libro ilustrado" de ChatGPT;
   - en el formato: imágenes fijas con zoom, voz sintética y guion de muletillas.

   Merriam-Webster eligió "slop" como palabra del año 2025. McDonald's Países Bajos retiró su anuncio de IA en 3 días. En los comentarios de LPI ya se critican los "errores visuales de la IA" (ronda 1). [V]
5. **Recomendación** [I]:
   - **Base:** la dirección **1 "Mechón"**: humano geométrico de unas 3 cabezas de alto, con un mechón en onda que funciona como rasgo firma y como barómetro emocional. Es la única de las seis que pasó la prueba de silueta y la de avatar de 48 px sin depender del color.
   - **Color:** la paleta mexicana de la dirección **2 "Barro"** (terracota, añil, cempasúchil, jade).
   - **Acabado:** el "line boil" (trazo que tiembla) y el grano de papel de la dirección **3**, como señal de hecho a mano.
   - **Coste:** todo se anima con un rig SVG por código (unas 12 piezas y 6 bocas) a bajo coste.

---

## 1. Método y limitaciones

**Listas y vistas** [V]
- Con `yt-dlp --flat-playlist` bajé los últimos ≤150 videos de cada canal, con sus vistas y su duración.
- Para cada canal calculé la mediana de vistas y separé los 3–4 videos con más vistas y los 4 con menos.
- También obtuve el número de suscriptores de cada canal.

**Miniaturas** [V]
- Bajé la miniatura `mqdefault` (320×180) de cada video top y bottom: 120 imágenes en total.

**Fotogramas** [V]
- La descarga de video la bloqueó YouTube ("Sign in to confirm you're not a bot"). Como alternativa usé los fotogramas que YouTube genera solo (`sd1/sd2/sd3.jpg`), que caen más o menos al 25, 50 y 75% del video.
- Son 3 fotogramas por video, de los 3 videos top de cada canal y de 7 referencias extra (tráiler de Strange Planet, Pictoline, Molang, Sarah's Scribbles y Psicología Animada).
- Les recorté las franjas negras y los reduje a 480 px.

**Paletas** [V, aproximadas]
- Las saqué con cuantización median-cut sobre el conjunto de fotogramas y miniaturas de cada canal.
- Además muestreé píxeles directamente sobre el personaje.
- Cuando conozco el color oficial de la marca lo indico aparte.

**Límites**
- El nivel de animación se infiere de los fotogramas, del formato y de conocimiento público. No se midió fotograma a fotograma. [I]
- Las medianas mezclan videos de distintas edades. En canales que suben poco (Oversimplified, TheOdd1sOut) la ventana abarca muchos años, así que la proporción vistas/suscriptores sirve como señal, no como métrica limpia.
- La relación entre estilo y rendimiento es correlacional: el tema, la duración, la antigüedad y el algoritmo también influyen.
- Instagram y TikTok no se midieron. Lennnie, Strange Planet y Sarah's Scribbles viven sobre todo ahí.

---

## 2. Tabla maestra de los 22 referentes

"Cab." = alto del personaje medido en cabezas. Las vistas son la mediana de los últimos ≤150 videos.

| # | Canal | Subs | Mediana de vistas | Vistas/subs | Tipo de personaje | Cab. | Animación |
|---|---|---|---|---|---|---|---|
| 1 | **La Psicología Invisible** (LPI) | 256K | 38K | 15% | Semihumano: figura humanoide sin rasgos | ~5–6 (cabeza y cuerpo en una sola pieza, sin cuello) | Imágenes fijas + zoom o paneo [I] |
| 2 | **Casi Creativo** | 8.79M | 5.8M | 66% | Humano estilizado + órganos y comida personificados | ~2.5 | Cutout/rig 2D con lipsync |
| 3 | **Psych2Go** | 13.2M | 65K | 0.5% | Semihumano kawaii (cuerpo blanco con brote) + humanos anime | ~2 | Animatic o animación limitada; varios animadores |
| 4 | **Sprouts** | 1.95M | 159K | 8% | Humanos realistas en boceto | 6–7 | Draw-on con plantilla (MinuteVideos) |
| 5 | **The School of Life** | 9.81M | 194K | 2% | Humano editorial, sin personaje fijo | 6–7, alargados | 2D limitada; un ilustrador distinto por video |
| 6 | **Kurzgesagt** | 25.8M | 10M | 39% | Humanos geométricos + pájaro mascota | 5–6 | Motion design completo (coste alto) |
| 7 | **TED-Ed** | 23M | 417K | 1.8% | Humano ilustrado; cambia por animador | 5–7 | 2D completa |
| 8 | **Escéptico** | 79K | 1.45K | 1.8% | Ninguno: retratos IA "de óleo" o caricatura variable | — | Fijas + subtítulos |
| 9 | **After Skool** | 3.79M | 613K | 16% | Caricaturas a mano (whiteboard) | 4–6 | Time-lapse de dibujo con mano real |
| 10 | **Headspace** | 1.17M | 11K | 0.9% | Abstracto: formas con cara | — | Loop mínimo (sus 3 fotogramas son casi idénticos) |
| 11 | **Duolingo** | 7.1M | 163K | 2.3% | Animal (búho) | ~1.3 | 2D/3D + botarga en acción real |
| 12 | **TheOdd1sOut** | 20.9M | 27M | 129% | Humano estilizado blanco | ~2 | Limitada, poses sostenidas |
| 13 | **Strange Planet** (IG/Apple TV+) | — | — | — | Semihumano (seres azules) | ~3 | Webcomic estático; 2D en la serie |
| 14 | **Sarah's Scribbles** (IG/libros) | — | — | — | Humano estilizado | ~2.5–3 | Webcomic estático |
| 15 | **Lennnie** (TikTok/IG) | 50K en YT | 6.3K | 12% | Abstracto: blob | ~1 | 2D simple + fondos cálidos detallados |
| 16 | **Domics** | 7.15M | 6.1M | 85% | Humano manga-chibi | 3–4 | Frame a frame limitado |
| 17 | **Jaiden Animations** | 15.3M | 18M | 118% | Humano estilizado | ~2.5 | Frame a frame limitado |
| 18 | **OverSimplified** | 9.69M | 40M | 413% | Humano caricatura | ~2.5 | Cutout sobre mapas |
| 19 | **Life Noggin** | 3.12M | 59K | 1.9% | Semihumano cuadrado ("Blocko") | ~2 | Vector limitado |
| 20 | **Pictoline · La vida secreta de tu mente** (CN/HBO Max, MX) | — | — | — | Cerebro antropomorfo | head = cuerpo | 2D de TV, completa |
| 21 | **Psicología Animada** | — | — | — | Humanos de plantilla (tipo Vyond) | ~6 | Plantilla de marionetas |
| 22 | **Molang** | — | — | — | Animal (conejo) | ~1.3 | 2D limitada |

### 2.1 Rasgos faciales, paleta, línea y textura

| # | Canal | Rasgos faciales | Paleta (hex aprox.) [V] | Línea y textura |
|---|---|---|---|---|
| 1 | LPI | Ojos punto pequeños; casi nunca boca. La postura carga la emoción. | Figura salvia `#8E9C8A`–`#9FAC9B`; fondo crema `#F1F0E4`/`#F4F3E9`; sombra `#50473E`; texto de miniatura amarillo ~`#FFD200` sobre negro. | Contorno fino; grano de lápiz o "libro ilustrado"; fondos muy detallados. |
| 2 | Casi Creativo | Ojos enormes de esclera blanca y pupila pequeña; cejas; boca grande; pecas. | Piel blanca `#FDFCFE`; contorno `#2D2434`; fondos `#B76F6A`, `#4D6478`, `#A8C9C2`. | Línea negra gruesa y uniforme; color plano; a veces fondos de foto. |
| 3 | Psych2Go | Ojos kawaii, rubor, lágrimas. | Rosas `#DB7190`/`#FADCDF`, magenta `#B42667`, noche `#1B273B`, aqua `#9DD3D8`. | Varía por animador: de línea limpia a pintura con brillo. |
| 4 | Sprouts | Rostros realistas. | Blanco; piel `#EFDED2`; gris `#878B92`; tinta `#4D3535`; acentos planos. | Línea de tinta a mano; sin textura. |
| 5 | School of Life | Rasgos mínimos; la emoción se cuenta con metáforas visuales. | Durazno `#FBE4D3`, verde agua gris `#94B4AF`, azul `#5E809F`, ciruela `#73515E`, salvia `#8FA08A`. | Línea fina; grano tipo risograph; mucho espacio vacío. |
| 6 | Kurzgesagt | Ojos simples; poca expresión. | Azul profundo `#22408D`/`#0F0746`, magenta `#D82961`/`#970A7B`, violeta `#350C53`, brillos cálidos. | Sin contorno; degradados y glow. |
| 7 | TED-Ed | Rasgos dibujados (nariz, labios). | Crema `#FAF8E4`, rosa viejo `#C27E7C`, aqua `#91D4D2`, índigo `#231B48`. | Pincel y papel; textura visible. |
| 8 | Escéptico | Rostros realistas de "pintura". | Oscuros `#444A4A`/`#34312F`/`#232829`, ocre `#7C8855`. | Pseudopintura con barniz; textura de IA. |
| 9 | After Skool | Caricatura expresiva. | Blanco `#FFFEFE` + marcadores saturados. | Marcador real; papel blanco. |
| 10 | Headspace | Ojos de arco y sonrisa de una línea. | Naranja de marca `#F47D31` (oficial); amarillo `#F8D308`; azul `#1673EE`/`#055FEC`; rosa `#F69FB6`; morado `#472176`. | Sin línea; formas planas con degradado suave. |
| 11 | Duolingo | Ojos enormes, pico, cejas. | Verde oficial "Feather" `#58CC02`; en sus videos, `#698606`. | Formas redondeadas sin contorno. |
| 12 | TheOdd1sOut | Ojos óvalo; boca grande con interior rojo. | Blanco `#FEFFFE`; sombra lavanda `#C4B7B6`; fondos de color. | Línea oscura; plano. |
| 13 | Strange Planet | Ojos grandes con brillo; cejas. | Azul `#93B4DA`; rosas `#D28BBD`; morado `#503961`. | Contorno de color; plano. |
| 14 | Sarah's Scribbles | Pelo enmarañado negro; ojos círculo grandes con ojeras. | Blanco y negro `#040404`. | Tinta; nada de textura. |
| 15 | Lennnie | Ojos enormes con doble brillo. | Malva `#CCA0C1`; tinta `#542B24`. | Línea simple; fondos cálidos muy detallados. |
| 16 | Domics | Ojos punto o anime, simples. | Blanco y negro + grises. | Línea fina; sin color. |
| 17 | Jaiden | Ojos óvalo simples; **silueta del pelo como firma**. | Piel blanca; pelo `#1B1745`; acentos de color. | Línea oscura; plano con trama en miniaturas. |
| 18 | OverSimplified | Cabezas redondas, cejas fuertes. | Realista apagada + mapas. | Línea; plano. |
| 19 | Life Noggin | Rasgos de píxel. | `#20C4D9`, `#D00E3B`, `#25E9B4`. | Bloques planos. |
| 20 | Pictoline | Ojos grandes, cejas expresivas. | Rosa cerebro `#CA799F`, violetas `#551D79`/`#2D244D`. | Línea + color de TV, con luces. |
| 21 | Psicología Animada | Genéricos de plantilla. | Aqua `#48D3BD`, oliva `#A9A473`. | Vector de plantilla. |
| 22 | Molang | Ojos punto y boca "3". | Pastel `#B3E8F7`, `#DBABB9`. | Línea marrón suave. |

### 2.2 Cómo muestra la emoción y qué lo hace icónico

| # | Canal | Cómo muestra la emoción | Qué lo hace icónico (o qué le falta) [I] |
|---|---|---|---|
| 1 | LPI | Postura: encorvado, brazos caídos, señalar. | Color salvia + postura melancólica + fondo crema. Le falta: el personaje cambia de cuerpo entre escenas y en el mismo plano aparecen humanos realistas. |
| 2 | Casi Creativo | Ojos, cejas y boca exagerados. | La cabeza blanca redonda y los órganos con cara. El formato "Tus órganos cuando…" es un activo del canal tanto como el personaje. |
| 3 | Psych2Go | Lágrimas y rubor. | El brote en la cabeza. La inconsistencia de estilo lo debilita. |
| 4 | Sprouts | Gestos realistas. | Bajo: es una estética de plantilla. |
| 5 | School of Life | Metáforas visuales. | El tono y la tipografía, no un personaje. |
| 6 | Kurzgesagt | Escala y metáfora, más que caras. | La paleta neón sobre azul y el pájaro. Se reconoce en un fotograma. |
| 7 | TED-Ed | Gesto y escena. | La calidad, no un personaje. |
| 8 | Escéptico | Rostros "trágicos". | Nada: cada video se ve distinto. |
| 9 | After Skool | Caricatura + texto. | El gesto de la mano dibujando. |
| 10 | Headspace | Dos líneas cambian toda la expresión. | La carita mínima y el naranja. En 2024 ampliaron el rango a estrés y tristeza. |
| 11 | Duolingo | Exageración extrema. | Color propio + ojos + personalidad, y el meme de la notificación. |
| 12 | TheOdd1sOut | Boca y cejas. | La cabeza blanca enorme. Gorra o peinado distinguen a cada personaje. |
| 13 | Strange Planet | Ojos y cejas. | El azul + el lenguaje literal ("describir lo humano desde fuera"). |
| 14 | Sarah's Scribbles | Ojos exagerados. | El pelo y los ojos con ojeras. Humor de ansiedad. |
| 15 | Lennnie | Ojos y voz suave. | Forma + voz + mensaje de autocuidado. |
| 16 | Domics | Cara y gesto. | Autobiografía relatable. |
| 17 | Jaiden | Cara y gesto. | La silueta del pelo + la plantilla de miniatura con su avatar en la esquina. |
| 18 | OverSimplified | Caricatura facial. | Cabezas calvas redondas + humor. |
| 19 | Life Noggin | Ojos. | Cabeza cuadrada. |
| 20 | Pictoline | Ojos y cejas. | **"Cerebro con cara" ya está ocupado en México.** |
| 21 | Psicología Animada | Mínima. | Nada: de plantilla. |
| 22 | Molang | Ojos mínimos. | Una forma reconocible al instante. |

---

## 3. Fichas breves: lo que se aprende de cada referente

1. **La Psicología Invisible.** Fotogramas en `fotogramas/psicologia_invisible_*`.
   - Su gran acierto es conceptual: el personaje sin rasgos sirve de espejo y los temas son rasgos cotidianos no patológicos. Es lo más cercano al tono que busca el fundador. [I]
   - Visualmente se aprecian:
     - personas realistas con manos detalladas junto a la figura estilizada;
     - otras criaturas de colores con un acabado distinto;
     - cambios de grosor y de cuerpo del personaje entre escenas;
     - fondos de "ilustración de libro" muy recargados.

     Son señales compatibles con imágenes generadas por IA. Los comentarios recogidos en la ronda 1 critican los "errores visuales de la IA". [V/I]
   - Miniaturas: el personaje hace una acción concreta con un objeto (pastel, máquina, casa) + 2–4 palabras en un bloque amarillo sobre negro. Los éxitos y los fracasos usan la misma plantilla: lo que decide es el tema. [V]
   - Lección: el espejo neutro funciona. Hay que hacerlo con consistencia de rig y sin rastro de IA.
2. **Casi Creativo.** Mediana de 5.8M.
   - Sus éxitos son **personificaciones de órganos y comida** (40M en "Tus órganos cuando estás embarazada") y sketches familiares mexicanos ("Amenazas de madre", 27M). [V]
   - El humano es solo uno de los registros: el canal es un universo de cosas con cara.
   - Lección: la cabeza grande con ojos de esclera blanca da una expresividad máxima para el humor. El "elenco secundario" de cosas con cara multiplica los temas posibles.
3. **Psych2Go.**
   - El top 1 (1.4M) es la mascota haciendo una pose absurda sobre fondo rosa, con texto corto. [V]
   - En los fotogramas, la mascota aparece en 3 estilos distintos: línea simple, kawaii pintado y 3D-ish con brillos. [V]
   - Lección: una mascota sin una guía de estilo estricta se diluye.
4. **Sprouts.**
   - Usa plantillas whiteboard (marca de agua "MinuteVideos"). [V]
   - El top (19M, "Pygmalion") lo explica el tema de libro de texto.
   - Lección: sirve para temas de psicología "de examen". No construye marca.
5. **The School of Life.**
   - En el top, ilustración editorial plana con figuras pequeñas y mucho espacio vacío. En el fondo, collage de fotos (44K). [V]
   - Lección: el minimalismo editorial cálido rinde mejor que la foto, incluso en el mismo canal.
6. **Kurzgesagt.**
   - El top lo forman temas espectaculares sin el pájaro. El pájaro sale en los videos de autopromoción del fondo. [V]
   - Lección: la paleta y el estilo identifican; el personaje, por sí solo, no vende el clic.
7. **TED-Ed.**
   - Top: "aislamiento" (8.5M) y "atención" (4.7M). Miniaturas con una persona grande y una emoción clara (ceño fruncido, cansancio). [V]
   - Lección: una emoción legible en primer plano y un problema cotidiano.
8. **Escéptico.**
   - Cada miniatura usa un estilo distinto: caricatura, óleo, "Tim Burton". Los fotogramas son "pinturas antiguas" generadas, con subtítulos. [V]
   - Es el contraejemplo de todo este informe.
9. **After Skool.**
   - La mano real dibujando es la prueba visible de autoría humana. Hoy esa prueba vale más que hace tres años. [I]
10. **Headspace.**
    - En sus meditaciones, los 3 fotogramas del video son casi idénticos y aun así superan el millón de vistas. [V]
    - Lección: con un personaje mínimo, un loop sutil basta si la promesa es calma.
11. **Duolingo.**
    - Las miniaturas con Duo multiplican unas 3,000 veces las vistas de las miniaturas con personas reales (32M frente a 5K–10K). [V]
    - Rediseño de 2018–2019:
      - formas geométricas simples y planas, más fáciles de animar "sin importar quién lo dibuje" (Greg Hartman);
      - Duo pasó de logo a personaje;
      - la empresa reporta un aumento de alrededor del 5% en sesiones. [V, cifra de la propia empresa]
12. **TheOdd1sOut, Jaiden y Domics.**
    - Humanos estilizados de 2–3 cabezas, de cara blanca o sin color. [V]
    - Cada personaje se distingue por **un accesorio o peinado**: la gorra, el pelo de Jaiden.
    - Son los canales con mejor proporción vistas/suscriptores del benchmark (85–129%). [V]
    - Lección: con humor relatable en primera persona, un humano simple es suficiente.
13. **Strange Planet.**
    - Ser azul con cabeza de gota, ojos grandes y lenguaje literal. [V]
    - Lección: describir la conducta humana "desde fuera" es psicología pura. El azul y la gota ya están tomados.
14. **Sarah's Scribbles.**
    - Ojos-círculo con ojeras y pelo enmarañado: dos rasgos bastan. [V]
    - Lección: el blanco y negro funciona en viñeta. En miniatura de video necesita un acento de color.
15. **Lennnie.**
    - En YouTube rinde poco (mediana de 6K). En TikTok/IG pasa de 4M de seguidores y tiene campaña con Dove. [V]
    - Lección: el formato de "mensaje directo a cámara con voz suave" es de video corto vertical.
16. **Pictoline · La vida secreta de tu mente.**
    - Serie mexicana de psicología cotidiana con un cerebro de protagonista, en Cartoon Network y HBO Max (2023). [V]
    - Lección: en México, el cerebro-mascota de psicología ya tiene dueño.
17. **Psicología Animada.**
    - Personajes de plantilla (tipo Vyond). [V]
    - En la búsqueda apareció también un tutorial titulado "€2,900/MONTH AI ANIMATED PSYCHOLOGY CHANNEL: Faceless & Automated". [V]
    - Lección: el nicho "psicología animada sin cara" se está llenando de canales automatizados. Diferenciarse con autoría visible es estratégico. [I]
18. **OverSimplified, Life Noggin y Molang.**
    - OverSimplified demuestra que el cutout barato con humor rinde muchísimo: 40M de mediana. [V]
    - Life Noggin, con su cabeza cuadrada, muestra que la forma geométrica identifica.
    - Molang muestra que con una forma mínima basta.

---

## 4. Estilo frente a rendimiento

### 4.1 Mismo canal: miniaturas top frente a bottom [V]

Panel: `01_panel_miniaturas_top_vs_low.jpg`.

| Canal | Top (vistas) | Bottom (vistas) | Qué cambia visualmente |
|---|---|---|---|
| Duolingo | 32M · 18M · 16M | 9.9K · 7.7K · 5.2K · 5.2K | Top: Duo en primer plano (3/3). Bottom: personas reales recortadas (4/4). |
| Headspace | 1.7M · 1.3M · 1.2M | 1.9K · 1.8K · 1.7K · 1.2K | Top: formas con cara, una sola emoción y fondo de un color. Bottom: fotos de personas, iconos sin cara o carita secundaria. |
| Psych2Go | 1.4M · 654K · 619K | 23K · 22K · 20K · 15K | Top: mascota protagonista (2/3) o primer plano de ojos. Bottom: humanos anime en escenas oscuras o mascota diminuta. |
| School of Life | 2.0M · 1.8M · 1.6M | 45K · 44K · 42K · 34K | Top: ilustración plana pastel con figura pequeña (3/3). Bottom: collage de fotos (2/4). |
| Sprouts | 19M · 11M · 7.8M | 13K · 11K · 10K · 8.5K | Top: personas dibujadas, cálidas y sepia. Bottom: blobs rojos abstractos y una foto real. |
| LPI | 3.6M · 2.8M · 1.7M | 10K · 9.5K · 5.7K · 5.4K | Plantilla idéntica. Cambia el tema: identidad cotidiana frente a autoayuda o liderazgo. |
| Kurzgesagt | 89M · 35M · 33M | 1.3M · 1.1M · 715K · 340K | Top: espectáculo temático, sin pájaro. Bottom: autopromoción con el pájaro. |
| Escéptico | 161K · 31K · 20K | 374 · 368 · 341 · 330 | Estilo distinto en cada miniatura. Sin personaje. |
| TheOdd1sOut, Jaiden, Domics, Casi Creativo | — | — | El personaje aparece siempre. Los bottom son anuncios, Q&A o piano: formato, no estilo. |

### 4.2 Qué se puede concluir [I]

1. **Una cara con una emoción legible y grande vende más que una escena.** Se repite en Headspace, TED-Ed, Psych2Go y Duolingo.
2. **Lo ilustrado gana a la foto real** dentro de marcas ilustradas: School of Life, Duolingo, Headspace y Sprouts.
3. **El personaje no sustituye al tema.** Con el personaje fijo, la varianza la explica el concepto (LPI, Kurzgesagt). El personaje sirve para:
   - reconocer el canal en el feed;
   - acumular afecto entre un video y otro;
   - abaratar la producción gracias al rig.
4. **Los canales sin identidad visual estable están en la parte baja de la proporción vistas/suscriptores:** Psych2Go tiene la peor del grupo (0.5%) y Escéptico está en 1.8%. Los canales de personaje fijo con humor relatable tienen las mejores: TheOdd1sOut 129%, Jaiden 118%, Domics 85% y Casi Creativo 66%. Ojo: las marcas o instituciones con estilo consistente pero sin personaje protagonista también están bajas (TED-Ed 1.8%, School of Life 2%, Headspace 0.9%). Hay factores de confusión: la edad del canal, el formato, el humor y el hecho de que muchos suscriptores llegaron hace años.
5. **Plantilla de miniatura ganadora para nosotros:**
   - personaje grande con una sola emoción;
   - un objeto concreto que cuente la situación;
   - 2–4 palabras;
   - fondo de un color;
   - avatar fijo en una esquina, como Jaiden.

---

## 5. Qué hace "icónico" a un personaje (fuentes de diseño)

| Principio | Evidencia | Prueba práctica para nosotros |
|---|---|---|
| **Silueta legible** | Rellenar el personaje de negro y comprobar si se reconoce. Disney Family Museum documenta la prueba de silueta como método clásico. Si la legibilidad depende del color o de la textura, la estructura de formas no es lo bastante fuerte (guías de shape language). | Silueta negra a 160 px y a 48 px. Ver `02_direcciones_bocetos.png`. |
| **Forma dominante = personalidad** | Círculos y cuadrados se leen como confiables y accesibles; los ángulos, como tensión (shape language). | Para salud mental: círculo y squircle; ángulos solo como acento. |
| **Uno o dos rasgos memorables, no diez** | Las guías de mascota coinciden: 1–2 detalles memorables superan a un diseño recargado. Duolingo: "pocos detalles, pero los suficientes". | Elegir **un** rasgo firma y quitar el resto. |
| **Color propio y exclusivo** | Romaniuk (Ehrenberg-Bass): un activo distintivo se mide por fama (cuánta gente lo asocia a la marca) y **unicidad** (que no remita a un competidor); la unicidad suele ser la más importante. | El color de la piel o de la prenda no debe coincidir con LPI (salvia), Strange Planet (azul), TheOdd1sOut (blanco) ni Lennnie (malva). |
| **Formas simples = escalable y animable** | Duolingo pasó a formas geométricas planas para producir y animar más rápido "sin importar quién lo dibuje". | Que lo pueda dibujar cualquiera del equipo (o el código) sin que cambie. |
| **Rango emocional amplio** | Headspace amplió en 2024 sus caras a "estrés, tristeza, satisfacción y todo lo intermedio". | Hoja de 12 expresiones antes del primer video. |
| **Consistencia sostenida** | System1/IPA: las campañas con "fluent devices" (personajes recurrentes) tienen un 37% más de probabilidad de ganar cuota de mercado y ~30% más de ganar beneficio. Las marcas más consistentes puntúan 1 estrella más. El efecto suele tardar en aparecer y muchas marcas abandonan el personaje a los 12–18 meses. | Compromiso mínimo de 12 meses sin rediseñar. Guía de estilo estricta (contraejemplo: Psych2Go). |
| **Personalidad y voz** | Duo es "pasivo-agresivo"; Lennnie, voz suave; Strange Planet, lenguaje literal. El icono es también cómo habla. | Definir 3 adjetivos + una muletilla visual o verbal propia. |

Nota: los datos de System1 son investigación de la propia empresa, basada en IPA DataMINE (~2018 y 2024). Son útiles como señal, no como prueba independiente.

---

## 6. Señales que hoy se perciben como "IA genérica" (2025–2026)

### 6.1 Contexto verificado [V]

- **"Slop" fue la palabra del año 2025 de Merriam-Webster.** La definen como contenido digital de baja calidad producido en cantidad con IA. El tono que describe es más de burla que de miedo.
- **McDonald's Países Bajos** retiró su anuncio navideño hecho con IA unos 3 días después de publicarlo (6–9 dic 2025). Primero cerró los comentarios y luego lo hizo privado. La gente lo llamó "creepy" y "AI slop".
- **Coca-Cola** recibió críticas de "soulless" por segundo año (2024 y 2025). En 2025 cambió los humanos por animales porque "era difícil sacar expresiones". Los críticos lo leyeron como una forma de esquivar el valle inquietante, y aun así vieron animales "planos" y "mal animados".
- **NielsenIQ (2025, más de 2,000 participantes):** los anuncios hechos con IA resultan más molestos, aburridos y confusos, y generan un "halo negativo" que se traslada a la marca.
- **YouTube:** desde el 15-jul-2025 no monetiza el "contenido no auténtico", es decir, masivo, repetitivo o de plantilla.
- **Etiquetas "hecho por humanos":** en 2026 aparecen sellos como The Human Made Mark (lanzado el 23-abr-2026). Por ahora cubre acción real y stop-motion. Las marcas se reposicionan con "artesanía humana".
- **Tinte amarillo de ChatGPT ("piss filter"):** desde marzo de 2025 se reconoce un sesgo cálido o sepia en las imágenes de GPT-4o: blancos que tiran a crema, sombras marrón barro. Hay herramientas solo para quitarlo.
- **Caso cercano:** en LPI, el comentario con más likes del video "casa limpia" (1,300) critica el guion "de ChatGPT", y otros señalan errores visuales (ronda 1).

### 6.2 Checklist de señales visuales "IA" para evitar [V/I]

| Señal | Ejemplo observado en el benchmark | Antídoto en nuestro pipeline |
|---|---|---|
| Tinte amarillo o sepia global, blancos cremosos | Fondos crema "de libro" muy uniformes (LPI), pinturas sepia (Escéptico) | Blanco real o crema elegido a propósito; paleta cerrada en tokens. |
| Acabado liso o "plástico", luz de estudio perfecta, bloom suave | 3D "Pixar" genérico (ya marcado como riesgo en `REFERENCIAS_PERSONA.md`) | Plano vectorial con grano controlado y línea de color. |
| Personaje que cambia de proporciones, ropa o cara entre escenas | LPI (cuerpos de grosor distinto), Psych2Go (3 estilos) | Rig SVG único: es imposible que el personaje "mute". |
| Mezcla de niveles de realismo en un mismo plano | En LPI, niño realista con manos detalladas junto a la figura minimal | Un solo nivel de abstracción para todo el elenco. |
| Fondos sobredetallados, con objetos que no tienen función | Interiores llenos de cachivaches (LPI, fondo de Lennnie) | Fondos de 3–5 formas; solo objetos que cuentan algo. |
| Texto o símbolos ilegibles; manos con dedos de más | Guías de detección (Creative Bloq y otras) | Todo el texto se compone en código; manos de manopla o de 4 dedos estilizadas. |
| Estética "óleo antiguo", "Ghibli" o "storybook" de moda | Escéptico; ola Ghibli de 2025 | Estilo propio con reglas escritas. |
| Imágenes fijas + zoom + voz sintética + subtítulos centrados | Escéptico; tutoriales de "canal automatizado" | Animación real, aunque sea limitada (parpadeo, respiración, lipsync), y **voz humana** ("Por fin un narrador humano", 223 likes, ronda 1). |
| Paleta "Corporate Memphis" (morado, coral y cuerpos deformes sin rostro) | Crítica extendida a ese estilo por "insípido" e "insincero" | Rostro con ojos y cejas; proporciones coherentes; paleta mexicana propia. |

**Señales positivas de autoría humana**, para usarlas a propósito:
- "line boil": un trazo que tiembla 2–3 px en un ciclo de 3 fotogramas;
- imperfecciones consistentes;
- timing con pausas de comedia;
- una mano o un boceto visible en el *making-of*;
- la firma del ilustrador o ilustradora;
- publicar la hoja de modelo del personaje.

---

## 7. Mapa de territorio ocupado [V/I]

| Rasgo | Lo usa | Riesgo si lo usamos |
|---|---|---|
| Figura humanoide alargada sin rasgos, color salvia, fondo crema | La Psicología Invisible | Se percibiría como copia directa del referente que más le gusta al fundador. |
| Cabeza blanca redonda enorme, sin color de piel | TheOdd1sOut, Casi Creativo | Derivado. |
| Ser azul con cabeza de gota | Strange Planet | Derivado. |
| Cerebro con cara | Pictoline/Cartoon Network (MX) | Choque directo en el mismo país. |
| Brote u hoja en la cabeza | Psych2Go | Choque con el concepto "C · Brote" ya explorado. |
| Blob rosa con ojos grandes | Lennnie | Derivado; además no es "persona". |
| Cara-sonrisa abstracta naranja | Headspace | Asociación a meditación o app. |
| Ojos-círculo con ojeras + pelo enmarañado | Sarah's Scribbles | Aceptable como inspiración de ojos; no copiar el pelo. |

**Libre (oportunidad):**
- un color de piel no realista **cálido, terroso y mexicano**, como terracota o barro;
- un rasgo firma que **sea a la vez indicador emocional**: nadie del benchmark lo tiene en un personaje humano;
- squircle o "cojín" como forma de cabeza en un humano: solo Life Noggin usa un cuadrado, y en píxel.

---

## 8. Seis direcciones de personaje humano estilizado

Bocetos esquemáticos con prueba de silueta y avatar de 48 px: `referencias_visuales/02_direcciones_bocetos.png`. No son diseños finales: sirven para comparar silueta, proporción y paleta.

**Resultado de la prueba de silueta de los bocetos** [V, sobre nuestros propios bocetos]
- Pasan sin color: **1 (mechón)**, **5 (capucha-halo)** y **6 (cabeza-ventana)**.
- Quedan genéricas sin color: **2, 3 y 4**. Necesitan un rasgo de silueta añadido.

**Pipeline común de animación** (para todas)
- Rig SVG generado por código, como en `personaje/helpers.js`: cabeza, cejas, ojos, párpados, boca, torso, 2 brazos en 2 segmentos y piernas.
- Animaciones base: parpadeo aleatorio, respiración (scaleY de 1.00 a 1.02 en 3–4 s), inclinación de cabeza y morph de cejas.
- Lipsync con 6 bocas (A/E/I-O/U/M-B-P/reposo), sincronizado con Rhubarb Lip Sync, que es open source.
- Render con Playwright o Remotion. [I]

### Dirección 1 · "Mechón": humano geométrico con barómetro emocional ★ recomendada como base

- **Descripción**
  - Persona sin edad marcada (veintitantos a treinta y tantos) y de género ambiguo.
  - Cabeza circular, cuerpo trapezoidal suave sin cuello, extremidades de cápsula.
  - Un **mechón en onda** que sale de la coronilla.
- **Proporciones**
  - 3 cabezas de alto. Cabeza = 1/3 del total.
  - Ojos en el 55% inferior de la cabeza, para que se lea como "cara de persona" y no de bebé.
  - Ancho del torso = 0.7 del diámetro de la cabeza.
- **Paleta** (con los hex del boceto)
  - Piel coral no realista `#F4A38C`.
  - Pelo índigo `#2B2D5C`.
  - Prenda firma teal `#2F8F83`.
  - Acento mostaza `#F2B544`.
  - Fondo crema `#FBF4EA`.
  - Alternativa de piel: terracota `#D27D56` (cruce con la dirección 2).
- **Rasgo firma:** el mechón. Además de identificar la silueta, **expresa el estado interno**:

  | Estado | Cómo se ve el mechón |
  |---|---|
  | Calma | Onda suave |
  | Ansiedad | Zigzag erizado y vibrando |
  | Tristeza | Cae lacio |
  | Idea | Se enrosca hacia arriba |
  | Enojo | Se tensa recto |

  Es "lo invisible hecho visible" y funciona como glifo del logo o del avatar.
- **Emoción:** ojos punto + cejas en línea (el 80% de la expresión) + boca mínima + mechón.
- **Animación viable a bajo coste**
  - Mechón como path SVG con 3 puntos de control interpolados.
  - Física de resorte simple por código: un poco de retraso y rebote en los giros de cabeza.
  - Coste: **bajo**. Unas 12 piezas.
- **Referencias**
  - Jaiden: la silueta del pelo como firma.
  - Headspace: rango emocional con pocas líneas.
  - Duolingo: formas simples escalables.
  - TheOdd1sOut: cuerpo mínimo.
- **Riesgos**
  - Si el mechón es verde o tiene forma de hoja, se confunde con Psych2Go. Debe ser del color del pelo y con forma de onda o espiral, nunca de hoja.
  - Que se vea infantil. Mitigación: prendas adultas (suéter, saco), ojos no tan grandes y proporción de 3 cabezas, no 2.

### Dirección 2 · "Barro": persona terracota editorial, de identidad mexicana

- **Descripción**
  - Persona estilizada con piel color barro no realista (no pretende ser un tono de piel humano).
  - Suéter oversized de cuello alto que forma una silueta de bloque.
  - El elenco secundario usa otros tonos de barro, jade y añil: una "familia de barro".
- **Proporciones**
  - 4 cabezas. Cabeza ovalada vertical.
  - Hombros anchos, piernas cortas.
  - Más adulta y editorial: School of Life con más cara.
- **Paleta**
  - Barro `#D27D56`.
  - Añil `#2E3A6B`.
  - Cempasúchil `#E9A23B`.
  - Jade `#3E8E7E`.
  - Rosa mexicano suavizado `#E76F8A` (rubor y acentos).
  - Fondo papel `#F4E9DA`.
- **Rasgo firma:** el **color barro** + el suéter de cuello alto. Ojos de media luna (párpados caídos) que dan una calma de "persona que escucha".
- **Emoción:**
  - párpados que abren y cierran;
  - cejas;
  - rubor;
  - postura: hombros que suben con ansiedad y caen con tristeza.
- **Animación:** cutout SVG de unas 10 piezas. El suéter oculta las articulaciones, lo que abarata el rig. Coste: **bajo**.
- **Referencias**
  - School of Life: editorial cálido.
  - TED-Ed: textura y calidez.
  - Pictoline y Casi Creativo: conexión con la audiencia mexicana.
  - Romaniuk: el color como activo único.
- **Riesgos**
  - La silueta sin color es genérica (prueba fallida). Hay que añadir un rasgo de silueta, por ejemplo el mechón de la dirección 1 o un rebozo o bufanda característica.
  - El terracota podría leerse como un tono de piel real y prestarse a interpretaciones étnicas. Hay que validarlo con audiencia mexicana. Se puede usar en la prenda en vez de en la piel.

### Dirección 3 · "Línea viva": trazo de tinta + un solo acento emocional

- **Descripción**
  - Persona dibujada solo con línea de grosor variable en tinta azul-noche sobre papel crema.
  - El único color es una **mancha coral** que aparece en el pecho o alrededor de la cabeza cuando el personaje siente algo. Puede cambiar de forma según la emoción: corazón, nube, espina.
- **Proporciones:** 3 cabezas. Ojos-círculo grandes con ojeras ligeras (estilo webcomic relatable). Pelo con volumen.
- **Paleta**
  - Tinta `#1F2A44`.
  - Coral `#FF6F59` (emoción).
  - Papel `#F6F1E7`.
  - Secundarios: aqua `#7FB7BE` y mostaza `#F2C14E`, solo en objetos.
- **Rasgo firma:** la mancha de emoción de color.
- **Emoción:** ojos (tamaño de pupila y ojeras), cejas, y la forma y el tamaño de la mancha.
- **Animación**
  - Trazos que se dibujan con `stroke-dashoffset` (draw-on, como After Skool, pero por código).
  - "Line boil": jitter de 2–3 px en un ciclo de 3 fotogramas, la señal anti-IA más barata.
  - Coste: **muy bajo**.
- **Referencias**
  - Sarah's Scribbles y Domics: el blanco y negro relatable rinde (Domics, 6.1M de mediana).
  - School of Life: acento de color.
  - Notion Faces (Buck): línea elegante.
  - After Skool: draw-on.
- **Riesgos**
  - Poca fuerza en miniatura y en el feed. Necesita fondos de color plano en las miniaturas.
  - La silueta sin color es débil.
  - Puede parecer "boceto" si no hay rigor en el grosor de línea.

### Dirección 4 · "Papel recortado": cutout artesanal

- **Descripción**
  - El personaje y el mundo están hechos de formas de papel con fibra visible y bordes irregulares.
  - El personaje se mueve como un recorte real, con una ligera sombra proyectada.
  - Evoca la animación de recortes clásica y el collage mexicano de papel picado.
- **Proporciones:** 3.5 cabezas. Cabeza círculo, cuerpo trapecio, pelo recortado en zigzag o picos.
- **Paleta**
  - Piel papel `#F0C9A5`.
  - Mostaza `#E3A72F`.
  - Negro papel `#1E1E24`.
  - Rojo óxido `#C8553D`.
  - Fondo kraft claro `#EDE4D3`.
- **Rasgo firma:** el borde de papel picado del pelo + la sombra proyectada de recorte.
- **Emoción:** ojos punto, una boca triangular que cambia de forma, y gestos de cuerpo amplios (el cutout lo permite).
- **Animación**
  - Cutout natural, porque el estilo **es** cutout.
  - Textura con `feTurbulence` en SVG o con una imagen de papel escaneada una sola vez.
  - Cambios de cara por sustitución de piezas, como en stop-motion de recortes.
  - Coste: **bajo a medio**.
- **Referencias**
  - TED-Ed: texturas.
  - Tendencia anti-IA hacia lo artesanal (ronda 1).
  - The Human Made Mark: valora el stop-motion.
  - OverSimplified: el cutout barato funciona.
- **Riesgos**
  - Si la textura es tímida, cae en "Corporate Memphis" plano.
  - Silueta genérica: necesita el pelo de papel picado muy marcado.
  - Una textura excesiva ensucia en móvil.

### Dirección 5 · "Cabezón de sketch": humor relatable

- **Descripción**
  - Cabeza squircle enorme con ojos de esclera grande.
  - Siempre lleva una **sudadera con capucha violeta**: la capucha forma un halo detrás de la cabeza y da una silueta única.
  - Es la dirección para sketches cómicos y Shorts.
- **Proporciones:** 2.2 cabezas. Cabeza = 45% del alto. Contorno grueso `#2B2B33`.
- **Paleta**
  - Piel `#F9D3B9`. En el elenco, cada personaje lleva un color de piel distinto, incluidos tonos no realistas.
  - Violeta eléctrico `#5B4BDB` (prenda firma).
  - Tinta `#2B2B33`.
  - Amarillo `#FFC93C` (cordones y acentos).
  - Fondo `#FFF7EE`.
- **Rasgo firma:** la capucha-halo violeta + la cabeza squircle.
- **Emoción:** ojos (pupila y esclera), cejas gruesas y boca grande con interior, como TheOdd1sOut y Casi Creativo. Rango cómico máximo.
- **Animación:** rig de unas 14 piezas + 6 bocas. Poses sostenidas con smear de un fotograma en los cambios. Coste: **bajo a medio**.
- **Referencias:** Casi Creativo (5.8M de mediana), TheOdd1sOut (27M), OverSimplified (40M) y Life Noggin (cabeza cuadrada).
- **Riesgos**
  - Es la más cercana a Casi Creativo, el referente local con 8.8M de suscriptores: puede leerse como derivado.
  - Es menos "calma profesional" para una marca de salud mental.
  - El contorno negro grueso es lo más común del género.

### Dirección 6 · "Cabeza-ventana": el clima interno visible

- **Descripción**
  - La cabeza es un círculo-ventana con un cielo dentro. La cara mínima ocupa la parte inferior.
  - El clima interior cambia con la emoción: sol, nube, lluvia, tormenta, noche estrellada.
  - Es una metáfora psicológica directa y propia ("lo que sientes por dentro").
- **Proporciones:** 3 cabezas. Cabeza grande con contorno grueso de "marco". Cuerpo de túnica simple.
- **Paleta**
  - Noche `#1E2140` (marco y ropa).
  - Cielo `#8EC5E8`.
  - Sol `#FFD66B`.
  - Tormenta `#6B6F8F`.
  - Piel de manos y cara `#E7B89A`.
  - Fondo `#F7F2EA`.
- **Rasgo firma:** la cabeza-ventana con clima. Es único en el benchmark y funciona solo como avatar o logo.
- **Emoción:** el clima (cambio de color de fondo con degradado SVG animado, nubes y lluvia con partículas por código) + ojos y boca mínimos.
- **Animación:** `clipPath` + degradados interpolados + partículas simples. Coste: **bajo**, con un efecto vistoso.
- **Referencias**
  - Headspace: emociones con formas y color.
  - Kurzgesagt: el color como emoción.
  - La metáfora del "clima interno", muy usada en psicoeducación.
- **Riesgos**
  - Se lee menos como "persona" que las otras (la cabeza deja de ser cabeza).
  - Comparte territorio con "Intensamente" o Inside Out y con Pictoline (la mente por dentro).
  - Es complejo de leer en miniaturas pequeñas si el clima tiene detalles.
  - Puede reservarse como **recurso de una sección o de los momentos introspectivos** del personaje principal.

### 8.1 Matriz de decisión [I]

Puntuación de 1 a 5; más es mejor.

| Criterio | 1 Mechón | 2 Barro | 3 Línea viva | 4 Papel | 5 Cabezón | 6 Ventana |
|---|---|---|---|---|---|---|
| Se entiende que es una persona | 5 | 5 | 5 | 5 | 5 | 3 |
| Silueta y avatar de 48 px | 5 | 2 | 2 | 3 | 4 | 5 |
| Diferenciación frente al benchmark | 4 | 5 | 3 | 4 | 2 | 4 |
| Limpio, profesional y bonito | 4 | 5 | 4 | 4 | 3 | 4 |
| Expresa emoción (psicología) | 5 | 3 | 4 | 3 | 5 | 5 |
| Coste de animación por código (5 = más barato) | 5 | 5 | 5 | 4 | 4 | 4 |
| Lejos de "IA genérica" | 4 | 4 | 5 | 5 | 4 | 4 |
| **Total** | **32** | 29 | 28 | 28 | 27 | 29 |

### 8.2 Propuesta concreta [I]

**"Mechón" (1) con paleta "Barro" (2) y acabado "Línea viva" (3):**
- **Personaje:** 3 cabezas, cabeza circular, mechón-barómetro de color índigo.
- **Color:** piel o prenda terracota `#D27D56` + suéter añil `#2E3A6B`. Acentos cempasúchil `#E9A23B` y jade `#3E8E7E` sobre papel `#F4E9DA`.
- **Línea:** de color índigo oscuro (no negra), con un line boil sutil y grano de papel al 6–8%.
- **Elenco secundario:** humanos de la misma construcción con otros tonos de barro, y objetos con cara puntuales al estilo de Casi Creativo para los temas "tu cerebro cuando…". **Nunca un cerebro protagonista.**
- **Uso de la dirección 6:** la cabeza-ventana como recurso puntual ("por dentro se siente así").
- **Rol:** guía de ficción, no experto. La política de YouTube lo exige (ronda 1). El experto real, con cédula, aparece con su nombre en descripciones o cameos.

### 8.3 Siguientes pasos de validación

1. Pasar las 6 siluetas y los avatares de 48 px por una encuesta rápida con 30–50 personas de la audiencia objetivo (mujeres de 18 a 34 en México). Preguntas:
   - "¿Qué es esto?";
   - "¿qué edad o género tiene?";
   - "¿a qué canal te recuerda?". Esta última detecta parecidos con LPI, Casi Creativo o Psych2Go.
2. Hoja de modelo de la versión elegida: 12 expresiones (incluido cada estado del mechón), 6 bocas, 8 poses y un turnaround de 3/4.
3. Hacer 3 miniaturas con la plantilla de la sección 4.2 y probarlas con *Test & Compare* de YouTube.
4. Guía de estilo con tokens de color, grosor de línea, proporciones y prohibiciones (checklist de la sección 6.2), antes del primer video.
5. Compromiso de no rediseñar durante 12 meses (evidencia de System1 sobre consistencia).

---

## 9. Fuentes

**Datos propios**
- yt-dlp sobre los canales de YouTube citados (18-nov-2026): listas en `referencias_visuales/datos/`, miniaturas `i.ytimg.com/vi/<id>/mqdefault.jpg` y fotogramas `sd1–3.jpg`.

**Diseño de personajes y activos de marca**
- [Duolingo: Shape language, Duolingo's art style](https://blog.duolingo.com/shape-language-duolingos-art-style/)
- [Duolingo: Reshaping Duo](https://blog.duolingo.com/reshaping-duo/)
- [Design Week: el búho de Duolingo cambia de imagen (2019)](https://www.designweek.co.uk/issues/2-6-january-2019/duolingo-owl-receives-makeover-as-app-becomes-more-gamified)
- [Creative Bloq: el rediseño de la mascota de Duolingo](https://creativebloq.com/news/duolingos-redesigned-mascot-is-a-hoot)
- [It's Nice That: Italic Studio y Headspace (2024)](https://itsnicethat.com/articles/italic-studio-headspace-graphic-design-project-250424)
- [Walt Disney Family Museum: prueba de silueta (PDF)](https://www.waltdisney.org/sites/default/files/2020-05/T%26T_Silhouette-final2.pdf)
- [RocketBrush: shape language y legibilidad](https://rocketbrush.com/blog/shape-language-in-game-character-design-how-to-make-characters-readable-and-consistent)
- [Made Good Designs: diseño de mascotas](https://madegooddesigns.com/mascot-logo-design/)
- [Marketing Science: Brands of distinction (Romaniuk)](https://marketingscience.info/brands-of-distinction)
- [Umbrex: marco de activos distintivos de Ehrenberg-Bass](https://umbrex.com/resources/frameworks/marketing-frameworks/distinctive-brand-assets-framework-ehrenberg-bass/)
- [LBB: System1, los personajes memorables suben un 30% la probabilidad de beneficio](https://lbbonline.com/news/research-by-system1-shows-memorable-characters-in-ads-boost-chances-of-profit-by-30)
- [System1: Creating memorable characters in advertising](https://system1group.com/blog/creating-memorable-characters-in-advertising)
- [ANA: System1 y la consistencia creativa](https://ana.net/magazines/show/id/forward-2025-01-system1-compound-creativity)
- [Wikipedia: Nathan W. Pyle](https://en.wikipedia.org/wiki/Nathan_W._Pyle)
- [NPR: entrevista a Nathan Pyle (2019)](https://www.npr.org/2019/12/15/787618154/imagine-pleasant-nonsense-with-strange-planet-creator-nathan-pyle)
- [Campaign ME: Dove y Lennnie](https://campaignme.com/dove-partners-with-animated-influencer-to-promote-mental-health/)
- [Favikon: perfil de Lennnie](https://app.favikon.com/public/profile/lennnie-6826e310aa8c3c2c3af32c2a/)

**IA genérica, rechazo y políticas**
- [Engadget: "slop", palabra del año de Merriam-Webster](https://www.engadget.com/ai/slop-is-merriam-websters-word-of-the-year-181903322.html)
- [Deseret: palabras del año 2025](https://www.deseret.com/entertainment/2025/12/15/2025-words-of-the-year)
- [NBC News: McDonald's retira su anuncio navideño hecho con IA](https://www.nbcnews.com/world/europe/mcdonalds-ai-generated-christmas-advert-social-media-backlash-rcna248590)
- [Fox Business: McDonald's retira el anuncio "creepy"](https://www.foxbusiness.com/media/mcdonalds-pulls-creepy-ai-generated-christmas-ad-after-viewer-backlash)
- [The New Daily: el anuncio de IA de McDonald's](https://www.thenewdaily.com.au/life/social-media-life/2025/12/13/mcdonalds-ai-advert)
- [TechRadar: Coca-Cola y otro anuncio "AI slop"](https://www.techradar.com/ai-platforms-assistants/coca-cola-faces-backlash-again-for-missing-the-spirit-of-the-holidays-with-another-ai-slop-ad)
- [VnExpress: Coca-Cola, anuncio navideño "soulless"](https://e.vnexpress.net/news/tech/enterprises/coca-cola-slammed-again-for-soulless-ai-generated-christmas-ad-4960752.html)
- [ESM Magazine: los anuncios hechos con IA y la percepción del consumidor (NIQ)](https://esmmagazine.com/a-brands/ai-generated-ads-may-have-a-negative-effect-on-consumer-perceptions-279327)
- [Plagiarism Today: YouTube y el contenido "inauthentic"](https://www.plagiarismtoday.com/2025/07/08/youtube-targets-inauthentic-content/)
- [Digiday: la ofensiva de YouTube contra el AI slop](https://digiday.com/media/youtubes-ai-slop-crackdown-has-creators-concerned-marketers-cheering)
- [TechRadar: el tinte amarillo en las imágenes de ChatGPT](https://www.techradar.com/ai-platforms-assistants/chatgpt/tired-of-that-yellow-tint-in-chatgpt-images-heres-how-to-fix-it-with-simple-color-correction)
- [Know Your Meme: AI Art Becoming Yellow](https://knowyourmeme.com/memes/ai-art-becoming-yellow)
- [Popular AI: el "piss filter" de ChatGPT](https://www.popularai.org/p/chatgpts-piss-filter-why-ai-images)
- [Creative Bloq: cómo detectar imágenes de IA](https://creativebloq.com/ai/ai-art/how-to-spot-ai-images)
- [Euronews: cómo saber si una imagen está hecha con IA (2025)](https://www.euronews.com/2025/02/16/ai-slop-is-flooding-the-internet-this-is-how-can-you-tell-if-an-image-is-artificially-gene)
- [Señal News: lanzamiento de The Human Made Mark (2026)](https://senalnews.com/en/content/the-human-made-mark-launches-global-certification-to-champion-human-creativity-in-film-and-tv)
- [Skwigly: The Human Made Mark](https://www.skwigly.co.uk/the-human-made-mark-launch/)
- [Wikipedia: Corporate Memphis](https://en.wikipedia.org/wiki/Corporate_Memphis)
- [AIGA Eye on Design: el rechazo a las mascotas corporativas de colores](https://eyeondesign.aiga.org/the-internet-is-turning-on-big-techs-colorful-corporate-mascots/)

**Referentes**
- YouTube: Pictoline, "La vida secreta de tu mente" (Cartoon Network LA, `ajsqqOHCgqY`; tráiler de HBO Max, `mVVhxf3v2p8`)
- YouTube: tráiler de Strange Planet en Apple TV (`DmTLO-21XSk`)
- Tutorial "AI animated psychology channel" (`cQMcOI9y3oA`)
