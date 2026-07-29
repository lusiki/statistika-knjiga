---
name: book-review
description: Run the chapter review panel on a chapter of the "Osnove statistike za društvene znanosti" book. Use whenever the user wants a chapter reviewed, critiqued, pressure tested, or checked before calling it done, or asks for a second opinion on a chapter. Dispatches six read-only critics (economist, skeptic, pedagogy, evidence, style, structure), synthesizes their findings with cross-critic agreement scoring, and lets a reviser apply changes only after you confirm. The critics stand in for the substantive review a co-author or reviewer would otherwise give.
allowed-tools: Read, Edit
---

# Book Review (per-chapter panel)

## Purpose
Give a chapter the second opinion that absent co-authors are not providing. Six critics each read the chapter through one lens and return a structured critique. A synthesizer merges them and ranks issues by how many critics flagged the same thing. A reviser then implements agreed fixes, but only after you confirm.

## When to use
On a chapter that is drafted and enriched, before you mark it final, or any time you want it pressure tested. The chapter is Croatian. Critics judge substance and clarity, not the choice of language.

## The panel
Dispatch each critic at `${CLAUDE_PLUGIN_ROOT}/agents/`. They read and score, they never write. Each reads `${CLAUDE_PLUGIN_ROOT}/shared/chapter-spine.json` first so the panel concentrates on the load bearing terms.
- `critic-economist`. Correctness of the economics and the public choice framing, and policy relevance.
- `critic-skeptic`. Missing counterview, and value judgments stated as fact.
- `critic-pedagogy`. Second year comprehension, the learning path of the key terms, exercise quality.
- `critic-evidence`. Every `[@key]` in `references.bib`, no fabrication, and unsourced Croatian empirics flagged.
- `critic-style`. The subtle STYLE.md failures the linter cannot catch.
- `critic-structure`. Whether the opener, the chosen definitions, the figure intros, and the exercises fit the chapter spine.

The critics have deliberately clean boundaries so the agreement score means something, correctness to economist, balance to skeptic, sourcing to evidence, learnability to pedagogy, prose to style, structure to structure.

## Workflow
1. Load the chapter, `${CLAUDE_PLUGIN_ROOT}/shared/chapter-spine.json`, and `${CLAUDE_PLUGIN_ROOT}/shared/concept-ledger.json`.
2. Dispatch the six critics on the chapter. Collect each structured critique (scores, strengths, concerns with severity and location and fix, verdict).
3. Synthesize. For each concern, count how many critics raised it and rank high agreement first. Surface disagreements as an explicit trade off, do not average them away. Write the panel report.
4. Revise only what you approve. The reviser preserves the integrity rails, it inserts no citation that is not in `references.bib` and no Croatian empiric. Show a before and after for each change and wait for confirmation.
5. Update the ledger stage if the chapter passes.

## Modes
`review` (full six critic panel), `single-critic` (one named critic only). Infer if unspecified.

## Quality gates / checklist
`assets/checklist.json`. All six critics run, an agreement scored synthesis is produced, reviser changes are confirmed before any write, no fabricated citation, no auto inserted Croatian empiric.

## Knowledge base & references
`reference/panel.md` (the critics, the agreement scoring, the reviser loop). The critic files live at `${CLAUDE_PLUGIN_ROOT}/agents/`.

## Autonomy note
The critics only read and advise. The synthesizer surfaces disagreement rather than hiding it. Nothing is written until you confirm. You own every claim and every edit.
