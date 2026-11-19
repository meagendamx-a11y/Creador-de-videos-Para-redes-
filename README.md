# Psicología Cotidiana · canal de divulgación psicológica (Agenda PSI)

Canal de redes (YouTube, TikTok, Instagram) con un **personaje animado propio** que divulga psicología cotidiana para público mexicano. El objetivo de negocio es atraer, de forma indirecta y sin publicidad, a personas que luego buscan terapia en [agendapsi.mx](https://agendapsi.mx).

> **Si es tu primera vez aquí:** lee `investigacion/00_SINTESIS.md` y después `docs/plan_de_trabajo.md`.

## Estado actual

| Etapa | Estado |
|---|---|
| 1. Investigación de audiencia | ✅ Terminada (nov-2026) |
| 2. Personaje | ✅ Elegido: **El Observador** (`personaje/observer/`). Pendiente: acento distintivo y nombre |
| 3. Voz | ⏳ Pendiente |
| 4. Psicólogo responsable y protocolo de crisis | ⏳ Pendiente |
| 5. Guiones y temas (con retroalimentación del fundador) | ⏳ Pendiente |
| 6. Producción: pipeline de animación y render | 🧪 Prueba técnica hecha |
| 7. Piloto, ~1 video al día | ⏳ Pendiente |
| 8. Publicación conectada a YouTube, Instagram y TikTok | 🟡 Canal de YouTube creado y configurado ("Psicología del día a día"); faltan TikTok e IG |

Detalle de cada etapa en `docs/plan_de_trabajo.md`.

## Mapa del repositorio

```
README.md                  ← este archivo
CLAUDE.md                  ← memoria y reglas para las sesiones con Claude
docs/
  plan_de_trabajo.md       ← etapas, entregables y pendientes
  herramientas_video.md    ← proveedores de video IA (Gemini elegido, alternativas)
  herramientas_audio.md    ← voz (clonación) y música libre de uso
  decisiones.md            ← registro de decisiones (qué, cuándo, por qué)
  reglas_contenido.md      ← reglas obligatorias: políticas, crisis, IA, firma clínica
investigacion/
  00_SINTESIS.md           ← ★ conclusiones de toda la investigación
  01…07_*.md               ← informes de detalle por frente
  datos/                   ← tablas procesadas (CSV/JSON) para re-analizar
  scripts/                 ← scripts usados (referencia; ver nota abajo)
  referencias_visuales/    ← bocetos propios (el material de terceros NO se versiona)
personaje/
  observer/                ← ★ PERSONAJE OFICIAL: ficha, referencias y prompts para Gemini
  mechon/                  ← dirección descartada
  exploracion/             ← primeras exploraciones (conceptos, estilos, prompts)
```

## Informes de investigación

| # | Informe | Muestra |
|---|---|---|
| 00 | **Síntesis** | Todo |
| 01 | Ronda 1: tendencias, rechazo a la IA, México, estilos | Estudios y prensa 2025-26 |
| 02 | Videos de YouTube que superan a su canal | 18,089 videos, 39 canales |
| 03 | Comentarios de la audiencia | 15,627 comentarios, 121 videos |
| 04 | Qué busca México (Google y YouTube) | 40 términos y ~16k sugerencias |
| 05 | TikTok e Instagram (fuentes públicas) | 2,229 TikToks, 38 cuentas |
| 06 | Benchmark visual de personajes | 22 referentes |
| 07 | TikTok e Instagram con datos de Apify | 378 TikToks, 170 posts, 2.1k comentarios |

## Herramientas

| Herramienta | Uso | Costo |
|---|---|---|
| Animación vectorial por código (SVG + Chromium/Playwright + ffmpeg) | Personaje y video | $0 |
| `yt-dlp` | Catálogos y comentarios de YouTube (a veces YouTube bloquea) | $0 |
| `pytrends` + autocompletado de Google/YouTube | Demanda de búsqueda en México | $0 |
| Apify (plan Free, USD 5/mes) | Datos de TikTok e Instagram | Se gastaron USD 3.74 en nov-2026 |

## Notas

- **Datos y privacidad:** las tablas no incluyen nombres de usuario de comentaristas. Los JSON crudos (con nombres de usuario) no se versionan. Tampoco se versionan miniaturas ni fotogramas de terceros, por derechos de autor (ver `.gitignore`).
- **Scripts:** son una referencia de método. Varios apuntan a rutas temporales de la sesión en que se escribieron, así que hay que ajustar las rutas para re-ejecutarlos.
- **Secretos:** nunca van al repo. La clave de Apify vive en el entorno seguro de la sesión, no en archivos.
