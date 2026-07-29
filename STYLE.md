# Editorial style guide — Osnove statistike za društvene znanosti

This file is the single source of truth for prose style. It is meant to grow:
add a rule whenever a new editorial decision surfaces, following the lifecycle
at the bottom.

**Provenance.** Rules H1–H8 and S1–S7 are inherited, tested over a full
Croatian-language textbook. H9, S8 and S9 are new and specific to a statistics
textbook. IDs are stable and never renumbered.

**Scope.** Binding for every `.qmd` in `chapters/` and `dodaci/`. The standalone
pages (`pojmovnik`, `interakcije`, `podaci`, `resursi`, `uci-s-ai`, `silabus`,
`raspored`) follow the typography and citation conventions (S4, S5) but not the
structural-element formats. `index.qmd` is marketing register and exempt. All
prose is Croatian (hr-HR).

---

## The test

Every chapter must read like a printed manuscript — continuous prose where one
argument flows into the next. No structural scaffolding that signals "this was
assembled, not written." If a sentence reads like a slide bullet, summary box,
or signpost, it gets rewritten. When in doubt, read the passage aloud: if a
lecturer would not say it to a room, it does not belong on the page.

---

## Quick card

| ID | Rule |
|----|------|
| H1 | No colons in prose |
| H2 | No mid-sentence em dashes as list introducers or appositives |
| H3 | No mechanical transition formulae or takeaway announcements |
| H4 | No meta-structural callouts; no bullet/numbered lists in running prose |
| H5 | Restatement connectives at most once per chapter (whole family combined) |
| H6 | Titles and headings: em dash separator, nominal register |
| H7 | Every number, study, or named finding carries a `[@key]` in the same sentence |
| H8 | Bold only for first-mention concept anchors and definition terms |
| H9 | Notation discipline: no symbol without a prose gloss, no formula without an intuition before it |
| S8 | Simulation before formalism |
| S9 | Honesty about uncertainty, and about the assistant |

---

## Voice

The book speaks as one author: a seasoned lecturer writing, not talking —
confident, analytical, warm but impersonal. It never condescends about
mathematics and never pretends the reader will enjoy it automatically.

- **Person.** Authorial *mi* ("pokazali smo", "vraćamo se na"). The reader is
  addressed directly only in exercises, in the `Što isprobati` blocks beside
  widgets, and in the capstone chapter, which is deliberately first-person
  plural throughout because it walks through a study together.
- **Tense.** Present for methods and models, past for historical episodes,
  studies and the replication crisis narrative.
- **Distance.** No chatty asides, no exclamation marks, no irony markers.
  Humour, where it appears, is dry and embedded in the argument.
- **Sentence rhythm.** Vary sentence length. Three consecutive sentences
  sharing the same syntactic opener read as a list in disguise (see S3).
- **Statistics is not a morality play.** Researchers who p-hacked are not
  villains, and the reader is not being warned about bad people. The book
  explains incentives and procedures, and lets the reader draw the conclusion.

---

## Prose zones

"Prose" means every string a reader sees rendered.

| Zone | H1 colon | H2 em dash | Other rules |
|------|----------|------------|-------------|
| Paragraph prose | banned | banned mid-sentence | all apply |
| Headings | banned | **allowed** as separator | H6 |
| Chapter titles (YAML `title:`) | banned inside the title text | **allowed** as separator | H6 |
| Figure captions and alt text | banned | allowed as title-style separator at the start; banned mid-sentence | H7, H8 |
| Table cells | banned | banned | — |
| Table caption text | banned (the leading `: ` marker is Quarto syntax, exempt) | allowed as separator | see Tables |
| Callout bodies | banned | banned | all apply; see Callouts |
| Exercise stems | banned | banned | imperative voice allowed |
| YAML (other fields), code, OJS, URLs, math | exempt | exempt | exempt |

---

## Hard rules

### H1 — No colons in prose

Colons used to introduce lists, definitions, programmatic statements, or quoted
material break the rhythm of running prose. Eliminate all of them in every
prose zone. Restructure into new sentences, relative clauses, or indirect
formulations (see Repair patterns).

Exempt: YAML frontmatter, code blocks, URLs, math, and the leading `: `
table-caption marker — but the caption *text* after it must be colon-free.

### H2 — No mid-sentence em dashes as list introducers or appositives

Em dashes (`—`) used to introduce a list or appositive enumeration read as a
tic. Restructure with `koji uključuje`, a relative clause, or a new sentence.

