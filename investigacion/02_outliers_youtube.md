# 02 · Outliers en YouTube: qué videos rompen la media en psicología y divulgación (nov-2026)

**Ronda 2, frente "outliers".** Fecha de corte de los datos: 18-nov-2026.
**Leyenda:** **[D]** = dato medido en los catálogos descargados · **[I]** = inferencia o interpretación mía · **[W]** = dato de una fuente web.

---

## 0. Resumen ejecutivo (lo accionable)

1. **[D] El formato que más outliers produce en 2026 es "La psicología de las personas que [rasgo cotidiano]".** En los últimos 12 meses, en español, está en el 7.7% de los videos largos y en el 14.8% del decil superior (lift 1.9). En inglés: 13% de los videos y 23% del decil superior (lift 1.7). En Shorts en inglés el lift es 4.0. **[D] En español ningún canal de la muestra lo usa en Shorts.** [I] Ese es el hueco más claro.
2. **[D] Es un formato de lotería.** Su mediana es baja (en es: 600–2,000 vistas por video en la mayoría de los meses de 2026), pero su cola es enorme (p90 = 14× la mediana local).
   - De 12 canales nuevos en español (creados entre nov-2025 y ago-2026), **8 tuvieron 1 o 2 meses virales y luego se desplomaron** a cientos o pocos miles de vistas por video. IdealMente cayó y luego rebotó, y otros 2 acaban de tener su primer viral en oct-2026.
   - [D] El único que sostiene tracción mes a mes es **La Psicología Invisible (LPI)**: 81 videos, 22.5M de vistas, mediana de 38K, 13 videos con más de 500K.
3. **Temas ganadores (lift en el decil superior, español, últimos 12 meses):**
   - [D] **Inteligencia** (lift 2.1): "bajo IQ", "inteligencia mecánica", "inteligencia emocional".
   - [D] **Rasgos cotidianos e identidad** (1.7): cumpleaños, casa limpia, guardar cosas, no publicar fotos, estar solo en casa.
   - [D] **Social y autopercepción** (1.6): "le caes mal", "molestas sin darte cuenta", "te envidian".
   - [D] **Compendios** "Todas las X explicadas en N minutos" (lift 3.7, n=43 en es).
   - [D] **Tests** (2.2).
4. **[D] Temas saturados o a la baja en español.** Los que dominaron 2023–2024 ahora rinden por debajo de la media:
   - **narcisismo y relaciones tóxicas:** eran el 26.5% de los videos hace 2–3 años y hoy son el 3–4%, con lift 0.6.
   - **apego:** lift 0.6.
   - **familia e infancia:** lift 0.5.
   - **autoayuda directa:** lift 0.4. Los "Psicología del Liderazgo/Carisma/Autoestima" de LPI de nov-2026 se quedan en 5–38K, contra su mediana de 38K.
   - [I] Ojo: siguen funcionando para psicólogos con cara y en Shorts (apego evitativo, celos, amor propio).
5. **[D] Los outliers en español suelen ser traducciones de outliers en inglés, con 1 a 3 meses de retraso.**
   - Ejemplos: cumpleaños, Xennials/Gen X, no ver deportes, no publicar fotos, "inteligencia mecánica" y disciplina.
   - "Inteligencia mecánica" salió en PsychToons el 21-oct y ClaridadMental lo tradujo literal el 23-oct: 781K vistas con 3,160 suscriptores.
   - [D] Copiar un tema ya viral **no garantiza nada**: el mismo título ("La PSICOLOGÍA de las personas INFIELES") hizo 18K, 46K y 698K según el canal.
6. **[D] Patrón visual de las miniaturas ganadoras.**
   - **Un solo personaje**, simple y sin rasgos (un monito de palo, una figura en forma de frijol o una silueta), en una escena cotidiana reconocible.
   - **2 a 5 palabras** en mayúsculas condensadas, negro sobre **amarillo** o blanco sobre **rojo**.
   - Una **flecha roja** que señala el objeto clave y fondo claro o neutro.
   - El texto de la miniatura **no repite el título**: lo resume en el gancho ("NO CELEBRAN SU CUMPLEAÑOS", "ARREGLA TODO", "PREFIERO ESTAR SOLO").
7. **[D] Duración.** Los outliers largos se concentran entre 8 y 10 minutos: mediana de 9:10 en el top-50 en español y 9:19 en el top-30 en inglés. LPI publica casi todo entre 8 y 9.5 minutos.

---

## 1. Método y muestra

**Muestra [D]**
- **39 canales:** 31 en español y 8 de referencia en inglés.
- **18,089 videos:** 14,571 largos y 3,518 Shorts.
- Se descargaron con `yt-dlp --flat-playlist` (pestañas /videos y /shorts por separado) el 18-nov-2026.

**Selección de canales**
- Sembrada con 18 búsquedas en YouTube en español: "psicología de las personas que", "señales psicológicas", "apego ansioso", "narcisista señales", "psicología oscura", "trauma infancia", "relación tóxica", etc.
- Más 6 búsquedas en inglés y 4 de Shorts en español.
- Se eligieron los canales más recurrentes en los resultados, en tres tipos:
  - **faceless o animados**, los más parecidos al proyecto;
  - **psicólogos con cara**, como comparación;
  - **2 canales generalistas** con contenido de psicología: Te lo Pinto y CuriosaMente. De ellos solo se rankean los videos con tema psicológico.

**Métricas**
- **Outlier score** = vistas ÷ mediana de vistas del canal en ese formato (largo o Short por separado).
- **Score local** = vistas ÷ mediana de los 10 videos anteriores y los 10 posteriores del mismo canal. Corrige que el canal crezca o decaiga con el tiempo. Lo uso para las tablas de *lift*.
- **Lift de un tema** = su peso en el decil superior de score local ÷ su peso en todos los videos. Más de 1 significa que aparece más entre los outliers de lo que pesa en la producción.

**Filtros de los rankings**
- Canal con 20 o más videos en ese formato.
- Video con 14 días o más de antigüedad.
- Vistas mínimas: 100K en español y 500K en inglés.
- Se excluyen los videos largos de Mentes Expertas porque son clips y muchos no tratan de psicología.

**Codificación de temas y plantillas**
- Automática por expresiones regulares sobre el título, en `videos_all.csv`.
- Manual para los top-50 en español y top-30 en inglés, en `outliers_coded.csv`.

**Limitaciones (importantes)**
- **Fechas aproximadas.** El modo de catálogo da fechas relativas ("hace 3 meses"):
  - Resolución mensual para los videos de menos de 12 meses.
  - Para los mayores solo sé el año, y todo lo que tiene 12–23 meses cae en "≥2025".
  - Para una parte de los outliers obtuve la fecha exacta con una consulta individual (columna `upload_date_exact`). YouTube bloqueó parte de esas consultas ("confirm you're not a bot"), así que no están todas.
- **Las vistas del catálogo están redondeadas** (p. ej. 3.6M).
- **Sesgo de selección.** Descubrí los canales por búsqueda, y la búsqueda favorece a los que ya tienen algún éxito. Los canales nuevos que nunca pegaron casi no están en la muestra. La tasa real de "fracaso total" es **mayor** que la que se ve aquí.
- **El clasificador de temas deja ~33% de los títulos en "otro".** Los lifts son orientativos. Las conclusiones fuertes se apoyan en la codificación manual de los top.
- **Shorts sin fecha.** El catálogo de Shorts no trae fecha, así que no hay serie temporal de Shorts.
- **Faltan canales.** Psych2Go Español (@Psych2GoEspanol) no existe con ese handle. El canal real es "Psych2Go Español - Psicología Para Llevar" y sí está incluido. La mayoría de los canales faceless en español **no tiene pestaña de Shorts**.
- **Títulos auto-traducidos.** Con el idioma por defecto (inglés), YouTube muestra los títulos en español traducidos automáticamente al inglés. Todos los catálogos en español se bajaron con `lang=es`.

---

## 2. Panorama por canal (videos largos salvo que se indique)

