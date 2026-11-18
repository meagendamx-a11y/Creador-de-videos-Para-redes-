# 04 · Qué busca la gente en México sobre psicología (Google y YouTube)

**Proyecto:** canal de divulgación psicológica con personaje animado — Agenda PSI (agendapsi.mx)
**Fecha de corte de datos:** 18 de noviembre de 2026 · **Geografía:** México (geo = MX)
**Fuentes:** Google Trends vía `pytrends` (búsqueda web y búsqueda en YouTube) + autocompletado público de Google y de YouTube (`suggestqueries`, hl=es, gl=mx).
**Datos crudos:** `/tmp/claude-0/-home-user-Creador-de-videos-Para-redes-/f6e80049-54f1-5e5b-b0dd-1d5ea884d7d2/scratchpad/research/trends/` (ver §11). Ojo: es una carpeta temporal; conviene copiarla a un lugar permanente si se quiere conservar.

---

## 0. Resumen ejecutivo

1. **La ansiedad es el tema con más demanda, y por mucho.** En Google, "ansiedad" se busca unas **6.6 veces más** que "psicólogo" y unas **3.4 veces más** que "depresión" (escrita con acento). Pasa lo mismo en el autocompletado: "cómo dejar de pensar demasiado", "cómo dejar de sobrepensar", "por qué me siento nervioso sin razón", "por qué siento que me falta el aire", "cómo controlar un ataque de ansiedad".
2. **La neurodivergencia en adultos es lo que más crece.** En cinco años, en YouTube: "autismo adultos" **+1,100 %**, "TDAH adultos" **+338 %**, "TDAH" **+226 %**. En Google, "autismo adultos" se duplicó (+100 %). Entre las consultas "en aumento" aparecen *cómo detectar autismo en adultos* (Google, con un salto de +85,500 %), *rasgos de autismo en adultos* (YouTube, +138,250 %), *TDAH en mujeres adultas*, *autismo en mujeres adultas*, *cómo saber si tengo TDAH* y *quién diagnostica TDAH en adultos*. Estas preguntas llevan casi directo a una evaluación profesional.
3. **Las relaciones de pareja son la mina de preguntas exactas.** Raíces como "mi pareja me…", "cómo superar…" o "señales de que…" devuelven cientos de frases en primera persona: *mi pareja me aplica la ley del hielo*, *me culpa de todo*, *me hace sentir insuficiente*, *cómo superar una infidelidad y seguir con tu pareja*, *cómo dejar de idealizar a una persona*, *mi pareja tiene apego evitativo*. En YouTube, "apego ansioso" y "apego evitativo" ya superan a "el apego" como consultas principales, y *qué tipo de apego tengo* sube +4,900 % y en Google *apego ansioso cómo superarlo* es Breakout (+31,050 %). Ese vocabulario ("apego ansioso", "sobrepensar", "relación tóxica") pesa entre 3 y 28 veces más en YouTube que en Google.
4. **El formato "La psicología de las personas que…" es una tendencia de YouTube y Shorts en México.** El autocompletado devuelve más de 120 variantes: *…imaginan escenarios falsos*, *…mantienen su casa limpia*, *…prefieren estar solas*, *…no publican fotos en redes*, *…cortan el contacto con su familia*, *…se quedan calladas cuando están heridas*, *…te castigan con silencio*. Va hecho a la medida de un personaje animado.
5. **La búsqueda explícita de terapia es pequeña y la gente pregunta por el precio.** "psicólogo" + "psicologo" (sin acento) juntos equivalen a ~1/3 de "ansiedad". Las búsquedas de servicio (*psicólogo cerca de mí*, *terapia en línea*, *cuánto cobra un psicólogo*) tienen tan poco volumen que Trends las redondea a 0 frente a los términos grandes. Aun así, en el autocompletado dominan **"psicólogo gratis"** (en línea, CDMX, Simi, DIF, IMSS, para niños, 24 horas) y en las consultas en aumento aparecen *cuánto cobra un psicólogo*, *psicólogo en línea gratis*, *psicólogo infantil gratuito* (+5,050 %) y *terapeuta y psicólogo es lo mismo*. El tipo de terapia más buscado por nombre es **terapia de pareja** (CDMX, Guadalajara, Monterrey, Querétaro; en YouTube, *terapia de pareja por infidelidad*). Conclusión: **el puente hacia terapia se hace con contenido que resuelve dudas sobre síntomas ("¿esto que siento es ansiedad?") y que quita barreras ("¿cuánto cuesta?", "¿psicólogo o psiquiatra?", "¿cómo es la primera sesión?"), no con anuncios de "agenda tu cita".**
6. **La estacionalidad depende sobre todo de eventos y del calendario escolar, no de la "cuesta de enero".** Diciembre es el valle de casi todos los temas (–15 % a –45 % frente a su promedio). La excepción es "soledad". Julio es el segundo valle para todo lo ligado a la escuela. Los picos llegan con fechas y con cultura pop: **Intensamente 2** (junio de 2024) dejó el máximo histórico de "ansiedad"; también pesan el **Día del Psicólogo** (20 de mayo, +82 % para "psicólogo"), el **Día Mundial del Autismo** (2 de abril), el **Día Mundial de la Salud Mental** (10 de octubre, +76 % para "salud mental") y el **Día Mundial de Lucha contra la Depresión** (13 de enero).
7. **Hay ruido en los datos y hay que controlarlo.** Muchos términos se mezclan con canciones, lugares o noticias: "Ansiedad" de Fuerza Regida, "Duelo" (grupo musical), "Demasiada personalidad" de Carín León, "Insomnio mental" de Saúl de la Rosa, "Soledad de Graciano Sánchez", "depresión tropical", "Roth IRA". **Los índices de YouTube para emociones sueltas ("ansiedad", "soledad", "duelo", "tristeza", "celos") están inflados por música.** Para planear, conviene la frase con intención ("cómo superar…", "qué es el apego ansioso") y no la palabra suelta.

---

## 1. Método

| Paso | Qué se hizo | Cobertura |
|---|---|---|
| 1. Interés en el tiempo | 40 términos en 7 grupos (emociones, relaciones, familia, trabajo, neurodivergencia, autoconocimiento, terapia). Lotes de 5 con **"psicólogo" como ancla común** en cada lote. Cada índice se expresa como *veces el volumen de "psicólogo"* (suma del término ÷ suma del ancla × 100). | Google y YouTube · 5 años (semanal) y 12 meses (semanal) · 40 llamadas de serie |
| 1b. Variantes | Lotes extra con formas **sin acento** y frases reales ("psicologo", "depresion", "terapia online", "relacion toxica", "apego ansioso", "sobrepensar", "terapia de pareja", "psicologo gratis"…) | Google 5a/12m + YouTube 12m |
| 2. Consultas relacionadas | "Principales" (top) y "en aumento" (rising) de los últimos 12 meses para cada término | ~2,100 filas, Google y YouTube |
| 3. Estacionalidad | Serie semanal de Google a 5 años → cociente de cada semana contra su media móvil de 52 semanas → promedio por mes (100 = mes típico) | 31 términos con datos suficientes |
| 3b. Estados | Interés por estado (12 meses, Google), un término por consulta para que el índice 0–100 sea comparable entre estados | 11 términos clave |
| 4. Sopa de letras | 41 raíces × (raíz sola + a–z + ñ) × Google y YouTube = **2,296 consultas de autocompletado → ~16,450 sugerencias únicas (fuente × texto)**. Se clasificaron por expresiones regulares en 20 temas y se ponderaron por posición (las primeras sugerencias y las de la raíz sola valen más) | 0 consultas fallidas |

