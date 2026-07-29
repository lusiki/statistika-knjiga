# Architecture

Bookwright treats the book as a matrix. One axis is the lifecycle of each
chapter (`stub`, `draft`, `enriched`, `style_swept`, `figures_done`,
`coauthor_review`, `final`). The other axis contains work that only makes sense
across the complete book, including terminology, structural rhythm, voice, and
the narrative arc.

## Components

Six skills divide the work by responsibility:

- `book-conductor` owns status, routing, outside asks, and final checkpoints.
- `book-style` owns the `STYLE.md` prose pass.
- `book-enrich` owns the five `ENRICHMENT.md` value slots.
- `book-figure` owns figure-introduction checks.
- `book-review` owns the six-critic chapter panel and approved revision loop.
- `book-continuity` owns whole-book structure, spines, terms, voice, and arc.

Eight read-only critic roles live under `agents/`. The chapter panel contains
`critic-methods`, `critic-skeptic`, `critic-pedagogy`, `critic-evidence`,
`critic-style`, and `critic-structure`. The whole-book panel contains
`critic-voice` and `critic-arc`.

Four mutable registries live under `shared/`:

- `chapter-ledger.json` stores lifecycle and open-work state.
- `chapter-spine.json` stores ratified key aspects and key terms.
- `concept-ledger.json` stores canonical concepts and notation.
- `conventions.json` stores current structural names, widget policy, exceptions,
  and provisional count bands.

Every registry has a schema under `shared/schemas/`.

## Data flow

The conductor reads and updates the live chapter ledger. Worker skills read the
book contract and propose or apply work within their narrow responsibility.
Chapter critics read the same chapter and shared context independently; the
review skill merges equivalent findings, ranks severity before agreement, and
surfaces disagreement. Continuity checks chapters in `_quarto.yml` order and
updates a shared registry only after approval.

Installed plugin files provide read-only instructions and defaults. Mutable
state is read from the active repository's
`bookwright_plugin/bookwright/shared/` directory so an installed cache cannot
become a second source of truth.

## Routing

Work remains self-service when the repository already contains the authority,
source, data, or rule needed to complete it. This includes verifiable Croatian
and international evidence. Work becomes an outside ask only when it requires
an unresolved authorial choice, a new source or bibliography approval,
licensing or access, course policy, or a sign-off that repository evidence
cannot settle.

The legacy JSON field `coauthor_asks` is retained for compatibility. It means
any bounded author, co-author, course-owner, or external decision.

## Integrity rails

The evidence rail is geographic-neutral. No workflow may invent a citation,
study, empirical quantity, page, finding, or source. A dataset used for an
analysis must have verifiable provenance and a Dodatak C entry.

The structural rail uses the current book vocabulary: `#def-`,
`callout-vinjeta`, `callout-divljina`, `callout-model`, `callout-greska`, and
the four exercise tiers. `data/widgets.json` is the operational widget
inventory; numbered chapters 1–17 require a registered widget and static twin,
while the preface and capstone are exempt.

## Host adapters

The skill and role prose is host-neutral. Claude Code discovers the Claude
plugin and Markdown role definitions. Codex discovers `AGENTS.md`, the Codex
plugin manifest, and project agent configurations under `.codex/agents/`.
When parallel subagents are unavailable, a panel may run sequentially only if
all roles remain separate and the fallback is disclosed.