Allowed: em dash as a *separator in title position* — chapter titles, section
headings, and the lead-in of a figure caption.

### H3 — No mechanical transition formulae

A transition must carry content. It names the substance it hands over, never
merely announces that an insight is coming. A transition that would fit equally
well in any chapter is a slot filler and gets cut. Varied slot fillers are still
slot fillers. If three adjacent sections open or close with structurally similar
phrasing, at least two are wrong.

### H4 — No meta-structural callouts; no lists in running prose

Avoid pullquote blocks dropped into prose to highlight a "key idea", sub-headers
that mechanically signpost the part title, section headings whose first sentence
restates the heading, and **bullet or numbered lists in running prose** — the
strongest slide tell. Fold enumerations into sentences or, if the material is
genuinely tabular, use a table with caption and source.

Numbered lists are sanctioned only inside `callout-greska` steps, the four
exercise tiers, `Što isprobati` widget-guidance blocks, and the procedural
passages of the praktikum and the capstone chapter.

**Kept** — the four pedagogical callouts. They have a defined instructional
purpose and their own format rules below.

### H5 — Restatement connectives at most once per chapter

The family: "Drugim riječima,", "Naime,", "Točnije,", "Ukratko,", "Jednostavnije
rečeno,", and the escalator "Štoviše,". **The budget is one occurrence per
chapter for the whole family combined**, and only when the restatement genuinely
sharpens something the previous sentence could not. Default to deleting the
connective and either dropping the restatement or merging the two thoughts.

### H6 — Titles and headings

- Em dash as separator, never a colon.
- Titles are **nominal phrases**. The em dash subtitle may be a question; a
  standalone interrogative title is avoided.
- Headings never hard-code numbering — Quarto numbers them.
- A heading's first sentence must not restate the heading (H4).

### H7 — Evidence anchoring

Every specific number, percentage, named study, or empirical finding carries a
`[@key]` citation **in the same sentence**. A magnitude remembered but unsourced
is either softened into an order-of-magnitude statement attributed to a
literature, or cut.

- If the source is not in `references.bib`, flag it — never cite from memory,
  never invent a key, finding, effect size, sample size or page number.
- Bib-key hygiene: the year in the key matches the edition cited.
- A theoretical work is never cited for an empirical claim it does not contain.

**This rule is load-bearing in this book.** A textbook that teaches readers to
distrust unsourced numbers cannot itself carry any. A fabricated citation here
is not a style slip; it is a contradiction of the book's subject.

### H8 — Bold discipline

Bold is kept for exactly two jobs: the **first-mention concept anchor** and the
bolded term inside a definition div. Never for mid-sentence emphasis, never as a
pseudo-heading inside a paragraph. Sanctioned exceptions: the literal lead-in
**Što isprobati.** in widget-guidance blocks, and the optional case title on the
first line of a `callout-divljina` or `callout-vinjeta`.

### H9 — Notation discipline

New in this book.

- **A symbol is introduced once, in prose, before it appears in a formula.**
  Write what it stands for in words in the same sentence that first shows it.
- **No display formula without an intuition paragraph before it.** The paragraph
  says what the formula does, not what it looks like. If the intuition cannot be
  written, the formula is not ready to appear.
- **One symbol, one meaning, book-wide.** The registry is the concept ledger
  (`bookwright_plugin/bookwright/shared/concept-ledger.json`). Sample statistics
  are Latin, population parameters Greek, and the distinction is stated the
  first time it matters and then held.
- **Derivations are not proofs of seriousness.** If a step can be replaced by a
  simulation the reader can run, it is (see S8).
- Inline math for a single symbol, display math for anything the eye must scan.

---

## Soft conventions

### S1 — Indirect questions over direct questions

Prefer an indirect formulation embedded in prose over a direct question. Direct
questions in **clusters** are fine when the rhetorical sequence is itself the
device. A single isolated question is the problem. The vignette is exempt — it
opens on a question someone actually faced, and that question may be direct.

### S2 — English parentheticals

A term of art gets its English original at most once, at first mention. The
Croatian term leads; the English follows in parentheses, italicised, with no
"engl." prefix — "**Standardna pogreška** (*standard error*)" — and only when
the literature genuinely lives under the English name. After first mention, the
Croatian term exclusively.

