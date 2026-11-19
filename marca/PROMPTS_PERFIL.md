# Imagen de perfil y banner (YouTube, TikTok, Instagram, Facebook)

## Medidas
| Pieza | Subir en | Cómo se ve | Zona segura |
|---|---|---|---|
| Foto de perfil (todas las redes) | **1080 × 1080 px** | Recortada en círculo, muy pequeña (40–100 px) | Personaje dentro del círculo central (~70% del ancho) |
| Banner de YouTube | **2560 × 1440 px** | TV: completo · Celular: solo la franja central | **1546 × 423 px al centro** |

**Regla:** pedir a Gemini las imágenes **sin texto**. Claude agrega el nombre del canal con la tipografía del canal (Nunito) para que no salga con errores.
**Color de marca propuesto:** azul cielo suave `#CFE6F5` con blanco cálido `#FBF8F3` y línea `#4A4A5C`. Evitar el verde salvia, que es el color de La Psicología Invisible.

## Prompt 1 · Foto de perfil
Adjunta `personaje/observer/referencia_gemini_conceptos_observer.jpg`.
```
Create a SQUARE 1:1 profile picture, 1080x1080 px, for a psychology education channel.
CHARACTER: "The Observer" exactly as in the attached reference — warm white soft body, thin soft charcoal outline, round head, two small SEPARATE dot eyes, short eyebrows, tiny mouth. Never connect the eyes with a line.
COMPOSITION: head and upper body only, centered, facing the camera, with a warm curious expression (one eyebrow slightly raised, small smile), one hand gently raised in a small wave. The character must fit completely inside a centered circle that is 70% of the image width (the image will be cropped to a circle), with comfortable margin around the head.
BACKGROUND: solid flat soft sky blue (#CFE6F5), with a subtle slightly lighter circle behind the character. No other objects.
STYLE: flat 2D hand-drawn illustration, clean lines, high contrast between the white character and the blue background so it reads well at a tiny size. NOT 3D, no sepia, no gradients except the subtle circle.
NO text, NO letters, NO logos.
```
Variante (alternativa a probar): misma imagen, pero sosteniendo una pequeña lupa junto al ojo (rasgo de "El Observador").

## Prompt 2 · Banner de YouTube
```
Create a WIDE banner image, 2560x1440 px (16:9), for a YouTube psychology education channel.
CHARACTER: "The Observer" exactly as in the attached reference (warm white soft body, thin charcoal outline, two small SEPARATE dot eyes, never connected).
IMPORTANT LAYOUT: only the CENTER horizontal strip (1546x423 px in the middle of the image) is visible on phones. Place the character inside that central strip, on the RIGHT side of it, full body or from the waist up, looking curiously through a small magnifying glass. Leave the LEFT half of the central strip completely EMPTY (plain background) for the channel name, which will be added later.
BACKGROUND: soft flat sky blue (#CFE6F5) with a few very subtle simple doodles in lighter blue spread across the whole image (small thought bubbles, a heart, a question mark, swirls), sparse and calm. The outer areas (top, bottom, sides) should continue the same background so it looks good on TV.
STYLE: flat 2D hand-drawn illustration, calm and warm, NOT 3D, no sepia.
NO text, NO letters, NO logos.
```

## Pendiente
- **Nombre del canal** (y frase corta, p. ej. "Psicología cotidiana, explicada simple").
- Claude compone el texto sobre el banner y genera las versiones finales.

## Banner · versión 2 del prompt (corrige la v1)
En la v1, Gemini dibujó la "franja central" como un recuadro negro y cortó el cuerpo del personaje en el borde. Este prompt lo evita:
```
Create a WIDE banner image, 2560x1440 px (16:9), for a YouTube psychology channel. Do NOT draw any frame, box, border or guide lines.
CHARACTER: "The Observer" exactly as in the attached reference (warm white soft body, thin charcoal outline, two small SEPARATE dot eyes, never connected).
LAYOUT: the character is SMALL (about 25% of the image height), FULL BODY visible from head to feet, standing on nothing (floating on the plain background), placed slightly right of the center, at the vertical middle of the image. It looks curiously through a small magnifying glass. The left-center area stays empty for the channel name.
BACKGROUND: one continuous soft flat sky blue (#CFE6F5) with a few very subtle light-blue doodles (thought bubbles, heart, question mark, swirls), sparse and calm, across the whole image.
STYLE: flat 2D hand-drawn illustration, NOT 3D, no sepia. NO text, NO letters, NO logos, NO frames.
```