Raíces de la sopa: *la psicología de las personas que · por qué me siento · cómo dejar de · cómo saber si · señales de que · por qué las personas · psicólogo · terapia · ansiedad · mi pareja · mi mamá · mi hijo*. Se añadieron dos rondas: (a) *qué hacer si · es normal · por qué no puedo · cómo superar · cómo manejar · test de*; (b) *cómo saber si tengo · cómo saber si soy · señales de que tienes · señales de que eres · mi pareja me · mi pareja no · por qué mi pareja · mi mamá me · mi mamá no · mi papá · mi hijo no · mi hijo adolescente · mi jefe · por qué soy · por qué siento · cómo controlar · cómo ayudar a · qué hacer cuando · cómo dejar de pensar en · es normal sentir · cómo poner límites · psicólogo gratis · cómo ser más*.

## 2. Cómo leer los números (limitaciones importantes)

- **Google Trends da índices relativos (0–100), no volúmenes.** Cada consulta se escala contra su propio máximo. Aquí todo se reexpresa contra el ancla "psicólogo" para comparar entre lotes, pero **"656" no significa 656 búsquedas: significa ~6.6 veces lo que se busca "psicólogo"**.
- **Redondeo y umbral de privacidad.** Trends redondea a enteros y pone 0 cuando el volumen relativo es bajo. Por eso frases largas como "psicólogo cerca de mí", "terapia en línea" o "cuánto cuesta un psicólogo" salen en ~0. **Eso no quiere decir que nadie las busque**: son una fracción mínima de "ansiedad" o "depresión". El autocompletado confirma que esas búsquedas existen.
- **El ancla en YouTube es débil.** "psicólogo" vale ~2–7 puntos en YouTube. Los índices de YouTube tienen un error de redondeo de ±20–30 % y **conviene leerlos como orden de magnitud o como ranking**, no como cifra exacta.
- **Los acentos parten la demanda.** Trends trata "psicólogo" y "psicologo" (y "depresión" y "depresion") como consultas distintas, de tamaño parecido. Los términos con tilde están **subestimados ~50 %** frente a los que no la llevan (ansiedad, TDAH, autismo, narcisista, apego). Ejemplo: psicólogo 100 + psicologo ≈ 123 → ~223. Depresión 191 + depresion ≈ 172 → ~363.
- **Contaminación semántica.** Trends cuenta todas las búsquedas que contienen el término, sin importar la intención (ver tabla §3, columna "ruido").
- **El autocompletado refleja popularidad, pero no la mide.** Google filtra términos sensibles (autolesión y suicidio aparecen poco a propósito) y las sugerencias varían con el tiempo. El conteo de sugerencias por tema depende de qué raíces se eligieron. **Su valor está en las frases exactas, no en los conteos.**
- **El periodo de 5 años empieza en noviembre de 2021**, todavía en la ola de interés por salud mental de la pandemia. Por eso varios temas "caen" en 5 años aunque en el último año estén estables.
- Reddit no fue accesible. Tampoco se usaron herramientas de pago (Ahrefs/Semrush), que sí dan volúmenes absolutos.

---

## 3. Volumen relativo por tema

**Índice = veces "psicólogo" (con acento) = 100.** Últimos 12 meses. Orden según Google.

| Término | Grupo | Google 12m | YouTube 12m | Ruido / comentario |
|---|---|---:|---:|---|
| ansiedad | emociones | **657** | 2,962* | Google bastante limpio. YouTube inflado por la canción "Ansiedad" (Fuerza Regida) y por *música para la ansiedad* |
| adolescentes | familia | 610* | 1,789* | Muy contaminado: tareas escolares ("derechos de niñas, niños y adolescentes"), la banda Los Adolescentes, películas |
| personalidad | autoconocimiento | 353 | 500* | Parte real (trastorno límite de la personalidad, tests). En YouTube domina la canción "Demasiada personalidad" |
| soledad | emociones | 337* | 2,704* | Soledad de Graciano Sánchez (SLP), *Cien años de soledad*, canciones |
| autismo | neurodivergencia | **292** | 273 | Limpio. Sobre todo *niños con autismo*, *test de autismo*, *autismo nivel 1* |
| divorcio | familia | 289 | 712* | Google: trámite legal (acta, divorcio incausado). YouTube: dramas chinos "tras el divorcio…" |
| TDAH | neurodivergencia | **253** | 220 | Limpio |
| duelo | relaciones | 243* | 3,646* | El grupo musical "Duelo" contamina. La parte psicológica es *etapas del duelo* |
| depresión | emociones | 191 (+172 sin acento ≈ **363**) | 407 | Contaminada por "depresión tropical" (huracanes), *depresión sonora* (banda) |
| salud mental | terapia | 181 | 126 | Limpio, muy escolar y estacional (pico en octubre) |
| estrés | emociones | 175 | 173 | Limpio (*diferencia entre estrés y ansiedad*) |
| ira | emociones | 167* | 536* | Roth IRA, "irá al mundial", canciones |
| trauma | autoconocimiento | 147* | 183 | Manhwa *Alpha Trauma*, trauma médico |
| tristeza | emociones | 142 | 1,823* | Intensamente; música en YouTube |
| narcisista | relaciones | **119** | 346 | Limpio en Google. En YouTube, la canción "Narcisista por excelencia" (Panda) |
| psiquiatra | terapia | 115 | 388 | Limpio |
| **psicólogo** (ancla) | terapia | 100 (+123 sin acento) | 100 | Pico cada 20 de mayo |
| apego | relaciones | 97 | 131 | Limpio. En YouTube, *apego ansioso* > *apego evitativo* > *el apego* |
| celos | relaciones | 94 | 1,207* | Canciones (Vicente Fernández, "Estos celos") |
| autoestima | autoconocimiento | 93 | 214 | Muy escolar |
| infidelidad | relaciones | 90 | 467* | Noticias (Messi, CEO de Nvidia), películas, Badabun |
| insomnio | emociones | 87 | 948* | Canción "Insomnio mental" |
| burnout | trabajo | 78 | 162* | Videojuego *Burnout*; *signs of burnout* en aumento |
| ruptura | relaciones | 77 | 177 | Médico (membranas, tendón) en Google; en YouTube sí es *superar una ruptura amorosa* |
| crianza | familia | 57 | 98 | Vino "crianza", crianza de animales |
| inteligencia emocional | autoconocimiento | 47 | 55 | Goleman, escuela |
| test de personalidad | autoconocimiento | 22 | 3 | MBTI, 16 personalidades |
| introvertido | autoconocimiento | 22 | 8 | *diferencia entre introvertido y tímido* en aumento |
| TDAH adultos | neurodivergencia | 17 | 27 | Ver crecimiento |
| dependencia emocional | relaciones | 11 | 20 | |
| autismo adultos | neurodivergencia | 7 | 3 | Base pequeña, crecimiento enorme |
| terapia psicológica | terapia | 7 | ~0 | |
| estrés laboral | trabajo | 7 | ~0 | |
| ataque de pánico | emociones | 3 | ~0 | (la gente escribe "ataque de ansiedad") |
| síndrome del impostor | trabajo | 1.4 | 0.8 | Base mínima, sube rápido |
| relación tóxica · padres tóxicos · jefe tóxico · terapia en línea · psicólogo cerca de mí · cuánto cuesta un psicólogo | | ~0 | ~0 | Por debajo del umbral frente a términos grandes (ver §2) |

\* = índice inflado por ruido no psicológico.

**Variantes sin acento y frases reales** (lotes extra, mismo ancla; archivo `variantes_indices.csv`):

