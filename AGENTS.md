# AGENTS.md — Osnove statistike za društvene znanosti

## Agent operating layer

This is the canonical operating manual for both Codex and Claude Code. Codex
loads it directly. `CLAUDE.md` imports it for Claude Code. Keep shared project
rules here so the two hosts cannot drift.

Before book-content work, read `notes/struktura-knjige.md` for scope,
`STYLE.md` for editorial rules, `ENRICHMENT.md` for substantive additions, and
`DESIGN.md` before visual changes. Preserve unrelated working-tree changes.
Never hand-edit `docs/` or `_freeze/`.

Bookwright lives at `bookwright_plugin/bookwright/` and is packaged for both
hosts. Use its skills when the task matches:

- `book-conductor` for status, routing, outside asks, and final checkpoints
- `book-style` for chapter prose edits and style sweeps
- `book-enrich` for substantive chapter enrichment
- `book-figure` for figure-introduction checks
- `book-review` for the six-critic chapter panel
- `book-continuity` for cross-chapter structure, terminology, voice, and arc

If the installed plugin is unavailable in the current session, read the
matching `SKILL.md` directly and follow it. Installed skills become discoverable
in a new thread.

Bookwright critic panels are explicitly multi-agent workflows. Run independent
critics in parallel when subagents are available, wait for all requested
critics, and synthesize their findings. Critics are read-only. Codex project
definitions live under `.codex/agents/`; host-neutral prompts live under
`bookwright_plugin/bookwright/agents/`.

Installed plugins run from a cache. Treat
`bookwright_plugin/bookwright/shared/` in the active Git checkout as the only
mutable Bookwright state. Never update a ledger or registry in an installed
plugin cache.

Bookwright R commands must not assume `Rscript` is on `PATH`. Invoke them
through:

```text
python bookwright_plugin/bookwright/scripts/run_rscript.py <script.R> [args...]
```

Pass concrete paths to shell commands; do not rely on Bash-style environment
variable expansion in PowerShell.

## Comprehensive-review packet workflow

The ratified comprehensive-review programme is controlled by four checkout-
local files:

- `notes/reports/comprehensive-review-implementation-plan-2026-08-03.md`
  defines scope, decisions, dependencies, packets, and gates;
- `notes/reports/comprehensive-review-implementation-register.yml` is the
  authoritative work and status register;
- `notes/reports/comprehensive-review-forward-handoffs.yml` is the durable
  queue for discoveries that constrain later packets;
- `notes/reports/comprehensive-review-dashboard.md` is the human-readable
  current-state view and contains the exact next-thread prompt.

Read all four completely before comprehensive-review implementation work. Do
not rely on prior chat. Execute only `next_permitted_packet`, keep at most one
write packet active, and stop after closing that packet. Before its first
substantive edit, acknowledge every applicable incoming handoff; before
closeout, consume it with a recorded disposition and evidence. A packet cannot
close until it records either all outgoing handoffs or an explicit declaration
that it found no future-relevant effect. Never leave a discovery needed by a
later packet only in chat.

Update the register, handoff ledger, and dashboard together at packet closeout,
then run:

```text
python bookwright_plugin/bookwright/scripts/run_rscript.py scripts/check-review-workflow.R
```

Only the root/conductor agent writes these control files or Bookwright shared
registries. Parallel critics and workers remain read-only on them. Local,
scoped packet commits are authorised; push, merge, tag, archive, and deployment
still require separate explicit authorisation.

## Project overview

A Quarto book teaching statistics to undergraduate social-science students —
sociology, political science, psychology, communication, economics — who must
be able to **understand research**, not become analysts. No mathematics beyond
secondary school is assumed, and no programming.

The full plan (audience, promise, per-chapter scope, widget inventory,
production phases, open decisions) is [notes/struktura-knjige.md](notes/struktura-knjige.md).
Read it before drafting any chapter. This file is the operating manual; that
one is the blueprint.

**All prose must be written in Croatian (hr-HR).** Do not draft chapter content
in English.

**Status: substantive draft under comprehensive-review revision.** Every
chapter file has content and the shared structural components, but all 19
ledger units remain at `draft` until the ratified revision gates are passed.
The engine is operational, with known governance and release safeguards still
scheduled in the implementation register.

## The four promises

After reading, the student can:

1. critically judge statistical claims met in media, reports and AI output;
2. describe and visualise a dataset honestly;
3. read, interpret and modestly reproduce the inferential analyses that
   dominate published social science;
4. work with an AI assistant on quantitative tasks in a disciplined way —
   delegating computation while keeping judgment, verification and
   responsibility.

**Out of scope, stated in the preface and not smuggled back in:** time series,
factor analysis and psychometrics, multilevel models, the mathematics of
machine learning (its concepts and social consequences get chapter 17), and
full Bayesian inference (a framed box in chapter 10, an outlook paragraph in
chapter 16).

