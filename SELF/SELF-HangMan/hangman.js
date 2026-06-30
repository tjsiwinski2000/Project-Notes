const params = new URLSearchParams(window.location.search);
const n = parseInt(params.get('n')) || 0;


function drawHangman(svgEl, n) {
  const S = (tag, attrs, parent) => {
    const el = document.createElementNS('http://www.w3.org/2000/svg', tag);
    for (const [k, v] of Object.entries(attrs)) el.setAttribute(k, v);
    if (parent) parent.appendChild(el);
    return el;
  };

  svgEl.innerHTML = '';
  const base = {
    stroke: '#222',
    'stroke-linecap': 'round',
    'stroke-linejoin': 'round',
    fill: 'none'
  };

  // Gallows (always shown)
  const g = S('g', { 'stroke-width': '3', ...base }, svgEl);
  S('line', { x1: 20,  y1: 230, x2: 180, y2: 230 }, g); // ground
  S('line', { x1: 60,  y1: 230, x2: 60,  y2: 20  }, g); // pole
  S('line', { x1: 60,  y1: 20,  x2: 130, y2: 20  }, g); // beam
  S('line', { x1: 130, y1: 20,  x2: 130, y2: 50  }, g); // rope

  if (n < 1) return;
  const p = S('g', { 'stroke-width': '2.5', ...base }, svgEl);

  // 1 - head
  S('circle', { cx: 130, cy: 65, r: 15, stroke: '#222' }, p);
  if (n < 2) return;

  // 2 - body
  S('line', { x1: 130, y1: 80,  x2: 130, y2: 145 }, p);
  if (n < 3) return;

  // 3 - left arm
  S('line', { x1: 130, y1: 95,  x2: 105, y2: 120 }, p);
  if (n < 4) return;

  // 4 - right arm
  S('line', { x1: 130, y1: 95,  x2: 155, y2: 120 }, p);
  if (n < 5) return;

  // 5 - left leg
  S('line', { x1: 130, y1: 145, x2: 105, y2: 175 }, p);
  if (n < 6) return;

  // 6 - right leg
  S('line', { x1: 130, y1: 145, x2: 155, y2: 175 }, p);
  if (n < 7) return;

  // 7 - left hand
  S('line', { x1: 105, y1: 120, x2: 95,  y2: 132 }, p);
  S('line', { x1: 105, y1: 120, x2: 100, y2: 133 }, p);
  if (n < 8) return;

  // 8 - right hand
  S('line', { x1: 155, y1: 120, x2: 165, y2: 132 }, p);
  S('line', { x1: 155, y1: 120, x2: 160, y2: 133 }, p);
  if (n < 9) return;

  // 9 - left foot
  S('line', { x1: 105, y1: 175, x2: 93,  y2: 178 }, p);
  S('line', { x1: 105, y1: 175, x2: 97,  y2: 182 }, p);
  if (n < 10) return;

  // 10 - right foot
  S('line', { x1: 155, y1: 175, x2: 167, y2: 178 }, p);
  S('line', { x1: 155, y1: 175, x2: 163, y2: 182 }, p);
  if (n < 11) return;

  // 11 - eyes
  S('circle', { cx: 125, cy: 62, r: 2, stroke: '#222', fill: '#222' }, p);
  S('circle', { cx: 135, cy: 62, r: 2, stroke: '#222', fill: '#222' }, p);
  if (n < 12) return;

  // 12 - mouth
  S('path', { d: 'M124 71 Q130 76 136 71', 'stroke-width': '2', stroke: '#222', fill: 'none', 'stroke-linecap': 'round' }, p);
}

// Pass any number 0–12
// Pass any number 0–12
drawHangman(document.getElementById('hangman-svg'), n);