| Término | Google 12m | YouTube 12m | Lectura |
|---|---:|---:|---|
| psicologo (sin acento) | 123 | 143 | Más usado que "psicólogo" → demanda real de la palabra ≈ 223 |
| depresion (sin acento) | 171 | 510 | Depresión total ≈ 361 en Google |
| terapia de pareja | **15** | 13 | **El tipo de terapia más buscado.** Principales: *terapia de pareja CDMX, Guadalajara, Monterrey, Querétaro, cerca de mí, en línea, gratuita*. En YouTube: *terapia de pareja por infidelidad* |
| apego ansioso | 16 | **46** | Pesa 3 veces más en YouTube. En aumento: *apego ansioso cómo superarlo* (Breakout, +31,050 %), *apego ansioso en niños* (+120 % en YouTube) |
| sobrepensar | 9 | **44** | Pesa 5 veces más en YouTube. Principales: *dejar de sobrepensar*, *qué es sobrepensar* |
| relacion toxica | 0.5 | **14** | Casi solo se busca en YouTube: *cómo salir de una relación tóxica*, *señales de una relación tóxica* |
| sindrome del impostor (sin acento) | 9.4 | 5 | Se escribe sin acento (la versión con tilde da 1.4) |
| ataque de panico / estres laboral (sin acento) | 7.6 / 8.1 | 3.7 / 0.4 | Igual: sumar las dos grafías. *Síntomas de estrés laboral* y *cómo evitar el estrés laboral* están en aumento |
| terapia en linea · terapia online · psicologo en linea | 2.0 · 0.3 · 0.8 | ~0 | Muy pequeño. Lo que domina es **"gratis"**: *terapia en línea gratis*, *psicólogo en línea gratis* |
| cuanto cobra un psicologo · psicologo gratis | ~0 · 0.1 | ~0 | Long tail. Principal: *cuánto cobra un psicólogo por sesión* |
| padres toxicos · jefe toxico · psicologo cerca de mi | 0 | 0 | Por debajo del umbral |

**Hallazgo:** el vocabulario "pop-psicológico" (apego ansioso, sobrepensar, relación tóxica) es **nativo de YouTube**. Relativo al ancla, se busca entre 3 y 28 veces más allí que en Google, mientras que términos institucionales como "salud mental" o "terapia de pareja" pesan igual o menos en YouTube.

**Lectura limpia (solo intención psicológica), de mayor a menor demanda en Google:**
**ansiedad ≫ depresión (sumando ambas grafías) > autismo ≈ TDAH > psicólogo/psicologo > salud mental > estrés > narcisista ≈ psiquiatra > apego ≈ autoestima ≈ celos ≈ infidelidad > insomnio > burnout > inteligencia emocional > dependencia emocional.**

**En YouTube (quitando música):** depresión, psiquiatra, narcisista, autismo, TDAH, autoestima, superar una ruptura, estrés, apego ansioso o evitativo y salud mental. En YouTube domina el "cómo superar…" y el "qué tipo de… tengo".

---

## 4. Crecimiento

### 4.1 Cambio anual y a 5 años (Google y YouTube, series semanales)

*Cambio anual = últimas 52 semanas contra las 52 previas. Cambio a 5 años = últimas 52 semanas contra las primeras 52 (nov 2021–nov 2022).*

| Término | Google anual | Google 5 años | YouTube anual | YouTube 5 años |
|---|---:|---:|---:|---:|
| autismo adultos | −44 % (base chica) | **+100 %** | +20 % | **+1,100 %** |
| TDAH adultos | −17 % | +13 % | −10 % | **+338 %** |
| TDAH | −6 % | +9 % | +1 % | **+226 %** |
| autismo | −3 % | +3 % | +2 % | +76 % |
| depresión | +4 % | −39 % | **+43 %** | +84 % |
| apego | −3 % | −6 % | +6 % | +64 % |
| trauma | +28 %* | +17 % | +11 % | +60 % |
| salud mental | −19 % | −28 % | −6 % | +55 % |
| burnout | **+19 %** | +4 % | +4 % | +38 % |
| crianza | −13 % | −4 % | +5 % | +36 % |
| ruptura | +9 % | −9 % | **+26 %** | +31 % |
| estrés | **+23 %** | 0 % | +5 % | −22 % |
| síndrome del impostor | **+137 %** (base mínima) | −30 % | +150 % | +150 % |
| ataque de pánico | +62 % (base mínima) | −7 % | — | — |
| psicólogo (ancla) | +10 % | −3 % | +2 % | +18 % |
| psiquiatra | +5 % | +6 % | −10 % | +5 % |
| narcisista | −8 % | −48 % | −13 % | +23 % |
| ansiedad | −5 % | −33 % | −35 %* | +89 %* |
| autoestima | −19 % | −62 % | −17 % | −37 % |
| dependencia emocional | −14 % | −65 % | −29 % | −23 % |
| inteligencia emocional | −25 % | −55 % | −27 % | −40 % |
| test de personalidad | −67 % | −86 % | −70 % | −88 % |
| introvertido | −78 % | −96 % | −46 % | −14 % |

**Lectura:**
- **YouTube crece y Google se estanca en lo informativo.** Las búsquedas tipo "qué es X" en Google bajan en casi todos los temas desde 2021 (fin de la ola pandémica y probablemente más respuestas directas o de IA en el buscador). En YouTube, en cambio, crecen depresión, apego, trauma, salud mental, crianza y ruptura. **Esto respalda el formato video del canal.**
- **Neurodivergencia adulta = el nicho que más crece en los dos buscadores.**
- **Trabajo (burnout, estrés, impostor) sube en el último año en Google.** Es un nicho pequeño pero en ascenso.
- **Lo que pasó de moda:** tests de personalidad genéricos, "introvertido" y la "inteligencia emocional" estilo Goleman. Si se tocan, que sea con otro ángulo, por ejemplo *introvertido vs. tímido* o *¿qué tipo de apego tengo?*.

### 4.2 Consultas "en aumento" más útiles (12 meses)

Se omiten las que vienen de canciones, dramas o noticias. "Breakout" = más de +5,000 %.