Statistics is the exception that proves the rule: Croatian statistical
vocabulary is inconsistent across faculties and students read international
literature, so the English original is *more* often justified here than in an
ordinary textbook. The bilingual pairing belongs in the chapter's `{.pojmovi}`
block and in Dodatak E, not scattered through the prose. More than six English
parentheticals in a chapter is still a register failure.

### S3 — Definition cadence

No glossary stacking: three consecutive sentences that each open with the term
they define read as a bulleted list with the bullets removed. Weave the
definitions into the argument, or give the load-bearing term a `#def-` div and
let the prose use it.

### S4 — Typography and numbers

- Croatian quotation marks „ovako", italics for foreign-language terms and
  titled works.
- **Decimal comma** (7,3 %), a space before % (write `7,3 %`). This is set in
  R via `options(OutDec = ",")` in `R/setup.R`; check that figures and tables
  actually honour it.
- In running argument, numbers one through nine in words, unless data, units,
  or formulas are involved.
- Ranges in prose are worded ("od 15 do 20 %"), not dashed.
- Report statistics as the book teaches them, not as SPSS prints them: an
  estimate with its interval, then the test, then the effect size. Never a bare
  p-value.
- No exclamation marks; ellipses only inside quoted material.

### S5 — Citations in prose

- `[@key]` sits at the end of the claim's sentence, before the full stop.
  Multiple keys in one bracket, chronological.
- Narrative attribution is for landmark works whose author matters to the
  argument — use sparingly, not as default.
- No footnotes for sourcing; margin citations render automatically.

### S6 — Cross-references between chapters

- The standard formula is textual: "u poglavlju o uzorkovanju", "kako smo
  pokazali u poglavlju o procjeni". Name the topic, not the number.
- One forward announcement per concept, in the chapter that motivates it; the
  receiving chapter owns the full development. The three planted seeds
  (causality in ch. 2, the linear model in ch. 14, prediction in ch. 16) are
  announced exactly once each and harvested where the plan says.
- When a chapter ends up referenced more than twice, add a `{#sec-...}` id and
  switch those references to `@sec-` links in a dedicated pass.

### S7 — Section rhythm

A chapter reads as evenly weighted, not as one essay with decorative headings
around a cluster of stubs. Two failure modes, each with a fixed remedy.

- **Monster section** — one `##` swallows the chapter, usually carrying `###`
  subsections. Remedy: **split**, promoting its `###`s to `##`.
- **Stub section** — a `##` the TOC promises, paid off with one or two
  paragraphs. Remedy: **merge up** or **thicken** via the ENRICHMENT.md slots.

The bands live in `conventions.json` under `structure` and are measured, not
guessed — run the detector once four or five chapters exist and ratify the real
distribution.

**The coda must be a destination, not an appendix.** The last body section
carries at least the chapter's median weight, or it does not exist as a separate
section. A chapter that fizzles into a one-paragraph "zašto je to važno" has
stopped rather than arrived.

**Weight is what the reader sees.** A section's weight is its rendered
footprint. Callouts, figures, widgets and tables count toward it — which also
exposes the opposite failure, the **scaffold section** that is mostly boxes and
charts with almost no argument connecting them. Its remedy is prose, not
reorganisation.

**Paragraphs have rhythm too.** Aim for paragraphs roughly between forty and one
hundred and thirty words; an isolated one-sentence paragraph is either promoted
into its neighbour or earned as a deliberate beat.

### S8 — Simulation before formalism

New in this book, and the operating form of design principle 1.

Every inferential idea is *experienced* before it is *named*. The order inside a
section is: the concrete situation, then the simulation the reader can run or
watch, then the name, then the formula, then the conditions under which it
fails. A section that opens with a definition and works toward an example has
the order backwards.

The widget is part of the argument, not an ornament beside it. Prose before the
widget says what the reader will see and why it matters here; prose after it
states what the reader should now believe. A widget with no paragraph on either
side is unfinished.

### S9 — Honesty about uncertainty, and about the assistant

New in this book.

- Every estimate the book reports carries its uncertainty in the same sentence.
  The book never writes "prosjek je 3,4" where "3,4 (95 % IP 3,1 do 3,7)" is
  available.
- Hedging is not the same as honesty. "Čini se da bi moglo postojati" is worse
  than a clear claim with a stated interval. State the finding, then its
  precision, then its limits.
- The `callout-model` box tells the reader what to ask, **what to verify, and
  where models typically fail** on this specific task. A box that only says "AI
  can help with this" has not been written.
