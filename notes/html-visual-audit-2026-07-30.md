# HTML visual audit — full book

**Date:** 30 July 2026
**Scope:** all 36 rendered HTML pages; seven widths; light and dark themes
**Status:** ready for HTML visual sign-off

## Final remediation and sign-off

All visual defects identified in the original audit have been corrected in the
source system and the canonical `docs/` build. The introductory italic text is
fully visible, cited callouts remain inside the reading column, and the dark
callout treatment no longer becomes a page-spanning band. Body text computes to
the intended 17 px; no page-specific shrinking was used to conceal layout
problems.

Figures now use the book theme, transparent SVG canvases, and explicit
light/dark pairs. Static ggplots therefore sit directly on the page without a
white outer canvas or default gray plotting panel. Phone-specific assets or
geometry are used where scaling a desktop figure would make its labels too
small. All 17 chapter interactions are implemented, responsive, and paired with
their static print twins.

Tables now distinguish prose from numeric content, avoid mid-word breaks, and
reflow where possible. Comparisons that genuinely need width use a visible,
keyboard-focusable, labelled horizontal scroller with a sticky first column.
Chapter openers, terminology lists, appendix numbering, navigation, search,
support-page empty states, the weekly schedule, mobile footers, and the portable
404 page all use the same editorial system.

### Final verification

| Check | Result |
|---|---|
| Full Quarto render | 36/36 inputs; 19 chapter exports |
| Canonical HTML freshness | 36/36 pages current; no skeletons, development widgets, or duplicate appendix titles |
| Widget contracts | 17/17 HTML graphs, static twins, and registry entries |
| Browser matrix | 37 routes × 7 widths × 2 themes = 518 cases; 0 failures |
| Screenshot evidence | 660 full-page images/numbered tall-page tiles |
| Viewports | 1440, 1100, 1000, 768, 600, 390, and 320 px |
| Themes | light and dark on every route/width |
| Editorial style | 19/19 chapter files; 0 deterministic candidates |
| Figure introductions | 19/19 chapter files; 0 conceptual figures missing an introduction |
| Design tokens | all CSS, TeX, and R layers synchronized |
| Source whitespace | `git diff --check` passes outside generated output |

The browser matrix checks document and component overflow, callout bounds,
table accessibility, widget execution, effective SVG text size, figure-theme
pairing, broken images, Croatian interface text, navigation height and utility
icons, and browser/runtime errors. Very tall phone pages are captured as
numbered tiles so their exercise, navigation, citation, and footer tails are
also inspected.

Every page received human visual review at representative desktop, tablet, and
phone widths in both themes. After the first review found a final set of narrow
and intermediate-width polish issues, the affected pages were corrected and
reinspected from the consolidated full build. No remaining overlap, clipping,
unintended full-page shape, graph-background seam, broken table word, illegible
plot label, or incomplete page tail was found.

The only render warning is the optional Quarto code-linking warning that the R
packages `downlit` and `xml2` are not installed. It does not affect layout,
content, figures, widgets, or navigation.

---

The sections below preserve the original pre-remediation audit for traceability.
Descriptions written in the present tense refer to the original baseline, not
to the signed-off build above.

## Pre-remediation executive verdict

The visual foundation is good: the warm paper, restrained palette, reading
measure, serif hierarchy, whitespace, folded code, summaries, and lower-page
navigation already feel like one coherent editorial system. Ordinary prose does
not generally overlap, and most chapter pages do not create whole-document
horizontal scrolling.

The conspicuous failures are real, but they are concentrated in a small number
of shared systems:

1. The HTML committed in `docs/` is a stale skeleton build and does not represent
   the current chapter sources.
2. Margin citations promote their containing callouts to Quarto's `page-full`
   grid. This clips 18 of 19 opening vignettes behind the left sidebar and turns
   all 19 “Statistika u divljini” callouts into viewport-wide black bands.
3. The figures on all six current figure-bearing pages are stale/default ggplot
   assets. Their PNG devices also have opaque white canvases, so merely
   refreshing the existing theme will not completely remove the seam against
   the page.
4. The type scale is applied twice. Body text is approximately 18.06 px rather
   than the specified 17 px, and all rem-based headings are enlarged by the
   same 6.25%.
5. Mobile tables, navigation, and several custom components need structural
   reflow. Making their text smaller would conceal rather than solve the
   problem.
