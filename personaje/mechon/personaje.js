// Generador del personaje "Mechón" en SVG (sin dependencias).
// Un solo modelo paramétrico => el personaje no puede "mutar" entre escenas (regla anti-IA-genérica).
// Coordenadas del personaje: 0..400 x 0..600, pies en y≈560, 3 cabezas de alto.

let _uid = 0;

const PALETAS = {
  coral: {
    nombre: 'Coral · índigo · teal',
    piel: '#F4A38C', pielSombra: '#DE8670', pielLuz: '#FFC6B4',
    pelo: '#2B2D5C', peloLuz: '#4A4E8F',
    ropa: '#2F8F83', ropaSombra: '#21706A', ropaLuz: '#4FB0A3',
    pantalon: '#2B2D5C', zapato: '#F2B544',
    linea: '#24264F', mejilla: '#F27C6B', fondo: '#FBF4EA', cuello: 'redondo',
  },
  terracota: {
    nombre: 'Terracota · cempasúchil · añil',
    piel: '#D9875F', pielSombra: '#BC6B46', pielLuz: '#ECA67F',
    pelo: '#2A2440', peloLuz: '#4A4170',
    ropa: '#E9A23B', ropaSombra: '#C9821F', ropaLuz: '#F6C46A',
    pantalon: '#2E3A6B', zapato: '#3E8E7E',
    linea: '#2A2440', mejilla: '#C95B45', fondo: '#F6EEE2', cuello: 'tortuga',
  },
  ventana: {
    nombre: 'Cabeza-ventana · noche · cielo',
    piel: '#EDB894', pielSombra: '#D39A76', pielLuz: '#F8D3B8',
    pelo: '#1E2140', peloLuz: '#3A3F70',
    ropa: '#1E2140', ropaSombra: '#141632', ropaLuz: '#343A6B',
    pantalon: '#3A3F70', zapato: '#FFD36B',
    linea: '#141632', mejilla: '#E98A78', fondo: '#EEF3F8', cuello: 'redondo',
    cielo: ['#8EC5E8', '#CFE7F7'],
  },
};

// Estados del mechón: el rasgo firma también es el "barómetro" emocional.
const MECHON = {
  calma:    'M200,82 C188,58 214,48 206,26 C202,14 212,6 220,10',
  feliz:    'M200,82 C184,58 228,50 210,24 C204,14 214,4 224,10',
  triste:   'M200,82 C216,78 240,86 248,112 C250,120 246,128 240,130',
  ansiedad: 'M200,82 L188,66 L212,56 L190,42 L214,30 L194,16 L210,6',
  enojo:    'M200,82 L200,46 L200,14',
  idea:     'M200,82 C194,52 232,42 228,22 C224,4 198,8 204,24 C208,34 220,28 216,20',
};

const BRAZOS = {
  // [izquierdo, derecho] como trayectorias hombro -> mano
  neutral:  ['M142,266 Q106,330 104,398', 'M258,266 Q294,330 296,398'],
  saludo:   ['M142,266 Q106,330 104,398', 'M258,266 Q318,250 322,170'],
  arriba:   ['M146,268 Q92,240 84,170', 'M254,268 Q308,240 316,170'],
  caidos:   ['M142,266 Q116,340 118,412', 'M258,266 Q284,340 282,412'],
  pecho:    ['M146,268 Q120,330 186,336', 'M254,268 Q280,330 214,336'],
  barbilla: ['M142,266 Q106,330 104,398', 'M258,266 Q300,330 226,236'],
};

