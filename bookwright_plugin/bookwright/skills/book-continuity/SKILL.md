---
name: book-continuity
description: The whole book consistency checker and spine keeper for the "Osnove statistike za društvene znanosti" book. Use whenever you want to check the book for consistency across chapters, set or review the key aspects and key terms of a chapter, measure structural symmetry, or run the book wide voice and arc review. Reads every chapter, counts structural elements against the conventions, reconciles each chapter against its spine, checks terminology against the concept ledger, and dispatches the book wide critics. Never edits chapter prose. Trigger on phrases like check consistency, is the book homogeneous, propose the spine for chapter N, are the chapters symmetrical, run the arc or voice review.
allowed-tools: Read, Write, Bash
---

# Book Continuity (whole book)

## Purpose
Hold the book together across chapters. It measures structure against `${CLAUDE_PLUGIN_ROOT}/shared/conventions.json`, reconciles each chapter against `${CLAUDE_PLUGIN_ROOT}/shared/chapter-spine.json`, checks terminology against `${CLAUDE_PLUGIN_ROOT}/shared/concept-ledger.json`, and runs the book wide review. It reports and it maintains the shared registries. It never edits chapter prose.

## When to use
For a consistency sweep, to propose or revise a chapter spine, to measure structural symmetry across chapters, or to run the voice and arc review. For writing or repairing the elements use `book-structure` and `book-figure`. For per chapter critique use `book-review`.

## Modes
- `scan`. Run `Rscript ${CLAUDE_PLUGIN_ROOT}/skills/book-continuity/scripts/structure_scan.R chapters/*.qmd`. It prints, per chapter, opener presence and the counts of `Definicija`, figures, `callout-praksa`, `callout-empirija`, and the closing exercise. Read `shared/conventions.json` and flag any count outside its band and any non exempt chapter missing the opener. On the first run, also report the current distribution and propose bands for you to ratify into `conventions.json`.
- `spine`. For a chapter, read it and propose a short set of key aspects and the handful of key terms that earn a `Definicija`. Present them. On approval, write them into `shared/chapter-spine.json` with `ratified` true.
- `terms`. Compare term usage against `shared/concept-ledger.json` and flag a term defined twice, used before its introducing chapter, or named differently for one concept.
- `panel`. Dispatch the book wide critics at `${CLAUDE_PLUGIN_ROOT}/agents/`, `critic-voice` and `critic-arc`, over the chapters, and synthesize the way `book-review` does, ranking by agreement.

If no mode is given, infer and say which.

## Workflow
Run the relevant detector or dispatch, gather results, and hand back a report. Writes are limited to the shared registries, chiefly `chapter-spine.json`, and only after you approve. Chapter files are never edited here.

## Quality gates / checklist
`assets/checklist.json`. Counts measured against the bands, spine ratified per chapter, terminology reconciled, book wide critics run for a full pass.

## Knowledge base & references
`reference/checks.md` (the consistency battery and the script versus reader split). `scripts/structure_scan.R` (the counting sweep). It reuses `${CLAUDE_PLUGIN_ROOT}/skills/book-figure/scripts/figure_intro_check.R` for the figure paragraph rule. Shared state at `${CLAUDE_PLUGIN_ROOT}/shared/`.

## Autonomy note
It diagnoses and proposes. It writes only the spine, only with your approval, and it never touches chapter prose. You ratify the spine and the bands, and you decide what to fix.