| Tema | Consulta en aumento | Fuente | Crecimiento |
|---|---|---|---:|
| Autismo adulto | cómo detectar autismo en adultos | Google | +85,500 % |
| Autismo adulto | cómo se diagnostica el autismo en adultos | Google | +51,450 % |
| Autismo adulto | rasgos de autismo en adultos | YouTube | +138,250 % |
| Autismo adulto | autismo en mujeres adultas | YouTube | +950 % |
| Autismo adulto | quién diagnostica el autismo en adultos · autismo leve en adultos | Google | +130 % · +120 % |
| TDAH | cómo saber si tengo TDAH | Google | +150 % |
| TDAH | TDAH en mujeres adultas | Google | +140 % |
| TDAH | cómo se trata el TDAH en adultos · quién diagnostica TDAH en adultos | Google | +400 % · +170 % |
| TDAH | prueba de TDAH · ruido marrón TDAH · ejercicios para niños con TDAH | YouTube | +140 % · +140 % · +90 % |
| Neurodivergencia | neurodivergente · neurodivergencia | Google | +70–100 % |
| Síndrome del impostor | qué es el síndrome del impostor | YouTube | Breakout |
| Estrés/ansiedad | cuál es la diferencia entre estrés y ansiedad | Google | Breakout (+47,250 %) |
| Ansiedad | qué es la ansiedad social · cómo se siente la ansiedad · cómo calmar la ansiedad · qué puedo tomar para la ansiedad | Google | +160 % · +70 % · +60 % · +60 % |
| Ansiedad | la ansiedad me tiene miedo · calmar la ansiedad · música para calmar la ansiedad | YouTube | +110 % · +60 % · +40 % |
| Depresión | cómo ayudar a una persona con depresión (y ansiedad) | Google | +70 % |
| Depresión | test de depresión gratis · la depresión tiene cura · depresión funcional · depresión post concierto · depresión post viaje | Google | +40–80 % |
| Apego | qué tipo de apego tengo | YouTube | +4,900 % |
| Apego | qué es el apego ansioso · cómo sanar el apego ansioso | YouTube | +150 % · +100 % |
| Apego | apego evitativo pareja · apego ansioso y evitativo | Google | +90 % · +50 % |
| Dependencia emocional | cómo dejar de tener dependencia emocional | YouTube | +350 % |
| Narcisismo | cómo saber si una persona es narcisista · narcisista maligno · narcisista vulnerable · cómo dejar a un narcisista | Google/YouTube | +60–170 % |
| Celos | celos retroactivos · los celos son buenos o malos · test de celos · los celos no son amor | Google | +300 % · +650 % · +100 % · +70 % |
| Ruptura | fases de una ruptura amorosa · cómo sobrevivir a una ruptura | Google/YouTube | +350 % |
| Trauma | trauma bonding (vínculo traumático) | Google | +160 % |
| Introversión | diferencia entre introvertido y tímido | Google | +180 % |
| Burnout | signs of burnout · burnout emocional · burnout recovery | Google/YouTube | Breakout · +110 % · +200 % |
| Insomnio | por qué tengo insomnio · cómo quitar el insomnio | Google | +120 % · +70 % |
| Terapia | terapeuta y psicólogo es lo mismo · diferencia entre psicólogo y terapeuta | Google | +90 % · +60 % |
| Terapia | cuánto cobra un psicólogo · psicólogo online · psicólogo en línea gratis · psicólogo de pareja | Google | +40–50 % |
| Terapia | psicólogo infantil gratuito | Google | +5,050 % |
| Terapia | psicólogo o psiquiatra · psicólogo near me | Google | +50 % · +110 % |
| Formato viral | mi psicólogo dice… | YouTube | +500 % |

---

## 5. Estacionalidad (Google, 5 años)

Índice mensual: 100 = mes promedio de ese término. En **negritas**, los picos (≥ 115) y los valles (≤ 85).

| Término | ene | feb | mar | abr | may | jun | jul | ago | sep | oct | nov | dic | Causa principal |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| psicólogo | 92 | 99 | 97 | 94 | **182** | 91 | 86 | 99 | 102 | 99 | 91 | **69** | Día del Psicólogo (20 de mayo) |
| ansiedad | 94 | 98 | 103 | 102 | 103 | 106 | 102 | 103 | 102 | 100 | 101 | 86 | Estable. Pico histórico: Intensamente 2 (jun 2024) |
| depresión | 92 | 100 | 98 | 95 | 99 | **130** | **82** | 102 | 114 | **119** | 100 | **69** | Temporada de huracanes ("depresión tropical") + escuela |
| estrés | 86 | 106 | 112 | 105 | 104 | 96 | 89 | 97 | 107 | 112 | 109 | **77** | Ciclo escolar y laboral |
| soledad | 101 | 98 | 97 | 100 | 98 | 96 | 92 | 101 | 101 | 101 | 97 | **118** | Diciembre (*Cien años de soledad* en Netflix, dic 2024; fiestas) |
| tristeza | 98 | 105 | 102 | 95 | 98 | 105 | 89 | 88 | 112 | **116** | 106 | 86 | Escuela |
| apego | 88 | 100 | 104 | 103 | 100 | 99 | 97 | 101 | 108 | 114 | 102 | **83** | |
| ruptura | 87 | 112 | 109 | 106 | 106 | 97 | 92 | 97 | 105 | 104 | 103 | **80** | Febrero (San Valentín) |
| dependencia emocional | 87 | 103 | 110 | 113 | **116** | 98 | 95 | 87 | 98 | 103 | 107 | **83** | |
| narcisista | 94 | 94 | 100 | **115** | 104 | 107 | 113 | 106 | 96 | 95 | 86 | 90 | |
| duelo | 105 | **117** | 104 | 102 | 98 | 95 | 92 | 94 | 96 | 100 | 102 | 96 | |
| infidelidad · celos | ≈100 todo el año | | | | | | | | | | | | Sin estacionalidad |
| autismo | 87 | 96 | **162** | **123** | 89 | 88 | 92 | 94 | 105 | 99 | 89 | **76** | Día Mundial del Autismo (2 de abril) |
| TDAH | 98 | 103 | 110 | 91 | 99 | 99 | 106 | 96 | 110 | 103 | 101 | 84 | Inicio de ciclos escolares |
| burnout | 86 | 99 | 102 | 103 | 113 | **125** | 99 | 95 | 94 | 96 | 99 | 89 | Fin del semestre o año laboral |
| estrés laboral | **74** | **125** | 112 | **123** | 109 | 100 | **73** | 84 | 97 | **118** | **141** | **43** | Escolar y de recursos humanos |
| autoestima | 90 | **118** | **117** | 91 | 104 | 89 | **60** | **82** | **133** | **136** | **117** | **62** | 100 % escolar |
| salud mental | 87 | **116** | 105 | 88 | 104 | 84 | **61** | 88 | **125** | **176** | 112 | **55** | Día Mundial de la Salud Mental (10 de octubre) + escuela |
| crianza · adolescentes | 97 | 113 | 109 | 92 | 103 | 90 | **72** | 84 | 113 | **124** | **119** | **78** | Escolar |
| trauma | 97 | 100 | 97 | 95 | 92 | **147** | 84 | 88 | 84 | 79 | 111 | **125** | Mezclado con el manhwa |
| insomnio | 106 | 101 | 103 | 111 | 98 | 92 | 113 | 110 | 94 | 93 | 88 | 91 | Calor (abr–ago) |

**Conclusiones de calendario:**
- **Enero no es un pico.** Ningún término psicológico sube de forma clara en enero. Febrero sí (regreso real a la rutina y San Valentín: ruptura, duelo, estrés laboral).
- **Diciembre es el valle general** (la gente busca menos de todo), **salvo soledad**. Contenido de diciembre: soledad en fiestas, duelo en Navidad, "mi familia me estresa en las posadas", y producción adelantada para enero y febrero.
- **Regreso a clases (agosto–octubre) = pico de autoestima, salud mental, crianza, adolescentes y estrés.** Mucha de esa demanda es de estudiantes que hacen tareas. Para el canal es una ventana para piezas explicativas que los maestros compartan ("qué es la autoestima, explicado con caricaturas").
- **Fechas ancla:** 13 de enero (depresión), 14 de febrero (rupturas y apego), 2 de abril (autismo), 20 de mayo (Día del Psicólogo en México: "¿qué hace un psicólogo?", "¿psicólogo o psiquiatra?"), 10 de octubre (salud mental), diciembre (soledad y duelo).
- **Cultura pop = los picos más grandes.** El máximo de 5 años de "ansiedad" coincide con *Intensamente 2* (junio 2024); "soledad" con *Cien años de soledad*; "depresión post concierto" y "Messi autismo" también aparecen. **El personaje animado puede montarse en estrenos y fenómenos virales** (películas, canciones como "Ansiedad" o "Narcisista", realities).

---

## 6. Diferencias por estado

*Google, 12 meses. Índice 0–100 = proporción de búsquedas del término sobre el total de búsquedas del estado, escalada al estado máximo. Un término por consulta (archivo `estados_interes_por_termino.csv`). En estados pequeños (Colima, Campeche, BCS) hay más ruido, y un 0 significa que no alcanzan el umbral.*

