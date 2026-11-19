# Registro de decisiones

Formato: fecha · decisión · por qué · estado.

| Fecha | Decisión | Por qué | Estado |
|---|---|---|---|
| 2026-11-18 | El canal **no** menciona a Agenda PSI en el contenido. El puente es indirecto: link en la bio y temas como costo, cómo elegir psicólogo y la primera sesión | Una plataforma como protagonista rinde poco (un competidor tiene una mediana de 675 vistas). La gente desconfía de la venta | ✅ Decidido |
| 2026-11-18 | Presupuesto mínimo: primero producción gratuita (vector por código), proveedores pagados solo si hace falta | Indicación del fundador | ✅ Decidido |
| 2026-11-18 | Personaje **tipo persona estilizada**, no animal ni objeto | Preferencia del fundador. Que el personaje sea "alguien" ayuda a que la gente se identifique | ✅ Decidido |
| 2026-11-18 | Se descartan Brote, Gota, Piedrita, Nube, Ajolote y los demás animales u objetos | Muy simples para el fundador. Además Psych2Go ya tiene el brote en la cabeza y Pictoline el cerebro con cara | ✅ Decidido |
| 2026-11-18 | El acabado debe ser pulido: líneas de color, degradado suave, sombra interna, luz y escenario | La primera exploración se veía "demasiado simple". La prueba `pulido.png` mostró que el vector gratis puede verse profesional | ✅ Decidido |
| 2026-11-18 | Investigar a fondo antes de diseñar: 6 agentes y Apify (USD 3.74) | Diseñar con evidencia | ✅ Hecho |
| 2026-11-18 | El personaje es guía de ficción; el conocimiento lo firma un psicólogo real con cédula | Política de YouTube del 16-jul-2026 sobre personajes de IA y salud | ✅ Decidido |
| 2026-11-18 | ~~Dirección "Mechón"~~ **descartada por el fundador** (no le gustó). Antes: Dirección de personaje recomendada: **"Mechón"** (rasgo firma que también expresa la emoción) + paleta mexicana + acabado hecho a mano | Benchmark visual (informe 06): solo 3 de 6 direcciones pasan la prueba de silueta; ningún personaje humano del benchmark tiene un rasgo que identifique y exprese a la vez | ❌ Descartado |
| 2026-11-18 | Material de terceros fuera del repo (`.gitignore`) | Derechos de autor | ✅ Hecho. ⚠️ Aún queda en el historial; limpiarlo requiere force push y la aprobación del fundador |

| 2026-11-18 | **Personaje oficial: "El Observador" (The Observer · Simple, generado con Gemini).** Ficha en `personaje/observer/README.md` | Lo eligió el fundador. Es abrazable y calmado (la lógica de Baymax), es "alguien" universal y cuenta historias con el cuerpo y objetos | ✅ Decidido |
| 2026-11-18 | Reparto: Claude hace diseño, guiones y revisión; **Gemini genera el video** a partir de la referencia canónica | Indicación del fundador | ✅ Decidido |
| 2026-11-18 | **Video: empezar con Gemini** (suscripción barata) y guardar las alternativas: Kling, Seedance, Runway, Higgsfield | El personaje nació en Gemini, tiene créditos diarios y la función "Ingredients" para la consistencia. Ver `docs/herramientas_video.md` | ✅ Decidido |
| 2026-11-18 | Flujo de video: imagen fija por escena → imagen a video (Gemini) → Claude arma voz, subtítulos, música y miniatura | Controlar la consistencia antes de gastar en video | ✅ Decidido |
| 2026-11-18 | **Voz: ElevenLabs Starter, clonación instantánea de la voz del fundador.** Texto → audio listo. Opcional: Claude genera el audio vía API si se guarda la clave con el formulario seguro | El fundador quiere solo pasar texto y recibir el audio | ✅ Decidido |
| 2026-11-18 | **Música:** piano suave o ambient, volumen bajo, de la biblioteca de YouTube o de las bibliotecas de TikTok/IG. El fundador descarga las pistas; Claude indica el estilo | Gratis y con bajo riesgo de reclamos. Guardar la licencia de cada pista | ✅ Decidido |
| 2026-11-18 | **Edición: Claude** (clips + voz + música + subtítulos + textos + miniatura). El fundador aprueba guion, imágenes y el video final | Reparto acordado | ✅ Decidido |
| 2026-11-18 | **Elenco:** **El Observador** es el personaje por defecto (neutro, o hombre cuando haga falta). **La Observadora** se usa solo cuando el fundador pida un personaje mujer. Mismo estilo; solo cambian el pelo y la ropa | Indicación del fundador. Las escenas de pareja rinden mucho (informe 07) | ✅ Decidido |
| 2026-11-18 | **Formato de edición fijo** (aprobado con el video 001): 9:16 a pantalla completa, recorte centrado en la persona, personaje subido ~340 px, franja inferior desenfocada para los subtítulos, títulos en caja amarilla arriba, firma al pie, música que baja cuando hay voz. Script: `produccion/editar.py` | Aprobado por el fundador | ✅ Decidido |
| 2026-11-18 | **Sin firma en pantalla.** El crédito del psicólogo (nombre y cédula) va solo en la descripción del video | Preferencia visual del fundador. La descripción sigue cumpliendo con mostrar al experto detrás | ✅ Decidido |
| 2026-11-18 | Música: biblioteca compartida en `audio/musica/` con registro obligatorio de licencias (`LICENCIAS.md`). Primera pista: "Calma Suave", generada con ElevenLabs Music | Evitar reclamos de derechos | ✅ Decidido |
| 2026-11-19 | **Nombre del canal: "Psicología Cotidiana"** (corrección del fundador; antes se había anotado "La Psicotidiana" por error). Frase: "Psicología para la vida de todos los días." | Transmite "psicología del día a día, para todos" de forma clara | ✅ Decidido · ⚠️ YouTube rechazó el nombre al crear el canal y propone el identificador @psicologiacotidiana-m9f (el limpio parece reservado). Alternativas: canal de marca, nombre temporal y cambio posterior, o variante (@psicologiacotidianamx libre) |
| 2026-11-19 | Identidad visual: foto de perfil `marca/perfil_1080_cerrado.png`, banner `marca/banner_youtube_Psicologia_Cotidiana_2560x1440.png`, azul cielo `#CFE6F5`, título navy `#2E3A55` con "Cotidiana" en azul `#3F7FB5`, tipografía Nunito | Contraste y diferenciación (sin verde salvia) | ✅ Decidido |

## Pendientes de decisión del fundador
- Si El Observador lleva un acento distintivo (bufanda, color) para diferenciarse de Baymax y del muñeco de stock. Ver `personaje/observer/variantes.png`.
- Psicólogo responsable de firmar y revisar los guiones.
- Si se limpia el historial de git de imágenes de terceros.
- Consultar a un abogado si el aviso de publicidad de COFEPRIS aplica cuando se promocionen citas.