| Canal | Tipo | n | Mediana | p90 | Máx. | Top-10 = % de vistas | ≥10× mediana | Desde |
|---|---|---|---|---|---|---|---|---|
| La Psicología Invisible | faceless-animado | 81 | 38K | 708K | 3.6M | 66% | 16 | feb-2026 |
| Psych2Go Español | faceless-animado | 559 | 34K | 482K | 6.8M | 27% | 73 | ≤2021 |
| Psych2Go Español (Shorts) | — | 408 | 12K | 41K | 563K | 28% | 8 | — |
| Psicología Animada | faceless-animado | 624 | 7K | 114K | 2.6M | 32% | 95 | ≤2020 |
| Sapiencia Práctica | faceless | 467 | 42K | 753K | 8.3M | 29% | 76 | ≤2021 |
| Sprouts Español | faceless-animado | 83 | 127K | 1.4M | 6.0M | 69% | 10 | ≤2020 |
| La Mente Oculta | faceless | 21 | 721 | 22K | 2.3M | 99.8% | 5 | abr-2026 |
| Psicología Clara | faceless | 80 | 268 | 1.3K | 388K | 96% | 5 | mar-2026 |
| Psicología Sin Filtro | faceless | 47 | 1.5K | 18K | 689K | 96% | 7 | may-2026 |
| LoDescomún | faceless | 38 | 4.3K | 62K | 1.0M | 96% | 7 | ene-2026 |
| El Consejero | faceless (filosofía/Jung) | 576 | 10K | 118K | 1.8M | 35% | 66 | ≤2024 |
| IdealMente | faceless | 127 | 1.3K | 56K | 693K | 85% | 24 | feb-2026 |
| Te lo Pinto (generalista) | faceless-animado | 201 | 321K | 1.6M | 5.2M | 25% | 3 | ≤2024 |
| DatoVisual | faceless-animado | 51 | 5.1K | 154K | 1.0M | 91% | 10 | ~nov-2025 |
| Psicótico | faceless | 427 | 14K | 63K | 1.0M | 37% | 22 | ≤2025 |
| Escéptico | faceless | 348 | 3K | 20K | 448K | 42% | 31 | ≤2025 |
| CuriosaMente (generalista) | animado-edu | 653 | 455K | 1.7M | 8.9M | 12% | 12 | 2015 |
| MenteConsciente | faceless | 23 | 1.7K | 14K | 573K | 99% | 3 | ene-2026 |
| Claridad Mental | faceless | 43 | 204 | 2.6K | 781K | 99% | 6 | ago-2026 |
| Manual de Vida | faceless | 93 | 133 | 2.9K | 424K | 95% | 16 | ≤nov-2025 |
| Psicología Oscura | faceless | 103 | 2.5K | 24K | 594K | 82% | 11 | ≤nov-2025 |
| Psicología Cotidiana | faceless | 149 | 333 | 1.7K | 982K | 97% | 9 | jun-2026 |
| Doctora Flórez | psicóloga con cara | 115 | 45K | 251K | 1.5M | 43% | 5 | ≤2024 |
| Doctora Flórez (Shorts) | — | 387 | 7.4K | 32K | 839K | 39% | 19 | — |
| Hablemos con la vida | psicólogo con cara | 62 | 110K | 523K | 883K | 52% | 0 | ≤2023 |
| Chris Núñez | psicólogo con cara | 108 | 15K | 252K | 4.6M | 76% | 15 | ≤2018 |
| Lluís Rodríguez | psicólogo con cara | 539 | 12K | 61K | 520K | 20% | 22 | ≤2021 |
| Lluís Rodríguez (Shorts) | — | 313 | 4.6K | 17K | 209K | 32% | 7 | — |
| Omar Rueda | psicólogo con cara | 406 | 56K | 343K | 2.4M | 22% | 20 | ≤2017 |
| Natalia Gurdián | psicóloga con cara | 217 | 6.2K | 41K | 446K | 41% | 13 | ≤2016 |
| Gemma Albarracín | psicóloga con cara | 1266 | 9K | 52K | 585K | 13% | 67 | ≤2022 |
| Carla Kuhn | psicóloga con cara | 704 | 3.6K | 25K | 255K | 18% | 47 | ≤2018 |
| Carla Kuhn (Shorts) | — | 304 | 4.6K | 14K | 737K | 49% | 16 | — |
| Ale Álvarez Psi (Shorts) | psicóloga con cara | 799 | 60K | 203K | 2.2M | 17% | 17 | — |
| Mentes Expertas (Shorts) | clips de expertos | 200 | 3.8K | 29K | 365K | 50% | 15 | — |
| **Psych2Go (en)** | faceless-animado | 3453 | 190K | 1.5M | 18M | 7% | 269 | 2014 |
| Psych2Go (en, Shorts) | — | 497 | 68K | 264K | 2.4M | 23% | 22 | — |
| **Sprouts (en)** | faceless-animado | 193 | 174K | 1.7M | 19M | 50% | 20 | 2014 |
| **The School of Life (en)** | faceless-animado | 1081 | 431K | 2.2M | 14M | 10% | 29 | 2013 |
| **Psychology Simplified (en)** | faceless | 151 | 13K | 270K | 3.5M | 71% | 27 | dic-2025 |
| **Revers Hub (en)** | faceless-animado | 68 | 5.9K | 238K | 3.3M | 90% | 16 | ≤nov-2025 |
| Revers Hub (en, Shorts) | — | 39 | 22K | 1.5M | 4.9M | 96% | 9 | — |
| **PsychToons (en)** | faceless-animado | 148 | 6.2K | 352K | 5.3M | 77% | 35 | ene-2026 |
| **Psychology Insight (en)** | faceless | 74 | 3.2K | 61K | 3.1M | 95% | 10 | mar-2026 |
| **Apex Psychology (en)** | faceless | 122 | 17K | 188K | 2.8M | 69% | 15 | feb-2026 |

La tabla completa, con todos los formatos, está en `channels_summary.csv`.

**Lectura [D]**
- **Concentración extrema en los canales nuevos.** En los canales faceless creados en 2026, sus 10 mejores videos suman entre el 85% y el 99.8% de todas sus vistas. En los canales establecidos ese número baja al 7–35% (Psych2Go, School of Life, Gemma Albarracín, Lluís Rodríguez).
- **Vistas desligadas de los suscriptores** (consulta individual):
  - Claridad Mental: 781K vistas con **3,160** suscriptores.
  - Manual de Vida: 424K con **2,520**.
  - Psicología Clara: 388K con **4,650**.
  - Psicología Cotidiana: 983K con **12,300**.
  - La Mente Oculta: 2.4M con **28,700**.
  - [I] Estos videos explotan por *browse/suggested*, no por los suscriptores. Un canal nuevo puede pegar desde el día 1 si el tema y la miniatura son correctos, pero eso no le garantiza audiencia recurrente.

---

## 3. Top outliers

Las tablas completas, con URL y más columnas, están en `outliers_coded.csv`.

> "Score" = vistas ÷ mediana del canal. En canales diminutos (mediana de 100 a 300 vistas) el score se dispara. Por eso conviene leerlo junto a las vistas absolutas y al score local.
>
> **Fecha:** `AAAA-MM-DD` es exacta; `~AAAA-MM` es aproximada al mes; `≥2025` significa "hace 12–23 meses"; `~AAAA` es aproximada al año.

<!-- TABLAS_INICIO -->

### Top-50 outliers · español · videos largos