6. All 17 planned chapter widgets are still developer placeholders. Their final
   visual quality and responsive behaviour therefore cannot yet be signed off.

The first three items should be treated as release blockers. They explain the
cut italic openings, unexplained black shapes, and white/gray plot islands
reported in the brief.

## Method

The audit used:

- a comparison of the committed `docs/` HTML with a fresh isolated HTML render;
- every one of the 36 HTML pages at 1440 × 900 and 390 × 844;
- DOM measurements for page width, element bounds, clipping, and overflow;
- focused checks at intermediate widths for margin references;
- representative light- and dark-mode checks;
- pixel inspection of the existing plot canvases;
- a forced no-cache re-execution of a figure-bearing chapter to distinguish an
  obsolete plot theme from an opaque graphics-device background;
- inspection of the corresponding SCSS, Quarto configuration, R theme, and
  post-render JavaScript.

The fresh render is the basis for page-level judgments. The stale `docs/` build
is reported separately because it is what would currently be published.

Severity used below:

- **P0:** blocks publication or makes the rendered book materially misleading.
- **P1:** prominent visual or responsive defect.
- **P2:** important consistency, polish, or content-presentation defect.
- **P3:** optional refinement.

## Direct answers to the questions in the brief

### Is the introductory italic text cut off?

Yes. This is not caused by the text being too large. A citation inside the
vignette makes Quarto add `page-columns page-full` to the callout. At the
desktop test width, normal prose begins around x = 299 px, but the vignette
starts at x = 0 and its text begins around x = 243 px. The fixed left sidebar
ends around x = 260 px, so the first part of every line is physically hidden
behind it.

This affects the preface and chapters 1–17. Chapter 18 has an uncited vignette
and renders correctly, making it a useful reference implementation. On phones,
the text is no longer behind a sidebar, but the `VINJETA` label and first line
collide.

### What are the black shapes through the whole page?

They are the same grid bug expressed through a background. Every cited
“Statistika u divljini” callout becomes `page-full`; its ink background is then
painted from one viewport edge to the other, beneath both navigation rails.
The stale `docs/` build makes this look worse because several of those bands are
empty.

The dark reversed treatment itself is currently prescribed by `DESIGN.md`, but
the accidental viewport span is not. The recommended design is a deliberately
bounded body-width reversed block. If any dark slab is still too dominant, use
the same semantic label with paper background and a strong top rule instead.
The decision should be recorded in `DESIGN.md` so implementation and visual
intent no longer conflict.

### Should the text be smaller?

Only slightly, and only by correcting the duplicate scale. The intended 17 px
body size is applied once by the SCSS token and again through Quarto's
`fontsize`, producing approximately 18.06 px. Remove one declaration—preferably
the duplicate YAML value—and retain the 17 px design token.

Do not make introductory prose or phone body copy smaller to solve clipping.
Several plot labels should actually become larger on phones. Wide tables need
reflow, shorter reader-facing labels, or an explicit scroll treatment rather
than compressed type.

### Can the plots sit seamlessly on the page?

Yes. The current R theme already points in the right direction, but the
rendered assets do not reflect it. There are two independent failures:

1. freeze/cache reuse leaves old default ggplot panels, colors, and typography
   in the HTML;
2. the PNG graphics device paints an opaque white canvas even when the ggplot
   plot and panel fills are transparent.

A forced re-execution removed the default gray panel and default blue styling,
but the white outer canvas remained. The complete correction is therefore:

- refresh all figure caches;
- make shared theme files explicit cache dependencies;
- run setup chunks without cache side-effect reuse;
- set `fig.bg = "transparent"` globally;
- prefer transparent SVG for HTML where practical;
- use neutral ink for normal analytical marks and reserve ochre for intentional
  emphasis;
- create a dark-mode asset or dark-aware vector treatment rather than placing
  a light-palette transparent raster on dark paper.

## Priority findings and corrections

### P0 — `docs/` is not the current book

The committed HTML still contains skeleton markers, empty callouts, and
placeholder headings such as “Naslov prvog odjeljka,” while the current QMD
files contain substantive chapters. A fresh render is materially different.

**Correction**

1. Complete the systemic visual fixes below.
2. Regenerate figures with a cache refresh.
3. Render the complete book into `docs/`.
4. Add a CI freshness gate. At minimum, a release build should fail when a
   render changes tracked output or when known source markers are absent from
   the corresponding HTML.
