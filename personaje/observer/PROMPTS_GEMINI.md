# Prompts para Gemini: El Observador

Siempre **adjunta `referencia_gemini_conceptos_observer.jpg`** y pega la ficha. Así el personaje sale igual en cada pieza.

## 0. Ficha del personaje (pégala al inicio de cualquier prompt)
```
CHARACTER SHEET — "The Observer" (keep EXACTLY consistent):
- Soft, rounded humanoid. Round head SEPARATE from a soft pear-shaped body, same color.
- Warm white body (#FBF8F3) with subtle cool-grey shading (#D9D4CC); thin soft charcoal-grey outline (#4A4A5C).
- Face: two small SEPARATE dot eyes, short expressive eyebrows, tiny mouth. No nose, no hair, no clothes.
- NEVER connect the eyes with a line (must not resemble Baymax). Not a robot.
- Long soft noodle arms, short legs with rounded feet. Simple hands.
- Personality: curious, observant, empathetic, a little awkward. Fictional guide, not a doctor.
- Style: clean hand-drawn 2D illustration, flat soft shading, plain off-white background, minimal props.
- Avoid: 3D/Pixar render, anime, Ghibli, sepia tint, clutter, realistic hands, changing proportions.
```

## 1. SVG por capas (para que yo lo anime)
```
[CHARACTER SHEET]
Using the attached reference, write clean SVG code (viewBox 0 0 400 600) of The Observer standing in a neutral front pose.
Put each body part in its own named <g> group so it can be animated: head, eyebrow-left, eyebrow-right, eye-left, eye-right, mouth, body, arm-left, arm-right, leg-left, leg-right.
Use only simple paths/ellipses, the exact colors above, no embedded images, no gradients except one soft radial shading.
Return only the SVG code.
```
Pega aquí el código que te dé y lo guardo en `personaje/observer/observer.svg`.

## 2. Hoja de modelo (imagen)
```
[CHARACTER SHEET]
Create a character model sheet of The Observer matching the attached reference exactly:
row 1: front, 3/4, side, back views;
row 2: expressions — neutral, happy, sad, anxious, angry, surprised, thinking, calm;
row 3: poses — sitting on a stool thinking, looking through a magnifying glass, writing in a notebook, waving, hugging knees, walking.
Plain off-white background, evenly spaced, no text.
```

## 3. Video (Veo / Gemini)
```
[CHARACTER SHEET]
Animate The Observer from the attached reference. Vertical 9:16, 8 seconds, simple 2D hand-drawn animation style, gentle motion, plain off-white background, no text, no voice.
Scene: {DESCRIBE LA ESCENA, p. ej. "The Observer sits on a stool, rests chin on hand thinking, a small question-mark thought bubble appears, then it blinks and slowly smiles"}.
Keep the character's design, colors and proportions identical in every frame. Camera static.
```
Consejos:
- Pide escenas cortas de 5 a 8 s, una acción por clip. Yo armo la edición, los subtítulos y la voz.
- Deja libre la parte de arriba del encuadre para los textos.
- Si en algún clip el personaje cambia, por ejemplo con ojos unidos, otro grosor o nariz, se descarta.