- The `callout-greska` box contains **exactly one** realistic mistake, of a kind
  a real assistant actually makes — a plausible wrong number, a mis-specified
  test, a causal conclusion from correlational data, a confidently wrong
  interpretation of a p-value. Never a typo, never something absurd. The
  solution lives in the `kolegij` profile gate, never on the page.
- The book never claims that an assistant is unreliable in general or reliable
  in general. It shows a specific failure and a specific check.

---

## Structural elements

The sanctioned non-prose elements and their formats. Everything not listed here
is prose and follows the rules above.

**This section governs what goes in each element. Its visual form — the rule
weight, the label, the typeface — is specified in [DESIGN.md](DESIGN.md) §5 and
drawn by CSS.** Never type a category label into a box, never write a raw
`<div>`, never write an inline style. If an element you need does not exist,
ask for the design system to be extended; do not improvise one in a chapter.

### Vinjeta

`::: {.callout-vinjeta}`. Opens the chapter, immediately after the title. One
page at most, two to four paragraphs. A real case, a real decision, a question
someone actually faced. It ends on the question the chapter answers, and does
not answer it. No meta sentence announcing what the chapter will do.

### Interakcija

One widget per chapter, named and registered in `data/widgets.json`. Follows
the twin pattern (see CLAUDE.md). Preceded by one prose paragraph in chapter
voice saying what it shows and why it matters at this point in the argument;
the caption does not satisfy this, and a heading directly above a widget is a
violation. May carry one guidance block after it: the bold lead
**Što isprobati.** followed by numbered experiments sequenced from the obvious
case to the counterintuitive one.

### Statistika u divljini

`::: {.callout-divljina}`. One genuine published claim — a poll, headline,
chart, or report — dissected in continuous prose, at most two paragraphs. The
source is named and cited (H7 with no exceptions). The box shows the reasoning,
not the verdict: it takes the claim apart and lets the reader see where it holds
and where it does not. Never mocks the source.

### Pitajte model

`::: {.callout-model}` followed by `::: {.callout-greska}`. First beat: how to
use an assistant for this chapter's task, what to ask, what to verify, where
models typically fail. Second beat: a short AI-produced analysis containing one
planted realistic mistake. See S9 for what counts.

The prompt itself, when the box shows one, is written as an ordinary block
quote inside `callout-model`; CSS renders it as a monospace strip.

### Razrađeni primjer

A `##` section, not a box. One complete analysis narrated from question to
conclusion, with the code folded beneath the prose. The prose stands alone: a
reader who never opens a single code block still follows the whole analysis.
Every number in the narration comes from the code that is actually there.

### Sažetak i pojmovi

`## Sažetak {.sazetak}` — one paragraph, three to six sentences, in chapter
voice. It synthesises the chapter's *move*: what was established, what tension
remains, what it hands to the next chapter. No new citations, no new concepts,
no lists, and it must not reuse the vignette's sentences.

`## Pojmovi {.pojmovi}` — the chapter's key terms, Croatian and English side by
side, in the order the chapter introduced them. Every term with a `#def-` div
appears here; the reverse need not hold.

### Zadaci

Four tiers, in this order, each a `###` with class `{.zadaci-razina}`:

1. **Konceptualni** — no computation; the reader explains, distinguishes or
   predicts.
2. **Računski** — a calculation or a small analysis, with the data named.
3. **Kritički** — a published claim, chart or abstract to be judged.
4. **Revizija modela** — an AI-generated solution the reader must grade,
   naming what is right, what is wrong, and how they know.

Imperative voice. Each exercise names its deliverable. Solutions, where they
exist, are gated `::: {.content-visible when-profile="kolegij"}`.

### Definitions

```markdown
::: {#def-standardna-pogreska}
**Standardna pogreška** je standardna devijacija distribucije uzorkovanja
procjenitelja.
:::
```

One or two sentences, genus + differentia, no colon. The surrounding prose uses
the term immediately before or after the div. Which terms earn a div is a spine
decision, not a style one — and a `#def-` div automatically enters the concept
graph and the glossary.

A term that does not earn a div may still carry a hover gloss:

```markdown
[statističko zaključivanje]{.pojam def="Izvođenje tvrdnji o populaciji na
temelju uzorka." en="statistical inference" ch="8"}
```

This is a reading aid, not a definition. It does not enter the glossary, and it
does not discharge S2 — a term that needs its English original in prose still
gets it once, at first mention.

### Figures and tables

Every figure is preceded by one prose paragraph in chapter voice. Captions are
sentence-case, end with a full stop, and may use an em dash only as a
title-style separator at the start. Every figure carries `fig-alt`.