5. Make the clean rendered result, not a frozen skeleton, the visual-regression
   baseline.

### P1 — citation grids break callouts and exercise separators

Relevant locations:

- `_quarto.yml:214–215`
- `styles/_callouts.scss:36`
- `styles/_callouts.scss:83`
- `styles/_callouts.scss:294`

Quarto places citations in the margin and promotes their ancestors to
`page-full`. Custom callout decoration is attached to that promoted root, so
the border, label, background, and prose no longer share the intended body
column. The same propagation gives every chapter at least one page-wide
exercise separator. Empty margin containers also retain borders, producing
floating hairlines.

**Preferred correction**

Introduce a render-time wrapper or small Pandoc filter:

- the semantic callout remains the outer container;
- a visual callout body is explicitly placed in
  `body-content-start / body-content-end`;
- the generated margin citation remains a separate grid sibling in the margin;
- backgrounds, borders, labels, and mobile padding belong to the visual body,
  never to the `page-full` root.

This preserves margin citations without allowing them to redesign their parent.
A CSS-only body-column constraint was tested and removes the clipping and black
band, but moving citations into normal flow below the callout is the safer
fallback if the wrapper is not introduced.

Additional corrections:

- hide truly empty `.column-margin` elements;
- attach exercise rules to the body-column heading or an inner wrapper;
- target an explicit solution element inside error callouts rather than
  `:last-child`, which can accidentally select a generated margin container;
- below 600 px, reduce horizontal callout padding to about 1–1.25 rem and stack
  the label above the content.

### P1 — figure pipeline does not carry the design into HTML

Affected current figure pages: chapters 1, 5, 7, 8, 10, and 18.

Relevant locations:

- `R/setup.R:38`
- `R/theme_book.R:121–138`
- `R/theme_book.R:235–256`
- `_quarto.yml:242–244`

**Correction**

- Add `fig.bg = "transparent"` to the global knitr options.
- Run each chapter setup chunk with `cache: false`; it establishes global theme
  state and should not be restored as an ordinary cached value.
- Either disable knitr cache while the book is being designed or add a
  `cache.extra` fingerprint covering `R/setup.R`, `R/theme_book.R`, and
  `design-tokens.yml`.
- Regenerate all existing figure assets and their frozen outputs.
- Prefer SVG for HTML; retain the established static print twin for PDF/Word.
- For dark mode, produce a dark asset or a CSS-addressable vector palette and
  switch explicitly. Do not invert rasters.
- Remove redundant in-plot titles when the HTML caption already names the
  figure.
- Increase figure base type and/or height on narrow screens. A 2 × 2 small
  multiple should become one column or receive a dedicated mobile asset.
- Reconsider the global accent-colored smoothing default. The accent should
  indicate “look here,” not merely “this geom is a smoother.”

### P1 — margin references fail at intermediate widths

The current media rule changes the appearance of margin notes below 1000 px but
does not fully reset their Quarto grid placement, height, or overflow. Measured
documents remain wider than their viewports at 1100, 1000, and 768 px. Long
DOIs can still escape even at smaller widths.

**Correction**

- At the breakpoint, explicitly return margin notes to the body column.
- Reset height and overflow to normal flow values.
- Apply `overflow-wrap: anywhere` to citation links and DOI/URL strings.
- Test 1200, 1100, 1000, 768, 600, 390, and 320 px, not only desktop and phone.

### P1 — navigation tools are nearly invisible in light mode

The paper navbar overrides its text links but leaves Quarto navigation tools and
the toggler with the light foreground inherited from a dark navbar. Source,
share, theme, reader-mode, and hamburger icons are consequently almost
white-on-paper. On phones they wrap into a ghost second toolbar row and the
fixed header can consume 149–170 px.

**Correction**

- Give navigation tools and the toggler explicit ink/ink-muted colors in light
  mode, with accent only on hover and focus.
- Move secondary tools into the phone menu.
- Use a deliberate short phone brand such as “Osnove statistike.”
- Remove or shorten the redundant current-page breadcrumb on phones.
- Disable the global source `Code` control in the reader edition, or localize it
  and move it out of the title row. Per-chunk “Prikaži kod” controls already
  serve the reader.
- Set `scroll-padding-top` and heading `scroll-margin-top` after the final
  header height is known.

### P2 — the type scale is compounded

Relevant locations:

- `styles/_tokens.scss:89`
- `_quarto.yml:222`

