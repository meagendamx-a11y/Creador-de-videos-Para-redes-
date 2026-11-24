# Estado de los videos

Cada carpeta contiene `guion.md` (texto para ElevenLabs y publicación), `prompts_gemini.md` (cómo pedir el video a la IA), `edicion.json` (configuración del editor), `assets/` (voz y clips), `render/` (video final) y `publicacion/` (miniatura de YouTube y portada vertical para IG/TikTok; guía en `docs/guia_miniaturas.md`). Textos de publicación y calendario: `PUBLICACION_semana1.md`.
Para editar: `python3 produccion/editar.py contenido/<carpeta>/edicion.json`

| # | Tema | Duración | Audio | Clips | Video final |
|---|---|---|---|---|---|
| 001 | Ensayan conversaciones en su cabeza (v2) | 27 s | ✅ | ✅ (regadera, espejo, recámara) | ✅ |
| 002 | Para quien siempre dice "estoy bien" | 15 s | ✅ | ✅ | ✅ |
| 003 | ¿No puedes dormir? Respiración práctica | 26 s | ✅ | ✅ | ✅ |
| 004 | Las personas que prefieren estar solas | 17 s | ✅ | ✅ | ✅ |
| 005 | ¿Psicólogo o psiquiatra? (sin recorte) | 19 s | ✅ | ✅ | ✅ |
| 006 | ¿Por qué te falta el aire cuando estás nervioso? | 33 s | ✅ | ✅ (A, B, C) | ✅ |
| 007 | TDAH en adultos: lo que se confunde con flojera | ~30 s | ✅ El fundador lo tiene | ⏳ (prompts listos) | ⏳ |
| 008 | La ley del hielo: pausa o castigo (con La Observadora) | ~30 s | ✅ El fundador lo tiene | ⏳ (prompts listos) | ⏳ |
| 009 | Ir a terapia es más que hablar | ~30 s | ⏳ | ⏳ | ⏳ |
| 010 | ¿Qué es un enfoque terapéutico? | ~45 s | ⏳ | ⏳ | ⏳ |
| 011 | Ansiedad: técnica 5-4-3-2-1 | 10–15 s | ✅ Audio · prompts listos | ⏳ | ⏳ |
| 012 | Para quien se exige demasiado | 10–15 s | ✅ Audio · prompts listos | ⏳ | ⏳ |
| 013 | Las personas que necesitan ruido para dormir | 10–15 s | ✅ Audio · prompts listos | ⏳ | ⏳ |

Pendiente general: el nombre y la cédula del psicólogo para las descripciones.

Temas descartados por el fundador: autismo en mujeres (delicado), primera sesión de terapia (no convenció el enfoque), personas que piden perdón por todo.

## Siguiente paso (acordado el 18-nov-2026)
1. **Terminar el 001:** faltan las escenas E3–E7. Los prompts están en `001_ensayan_conversaciones/prompts_gemini.md` (E1 se puede rehacer con fondo 2D y sin sepia).
2. Después, los videos **006, 007, 008, 009 y 010**. Los audios ya están en ElevenLabs. Los prompts del 006–008 ya existen; los del 009 y 010 se escriben con los tiempos del audio.
Cuando el fundador lo pida, se le entregan los prompts completos o los que falten de cada video.
