---
workflow_schema_version: 1
branch: revision/comprehensive-review
baseline_commit: c163bda524b7081ec6a41d5ab75370f1700b1748
control_implementation_commit: b3463c7b6f7dc7e03a76f74f3a297e2e158e4c6e
active_write_packet: P0-REGISTER
last_completed_packet: P0-CONTROL
next_permitted_packet: null
atomic_children: 371
packet_count: 188
source_coverage_sections: 18
unmapped_actionable: 0
forward_handoffs: 12
last_updated: "2026-08-03"
---

# Comprehensive-review implementation dashboard

This is a view of the canonical implementation register and forward-handoff
ledger, not a second task list. If this page disagrees with either YAML file,
stop and repair the control state before editing book content.

## Current state

| Field | Value |
|---|---|
| Gate A0 | Accepted: D01-D16 and O01-O03 |
| Branch | `revision/comprehensive-review` |
| Baseline | `c163bda524b7081ec6a41d5ab75370f1700b1748` |
| Control implementation | `b3463c7b6f7dc7e03a76f74f3a297e2e158e4c6e` |
| Active write packet | `P0-REGISTER` |
| Last completed packet | `P0-CONTROL` |
| Next permitted packet | None while `P0-REGISTER` is active |
| Review parents | 36 ratified; 0 accepted |
| Atomic child inventory | Complete: 371 stable children; zero unmapped |
| Exact packet catalogue | 188 packets with stable IDs, typed contracts, unique sequence, and just-in-time dependencies |
| Review source coverage | 18 exact section manifests; their fingerprint union equals all 371 children; zero uncovered actionable findings |
| Chapter stages | 19 `draft` |
| Open outside asks | None registered; `P0-OUTSIDE` will create one bounded ask per owner/decision |
| Invalidated or reopened work | None |
| Failed gates | None; P0 remains open and has not yet been evaluated |

No chapter prose has been changed by `P0-REGISTER`.

## Required incoming handoffs for P0-REGISTER

- `H-G-A0-001`: preserve D01-D16, the dedicated branch, and local scoped
  commit authority; do not infer permission to push, merge, tag, archive, or
  deploy, and do not bypass later evidence gates.
- `H-P0-CONTROL-001`: the 36 parent rows are only coverage headings. Map every
  actionable finding in the complete review to a stable child item with an
  exact source anchor and acceptance test. Close only with zero unmapped
  findings and no generic placeholder children.

Both deliveries are `before_close` and were acknowledged when `P0-REGISTER`
was claimed. They must be consumed with evidence before closeout.

## P0-REGISTER exit

- Read the complete comprehensive review, especially sections 4-14 and 16.
- Give every actionable finding a stable child ID, parent, source section plus
  fingerprint, disposition, owner, approval owner, affected scope,
  prerequisites, evidence requirements, acceptance tests, and packet.
- Add the complete packet catalogue and dependency links before using a packet
  as a handoff target.
- Prove that the unmapped actionable count is zero.
- Update the register, handoff ledger, and dashboard together; run the
  validator; commit only the scoped control files; stop.

The inventory and packet graph now satisfy the first three conditions. The
packet remains active until its hardened validator, independent closeout audit,
implementation commit, and coordinated closeout record all pass.

## Findings that constrain later packets

- `P1C-INTEGRITY` is an independent packet for blocking token, manuscript,
  citation, concept, figure, and data checks; it is not part of PDF repair.
- All 18 displayed chapter reading times must ultimately be measured against a
  relevant source state, visibly labelled as estimates, or removed.
- Chapter 17's live spine must settle whether Chapter 13 is a prerequisite
  before either advertised route is published.
- Identity-pillar prose waits for its governed evidence package and approved
  brief; Chapter 17 retains the fairness widget and uses text analysis as its
  worked example.
- Any material chapter edit invalidates an older six-critic panel for final
  acceptance purposes.

## Simple implementation order

1. Control plane and baseline.
2. Correctness, licensing, and build safeguards.
3. Claim map, lifecycle, spines, terminology, and assessment policy.
4. Data catalogue, governed datasets, and reader pilots.
5. Chapter waves: `00-03 -> 04-06 -> 07-12 -> 13-17 -> 18`.
6. Solutions, appendices, and student pathways.
7. Whole-book continuity and editorial checks.
8. Release-candidate validation.
9. Publication only after separate authorisation.

## Exact next-thread prompt

If this packet is interrupted before closeout, paste this into a new thread:

```text
Continue the ratified comprehensive-review implementation from the repository's
canonical state. Read AGENTS.md and fully read:
- notes/reports/comprehensive-review-implementation-plan-2026-08-03.md
- notes/reports/comprehensive-review-implementation-register.yml
- notes/reports/comprehensive-review-dashboard.md
- notes/reports/comprehensive-review-forward-handoffs.yml
Also read the applicable checkout-local Bookwright skill instructions. Do not
rely on prior chat.

Resume the active P0-REGISTER packet only; do not clear or replace its lock and
do not choose or prepare a later packet. H-G-A0-001 and H-P0-CONTROL-001 are
acknowledged and must be consumed with evidence before closeout. Build the
complete atomic child inventory
for every actionable finding in the comprehensive review, especially sections
4-14 and 16, and the complete packet/dependency catalogue. Do not use generic
placeholder children and do not edit chapter prose. Close only after a
reproducible check shows zero unmapped actionable findings.

Use the implementation register as authoritative. Preserve unrelated changes,
run every packet exit check, and make only the authorised scoped local commit.
At closeout, update the register, dashboard, and forward-handoff ledger
together: consume incoming handoffs with evidence, record all new downstream
handoffs (or explicitly declare none), clear the active lock, and set the next
permitted packet. Run scripts/check-review-workflow.R, then stop. Do not start
P0-STATE or P0-OUTSIDE.

Report the IDs addressed, files changed, decisions implemented, checks and
results, unresolved asks or risks, handoffs consumed or created, and the next
permitted packet with its exact prompt.
```