Table captions use Quarto syntax with a source every time:

```markdown
: Usporedba postupaka. Izrada autora prema @cohen1988. {#tbl-postupci}
```

No hard-coded numbering inside the caption text. The source formula is "Izrada
autora." / "Izrada autora prema @key." / "Prilagođeno prema @key." — never a
bare dangling "Izvor:".

---

## Repair patterns

- **Colon before a list** → split into a lead sentence plus a sentence per item,
  or a relative clause with `koji uključuje / obuhvaća`.
- **Colon before a definition** → make the definiens a clause, or move it to a
  `#def-` div.
- **Colon before a quotation** → introduce with `kako piše X,` or fold the quote
  into the sentence.
- **Em dash enumeration** → `koji uključuje...` or a new sentence.
- **Slot-filler transition** → replace with a sentence naming the actual
  substance being handed over; if nothing is handed over, delete.
- **Restatement connective** → delete the connective; merge the two sentences if
  the second adds anything, otherwise cut it.
- **Formula with no intuition (H9)** → write the intuition paragraph. If it
  cannot be written, the formula does not belong in this chapter.
- **Bare p-value (S4)** → add the estimate and its interval; the test follows,
  not leads.
- Never repair by deleting meaning. If the restructure loses a claim, the
  restructure is wrong.

---

## Linting

```bash
Rscript bookwright_plugin/bookwright/skills/book-style/scripts/style_lint.R chapters/<file>.qmd
Rscript bookwright_plugin/bookwright/skills/book-continuity/scripts/structure_lint.R chapters/<file>.qmd
```

Mapping: "colon in prose" → H1, "mid-sentence em dash" → H2, "mechanical opener
/ restatement" → H3/H5, "colon in chapter title" → H6. The linter is zone-blind,
so judge every hit against the Prose zones table. Known false-positive classes:

1. Table caption marker lines (`: Caption {#tbl-...}`) — syntax, not prose.
2. Table alignment rows (`| :--- |`).
3. Em dash as separator in headings and caption lead-ins.
4. Colons inside R and OJS code, and inside `$...$` math.

H4, H7, H8, H9 and the soft conventions are reader-checked; no detector sees
them. The structure linter reads its bands from `conventions.json`; those bands
are placeholders until the first four or five chapters exist and are measured.

---

## Workflow for editing a chapter

1. Read this file — it grows, and the newest rules are the ones the chapter most
   likely violates.
2. Run the linters; triage hits against the Prose zones table.
3. Fix H1/H2/H6 hits with the Repair patterns.
4. Check the structural elements against their formats: vignette, widget intro,
   divljina, the two AI boxes, worked example, summary, terms, four exercise
   tiers.
5. Sweep for H7 and H9: every number and named finding has its `[@key]`
   in-sentence; every symbol has a prose gloss; every formula has an intuition
   before it.
6. Re-read top to bottom for what no detector catches: slide cadence, glossary
   stacking (S3), register drift, bold abuse (H8), and whether the simulation
   really does precede the formalism (S8).
7. Verify the render and commit.

## Verification

Run `quarto preview chapters/<file>.qmd` and read the rendered HTML top to
bottom. Open the widget and actually move the controls. Read one paragraph aloud
from the beginning, middle, and end: if any of them sounds assembled rather than
written, the chapter is not done.

---

## Rule lifecycle

- IDs are permanent. New rules append (H10, S10, ...); nothing is renumbered.
- A soft convention is promoted to hard when it has been violated in at least
  two chapters **and** the fix produced a before/after pair worth recording.
- Every rule addition, promotion, or scope change gets a Provenance entry with
  the date and the triggering chapter.
- If a rule and actual book practice diverge, the divergence is resolved
  explicitly. Silent drift is the failure mode.

---

## Provenance

- **2026-07-29** — File created for this book. H1–H8 and S1–S7 carried over
  unchanged in substance from the editorial guide of *Javne politike u
  Hrvatskoj*, where they were distilled from a whole-book evaluation and a
  chapter-by-chapter sweep. Scope, examples and the structural-elements section
  rewritten for this book's seven-part chapter skeleton. Added H9 (notation
  discipline), S8 (simulation before formalism) and S9 (honesty about
  uncertainty and about the assistant), and extended S2 to acknowledge that
  statistical terminology justifies more English parentheticals than an ordinary
  textbook, and S4 to fix the reporting order for estimates.
