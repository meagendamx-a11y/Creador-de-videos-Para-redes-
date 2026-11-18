# Voz y música (revisión nov-2026)

> Verifica precios y licencias en la página oficial antes de pagar. Cambian seguido.

## Voz
| Opción | Qué es | Costo | Comentario |
|---|---|---|---|
| **0. Grabar tu voz directamente** | Celular o micrófono USB en un cuarto silencioso, y limpieza de audio gratis | $0 | La investigación dice que la voz humana es lo más valorado ("Por fin un narrador humano", 223 likes). Es la opción más auténtica |
| **1. ElevenLabs Starter: clonación instantánea** | Grabas de 1 a 3 min de audio limpio y genera tu voz a partir de texto | USD 1 el primer mes (promo hasta el 1-dic-2026), luego USD 6/mes. Incluye licencia comercial y ~30 min al mes ([precios](https://www.elevenlabs.io/pricing), [resumen](https://bigvu.tv/blog/elevenlabs-pricing-2026-plans-credits-commercial-rights-api-costs/)) | Para producir un video al día sin grabar cada uno. Recomendado para empezar |
| **2. ElevenLabs Creator: clonación profesional** | Clon entrenado con ~30 min o más de grabación. Suena más natural | ~USD 22/mes | Solo si la instantánea no convence |
| Alternativas | Fish Audio, Typecast, Descript | Variable | Fish Audio dice ser hasta 70% más barato; no lo he probado en español de México |

**Reglas:**
- Solo se clona **tu propia voz** o la de alguien que dé su consentimiento por escrito.
- El plan Free no permite uso comercial ni clonación.
- Prueba hecha (pendiente): mismo guion grabado con tu voz real y con el clon. Que lo escuchen 5 personas y digan cuál prefieren.

## Música de fondo
| Fuente | Costo | Riesgo de reclamo de derechos (Content ID) | Uso |
|---|---|---|---|
| **YouTube Audio Library** (YouTube Studio → Biblioteca de audio) | $0 | Bajo: YouTube dice que no genera reclamos ([guía](https://www.foximusic.com/blog/what-background-music-can-i-use-on-youtube-guide/)) | **Recomendado para YouTube.** Revisa si la pista pide atribución |
| Bibliotecas de TikTok e Instagram (en la app; en cuentas de empresa, la *Commercial Music Library*) | $0 | Bajo dentro de su plataforma | Para TikTok y Reels, agrega la música desde la app |
| ElevenLabs Music (planes de pago) | Gasta muchos créditos (~900 por minuto) | Uso comercial desde Starter | Música original a la medida; caro para uso diario |
| Uppbeat, Incompetech | Gratis con atribución | Medio | Revisa la licencia de cada pista ([Uppbeat](https://uppbeat.io/blog/royalty-free-and-copyright-free-music/copyright-safe-music-for-shorts-reels-and-tiktok-how-to-post-without-claims-or-mutes)) |
| Pixabay Music | Gratis | ⚠️ A veces genera reclamos | Evitar en videos monetizados |

**Reglas:**
- "Libre de regalías" no significa "sin reclamos". Guarda el comprobante de la licencia de cada pista que uses.
- Música suave e instrumental, debajo de la voz (aprox. −18 a −24 dB respecto a la voz).

## Grabación de voz (si grabas tu voz real)
| Herramienta | Costo | Uso |
|---|---|---|
| **Celular** (Grabadora de iPhone / Android) | $0 | Suficiente si grabas en un clóset o cuarto con ropa y cortinas (sin eco), a 15–20 cm del teléfono |
| **Audacity** (PC/Mac) | $0, código abierto | Grabar y limpiar: reducción de ruido, normalización, cortes ([referencia](https://www.guideflow.com/blog/voiceover-software)) |
| Adobe Podcast "Enhance Speech" (web) | Plan gratis con límites | Hace que una grabación casera suene a estudio. Verifica los límites vigentes |
| ElevenLabs Voice Isolator | Incluido en el plan | Quita el ruido de fondo |
| Micrófono USB (opcional, más adelante) | ~USD 30–60 | Solo si el celular no alcanza |

Entrega: archivo WAV o M4A, una toma por guion. Los errores no importan: yo corto las pausas.

## Música tipo "La Psicología Invisible"
El estilo del nicho es **piano suave, ambient o lo-fi tranquilo**, sin voz, a volumen bajo.

**Opción A: Biblioteca de audio de YouTube (gratis)**
- En YouTube Studio → Biblioteca de audio, filtra por *Estado de ánimo: Calma*, *Género: Ambient / Clásica / Piano* y *Atribución: no se requiere*.
- Descarga 3 a 5 pistas y súbelas a `audio/musica/` junto con una nota del nombre y la licencia de cada una.
- ⚠️ Fuera de YouTube (TikTok, Instagram) depende de la licencia de cada pista: algunas piden atribución o no permiten otros usos ([guía](https://usethirdchair.com/blog/can-you-use-youtube-audio-library-music-on-instagram), [comparativa](https://www.digitalapplied.com/blog/social-video-music-rights-platform-comparison)).

**Opción B: música propia con ElevenLabs Music (recomendada si contratas Starter)**
- Generas una vez 3 loops de ~1 minuto (piano calmado, ambient pensativo, lo-fi cálido) y los reutilizas en todos los videos.
- Son pistas generadas con tu plan y con uso comercial, así que no debería haber reclamos de terceros ni dudas entre plataformas. Gasta ~900 créditos por minuto, pero solo se hace una vez.

**Opción C: música nativa de TikTok e Instagram** (desde la app; en cuentas de empresa, la biblioteca comercial). Solo sirve dentro de esa plataforma.

## Edición (Claude)
Claude puede armar el video completo con herramientas gratuitas (ffmpeg + transcripción automática local):
1. Une los clips de Gemini en el orden del guion.
2. Pone tu voz y la música debajo; la música baja sola cuando hablas.
3. **Subtítulos automáticos palabra por palabra**, con la palabra clave resaltada, transcritos de tu voz.
4. Textos en pantalla: la idea principal en el primer cuadro, listas numeradas y el cierre.
5. Exporta en 9:16 (1080×1920) para TikTok, Reels y Shorts, y en 16:9 para YouTube largo.
6. Miniatura con la plantilla del canal.
Tú revisas el video final antes de publicarlo.
