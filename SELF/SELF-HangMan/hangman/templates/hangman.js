// ---- drawHangman (your existing function) ----
function drawHangman(svgEl, n) {
    const S = (tag, attrs, parent) => {
      const el = document.createElementNS('http://www.w3.org/2000/svg', tag);
      for (const [k, v] of Object.entries(attrs)) el.setAttribute(k, v);
      if (parent) parent.appendChild(el);
      return el;
    };
    svgEl.innerHTML = '';
    const base = { stroke: '#222', 'stroke-linecap': 'round', 'stroke-linejoin': 'round', fill: 'none' };
    const g = S('g', { 'stroke-width': '3', ...base }, svgEl);
    S('line', { x1: 20,  y1: 230, x2: 180, y2: 230 }, g);
    S('line', { x1: 60,  y1: 230, x2: 60,  y2: 20  }, g);
    S('line', { x1: 60,  y1: 20,  x2: 130, y2: 20  }, g);
    S('line', { x1: 130, y1: 20,  x2: 130, y2: 50  }, g);
    if (n < 1) return;
    const p = S('g', { 'stroke-width': '2.5', ...base }, svgEl);
    S('circle', { cx: 130, cy: 65, r: 15, stroke: '#222' }, p);
    if (n < 2) return;
    S('line', { x1: 130, y1: 80,  x2: 130, y2: 145 }, p);
    if (n < 3) return;
    S('line', { x1: 130, y1: 95,  x2: 105, y2: 120 }, p);
    if (n < 4) return;
    S('line', { x1: 130, y1: 95,  x2: 155, y2: 120 }, p);
    if (n < 5) return;
    S('line', { x1: 130, y1: 145, x2: 105, y2: 175 }, p);
    if (n < 6) return;
    S('line', { x1: 130, y1: 145, x2: 155, y2: 175 }, p);
    if (n < 7) return;
    S('line', { x1: 105, y1: 120, x2: 95,  y2: 132 }, p);
    S('line', { x1: 105, y1: 120, x2: 100, y2: 133 }, p);
    if (n < 8) return;
    S('line', { x1: 155, y1: 120, x2: 165, y2: 132 }, p);
    S('line', { x1: 155, y1: 120, x2: 160, y2: 133 }, p);
    if (n < 9) return;
    S('line', { x1: 105, y1: 175, x2: 93,  y2: 178 }, p);
    S('line', { x1: 105, y1: 175, x2: 97,  y2: 182 }, p);
    if (n < 10) return;
    S('line', { x1: 155, y1: 175, x2: 167, y2: 178 }, p);
    S('line', { x1: 155, y1: 175, x2: 163, y2: 182 }, p);
    if (n < 11) return;
    S('circle', { cx: 125, cy: 62, r: 2, stroke: '#222', fill: '#222' }, p);
    S('circle', { cx: 135, cy: 62, r: 2, stroke: '#222', fill: '#222' }, p);
    if (n < 12) return;
    S('path', { d: 'M124 71 Q130 76 136 71', 'stroke-width': '2', stroke: '#222', fill: 'none', 'stroke-linecap': 'round' }, p);
  }
  
  // ---- Game logic ----
  const MAX_WRONG = 12;
  const word = WORD;  // injected by Django
  
  let guessed = new Set();
  let wrong = 0;
  
  const svgEl      = document.getElementById('hangman-svg');
  const wordDisplay = document.getElementById('word-display');
  const lettersEl  = document.getElementById('letters');
  const messageEl  = document.getElementById('message');
  
  function getDisplay() {
    return word.split('').map(ch => guessed.has(ch) ? ch : '_').join(' ');
  }
  
  function isWon() {
    return word.split('').every(ch => guessed.has(ch));
  }
  
  function guess(letter) {
    if (guessed.has(letter)) return;
    guessed.add(letter);
  
    if (!word.includes(letter)) {
      wrong++;
    }
  
    render();
  }
  
  function render() {
    // update SVG
    drawHangman(svgEl, wrong);
  
    // update word
    wordDisplay.textContent = getDisplay();
  
    // update buttons
    lettersEl.querySelectorAll('button').forEach(btn => {
      const l = btn.dataset.letter;
      btn.disabled = guessed.has(l);
      if (guessed.has(l)) {
        btn.classList.add(word.includes(l) ? 'correct' : 'wrong');
      }
    });
  
    // message
    if (isWon()) {
      messageEl.textContent = '🎉 You won!';
      disableAll();
    } else if (wrong >= MAX_WRONG) {
      messageEl.textContent = `💀 Game over! The word was: ${word}`;
      disableAll();
    } else {
      messageEl.textContent = `Wrong guesses: ${wrong} / ${MAX_WRONG}`;
    }
  }
  
  function disableAll() {
    lettersEl.querySelectorAll('button').forEach(btn => btn.disabled = true);
  }
  
  // Build A–Z buttons
  'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('').forEach(letter => {
    const btn = document.createElement('button');
    btn.textContent = letter;
    btn.dataset.letter = letter;
    btn.addEventListener('click', () => guess(letter));
    lettersEl.appendChild(btn);
  });
  
  // Also support keyboard input
  document.addEventListener('keydown', e => {
    const l = e.key.toUpperCase();
    if (/^[A-Z]$/.test(l)) guess(l);
  });
  
  // Initial render
  render();