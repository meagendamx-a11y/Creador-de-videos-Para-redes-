# Memoria del proyecto para Claude

## Contexto
- El fundador de **Agenda PSI** (agendapsi.mx) conecta pacientes con psicólogos verificados en México.
- Este repo es para crear un **canal de divulgación psicológica con personaje animado** que atraiga público hacia la plataforma **sin publicidad directa**.
- Responde siempre en **español**.
- Estilo de trabajo del fundador:
  - Va paso a paso.
  - Quiere un enfoque práctico, con cambios mínimos y la solución más simple que funcione.
  - Antes de diseñar quiere evidencia y buenas referencias.
  - Quiere el **mínimo presupuesto**: primero lo que puede hacer Claude gratis, y si no alcanza, proveedores externos.

## Antes de trabajar, lee
1. `investigacion/00_SINTESIS.md`: conclusiones de la investigación de audiencia.
2. `docs/plan_de_trabajo.md`: en qué etapa vamos.
3. `docs/decisiones.md`: lo ya decidido. No lo reabras sin una razón nueva.
4. `docs/reglas_contenido.md`: reglas obligatorias para todo guion o video.

## Canal
**La Psicotidiana** (@lapsicotidiana) · "Psicología para la vida de todos los días." Archivos de marca en `marca/`.

## Personaje oficial
**El Observador**: personaje por defecto en todos los videos (neutro, o hombre cuando haga falta). **La Observadora**: solo cuando el fundador pida un personaje mujer. Ficha y rasgos canónicos en `personaje/observer/README.md`. Nunca unir los ojos con una línea (evita el parecido con Baymax). El video lo genera Gemini (`personaje/observer/PROMPTS_GEMINI.md`).

## Reglas no negociables
- **El personaje es un guía de ficción y nunca se presenta como psicólogo.**
  - YouTube no monetiza a personajes de IA que dan consejos de salud.
  - Los guiones los firma un psicólogo real con cédula.
- Sin guiones con muletillas de IA ("no es esto, sino aquello", etc.).
- Nada de convertir en enfermedad los rasgos normales, ni de diagnosticar.
- En temas de crisis, siempre poner la Línea de la Vida (800 911 2000) y el 911.
- Un personaje y un estilo constantes. Evitar la estética de "IA genérica" (3D pulido, pseudo-Ghibli, sepia).
- **Secretos:**
  - Nunca escribirlos en archivos ni pedirlos por chat. Se usa `request_credential`.
  - Apify ya está configurado en el entorno, en `api.apify.com`, inyectado por el proxy.
- **Material de terceros** (miniaturas, fotogramas) solo para estudio local. No se versiona.
- No tocar `.env` ni credenciales. Cambios grandes o de lógica de negocio: explicar las opciones y esperar aprobación.

## Flujo de git
- Rama de trabajo: `claude/brave-hawking-0mrvb8`.
- Hacer commit y push al terminar cada bloque. No crear PR salvo que se pida.

## Pipeline técnico disponible (gratis)
- **Personaje en SVG generado por código:** ver `personaje/exploracion/*.html` y `helpers.js`.
- **Render:** Playwright y Chromium (preinstalados) producen fotogramas; ffmpeg los convierte a MP4 1080×1920.
- **Investigación:** `yt-dlp --js-runtimes node` (si YouTube pide verificación anti-bot, ir más lento o agregar `--ignore-no-formats-error` para comentarios), `pytrends` y el autocompletado de Google en `suggestqueries.google.com`.
