---
name: book-review
description: Review a drafted chapter of the Osnove statistike za društvene znanosti book with a six-critic panel. Use when the user asks to review, critique, pressure-test, obtain a second opinion on, or check a chapter before final. Dispatch independent read-only critics for statistical methods, skepticism, pedagogy, evidence, style, and structure; synthesize agreement and disagreement; revise only changes the user approves.
allowed-tools: Read, Edit, Bash
---

# Book Review

Give each drafted chapter six independent readings, then synthesize rather than
vote. The chapter is Croatian; critics judge their assigned lens.

## Panel

1. `critic-methods` — statistical correctness, assumptions and interpretation
2. `critic-skeptic` — hidden assumptions, alternative explanations and overclaim
3. `critic-pedagogy` — beginner comprehension, sequencing and exercises
4. `critic-evidence` — bibliography integrity and empirical support
5. `critic-style` — manuscript qualities a linter cannot judge
6. `critic-structure` — vignette, definitions, figures, AI boxes and exercises

Use the host-neutral prompts under `<plugin-root>/agents/`. For Codex, prefer
the corresponding read-only project agents `critic_methods`,
`critic_skeptic`, `critic_pedagogy`, `critic_evidence`, `critic_style`, and
`critic_structure` when the runtime can select named agents. Otherwise spawn
generic read-only subagents and include the complete role prompt in each task.
Claude Code may dispatch the Markdown agent definitions directly.

Run independent critics in parallel when subagents are available. If the host
cannot spawn subagents, run all six roles sequentially with isolated headings
and disclose the fallback. Never silently skip a critic.

## State and path resolution

Resolve `<repo-root>` from the active Git checkout. Read mutable state from
`<repo-root>/bookwright_plugin/bookwright/shared/`, not from an installed plugin
cache. Resolve `<plugin-root>` from the installed environment or this
`SKILL.md`; use it for read-only role prompts, references, and checklists.

Before dispatch, load the target chapter, live `chapter-spine.json` and
`concept-ledger.json`, `references.bib`, `STYLE.md`, and the relevant plan. A
full pre-final review requires a ratified chapter spine. If the spine is absent
or unratified, label the review provisional and route that gap to
`book-continuity spine`.

## Workflow

1. Confirm the target chapter and review mode.
2. Run the style linter, structure scan, and figure-introduction detector before
   dispatch. Include concise results so reader critics do not duplicate
   mechanical checks.
3. Dispatch all six critics with the same target and shared context contract.
   Each returns scores, strengths, concerns with severity/location/reason/fix,
   and a one-line verdict. `critic-evidence` also returns
   `missing_or_unverified`.
4. Merge equivalent concerns and count cross-critic agreement. Rank first by
   severity and then by agreement, so a fatal single-lens methods error never
   falls below duplicated minor comments. Surface disagreements as explicit
   trade-offs; never average them away.
5. Return one panel report with critic coverage, ranked concerns, disagreements,
   strengths and a verdict.
6. Propose revisions only for accepted findings. Show the relevant before and
   after, insert no unverified citation or empirical claim, and edit only after
   user approval.
7. A passing panel may advance a chapter to editorial/co-author review when the
   user approves. It never marks the chapter `final`; the conductor owns final
   checkpoints.

Use `review` for the full panel and `single-critic` only when the user explicitly
requests one lens. Follow `reference/panel.md` and `assets/checklist.json`.
