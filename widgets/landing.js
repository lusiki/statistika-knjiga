// Schematic sampling distribution for independent normal observations.
// Population mean = 0, population SD = 1; mean SD = 1 / sqrt(n).
// Common x/y scales preserve the increase in density as the spread narrows.
// This preview is separate from the chapter's empirical simulations.
(() => {
  const root = document.querySelector('.landing-distribution');
  if (!root) return;
  const slider = root.querySelector('input');
  const plot = root.querySelector('.landing-bars');
  const output = root.querySelector('output');
  const compare = root.querySelector('.landing-compare');
  const note = root.querySelector('.landing-distribution-note');
  const marks = Array.from({length: 41}, () => {
    const mark = document.createElement('i');
    plot.appendChild(mark);
    return mark;
  });
  function update(announce = false) {
    const n = Number(slider.value);
    const sigma = 1 / Math.sqrt(n);
    output.value = String(n);
    marks.forEach((mark, i) => {
      const x = (i - 20) * 0.07;
      const density = Math.exp(-0.5 * (x / sigma) ** 2) / (sigma * Math.sqrt(2 * Math.PI));
      mark.style.height = `${density / 4.1 * 100}%`;
    });
    plot.setAttribute('aria-label', `Shematska raspodjela sredina uzoraka veličine ${n}. Veći uzorci daju užu raspodjelu.`);
    compare.textContent = n < 100 ? 'Usporedi s većim uzorkom →' : 'Usporedi s manjim uzorkom →';
    if (announce) note.textContent = n >= 50
      ? 'Veći uzorci daju sredine koje su bliže jedna drugoj.'
      : 'Manji uzorci daju više raspršene sredine.';
  }
  update();
  root.querySelectorAll('[hidden]').forEach(element => { element.hidden = false; });
  slider.addEventListener('input', () => update());
  slider.addEventListener('change', () => update(true));
  compare.addEventListener('click', () => {
    slider.value = Number(slider.value) < 100 ? '100' : '5';
    update(true);
  });
})();
