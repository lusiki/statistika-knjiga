---
name: book-continuity
description: Check consistency across the Osnove statistike za društvene znanosti book. Use to scan chapter structure, propose or ratify a chapter spine, reconcile terminology, compare chapters for symmetry, or run the whole-book voice and narrative-arc panel. Maintain shared registries when approved, report findings, and never edit chapter prose.
allowed-tools: Read, Write, Bash
---

# Book Continuity

Hold the book together across chapters. Resolve `<repo-root>` from the active
Git checkout and read live `conventions.json`, `chapter-spine.json`, and
`concept-ledger.json` from
`<repo-root>/bookwright_plugin/bookwright/shared/`. Installed plugins run from a
cache, so never write shared state under an installed `<plugin-root>`. Treat
`notes/struktura-knjige.md` as the plan and `_quarto.yml` as canonical chapter
order.

Resolve `<plugin-root>` from the installed environment or this `SKILL.md` path.
Use concrete paths in commands. Run R checks through
`<plugin-root>/scripts/run_rscript.py` so Windows does not require `Rscript` on
`PATH`.

## Modes

- `scan` — Run `structure_scan.R` over `chapters/*.qmd`. Report
  `callout-vinjeta`, `#def-` definitions, figures, `callout-divljina`, the two AI
  boxes (`callout-model` and `callout-greska`), and all four exercise tiers.
  Compare counts with `shared/conventions.json`. Starting bands are provisional
  until four or five chapters contain real prose.
- `rhythm` — Run `structure_lint.R` over the requested chapters and report its
  candidates without editing prose.
- `spine` — Propose the chapter's small set of load-bearing aspects and key
  terms from the plan and draft. Present it first; write
  `shared/chapter-spine.json` only after approval and set `ratified` accurately.
- `terms` — Compare definitions and usage against `concept-ledger.json`. Flag a
  term defined twice, used before its introducing chapter, or named two ways.
  Update registries only after approval.
- `panel` — Run `critic-voice` and `critic-arc` as independent read-only
  subagents and synthesize agreement and disagreement.

For Codex, prefer the project agents `critic_voice` and `critic_arc` under
`.codex/agents/`. For Claude Code or another host, dispatch the host-neutral
prompts under `<plugin-root>/agents/`. If subagents are unavailable, run the
roles sequentially with separate outputs and say that the fallback was used.

## Command pattern

```text
python <plugin-root>/scripts/run_rscript.py <plugin-root>/skills/book-continuity/scripts/structure_scan.R "chapters/*.qmd"
```

## Boundaries

Report and maintain shared registries; never edit chapter prose in this skill.
Use `book-style`, `book-enrich`, or `book-figure` for approved repairs. Follow
`reference/checks.md` and `assets/checklist.json`.