| Término | Estados más altos (100 = máximo) | Estados más bajos |
|---|---|---|
| ansiedad | Guerrero 100, Michoacán 99, Chiapas 97, Colima 95, Sinaloa 95, Guanajuato 94 | CDMX 71, BCS 62, Quintana Roo 53 |
| depresión (sin acento) | Sonora 100, Durango 99, SLP 99, Colima 99, Sinaloa 99, Zacatecas 96 | Veracruz 70, Puebla 68, Q. Roo 60 |
| psicólogo (sin acento) | Sinaloa 100, Sonora 99, Baja California 95, Durango 94, CDMX 92, Nayarit 92 | Campeche 66, Oaxaca 64, Chiapas 62 |
| TDAH | Sinaloa 100, Colima 93, Sonora 90, Nayarit 89, Nuevo León 88 | Oaxaca 64, Guanajuato 63, Puebla 61 |
| autismo | Sinaloa 100, Baja California 99, Campeche 98, Sonora 95, Nayarit 90 | CDMX 61, Guanajuato 60, Querétaro 58 |
| apego | Colima 100, **CDMX 99**, Morelos 98, Edomex 96, Nayarit 93 | Nuevo León 76, Coahuila 74, Q. Roo 71 |
| narcisista | Durango 100, Colima 95, Morelos 94, Chihuahua 93, Sonora 92 | Q. Roo 68, Tabasco 68, Puebla 67 |
| terapia de pareja | **CDMX 100, Querétaro 93, Edomex 91, Jalisco 86, Yucatán 85** | Guerrero 40, Colima 0, Campeche 0 |
| burnout | Zacatecas 100, **CDMX 96**, Sonora 89, Yucatán 89 | Edomex 63, Tlaxcala 62, Chiapas 58 |
| autoestima | Tlaxcala 100, Oaxaca 96, Zacatecas 96, Guerrero 90, Hidalgo 90, Puebla 89 | Sonora 49, BCS 46, Q. Roo 44 |
| divorcio | Aguascalientes 100, Campeche 100, Nuevo León 99, Tabasco 96, Zacatecas 96 | Querétaro 70, BCS 67, Puebla 64 |

**Patrones:**
- **Las ciudades con mercado de terapia buscan "servicio" y conceptos de relación.** CDMX, Querétaro, Edomex, Jalisco (Guadalajara) y Yucatán (Mérida) lideran *terapia de pareja*. CDMX también sobresale en *apego* y *burnout*. Son las plazas con más probabilidad de pagar terapia privada o en línea, y el público natural de Agenda PSI.
- **El noroeste (Sinaloa, Sonora, Baja California, Nayarit, Durango) se interesa más en neurodivergencia y en "psicólogo".** TDAH, autismo y psicólogo tienen ahí sus índices más altos. Es una oportunidad para contenido de diagnóstico adulto con ejemplos del norte.
- **El sur y el occidente (Guerrero, Michoacán, Chiapas, Oaxaca, Guanajuato) concentran la búsqueda de "ansiedad"**, con menor búsqueda de "psicólogo". La brecha entre malestar y acceso es mayor ahí, así que pesa el contenido gratuito, de autocuidado y de "cuándo pedir ayuda", y la mención de opciones de bajo costo.
- **"Autoestima" sobre-indexa en estados del centro-sur con mucha población estudiantil** (Tlaxcala, Oaxaca, Puebla, Hidalgo, Guerrero), lo que es coherente con su estacionalidad escolar.
- El norte industrial (Nuevo León, Aguascalientes, Coahuila) sobre-indexa en *divorcio*, que es sobre todo trámite.

---

## 7. Sopa de letras: lo que la gente escribe de verdad

**Totales:** ~16,450 sugerencias únicas; ~3,300 de las ~8,200 de la primera ronda se clasificaron como psicológicas. El resto son ruido: salud física, trámites, WhatsApp, canciones, dramas.

### 7.1 Peso por tema en el autocompletado (ronda 1)

*Puntuación ponderada por posición; depende de las raíces elegidas, así que es orientativa.*

| Tema | Sugerencias Google | Sugerencias YouTube | Comentario |
|---|---:|---:|---|
| Terapia y acceso al psicólogo | 295 | 279 | Tipos de terapia, *gratis*, *en línea*, *infantil*, *psicólogo o psiquiatra* |
| Ansiedad, pánico y sobrepensar | 273 | 257 | El tema emocional más rico |
| Crianza e hijos | 284 | 252 | Mucho ruido médico pediátrico, pero muchas preguntas de conducta |
| Familia (mamá, papá) | 241 | 251 | "mi mamá no me quiere", "me grita", "me hace sentir mal" |
| "La psicología de las personas que…" / rasgos | 94 | 128 | **Formato viral**, con el mayor peso por sugerencia |
| Hábitos y adicciones | 111 | 91 | fumar, alcohol, celular, procrastinar, casino |
| Pareja: ruptura, ex, desamor | 77 | 90 | |
| Atracción y "señales de que le gustas" | 27 | 78 | **Muy fuerte en YouTube** (público joven) |
| Tristeza, depresión, vacío | 71 | 45 | |
| Síntomas físicos (mareo, cansancio, falta de aire) | 74 | 29 | Puente cuerpo–ansiedad |
| Soledad y aislamiento | 27 | 37 | |
| Sueño | 49 | 27 | |
| Trauma, heridas, duelo | 43 | 36 | "herida de abandono", "heridas de la infancia" |
| Celos, infidelidad | 28 | 41 | |
| Apego, dependencia, narcisismo, violencia | 33 | 39 | |
| Enojo, gritos | 36 | 23 | "cómo dejar de gritar a mis hijos" |
| Miedos, fobias, TOC | 56 | 22 | |
| Autoestima, validación | 32 | 41 | "cómo dejar de necesitar validación" |
| Neurodivergencia | 35 | 25 | |
| Estrés y burnout | 23 | 7 | |

### 7.2 Preguntas exactas por tema (seleccionadas de las sugerencias reales)

Se escriben tal como la gente las teclea (sin corregir tildes en algunos casos). Sirven como títulos o ganchos.

**Ansiedad, sobrepensar y cuerpo**
- cómo dejar de pensar demasiado · cómo dejar de sobrepensar · cómo dejar de sobrepensar y tener ansiedad
- cómo dejar de pensar en escenarios ficticios · la psicología de las personas que imaginan escenarios falsos
- cómo dejar de pensar en bucle · cómo dejar de pensar en cosas que no puedo controlar · cómo dejar de pensar en el futuro y vivir el presente
- cómo dejar de preocuparme por todo · cómo dejar de estresarme por todo
- cómo controlar un ataque de ansiedad · cómo controlar los nervios · cómo controlar las emociones
- por qué me siento nervioso sin razón · por qué me siento nerviosa de la nada · por qué me siento ansiosa y desesperada
- por qué siento que me falta el aire · por qué siento que me voy a morir · por qué siento que me voy a desmayar · por qué siento presión en el pecho · por qué siento un nudo en la garganta
- por qué me siento como si no fuera yo · por qué no me siento real (despersonalización)
- ansiedad: qué es y síntomas · ansiedad que se siente · ansiedad social · ansiedad generalizada · ansiedad y depresión · ansiedad o estrés (es lo mismo) · ansiedad al dormir · ansiedad hipocondría
- cómo dejar de comer por ansiedad · es normal sentir ansiedad en el embarazo
- cómo ayudar a alguien con un ataque de ansiedad · qué hacer cuando alguien tiene un ataque de ansiedad
- cómo saber si tengo ansiedad · señales de que tienes ansiedad

