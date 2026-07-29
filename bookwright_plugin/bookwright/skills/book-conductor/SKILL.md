---
name: book-conductor
description: The manager for the "Osnove statistike za društvene znanosti" book. Use whenever you want the status of the book, want to know what to work on next, want to sort a chapter's open work into a self pile versus a co-author pile, or want to turn a co-author task into a short bounded request. Reads the chapter ledger and reports a one line per chapter dashboard, applies the self vs co-author routing rules, and enforces the book checkpoints. Trigger on phrases like where does the book stand, what can I do now, what is blocked on an outside decision, status of chapter N, route this work, draft a co-author ask.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
---

# Book Conductor (manager)

## Purpose
Hold the state of the whole book in one place and answer three questions on demand. Where does every chapter stand, what can be done now without waiting for anyone, and what is genuinely blocked on a co-author. The skill reads and updates the chapter ledger, applies the routing rules, drafts bounded co-author requests, and refuses to mark a chapter final until the book checkpoints pass.

## When to use
Use this skill to get a status dashboard, to decide the next action, to sort a chapter's open work into self or co-author piles, to draft a low effort co-author request, or to check a chapter against the book checkpoints before calling it final. For the actual editing jobs invoke the specific skill instead (book-style, book-enrich, book-review).

## Inputs / Outputs
Inputs. The chapter ledger at `${CLAUDE_PLUGIN_ROOT}/shared/chapter-ledger.json`, the routing rules at `assets/routing-rules.json`, the checkpoint list at `assets/checklist.json`, and the book repo itself (`chapters/`, `references.bib`, `STYLE.md`, `ENRICHMENT.md`). The ledger is the single source of truth for chapter state.

Outputs. A status dashboard (one line per chapter, grouped by stage, with blocked chapters and pending co-author asks surfaced), an updated ledger, sorted self and co-author task lists, and drafted co-author requests.

## Workflow
Pick the mode that fits, or infer it and say which you chose.

1. Status. Read the ledger. Emit one line per chapter showing its stage, its open self items, and its open co-author asks. Group by stage so the front of the book and the unfinished tail are both visible at a glance. Call out any chapter whose last render failed and any co-author ask open a long time. See `reference/status-report.md`.

2. Route. For a given chapter or the whole book, take each open piece of work and sort it using `assets/routing-rules.json`. Anything matching a self rule goes in the self pile and can be done now with book-style, book-enrich, book-review, or a figure built from data already in `data/atlas`. Anything matching a co-author rule (Croatian empirics, HNB or MFin data, a domestic example, a domestic reform specific, a sign off on a contested domestic claim) goes in the co-author pile and is never auto filled. Write the result back to the ledger.

3. Ask. For each co-author item, draft a short bounded request following `reference/coauthor-asks.md`. The request names the exact thing needed, shows that the surrounding prose is already written, and points at the single slot where it drops in. The goal is the smallest possible action on their side.

4. Check. Before a chapter moves to final, run it against `assets/checklist.json`. The blocking items are the book checkpoints. Do not mark final if any blocking item fails. Record pass or fail with a short note in the ledger.

## Modes
`status`, `route`, `ask`, `check`. If none is given, infer from the request and state the choice.

## Quality gates / checklist
The blocking items in `assets/checklist.json` are the five book checkpoints. No fabricated citation or finding in committed prose. No system generated Croatian empiric or domestic example in committed prose. The chapter renders cleanly. No unresolved continuity contradiction at assembly. STYLE.md hard rules pass before any prose commit.

## Knowledge base & references
Load on demand. `reference/status-report.md` (how to read the ledger and shape the dashboard), `reference/coauthor-asks.md` (how to write a bounded request). Shared state lives at `${CLAUDE_PLUGIN_ROOT}/shared/chapter-ledger.json` and `${CLAUDE_PLUGIN_ROOT}/shared/concept-ledger.json`.

## Autonomy note
The conductor reports state and proposes routing and requests. It does not decide what a chapter should say, and it never fabricates the co-author material it is waiting for. You evaluate, edit, and ratify every output. It makes the management easier, it does not take it over.