| # | Canal | Score (×mediana) | Score local | Vistas | Fecha | Dur. | Tema | Plantilla | Título |
|---|---|---|---|---|---|---|---|---|---|
| 1 | ClaridadMental | 3828 | 1761 | 781K | 2026-10-23 | 14:53 | rasgos/inteligencia | Psicología de [rasgo] (Por qué algunas personas…) | [Psicología de la Inteligencia Mecánica (Por Qué Algunas Personas Pueden Arreglar CUALQUIER](https://www.youtube.com/watch?v=VJ1E2xp0bdg) |
| 2 | LaMenteOculta | 3190 | 1278 | 2.3M | 2026-04-17 | 8:36 | rasgos cotidianos | La psicología de las personas que [hábito] | [La Psicología de las Personas que Guardan Objetos "Por Si Algún Día Sirven"](https://www.youtube.com/watch?v=3d0msMp2gTY) |
| 3 | ManualDeVida | 3188 | 314 | 424K | 2026-10-24 | 10:34 | rasgos cotidianos | La psicología de las personas que [hábito] (Y por qué molestan) | [La Psicología de las Personas que Prefieren una Vida Simple (Y Por Qué Molestan)](https://www.youtube.com/watch?v=f5mPz3luBDQ) |
| 4 | PsicologiaCotidiana | 2949 | 1358 | 982K | 2026-06-18 | 12:21 | trastornos (detección) | COMPORTAMIENTOS extraños que son señales de [X] | [COMPORTAMIENTOS Extraños Que Son Señales de Enfermedad Mental](https://www.youtube.com/watch?v=1QLCErNsLo4) |
| 5 | PsicologiaCotidiana | 2393 | 3399 | 797K | ~2026-08 | 8:29 | rasgos cotidianos (sueño) | La PSICOLOGÍA de las personas que [hábito] | [La PSICOLOGÍA de las personas que ABRAZAN la almohada para poder dormir](https://www.youtube.com/watch?v=t0a2EC_rb2c) |
| 6 | PsicologiaClara | 1448 | 809 | 388K | 2026-03-23 | 7:04 | relaciones/rasgo | La psicología de las personas que [conducta] | [La Psicología de las Personas que Cortan a Todos de Su Vida](https://www.youtube.com/watch?v=ugMSSFqjFKo) |
| 7 | IdealMente | 533 | 295 | 693K | 2026-03-05 | 5:46 | amor/atracción | N señales psicológicas de que le gustas (la ciencia no miente) | [5 Señales Psicológicas de que le gustas (La ciencia no miente)](https://www.youtube.com/watch?v=h-5KtD1HUwg) |
| 8 | IdealMente | 494 | 195 | 642K | 2026-10-20 | 9:23 | social/autopercepción | N señales de que [defecto] sin darte cuenta (la psicología lo explica) | [7 Señales de que Molestas a los Demás sin Darte Cuenta (la psicología lo explica)](https://www.youtube.com/watch?v=p6qZ53yusV4) |
| 9 | PsicologiaSinFiltro | 459 | 53 | 689K | 2026-05-06 | 7:30 | rasgos cotidianos (redes) | La PSICOLOGÍA de las personas que NO [hábito] | [La PSICOLOGÍA de las Personas que NO Publican FOTOS en Redes Sociales](https://www.youtube.com/watch?v=m90JpoHRN2c) |
| 10 | IdealMente | 442 | 805 | 575K | 2026-02-10 | 7:52 | inteligencia | N señales de [bajo IQ] (lo que nadie te dice) | [7 Señales de un Bajo IQ (Lo que nadie te dice sobre la inteligencia)](https://www.youtube.com/watch?v=vYwZ6acM8RY) |
| 11 | PsicologiaClara | 381 | 116 | 102K | 2026-03-15 | 9:49 | rasgos cotidianos | Si [no te gusta X], tu cerebro es diferente | [Si el deporte no te interesa, tu cerebro es diferente](https://www.youtube.com/watch?v=Lj9DJ-mrLMc) |
| 12 | PsicologiaCotidiana | 375 | 196 | 125K | 2026-07-12 | 13:53 | inteligencia emocional | ¿Tienes ESTAS actitudes? Señales de [X] | [¿Tienes ESTAS Actitudes? Señales de Baja Inteligencia Emocional](https://www.youtube.com/watch?v=U_uTow44Sng) |
| 13 | PsicologiaAnimada | 369 | 19 | 2.6M | 2021-11-22 | 12:36 | trastornos (ansiedad) | TODOS LOS [síntomas de X] EXPLICADOS | [TODOS LOS SÍNTOMAS DE LA ANSIEDAD EXPLICADOS (FÍSICOS Y PSICOLÓGICOS)](https://www.youtube.com/watch?v=x44EQym4Xpo) |
| 14 | IdealMente | 367 | 222 | 477K | 2026-03-19 | 5:28 | social | N señales psicológicas de que le CAES MAL a alguien | [5 Señales psicológicas de que le CAES MAL a alguien](https://www.youtube.com/watch?v=AT3idzyDZBk) |
| 15 | MenteConsciente | 337 | 395 | 573K | 2026-01-09 | 6:44 | rasgos cotidianos | La psicología de las personas que [gusto] | [La Psicología de las Personas que Aman las Plantas](https://www.youtube.com/watch?v=4ieVLDarwkU) |
| 16 | ChrisNunez | 307 | 37 | 4.6M | 2019-04-22 | 11:10 | trastornos/autoayuda práctica | ¿Cómo combatir [X]? (N pasos) | [¿Cómo Combatir los PENSAMIENTOS de Ansiedad y Depresión? (siguiendo 4 pasos)](https://www.youtube.com/watch?v=1eZepcg6aC0) |
| 17 | PsicologiaSinFiltro | 291 | 34 | 436K | 2026-05-10 | 10:35 | rasgos (introversión) | La PSICOLOGÍA de las personas que prefieren estar SOLAS | [La PSICOLOGÍA de las Personas que Prefieren Estar SOLAS en Casa](https://www.youtube.com/watch?v=Gp23baTElI8) |
| 18 | IdealMente | 245 | 120 | 318K | ~2026-04 | 5:04 | social | N señales de que te envidian | [5 Señales Psicológicas de que te Envidian (Cómo detectarlas)](https://www.youtube.com/watch?v=57qC7VapuEE) |
| 19 | PsicologiaOscura | 238 | 186 | 594K | ~2026-02 | 12:08 | test/psicología oscura | N preguntas revelan tu [lado oscuro] | [3 Preguntas Revelan Tu Lado Más Oscuro](https://www.youtube.com/watch?v=j91tShUD4LE) |
| 20 | LoDescomun | 235 | 91 | 1.0M | ~2026-01 | 8:12 | rasgos cotidianos | Psicología de personas que NO [hábito] (y no es casualidad) | [Psicología de personas que NO toman cerveza (y no es casualidad)](https://www.youtube.com/watch?v=cj8aMvG9Ta8) |
| 21 | PsicologiaAnimada | 213 | 94 | 1.5M | ~2021 | 4:53 | trastornos (depresión) | N síntomas de [depresión oculta] | [11 Síntomas de que alguien tiene DEPRESIÓN OCULTA O ENCUBIERTA (tal vez la tienes y no lo ](https://www.youtube.com/watch?v=pRvLmNmrBZU) |
| 22 | IdealMente | 212 | 172 | 275K | ~2026-03 | 6:16 | amor/apego | Psicología de las personas que se ILUSIONAN rápido | [Psicología de las personas que se ILUSIONAN demasiado rápido (La OBSESIÓN Temprana)](https://www.youtube.com/watch?v=3CmQ1ASRksc) |
| 23 | Psych2GoES | 200 | 11 | 6.8M | ~2021 | 4:07 | amor | N señales de que nunca estuviste enamorado | [6 Señales de que Nunca Estuviste Realmente Enamorado / Psych2Go](https://www.youtube.com/watch?v=Nsr0RICFRdI) |
| 24 | PsicologiaOscura | 198 | 106 | 495K | ~2026-01 | 9:07 | test | "Si respondiste esto en N segundos, no eres normal" | ["Si Respondiste Esto en 5 Segundos, No Eres Normal" (Test Psicológico)](https://www.youtube.com/watch?v=acW9TubOOh8) |
| 25 | SapienciaPractica | 198 | 14 | 8.3M | ~2021 | 4:53 | trastornos (TDAH) | N señales de que es [X], y NO [Y] | [5 señales de que es TDAH, y NO PEREZA](https://www.youtube.com/watch?v=YRYT6uLemks) |
| 26 | DatoVisual | 196 | 187 | 1.0M | ~2026-01 | 22:54 | trastornos (neurodivergencia) | Todas las [X] explicadas en N minutos | [Todas las NEURODIVERGENCIAS explicadas en 22 minutos](https://www.youtube.com/watch?v=qnXpozwra-s) |
| 27 | LoDescomun | 183 | 52 | 779K | ~2026-01 | 7:31 | rasgos (introversión) | Psicología de personas que NO disfrutan [X] | [Psicología de personas que NO disfrutan las fiestas y discotecas](https://www.youtube.com/watch?v=AJDxqq1lybQ) |
| 28 | ElConsejero | 180 | 150 | 1.8M | ≥2025 | 23:18 | filosofía/pseudo | [Afirmación] – [autor clásico] | [La Casualidad No Existe, Aquí Está la Prueba – Maquiavelo](https://www.youtube.com/watch?v=HGCWhAE37SA) |
| 29 | ElConsejero | 170 | 46 | 1.7M | ≥2025 | 15:20 | filosofía/autoayuda | [Consejo] – La filosofía de [autor] | [Cuando dejas de preocuparte, los resultados llegan – La filosofía de Michel de Montaigne](https://www.youtube.com/watch?v=qtQiNBBI3ME) |
| 30 | ChrisNunez | 160 | 16 | 2.4M | ~2019 | 10:29 | emociones/autoayuda práctica | Cómo dejar de [X] (técnica de N pasos) | [Cómo dejar de tener MIEDO (con una técnica de 5 pasos)](https://www.youtube.com/watch?v=sh5jXOx2tkw) |
| 31 | SapienciaPractica | 160 | 11 | 6.7M | ~2022 | 5:24 | relaciones tóxicas | [Trastorno]: N frases habituales | [Trastorno de la Personalidad Narcisista (TPN): 10 frases habituales](https://www.youtube.com/watch?v=BH-cK0OabnE) |
| 32 | Esceptico | 152 | 33 | 448K | ≥2025 | 26:44 | adicciones/Jung | La psicología de [X] – Carl Jung | [La psicología de un adicto – Carl Jung](https://www.youtube.com/watch?v=R5dJIAijUuY) |
| 33 | PsicologiaAnimada | 142 | 104 | 1.0M | ~2024 | 5:50 | trastornos (autismo) | [X] vs [Y] ¿Qué diferencia hay? | [AUTISMO vs ASPERGER (Autismo Grado 1) ¿Qué diferencia hay?](https://www.youtube.com/watch?v=ABmcYIKHnRc) |
| 34 | PsicologiaAnimada | 142 | 7 | 1.0M | ~2022 | 8:57 | relaciones tóxicas | N señales de que tu PAREJA es [X] | [20 señales de que tu PAREJA es un NARCISISTA SEXUAL](https://www.youtube.com/watch?v=RKr9xQ6VobM) |
| 35 | ElConsejero | 140 | 44 | 1.4M | ≥2025 | 20:07 | filosofía/autoayuda | [Frase inspiracional] | [La vida comienza cuando te encuentras a ti mismo](https://www.youtube.com/watch?v=FkxdbPjslMY) |
| 36 | ElConsejero | 140 | 26 | 1.4M | ~2024 | 20:44 | autoayuda/reencuadre | No eres [X], solo estás [Y] | [No eres perezoso, solo estás perdido](https://www.youtube.com/watch?v=7IIawiXqLsU) |
| 37 | IdealMente | 130 | 12 | 169K | ~2026-11 | 9:13 | social | N cosas que te hacen [defecto] sin que te des cuenta | [7 cosas que te hacen socialmente torpe sin que te des cuenta](https://www.youtube.com/watch?v=2i5Ct63Byko) |
| 38 | IdealMente | 120 | 66 | 156K | ~2026-03 | 4:49 | atracción | N señales de que eres ATRACTIVO (y no lo sabes) | [5 Señales Psicológicas de que eres ATRACTIVO (y no lo sabes)](https://www.youtube.com/watch?v=AL5ic-GqR8g) |
| 39 | IdealMente | 112 | 48 | 145K | ~2026-10 | 8:45 | atracción/personalidad | N señales de que tienes una personalidad ATRACTIVA (y nadie te lo ha dicho) | [7 Señales de que Tienes una Personalidad ATRACTIVA (y Nadie te lo Ha Dicho)](https://www.youtube.com/watch?v=mcWrD7y39yI) |
| 40 | ElConsejero | 110 | 110 | 1.1M | ≥2025 | 21:18 | amor/espiritualidad | Por qué el universo te envía a alguien… | Psicología de Carl Jung | [Por Qué el Universo Te Envía a Alguien Con Quien No Puedes Estar / Psicología de Carl Jung](https://www.youtube.com/watch?v=4DTEnSx5V2c) |
| 41 | ElConsejero | 110 | 20 | 1.1M | ≥2025 | 24:05 | autoconocimiento | La psicología de [X] | [La psicología de conocerse a uno mismo](https://www.youtube.com/watch?v=DjQhIGol33M) |
| 42 | PsicologiaAnimada | 107 | 26 | 756K | ~2021 | 16:26 | relaciones tóxicas | N preguntas para saber si tu pareja es [X] | [50 Preguntas para saber si tu pareja es NARCISISTA: Descubre si vives con uno](https://www.youtube.com/watch?v=zSXROx1o63Y) |
| 43 | SapienciaPractica | 107 | 12 | 4.5M | ~2023 | 6:58 | trauma | N señales de que arrastras HERIDAS EMOCIONALES | [7 señales de que arrastras HERIDAS EMOCIONALES](https://www.youtube.com/watch?v=i4JRa3Cmf_s) |
| 44 | DatoVisual | 101 | 64 | 514K | ~2025-12 | 18:27 | trastornos (fobias) | Todas las [X] explicadas en N minutos | [Todas las FOBIAS explicadas en 18 minutos](https://www.youtube.com/watch?v=z3t2n-YKqPU) |
| 45 | SapienciaPractica | 100 | 37 | 4.2M | ~2023 | 6:11 | trastornos (burnout) | N señales de que NO es [X], sino [Y] | [6 señales de que NO es PEREZA, sino BURNOUT](https://www.youtube.com/watch?v=k1TwwjL6ZXk) |
| 46 | ElConsejero | 96 | 31 | 957K | ≥2025 | 26:09 | social/lenguaje | ¿Por qué [hábito] – y qué dice eso sobre ti? | [¿Por qué hablas como hablas – y qué dice eso sobre ti?](https://www.youtube.com/watch?v=wquD47mWOIs) |
| 47 | LaPsicologiaInvisible | 95 | 31 | 3.6M | ~2026-04 | 8:32 | rasgos cotidianos | La psicología de las personas a las que no les importa [X] | [La Psicología de las Personas a las que No les Importa su Cumpleaños](https://www.youtube.com/watch?v=LvwkpWE1lzg) |
| 48 | LoDescomun | 95 | 10 | 402K | ~2026-01 | 7:15 | rasgos cotidianos (redes) | ¿Por qué algunas personas [hábito]? (Psicología) | [¿Por qué algunas personas no publican sus fotos? (Psicología)](https://www.youtube.com/watch?v=xEbdGaYO5MY) |
| 49 | DatoVisual | 95 | 68 | 482K | ~2026-03 | 15:25 | trastornos (personalidad) | Cada [X] explicado en N minutos | [Cada TRASTORNO de la PERSONALIDAD explicado en 15 minutos.](https://www.youtube.com/watch?v=sYrx3AGQcX4) |
| 50 | Psych2GoES | 94 | 11 | 3.2M | ~2022 | 9:41 | emociones (depresión oculta) | N señales de que NO "estoy bien" | [7 Señales de que NO "Estoy Bien" / Psych2Go](https://www.youtube.com/watch?v=_AdKwR8LYWo) |

### Top-30 outliers · inglés · videos largos (referencia)

| # | Canal | Score (×mediana) | Score local | Vistas | Fecha | Dur. | Tema | Plantilla | Título |
|---|---|---|---|---|---|---|---|---|---|
| 1 | PsychologyInsight | 969 | 221 | 3.1M | ~2026-03 | 5:56 | inteligencia | Psychology of People With [rasgo] | [Psychology of People With Extremely High IQ](https://www.youtube.com/watch?v=DHEDiXy7B-Q) |
| 2 | PsychToons | 855 | 530 | 5.3M | ~2026-08 | 14:45 | autoayuda (virtud) | Psychology of [virtud] (And How to [truco]) | [Psychology of Discipline (And How to Trick Your Brain Into Craving It)](https://www.youtube.com/watch?v=CkP_8bkjf1E) |
| 3 | PsychToons | 581 | 18 | 3.6M | ~2026-08 | 13:38 | inteligencia/rasgos | Psychology of [rasgo]: Why [X] Is an Unfair Advantage | [Psychology of Polymaths: Why Having Multiple Interests Is an Unfair Advantage](https://www.youtube.com/watch?v=D0SGbomVuKc) |
| 4 | PsychToons | 565 | 41 | 3.5M | ~2026-09 | 15:04 | inteligencia/autoayuda | Psychology of [X]: [promesa hiperbólica] So Fast It's Almost Unfair | [Psychology of Intelligence: Learn Anything So Fast It's Almost Unfair](https://www.youtube.com/watch?v=f1gkkzHZxNg) |
| 5 | ReversHub | 564 | 418 | 3.3M | ≥2025 | 3:22 | rasgos cotidianos | Psychology of People Who [hábito] | [Psychology of People Who Treat Their Birthday Like a Normal Day](https://www.youtube.com/watch?v=ThIYhNHSQ1I) |
| 6 | PsychToons | 371 | 575 | 2.3M | ~2026-03 | 10:27 | emociones/rasgo | Psychology of People Who [reacción emocional] | [Psychology of People Who Go Quiet When They’re Hurt](https://www.youtube.com/watch?v=N95Tb2sDWVs) |
| 7 | PsychologyInsight | 344 | 117 | 1.1M | ~2026-04 | 6:21 | rasgos cotidianos | People Who [rasgo] | Psychology explained | [People Who Think Too Much / Psychology explain ](https://www.youtube.com/watch?v=La3WDl3WqjQ) |
| 8 | PsychToons | 323 | 31 | 2.0M | ~2026-10 | 13:45 | inteligencia/autoayuda | Psychology of [tipo de inteligencia]: How To… | [Psychology of Verbal Intelligence: How To Articulate Your Thoughts Intelligently](https://www.youtube.com/watch?v=6wPcR6MrsIk) |
| 9 | PsychologyInsight | 312 | 95 | 1.0M | ~2026-04 | 6:13 | inteligencia/trauma | N Signs You Have [inteligencia rara] | [10 Signs You Have Traumatic Intelligence The Rarest Form of Smart / Psychology explain](https://www.youtube.com/watch?v=irA2_BrdKVs) |
| 10 | PsychologySimplified | 269 | 24 | 3.5M | ~2026-02 | 8:11 | generaciones | Psychology of [generación] | [Psychology of Gen X](https://www.youtube.com/watch?v=G5YmIqYSqA0) |
| 11 | PsychToons | 258 | 31 | 1.6M | ~2026-10 | 15:31 | inteligencia/rasgos | Psychology of [tipo de inteligencia] (Why Some People…) | [Psychology of Mechanical Intelligence (Why Some People Can Fix Anything)](https://www.youtube.com/watch?v=AACwyjlk8ko) |
| 12 | PsychToons | 258 | 16 | 1.6M | ~2026-08 | 18:56 | autoayuda (virtud) | Psychology of [virtud]: Build a Mind So Strong It Scares People | [Psychology of Resilience: Build a Mind So Strong It Scares People](https://www.youtube.com/watch?v=TRd1kuUGazE) |
| 13 | ReversHub | 239 | 140 | 1.4M | ~2025-12 | 5:31 | generaciones | Psychology of People Who Grew Up in the [década] | [Psychology of People Who Grew Up in the 1970s](https://www.youtube.com/watch?v=Sbi0UNdCxB4) |
| 14 | PsychologySimplified | 238 | 35 | 3.1M | ~2026-01 | 3:20 | rasgos (introversión) | The Psychology of People Who Love [hábito] | [The Psychology of People Who Love Staying At Home](https://www.youtube.com/watch?v=2GZi3RM6QVg) |
| 15 | PsychologySimplified | 231 | 24 | 3.0M | ~2026-01 | 8:02 | rasgos cotidianos | Psychology of People Who Don't [hábito] | [Psychology of People Who Don't Obsess Over Sports](https://www.youtube.com/watch?v=O2Fb-SJ9v0M) |
| 16 | ApexPsychology | 165 | 455 | 2.8M | ~2026-04 | 16:08 | rasgos (hiperconciencia) | The Psychology of People Who Are Too [rasgo] | [The Psychology of People Who Are Too Aware](https://www.youtube.com/watch?v=7jBy6_KSCXg) |
| 17 | PsychToons | 161 | 14 | 1.0M | ~2026-08 | 11:42 | rasgos (soledad) | Why Some People Are Meant to [X] (Psychology Explains) | [Why Some People Are Meant to Walk Alone (Psychology Explains)](https://www.youtube.com/watch?v=POqCOvbJFbE) |
| 18 | PsychologySimplified | 154 | 24 | 2.0M | ~2026-02 | 8:02 | generaciones | Psychology of [generación] (años) | [Psychology of Xennials (1976 - 1985)](https://www.youtube.com/watch?v=Pqs0PokPDqo) |
| 19 | PsychToons | 143 | 11 | 888K | ~2026-09 | 16:58 | autoayuda (adicción) | Psychology of [problema] (And How to Beat It Without [X]) | [Psychology of Addiction (And How to Beat It Without Willpower)](https://www.youtube.com/watch?v=opyoqoddtBc) |
| 20 | PsychToons | 139 | 8 | 860K | ~2026-09 | 14:55 | autoayuda (virtud) | Psychology of [virtud]: Be So [X] It Makes People Nervous | [Psychology of Composure: Be So Calm It Makes People Nervous](https://www.youtube.com/watch?v=wq8TrxPYN7A) |
| 21 | PsychToons | 133 | 7 | 826K | ~2026-09 | 14:56 | autoayuda (virtud) | Psychology of [virtud]: [X] So Well It Makes You Dangerous | [Psychology of Rest: Recover So Well It Makes You Dangerous](https://www.youtube.com/watch?v=CwhUi9A8LeE) |
| 22 | PsychToons | 133 | 11 | 824K | ~2026-09 | 15:22 | autoayuda (social) | Psychology of [virtud]: How To Actually… | [Psychology of Charisma: How To Actually Make People Like You](https://www.youtube.com/watch?v=uw61C_qbgNg) |
| 23 | PsychToons | 118 | 11 | 732K | ~2026-10 | 15:44 | autoayuda | The Psychology of Not Giving A F*ck | [The Psychology of Not Giving A F*ck](https://www.youtube.com/watch?v=1dzUVXPj4yE) |
| 24 | Sprouts | 109 | 28 | 19.0M | ~2019 | 4:47 | concepto/efecto | The [efecto psicológico] | [The Pygmalion Effect](https://www.youtube.com/watch?v=4aN5TbGW5JA) |
| 25 | ReversHub | 106 | 21 | 621K | ≥2025 | 4:22 | rasgos cotidianos | Psychology of People Who Don't [hábito] | [Psychology of People Who Don’t Watch Football](https://www.youtube.com/watch?v=YtXYUZbDyEg) |
| 26 | Psych2Go | 95 | 39 | 18.0M | ~2020 | 5:43 | familia/infancia | N Toxic Things Parents Say To Their Children | [8 Toxic Things Parents Say To their Children](https://www.youtube.com/watch?v=GS_mATLF7BE) |
| 27 | ReversHub | 92 | 47 | 538K | ≥2025 | 3:47 | rasgos cotidianos (redes) | Psychology of People Who Don't [hábito] | [Psychology of People Who Don’t Post Their Photos on Social Media](https://www.youtube.com/watch?v=JtHIgGqTS-8) |
| 28 | ReversHub | 91 | 55 | 533K | ≥2025 | 4:17 | rasgos (introversión) | Psychology of People Who Love [hábito] | [Psychology of People Who Love Staying at Home](https://www.youtube.com/watch?v=ibksvBVKIq0) |
| 29 | Psych2Go | 89 | 45 | 17.0M | ~2020 | 4:55 | social | N Things Only Fake Friends Do | [7 Things Only Fake Friends Do](https://www.youtube.com/watch?v=HR-PwsUayY0) |
| 30 | PsychToons | 87 | 7 | 537K | ~2026-09 | 17:39 | autoayuda (virtud) | Psychology of [virtud] (And How To Stop [X]) | [Psychology of Self-Worth (And How To Stop Seeking External Validation)](https://www.youtube.com/watch?v=0nBvAYO-DGg) |

### Top-25 outliers · español · Shorts

| # | Canal | Score | Vistas | Título |
|---|---|---|---|---|
| 1 | CarlaKuhn | 160 | 737K | [Esa Persona En Tu Mente, Siente De Forma Parecida Lo Mismo Que Tú](https://www.youtube.com/watch?v=ZppluZ1dufM) |
| 2 | DoctoraFlorez | 113 | 839K | [Amor propio NO es mendigar. Episodio 16 completo en mi perfil. #podcast](https://www.youtube.com/watch?v=OLjocUgKnJI) |
| 3 | MentesExpertas | 97 | 365K | [La mejor frase que vas a escuchar hoy / Victor Küppers](https://www.youtube.com/watch?v=cYhxvaqjPrE) |
| 4 | CarlaKuhn | 95 | 435K | [Te Empiezan A Echar de Menos Cuando](https://www.youtube.com/watch?v=G5bxcNIWI5Q) |
| 5 | MentesExpertas | 65 | 243K | [El dolor social / Marian Rojas Estapé #shorts](https://www.youtube.com/watch?v=n1H47pSGAnw) |
| 6 | DoctoraFlorez | 57 | 420K | [Hazte esta pregunta. Episodio 19 en mi perfil: todo sobre celos y amor propio. #psicologia](https://www.youtube.com/watch?v=8Gi9RHbj1V0) |
| 7 | DoctoraFlorez | 47 | 351K | [Apego ansioso a la pareja: ¿cómo romper con la dependencia emocional? Episodio en mi perfi](https://www.youtube.com/watch?v=T3mRPjcPC0M) |
| 8 | Psych2GoES | 47 | 563K | [4 Tipos de Introvertidos #Shorts / Psych2Go](https://www.youtube.com/watch?v=SC5JW0dHGLI) |
| 9 | DoctoraFlorez | 47 | 345K | [🎙️¡Escucha el episodio completo de El Consultorio de Florez en mi perfil! #pareja](https://www.youtube.com/watch?v=xKaxBeBBmfk) |
| 10 | LluisRodriguez | 45 | 209K | [El apego evitativo NO es un comportamiento](https://www.youtube.com/watch?v=_aAKA8Pou_c) |
| 11 | DoctoraFlorez | 44 | 324K | [🎙️ Episodio completo en mi perfil. #psicologa #terapiadepareja #podcast #amor #relaciondep](https://www.youtube.com/watch?v=qtb0GvtSldA) |
| 12 | LluisRodriguez | 44 | 201K | [Apego evitativo. ¿Qué le hace feliz?    #apego #apegoevitativo #feliz](https://www.youtube.com/watch?v=4rL8CjuNJvA) |
| 13 | MentesExpertas | 38 | 141K | [¿Cómo disfrutar del trabajo? / Victor Küppers](https://www.youtube.com/watch?v=Dj-_wdTd84U) |
| 14 | Psych2GoES | 37 | 445K | [Señales de Inteligencia #Shorts / Psych2Go](https://www.youtube.com/watch?v=wPJtwdZ7jS0) |
| 15 | AleAlvarezPsi | 37 | 2.2M | [COMO SUPERAR A ALGUIEN #reflexion #psicologia #amor #relaciones #pareja #superacion #short](https://www.youtube.com/watch?v=xGs7MlVPnHQ) |
| 16 | AleAlvarezPsi | 37 | 2.2M | [¿Qué hacer si no me QUIERE? #psicologia #amor #relaciones #pareja #autoestima #shorts #sup](https://www.youtube.com/watch?v=WL8trCrhyWg) |
| 17 | MentesExpertas | 34 | 128K | [¿Cómo aprender a aceptar las circunstancias? / Pilar Sordo](https://www.youtube.com/watch?v=7p07cyXfUKo) |
| 18 | MentesExpertas | 33 | 122K | [Ser capaz de elegir tu mejor actitud / Victor Küppers](https://www.youtube.com/watch?v=lHgyt4ud41w) |
| 19 | DoctoraFlorez | 32 | 240K | [🎙️ ¡EPISODIO EN MI PERFIL! #amorpropio #podcastpsicologia](https://www.youtube.com/watch?v=pCZCpVXiy48) |
| 20 | LluisRodriguez | 32 | 146K | [Apego evitativo. ¿Por qué un día está bien y al otro te rechaza?     #apego #apegoevitativ](https://www.youtube.com/watch?v=lokPa2jy7fQ) |
| 21 | CarlaKuhn | 32 | 146K | [¿El Apego Evitativo Echa De Menos?](https://www.youtube.com/watch?v=AI9Zf2nieKM) |
| 22 | MentesExpertas | 30 | 114K | [¿Qué es lo mejor que llevas dentro? / Victor Küppers](https://www.youtube.com/watch?v=lWR9F2weyhA) |
| 23 | AleAlvarezPsi | 30 | 1.8M | [No fuerces lo que no va! #psicologia #amor #relaciones #autoestima #amorpropio #shorts #ti](https://www.youtube.com/watch?v=LYi42_pq8aE) |
| 24 | Psych2GoES | 28 | 331K | [¿Tienes Pareja y te gusta otra persona? 😱 #shorts / Psych2Go](https://www.youtube.com/watch?v=gZsvNkRLDbA) |
| 25 | DoctoraFlorez | 26 | 196K | [Descubre el motivo de los celos en el episodio 19 de mi perfil. #psicolgia](https://www.youtube.com/watch?v=nocoXcOKbB4) |

### Top-15 outliers · inglés · Shorts

| # | Canal | Score | Vistas | Título |
|---|---|---|---|---|
| 1 | Sprouts | 343 | 4.8M | [Sex differences [Short Version] #gender #biology #sexdifferences](https://www.youtube.com/watch?v=vWqK2NJA3sM) |
| 2 | ReversHub | 223 | 4.9M | [Psychology of People Who Don't Get Tattoos](https://www.youtube.com/watch?v=6MWE17Wqcco) |
| 3 | ReversHub | 182 | 4.0M | [Psychology of People Who Treat Their Birthday Like a Normal Day](https://www.youtube.com/watch?v=Y5F-oWHomL4) |
| 4 | ReversHub | 86 | 1.9M | [Psychology of Men Who Don’t Care About Girls](https://www.youtube.com/watch?v=dt9L2q8XNS4) |
| 5 | ReversHub | 68 | 1.5M | [Psychology of people who don’t post their photos on social media](https://www.youtube.com/watch?v=T51BaXtQ-s0) |
| 6 | ReversHub | 68 | 1.5M | [Psychology of people who love staying at home](https://www.youtube.com/watch?v=6s1uOAwRuwc) |
| 7 | ReversHub | 45 | 1.0M | [Psychology of People Who Stay Single](https://www.youtube.com/watch?v=Wl9qyfYOWNg) |
| 8 | ReversHub | 39 | 866K | [Psychology of People Who Love Being Alone](https://www.youtube.com/watch?v=XWftdKJw5_w) |
| 9 | SchoolOfLife | 39 | 2.4M | [Why Unloved People Hate Themselves #shorts  #selfcare](https://www.youtube.com/watch?v=LCaTPmNKEm8) |
| 10 | Psych2Go | 35 | 2.4M | [Which Type of Friend Are You? #shorts](https://www.youtube.com/watch?v=QenqsWLiDHc) |
| 11 | Psych2Go | 29 | 2.0M | [6 Signs You Were Never in Love](https://www.youtube.com/watch?v=YWI-yzmUxyo) |
| 12 | Psych2Go | 28 | 1.9M | [7 Signs You’re Not Lazy, But Depressed](https://www.youtube.com/watch?v=WYF0v7itMl4) |
| 13 | SchoolOfLife | 28 | 1.7M | [How To Be Very Attractive #shorts #dating #attractive](https://www.youtube.com/watch?v=29UuouECAbA) |
| 14 | Psych2Go | 26 | 1.8M | [Signs Someone is Secretly Admiring You](https://www.youtube.com/watch?v=cUS8zuoOp3g) |
| 15 | Psych2Go | 26 | 1.8M | [Will DELETE in 24 hours](https://www.youtube.com/watch?v=MHCid1pqUAI) |

<!-- TABLAS_FIN -->

### 3.1 Codificación del top-50 en español [D]

**Tema (manual)**

| Tema | Videos |
|---|---|
| Rasgos cotidianos e identidad ("personas que…", incluida la inteligencia mecánica) | 13 |
| Trastornos y salud mental explicados o detección (ansiedad, TDAH, depresión oculta, neurodivergencias, fobias, autismo, burnout, heridas) | 12 |
| Filosofía y "autor clásico" (Jung, Maquiavelo, Montaigne) | 7 (6 de El Consejero y 1 de Escéptico) |
| Social y autopercepción (caes mal, molestas, envidia, torpeza, lenguaje) | 5 |
| Amor, atracción y apego | 5 |
| Relaciones tóxicas y narcisismo | 3 (todos de 2021–2022) |
| Inteligencia (IQ bajo, inteligencia emocional) | 2 |
| Tests | 2 |
| Emociones (cómo dejar de tener miedo) | 1 |

**Gancho psicológico**

| Gancho | Videos |
|---|---|
| Identificación o validación ("esto soy yo") | ~18 |
| Detección en otro ("le gustas", "te envidia", "tu pareja es narcisista") | 7 |
| Autoevaluación o test | 6 |
| Compendio ("todas las X") | 4 |
| Alivio de culpa o reencuadre ("No es pereza, es TDAH/burnout", "No eres perezoso, solo estás perdido") | 3 |
| Solución práctica | 2 (los dos son del psicólogo con cara Chris Núñez) |

**Otras características**
- **Duración:** mediana de 9:10. Los compendios y los videos de "autor clásico" duran entre 15 y 26 minutos.
- **Fecha:** 29 de los 50 son de dic-2025 a nov-2026, y **los 29 son de canales nacidos en esa misma ola**. Los otros 21 son éxitos acumulados de 2019–2025 de Psych2Go ES, Sapiencia Práctica, Psicología Animada, Chris Núñez, El Consejero y Escéptico.
- **Series y franquicias:** 11 pertenecen a "Psicología de las personas que…", 13 a "N señales de…" y 3 a "Todas las X explicadas en N min". Casi ninguno es "parte 2" de una serie; la "serie" es la **plantilla repetida**.

### 3.2 Codificación del top-30 en inglés [D]

- **Autoayuda en forma de "Psychology of [virtud]: [promesa hiperbólica]"** (8 videos, casi todos de PsychToons entre ago y oct de 2026). Ejemplos: "Psychology of Discipline (And How to Trick Your Brain Into Craving It)", con 5.3M, y "Psychology of Composure: Be So Calm It Makes People Nervous".
- **Inteligencia:** 6.
- **Rasgos cotidianos "people who":** 9.
- **Generaciones** (Gen X, Xennials, 1970s): 3.
- Clásicos de catálogo: Sprouts "The Pygmalion Effect" (19M) y Psych2Go "8 Toxic Things Parents Say" (18M).
- Mediana de duración: 9:19.
- **[I] En inglés la ola "people who…" (nov-2025 a jun-2026) ya está dando paso a "Psychology of [virtud] + promesa de poder".** En español esa segunda ola **todavía no funciona**: LPI la copió en nov-2026 y obtuvo entre 5K y 38K, con la excepción de "disciplina" (862K en sep-2026). Esos videos de LPI tienen menos de 2 semanas, así que el dato es preliminar.

### 3.3 Shorts [D]

**En español**
- Los outliers de Shorts son casi todos **de psicólogos con cara y de clips de expertos**, sobre **amor, apego y amor propio**:
  - Doctora Flórez: 10 de los top-25, todos recortes de su podcast con CTA "episodio completo en mi perfil".
  - Carla Kuhn: "Esa persona en tu mente siente de forma parecida lo mismo que tú", 737K.
  - Ale Álvarez Psi: 3 videos de 1.8M a 2.2M sobre "cómo superar a alguien" o "qué hacer si no me quiere".
  - Lluís Rodríguez: apego evitativo, de 146K a 209K.
  - Mentes Expertas: Marian Rojas Estapé y Víctor Küppers.
- Psych2Go ES aporta 4 Shorts de "tipos de introvertidos" y "señales de inteligencia".
- Por plantilla, en Shorts en español gana "Cómo…" (lift 1.3) y por tema "inteligencia" (2.7, n pequeño). **No hay ningún Short "psicología de las personas que…" en los 3,518 Shorts analizados.**

**En inglés**
- Revers Hub pone **6 de los top-8 Shorts** con exactamente la plantilla larga "Psychology of People Who…": no se tatúan (4.9M), cumpleaños (4.0M), hombres a los que no les importan las chicas (1.9M), no publican fotos (1.5M), aman quedarse en casa (1.5M).
- El lift de la plantilla en Shorts en inglés es **4.0**, el más alto de todo el estudio.
- [I] Un Short de 30–60 s con la plantilla "personas que…" y el mismo personaje es la jugada de menor riesgo y mayor techo para el canal en español.

---

## 4. Qué funciona: temas y plantillas (lift)

**Español, videos largos, últimos 12 meses** (n=3,837; decil superior = score local ≥ 4.4) [D]

| Tema | n | % de videos | % del decil top | Lift | Mediana score local | p90 |
|---|---|---|---|---|---|---|
| Inteligencia | 105 | 2.7% | 5.7% | **2.09** | 1.10 | 12.6 |
| Rasgos cotidianos | 242 | 6.3% | 10.6% | **1.69** | 1.09 | 10.2 |
| Social y comunicación | 177 | 4.6% | 7.3% | **1.58** | 1.00 | 8.0 |
| Trastornos y salud mental | 198 | 5.2% | 6.2% | 1.21 | 0.97 | 4.7 |
| Personalidad y tipos | 291 | 7.6% | 8.3% | 1.10 | 1.05 | 4.8 |
| Psicología oscura | 215 | 5.6% | 5.5% | 0.97 | 1.09 | 4.1 |
| Amor y pareja | 350 | 9.1% | 8.1% | 0.88 | 1.06 | 3.9 |
| Apego | 174 | 4.5% | 2.9% | 0.63 | 1.14 | 3.3 |
| Generaciones y nostalgia | 33 | 0.9% | 0.5% | 0.60 | 0.79 | 2.0 |
| Tóxico y narcisismo | 153 | 4.0% | 2.3% | **0.59** | 0.92 | 2.9 |
| Familia e infancia | 135 | 3.5% | 1.8% | **0.52** | 0.75 | 2.3 |
| Autoayuda y desarrollo | 71 | 1.9% | 0.8% | **0.42** | 0.80 | 2.4 |

| Plantilla (es, últimos 12 meses) | n | Lift | p90 score local |
|---|---|---|---|
| "Todas/Cada X explicad@s en N minutos" | 43 | **3.71** | 25.1 |
| Test o quiz | 37 | **2.15** | 10.0 |
| "La psicología de las personas que…" | 297 | **1.91** | 14.2 |
| "N señales de…" | 170 | **1.58** | 8.2 |
| "Psicología de [X]" | 153 | 1.43 | 7.1 |
| "¿Qué dice de ti…?" | 67 | 1.04 | 3.3 |
| "¿Por qué…?" | 430 | 0.93 | 4.1 |
| "Cómo…" | 227 | **0.70** | 3.3 |

**En inglés, últimos 12 meses (n=1,229) [D]**
- Mejores plantillas: "What is / What happens…" (lift 2.75), "Psychology of [X]" (1.9), test (1.8) y "people who" (1.7).
- Peores: "Why…" (0.77), "How to" (0.49) y "If you…" (0.27).
- Mejores temas: inteligencia (1.8) y rasgos (1.6).
- Peores temas: autoayuda (0.6), familia (0.4) y emociones genéricas (0.55).

**Rasgos del título (es, últimos 12 meses, mediana del score local con y sin el rasgo) [D]**
- Efectos pequeños: con número 1.07 frente a 0.98; con una palabra en MAYÚSCULAS 1.04 frente a 0.98; con paréntesis 1.04 frente a 1.00.
- Con signo de pregunta: 0.93 frente a 1.02.
- Título entero en mayúsculas: 0.86.
- [I] El formato del título importa mucho menos que el tema y la miniatura. Una o dos palabras clave en mayúsculas y un paréntesis de remate ("(y no es casualidad)", "(No es lo que parece)", "(y nadie te lo dice)") son baratos y no restan. Evitar el título en forma de pregunta: rinde algo menos en los dos idiomas.

**Duración (es, largos, últimos 12 meses) [D]**

| Duración | % de videos con 10× o más sobre la mediana del canal |
|---|---|
| Menos de 3 min | 1.3% |
| 3–5 min | 2.2% |
| 5–8 min | 4.1% |
| **8–12 min** | **8.7%** |
| 12–20 min | 5.7% |
| 20–40 min | 8.2% (compendios y "autor clásico") |

En inglés el mejor rango es 12–20 min (20.1%), seguido de 8–12 min (11.5%).

---

## 5. Tendencias en el tiempo (2024 → 2026)

**Peso de cada tema en lo que se sube (es, largos) [D]**

| Tema | hace 24–36 meses | hace 12–24 meses | hace 6–12 meses | últimos 6 meses |
|---|---|---|---|---|
| Tóxico y narcisismo | **26.5%** | 4.8% | 3.0% | 3.2% |
| Apego | 9.5% | 6.5% | 2.6% | 2.3% |
| Amor y pareja | 14.0% | 10.0% | 9.5% | 6.8% |
| Rasgos cotidianos | 0.1% | 1.4% | 9.9% | **13.5%** |
| Plantilla "psicología de las personas que" | 0.0% | 1.1% | 12.1% | **10.8%** |
| Social y comunicación | 2.1% | 3.2% | 5.9% | 6.5% |
| Cerebro, cuerpo y sueño | 1.4% | 0.9% | 4.1% | 4.9% |
| Psicología oscura | 3.3% | 7.0% | 6.4% | 1.9% |
| Generaciones | 0.1% | 0.2% | 2.2% | 1.0% |

**Lectura**
- [D] **La ola del narcisismo** (2023–2024) se apagó en cuanto a lo que se publica, y lo que se sigue publicando rinde menos (score local de 0.66 a 0.82 en los últimos 12 meses).
- [D] **La ola de "personas que…"** llegó a los canales en español hacia dic-2025 a ene-2026, un mes o dos después de la ola en inglés (Revers Hub, Psychology Simplified).
- [D] La plantilla pasó a ser el **10–21% de todo lo que publican los canales de la muestra en 2026**.
- [D] **Su mediana de vistas por video cayó** de ~126K en mar-2026 (pocos canales, sobre todo LPI) a 600–1,800 entre jul y nov de 2026, mientras el resto de los videos se mantiene en 4–5K.
- [I] **La plantilla está saturada en oferta.** Solo funciona con un tema muy bien elegido y con una "marca" que el algoritmo ya reconoce, como LPI.
- [D] **"Psicología oscura"** subió entre 2024 y 2025 (6–7% de lo publicado) y está cayendo (1.9%).
- [D] **Generaciones** tuvo un pico corto: LPI "Xennials" 1.4M en mar-2026 y Psychology Simplified "Gen X" 3.5M en feb-2026. Sus secuelas fracasan: "10 cosas que solo la Gen X recordará", de LPI, hizo 5.7K.
- **En inglés [D]** "Psychology of [virtud/inteligencia]" pasa del 1% al 20% de lo que se publica en los últimos 6 meses, y los temas de "inteligencia" del 0.8% al 11.8%. [I] Es la próxima ola que llegará traducida al español. Hoy rinde mal en español, así que conviene probarla con cuidado.

### 5.1 Velocidad de los canales nuevos [D]

Vistas de los videos publicados en cada mes; el mes es aproximado.

| Canal (inicio) | Curva |
|---|---|
| **La Psicología Invisible** (feb-2026) | feb: 66K → mar: 3.1M (primer video de 1.4M en su **mes 2**) → abr: 5.2M (3.6M en "cumpleaños") → may: 6.2M → de jun a nov, 0.75–2.2M al mes. Publica 8–11 videos al mes, de 8 a 9.5 min. Ronda 1: 256K suscriptores. [W] Social Blade lista la creación el 3-feb-2026 y 215K suscriptores en una fecha anterior. |
| PsychToons (ene-2026, inglés) | **7 meses casi planos** (menos de 100K vistas al mes, salvo un video de 2.3M en marzo) → ago: 13.2M, sep: 8.0M, oct: 5.5M con la serie "Psychology of [virtud]". |
| Psychology Simplified (dic-2025, inglés) | ene: 9.0M, feb: 8.3M → declive a ~0.1–0.3M al mes desde jul. |
| Revers Hub (≤nov-2025, inglés) | 6.4M en su primer mes → menos de 25K al mes desde jun → dejó de publicar en ago-2026. |
| Apex Psychology (feb-2026, inglés) | abr–jun: ~3M al mes → 0.5–1.7M después. |
| IdealMente (feb-2026) | feb–abr: 0.6–1.2M al mes → jul–sep: menos de 20K → oct–nov: rebrote (642K y 416K) con "N señales de que molestas / socialmente torpe". |
| La Mente Oculta, Psicología Clara, Psicología Sin Filtro, LoDescomún, MenteConsciente, Psicología Cotidiana, DatoVisual, Psicología Oscura | 1 o 2 meses buenos (uno o dos videos de 0.4–2.3M) → caída a cientos o pocos miles de vistas por video. Varios dejaron de publicar. |
| Claridad Mental (ago-2026), Manual de Vida (≤nov-2025) | Meses en cero → un viral en oct-2026 (781K y 424K) traduciendo temas de PsychToons y LPI. |

**Lectura [I]**
- **"Pegar" no es difícil** con el formato correcto: la mayoría de los canales lo logró en sus primeros 1 a 3 meses.
- **Retener sí lo es.** LPI se distingue por cuatro cosas:
  1. un **personaje recurrente reconocible** (el frijol verde-gris);
  2. una **cadencia constante** (unos 2 por semana);
  3. un **título siempre igual**, que funciona como marca;
  4. la **voz humana** (dato de la ronda 1).
- La mayoría de los clones usa personajes genéricos de IA (monitos blancos, siluetas) que cambian de video a video.

### 5.2 Cómo viajan los temas: copiar de inglés a español [D]

| Tema | Inglés (primero y mejor) | Español (mejor) | Lag aprox. |
|---|---|---|---|
| Cumpleaños como día normal | Revers Hub, ≤nov-2025, 3.3M | LPI, abr-2026, **3.6M** | ~5 meses o más |
| Gen X / Xennials | Psychology Simplified, feb-2026, 3.5M y 2.0M | LPI Xennials, mar-2026, 1.4M | ~1 mes |
| No ver deportes o fútbol | Psychology Simplified, ene-2026, 3.0M | LoDescomún, ene-2026, 351K; LPI, jun-2026, 298K | 0–5 meses |
| No publicar fotos | Revers Hub, ≤nov-2025 | Psicología Sin Filtro, 6-may-2026, 690K; LPI, ago-2026, 293K | ~6 meses |
| Inteligencia mecánica / arreglarlo todo | LPI, may-2026, 2.8M (el primero en la muestra) → PsychToons, 21-oct-2026, 1.6M | Claridad Mental, 23-oct-2026, 781K (traducción literal de PsychToons) | **2 días** |
| Disciplina | PsychToons, ago-2026, 5.3M | LPI, sep-2026, 862K | ~1 mes |
| Personas que se quedan calladas cuando les duele | PsychToons, mar-2026, 2.3M | LPI, may-2026, 38K (fracaso) | 2 meses |
| Infieles (mismo título exacto) | — | Psicología Sin Filtro, jun, 18K → Psicología Cotidiana, ago, 46K → **LPI, oct, 698K** | — |
| Abrazar la almohada (mismo título) | — | Psicología Cotidiana, ago, **797K** → Sin Filtro, sep, 511 → LPI, oct, 392K → Manual de Vida, nov, 709 | — |

La lista completa está en `topic_lag.csv`.

**Lectura**
- [I] El ecosistema funciona como un "mercado de outliers": los canales vigilan los éxitos de otros (en inglés y en español) y los re-producen.
- [I] Los títulos idénticos, con la misma tipografía de MAYÚSCULAS y el mismo orden de publicación, sugieren que **varios de estos canales usan las mismas herramientas de detección de outliers o son del mismo operador**.
- [D] **El mismo tema rinde según el canal que lo publica:** de 511 a 797K vistas. [I] La autoridad del canal y la ejecución pesan tanto como el tema.
- [D] **Repetir un tema propio fracasa.** LPI rehízo cumpleaños dos veces: "La Verdad Psicológica Detrás de Quienes Ignoran su Cumpleaños" (10K) y "Si NO te importa tu cumpleaños, CUIDADO con esto" (21K), frente a 3.6M del original. Las variaciones de "estar solas" obtuvieron 662K, 356K, 100K, 22K y 16K, de más a menos.

### 5.3 Dentro de LPI: qué separa sus éxitos de sus fracasos [D]

| Grupo | Ejemplos |
|---|---|
| **Éxitos (≥500K)** | cumpleaños (3.6M), arreglarlo todo (2.8M), casa limpia (1.7M), demasiado conscientes (1.4M), Xennials (1.4M), escenarios falsos (961K), disciplina (862K), hombre niño (725K), desaparecen sin explicar (708K), infieles (698K), prefieren estar en casa (662K), demasiados intereses (557K), nunca se tatúan (518K) |
| **Fracasos (<20K)** | perros que duermen contigo, deudas, coches de lujo antiguos, café al despertar, TV encendida, mensajes de texto frente a llamar, liderazgo (5.4K), "no recuerdas haber sido bebé" (9.5K), Gen X 2 (5.7K) |

**[I] Regla que se desprende**
- Gana el rasgo que **una gran parte del público puede reconocer en sí misma** y que se presenta como una **virtud incomprendida** ("No es lo que parece", "no es casualidad").
- Pierden el rasgo nicho (coches de lujo, deudas), el hábito sin carga identitaria (café, TV), la autoayuda imperativa y la secuela.

---

## 6. Patrones visuales de las miniaturas

Revisé las miniaturas de los top-20 outliers en español, 6 éxitos y 3 fracasos de LPI, y 7 éxitos de Psych2Go ES, Sapiencia Práctica, Sprouts ES y DatoVisual. Las hojas de contacto están copiadas en `investigacion/referencias_visuales/outliers/` (`sheet_top1-10.jpg`, `sheet_top11-20.jpg`, `sheet_extra_a.jpg` y `sheet_extra_b.jpg`).

**Composición [D]**
- **~18 de 20** son miniaturas partidas en dos: **personaje o ilustración a un lado y bloque de texto al otro**, con el texto casi siempre a la derecha.
- **Personaje:** una sola figura simple y casi sin rasgos.
  - El monito de cabeza blanca redonda aparece en Claridad Mental, La Mente Oculta, Psicología Clara, Psicología Sin Filtro y LoDescomún.
  - El "frijol" verde-gris de LPI.
  - Figuras lilas tipo "frijol" en Psicología Cotidiana.
  - Siluetas negras en IdealMente, Manual de Vida y Psicología Oscura.
- La cara del personaje expresa **una sola emoción legible**: duda, mano en la barbilla, tristeza, fastidio.
- [I] La expresión es mínima, para que cualquiera se proyecte en ella.
- **Escena cotidiana concreta** que ilustra el rasgo: un cajón lleno de cables, una lavadora abierta, un pastel con una vela, una sala desordenada frente a una ordenada, un estadio, una puerta de casa, un walkman, íconos de redes tachados.
- [I] El objeto cuenta el tema antes que el texto.

**Texto [D]**
- **2 a 5 palabras**, en mayúsculas, con tipografía condensada gruesa (tipo Bebas/Anton/Impact).
- **Colores:** negro sobre bloque **amarillo** (LPI, La Mente Oculta, Psicología Clara, Psicología Sin Filtro, el rótulo de Claridad Mental) o blanco y negro sobre **rojo** (IdealMente, Manual de Vida, LoDescomún, Claridad Mental). Rara vez otro color.
- El texto **reformula el título en segunda o tercera persona, más corto y emocional**:
  - "NO CELEBRAN SU CUMPLEAÑOS"
  - "¿PUEDEN ARREGLARLO TODO?"
  - "PREFIERO ESTAR SOLO"
  - "PERSONAS QUE ELIMINARON A TODOS"
  - "Eres MOLESTO (y nadie te lo dice)"
  - "NO PUBLICAN NADA. Y esto dice de ellos."
- **Elementos de dirección:** una **flecha** curva (casi siempre roja) que apunta al objeto o al personaje en 8 de 20 (y en casi todas las de LPI), círculos rojos de "pista" y a veces un "¿TÚ?" manuscrito.

**Color y fondo [D]**
- Fondos claros, crema o beige, de baja saturación (LPI y Psicología Clara), o blanco plano (IdealMente).
- Los acentos saturados (amarillo y rojo) quedan reservados al texto y la flecha.
- Los canales de "psicología oscura" usan negro con grabado de tinta y vetas rojas.

**Contraste éxito / fracaso dentro de LPI [D]**
- Mismo estilo en todos, así que **el estilo no explica el fracaso**: el tema sí.
- Sus fracasos "Gen X recordará" (5.7K) y "cumpleaños 2" (10K) tienen miniaturas igual de pulidas.
- [I] El estilo visual es una condición necesaria (te deja competir), no suficiente.

**Estilo de los éxitos establecidos [D]**
- Psych2Go ES, Sapiencia Práctica y Sprouts ES usan un **personaje propio dibujado a mano** (el monito blanco de Psych2Go, el personaje con hoja de Sapiencia), con colores planos, texto grande en 2 colores y emoción clara.
- DatoVisual usa una **retícula de íconos** en su compendio de neurodivergencias.

**Riesgo detectado [I]**
- Varias miniaturas de los clones (Psicología Cotidiana, Psicología Clara, IdealMente) son visiblemente de **IA genérica**, con ilustración "limpia" y personajes que cambian entre videos.
- La ronda 1 documentó el rechazo creciente a la "AI slop".
- El hueco está en hacer lo mismo **con un personaje propio, consistente y hecho a mano**, como Psych2Go ES o Sapiencia.

---

## 7. Recomendaciones para Agenda PSI

Todas son [I], apoyadas en los datos anteriores.

### 7.1 Formato largo (YouTube)

**Plantilla base:** "La psicología de las personas que [rasgo cotidiano que mucha gente reconoce en sí misma]" + un paréntesis que reencuadre ("(no es lo que parece)", "(y no es casualidad)"). Duración: 8–10 min.

**Temas que hoy tienen datos a favor en español:**
1. **Rasgos e identidad cotidiana:** prefieren estar en casa, olvidan nombres, imaginan escenarios, piensan demasiado, guardan todo, no celebran su cumpleaños, no publican fotos.
2. **Inteligencias "no académicas":** mecánica, emocional, social; "señales de inteligencia que nadie valora".
3. **Social y autopercepción:** "N señales de que molestas sin darte cuenta" o "de que le caes mal".
4. **Compendios de salud mental** "Todas las [fobias / neurodivergencias / tipos de ansiedad] explicadas en N minutos". Tienen lift 3.7 y son el lugar natural para que el psicólogo real dé autoridad.
5. **Reencuadre que alivia la culpa:** "No es pereza, es [TDAH/burnout/depresión]". En Sapiencia acumula 8.3M y 4.2M; [I] está desatendido en 2026.

**Lo que conviene evitar en el formato largo:** narcisismo y relaciones tóxicas, apego como tema central, autoayuda imperativa ("Cómo ser un gran líder"), secuelas de un tema propio ya viral y generaciones como serie.

**Diferenciación que el mercado no tiene:**
- **Contexto mexicano** en los ejemplos.
- **Psicólogo real con cédula visible** (esto también protege la monetización, ver ronda 1).
- **Personaje propio y estable.**

### 7.2 Shorts, TikTok y Reels

- Llevar la plantilla "personas que…" al formato vertical de 30–60 s con el mismo personaje.
- [D] En inglés tiene lift 4.0 y en español nadie la usa.
- Segundo carril: **amor propio, apego y "cómo superar a alguien"**, que es lo que gana en Shorts en español. Mejor en voz del psicólogo real que del personaje, en línea con Doctora Flórez, Ale Álvarez y Carla Kuhn.

### 7.3 Proceso: vigilar outliers como sistema

- Revisar cada semana Revers Hub, PsychToons, Psychology Simplified, Apex Psychology y Psychology Insight (inglés), y LPI e IdealMente (español).
- Detectar temas con score de 20× o más sobre la mediana del canal.
- Producir la versión mexicana en 2 a 6 semanas.
- Un solo intento por tema. Si falla, no repetirlo.
- Los scripts de este estudio sirven para eso.

### 7.4 Miniatura

Partida en dos:
- **A la izquierda**, nuestro personaje en una escena cotidiana con un objeto que cuente el tema y una flecha roja.
- **A la derecha**, 2 a 4 palabras en mayúsculas condensadas, negro sobre amarillo o blanco sobre rojo.
- Fondo claro y emoción única en el personaje.

### 7.5 Expectativas

Planear para una distribución de cola larga:
- Unos 2 de cada 10 videos harán el 80% de las vistas (en LPI: 13 de 81 superan 500K).
- Los primeros 3 meses pueden ser planos, como los 7 meses de PsychToons.
- Medir por "hits por cada 10 videos", no por promedio.

---

## 8. Archivos de datos y reproducibilidad

Todos en `/tmp/claude-0/-home-user-Creador-de-videos-Para-redes-/f6e80049-54f1-5e5b-b0dd-1d5ea884d7d2/scratchpad/research/outliers/`.

| Archivo | Contenido |
|---|---|
| `channels.tsv` | Los 39 canales con ID, idioma y tipo |
| `raw/*.json` | Catálogos crudos de yt-dlp (`--flat-playlist -J`, títulos en es) |
| `dates/*.tsv` | Pase de fechas aproximadas para los canales en español |
| `videos_all.csv` | 18,089 filas: vistas, duración, fecha aprox., score, score local, tema y plantilla automáticos, banderas del título |
| `channels_summary.csv` | Mediana, p90, máximo, concentración top-10, número de outliers de 10× o más, por canal y formato |
| `final_outliers.csv` | Rankings filtrados: es_long 50, en_long 30, es_short 25, en_short 15 |
| `outliers_coded.csv` | Los mismos, con codificación manual (tema, plantilla, franquicia, gancho), más fecha exacta, likes, comentarios y suscriptores cuando se pudieron obtener |
| `top_outliers_*.csv`, `top_local_outliers_*.csv` | Rankings sin piso de vistas (top 80/50) |
| `aggregates.txt`, `lift_tables.json` | Tablas de lift, tendencias, duración y crecimiento de canales nuevos |
| `topic_lag.csv`, `topic_lag.txt` | Propagación de temas entre inglés y español |
| `thumbs/*.jpg`, `sheet_*.jpg` | Miniaturas y hojas de contacto |
| `details/*.json` | Metadatos individuales (fecha exacta, likes, suscriptores) |
| `discovery/` | Resultados de las búsquedas de descubrimiento |

Los scripts para reproducir están en `.../scratchpad/scripts/`: `fetch_catalogs.sh`, `fetch_dates.sh`, `fetch_details.sh`, `analyze_outliers.py`, `select_final.py`, `aggregate.py`, `topic_lag.py`, `code_outliers.py`, `md_tables.py` y `montage.py`.

**Fuente web:** [Social Blade — @lapsicologiainvisible](https://socialblade.com/youtube/handle/lapsicologiainvisible), consultada para la fecha de creación del canal.