**Tristeza, depresión y vacío**
- por qué me siento sin ganas de hacer nada · por qué me siento cansada sin ganas de nada
- por qué me siento vacío (por dentro) · por qué me siento vacía emocionalmente · por qué me siento vacío cuando me miro al espejo
- por qué me siento triste sin razón · por qué me siento triste de la nada · es normal sentir ganas de llorar de la nada
- cómo dejar de llorar por todo · por qué no puedo llorar · la psicología de las personas que lloran con facilidad
- cómo superar la depresión · cómo saber si tengo depresión · señales de que tienes depresión · test de depresión
- cómo ayudar a una persona con depresión · cómo ayudar a mi hijo con depresión · mi pareja tiene depresión y me está afectando
- por qué me siento insuficiente · por qué me siento inferior a los demás · por qué me siento culpable de todo
- la psicología de las personas que están cansadas de existir · cómo dejar de vivir en modo supervivencia

**Soledad**
- por qué me siento solo / tan sola · por qué las personas se alejan de mí · por qué las personas me evitan / me ignoran
- cómo superar la soledad · cómo superar la soledad de no tener pareja · señales de que creciste en soledad
- la psicología de las personas que prefieren estar solas / les encanta quedarse en casa / viven solas / tienen pocos amigos

**Pareja: lo que la gente vive (raíz "mi pareja me…/no…")**
- mi pareja me aplica la ley del hielo · me castiga con el silencio · me ignora después de discutir · me deja de hablar por días
- mi pareja me culpa de todo · me hace sentir culpable · me hace sentir insuficiente / insegura / sola
- mi pareja me critica constantemente · me compara con su ex · me juzga por mi pasado
- mi pareja me agota psicológicamente · me desestabiliza emocionalmente · me drena la energía · me causa ansiedad
- mi pareja me grita (cuando se enoja / delante de mis hijos) · golpea la pared cuando se enoja · me aleja de mi familia · me amenaza con dejarme cada vez que discutimos
- mi pareja me bloquea y me desbloquea · me corre de la casa cuando discutimos
- mi pareja no acepta sus errores y me culpa · no quiere hablar de nuestros problemas · nunca reconoce sus errores · no me valora · no me demuestra afecto · no entiende mi ansiedad / depresión / duelo
- por qué peleo tanto con mi pareja · por qué no soy feliz con mi pareja · por qué desconfío tanto de mi pareja · por qué mi pareja se enoja por todo · mi pareja ya no me desea
- mi pareja tiene apego evitativo / apego ansioso · mi pareja es narcisista · mi pareja dice que soy narcisista · mi pareja tiene TDAH

**Rupturas, ex y desamor**
- cómo superar una ruptura amorosa (rápido) · cómo superar a tu ex · cómo superar una separación (con hijos / cuando todavía se ama / si aún vivimos juntos)
- cómo dejar de pensar en mi ex · cómo dejar de amar / querer a alguien (que no te quiere) · cómo superar a un casi algo
- cómo superar que mi ex ya tiene pareja · cómo superar ver a tu ex con otra persona · cómo superar el ghosting
- señales de que tu ex te ama aunque lo niegue · fases de una ruptura amorosa · por qué no puedo olvidarte

**Celos, infidelidad, confianza**
- cómo superar una infidelidad (y seguir con tu pareja / y recuperar la confianza) · mi pareja me fue infiel y no lo supero
- cómo superar haber sido infiel · qué hacer si fui infiel y estoy arrepentido · cómo dejar de ser infiel
- por qué las personas son infieles · qué dice la psicología de las personas infieles
- cómo dejar de ser celosa/celoso · cómo superar los celos y la desconfianza · celos retroactivos (retrospectivos)
- mi pareja me acusa injustamente de serle infiel · por qué sueño que mi pareja me es infiel

**Apego, dependencia, narcisismo y violencia**
- cómo superar el apego ansioso · qué tipo de apego tengo · apego ansioso y evitativo · cómo sanar el apego ansioso
- cómo dejar de depender emocionalmente de alguien · cómo dejar de necesitar a alguien · cómo dejar de idealizar a una persona · cómo dejar de obsesionarse con una persona
- cómo dejar de mendigar amor · cómo dejar de migajear · cómo dejar de buscar validación externa
- cómo saber si soy narcisista · señales de que eres narcisista · cómo manejar a una persona narcisista · cómo poner límites a una persona narcisista · cómo superar a un narcisista
- por qué las personas manipulan · cómo superar violencia psicológica · cómo superar relaciones tóxicas · cómo superar familia tóxica

**Familia (mamá, papá)**
- mi mamá no me quiere · mi mamá me odia (test) · mi mamá me grita todo el tiempo · mi mamá me hace sentir mal · mi mamá me hiere con sus palabras · mi mamá me genera ansiedad · mi mamá me juzga por todo · mi mamá me maltrata psicológicamente · mi mamá me ignora cuando le hablo
- la psicología de las personas que cortan el contacto con sus familias · cómo superar no ser el hijo preferido
- cómo poner límites con mi madre / con tus padres / con la familia / sin sentir culpa
- mi papá me gritó · mi papá no me quiere · mi mamá falleció y la extraño · mi papá falleció

**Crianza, hijos y adolescentes**
- mi hijo adolescente no me hace caso · me contesta mal · me falta al respeto · me grita y me insulta · dice que me odia · me ignora
- mi hijo adolescente se aísla · se siente solo · no tiene interés por nada · no quiere estudiar ni hacer nada · no quiere ir a la escuela · duerme todo el día
- mi hijo adolescente tiene ansiedad · tiene baja autoestima · tiene ataques de ira · se autolesiona · es adicto al móvil · consume drogas
- cómo poner límites a un adolescente · cómo poner límites a los niños sin dañarlos · cómo poner límites sin gritar
- cómo dejar de gritar a mis hijos · mi hijo grita mucho cuando se enoja · cómo controlar berrinches de 2 o 3 años · mi hijo llora por todo
- mi hijo no controla sus emociones · mi hijo no juega con otros niños · mi hijo no habla pero entiende todo · señales de que un niño tiene autismo
- cómo ayudar a gestionar las emociones en los niños · cómo ayudar a jóvenes con depresión / baja autoestima

**Autoestima y validación**
- cómo dejar de necesitar validación (externa) · cómo dejar de buscar la aprobación de los demás · cómo dejar de importarme lo que digan los demás · cómo dejar de compararme con los demás
- por qué me siento fea/feo · señales de que eres atractivo / feo (muy fuerte en YouTube) · cómo superar el autosabotaje · cómo superar las inseguridades
- señales de que intimidas · señales de que eres más atractivo de lo que crees

**Hábitos**
- cómo dejar de procrastinar (y empezar a hacer las cosas) · cómo dejar de usar tanto el celular · cómo dejar de hacer scroll / doomscrolling · cómo dejar de necesitar dopamina
- cómo dejar de fumar / tomar alcohol / apostar / jugar casino · cómo dejar de gastar dinero compulsivamente

**Enojo**
- cómo dejar de enojarme por todo · cómo manejar la ira y el enojo · por qué me siento enojada todo el tiempo · por qué me siento irritable · cómo dejar de gritar cuando me enojo · cómo dejar de llorar cuando me enojo

**Trauma y duelo**
- cómo superar la herida de abandono / de rechazo · cómo superar traumas de la infancia · cómo superar heridas emocionales
- cómo superar un duelo · cómo superar la muerte de un ser querido / de una mascota / de un hijo · cómo superar el nido vacío
- cómo dejar de pensar en una persona fallecida

**Miedos, TOC, pensamientos intrusivos**
- cómo superar pensamientos intrusivos · cómo dejar de pensar en pensamientos intrusivos · cómo superar el TOC de lavarse las manos · cómo superar la hipocondría · cómo superar la fobia social · cómo superar el miedo a hablar en público