## The five design principles

These are binding on every chapter, not a manifesto.

1. **Simulation before formulas.** Every inferential idea is first experienced
   through resampling, then named.
2. **Estimation over ritual.** Effect sizes and intervals lead; significance
   testing is taught with its history and its abuses.
3. **Literacy as content.** Reading other people's numbers is a first-class
   subject, not a motivational aside.
4. **Computation in the browser.** Interactive widgets carry the
   demonstrations, code is folded, print gets static figures through the
   filter chain.
5. **AI as instrument and as subject.** Every reader has an assistant; the book
   teaches disciplined use of it and treats algorithms as objects of social-
   scientific study.

## Chapter skeleton (fixed core)

Every retained chapter file already carries this shared core. Numbered chapters
1–17 use all seven parts. The preface has no widget; chapter 18 has no widget
and deliberately turns its central body into one extended worked example. Do
not reorder the applicable parts or add a section outside them without
recording the decision in STYLE.md.

1. **Vinjeta** — `::: {.callout-vinjeta}`. A real opening case, one page, always
   a question someone actually faced.
2. **Izgradnja pojma** — prose and figures develop the idea, lecture style.
3. **Interakcija** — in chapters 1–17, one central widget in the digital
   edition and its static twin in print (see the twin pattern below).
4. **Statistika u divljini** — `::: {.callout-divljina}`. A genuine published
   claim, poll, headline or chart, dissected.
5. **Pitajte model** — `::: {.callout-model}` for how to use an assistant on
   this chapter's task, then `::: {.callout-greska}` with a short AI-produced
   analysis containing exactly one realistic mistake the reader must find.
6. **Razrađeni primjer** — one complete analysis, narrated, code folded.
7. **Sažetak i pojmovi** — closing summary `{.sazetak}`, key terms in Croatian
   and English `{.pojmovi}`, then four exercise tiers: konceptualni, računski,
   kritički, revizija modela (grade an AI-generated solution).

## Structure

25 source files: 18 numbered chapters plus a preface, in five parts and a
finale, plus six appendices. The canonical order is `_quarto.yml`.

- **Predgovor** (`00-predgovor`) — optional; delete if the landing page carries it
- **DIO I — Statističko mišljenje** (1–3): zašto statistika, mjerenje i dizajn,
  kako brojke zavode
- **DIO II — Opisivanje podataka** (4–6): sažimanje, vizualizacija, povezanost
- **DIO III — Od uzorka do populacije** (7–9): vjerojatnost, uzorkovanje, procjena
- **DIO IV — Zaključivanje** (10–12): logika testiranja, veličina učinka i snaga,
  kriza i obnova
- **DIO V — Modeli** (13–17): kategorički podaci, dvije grupe, više grupa,
  regresija, doba algoritama
- **ZAVRŠNICA** (18): vaše prvo istraživanje

Appendices in `dodaci/`: A R praktikum, B put bez koda (jamovi), C katalog
podataka, D koji test kada, E rječnik pojmova, F protokol za rad s asistentom.

**Three chapters carry the book's contemporary identity** and get
disproportionate care: 3 (kako brojke zavode), 12 (kriza i obnova),
17 (doba algoritama). Chapter 8 (uzorkovanje) is the pedagogical hinge and
chapter 16 (regresija) is the summit.

## Navbar / site structure

| Tab | Source |
|-----|--------|
| Knjiga | `chapters/00-predgovor.qmd` |
| Interakcije | `interakcije.qmd` — hub of all widgets |
| Praktikum | `dodaci/a-praktikum.qmd` |
| Pojmovnik | `pojmovnik.qmd` — glossary + concept graph |
| Podaci | `podaci.qmd` |
| Uči uz AI | `uci-s-ai.qmd` |
| Nastava (dropdown) | `predavanja.qmd` · `silabus.qmd` · `raspored.qmd` |
| Resursi | `resursi.qmd` |

## Build commands

```bash
quarto preview                    # live preview
quarto render                     # full HTML build to docs/
quarto render --profile kolegij   # teaching edition to docs-kolegij/ (code unfolded)

powershell -File scripts/render-book-pdf.ps1    # pdf/Statistika.pdf
powershell -File scripts/render-book-docx.ps1   # word/Statistika.docx (manuscript)

python bookwright_plugin/bookwright/scripts/run_rscript.py scripts/check-tokens.R
python bookwright_plugin/bookwright/scripts/run_rscript.py R/build-ai-exports.R
python bookwright_plugin/bookwright/scripts/run_rscript.py R/build-concept-graph.R
```

Never run a bare `quarto render --profile pdf`. Quarto merges `book.appendices`
additively, so the profile cannot shrink the appendix list; the PowerShell
script rewrites the block for the duration of the render and always restores it.

