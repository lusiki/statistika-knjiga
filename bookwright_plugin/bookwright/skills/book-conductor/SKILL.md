---
name: book-conductor
description: Manage the Osnove statistike za društvene znanosti book. Use for a chapter-status dashboard, choosing the next task, routing work that can proceed versus work needing an author or external decision, drafting a bounded outside ask, or checking whether a chapter may be marked final. Read and update the chapter ledger, apply routing rules, and enforce book checkpoints.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
---

# Book Conductor

Keep the book's state in one ledger and answer three questions: where every
chapter stands, what can proceed now, and what genuinely requires outside input.

## Inputs and path resolution

Resolve `<repo-root>` from the active Git checkout and use
`<repo-root>/bookwright_plugin/bookwright/shared/chapter-ledger.json` as the
state source. Installed plugins run from a cache, so never write mutable state
under an installed `<plugin-root>`. Resolve `<skill-root>` as the directory
containing this `SKILL.md`. Use `<skill-root>/assets/routing-rules.json` for
routing and `<skill-root>/assets/checklist.json` for final checks. Read the
repository's `AGENTS.md`, `STYLE.md`, `ENRICHMENT.md`,
`notes/struktura-knjige.md`, `references.bib`, `chapters/`, and `data/` as
needed.

Resolve `<plugin-root>` by walking up from the actual location of this
`SKILL.md`. A host-provided plugin-root variable may be used only after checking
that it resolves to the same existing directory. Pass concrete absolute paths
to shell commands; do not depend on shell-specific variable syntax.

## Modes

Infer the mode when omitted and state the selected mode.

1. `status` — Read the ledger and emit one line per chapter with its stage,
   count of open self items, and count of outside asks. Group by stage. Surface
   failed renders and every open outside ask. Follow
   `<skill-root>/reference/status-report.md`.
2. `route` — Sort each open item through `assets/routing-rules.json`. Work is
   `self` when the repository already contains the evidence, data, rules, or
   authority needed. Record it in `self_items`. Work becomes an outside ask when
   it needs a new source not yet verified, a licence/access decision, course
   policy, scope choice, or authorial sign-off. Record it in `coauthor_asks`;
   that legacy field name means any author, co-author, or external decision.
3. `ask` — Draft one small request per outside item using
   `reference/coauthor-asks.md`. Name the exact evidence or decision, expected
   form, insertion point, owner, and why repository evidence cannot resolve it.
4. `check` — Run the chapter through `assets/checklist.json`. Execute
   deterministic checks where available and report judgment checks separately.
   Do not mark a chapter final while a blocking item fails.

Write ledger changes only when the user requested a state change or approved a
proposed routing decision. Preserve existing notes and unrelated entries.

## Quality gates

Never invent a citation, study, empirical quantity, page, or source. Croatian
examples follow the same rule as all others: use them when verifiable and flag
them when not. Require a clean targeted render, cleared style checks, figure
introductions, a resolved chapter spine, consistent terminology, all four
exercise tiers, and no unresolved blocking contradiction before `final`.

## References

Load `<skill-root>/reference/status-report.md` for dashboards and
`<skill-root>/reference/coauthor-asks.md` for bounded requests. Use the shared
schemas when editing ledger JSON.
