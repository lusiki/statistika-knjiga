# Bookwright

Editorial tooling for the *Osnove statistike za društvene znanosti* Quarto
book. Bookwright keeps chapter state, applies the book's style and enrichment
rules, checks figures and continuity, and provides independent editorial
review.

## Components

- `book-conductor` maintains the chapter dashboard, routes work, and enforces
  the final checkpoints.
- `book-style` applies `STYLE.md` with a deterministic linter and a manual
  manuscript pass.
- `book-enrich` applies the five value slots in `ENRICHMENT.md`.
- `book-figure` checks the prose introduction required before each logical
  figure or widget/static-twin pair.
- `book-review` runs six read-only chapter critics and synthesises findings by
  severity and agreement.
- `book-continuity` audits the complete book in canonical `_quarto.yml` order,
  maintains the chapter spine and terminology registries, and runs the two
  book-wide critics.

The six chapter critics cover statistical methods, skepticism, pedagogy,
evidence, style, and structure. The two book-wide critics cover voice and
narrative arc.

## Evidence rule

Bookwright never invents a citation, study, number, sample size, effect,
finding, page, or source. Croatian evidence is not a reserved category. It is
welcome under the same rule as international evidence when its source is named,
verifiable, and represented in `references.bib` or the data catalogue as
appropriate.

## Shared state

The four files under `bookwright/shared/` are live, and none of them is a
placeholder:

- `chapter-ledger.json` contains all 19 chapter records and is the live
  lifecycle dashboard.
- `chapter-spine.json` contains all 19 records and every one is ratified, each
  naming its own `G-A2b` gate, its ratification date, its decision record, its
  prerequisites and its exclusions. No registry may ratify a spine itself.
- `concept-ledger.json` carries the canonical Croatian terms and the book-wide
  notation, and its term list must agree exactly with the live `#def-` divs.
  `scripts/check-concepts.py` enforces that agreement and the freshness of the
  generated `data/concept-graph.json`, and it fails closed.
- `conventions.json` carries the callout names, four exercise tiers, widget
  policy, the ratified structural bands, the ratified intellectual, assessment
  and identity architectures, and the ratified terminology registry. The
  structural bands were measured and ratified on 30 July 2026 and are no longer
  provisional; the terminology registry was ratified at `G-A2c` and is enforced
  by `scripts/check-terminology.py`.

Changing any of these is conductor work. A packet that adds, merges or demotes
a `#def-` block must update `concept-ledger.json` and regenerate
`data/concept-graph.json` in the same packet.

JSON schemas live in `bookwright/shared/schemas/`.

## Host scaffolding

The repository exposes the same workflows to both hosts:

- Claude Code uses the manifests under `.claude-plugin/`, the skills under
  `bookwright/skills/`, and the read-only role prompts under
  `bookwright/agents/`.
- Codex reads the root `AGENTS.md`, project agents under `.codex/agents/`, the
  Codex plugin manifest under `bookwright/.codex-plugin/`, and the repository
  marketplace entry under `.agents/plugins/marketplace.json`.

Run either host from the book repository so the workflows use the live
`chapters/`, `data/`, `references.bib`, `STYLE.md`, `ENRICHMENT.md`, and shared
registries rather than an installed cache.

## Install

For Codex, run from the repository root:

```powershell
codex plugin marketplace add . --json
codex plugin add bookwright@statistika-local --json
```

For Claude Code, run from the repository root:

```powershell
claude plugin marketplace add ./bookwright_plugin
claude plugin install bookwright@bookwright-local
```

Open a new host session after installing or updating so the skills are
rediscovered. During development, update the Codex plugin cache-buster before
reinstalling:

```powershell
py -3.11 $env:USERPROFILE\.codex\skills\.system\plugin-creator\scripts\update_plugin_cachebuster.py .\bookwright_plugin\bookwright
codex plugin add bookwright@statistika-local --json
```

## Typical requests

- `Where does the book stand?` — show the chapter dashboard.
- `What can I work on next?` — route the current open work.
- `Sweep chapter 8 for style.` — lint and manually inspect its prose.
- `Check the figures in chapter 5.` — inspect logical figures and their
  introductions.
- `Enrich chapter 12.` — propose focused insertions for approval.
- `Review chapter 8.` — run the six-critic chapter panel.
- `Check continuity across the book.` — scan structure, terms, voice, and arc.
- `Propose the spine for chapter 3.` — propose key aspects and `#def-` terms for
  ratification.

## Deliberate boundary

Bookwright diagnoses missing or weak vignettes, definitions, exercises,
widgets, and figures, but it does not invent evidence or silently author
repairs. Approved prose work is handled through the relevant skill. Widget
implementation and data acquisition remain governed by `widgets/README.md`,
`data/README.md`, and Dodatak C.