The root becomes 17 px and the body then applies `1.0625rem` again. Computed
body text is approximately 18.06 px, H2 is approximately 36.13 px rather than
34 px, and the desktop H1 reaches approximately 61.2 px.

**Correction**

Keep the SCSS design token as the single source of truth and remove the duplicate
Quarto size. After that correction, assess a phone-only H2 value within the
existing scale. Do not introduce page-specific body-size reductions.

### P2 — table styling treats text like data and width like a type problem

Global CSS makes all table cells monospaced and right-aligns all non-first
columns. Bootstrap stripes remain visible because they are cell inset shadows,
even though the local rule says no zebra. Several captions are centered.

**Correction**

- Use the prose sans treatment and left alignment for textual cells.
- Apply monospaced tabular numerals only to explicit numeric/identifier classes.
- Remove Bootstrap stripe variables or odd-cell shadows at their source.
- Left-align captions.
- Convert raw machine headers and underscores into short Croatian labels.
- Apply Croatian decimal commas after cache refresh.
- For narrow screens, prefer stacked records for semantically textual tables.
  Use an overflow wrapper only for tables whose column comparison is essential,
  and add a visible scroll cue and sticky first column.

### P2 — custom components assume DOM children that Pandoc does not emit

Consecutive inline spans/links are wrapped in one paragraph, while the CSS
expects them to be direct grid/flex children. This breaks:

- `.tjedan` on the schedule;
- `.hub-card` on the landing page;
- `.hero-cta` on the landing and 404 pages;
- the empty lecture card.

**Correction**

Prefer block-level authoring that produces the intended semantic children.
Where that is impractical, add a narrowly scoped `> p { display: contents; }`
bridge and verify keyboard focus and accessible reading order.

### P2 — chapter-opening and terminology systems are incomplete

Numbered chapter pages omit the designed chapter-number kicker, subtitle/lede,
and metadata strip. The global English `Code` control becomes more visually
prominent than the missing editorial opener. “Pojmovi” sections are dense
comma-separated paragraphs rather than the intended Croatian/English paired
presentation.

**Correction**

- Generate the opener consistently from metadata/filtering rather than
  hand-authoring it 18 times.
- Render term pairs as structured rows, with Croatian on the left and English
  on the right, stacked on phones.
- Localize remaining interface strings, including “Table of contents,”
  “Appendix/Appendices,” and source-code controls.

### P2 — all central widgets are unfinished

Chapters 1–17 show a bare monospace development message that points readers to
`data/widgets.json`. The surrounding “Što isprobati” disclosure is also
structurally broken: the lead paragraph is wrapped, but the following list
remains permanently visible.

**Correction**

- Implement the widgets before visual sign-off.
- Until then, hide the interaction section in reader-facing builds or use one
  deliberate “u izradi” frame that cannot be mistaken for failed output.
- Move the instruction list into the actual disclosure body.
- Add each finished widget and its static print twin to the visual-regression
  suite.

## Pre-remediation page-by-page audit

The recurring chapter defects are abbreviated below:

- **C1:** cited opening vignette clips behind the desktop sidebar and collides
  with its label on phones.
- **C2:** cited “Statistika u divljini” becomes a viewport-wide band; phone
  label, title, padding, and measure are poor.
- **C3:** central widget is a developer placeholder.
- **C4:** chapter opener omits kicker, subtitle, and metadata; global code tool
  is over-prominent.
- **C5:** current committed `docs/` page is a stale skeleton.

### Chapters

