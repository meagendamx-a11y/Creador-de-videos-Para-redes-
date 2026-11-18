# Plan de trabajo

El orden lo acordó el fundador: personaje, luego voz, luego psicólogo responsable, luego guiones con retroalimentación, luego piloto, y al final publicación diaria conectada a las cuentas.

## Etapa 1 · Investigación de audiencia ✅
Entregables: `investigacion/00_SINTESIS.md` + informes 01–07 + `investigacion/datos/`.

## Etapa 2 · Personaje 🔄
**Objetivo:** un personaje humano estilizado, icónico y constante, que se pueda animar gratis por código.
- [ ] Hoja de modelo de **"Mechón"** con 2 alternativas, con acabado pulido y una paleta propia.
- [ ] Prueba de silueta y de avatar a 48 px, para comprobar que se reconoce en miniatura.
- [ ] El fundador elige una dirección. *(decisión)*
- [ ] Hoja final:
  - vistas: frente, 3/4, perfil y espalda;
  - 12 expresiones, incluidos los estados del mechón;
  - 6 bocas para sincronizar con la voz;
  - 8 poses;
  - 2 o 3 personajes secundarios.
- [ ] Armado en piezas (rig SVG) para animarlo, con una prueba de 10 s.
- [ ] Opcional: validar las siluetas con 30 a 50 personas del público ("¿a qué canal te recuerda?").
- [ ] Guía de estilo: paleta, línea, textura, tipografía y plantilla de miniatura. Compromiso de no rediseñar en 12 meses.

## Etapa 3 · Voz ⏳
- [ ] Definir quién pone la voz: humana, mexicana, cálida y pausada. *(decisión del fundador)*
- [ ] Probar la grabación: micrófono, sala y limpieza de audio con herramientas gratuitas.
- [ ] Sincronizar la boca del personaje con el audio.
- Nota: si en algún momento se clona la voz, solo con consentimiento escrito de la persona.

## Etapa 4 · Psicólogo responsable y protocolo ⏳
- [ ] Elegir al psicólogo o psicóloga que firma. Se pueden rotar psicólogos de la red de Agenda PSI. *(decisión)*
- [ ] Flujo de revisión de guiones: quién revisa, en cuánto tiempo y con qué checklist (`reglas_contenido.md`).
- [ ] Protocolo de moderación y crisis: respuestas tipo y escalamiento.
- [ ] Solicitar el panel de "Fuente de salud" de YouTube.
- [ ] Consultar a un abogado: COFEPRIS y aviso de privacidad.

## Etapa 5 · Guiones y temas ⏳
Claude propone guiones y el fundador da retroalimentación. Iteramos.
- [ ] Banco de 30 temas priorizados (síntesis §8): ansiedad, neurodivergencia en adultos, apego y pareja, "La psicología de las personas que…" en Shorts, infancia y crianza, acceso a terapia, y actualidad mexicana.
- [ ] Plantillas de guion por tipo de pieza (síntesis §7): para guardar (60–90 s), para compartir (30–45 s), escena o historia, video largo (8–10 min) y carrusel.
- [ ] Calendario editorial con las fechas clave: 2-abr, 20-may, 10-oct, regreso a clases.

## Etapa 6 · Producción ⏳
- [ ] Pipeline: guion → voz → animación SVG por escenas → subtítulos → render MP4 1080×1920 (y 16:9 para YouTube largo).
- [ ] Biblioteca de escenarios y objetos reutilizables.
- [ ] Plantilla de miniatura.
- [ ] Meta: producir una pieza al día con revisión humana.

## Etapa 7 · Piloto ⏳
- [ ] 6 a 8 piezas con la mezcla semanal: 2 para guardar, 1 para compartir, 1 de humor o actualidad, 1 carrusel.
- [ ] Medir, por pieza, compartidos y guardados (meta: 1.5% o más cada uno), retención y comentarios.
- [ ] Ajustar y luego subir a ~1 video al día.

## Etapa 8 · Publicación conectada ⏳
Conectar YouTube, Instagram y TikTok para programar y publicar desde aquí. Antes de implementar, **validar la documentación oficial vigente**, porque los requisitos cambian:
- **YouTube:** YouTube Data API v3 con OAuth del canal (subida de videos).
- **Instagram:** Instagram Graph API. Requiere cuenta profesional vinculada y una app de Meta.
- **TikTok:** Content Posting API. Requiere una app aprobada por TikTok; las apps sin auditar pueden tener restricciones de publicación.
- Las credenciales se guardan siempre con el formulario seguro, nunca en el repo.
- Hay que decidir si la publicación es automática o con aprobación humana de cada pieza. *(Recomendado: con aprobación.)*