**Trabajo**
- cómo superar el burnout (laboral) · cómo manejar el estrés laboral · cómo superar el síndrome del impostor
- mi jefe me hace sentir mal · mi jefe no valora mi trabajo · mi jefe habla mal de mí a mis espaldas · qué hacer cuando tu jefe te menosprecia / te trata mal · cómo poner límites a un jefe tóxico / narcisista · cómo poner límites en el trabajo

**Neurodivergencia**
- cómo saber si tengo autismo / TDAH · cómo saber si soy autista · señales de que eres autista · señales de que eres neurodivergente · señales de que eres altas capacidades
- test de autismo · test de TDAH (para adultos gratis) · test de neurodivergencia
- cómo controlar a un niño hiperactivo · mi hijo adolescente con TDAH quiere estudiar pero reprueba · mi pareja tiene TDAH

**"Cómo saber si soy…" (autoconocimiento)**
- bipolar · narcisista · autista · celosa · hipocondríaca · introvertida o extrovertida · inteligente · atractivo · bisexual / gay (presentes y frecuentes)
- por qué soy tan sensible · por qué soy demasiado sensible · por qué soy así · por qué soy diferente a los demás · por qué soy antisocial · por qué soy insegura · por qué soy tan celosa · por qué soy muy enojona · por qué no soy feliz

**La psicología de las personas que… (top de ambos buscadores)**
imaginan escenarios falsos · mantienen su casa limpia · saben arreglarlo todo · guardan objetos por si algún día sirven · no quieren tener hijos · prefieren estar en casa · les encanta estar solas · tienen demasiados intereses · no publican fotos en redes · tratan a sus mascotas como hijos · lloran con facilidad · no celebran su cumpleaños · no ven futbol · piensan demasiado · hablan solas · desaparecen sin explicar nada · cortan el contacto con su familia · se quedan calladas cuando están heridas · te castigan con silencio · son demasiado conscientes · han pasado por demasiado · nunca piden ayuda · se enojan por todo · llegan tarde · son infieles · tienen pocos amigos · están cansadas de existir.

**Terapia y acceso (raíces "psicólogo", "terapia", "psicólogo gratis")**
- psicólogo cerca de mí · psicólogo gratis (en línea / chat / CDMX / 24 horas / Simi / DIF / IMSS / del gobierno / anónimo / para hablar / para jóvenes / para niños)
- psicólogo o psiquiatra (para la ansiedad / para la depresión) · psicólogo y psiquiatra es lo mismo · terapeuta y psicólogo es lo mismo
- terapia cognitivo conductual · terapia de pareja · terapia Gestalt · terapia familiar · terapia para la ansiedad · terapia para dormir
- cuánto cobra un psicólogo · psicólogo privado · psicólogo en línea · psicólogo infantil
- por qué las personas van al psicólogo / al psiquiatra · qué hace un psicólogo
- En YouTube, "psicólogo" se usa sobre todo para buscar **creadores** (Fernando Leiva, Walter Riso, Mario Guerra, Juan Carlos Escamilla, Enrique Villanueva) y el formato **"psicólogo reacciona"**. Esa es la competencia directa y también un formato probado.

---

## 8. Mapa de demanda

Escala: Volumen (V) y Crecimiento (C): ●●● alto · ●● medio · ● bajo. **Puente a terapia** = qué tan natural es cerrar el video con "esto vale la pena hablarlo con un profesional".

| # | Tema | V | C | Puente a terapia | Ángulo recomendado |
|---|---|---|---|---|---|
| 1 | **Ansiedad y sobrepensar** (síntomas, cuerpo, ataques) | ●●● | ●● (sube en YouTube) | **Alto** | "¿Esto que siento es ansiedad?", "por qué me falta el aire", "cómo dejar de sobrepensar" |
| 2 | **Neurodivergencia adulta** (TDAH, autismo, mujeres) | ●● | ●●● | **Muy alto** (diagnóstico) | "Señales de TDAH en adultos que nadie te dijo", "¿quién diagnostica autismo en adultos?" |
| 3 | **Apego y patrones de pareja** (ansioso, evitativo, dependencia, idealizar) | ●● | ●● | **Alto** | "¿Qué tipo de apego tienes?", "cómo dejar de mendigar amor" |
| 4 | **Dinámicas de pareja dañinas** (ley del hielo, culpa, gritos, control) | ●● (long tail enorme) | ●● | **Muy alto** (+ violencia) | Narrar en primera persona con el personaje: "Mi pareja me aplica la ley del hielo" |
| 5 | **Rupturas y desamor** | ●● | ●● (+26 % en YouTube) | Medio | "Fases de una ruptura", "por qué no puedo olvidar a mi ex" |
| 6 | **Depresión, vacío y tristeza sin razón** | ●●● | ●● (+43 % en YouTube) | **Muy alto** | "Por qué me siento vacío", "depresión funcional", "cómo ayudar a alguien con depresión" |
| 7 | **Narcisismo** (pareja, madre, jefe) | ●● | ● | Alto | "¿Narcisista o solo egoísta?", "madre narcisista", "cómo poner límites a un narcisista" |
| 8 | **Familia y madre** (no me quiere, me grita, límites, cortar contacto) | ●● | ● | Alto | "Cómo poner límites a tu mamá sin sentir culpa" |
| 9 | **Crianza y adolescentes** (no me hace caso, se aísla, gritos) | ●● | ● | **Alto** (terapia infantil o familiar) | "Mi hijo adolescente se aísla: ¿normal o alerta?", "cómo dejar de gritar a mis hijos" |
| 10 | **"La psicología de las personas que…"** | ●●● (YouTube) | ●●● (formato viral) | Bajo-medio (puerta de entrada) | Serie fija del personaje, ideal para Shorts y TikTok |
| 11 | **Autoestima y validación** | ●● | ● (Google) | Medio | "Cómo dejar de necesitar validación" |
| 12 | **Trabajo: burnout, impostor, jefe** | ● | ●● (+19 a +137 %) | Alto | "Señales de burnout", "síndrome del impostor explicado" |
| 13 | **Duelo y trauma de infancia** (abandono, rechazo) | ●● | ● | **Muy alto** | "Herida de abandono", "duelo en Navidad" |
| 14 | **Soledad** | ●● (con ruido) | ● (pico en diciembre) | Medio | "Por qué las personas se alejan de mí" |
| 15 | **Acceso a terapia** (precio, gratis, tipos, psicólogo vs. psiquiatra) | ● (pero intención de compra) | ●● | **Conversión directa** | "¿Cuánto cuesta ir al psicólogo en México?", "¿psicólogo o psiquiatra?", "qué pasa en la primera sesión" |
| 16 | Hábitos (procrastinar, celular, dopamina) | ●● | ●● | Bajo-medio | "Cómo dejar de hacer scroll" |
| 17 | Celos e infidelidad | ●● | ● | Medio-alto | "Celos retroactivos", "¿se puede superar una infidelidad?" |
| 18 | Enojo, ira y gritos | ●● | ● | Alto | "Por qué me enojo por todo" |

**Prioridad sugerida para los primeros 3 meses:** 1 (ansiedad), 2 (neurodivergencia adulta), 3–4 (apego y dinámicas de pareja), 6 (depresión y vacío) y 10 (serie "la psicología de…" como motor de alcance), más 15 (acceso a terapia) como pieza de conversión fija o como video ancla del canal.

---

## 9. Banco de títulos (basados en búsquedas reales)

**Ansiedad**
1. ¿Por qué siento que me falta el aire si no tengo nada? (ansiedad explicada)
2. Cómo dejar de pensar demasiado: lo que pasa en tu cerebro
3. ¿Ansiedad o estrés? La diferencia que casi nadie sabe
4. Por qué me siento nervioso sin razón
5. Qué hacer si alguien tiene un ataque de ansiedad frente a ti
6. Escenarios falsos: por qué tu mente imagina lo peor
7. ¿Cómo se siente la ansiedad? (y cómo saber si la tienes)