## File layout

```
chapters/             18 chapters + preface (canonical order: _quarto.yml)
dodaci/               appendices A–F
widgets/              widget inventory, template and build order
styles/               _tokens.scss (design), _base, _callouts, _widgets,
                      _components, _nastava, custom.scss, _dark.scss,
                      styles.css, head.html (fonts), book-include.html,
                      statistika.theme + statistika-tisak.theme (syntax)
knjiga-stil/          the design package this identity was mapped from —
                      reference only, not a build dependency
R/                    setup.R (sourced by every chapter), theme_book.R,
                      build-ai-exports.R (pre-render hook), build-concept-graph.R,
                      fetch-podaci.R
scripts/              render-book-pdf.ps1, render-book-docx.ps1, check-tokens.R,
                      init-renv.R, svg-to-png.R
pdf-filters/          strip-ojs, swap-svg-png, strip-svg, book-callouts (Lua)
docx-filters/         book-callouts-docx, multiline-math-docx (Lua)
tex/                  theme.tex (print design layer), colophon.tex
data/                 datasets + generated ai-exports.json, concept-graph.json,
                      authored widgets.json
design/               incoming design material + brief (see DESIGN.md)
images/               static assets
notes/                struktura-knjige.md (the blueprint), specs, reports
predavanja/           reveal.js lecture decks (source + committed HTML)
fonts/print/          static font instances for the PDF (empty until chosen)
docs/                 HTML build output — do NOT hand-edit
_freeze/              Quarto execution cache — do NOT hand-edit
bookwright_plugin/    editorial-team tooling (manager + critics); not a build dep
AGENTS.md             canonical operating manual for Codex and Claude Code
CLAUDE.md             Claude Code import shim for AGENTS.md
index.qmd             landing page
references.qmd/.bib   bibliography
```

## Content conventions

### Editorial style
Every chapter follows [STYLE.md](STYLE.md) — hard rules H1–H10 and soft
conventions S1–S9. Run the linter and a full sweep before committing any
chapter prose edit.

### Substantive enrichment
Thickening an under-developed chapter follows [ENRICHMENT.md](ENRICHMENT.md) —
five value slots, an asymmetry test, and the constraint that examples come from
published social-science research, never invented.

### Citations
`[@key]` against `references.bib`. Margin citations are on. **Never cite from
memory and never invent a key, finding, page number or effect size.** If a
source is not in the bib, flag it. In a statistics textbook a fabricated number
is not a style slip, it is the failure the book exists to teach against.

### Pedagogical callouts

```markdown
::: {.callout-vinjeta}
Otvarajući slučaj poglavlja.
:::

::: {.callout-divljina}
**Naslov slučaja.** Rastavljena objavljena tvrdnja.
:::

::: {.callout-model}
Kako se ovaj zadatak radi s asistentom, što tražiti i što provjeriti.

> Sam upit, kao obični blok citat — CSS ga pretvara u mono traku.
:::

::: {.callout-greska}
Kratka AI-analiza s jednom greškom koju čitatelj mora naći.
:::
```

The category label is drawn by CSS. Do not type it into the box, and never
write a raw `<div>` or an inline style — if an element does not exist, ask for
the system to be extended rather than improvising one.

Three further authoring affordances, all specified in DESIGN.md §5:

```markdown
::: {.chapter-meta}
| Vrijeme čitanja | Widget | Podaci | Preduvjet |
|---|---|---|---|
| 28 min | Stroj za CLT | ESS HR 2023 | pogl. 4, 7 |
:::

…počiva cijelo [statističko zaključivanje]{.pojam
  def="Izvođenje tvrdnji o populaciji na temelju uzorka."
  en="statistical inference" ch="8"}.

::: {.widget-frame data-naslov="Stroj za CLT" data-oznaka="Widget 08.1 · interaktivno"}
```

`.pojam` gives a term a hover definition; it does **not** replace the `#def-`
div, since only `#def-` divs enter the glossary and the concept graph.

### Widget / print-twin pattern

Every widget ships with a static twin. The HTML gate carries the OJS chart, the
PDF gate carries the R chart. `scripts/render-book-docx.ps1` temporarily
rewrites the `pdf` gate to `docx` so Word gets the same static figures.

````markdown
::: {.content-visible when-format="html"}
```{ojs}
//| echo: false
viewof params = Inputs.form({ n: Inputs.range([10, 500], {value: 50, step: 10, label: "n:"}) })
```

```{ojs}
//| echo: false
//| label: fig-clt
//| fig-cap: "Opis grafa."
//| fig-alt: "Opis za čitače zaslona."
```
:::

::: {.content-visible when-format="pdf"}
```{r}
#| echo: false
#| label: fig-clt-print
#| fig-cap: "Isti sadržaj, statički."
```
:::
````

