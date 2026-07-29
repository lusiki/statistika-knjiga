# Bookwright

Editorial tooling for the *Osnove statistike za društvene znanosti* Quarto book.
It is a small editorial team that lives beside the book repo so the work keeps
moving between review cycles.

## What is here

A manager, the per chapter jobs, the whole book checker, and eight read only
critics.

* `book-conductor` (manager). Tracks the status of every chapter, sorts each
  open task into what can be done now and what is blocked on an outside
  decision, and enforces the book checkpoints.
* `book-style`. Enforces STYLE.md, with an R linter that flags the hard rules.
* `book-enrich`. Applies ENRICHMENT.md, adding one or two paragraph insertions
  in one of five value slots. Never invents empirics.
* `book-figure`. Checks that every figure has a prose paragraph before it (R
  detector) and drafts the missing intro under STYLE.md.
* `book-review`. Runs the six critic chapter panel, synthesizes with agreement
  scoring, revises with your confirmation.
* `book-continuity`. Whole book, read only. Counts structure against
  `conventions.json`, reconciles each chapter against `chapter-spine.json`,
  checks terminology, and dispatches the two book wide critics.
* `agents/`. Six chapter critics (economist, skeptic, pedagogy, evidence, style,
  structure) plus two book wide critics (voice, arc).

The `critic-economist` agent is inherited from the previous book and is the
weakest fit here. Either retarget it as a methods critic (does the chapter get
the statistics right, are the assumptions stated, is the interpretation
defensible) or drop it from the panel. Decide before the first review cycle.

## Two file types

MD files are the instructions Claude reads (every SKILL.md, every critic, the
reference docs). JSON files are the lists Claude checks and the data it carries
(the checklists, the schemas, and the ledgers in `shared/`).

## The shared files

All four are **seeded and empty**, which is correct for a skeleton repo.

* `shared/chapter-ledger.json` — the live dashboard, pre-filled with all 19
  chapter files at stage `stub`. Move a chapter's stage as it progresses.
* `shared/concept-ledger.json` — the running list of defined terms. A term
  enters when it gets a `::: {#def-…}` div. Must stay consistent with
  `data/concept-graph.json`, which is built from the same divs.
* `shared/conventions.json` — structural bands and labels. **The numbers are
  starting guesses.** Run `book-continuity scan` once four or five chapters
  exist, measure the real distribution, and replace them. Until then the
  structure linter reports noise.
* `shared/chapter-spine.json` — per chapter key aspects and key terms that the
  vignette, the definitions and the exercises all reconcile to. Empty;
  `book-continuity spine` proposes them from the plan and you ratify.

## Install (local marketplace)

From Claude Code, add this folder as a local marketplace and install the
`bookwright` plugin. Run Claude Code from inside the book repo so the skills can
see `chapters/`, `references.bib`, `STYLE.md`, and `ENRICHMENT.md`.

## Use

Open the book repo and ask in plain language.

* where does the book stand → book-conductor reports the dashboard
* what can I work on next → book-conductor routes the work
* sweep chapter 8 for style → book-style runs the linter then the pass
* check the figures in chapter 5 → book-figure runs the detector
* enrich chapter 12 → book-enrich proposes insertions for approval
* review chapter 8 → book-review runs the critic panel
* check consistency across the book → book-continuity scans and runs the voice
  and arc critics
* propose the spine for chapter 3 → book-continuity proposes key aspects and
  terms

## Not included

A writer that drafts and repairs the vignette, the definition wording and the
four exercise tiers against the spine. Until it exists, `book-continuity` and
the structure critic tell you what is off and you write the fix by hand. Widgets
and figures generated from data are also out of scope; those are specified in
`widgets/README.md`.