| Page | Findings and recommendation |
|---|---|
| **00 — Predgovor** | C1, C2, C5. The global Code menu is especially unnecessary because there is no reader-relevant source workflow. Once the callouts are corrected, the hierarchy, prose measure, citations, summary, and navigation are balanced. |
| **01 — Zašto statistika** | C1–C5. The figure has the white canvas, gray panel, stale defaults, and very small phone labels. Remove a redundant in-plot title, move/direct-label the legend, enlarge mobile type, and regenerate transparently. The small table itself fits. |
| **02 — Mjerenje i istraživački dizajn** | C1–C5. A five-column table is about 429 px inside a 315 px phone body and its rightmost data are clipped. Use shorter reader-facing labels, round the excessive precision, apply decimal commas, and provide a stacked or explicit scroll treatment. |
| **03 — Kako brojke zavode** | C1–C5. Its compact simulation table behaves well, but this identity chapter is left text-heavy because the central interaction is only a placeholder. Prioritize w03. |
| **04 — Sažimanje podataka** | C1–C5. The statistics table is about 586 px inside a 555 px desktop column and much wider than a phone body. Replace long underscored headers with short Croatian labels and reflow the metrics as rows/cards on phones. |
| **05 — Vizualizacija podataka** | C1–C5. The Anscombe plot is the clearest white/gray/default-blue mismatch. Its 2 × 2 facets are too small at 315 px; supply a one-column phone composition or taller mobile static twin. |
| **06 — Povezanost varijabli** | C1–C5. The model callout becomes disproportionately tall on phones. Its table is the best responsive table in this chapter group and should be used as a structural reference. |
| **07 — Vjerojatnost** | C1–C5. The histogram has an opaque white/default-gray treatment and tiny phone axes. This page also produces the tallest fixed mobile header in its group; simplify the phone navbar and regenerate the graph. |
| **08 — Uzorkovanje** | C1–C5. The CLT figure is a stale default-theme asset with a white canvas and small phone labels. This pedagogical hinge should receive an early widget/figure pass. Empty margin containers also leave floating rules. |
| **09 — Procjena** | C1–C5. The one-row table retains Bootstrap stripes and a decimal point. Remove the stripe shadow, left-align the caption, and apply Croatian formatting. |
| **10 — Logika testiranja** | C1–C5. The null-distribution graph repeats the opaque/default theme and has very small axes on phones. Regenerate it transparently and give the mobile version more height. |
| **11 — Veličina učinka i snaga** | C1–C5. The power table exposes a raw `N_PO_SKUPINI` header, decimal points, centered captioning, and zebra shading. The long page title itself wraps cleanly. |
| **12 — Kriza i obnova** | C1–C5. This has the worst vignette clipping and the largest phone dark callout (about 871 px). It is also the longest audited chapter. Correct callout padding/structure and double scaling rather than shrinking prose. Its data table otherwise has good Croatian labels and decimal commas. Prioritize w12 because this is an identity chapter. |
| **13 — Kategorički podaci** | C1–C5. The worked-example table mixes English category labels into Croatian prose and renders textual labels in monospace. Translate labels and reserve mono for numerals. It otherwise fits the phone width. |
| **14 — Uspoređivanje dviju grupa** | C1–C5. The table uses decimal points. The global Code control sits only a few pixels from the two-line title; remove it from the reader-facing opener. The table itself remains legible. |
| **15 — Uspoređivanje više grupa** | C1–C5. Raw headers such as `DIFF`, `LWR`, `UPR`, and `P ADJ` plus decimal points look like unprocessed software output; `0.00` falsely reads as exact zero. Localize and format the output. |
| **16 — Regresija, opći okvir** | C1–C5. The result table fits, but `ESTIMATE` and `STD.ERROR` and zebra shading remain raw. The missing regression widget is especially conspicuous at the book's conceptual summit; prioritize w16. |
| **17 — Statistika u doba algoritama** | C1–C5. The fairness table is about 541 px inside a 315 px phone body and has no visible scroll cue. Convert it to a vertical metric/value presentation or add an explicit comparison-table scroller. Long underscored headers and the missing w17 weaken another identity chapter. |
| **18 — Vaše prvo istraživanje** | C2, C4, C5. Its uncited vignette is the correct visual reference and does not clip. The first table is about 588 px in a 555 px desktop body and is clipped even before phone reflow; recast it as metric/value rows. The second table also exceeds the phone body. The regression plot repeats the opaque white/gray/default-blue problem. Divide the long worked example into numbered H3 steps using the existing worked-example treatment. |

### Landing, teaching, and support pages