function cara(p, mood, ventana) {
  const L = p.linea, ey = 178, lx = 172, rx = 228;
  let s = '';
  const ojo = (x, y, ry = 10, dx = 0, dy = 0) =>
    `<ellipse cx="${x + dx}" cy="${y + dy}" rx="7.5" ry="${ry}" fill="${L}"/>
     <circle cx="${x + dx + 2.6}" cy="${y + dy - 3.5}" r="2.6" fill="#fff"/>`;
  const ceja = (x1, y1, x2, y2) =>
    `<path d="M${x1},${y1} Q${(x1 + x2) / 2},${Math.min(y1, y2) - 3} ${x2},${y2}" fill="none" stroke="${L}" stroke-width="5" stroke-linecap="round"/>`;
  const arco = (x) => `<path d="M${x - 10},${ey + 3} Q${x},${ey - 9} ${x + 10},${ey + 3}" fill="none" stroke="${L}" stroke-width="5" stroke-linecap="round"/>`;

  switch (mood) {
    case 'feliz':
      s += arco(lx) + arco(rx) + ceja(160, 158, 182, 155) + ceja(218, 155, 240, 158);
      s += `<path d="M186,206 Q200,222 214,206 Q200,211 186,206Z" fill="${L}" stroke="${L}" stroke-width="3" stroke-linejoin="round"/>`;
      break;
    case 'calma':
      s += `<path d="M${lx - 9},${ey} Q${lx},${ey + 7} ${lx + 9},${ey}" fill="none" stroke="${L}" stroke-width="5" stroke-linecap="round"/>
            <path d="M${rx - 9},${ey} Q${rx},${ey + 7} ${rx + 9},${ey}" fill="none" stroke="${L}" stroke-width="5" stroke-linecap="round"/>`;
      s += ceja(160, 160, 182, 159) + ceja(218, 159, 240, 160);
      s += `<path d="M190,208 Q200,214 210,208" fill="none" stroke="${L}" stroke-width="4" stroke-linecap="round"/>`;
      break;
    case 'triste':
      s += ojo(lx, ey + 2, 9, 0, 2) + ojo(rx, ey + 2, 9, 0, 2);
      s += ceja(160, 160, 182, 152) + ceja(218, 152, 240, 160);
      s += `<path d="M190,214 Q200,206 210,214" fill="none" stroke="${L}" stroke-width="4" stroke-linecap="round"/>`;
      break;
    case 'ansiedad':
      s += ojo(lx, ey, 11) + ojo(rx, ey, 11);
      s += ceja(160, 156, 182, 150) + ceja(218, 150, 240, 156);
      s += `<path d="M186,210 q4,-4 7,0 q3,4 7,0 q4,-4 7,0 q3,4 7,0" fill="none" stroke="${L}" stroke-width="3.5" stroke-linecap="round"/>`;
      s += `<path d="M262,140 q7,12 0,18 q-7,-6 0,-18z" fill="#A9D6F2" stroke="${L}" stroke-width="2.5"/>`;
      break;
    case 'enojo':
      s += ojo(lx, ey + 2, 7) + ojo(rx, ey + 2, 7);
      s += `<path d="M160,158 L184,166" stroke="${L}" stroke-width="5.5" stroke-linecap="round"/><path d="M216,166 L240,158" stroke="${L}" stroke-width="5.5" stroke-linecap="round"/>`;
      s += `<path d="M190,212 L210,212" stroke="${L}" stroke-width="4" stroke-linecap="round"/>`;
      break;
    case 'idea':
      s += ojo(lx, ey, 10, 3, -3) + ojo(rx, ey, 10, 3, -3);
      s += ceja(160, 158, 182, 156) + ceja(218, 150, 240, 146);
      s += `<path d="M192,208 Q202,214 212,206" fill="none" stroke="${L}" stroke-width="4" stroke-linecap="round"/>`;
      break;
    default: // neutral
      s += ojo(lx, ey) + ojo(rx, ey);
      s += ceja(160, 158, 182, 157) + ceja(218, 157, 240, 158);
      s += `<path d="M190,208 Q200,213 210,208" fill="none" stroke="${L}" stroke-width="4" stroke-linecap="round"/>`;
  }
  // nariz mínima: es lo que hace que se lea "persona" y no "muñeco"
  s += `<path d="M201,186 q5,8 -3,11" fill="none" stroke="${L}" stroke-width="3.5" stroke-linecap="round" opacity=".7"/>`;
  if (mood !== 'enojo') s += `<ellipse cx="156" cy="200" rx="13" ry="7" fill="${p.mejilla}" opacity=".35"/><ellipse cx="244" cy="200" rx="13" ry="7" fill="${p.mejilla}" opacity=".35"/>`;
  return s;
}

/**
 * Devuelve el <g> del personaje.
 * opts: { paleta, mood, brazos, ventana, silueta }
 */
