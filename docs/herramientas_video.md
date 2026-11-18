# Herramientas de video con IA (revisión nov-2026)

> Precios y modelos cambian cada mes. Verifica en la página oficial antes de pagar.

## Lo que hay hoy
| Plataforma / modelo | Fuerte en | Personaje consistente | Precio orientativo |
|---|---|---|---|
| **Google Gemini / Flow (Veo, Nano Banana)** | Ecosistema completo: imagen de referencia, video, Flow para escenas | "Ingredients to Video": mantiene la identidad entre escenas usando imágenes de referencia ([Google](https://blog.google/innovation-and-ai/technology/ai/veo-3-1-ingredients-to-video/)) | AI Plus USD 4.99/mes, AI Pro USD 19.99 (1,000 créditos). Flow da ~50 créditos gratis al día y la app de Gemini ~3 videos al día ([fuentes](https://www.techbloat.com/how-much-do-ai-video-generators-cost-for-youtube-creators-pricing-compared-november.html), [guía](https://note.com/reika0830/n/nfb9a58008400?hl=en)) |
| **Kling 3.0** | Mejor relación calidad/precio; en votaciones a ciegas ya supera a Veo 3.1 | "Elements" / referencias de personaje | ~USD 0.10 por segundo ([MarkTechPost](https://www.marktechpost.com/2026/11/13/best-ai-video-generation-models-2026/)) |
| **Seedance 2.5 (ByteDance)** | #1 en imagen→video en votaciones a ciegas | Buena desde la imagen inicial | El más caro. Se usa vía terceros (fal.ai, Higgsfield) |
| **Wan 3.0 (Alibaba)** | #1 en texto→video con audio; tiene versión de pesos abiertos | Media | ~USD 0.20 por segundo |
| **Runway Gen-4.5** | Control de dirección y edición | Referencias de personaje | Standard USD 15/mes; ~USD 1.44 por clip de 5 s |
| **Higgsfield** (agregador) | Un solo lugar para Kling, Seedance y otros | Depende del modelo | Desde ~USD 15/mes |

⚠️ Según un explicador de terceros, Flow retira Veo 3.1 Fast y Quality y Omni Flash 1.1 el **5-dic-2026** y los cambia por modelos nuevos ([nhimg](https://nhimg.org/google-gemini-omni-and-flow-explained)). Hay que confirmarlo en la página oficial. No cambia la recomendación, pero sí los nombres de los modelos que vas a ver.

Ninguna fuente compara la consistencia en animación **2D simple** como la nuestra. Hay que probarla con una prueba propia.

## Decisión (18-nov-2026)
Empezamos con **Gemini** (suscripción barata). Las demás quedan como alternativas por si Gemini no mantiene bien al personaje o sale caro.

## Recomendación
1. **Gemini/Flow es una opción sólida para empezar.** Tiene créditos gratis diarios, la herramienta "Ingredients" sirve justo para mantener el personaje, y el personaje ya nació en Gemini.
2. **No conviene casarse con un solo proveedor:** los rankings cambian cada mes. Lo que no cambia es nuestra **referencia canónica** (imagen + ficha), y esa funciona con cualquier herramienta.
3. **No todo necesita IA de video.** Muchas piezas (personaje que parpadea, aparece un objeto, texto, zoom) las puedo animar gratis por código a partir del SVG. La IA de video se usa solo en las escenas con acción real: caminar, sentarse, manipular objetos.

## Prueba A/B antes de pagar (gratis o casi)
Mismas **3 escenas**, misma imagen de referencia y mismo prompt en **Gemini/Flow** y **Kling** (los dos tienen créditos gratis):
1. Sentado en un banco, pensativo, con una burbuja de "?".
2. Mira por una lupa y frunce el ceño.
3. Camina, se detiene, suspira y sonríe.

| Criterio (1–5) | Gemini/Flow | Kling |
|---|---|---|
| El personaje no cambia (ojos separados, proporciones, color) | | |
| Se ve 2D, hecho a mano, no 3D | | |
| Movimiento natural | | |
| Respeta el prompt | | |
| Costo por clip útil | | |

Gana el que tenga más clips **utilizables sin corregir**.

## Flujo de trabajo con cualquier proveedor
1. **Referencia canónica:** `personaje/observer/referencia_gemini_conceptos_observer.jpg` + la ficha de `PROMPTS_GEMINI.md`.
2. **Fotograma clave por escena:** genera primero la imagen fija de la escena (Gemini/Nano Banana) con el personaje en pose, revísala y apruébala.
3. **Imagen → video:** anima ese fotograma (5 a 8 s, una acción por clip, cámara fija).
4. **Edición (Claude):** unir clips, voz, subtítulos, textos, música y miniatura.
5. **Control de calidad:** descartar cualquier clip donde el personaje cambie.