| Page | Findings and recommendation |
|---|---|
| **index.html** | The default Quarto title/author/date block duplicates the custom hero and adds roughly 500 px on phones. Suppress the visible default block while retaining metadata. The custom `.hero-title` class is attached to a section, so its negative letter spacing and weight leak into the lede and visually collapse word spaces; target the H1 only. Hub cards run inline because of the paragraph-wrapper mismatch. The cover mockup is a very large blank white rectangle, especially on phones; remove it until a real cover exists or replace it with a restrained paper-native mark. The canonical `/` route fails standalone detection and retains the book sidebar, while `/index.html` works. |
| **interakcije.html** | All 17 inventory cards render and the four-column/one-column grid is clean. The filter is hidden under the inaccurate generic label “Parametri simulacije”; expose it as “Filtriraj interakcije.” Remove the orphan `§` separator. |
| **podaci.html** | A deliberately empty table renders as a header plus two dark rules, resembling the reported black bars. Replace it with one explicit empty state until data exist. Real source/license content will need stacked phone records or an intentional scroller. |
| **pojmovnik.html** | JavaScript runs, but the concept graph currently has zero nodes. Two duplicate generic control bars and two separate empty messages make the page look failed. Hide filters when empty and show one plain-language state; when populated, combine search and chapter filters into one glossary-specific control. The graph canvas itself is transparent and directionally correct. |
| **predavanja.html** | The empty lecture marker, title, and description run together because of the paragraph-wrapper mismatch. Use one full-width editorial empty state or remove the public navigation item until a deck is available. |
| **raspored.html** | Critical local defect: each week's number, topic, and status are one paragraph placed in the first narrow grid column. Topics wrap every few letters while most of the row is empty, creating pages about 3875 px desktop and 4175 px phone height. Re-author or flatten the children and give the phone layout explicit number/topic/status grid areas. The exposed “Projekt” section is also empty. |
| **resursi.html** | Six large empty H2 sections appear as a sequence of ruled blank bands. Hide the page while skeletal or replace the list with one compact “u izradi” state. |
| **silabus.html** | Five visible TODO values and seven empty sections make the page look broken. The desktop metadata block is strong, but its phone layout becomes one long column; a compact two-column phone summary is preferable once real values exist. |
| **uci-s-ai.html** | The export selector is mislabeled as simulation parameters. The complete mentor prompt becomes a very long soft-paper slab—several phone screens. Keep the copy action, show a concise preview, and disclose the full text behind “Prikaži cijelu uputu.” Remove the orphan `§`. |
| **404.html** | Under the configured production subpath the page is attractive, but serving it at the audit root breaks its absolute subpath assets and exposes raw unstyled content. Smoke-test both the production subpath and local preview. Phone CTA links also run together because of the shared paragraph-wrapper defect. |

The generic OJS control caption is also used for search, filtering, chapter
selection, and export selection. Each page should supply a task-specific label
rather than inheriting “Parametri simulacije.”

### Literature and appendices

| Page | Findings and recommendation |
|---|---|
| **references.html** | On a 390 px phone the document grows to about 486 px because DOI and URL strings do not wrap. Apply `overflow-wrap: anywhere`, reduce the phone hanging indent, and constrain desktop bibliography measure. Literature currently consumes “Appendix A,” making every following appendix letter wrong. |
| **Dodatak A — R praktikum** | Renders as “Appendix B — Dodatak A.” Code blocks are strong on desktop. On phones their horizontal scrolling has little visual cue, copy buttons obscure line endings, and comments have insufficient contrast. Add right padding beneath the copy control, a scroll cue, and a stronger muted-ink token. |
| **Dodatak B — Put bez koda** | Renders as “Appendix C — Dodatak B.” Apart from the title/localization defect and shared navigation/type issues, this is one of the strongest appendix layouts and needs no structural redesign. |
| **Dodatak C — Katalog podataka** | Renders as “Appendix D — Dodatak C.” Phone document width reaches about 533 px. The text-heavy table is forced into global monospace/right alignment. Recast each dataset as a stacked record: dataset, source, unit, and use. |
| **Dodatak D — Koji test kada** | Renders as “Appendix E — Dodatak D.” Phone document width reaches about 480 px. Recast each decision row as a structured record—outcome, design, and method—or provide a clearly signposted comparison scroller. |
| **Dodatak E — Rječnik pojmova** | Renders as “Appendix F — Dodatak E.” Phone document width reaches about 517 px. Use a two-column term/translation row at wider widths and place the chapter reference beneath it on phones; do not shrink glossary type. |
| **Dodatak F — Protokol za rad s asistentom** | Renders as “Appendix G — Dodatak F.” The page is structurally sound. Optional polish: number the protocol steps 01–04. |

**Appendix correction**

- Do not let the literature page consume an appendix letter.
- Choose one title system: either localized Quarto-generated “Dodatak X” or the
  authored title, never both.
- Localize “Appendix/Appendices.”
- Make the appendix sidebar scroll its active item into view or collapse earlier
  parts when the active appendix is below the desktop viewport.

