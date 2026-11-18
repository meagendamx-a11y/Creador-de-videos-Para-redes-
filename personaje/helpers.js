// Helpers compartidos de rostro/extremidades para todos los conceptos.
const INK = '#2B2B33', SW = 4.5;

function eyes(cx, cy, gap, mood) {
  const l = cx - gap, r = cx + gap;
  let s = '';
  if (mood === 'feliz') {
    // ojos cerrados en arco = sonrisa con los ojos
    s += `<path d="M${l-9},${cy+2} Q${l},${cy-9} ${l+9},${cy+2}" fill="none" stroke="${INK}" stroke-width="${SW}" stroke-linecap="round"/>`;
    s += `<path d="M${r-9},${cy+2} Q${r},${cy-9} ${r+9},${cy+2}" fill="none" stroke="${INK}" stroke-width="${SW}" stroke-linecap="round"/>`;
    s += `<ellipse cx="${l-6}" cy="${cy+16}" rx="9" ry="5" fill="#F29C9C" opacity=".55"/>`;
    s += `<ellipse cx="${r+6}" cy="${cy+16}" rx="9" ry="5" fill="#F29C9C" opacity=".55"/>`;
    return s;
  }
  const dy = mood === 'triste' ? 4 : 0;          // mirada hacia abajo
  const dx = mood === 'pensativo' ? 4 : 0;        // mirada de lado
  const ry = mood === 'ansioso' ? 8.5 : 7;        // ojos más abiertos
  s += `<ellipse cx="${l+dx}" cy="${cy+dy}" rx="5.5" ry="${ry}" fill="${INK}"/>`;
  s += `<ellipse cx="${r+dx}" cy="${cy+dy}" rx="5.5" ry="${ry}" fill="${INK}"/>`;
  s += `<circle cx="${l+dx+1.8}" cy="${cy+dy-2.5}" r="1.8" fill="#fff"/>`;
  s += `<circle cx="${r+dx+1.8}" cy="${cy+dy-2.5}" r="1.8" fill="#fff"/>`;
  // cejas: son las que más comunican emoción en un personaje sin boca grande
  const by = cy - 17;
  const brow = {
    neutral:   [[l-8,by,l+8,by],[r-8,by,r+8,by]],
    triste:    [[l-8,by+4,l+8,by-4],[r-8,by-4,r+8,by+4]],
    pensativo: [[l-8,by,l+8,by-3],[r-8,by-6,r+8,by-2]],
    ansioso:   [[l-8,by+2,l+8,by-5],[r-8,by-5,r+8,by+2]],
  }[mood];
  brow.forEach(([x1,y1,x2,y2]) => s += `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="${INK}" stroke-width="${SW-0.5}" stroke-linecap="round"/>`);
  if (mood === 'ansioso') s += `<path d="M${r+22},${cy-20} q4,8 0,12 q-4,-4 0,-12z" fill="#8EC5E8" stroke="${INK}" stroke-width="2"/>`;
  return s;
}

function mouth(cx, cy, mood) {
  const d = {
    neutral:   `M${cx-6},${cy} Q${cx},${cy+3} ${cx+6},${cy}`,
    triste:    `M${cx-7},${cy+3} Q${cx},${cy-4} ${cx+7},${cy+3}`,
    feliz:     `M${cx-9},${cy-1} Q${cx},${cy+9} ${cx+9},${cy-1}`,
    pensativo: `M${cx-4},${cy+1} L${cx+6},${cy-1}`,
    ansioso:   `M${cx-8},${cy+1} q4,-4 8,0 q4,4 8,0`,
  }[mood];
  return `<path d="${d}" fill="none" stroke="${INK}" stroke-width="${SW-1}" stroke-linecap="round"/>`;
}

// brazos según emoción (hombro izq/der dados)
function arms(lx, ly, rx, ry, mood, color) {
  const A = {
    neutral:   [`M${lx},${ly} q-22,18 -18,46`, `M${rx},${ry} q22,18 18,46`],
    triste:    [`M${lx},${ly} q-10,26 -6,58`, `M${rx},${ry} q10,26 6,58`],
    feliz:     [`M${lx},${ly} q-30,-10 -34,-44`, `M${rx},${ry} q30,-10 34,-44`],
    pensativo: [`M${lx},${ly} q-22,18 -18,46`, `M${rx},${ry} q20,10 -4,-26`],
    ansioso:   [`M${lx},${ly} q-14,10 6,24`, `M${rx},${ry} q14,10 -6,24`],
  }[mood];
  return A.map(d => `<path d="${d}" fill="none" stroke="${INK}" stroke-width="13" stroke-linecap="round"/>
                     <path d="${d}" fill="none" stroke="${color}" stroke-width="6.5" stroke-linecap="round"/>`).join('');
}

function legs(cx, y, color, spread=18) {
  return [-spread, spread].map(o =>
    `<path d="M${cx+o},${y} l${o>0?3:-3},26" stroke="${INK}" stroke-width="13" stroke-linecap="round"/>
     <path d="M${cx+o},${y} l${o>0?3:-3},26" stroke="${color}" stroke-width="6.5" stroke-linecap="round"/>`).join('');
}

const FRONT = m => m==='pensativo'||m==='ansioso';
const shadow = (cx,y,w) => `<ellipse cx="${cx}" cy="${y}" rx="${w}" ry="8" fill="#000" opacity=".08"/>`;

