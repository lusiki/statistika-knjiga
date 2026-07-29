# Architecture

Bookwright treats the book as a matrix, not a line. One axis is each chapter's lifecycle (stub, draft, enriched, style swept, figures done, co-author review, final). The other axis is the work that only makes sense across the whole book (continuity, terminology, the arc). The MVP covers the per chapter axis and the status tracking, and leaves the book wide axis for later.

## Pieces

* The manager is `book-conductor`, a skill folder whose SKILL.md is short and whose assets hold the routing rules and the checkpoint list. The chapter ledger and its schema live on the shelf.
* The workers are `book-style`, `book-enrich`, and `book-review`, one job each.
* The critics are five read only agents under `agents/`, dispatched by `book-review`.
* The shelf is `shared/`, holding the two ledgers and the schemas.

## How they connect

Two kinds of connection, the same as sciagent. Direct calls are only the manager handing work to a job, and `book-review` dispatching a critic. Everything else is coordinated through shared files. The conductor reads and writes `shared/chapter-ledger.json`. The critics and jobs read the book repo and the concept ledger. The checkpoints are the conductor reading `book-conductor/assets/checklist.json` and refusing to advance a chapter to final until the blocking items pass. Every reference to a shared file uses `${CLAUDE_PLUGIN_ROOT}` so it resolves wherever the plugin is installed.

## The routing

`book-conductor/assets/routing-rules.json` is the rule that keeps you unblocked. Self work (mechanism, international evidence, comparison, style, structural draft, a figure from existing data, a continuity fix) is done now. Co-author work (Croatian empirics, HNB or MFin data, domestic examples and reforms, a sign off on a contested domestic claim) is never auto filled and surfaces as a bounded request. This mirrors the analytic versus external split in sciagent and respects the reserved zone in ENRICHMENT.md.