## Dark mode

The core dark palette is readable and coherent. Its obvious failures are
inherited from light-mode structure:

- every broken dark callout becomes a page-wide light slab;
- current static figures remain opaque white/gray islands;
- the canonical landing route retains the book sidebar;
- the compounded rem scale remains oversized.

A transparent light-mode raster is not sufficient in dark mode because its dark
marks can disappear into dark paper. Use paired assets or a vector whose colors
can be switched deliberately.

## What already works

- The warm paper and restrained color use establish a convincing editorial
  identity.
- The normal desktop reading column remains close to the intended 66-character
  measure.
- Ordinary body prose, headings, summaries, exercises, and previous/next
  navigation generally do not overlap.
- The main type hierarchy is sound once its accidental 6.25% enlargement is
  removed.
- Folded code produces useful rhythm on long analysis pages.
- Margin references work well at full desktop width when they are outside
  custom callouts.
- Model and error callouts are distinct and generally responsive after the
  shared grid/padding issues are excluded.
- The interaction inventory, the non-code appendix, and the AI protocol show
  that the system can already produce calm, coherent pages.
- The design-token consistency check passes; the problem is not token drift but
  how generated HTML and cached assets consume those tokens.

## Recommended implementation sequence

### Wave 0 — establish a truthful build

1. Add cache dependencies and transparent figure-device settings.
2. Force-regenerate every current figure asset and inspect light/dark output.
3. Re-render the full book.
4. Add a stale-output CI gate.

### Wave 1 — remove the visually destructive defects

1. Introduce the body-wrapper/margin-sibling callout structure.
2. Constrain or redesign the dark callout.
3. Hide empty margin containers and body-bound exercise separators.
4. Fix the margin-reference breakpoint and DOI wrapping.
5. Correct light-navbar tools and phone header organization.

### Wave 2 — restore the specified hierarchy

1. Remove duplicate font scaling.
2. Implement chapter kickers, ledes, and metadata consistently.
3. Remove/localize global code tools.
4. Fix table stripes, captions, textual fonts, alignment, labels, and decimal
   formatting.
5. Repair the shared Pandoc paragraph-wrapper components.

### Wave 3 — page-specific responsive work

1. Redesign the schedule.
2. Reflow chapter 2, 4, 17, and 18 tables and appendices C–E.
3. Fix the landing-page title duplication, lede inheritance, cover placeholder,
   cards, and root-route standalone state.
4. Replace all exposed skeleton sections with deliberate empty states.
5. Correct literature/appendix numbering and localization.

### Wave 4 — content visuals

1. Implement and audit widgets 1–17 with their static twins.
2. Give identity chapters 3, 12, and 17 disproportionate visual attention.
3. Give chapter 8's sampling interaction and chapter 16's regression
   interaction early usability testing.
4. Recheck the chapter 18 capstone after the worked-example and table reflow.

## Visual acceptance criteria

A repaired build should meet all of the following:

- `docs/` contains current chapter prose and no skeleton marker intended only
  for drafting.
- No chapter callout decoration starts behind a sidebar.
- Vignette labels never share a row with or overlap their first sentence.
- No callout, exercise rule, margin note, DOI, or table expands the document
  beyond the viewport unless it is inside an explicit, keyboard-accessible
  scroller.
- Dark callouts use a consciously approved width in both themes.
- Every HTML figure has a seamless page background, current theme, legible
  phone labels, and an intentional dark-mode treatment.
- A change to the R theme or design tokens invalidates every dependent figure.
- Body text computes to 17 px at the standard root size.
- Light-navbar tools meet normal contrast and remain in one phone header row.
- All visible interface labels are Croatian.
- Every finished table identifies textual versus numeric columns semantically.
- Landing `/`, `/index.html`, support pages, and the production-subpath 404
  receive the intended standalone layout.
- Automated screenshots pass at 1440, 1100, 1000, 768, 600, 390, and 320 px in
  both light and dark modes.

## Pre-remediation final assessment

This is not a page-by-page typography failure. It is a good editorial system
whose generated grid, cache pipeline, and a few component assumptions are
currently overpowering the design. Fixing the shared callout structure,
truthful rendering, transparent figures, and duplicated type scale will remove
most of the conspicuous defects across the entire book at once. The remaining
work is then a finite set of responsive tables, unfinished states, landing-page
cleanup, localization, and widget implementation.