function personaje(opts = {}) {
  const p = PALETAS[opts.paleta || 'coral'];
  const mood = opts.mood || 'neutral';
  const brazos = BRAZOS[opts.brazos || 'neutral'];
  const ventana = !!opts.ventana;
  const id = 'm' + (++_uid);
  const L = p.linea;

  const torso = 'M154,238 Q200,229 246,238 Q266,246 268,272 L272,404 Q274,424 254,426 L146,426 Q126,424 128,404 L132,272 Q134,246 154,238 Z';
  const defs = `<defs>
    <radialGradient id="${id}skin" cx="38%" cy="32%" r="78%"><stop offset="0" stop-color="${p.pielLuz}"/><stop offset=".6" stop-color="${p.piel}"/><stop offset="1" stop-color="${p.pielSombra}"/></radialGradient>
    <linearGradient id="${id}ropa" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="${p.ropaLuz}"/><stop offset=".45" stop-color="${p.ropa}"/><stop offset="1" stop-color="${p.ropaSombra}"/></linearGradient>
    <linearGradient id="${id}pelo" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="${p.peloLuz}"/><stop offset=".5" stop-color="${p.pelo}"/></linearGradient>
    ${p.cielo ? `<linearGradient id="${id}cielo" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="${p.cielo[0]}"/><stop offset="1" stop-color="${p.cielo[1]}"/></linearGradient>` : ''}
    <clipPath id="${id}headclip"><circle cx="200" cy="162" r="80"/></clipPath>
    <clipPath id="${id}torsoclip"><path d="${torso}"/></clipPath>
    <filter id="${id}blur"><feGaussianBlur stdDeviation="10"/></filter>
    <!-- leve temblor de línea = sensación "hecho a mano" -->
    <filter id="${id}wob" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence type="fractalNoise" baseFrequency="0.04" numOctaves="2" seed="7"/><feDisplacementMap in="SourceGraphic" scale="2.2"/></filter>
  </defs>`;

  const brazo = (d) => `<path d="${d}" fill="none" stroke="${L}" stroke-width="36" stroke-linecap="round"/>
    <path d="${d}" fill="none" stroke="url(#${id}ropa)" stroke-width="27" stroke-linecap="round"/>`;
  const mano = (d) => {
    const m = d.match(/(-?[\d.]+),(-?[\d.]+)$/);
    return `<circle cx="${m[1]}" cy="${m[2]}" r="17" fill="url(#${id}skin)" stroke="${L}" stroke-width="5"/>`;
  };
  const frente = mood === 'ansiedad' || opts.brazos === 'pecho' || opts.brazos === 'barbilla';

  let g = `<g filter="url(#${id}wob)">`;
  // sombra de contacto
  g += `<ellipse cx="200" cy="566" rx="96" ry="12" fill="${L}" opacity=".12"/>`;
  // piernas y zapatos
  [170, 230].forEach((x) => {
    g += `<rect x="${x - 18}" y="404" width="36" height="148" rx="18" fill="${p.pantalon}" stroke="${L}" stroke-width="5"/>`;
  });
  g += `<path d="M138,560 Q136,538 168,538 Q186,538 188,560 Z" fill="${p.zapato}" stroke="${L}" stroke-width="5" stroke-linejoin="round"/>
        <path d="M262,560 Q264,538 232,538 Q214,538 212,560 Z" fill="${p.zapato}" stroke="${L}" stroke-width="5" stroke-linejoin="round"/>`;
  if (!frente) g += brazos.map(brazo).join('');
  // torso con sombra interna recortada y pliegues
  g += `<path d="${torso}" fill="url(#${id}ropa)" stroke="${L}" stroke-width="5" stroke-linejoin="round"/>
        <g clip-path="url(#${id}torsoclip)">
          <ellipse cx="300" cy="420" rx="120" ry="140" fill="${p.ropaSombra}" opacity=".55" filter="url(#${id}blur)"/>
          <path d="M156,404 q20,-14 40,-2 M214,410 q18,-12 36,0" fill="none" stroke="${p.ropaSombra}" stroke-width="4" stroke-linecap="round"/>
          <path d="M144,300 q-4,40 0,80" fill="none" stroke="${p.ropaLuz}" stroke-width="7" stroke-linecap="round" opacity=".6"/>
        </g>`;
  if (p.cuello === 'tortuga') g += `<rect x="166" y="222" width="68" height="30" rx="14" fill="${p.ropa}" stroke="${L}" stroke-width="5"/><path d="M172,236 h56" stroke="${p.ropaSombra}" stroke-width="3"/>`;
  else g += `<path d="M172,238 Q200,256 228,238" fill="none" stroke="${p.ropaSombra}" stroke-width="5" stroke-linecap="round"/>`;
  if (!frente) g += brazos.map(mano).join('');

  // orejas (detrás de la cabeza): otra señal clara de "persona"
  if (!ventana) [122, 278].forEach((x) => {
    g += `<circle cx="${x}" cy="178" r="15" fill="url(#${id}skin)" stroke="${L}" stroke-width="5"/>
          <path d="M${x + (x < 200 ? 2 : -2)},172 q${x < 200 ? 5 : -5},6 0,12" fill="none" stroke="${p.pielSombra}" stroke-width="3" stroke-linecap="round"/>`;
  });

  // mechón (detrás del pelo, sale de la coronilla)
  if (!ventana) {
    const d = MECHON[mood] || MECHON.calma;
    g += `<path d="${d}" fill="none" stroke="${L}" stroke-width="24" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="${d}" fill="none" stroke="url(#${id}pelo)" stroke-width="15" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="${d}" fill="none" stroke="${p.peloLuz}" stroke-width="3.5" stroke-linecap="round" opacity=".8" transform="translate(-3 -1)"/>`;
    if (mood === 'ansiedad') g += `<path d="M232,26 l10,-4 M236,44 l12,0 M168,30 l-10,-4" stroke="${L}" stroke-width="3.5" stroke-linecap="round"/>`;
    if (mood === 'idea') g += `<g transform="translate(262 34)"><path d="M0,-14 l3.5,10 l10.5,4 l-10.5,4 l-3.5,10 l-3.5,-10 l-10.5,-4 l10.5,-4z" fill="#F2B544" stroke="${L}" stroke-width="2.5" stroke-linejoin="round"/></g>`;
  }

  // cabeza
  if (ventana) {
    // la cabeza es una ventana al "clima interno": lo invisible hecho visible
    const clima = { triste: ['#8E9BB0', '#C5CEDA'], ansiedad: ['#6F7C9C', '#A9B6CF'], enojo: ['#E07A5F', '#F3B08F'] }[mood] || p.cielo;
    g += `<circle cx="200" cy="162" r="80" fill="${clima[1]}" stroke="${L}" stroke-width="6"/>
          <g clip-path="url(#${id}headclip)">
            <rect x="110" y="70" width="180" height="90" fill="${clima[0]}"/>
            ${mood === 'triste' || mood === 'ansiedad'
              ? `<path d="M140,120 a18,18 0 0 1 30,-16 a22,22 0 0 1 40,6 a16,16 0 0 1 10,28 h-74 a14,14 0 0 1 -6,-18z" fill="#E7ECF3"/>${mood === 'ansiedad' ? `<path d="M196,134 l-8,14 h8 l-6,12" fill="none" stroke="#FFD36B" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>` : `<path d="M160,140 l-4,10 M184,140 l-4,10 M208,140 l-4,10" stroke="#7FA9D6" stroke-width="3.5" stroke-linecap="round"/>`}`
              : `<circle cx="244" cy="110" r="20" fill="#FFD36B"/><path d="M134,126 a14,14 0 0 1 24,-12 a18,18 0 0 1 32,6 a12,12 0 0 1 4,20 h-56z" fill="#fff" opacity=".95"/>`}
            <path d="M110,160 H290 V250 H110Z" fill="url(#${id}skin)"/>
            <path d="M110,160 H290" stroke="${L}" stroke-width="5"/>
            <path d="M130,100 q30,-30 70,-24" fill="none" stroke="#fff" stroke-width="8" stroke-linecap="round" opacity=".45"/>
          </g>
          <circle cx="200" cy="162" r="80" fill="none" stroke="${L}" stroke-width="6"/>`;
    g += `<g transform="translate(0 14)">${cara(p, mood, true)}</g>`;
  } else {
    g += `<circle cx="200" cy="162" r="80" fill="url(#${id}skin)" stroke="${L}" stroke-width="5"/>
          <g clip-path="url(#${id}headclip)">
            <ellipse cx="262" cy="214" rx="90" ry="76" fill="${p.pielSombra}" opacity=".45" filter="url(#${id}blur)"/>
          </g>`;
    // pelo: casco con fleco de raya al lado
    g += `<path d="M122,170 C112,104 158,78 200,78 C250,78 292,106 280,170 C272,140 252,126 228,130 C216,114 186,114 174,132 C150,126 130,142 122,170 Z" fill="url(#${id}pelo)" stroke="${L}" stroke-width="5" stroke-linejoin="round"/>
          <path d="M160,100 q22,-14 48,-12" fill="none" stroke="${p.peloLuz}" stroke-width="5" stroke-linecap="round" opacity=".8"/>`;
    g += cara(p, mood, false);
  }
  if (frente) g += brazos.map(brazo).join('') + brazos.map(mano).join('');
  g += `</g>`;
  return defs + g;
}

if (typeof module !== 'undefined') module.exports = { personaje, PALETAS, MECHON, BRAZOS };
