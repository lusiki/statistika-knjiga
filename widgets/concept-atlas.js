// Living atlas: the canonical graph supplies terms, definitions and real edges.
// Every term is present; only the strongest connections and a few labels are shown.
export function createAtlas(graph, {d3, href, chapter = '', selected = ''} = {}) {
  const element = (tag, className = '', text = '') => {
    const node = document.createElement(tag);
    node.className = className;
    node.textContent = text;
    return node;
  };
  const button = (text, className, action) => {
    const node = element('button', className, text);
    node.type = 'button';
    node.addEventListener('click', action);
    return node;
  };
  const fold = value => String(value || '').toLocaleLowerCase('hr').normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '').replace(/đ/g, 'd').trim();
  const nodes = (graph.nodes || []).filter(n => n.id && n.term);
  const byId = new Map(nodes.map(n => [n.id, n]));
  const edges = (graph.edges || []).filter(e => byId.has(e.source) && byId.has(e.target));
  const scope = nodes.some(n => n.chapter === chapter) ? chapter : '';
  const available = scope ? nodes.filter(n => n.chapter === scope) : nodes;
  const availableIds = new Set(available.map(n => n.id));
  const root = element('section', 'concept-atlas');
  root.setAttribute('aria-label', 'Pojmovnik: živa mreža pojmova');
  const heading = element('header', 'atlas-header');
  const intro = element('div', 'atlas-intro');
  const title = element('h1', 'atlas-title', 'Pojmovnik');
  intro.append(title, element('p', 'atlas-hint', 'Povucite pojam. Odaberite ga za objašnjenje.'));
  if (scope) {
    const scopeLine = element('p', 'atlas-scope', available[0].chapterTitle + ' · ');
    const all = element('a', '', 'Sva poglavlja');
    all.href = window.location.pathname;
    scopeLine.append(all);
    intro.append(scopeLine);
  }
  const search = element('div', 'atlas-search');
  const input = element('input');
  input.type = 'search';
  input.placeholder = 'Pronađi pojam…';
  input.setAttribute('aria-label', scope ? 'Pronađi pojam u odabranom poglavlju' : 'Pronađi pojam');
  input.autocomplete = 'off';
  const results = element('div', 'atlas-results');
  results.hidden = true;
  const status = element('p', 'visually-hidden');
  status.setAttribute('role', 'status');
  search.append(input, results, status);
  heading.append(intro, search);
  root.append(heading);
  const stage = element('div', 'atlas-stage');
  const network = element('div', 'atlas-network');
  network.setAttribute('role', 'group');
  network.setAttribute('aria-label', 'Mreža pojmova. Strelice biraju sljedeći pojam; Enter otvara definiciju. Shift i strelica pomiču pojam.');
  const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
  svg.classList.add('atlas-links');
  svg.setAttribute('aria-hidden', 'true');
  const labelsLayer = element('div', 'atlas-labels');
  labelsLayer.setAttribute('aria-hidden', 'true');
  network.append(svg, labelsLayer);
  const panel = element('section', 'atlas-definition');
  panel.setAttribute('aria-label', 'Odabrani pojam');
  panel.hidden = true;
  const sidebar = element('div', 'atlas-sidebar');
  const invitation = element('div', 'atlas-invitation');
  invitation.append(element('span', 'atlas-eyebrow', `${available.length} povezanih pojmova`),
    element('h2', '', 'Jedan pojam vodi do drugoga.'),
    element('p', '', 'Odaberite točku u mreži ili pronađite pojam pretragom.'));
  sidebar.append(invitation, panel);
  stage.append(network, sidebar);
  root.append(stage);
  const footer = element('div', 'atlas-footer');
  const index = element('details', 'atlas-index');
  index.append(element('summary', '', `Svi pojmovi A–Ž (${available.length})`));
  const indexList = element('div', 'atlas-index-list');
  index.append(indexList);
  intro.append(button('Otvori popis A–Ž', 'atlas-list-shortcut', () => {
    index.open = true;
    indexList.querySelector('button')?.focus();
    index.scrollIntoView({block: 'center'});
  }));
  const motion = matchMedia('(prefers-reduced-motion: reduce)');
  let moving = !motion.matches;
  let selectedId = availableIds.has(selected) ? selected : '';
  let focusReturn = null;
  let width = 0, height = 0, drag = null, hoveredId = '', part = 0;
  let scale = 1, fitScale = 1, offsetX = 0, offsetY = 0;
  let searchIds = null;
  let visible = true, disposed = false, raf = 0, time = 0, last = 0;
  const pause = button('', 'atlas-pause', () => { moving = !moving; updateMotion(); });
  const note = element('p', 'atlas-edge-note', 'Veća točka: više spominjanja. Crta: zajednička uporaba, ne redoslijed učenja.');
  const notes = document.getElementById('o-nazivlju');
  const notesButton = button('O nazivlju', 'atlas-notes-toggle', () => {
    if (!notes) return;
    notes.open = !notes.open;
    notesButton.setAttribute('aria-expanded', String(notes.open));
    if (notes.open) notes.scrollIntoView({block: 'nearest'});
  });
  notesButton.setAttribute('aria-expanded', 'false');
  notesButton.setAttribute('aria-controls', 'o-nazivlju');
  if (notes) notes.classList.add('atlas-notes-enhanced');
  footer.append(index, notesButton, pause, note);
  root.append(footer);
  const neighbours = id => edges.filter(e => e.source === id || e.target === id)
    .sort((a, b) => b.weight - a.weight)
    .map(e => e.source === id ? e.target : e.source).filter(id => availableIds.has(id));
  const terms = [...available].sort((a, b) => a.term.localeCompare(b.term, 'hr'));
  terms.forEach(n => indexList.append(button(n.term, '', () => {
    choose(n.id);
    index.open = false;
    panel.scrollIntoView({block: 'nearest'});
  })));
  // Read aliases from the generated, reader-visible terminology table.
  // This avoids maintaining a second editorial vocabulary in JavaScript.
  const aliases = Array.from(notes?.querySelectorAll('#tbl-terminologija-uputnice tbody tr') || [])
    .map(row => { const cells = row.querySelectorAll('td'); return {
      form: cells[0]?.textContent.trim(), canonical: cells[1]?.textContent.trim(),
      reason: cells[3]?.textContent.trim(), row
    }; }).filter(a => a.form && a.canonical);

  function hideResults() { results.hidden = true; searchIds = null; draw(); }
  function searchTerms() {
    const query = fold(input.value);
    results.replaceChildren();
    results.hidden = !query;
    if (!query) { status.textContent = ''; searchIds = null; draw(); return; }
    const matching = terms.filter(n => fold(n.term + ' ' + n.firstSentence).includes(query))
      .sort((a, b) => Number(fold(b.term).includes(query)) - Number(fold(a.term).includes(query)));
    const routes = scope ? [] : aliases.filter(a => fold(a.form).includes(query));
    matching.slice(0, 6).forEach(n => results.append(button(n.term, '', () => choose(n.id))));
    routes.slice(0, Math.max(0, 6 - matching.length)).forEach(a => results.append(button(
      `${a.form} → ${a.canonical}`, '', () => {
        const canonical = terms.find(n => fold(n.term) === fold(a.canonical));
        if (canonical) choose(canonical.id);
        else {
          hideResults();
          input.value = '';
          notes.open = true;
          notesButton.setAttribute('aria-expanded', 'true');
          a.row.scrollIntoView({block: 'center'});
        }
      }
    )));
    const count = matching.length + routes.length;
    searchIds = new Set(matching.map(n => n.id));
    draw();
    status.textContent = count ? `Pronađeno pojmova i uputnica: ${count}.` : 'Nema pronađenih pojmova.';
    if (!count) results.append(element('p', '', 'Nema pronađenih pojmova.'));
  }
  input.addEventListener('input', searchTerms);
  input.addEventListener('keydown', event => {
    if (event.key === 'Escape') hideResults();
    if (event.key === 'ArrowDown' && !results.hidden) { event.preventDefault(); results.querySelector('button')?.focus(); }
    if (event.key === 'Enter' && !results.hidden) results.querySelector('button')?.click();
  });
  results.addEventListener('keydown', event => {
    if (event.key === 'Escape') { hideResults(); input.focus(); }
  });
  const outside = event => { if (!search.contains(event.target)) hideResults(); };
  document.addEventListener('pointerdown', outside);

  function closePanel() {
    panel.hidden = true;
    invitation.hidden = false;
    stage.classList.remove('has-selection');
    const prior = selectedId;
    selectedId = '';
    draw();
    const target = focusReturn?.isConnected ? focusReturn : marks.find(n => n.id === prior)?.button || input;
    target.focus({preventScroll: true});
  }
  function choose(id, focus = true) {
    const n = byId.get(id);
    if (!n || !availableIds.has(id)) return;
    focusReturn = document.activeElement;
    selectedId = id;
    hideResults();
    input.value = '';
    panel.replaceChildren();
    const close = button('Zatvori', 'atlas-close', closePanel);
    const heading = element('h2', '', n.term);
    heading.tabIndex = -1;
    const definition = element('p', 'atlas-definition-text', String(n.firstSentence || '').replace(/\s+([,.;:!?])/g, '$1'));
    const chapterLink = element('a', 'atlas-chapter', `${n.chapterTitle} →`);
    chapterLink.href = href(n);
    panel.append(close, heading, definition, chapterLink);
    const related = element('div', 'atlas-related');
    related.setAttribute('aria-label', 'Pojmovi koji se pojavljuju zajedno');
    neighbours(id).slice(0, 3).forEach(other => related.append(button(byId.get(other).term, '', () => choose(other))));
    if (related.childElementCount) panel.append(related);
    panel.hidden = false;
    stage.classList.add('has-selection');
    invitation.hidden = true;
    part = 0;
    updateLegend();
    draw();
    if (focus) {
      heading.focus({preventScroll: true});
      if (matchMedia('(max-width: 800px)').matches) panel.scrollIntoView({block: 'start'});
    }
  }
  panel.addEventListener('keydown', event => { if (event.key === 'Escape') closePanel(); });

  // Keep all canonical terms in one stable graph. The per-node edge budget
  // prevents the 615 real relationships from obscuring the map.
  const strongest = new Map();
  available.forEach(n => edges.filter(e => (e.source === n.id || e.target === n.id) &&
    availableIds.has(e.source) && availableIds.has(e.target))
    .sort((a, b) => b.weight - a.weight).slice(0, 3)
    .forEach(e => strongest.set([e.source, e.target].sort().join('|'), e)));
  const maxMentions = Math.max(1, ...available.map(n => n.mentions || 1));
  const marks = available.map((n, i) => ({...n,
    r: 6 + 18 * Math.sqrt((n.mentions || 1) / maxMentions),
    x: Math.cos(i * 2.4) * Math.sqrt(i + 1) * 28,
    y: Math.sin(i * 2.4) * Math.sqrt(i + 1) * 28,
    suppress: false, labelWidth: 0, labelHeight: 0
  }));
  const links = [...strongest.values()].map(e => ({...e}));
  links.forEach(e => {
    e.line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
    svg.append(e.line);
  });
  const simulation = d3.forceSimulation(marks).stop()
    .force('link', d3.forceLink(links).id(n => n.id)
      .distance(e => 110 - Math.min(8, e.weight) * 6).strength(.19))
    .force('charge', d3.forceManyBody().strength(-180))
    .force('x', d3.forceX(n => Math.cos((n.dio - 1) * Math.PI / 3) * 115).strength(.07))
    .force('y', d3.forceY(n => Math.sin((n.dio - 1) * Math.PI / 3) * 100).strength(.07))
    .force('collide', d3.forceCollide(n => n.r + 12).iterations(2))
    .velocityDecay(.5);
  // Start with a settled map even for readers who prefer reduced motion.
  simulation.tick(240);
  const anchors = new Map(marks.map(n => [n.id, {x: n.x, y: n.y}]));

  const legend = element('div', 'atlas-legend');
  legend.setAttribute('role', 'group');
  legend.setAttribute('aria-label', 'Istakni dio knjige');
  const partButtons = new Map();
  [...new Set(available.map(n => n.dio))].sort((a, b) => a - b).forEach(dio => {
    const data = available.find(n => n.dio === dio);
    const b = button('', 'atlas-part', () => {
      selectedId = ''; hoveredId = '';
      panel.hidden = true; invitation.hidden = false;
      stage.classList.remove('has-selection');
      part = part === dio ? 0 : dio;
      const entry = marks.find(n => !part || n.dio === part);
      marks.forEach(n => { n.button.tabIndex = n === entry ? 0 : -1; });
      updateLegend(); draw();
    });
    b.dataset.part = dio;
    const label = data.dioLabel.replace(/^DIO [IVX]+:\s*/, '').toLocaleLowerCase('hr');
    b.append(element('span', 'atlas-part-dot'), element('span', '', label[0].toLocaleUpperCase('hr') + label.slice(1)));
    b.setAttribute('aria-pressed', 'false');
    partButtons.set(dio, b); legend.append(b);
  });
  if (partButtons.size > 1) root.insertBefore(legend, stage);
  function updateLegend() {
    partButtons.forEach((b, dio) => b.setAttribute('aria-pressed', String(part === dio)));
  }

  const zoom = element('div', 'atlas-zoom');
  zoom.setAttribute('role', 'group');
  zoom.setAttribute('aria-label', 'Povećanje mreže');
  const zoomOut = button('−', '', () => zoomBy(1 / 1.3));
  const zoomIn = button('+', '', () => zoomBy(1.3));
  const reset = button('Cijela mreža', 'atlas-fit', () => { fit(); draw(); });
  zoomOut.setAttribute('aria-label', 'Umanji mrežu');
  zoomIn.setAttribute('aria-label', 'Povećaj mrežu');
  zoom.append(zoomOut, zoomIn, reset); network.append(zoom);
  function zoomBy(factor) {
    const next = Math.max(fitScale * .8, Math.min(fitScale * 3, scale * factor));
    const ratio = next / scale;
    offsetX = width / 2 + (offsetX - width / 2) * ratio;
    offsetY = height / 2 + (offsetY - height / 2) * ratio;
    scale = next; draw();
  }
  function fit() {
    if (!marks.length || !width || !height) return;
    const x0 = Math.min(...marks.map(n => n.x - n.r));
    const x1 = Math.max(...marks.map(n => n.x + n.r));
    const y0 = Math.min(...marks.map(n => n.y - n.r));
    const y1 = Math.max(...marks.map(n => n.y + n.r));
    scale = fitScale = Math.min((width - 64) / (x1 - x0 + 50), (height - 100) / (y1 - y0 + 50), 1.5);
    offsetX = width / 2 - (x0 + x1) * scale / 2;
    offsetY = (height - 30) / 2 - (y0 + y1) * scale / 2;
  }

  marks.forEach(n => {
    const b = button('', 'atlas-node', () => {
      if (n.suppress) { n.suppress = false; return; }
      choose(n.id);
    });
    n.button = b; b.dataset.part = n.dio; b.dataset.id = n.id;
    b.tabIndex = n === marks[0] ? 0 : -1;
    b.setAttribute('aria-label', `${n.term} — otvori definiciju`);
    n.label = element('span', 'atlas-node-label', n.term);
    b.append(element('span', 'atlas-node-shape'));
    labelsLayer.append(n.label);
    network.append(b);
    b.addEventListener('pointerenter', () => { hoveredId = n.id; draw(); });
    b.addEventListener('pointerleave', () => { hoveredId = ''; draw(); });
    b.addEventListener('focus', () => {
      marks.forEach(other => { other.button.tabIndex = other === n ? 0 : -1; });
      n.fx = n.x; n.fy = n.y;
      const x = n.x * scale + offsetX, y = n.y * scale + offsetY;
      if (x < 24 || x > width - 24 || y < 24 || y > height - 60) {
        offsetX = width / 2 - n.x * scale; offsetY = height / 2 - n.y * scale;
      }
      draw();
    });
    b.addEventListener('blur', () => { n.fx = n.fy = null; draw(); });
    b.addEventListener('pointerdown', event => {
      if (event.button !== 0) return;
      event.stopPropagation(); n.suppress = false;
      drag = {n, startX: event.clientX, startY: event.clientY, x: event.clientX, y: event.clientY, moved: false};
      n.fx = n.x; n.fy = n.y;
      b.setPointerCapture(event.pointerId);
    });
    b.addEventListener('pointermove', event => {
      if (drag?.n !== n) return;
      if (Math.hypot(event.clientX - drag.startX, event.clientY - drag.startY) > 5) drag.moved = true;
      if (drag.moved) {
        n.x += (event.clientX - drag.x) / scale;
        n.y += (event.clientY - drag.y) / scale;
        n.fx = n.x; n.fy = n.y;
        if (moving) simulation.alpha(.16);
        draw();
      }
      drag.x = event.clientX; drag.y = event.clientY;
    });
    const release = () => {
      if (drag?.n !== n) return;
      n.suppress = drag.moved; drag = null;
      anchors.set(n.id, {x: n.x, y: n.y});
      if (document.activeElement !== b) n.fx = n.fy = null;
    };
    b.addEventListener('pointerup', release);
    b.addEventListener('pointercancel', release);
    b.addEventListener('lostpointercapture', release);
    b.addEventListener('keydown', event => {
      const delta = {ArrowLeft: [-16,0], ArrowRight: [16,0], ArrowUp: [0,-16], ArrowDown: [0,16]}[event.key];
      if (!delta) return;
      event.preventDefault();
      if (!event.shiftKey) {
        const candidates = marks.filter(other => other !== n && (!part || other.dio === part));
        const forward = candidates.filter(other => (other.x - n.x) * delta[0] + (other.y - n.y) * delta[1] > 0);
        const target = (forward.length ? forward : candidates).sort((a,b) => Math.hypot(a.x-n.x,a.y-n.y)-Math.hypot(b.x-n.x,b.y-n.y))[0];
        target?.button.focus({preventScroll:true});
        return;
      }
      n.x += delta[0] / scale; n.y += delta[1] / scale;
      n.fx = n.x; n.fy = n.y;
      anchors.set(n.id, {x: n.x, y: n.y}); draw();
    });
  });
  // Dragging empty space pans; normal touch scrolling remains available.
  network.addEventListener('pointerdown', event => {
    if (event.target !== network || event.pointerType === 'touch' || event.button !== 0) return;
    drag = {x: event.clientX, y: event.clientY};
    network.setPointerCapture(event.pointerId);
  });
  network.addEventListener('pointermove', event => {
    if (!drag || drag.n) return;
    offsetX += event.clientX - drag.x; offsetY += event.clientY - drag.y;
    drag.x = event.clientX; drag.y = event.clientY; draw();
  });
  const stopPan = () => { if (drag && !drag.n) drag = null; };
  network.addEventListener('pointerup', stopPan);
  network.addEventListener('pointercancel', stopPan);
  network.addEventListener('lostpointercapture', stopPan);

  function draw() {
    if (!width || disposed) return;
    const focused = marks.find(n => document.activeElement === n.button)?.id;
    const active = hoveredId || focused || selectedId;
    const related = new Set(active ? [active, ...neighbours(active).slice(0, 5)] : []);
    const emphasized = searchIds?.size ? searchIds : active ? related : part ?
      new Set(marks.filter(n => n.dio === part).map(n => n.id)) : null;
    const overlaps = (a, b) => a.x < b.x + b.w + 5 && a.x + a.w + 5 > b.x &&
      a.y < b.y + b.h + 4 && a.y + a.h + 4 > b.y;
    const obstacles = [];
    marks.forEach(n => {
      n.sx = n.x * scale + offsetX; n.sy = n.y * scale + offsetY;
      n.sr = Math.max(5, n.r * scale);
      const size = Math.max(28, n.sr * 2 + 8);
      n.button.style.width = n.button.style.height = `${size}px`;
      n.button.style.transform = `translate(${n.sx - size / 2}px, ${n.sy - size / 2}px)`;
      n.button.style.setProperty('--node-size', `${n.sr * 2}px`);
      n.button.setAttribute('aria-pressed', String(n.id === selectedId));
      n.button.classList.toggle('is-muted', !!emphasized && !emphasized.has(n.id));
      n.button.classList.toggle('is-active', n.id === active);
      n.label.classList.remove('is-visible');
      n.label.classList.toggle('is-active', n.id === active);
    });
    links.forEach(e => {
      e.line.setAttribute('x1', e.source.sx); e.line.setAttribute('y1', e.source.sy);
      e.line.setAttribute('x2', e.target.sx); e.line.setAttribute('y2', e.target.sy);
      const connected = active && (e.source.id === active || e.target.id === active);
      e.line.classList.toggle('atlas-link-active', !!connected);
      e.line.classList.toggle('is-muted', !!emphasized && !connected &&
        !(emphasized.has(e.source.id) && emphasized.has(e.target.id)));
    });
    // Labels are secondary to the network. Place the important ones in free
    // space, and always reveal the term under the pointer or keyboard focus.
    const ranked = [...marks].sort((a, b) => Number(b.id === active) - Number(a.id === active) ||
      Number(emphasized?.has(b.id)) - Number(emphasized?.has(a.id)) || b.mentions - a.mentions);
    let labels = 0;
    for (const n of ranked) {
      if (emphasized && !emphasized.has(n.id)) continue;
      if (labels >= (width < 450 ? 4 : 8) && n.id !== active) break;
      const w = n.labelWidth || 100, h = n.labelHeight || 18;
      const gap = n.sr + 5;
      const positions = [{x: n.sx + gap, y: n.sy - h / 2}, {x: n.sx - gap - w, y: n.sy - h / 2},
        {x: n.sx - w / 2, y: n.sy + gap}, {x: n.sx - w / 2, y: n.sy - gap - h}];
      let box = positions.map(p => ({...p, w, h})).find(p => p.x >= 4 && p.y >= 4 &&
        p.x + w <= width - 4 && p.y + h < height - 48 && !obstacles.some(o => overlaps(p, o)));
      if (!box && n.id === active) box = {x: Math.max(4, Math.min(width - w - 4, n.sx - w / 2)),
        y: Math.max(4, Math.min(height - h - 48, n.sy + gap)), w, h};
      if (!box) continue;
      n.label.style.left = `${box.x}px`;
      n.label.style.top = `${box.y}px`;
      n.label.classList.add('is-visible'); obstacles.push(box); labels++;
    }
    zoomOut.disabled = scale <= fitScale * .801;
    zoomIn.disabled = scale >= fitScale * 2.999;
  }
  function layout() {
    const w = network.clientWidth, h = network.clientHeight;
    if (!w || !h || (width === w && height === h)) return;
    width = w; height = h;
    marks.forEach(n => { n.labelWidth = n.label.offsetWidth; n.labelHeight = n.label.offsetHeight; });
    svg.setAttribute('viewBox', `0 0 ${width} ${height}`);
    fit(); draw();
  }
  function frame(now) {
    raf = 0;
    if (!moving || !visible || document.hidden || disposed) return;
    // A fixed 30 Hz simulation is enough for a quiet, living background.
    if (!last || now - last >= 32) {
      time += .033; last = now;
      marks.forEach((n, i) => {
        if (n.fx != null) return;
        const a = anchors.get(n.id);
        n.vx += (a.x + Math.sin(time * .4 + i * 1.7) * 9 - n.x) * .008;
        n.vy += (a.y + Math.cos(time * .35 + i * 1.3) * 9 - n.y) * .008;
      });
      simulation.tick(); draw();
    }
    raf = requestAnimationFrame(frame);
  }

  function updateMotion() {
    pause.textContent = moving ? 'Zaustavi kretanje' : 'Pokreni kretanje';
    pause.setAttribute('aria-pressed', String(!moving));
    cancelAnimationFrame(raf); raf = 0; last = 0;
    if (moving && visible && !document.hidden && !disposed) raf = requestAnimationFrame(frame);
  }
  const preference = () => { moving = !motion.matches; updateMotion(); };
  motion.addEventListener('change', preference);
  document.addEventListener('visibilitychange', updateMotion);
  const observer = new ResizeObserver(() => layout());
  observer.observe(network);
  const visibility = new IntersectionObserver(entries => { visible = entries[0].isIntersecting; updateMotion(); });
  visibility.observe(network);
  const notesHash = () => {
    const hash = window.location.hash.slice(1);
    if (notes && (hash === 'o-nazivlju' || hash.startsWith('sec-terminologija-') || hash.startsWith('tbl-terminologija-'))) {
      notes.open = true;
      notesButton.setAttribute('aria-expanded', 'true');
      document.getElementById(hash)?.scrollIntoView({block: 'start'});
    }
  };
  window.addEventListener('hashchange', notesHash);
  if (!available.length) {
    stage.replaceChildren(element('p', 'atlas-empty', 'Pojmovnik se još gradi. Pojmovi su dostupni u abecednom rječniku.'));
    input.disabled = true; pause.hidden = true;
  }
  if (selectedId) choose(selectedId, false);
  updateMotion(); notesHash();
  root.dispose = () => {
    disposed = true; cancelAnimationFrame(raf); simulation.stop(); observer.disconnect(); visibility.disconnect();
    document.removeEventListener('pointerdown', outside);
    document.removeEventListener('visibilitychange', updateMotion);
    motion.removeEventListener('change', preference);
    window.removeEventListener('hashchange', notesHash);
    notes?.classList.remove('atlas-notes-enhanced');
  };
  return root;
}