**Neurodivergencia**
8. Señales de TDAH en adultos (sobre todo en mujeres)
9. ¿Puedo ser autista y no saberlo? Rasgos de autismo en adultos
10. ¿Quién diagnostica el TDAH o el autismo en adultos en México?
11. TDA vs. TDAH: ¿es lo mismo?
12. Qué significa ser neurodivergente

**Pareja y apego**
13. ¿Qué tipo de apego tienes? (ansioso, evitativo, seguro)
14. Mi pareja me aplica la ley del hielo: qué significa y qué hacer
15. Mi pareja me culpa de todo
16. Cómo dejar de mendigar amor
17. Cómo dejar de idealizar a una persona
18. Apego ansioso + apego evitativo: por qué se atraen
19. Celos retroactivos: cuando te duele el pasado de tu pareja
20. ¿Se puede superar una infidelidad y seguir juntos?
21. Por qué peleo tanto con mi pareja
22. Las fases de una ruptura amorosa
23. Por qué no puedo olvidar a mi ex
24. ¿Narcisista o solo egoísta? Cómo distinguirlos
25. Vínculo traumático: por qué no puedes dejar a quien te lastima

**Depresión y emociones**
26. Por qué me siento vacío por dentro
27. Por qué no tengo ganas de hacer nada
28. Depresión funcional: estar mal aunque "todo funcione"
29. Cómo ayudar a alguien con depresión (y qué no decirle)
30. Por qué me siento triste sin razón
31. Por qué me enojo por todo
32. Por qué me siento culpable de todo

**Familia y crianza**
33. "Mi mamá no me quiere": cuando el amor duele
34. Cómo poner límites a tu mamá sin sentir culpa
35. Por qué algunas personas cortan el contacto con su familia
36. Mi hijo adolescente se aísla: ¿normal o señal de alerta?
37. Mi hijo adolescente me falta al respeto: qué hay detrás
38. Cómo dejar de gritarle a tus hijos
39. Berrinches: qué pasa en el cerebro de tu hijo

**Autoconocimiento y "la psicología de…"**
40. La psicología de las personas que prefieren estar solas
41. La psicología de las personas que se quedan calladas cuando están heridas
42. La psicología de las personas que te castigan con silencio
43. La psicología de las personas que piensan demasiado
44. La psicología de las personas que lloran con facilidad
45. La psicología de las personas que nunca piden ayuda
46. Por qué soy tan sensible
47. Introvertido vs. tímido: no es lo mismo
48. Cómo dejar de necesitar validación
49. Herida de abandono: cómo saber si la tienes

**Trabajo**
50. Señales de burnout (antes de que sea tarde)
51. Síndrome del impostor: por qué sientes que no mereces lo que logras
52. Mi jefe me hace sentir mal: ¿qué hago?

**Terapia (conversión)**
53. ¿Cuánto cuesta ir al psicólogo en México? (y opciones gratis)
54. ¿Psicólogo o psiquiatra? A quién ir según lo que sientes
55. ¿Terapeuta y psicólogo es lo mismo?
56. Qué pasa en tu primera sesión con un psicólogo
57. ¿La terapia en línea funciona?
58. Señales de que ya es momento de ir a terapia
59. Terapia cognitivo-conductual explicada con caricaturas
60. "Mi psicólogo dice…" (serie corta de frases de terapia)

---

## 10. Recomendaciones para el canal y para Agenda PSI

1. **Dos líneas de contenido:**
   - **Alcance:** serie fija "La psicología de las personas que…" (formato probado, preguntas que ya se buscan, ideal para el personaje). Más "señales de que…" y "por qué me siento…".
   - **Profundidad y conversión:** ansiedad, depresión, neurodivergencia adulta, apego y dinámicas de pareja, crianza adolescente. Todos son temas donde el siguiente paso natural es una evaluación o terapia.
2. **Títulos en primera persona, como los escribe la gente:** "Mi pareja me…", "Por qué me siento…", "Mi hijo adolescente…". Las frases exactas del §7 son títulos listos.
3. **Puente a terapia sin vender:** cerrar con "señales de que esto ya merece hablarlo con un profesional" y quitar barreras (precio, primera sesión, en línea, psicólogo vs. psiquiatra). En México se busca mucho "psicólogo **gratis**". Conviene reconocerlo con honestidad (DIF, IMSS, Línea de la Vida) y explicar qué aporta la terapia privada o en línea.
4. **Calendario:** preparar en diciembre los contenidos de febrero. Publicar piezas de autismo en marzo y abril, sobre el Día del Psicólogo en mayo, sobre salud mental en octubre y sobre soledad y duelo en diciembre. Reaccionar en 48–72 h a estrenos o virales con tema psicológico (el efecto *Intensamente 2*).
5. **Usar la palabra que busca la gente, no la técnica:** "ataque de ansiedad" (no "de pánico"), "sobrepensar", "ley del hielo", "migajear", "casi algo", "escenarios falsos". En títulos y descripciones, poner **ambas grafías** cuando haya tilde (psicólogo/psicologo) y no depender de la palabra suelta en temas con homónimos musicales.
6. **Cuidado y protocolo:** en el autocompletado aparecen búsquedas de riesgo (*se autolesiona*, *pensamientos suicidas*, *señales de que alguien se quiere suicidar*, *mi pareja me golpeó*). Todo video sobre depresión, violencia o autolesión debe incluir recursos de crisis en México (Línea de la Vida 800 911 2000, 911) y no dar diagnósticos.

---

## 11. Archivos de datos crudos

Carpeta: `/tmp/claude-0/-home-user-Creador-de-videos-Para-redes-/f6e80049-54f1-5e5b-b0dd-1d5ea884d7d2/scratchpad/research/trends/`

| Archivo | Contenido |
|---|---|
| `raw/bNN_{google,youtube}_{5y,12m}_iot.csv` | Series de interés por lote (ancla "psicólogo" + 4 términos) |
| `raw/bNN_{google,youtube}_12m_related.json` | Consultas relacionadas principales y en aumento |
| `raw/bNN_google_12m_region.csv` | Interés por estado dentro de cada lote |
| `raw_extra/xN_*` | Lotes de variantes sin acento y frases reales |
| `raw_extra/region_*.csv` | Interés por estado, un término por consulta |
| `interes_normalizado_largo.csv` | Todos los índices normalizados contra "psicólogo" + cambios anual, a 5 años y trimestral |
| `resumen_terminos.csv` | Tabla resumen (§3–4) |
| `estacionalidad_google.csv` | Índices mensuales (§5) |
| `consultas_relacionadas.csv` | ~2,100 consultas relacionadas consolidadas |
| `variantes_indices.csv` | Índices de variantes sin acento y frases reales (§3) |
| `estados_interes_por_termino.csv` · `estados_sobreindice.csv` | §6 |
| `autocomplete_raw.json` · `autocomplete_raw_ronda2.json` | Sugerencias crudas (Google y YouTube, raíz × letra) |
| `autocomplete_clasificado.csv` · `autocomplete_temas.json` | Sugerencias clasificadas por tema con puntuación |

Scripts: `/tmp/claude-0/-home-user-Creador-de-videos-Para-redes-/f6e80049-54f1-5e5b-b0dd-1d5ea884d7d2/scratchpad/scripts/` (`trends_collect.py`, `trends_extra.py`, `trends_analyze.py`, `region_analyze.py`, `suggest_collect.py`, `suggest_collect2.py`, `suggest_analyze.py`).