### Theorem and definition environments

```markdown
::: {#def-standardna-pogreska}
**Standardna pogreška** je standardna devijacija distribucije uzorkovanja
procjenitelja.
:::
```

Definition divs use `#def-` ids with the term bolded inside the defining
sentence, no label prefix. `#prp-`, `#thm-`, `#exm-`, `#exr-` are available and
Croatian-labelled in `_quarto.yml`. The concept graph
(`R/build-concept-graph.R`) is built from `#def-` divs, so a term that gets a
div enters the glossary automatically.

### R code in chapters

```r
source("R/setup.R")
```

This loads ggplot2/dplyr/tidyr, registers the book's typefaces, sets
`theme_knjiga()` and the geom defaults, fixes the random seed (2026 — the book
simulates constantly and figures must be stable across renders) and sets a
Croatian decimal comma.

Use `boje_knjige` and `scale_fill_knjiga()` / `scale_color_knjiga()` for
categories, `skala_naglasak()` when one series must stand out, `hr_broj` for
axis labels, and `sivo` / `scale_*_sivo()` for print twins.
**Never hardcode a hex in a chapter.**

Two rules the palette encodes. It is ordered **by lightness, not by hue**, so
the black-and-white print interior turns it into five distinct grays; past five
levels change the point shape or the fill pattern, never the tone. And **ochre
is not a data colour** — it means "you can touch this", so it enters a figure
only through `skala_naglasak()`, and then it means "look here", not
"this is category A".

### OJS / Observable
Interactive charts execute in the browser, not via R. The control panel is
wrapped into a collapsible `<details>` and given a reset button automatically by
`styles/book-include.html`, so the `.qmd` source stays clean.

## Design

The book's visual identity is **airy editorial**: warm paper, one ochre accent,
a book-grade serif, and a black-and-white print block. The full specification is
[DESIGN.md](DESIGN.md); read it before touching anything visual. The reference
package it was mapped from is kept in `knjiga-stil/`.

Five principles, binding on every element:

1. **Air is the material.** Hairlines and whitespace separate sections — never
   a box, a shadow or a rounded card.
2. **Ochre means touch.** The one accent is reserved for interaction and
   wayfinding. Never decoration, never a data colour.
3. **Black and white first.** Meaning is carried by rule weight, position and
   label. Every element must survive having its colour removed.
4. **Numerals are monospace**, tabular and lining, everywhere.
5. **Measure before width.** The text column never exceeds 66 characters.

Mechanically: design lives in exactly four files (`design-tokens.yml` is the
source of truth; `styles/_tokens.scss` and `tex/theme.tex` mirror it;
`R/theme_book.R` reads it). Four further files legitimately carry values —
`styles/_dark.scss`, `styles/head.html` and the two `.theme` syntax files —
and are listed in DESIGN.md §2. No other file may contain a raw hex or a font
name, and
`python bookwright_plugin/bookwright/scripts/run_rscript.py scripts/check-tokens.R`
enforces that.

**Code ligatures are off everywhere.** JetBrains Mono would otherwise paint R's
`<-` as `←`, and `<=` `>=` `!=` `%>%` as glyphs absent from the keyboard. The
reader is assumed to have no programming background and must be able to retype
every character they see.

## Deployment

Pushing to `main` triggers `.github/workflows/publish.yml`, which renders the
book with `quarto render`, attempts the PDF (`continue-on-error`), and uploads
`docs/` to GitHub Pages. Update `site-url` in `_quarto.yml`, `SITE_URL` in
`R/build-ai-exports.R` and the link in `design-tokens.yml` once the repository has its
real address.

## Commit conventions

- `copy(<slug>):` — prose/copy edit
- `style(<slug>):` — SCSS / layout / visual change
- `feat(<slug>):` — new feature or component (a new widget is `feat(w08):`)
- `fix(<slug>):` — bug fix
- `ci:` — GitHub Actions change
- `docs(<slug>):` — generated artifact rebuild (`docs(pdf):`)
- `build:` — render output

The slug is the chapter basename without the numeric prefix
(`copy(uzorkovanje):`), `landing` for `index.qmd`, `design` for token changes.

## Branching convention

Experimental features use the `experiment/*` prefix. When an experiment is
ready, cherry-pick or check out specific files into `main` — do not rely on
`git merge` blindly.

## Do NOT

- Hand-edit files in `docs/` or `_freeze/` — they are build artifacts
- Break the chapter order in `_quarto.yml`
- Write prose in English
- Put a raw hex or a font name in any file other than the four design files
- Invent a number, a study, an effect size or a citation key
- Add a Croatian empirical example without a verifiable source — the book's
  own subject is claims that cannot be checked
- Commit `_cache/`, `_files/`, `tmp/`, `.Rhistory`, or root-level `tmp_*` scratch
