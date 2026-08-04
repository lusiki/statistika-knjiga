---
workflow_schema_version: 1
branch: revision/comprehensive-review
baseline_commit: c163bda524b7081ec6a41d5ab75370f1700b1748
control_implementation_commit: b3463c7b6f7dc7e03a76f74f3a297e2e158e4c6e
active_write_packet: null
last_completed_packet: P2-SPINE-II
next_permitted_packet: G-A2b-III
atomic_children: 371
packet_count: 188
source_coverage_sections: 18
unmapped_actionable: 0
forward_handoffs: 46
last_updated: "2026-08-04"
---

# Comprehensive-review implementation dashboard

This is a view of the canonical implementation register and forward-handoff
ledger, not a second task list. If this page disagrees with either YAML file,
stop and repair the control state before editing book content.

## Current state

| Field | Value |
|---|---|
| Gate A0 | Accepted: D01-D16 and O01-O03 |
| Gate A1a | Accepted: D01 Chapter 10 correction specification; reviewer Luka Sikic; 2026-08-03 |
| Gate A1b | Accepted: D02 Chapter 14 correction specification; reviewer Luka Sikic; 2026-08-03 |
| Gate A1c | Accepted as amended: minimise Navarro reliance; D08 and D12 unchanged; owner Luka Sikic; 2026-08-03 |
| Gate A1d | Accepted as recommended: pre-release governance mechanism; release, archive, and errata owner Luka Sikic; 2026-08-03; no external-action authority |
| Gate A2a | Accepted as recommended: claim map, audit questions, lifecycle, seven threads, four activities, and data-design principles; 70/20/10 diagnostic only; owner Luka Sikic; 2026-08-04 |
| Gate A2d | Accepted: D06 solutions policy, D09 Appendix B scope, D10 Appendix G scope, and the D05/H10 AI ladder as recommended; D15 privacy/tool lanes as the course's own dated policy v1.0; author, course owner and clean-install owner Luka Sikic; 2026-08-04 |
| Gate A2b-PREFACE | Accepted as drafted: preface spine with nine aspects, five terms, no prerequisite, twelve exclusions; owner Luka Sikic; 2026-08-04 |
| Gate A2b-I | Accepted as drafted: Part I contract, three chapter spines, and a bounded three-block definition increase; owner Luka Sikic; 2026-08-04 |
| Gate A2b-II | Accepted as drafted: Part II contract, three chapter spines, and a per-definition Chapter 4 disposition from six blocks to four; owner Luka Sikic; 2026-08-04 |
| Branch | `revision/comprehensive-review` |
| Baseline | `c163bda524b7081ec6a41d5ab75370f1700b1748` |
| Control implementation | `b3463c7b6f7dc7e03a76f74f3a297e2e158e4c6e` |
| Active write packet | None |
| Last completed packet | `P2-SPINE-II` |
| Next permitted packet | `G-A2b-III` |
| Review parents | 32 ratified; 4 accepted |
| Atomic child inventory | Complete: 371 stable children; 102 accepted, 5 deferred with reason, 264 ratified; zero unmapped |
| Exact packet catalogue | 188 packets: 39 accepted and 149 ratified, with stable IDs, typed contracts, unique sequence, and just-in-time dependencies |
| Review source coverage | 18 exact section manifests; their fingerprint union equals all 371 children; zero uncovered actionable findings |
| Chapter stages | 19 `draft` |
| Chapter spines | 7 of 19 ratified: `00-predgovor` at `G-A2b-PREFACE`; Chapters 1–3 at `G-A2b-I`; Chapters 4–6 at `G-A2b-II` |
| Open outside asks | 64 of the 82 canonical asks remain `drafted_unsent`; 18 are `done` — the two methods asks, three G-A1c licence/access asks, four G-A1d governance/owner asks, the G-A2a claim-system ask, the five G-A2d policy asks, and the preface, Part I and Part II spine asks; 0 external messages sent |
| Invalidated or reopened work | `P1A-C02` and `P1A-METHODS` were revalidated evidence-only at the current source state and remain accepted; no prose changed |
| Failed gates | None in `P1-VERIFY`; all twelve prerequisites pass independently. The pre-existing `_quarto.yml` checksum mismatch remains separately recorded in `H-P1C-EXPORT-002` for `P7-FREEZE` and `P8-META` |

No chapter prose was changed by `P0-OUTSIDE`.

## P2-SPINE-II closeout

- `H-G-A2B-II-001` was acknowledged and consumed with an exact disposition and
  evidence before the packet claim and before the first substantive edit.
  `H-P1C-INTEGRITY-001` remains `pending` for `WB-C05`; the Chapter 5 spine
  names the `fig-anscombe` debt as that packet's obligation without settling it.
  `H-P1C-INTEGRITY-002` remains `pending` for `P2-TERMS`.
- `chapter-spine.json` now carries three ratified Part II units:
  `04-sazimanje-podataka` with 9 aspects, 10 terms, 3 prerequisites and 8
  exclusions; `05-vizualizacija` with 10, 8, 2 and 8; and `06-povezanost` with
  10, 8, 3 and 8. Each is faithful to the accepted draft and names its gate,
  date and decision record. Its deterministic state is
  `spine:sha256-f2e08e172cbbc60a12c981ff92b7d72f64fe8344e3fe46e8cc0e55ac0084abad`.
- No prerequisite points at a later unit; Chapter 5 could not have been ratified
  before Chapter 4, nor Chapter 6 before Chapters 4 and 5.
- The rejected orders are written as binding exclusions rather than left as
  prose: measures of centre do not open Chapter 4, and visualisation does not
  lead in Chapter 5. All three chapters forbid assessed code production and
  invented or unsourced empirical material, and record sampling theory,
  intervals, tests, regression, least squares, causal identification, multiple
  imputation and natural-language-processing methods as explicit deferrals.
- The approved Chapter 4 definition-load map was deliberately **not**
  implemented here: merging, removing or adding a `#def-` block edits chapter
  prose, and `H-P1C-INTEGRITY-002` freezes the 46 live definitions, the concept
  ledger and the generated graph until `P2-TERMS` retires that debt. Chapter 4
  still carries six live blocks. `H-P2-SPINE-II-001` carries the approved map to
  `P2-TERMS` and `WB-C04` so the frozen concept gate can accept it rather than
  treat it as drift.
- `scripts/check-chapter-spines.py` now enforces the exact Part II exclusions,
  required load-bearing terms and a general ratification-order rule, and reports
  seven ratified and twelve unratified units. Both deliberate fixtures kept their
  identifiers, returned exit 1, and together prove all three new check kinds for
  Part II. The three architecture consumers count ratified spines and agree on 7
  of 19 with their accepted states unchanged, and the blocking structure lane
  passes with 19 chapters.
- No `#def-` block, concept-graph edge, chapter or appendix prose, chapter
  stage, terminology, data package, route, render, generated artifact or
  external authority changed. All 19 units remain `draft`.

The durable evidence is `notes/reports/p2-spine-ii-2026-08-04.md`.

## G-A2b-II closeout

- No handoff targets `G-A2b-II`; the complete ledger was read before the
  decision. `H-P1C-INTEGRITY-001` remains `pending` for `WB-C05` and owns the
  `fig-anscombe` introduction debt, which this gate names but does not take
  over. `H-P1C-INTEGRITY-002` remains `pending` for `P2-TERMS` and freezes the
  46 live definitions, so this gate decides the definition map and writes no
  block.
- The complete Part II contract, the three chapter spines and the definition
  hierarchy were drafted first, and the gate then closed against that drafted
  state. Author and editor Luka Sikic accepted it as drafted on 2026-08-04.
- Part II carries three steps and no more: the analysis table is constructed
  rather than found, then a visual claim must be honest, then association has
  limits. The order is load-bearing — the conventional summary-statistics-first
  order is explicitly rejected and visualisation does not lead — and the part
  carries the constructed-data thread that Chapters 8 and 16 later harvest.
- The part emphasises the validate, prepare and explore lifecycle stages, plants
  the reproducibility/provenance and communication threads, develops the unit,
  denominator and selection threads, and carries the full claim map and six
  audit questions at its boundary with an answerable self-check. It is the first
  part whose AI ladder requires a readable verification receipt; visible code is
  read rather than written and no assessed task requires code production.
- Chapter 4 carries nine aspects and ten terms and requires Chapters 1, 2 and 3.
  Chapter 5 carries ten aspects and eight terms and requires Chapters 3 and 4.
  Chapter 6 carries ten aspects including the Part II boundary and eight terms
  and requires Chapters 2, 4 and 5. No prerequisite points at a later unit.
- `R04-C04-definition-load` is settled with one explicit disposition per
  definition. Arithmetic mean, median and standardised value are retained, each
  with a named later dependant; variance is merged into the standard deviation
  as one block naming both terms in its defining sentence; skewness is demoted
  to prose under `.pojam`; nothing is moved to another chapter. Chapter 4 falls
  from six blocks to four and re-enters the ratified one-to-five band, while
  Chapters 5 and 6 keep their existing three blocks each unchanged. The net
  effect on the frozen set is 46 down to 44 definitions.
- The draft matches the recorded author intent in every respect. Seven
  alternatives were rejected, including keeping the summary-first order, putting
  visualisation before summarisation, leaving all six Chapter 4 definitions
  unchanged, demoting the standardised value, moving variance to Chapter 8,
  adding a block for the analysis table, and taking the `fig-anscombe` debt into
  this gate.
- `OA-G-A2B-II-SPINE` is `done`; no external message was sent.
  `H-G-A2B-II-001` carries the accepted spine to `P2-SPINE-II` at its
  `before_start` gate.
- No chapter or appendix prose, registry, spine, terminology, `#def-` block,
  concept graph, data package, render, generated artifact or external authority
  changed. All 19 units remain `draft` and 4 of 19 spines remain ratified.

The durable evidence is `notes/reports/g-a2b-ii-spine-decision-2026-08-04.md`.

## P2-SPINE-I closeout

- `H-G-A2B-I-001` was acknowledged and consumed with an exact disposition and
  evidence before the first substantive edit. `H-P0-REGISTER-008` remains
  `pending` for `WC-C08`, `WC-C09` and `WD-C17`; the Chapter 3 spine states its
  debt but does not settle it.
- `chapter-spine.json` now carries three ratified Part I units:
  `01-zasto-statistika` with 7 aspects, 8 terms, no prerequisite and 6
  exclusions; `02-mjerenje-i-dizajn` with 9, 10, 1 and 7; and
  `03-kako-brojke-zavode` with 10, 6, 2 and 8. Each is faithful to the accepted
  draft and names its gate, date and decision record. Its deterministic state is
  `spine:sha256-b660ac8ecfd6386aa39247b2e602f5324549264703b04d9851303a87b82d88cb`.
- No prerequisite points at a later unit, and Chapter 3 could not have been
  ratified before Chapters 1 and 2.
- All three Part I chapters carry the D05 no-visible-code exclusion, forbid
  assessed code production, and forbid invented or unsourced empirical material.
  Population, sample, sampling, causal identification, psychometrics, factor
  analysis and the margin of error are recorded as explicit deferrals to
  Chapters 8, 9 and 16 or to outside the book.
- The Chapter 3 spine is explicitly subordinate to its ratified identity brief
  `c03` and carries the Part I claim-map boundary as its tenth aspect.
- The approved three-block definition increase was deliberately **not**
  implemented here: adding a `#def-` block edits chapter prose, and
  `H-P1C-INTEGRITY-002` freezes the 46 live definitions, the concept ledger and
  the generated graph until `P2-TERMS` retires that debt. `H-P2-SPINE-I-001`
  carries the approved map to `P2-TERMS`, `WA-C01` and `WA-C03` so the frozen
  concept gate can accept it rather than treat it as drift.
- `scripts/check-chapter-spines.py` now enforces the exact Part I exclusions,
  required load-bearing terms and ratification order, and reports four ratified
  and fifteen unratified units. Both deliberate defects return exit 1, the three
  architecture consumers agree on 4 of 19 with their accepted states unchanged,
  and the blocking structure lane passes with 19 chapters.
- No `#def-` block, concept-graph edge, chapter or appendix prose, chapter
  stage, terminology, data package, route, render, generated artifact or
  external authority changed. All 19 units remain `draft`.

The durable evidence is `notes/reports/p2-spine-i-2026-08-04.md`.

## G-A2b-I closeout

- No handoff targets `G-A2b-I`; the complete ledger was read before the
  decision. `H-P0-REGISTER-008` targets `WC-C08`, `WC-C09` and `WD-C17`,
  remains `pending`, and was not consumed here.
- The complete Part I spine, part contract and definition hierarchy were drafted
  first, and the gate then closed against that drafted state. Author and editor
  Luka Sikic accepted it as drafted on 2026-08-04.
- Part I carries three steps and no more: a number is not a conclusion, then how
  a number is made, then how a correct number still misleads. The part
  emphasises the question, acquire and validate lifecycle stages, plants five
  threads, carries the full claim map and six audit questions at its boundary
  with an answerable self-check, and shows no visible code anywhere.
- Chapter 1 carries seven aspects and eight terms with no prerequisite. Chapter 2
  carries nine aspects and ten terms and requires Chapter 1. Chapter 3, explicitly
  subordinate to its ratified identity brief `c03`, carries ten aspects including
  the Part I boundary and six terms, and requires Chapters 1 and 2.
- The definition hierarchy is bounded and increases Part I by exactly three
  blocks: `jedinica analize` and `Simpsonov paradoks` in Chapter 1 and
  `temeljna stopa` in Chapter 3. Chapter 2 keeps its existing four unchanged. The
  four activities are stated from the accepted architecture rather than
  redefined; mediator and collider stay in prose under `.pojam`; and population,
  sample, sampling, margin of error and causal identification are explicitly
  deferred to Chapters 8, 9 and 16.
- The draft matches the recorded author intent in every respect: only
  definitions with a named later dependant are ratified, the D05 no-visible-code
  boundary is the first exclusion of all three chapters, and the ramp stays
  gentle. The remaining aspects each implement an already ratified register item
  or accepted architecture, so no new requirement was introduced.
- Six alternatives were rejected, including four definition blocks for the
  activities, defining population and sample in Chapter 1, formal blocks for
  mediator and collider, adding no block at all, defining the margin of error in
  Chapter 3, and allowing visible Chapter 3 code.
- `OA-G-A2B-I-SPINE` is `done`; no external message was sent. `H-G-A2B-I-001`
  carries the accepted spine to `P2-SPINE-I` at its `before_start` gate.
- No chapter or appendix prose, registry, spine, terminology, `#def-` block,
  concept graph, data package, render, generated artifact or external authority
  changed.

The durable evidence is `notes/reports/g-a2b-i-spine-decision-2026-08-04.md`.

## P2-SPINE-PREFACE closeout

- `H-G-A2B-PREFACE-001` was acknowledged and consumed with an exact disposition
  and evidence before the first substantive edit. `H-P0-STATE-001` remains
  `pending` for `WA-C00`; its obligation is now recorded as exclusion 2 of the
  ratified spine so that packet can carry it out against real prose.
- `chapter-spine.json` unit `00-predgovor` now carries nine load-bearing
  aspects, five load-bearing terms, an explicit empty prerequisite list, and
  twelve exclusions, with its gate, ratification date, and decision record. The
  written spine is faithful to the accepted draft with nothing added or omitted.
  Its deterministic state is
  `spine:sha256-53ee28d57cfb7fb1b533e77977abae152717a0afc1b3a7ec24ad35b03145149c`.
- The empty prerequisite list is a decision, not an omission: the preface is the
  book's entry point and may presuppose no chapter, appendix, or widget.
- `chapter-spine.schema.json` now admits `ratified_at`, `decision`,
  `decision_record`, `prerequisites`, and `exclusions`. No existing field was
  removed or altered, so every earlier entry stays valid.
  `scripts/check-chapter-spines.py` enforces the obligations for a ratified
  entry that the local schema validator cannot express conditionally.
- Three checkers previously asserted that zero of 19 spines were ratified. That
  was an accurate snapshot at their own closeout but never an invariant, since
  this packet exists to change the count. All three now assert the real
  invariant: no registry may itself ratify a spine, and every ratified spine
  names its own `G-A2b` gate. The accepted `architecture:sha256-30e10508…`,
  `assessment:sha256-c1206f08…`, and `identity:sha256-f09124e5…` states are
  unchanged.
- `scripts/check-chapter-spines.py` reports one ratified and eighteen
  unratified units. Both deliberate defects, a ratified spine without its gate
  and an admitted Part I visible-code exclusion removal, return exit 1. The
  blocking structure lane passes with 19 chapters.
- No chapter or appendix prose, chapter stage, terminology, data package, route,
  render, generated artifact or external authority changed. All 19 units remain
  `draft`.

The durable evidence is `notes/reports/p2-spine-preface-2026-08-04.md`.

## G-A2b-PREFACE closeout

- No handoff targets `G-A2b-PREFACE`; the complete ledger was read before the
  decision. `H-P0-STATE-001` targets `WA-C00`, remains `pending`, and was
  deliberately not consumed here.
- The complete preface spine was drafted first, and the gate then closed against
  that drafted state rather than against the earlier pre-disposition note.
  Author and editor Luka Sikic accepted it as drafted on 2026-08-04.
- The preface is a reader contract with nine load-bearing aspects: the four
  promised abilities stated as what the reader can afterwards do; the explicit
  out-of-scope boundary; what is expected of the reader; one genuine
  self-contained miniature inquiry instead of meta-scaffolding; the book's short
  stable thesis that computation is delegable while question choice, source
  verification and the signature under a conclusion stay human; a checkable
  calculation trace with its stated limit; the two reading routes as navigation
  without manifesto register; pathway language bounded to verified coverage; and
  a handoff to Chapter 1 that states the promise without arguing the lifecycle.
- Five terms are load-bearing and introduced without formal definition:
  statistical literacy, simulation, estimation, checkable calculation trace, and
  the division of responsibility with an assistant. Their canonical Croatian
  forms remain a `G-A2c` decision. The preface has no prerequisite.
- Twelve exclusions bind it, including no visible code block, no promise of
  visible code in the preface or Part I, no lifecycle exposition duplicating
  Chapter 1, no manifesto register, ASA removed or sharply subordinated, no
  Appendix B claim beyond the verified clean installation, no full claim map or
  audit-question list, no widget, no `#def-` block, no invented or unsourced
  example, no citable or released edition promise, and no assessed code
  production.
- The draft matches the recorded author intent in every respect. Pending handoff
  `H-P0-STATE-001` is satisfied by aspect 6 and exclusions 1 and 2; the accepted
  D09 Appendix B bound is satisfied by aspect 8 and exclusion 6. The three
  aspects beyond the literal intent text each implement an already ratified
  register item, so no new requirement was introduced and no further ask was
  needed.
- Six alternatives were rejected, including the manifesto preface, carrying the
  lifecycle argument, deleting the preface, promising visible code receipts,
  promising a complete no-code route, and carrying the full claim map.
- `OA-G-A2B-PREFACE-SPINE` is `done`; no external message was sent.
  `H-G-A2B-PREFACE-001` carries the accepted spine to `P2-SPINE-PREFACE` at its
  `before_start` gate.
- No chapter or appendix prose, registry, spine, terminology, data package,
  render, generated artifact or external authority changed. All 19 spines remain
  unratified and all 19 units remain `draft`.

The durable evidence is
`notes/reports/g-a2b-preface-spine-decision-2026-08-04.md`.

## P2-IDENTITY closeout

- No handoff targets `P2-IDENTITY`; the complete ledger was read before packet
  claim. `H-P0-REGISTER-007` targets `WA-C03`, `WC-C12` and `WD-C17`, remains
  `pending`, and was not consumed here. Its substance is encoded as the joint
  contract's `evidence_precondition`.
- `conventions.json` now carries one schema-valid `identity_briefs` object with a
  joint contract and three bound briefs. Its deterministic state is
  `identity:sha256-f09124e52089f2127b5064ed1b8f912a74628fd0b9ba3fb807bd0922cca6e3a3`.
- The joint contract binds all three pillars to one Tier F argument, one
  traceable case, named supported and unavailable claim dimensions, a stated
  conclusion-changing factor, one full six-critic panel, and argumentative
  rather than quota-driven length. It forbids assessed code production, a new
  numbered chapter, a new central widget, a new callout type, invented material,
  and any pillar prose before its evidence package and author gate.
- Chapter 3 is one audit of a single traceable public claim: axis and
  denominator, base rate, early poll reading, cherry-picking, an AI-produced
  number, synthetic media, and the simulation/synthetic/hypothetical/fabricated
  distinction, ending in a skeptic's protocol. The ASA episode is excluded, the
  margin-of-error justification is an explicit debt to Chapters 8 and 9, and the
  Part I no-visible-code boundary holds.
- Chapter 12 is one path from an attractive finding through pipeline
  flexibility, incentives and selection, replication as cumulative evidence, one
  sensitivity comparison, one forest plot, reform and its limits, to a
  reformed-practice contract. Invented study results, undated open-science
  claims, and significance-only comparison are excluded.
- Chapter 17 is one consequential text-classification decision from corpus and
  unit through coding frame, three kinds of label, held-out evaluation,
  threshold and confusion table, subgroup errors, a disputed recorded label,
  procedural fairness and appeal, to monitoring, feedback and language models as
  prediction systems.
- `R13-ARCH-measurement-first` is accepted. Chapter 17 is the ratified home of a
  measurement-first text module covering seven topics and excluding tokenizer or
  preprocessing implementation, an NLP programming course, machine-learning
  mathematics, and any model-training task. Student inputs are supplied text and
  prepared tables.
- D07 is preserved structurally: the existing fairness widget is retained and
  subordinated to prose, text analysis remains the worked example, and no second
  central widget is admitted.
- Eleven open selections are deferred to their exact gates, including
  `G-A4-03`, `G-A4-12`, `P3-EVIDENCE12`, `G-A4-17`, `G-A3-DZS`, `G-A3-DIP`,
  `G-A3-TEXT`, `P2-SPINE-I`, `P2-SPINE-IV`, `P2-SPINE-V` and `P5-ROUTES`.
  Chapter 17's prerequisite metadata explicitly remains a `P2-SPINE-V` decision.
- `scripts/check-identity-briefs.py` passes; both deliberate defects, a dropped
  fairness widget and an admitted NLP implementation, return exit 1. The book
  and assessment architecture checkers pass with their accepted states unchanged.
- No chapter or appendix prose, spine, terminology, data package, case, source,
  evidence artifact, route, render, generated artifact or external authority
  changed. All 19 spines remain unratified and all 19 units remain `draft`.

The durable evidence is `notes/reports/p2-identity-briefs-2026-08-04.md`.

## P2-ASSESS closeout

- `H-G-A2D-001` and `H-G-A2D-004` were acknowledged and consumed with exact
  D06 and D05/H10 dispositions before packet claim. `H-P1C-EXPORT-001` was
  acknowledged before the first substantive edit and consumed before closeout
  with structural export evidence.
- `conventions.json` now carries one schema-valid `assessment_architecture`
  object tied to `G-A2d` and the three governed items
  `R15-SCHEMA-closure`, `R24-BOOK-human-AI-competence`, and
  `R24-BOOK-three-roles`. Its deterministic state is
  `assessment:sha256-c1206f08e75502c748c2517a5020b4cd84074f5c2e5a03c5292c67dce928937a`.
- `solution-record.schema.json` defines one record per exercise with stable
  source binding and six machine-identifiable components: planted error,
  revealing diagnostic, plausible non-answers, model-response components,
  numerical check, and severity-ranked rubric. No second answer source is
  permitted.
- The severity order is `fatal`, `major`, `minor`, and `useful_improvement`, so
  a defect that invalidates the central claim cannot be averaged with an
  optional improvement.
- Five projections derive from the same record. The main task remains
  answer-free; a separated self-study route and its print twin receive concise
  checks; the protected `kolegij` layer receives full rubrics, alternatives,
  and instructor notes; public AI exports receive zero solution fields.
- Export protection is structural. Solution routes stay outside public export
  inputs, protected in-source content requires `content-visible` with
  `when-profile`, labels are not access control, and `P5-ROUTES` retains the
  final route and leak proof.
- The AI registry preserves the roles instrument, fallible analyst, and object
  of research. Its five competence dimensions are task specification,
  validation, alternatives, provenance, and responsibility, each with explicit
  plant/develop/harvest roles and exclusions.
- The seven-stage ladder progresses from provenance and fabricated-number
  checks in Part I through reproducible descriptive work, sampling and
  generalisation, inferential flexibility, model and prediction audits,
  deployed-system scrutiny, and a fully documented final evidence package.
  From the end of Part I onward, assistant-using tasks require a readable
  verification receipt.
- STYLE H10 now states the ratified boundary consistently: Part I has no
  visible code, hidden plumbing remains permitted, later code may be read and
  diagnosed, and no assessed task anywhere requires code production.
- `scripts/check-assessment-architecture.py`, the prior book-architecture
  checker, the configuration-driven inventory, JSON parsing, source-scope, and
  whitespace checks pass. Both assessment-policy negative fixtures fail with
  exit 1 for their injected protected-export and assessed-code defects.
- No chapter or appendix prose, spine, terminology, data package, exporter,
  route, render, generated artifact, or external authority changed. All 19
  spines remain unratified and the solution-route inventory remains empty.
- No new future-relevant effect was found. Existing dependencies already route
  final solution visibility and leak proof to `P5-ROUTES` and the suspect-code
  continuity audit to `P6-CONTINUITY`, so no duplicate handoff was created.

The durable evidence is
`notes/reports/p2-assessment-architecture-2026-08-04.md`.

## G-A2d closeout

- No incoming handoff targeted `G-A2d`; the complete handoff ledger was read
  before the decision was recorded.
- All five canonical asks received a dated disposition from their named owner
  and are `done`. No external message was sent.
- **D06 solutions policy** — approved as recommended. One canonical solution
  record per exercise renders in two layers: separated self-study checks with
  the intended planted errors, and protected `kolegij` rubrics with
  alternatives and instructor notes. Protected solutions are excluded from
  public AI exports and no second answer source may exist.
- **D09 Appendix B** — approved as recommended, with Luka Sikic as the named
  clean-install verification owner. Appendix B supports only the book's core
  analyses on the same files, variables, and expected values as Appendix A,
  with pinned product version, module, route, settings, golden values and test
  date. No public no-code promise may exceed the verified coverage.
- **D10 Appendix G** — approved as recommended: exactly percentages and
  percentage points, proportions and rates, slope, and logarithmic scale.
  Nothing added, nothing removed, sanctioned `podsjetnik` first-use links, and
  every configuration-driven inventory updated before the file is added.
- **D05 / H10 AI ladder** — approved as recommended. Computation stays
  delegable, readable verification receipts are required after Part I,
  assessment targets judgment rather than code production, Part I keeps its
  no-visible-code rule with hidden plumbing permitted, the three roles of AI
  are retained, and the suspect-code strand escalates with stage-appropriate
  approved exceptions.
- **D15 privacy and tools** — recorded as the course's own dated conservative
  policy, version 1.0, as of 2026-08-04, published in full in Appendix F and
  referenced by Chapter 18. The applicable institution is Hrvatsko katoličko
  sveučilište as the course's home institution. The policy is **not** a
  university regulation and may not be cited as one; no external legal or
  institutional document is named, and no later packet may supply one.
- Three lanes carry exact conditions: public tools for published,
  licence-cleared, simulated, synthetic and teaching-aggregate data only;
  contractually protected tools for pseudonymised working data under a written
  agreement excluding training on input and fixing retention; institutionally
  approved local tools with no data egress for restricted data within its own
  access conditions. Across all lanes, no task may require sending personal,
  identifiable, restricted or non-shareable data, and every such task ships a
  safe supplied-data alternative.
- The disclosure rule requires a short use statement — tool and version, what
  was delegated, which data lane, what the author verified and how, what
  remained unverified. Undisclosed use is an integrity breach; disclosed use is
  not by itself penalised. Every legal, institutional or product claim carries
  an as-of date and a source.
- The durable policy record is
  `notes/reports/g-a2d-policy-decisions-2026-08-04.md`. Nine rejected
  alternatives, the authority boundary, and all seventeen governed items are in
  the register.
- `H-G-A2D-001` through `H-G-A2D-005` carry the five dispositions to
  `P2-ASSESS`, `P5-B`, `P5-F`, `P5-G`, `P5-ROUTES`, `P6-CONTINUITY`,
  `P6-EVIDENCE` and `WE-C18`. No prose, registry, spine, terminology, data
  package or generated artifact changed, and `P2-ASSESS` was not started.

The accepted decision source state is
`conversation:G-A2d-policy-decisions-approved-2026-08-04-Luka-Sikic`.

## P2-CLAIMS closeout

- `H-G-A2A-001` was acknowledged at its `before_start` gate before the first
  substantive edit and consumed before closeout with the accepted `G-A2a`
  system, all 22 governed items, exact exclusions, and packet evidence.
- The existing checkout-local `conventions.json` now carries one strict
  `intellectual_architecture` object with canonical claim, lifecycle, thread,
  ethics, and data-science registries. Its deterministic state is
  `architecture:sha256-30e105082ac37f09b40667f6a9a3f4a70345cca4ed16004a09fd483d79816ef8`.
- The claim registry records six dimensions, independent population reach, six
  audit questions, the poll-reading card, the honest-sentence standard, and
  sensitivity as a primary analysis plus one defensible alternative.
- The lifecycle registry records nine stable stages and cumulative,
  nonexclusive part/finale roles. It preserves the separation between
  probability sampling and training/validation/test separation.
- All seven threads have explicit `plant`, `develop`, and `harvest` locations
  and roles plus exclusions. The global rule is a short seed, one substantial
  harvest, and later retrieval rather than repeated mini-lectures.
- Data science remains a delivery mechanism for the four promises, not a fifth
  promise. Every representation of the approximate `70/20/10` attention split
  marks it non-binding: it is not a page formula, quota, or admission rule.
- The architecture distinguishes four activities, four evidence objects,
  ordinary-practice ethics, and eight data-generating designs. It preserves
  text-package priority while leaving every exact package selection,
  promotion, and rights decision to its later gate.
- `scripts/check-book-architecture.py` validates the full conventions schema
  and exact semantic invariants without undeclared dependencies. The durable
  placement and evidence record is
  `notes/reports/p2-claims-architecture-2026-08-04.md`.
- No chapter or appendix prose changed; all 19 chapter spines remain
  unratified. Terminology, assessment, Chapter 17 prerequisites, renders,
  generated artifacts, and external actions remained outside scope.
- No new future-relevant effect was found. Existing dependencies already route
  every later consumer, so no duplicate outgoing handoff was created.
- The workflow validator passes with no active packet and `G-A2d` next. Both
  required negative fixtures fail with exit 1 for their exact injected defects:
  generic terminal evidence and an unknown outside-ask item.

`P2-CLAIMS` is accepted. `G-A2d` is the next permitted packet but was not
started.

## G-A2a closeout

- No incoming handoff targeted `G-A2a`; the complete handoff ledger was read
  before the decision was recorded.
- Author and editor Luka Sikic accepted the complete governing system as
  recommended on 2026-08-04, in one bounded disposition covering all 22 blocked
  items. No component amendment was requested.
- The book adopts six claim dimensions — description, association,
  generalisation, prediction, causation, decision — with population reach
  independent of claim type; six recurring audit questions; one stable
  nine-stage lifecycle with ratified part-level roles; and seven
  plant/develop/harvest threads, including the seventh communication thread
  that requires the reader to make a claim rather than only judge one.
- Statistics, data science, machine learning, and AI systems are defined once by
  their governing questions. Data science remains a delivery mechanism for the
  four promises and never becomes a fifth. The approximate 70/20/10 attention
  split is recorded as an editorial diagnostic only and may not be cited by any
  later packet to require or refuse content.
- The empirical portfolio is organised by data-generating design across eight
  designs rather than by disciplinary label or dataset count, with text priority
  over the optional World Bank extension. The four evidence objects,
  ordinary-practice ethics, the honest-sentence standard, sensitivity as primary
  plus one defensible alternative, and the poll-reading card are also accepted.
- The additions justify no new numbered chapter, central widget, or callout
  type. A thread receives a seed, one substantial harvest, and later retrieval.
- `OA-G-A2A-CLAIM-SYSTEM` is `done`; no external message was sent and no
  broader authority was inferred.
- `H-G-A2A-001` carries the accepted system and its exclusions to `P2-CLAIMS`
  at its `before_start` gate. No chapter prose, registry, spine, terminology,
  assessment contract, data package, or generated artifact changed, and
  `P2-CLAIMS` was not started.

The accepted decision source state is
`conversation:G-A2a-governing-system-approved-2026-08-04-Luka-Sikic`.

## P1-VERIFY closeout

- The accepted gate is tied to commit
  `89229759ed61ce3a3bced127496b731dfdd7cf73` and tree
  `59bbab72e2a10ea8bbd9fc5d9e95cd724a423568`. Its full twelve-row matrix is
  `notes/reports/p1-phase1-verification-2026-08-04.md`.
- The first pass exposed one exact source mismatch instead of hiding it:
  `P1A-C02` certified `ccae632a…`, while the current Chapter 2 blob was
  `908780ee…`.
- Luka Sikic authorised an evidence-only reopening of `P1A-C02` and
  `P1A-METHODS`, with no prose changes. A read-only `critic_methods` reread the
  complete current blob before and after, scored correctness, assumptions,
  interpretation and precision 5/5, and reported no fatal, major or minor
  finding. Removing the Navarro attribution created no methodological gap.
- `notes/reports/p1a-c02-methods-revalidation-2026-08-04.md` and
  `notes/reports/p1a-methods-revalidation-2026-08-04.md` bind the refreshed
  receipt and twelve-row aggregate to the current state. All other P1A chapter
  blobs still equal their original evidence.
- All twelve Phase 1 prerequisites now pass independently. Known later debts
  and all external-authority boundaries remain visible and unchanged.
- The canonical workflow validator passes with no active packet and `G-A2a`
  next. Both required in-memory negative fixtures fail for their exact injected
  defects. No new downstream handoff is needed because `G-A2a` already depends
  on the accepted gate.

## P1C-INVENTORY closeout

- Commit `8731a9d` introduces `config/book-inventory.json` as the sole
  sanctioned source for 37 pages, 19 chapter units, appendices A–F, navigation,
  the root alias and the empty solution-route inventory. No route was created
  or removed.
- `_quarto.yml` and `styles/book-include.html` carry marked generated
  projections. Profiles inherit them; rendered-HTML checks, the browser audit,
  portable-page handling and PDF/DOCX wrappers consume the same source or its
  checked projection.
- The default command fails on any missing, extra, reordered or stale path.
  The explicit `--write` command alone refreshes projections. Quarto pre-render,
  both wrappers and the publish workflow run the blocking positive gate; the
  workflow also runs all negative fixtures before render and Pages setup.
- A detached worktree at `8731a9d` restored the exact R, Node, npm, Playwright
  and Chromium locks into fresh empty paths. The 37-page positive path, a
  source-driven temporary addition, missing/extra/reordered regressions, PDF
  integration and JavaScript syntax checks all behaved as declared, and the
  worktree remained clean without render or publication.
- No new future-relevant effect was found. Existing `P1-VERIFY`, `P5-G`,
  `H-P1C-EXPORT-001` and `H-P1C-EXPORT-002` already own every downstream
  consequence, so no duplicate handoff was created and no later D10 decision
  was resolved.

The accepted inventory source state is
`inventory:sha256-1cc773c5b0a9546c2c111b994d6c9eda3797139419cb91e4396fa1d92c49e499`;
the durable evidence is
`notes/reports/p1c-book-inventory-2026-08-04.md`.

## P1C-PARITY closeout

- No applicable incoming handoff targeted `P1C-PARITY`; the complete handoff
  ledger was read before packet claim.
- Commit `79824e0524ec542b0ec1a8ae0610f1d4140d4053` records six exact and eleven
  distributional OJS/R pairs with parameters, seed policy, tolerances,
  adapter-specific golden values, adapters, source hashes, and bounded claims.
- A fresh detached worktree restored the accepted R, Node, npm, Playwright, and
  Chromium locks into empty paths. All 17 pairs passed, the deliberate
  in-memory expected-value regression returned exit 1, and the worktree stayed
  clean without rendering or publishing.
- The parity state is
  `parity:sha256-f22f3df467e42c14d2954820e1a7de39df67c374565123c418c366a0eb51a803`;
  durable evidence is in
  `notes/reports/p1c-widget-parity-2026-08-04.md`.
- `R18` is accepted because all required browser and parity children are now
  accepted. No new outgoing handoff is needed: `P1-VERIFY` already depends on
  this packet, and later source drift is blocked by the workflow and hashes.
- Inventory, catalogue, assessment, chapter, export, general browser,
  release-candidate, upload, deployment, and publication work did not occur.

## P0-REGISTER closeout

- `H-G-A0-001` and `H-P0-CONTROL-001` were consumed with evidence.
- The register contains 371 stable children under R01-R36, 188 exact packets,
  29 typed packet contracts, and 18 bidirectional source manifests.
- The validator reconciles every source fingerprint and requires structured
  receipts for every terminal packet requirement, output, and exit test.
- The `generic_packet_evidence` negative fixture proves that an arbitrary
  `done` token cannot close a packet.
- Eight forward handoffs, `H-P0-REGISTER-001` through `008`, preserve findings
  that constrain later packets.

The accepted implementation source state is
`b0a28b681fa7b4dcda6ee1b67ff80bcd303c3eac`.

## P0-STATE closeout

- `H-P0-REGISTER-001`, `H-G-A0-001`, and `H-P0-CONTROL-002` were consumed
  with preservation, authority, and implementation evidence.
- STYLE and checkout-local Bookwright contracts now agree on H1-H10 and D05:
  the preface and Part I have no visible code, hidden plumbing is exempt from
  the visible 12-line ceiling, and assessed code production is forbidden.
- Exactly 20 invalid ledger enums were migrated; all 19 chapter stages remain
  `draft`, and all four mutable shared JSON files validate against their Draft
  2020-12 schemas.
- Installed-cache structure lint now resolves the live checkout rules from the
  repository root and a nested working directory. Bookwright cachebuster
  `0.2.0+codex.20260803091452` is installed, enabled, and discoverable in a
  fresh Codex process.
- All 371 child IDs, 188 packet IDs, aliases, expansions, 18 manifests, D05,
  and the independent `P1C-INTEGRITY` boundary were preserved.
- `H-P0-STATE-001` records the only consequential downstream discovery: the
  `WA-C00` preface packet must reconcile its visible-code promise with D05.

The accepted implementation source state is
`sha256:9eaca86d36b3b7593b831d820cfd881bbdb9c114837b9431e4cc9536562fc4ab`.

## P0-OUTSIDE closeout

- `H-P0-REGISTER-002`, `H-G-A0-001`, and `H-P0-CONTROL-003` were consumed
  with inventory, authority, routing, and exact-link evidence.
- The register now contains 82 independently closable canonical asks across
  16 kinds: decisions and policy, package selection and rights, recruitment,
  specialist sign-off, proof and release ownership, and exact external-action
  authorisation.
- Every ask names its owner, available evidence, recommended default, exact
  reply, blocked register items and gates, and resume condition. All 22 packet
  gates that directly depend on `P0-OUTSIDE`, every unresolved decision gate,
  all C00-C18 acceptance gates, and all exact external-action gates are covered.
- Every ask remains `drafted_unsent`; no external message was sent and no
  permission was inferred. Push, merge, tag, archive, and deployment remain
  unauthorised.
- The workflow validator now checks the ask schema, item/gate references,
  direct-dependent coverage, message state, and inventory totals. Its
  `invalid_outside_ask_link` negative fixture fails as required.
- P0-OUTSIDE found no future-relevant effect outside the canonical ask records,
  so it created no outgoing handoff; duplicating ask state in the handoff
  ledger would violate the packet contract.

The accepted implementation source state is
`state:sha256-aacc04b76559edbea0e656bdd4e2a027a5912eff82792fda557706a60a47bdf1`.

## G-A1a closeout

- The author and named statistical reviewer Luka Sikic jointly accepted the
  recommended D01 specification on 2026-08-03.
- Chapter 10 retains raw-label permutation only for an
  exchangeability/full-distribution null and uses `(b + 1) / (B + 1)` for
  finite random-permutation p-values. The approved specification also fixes
  the known-null demonstration, observational claim boundary, analytic
  widget/twin scope, and Bayesian balance.
- `OA-G-A1A-C10-SPEC` is `done`; no external message was sent and no broader
  authority was inferred.
- `H-G-A1A-001` carries the exact approved specification to `P1A-C10` at its
  `before_start` gate.
- No chapter prose or code was changed, and `P1A-C10` was not started.

The accepted decision source state is
`conversation:joint-G-A1a-approval-2026-08-03-Luka-Sikic`.

## P1A-C10 closeout

- `H-G-A1A-001` was acknowledged and consumed before the packet claim, and the
  accepted D01 specification remained the exact correction boundary.
- Chapter 10 now states the exchangeability/full-distribution null and its
  independent-unit, observational, and noncausal assumptions; retains the
  two-sided raw difference in means; and uses `(b + 1) / (B + 1)` for every
  finite random-permutation p-value.
- The known-null demonstration, Type-I/Type-II explanation, AI-error key, and
  bounded Bayesian contrast were corrected. The analytic normal-p-value widget
  and print twin remained unchanged and outside the permutation correction.
- Clean-session reproduction, an independent methods reread on the exact
  source state, checkout-local deterministic and manual style passes,
  structure and figure-introduction checks, the targeted HTML render, and
  source-diff checks all passed.
- No new forward-relevant effect was found. Chapter 11 follow-through is
  already represented by `R01-C11-inherited-permutation` and the dependency of
  `P1A-C11` on this packet, so no duplicate outgoing handoff was created.

The accepted chapter source state is
`chapter:sha1-a90549950c4f410f757bdec9b6ac680380ab7662`; the durable evidence is
`notes/reports/p1a-c10-methods-review-2026-08-03.md`.

## P1A-C11 closeout

- No incoming handoff targeted `P1A-C11`; the packet claimed only its registered
  Chapter 11 source and control paths.
- Chapter 11 now uses `(b + 1) / (B + 1)` for its finite random-permutation
  p-value and states the empirical power curve's full-distribution null,
  statistic, independent-unit boundary, finite-population mechanism, sampling,
  and simulation assumptions.
- The analytic widget/twin and worked example now name their distinct
  independent-normal, common-known-SD, two-sided-z assumptions. Their
  algorithms remain unchanged, and the chapter stays estimation-first.
- Clean-session reproduction, an independent methods read on the exact source
  state, checkout-local deterministic and manual style passes, structure and
  figure-introduction checks, the targeted HTML render, and source-diff checks
  all passed.
- No new forward-relevant effect was found. The known later Chapter 11 work
  remains represented by its stable `WC-C11` items and dependencies, so no
  duplicate outgoing handoff was created.

The accepted chapter source state is
`chapter:sha1-2aaede845c2a93fcad5d473d6466f938285cd7b6`; the durable evidence is
`notes/reports/p1a-c11-methods-review-2026-08-03.md`.

## G-A1b closeout

- The author and named statistical reviewer Luka Sikic jointly accepted the
  recommended D02 specification on 2026-08-03.
- Chapter 14 retains Welch inference as its default. The binary-predictor OLS
  coefficient remains exactly the raw difference in means, while ordinary
  homoskedastic OLS uncertainty is explicitly separated from Welch standard
  errors and Welch-Satterthwaite degrees of freedom.
- The seeded numerical reproduction records the shared estimate of `1.185714`,
  Welch `SE = 0.372609` and `df = 102.471`, and ordinary OLS
  `SE = 0.369537` and `df = 118`. The coincident two-decimal interval display
  is not treated as inferential identity.
- `OA-G-A1B-C14-SPEC` is `done`; no external message was sent and no broader
  authority was inferred.
- `H-G-A1B-001` carries the exact approved specification to `P1A-C14` at its
  `before_start` gate. It also preserves the downstream Chapter 15/16
  revalidation boundary without starting either packet.
- No chapter prose or code was changed, and `P1A-C14` was not started.

The accepted decision source state is
`conversation:joint-G-A1b-approval-2026-08-03-Luka-Sikic`.

## P1A-C14 closeout

- `H-G-A1B-001` was acknowledged and consumed before the packet claim, and the
  accepted D02 specification remained the exact correction boundary.
- Chapter 14 now sources its default interval from Welch and states the
  two-sided population mean-difference null. The binary-predictor coefficient
  remains exactly the raw difference in means, while ordinary homoskedastic
  OLS is labelled as a distinct uncertainty procedure.
- The chapter exposes Welch `SE = 0.372609`, `df = 102.471`, and interval
  `[0.446686, 1.924742]` beside ordinary OLS `SE = 0.369537`, `df = 118`, and
  interval `[0.453930, 1.917498]`; their shared two-decimal display is no
  longer treated as inferential identity.
- Clean-session reproduction, an independent methods reread on the exact
  source state, checkout-local deterministic and manual style passes,
  structure and figure-introduction checks, the targeted HTML render, rendered
  claim assertions, widget/twin preservation, and scoped source-diff checks
  all passed.
- Chapters 15 and 16 were read for the dependency boundary but not changed.
  Their registered revalidation remains assigned to `P1A-C15` and
  `P1A-C16`, so no duplicate outgoing handoff was created.

The accepted chapter source state is
`chapter:sha1-449c88f25e032fd8d4a9066deb45c8648497e8e5`; the durable evidence is
`notes/reports/p1a-c14-methods-review-2026-08-03.md`.

## P1A-C15 closeout

- No incoming handoff targeted `P1A-C15`; the accepted D02 correction and the
  completed `P1A-C14` packet defined its dependent-revalidation boundary.
- Chapter 15 retains the common group-mean model and its point estimates as the
  bridge from Chapters 14 to 16, while its classical mean-square F ratio and
  `aov` receipt are now explicitly separated from Welch inference with
  group-specific variances and adjusted degrees of freedom.
- Clean-session reproduction confirmed classical `F = 8.381813` with df 4 and
  295, versus Welch `F = 7.320808` with denominator df 112.425285, as well as
  the complete existing Chapter 15 result set.
- An independent methods reread passed the exact final source state. The
  checkout-local deterministic and manual style passes, structure and
  figure-introduction checks, targeted HTML render, rendered-claim assertions,
  widget/twin preservation, and scoped source-diff checks also passed.
- `R09-C15-variance-ratio` and the separately registered suspect-code,
  narrative-payoff, dependence, reachback, and later Wave D repairs remain
  unmodified. Chapters 14 and 16 are unchanged.
- No new forward-relevant effect was found. Chapter 16 follow-through is
  already represented by `R02-C16-dependent-revalidation` and the dependency
  of `P1A-C16` on this packet, so no duplicate outgoing handoff was created.

The accepted chapter source state is
`chapter:sha1-0eadfd02627a95aed614a005f93f81878249ea10`; the durable evidence is
`notes/reports/p1a-c15-methods-review-2026-08-03.md`.

## P1A-C16 closeout

- No incoming handoff targeted `P1A-C16`; accepted D02 and the completed
  `P1A-C14` and `P1A-C15` packets defined its dependent-revalidation boundary.
- Chapter 16 now preserves the common group-mean point estimates while naming
  pooled Student and classical ANOVA as ordinary homoskedastic special cases
  whose inference is distinct from Welch.
- The main analysis consistently targets finite-population least-squares
  coefficients for the recorded outcome among all 50,000 units. Latent
  pre-measurement generator parameters are diagnostic comparators, and the
  census target carries no sampling interval.
- Prediction is evaluated immediately before the trust response. Willingness
  to pay is excluded as post-outcome target leakage, and the valid examples use
  disjoint learning and held-out units with eligible predictors available by
  the same time boundary.
- Clean-session reproduction confirmed the complete Chapter 16 result receipt.
  An independent methods reread passed exact source
  `ba93f9a62965dc1a9ae1c67a3c54d536976773cb` with no finding or requested
  change. Style, structure, figure, widget, render, rendered-claim, source-diff,
  and closeout checks also passed.
- Chapters 14 and 15, the widget and print-twin sources, and every separately
  registered later Chapter 16 repair remain unchanged. No new forward-relevant
  effect was found, so no duplicate outgoing handoff was created.

The accepted chapter source state is
`chapter:sha1-ba93f9a62965dc1a9ae1c67a3c54d536976773cb`; the durable evidence is
`notes/reports/p1a-c16-methods-review-2026-08-03.md`.

## P1A-C02 closeout

- No incoming handoff targeted `P1A-C02`; the four ratified Chapter 2 items
  and the exact packet instruction defined its surgical boundary.
- Chapter 2 now states randomisation as balance in expectation rather than
  guaranteed realised equality. It distinguishes assignment or offer from
  treatment received and qualifies adherence, spillover, attrition, and
  differential measurement.
- The negative item-rest association is now a diagnostic rather than proof of
  reverse coding, with multidimensionality, translation, wording, and
  inattentive response retained as alternatives. Stevens's levels are
  historicised and bounded as a practical description rather than a complete
  rule for permissible analysis.
- A confounder is now a common prior cause, distinct from a mediator and
  collider. The prose rejects controlling everything and accurately describes
  the zero-shift widget as the same negative conclusion with nonidentical fitted
  slopes.
- Clean-session reproduction confirmed the full item-rest, score-range, and
  widget-slope receipt. An independent methods reread passed exact source
  `ccae632a5d5adcb0e30d69ed3705b6e9f5a74a00` with no remaining finding after
  one minor widget-guidance precision sentence was corrected.
- Checkout-local deterministic and manual style passes, structure and
  figure-introduction checks, the all-widget contract, targeted HTML render,
  23 rendered presence/absence assertions, code-block preservation, scoped
  source diff, and closeout checks all passed. No separately registered later
  Chapter 2 work changed, and no new forward-relevant effect was found.

The accepted chapter source state is
`chapter:sha1-ccae632a5d5adcb0e30d69ed3705b6e9f5a74a00`; the durable evidence is
`notes/reports/p1a-c02-methods-review-2026-08-03.md`.

## P1A-C06 closeout

- No incoming handoff targeted `P1A-C06`; the four ratified Chapter 6 items
  and the exact packet instruction defined its surgical boundary.
- The scatterplot is now primary. Pearson--Spearman agreement is only a clue,
  not proof of linearity, robustness, or the absence of influential
  observations. Disagreement prompts graphical and data investigation rather
  than an automatic diagnosis or method choice.
- Range-restriction attenuation is conditional on relationship form,
  dispersion, and selection. The narrow-age example now distinguishes a
  changed target population from an attenuated version of one unchanged
  relation and allows weakening, strengthening, or sign reversal under other
  conditions.
- Clean-session reproduction confirmed every Chapter 6 value affected by the
  argument. An independent methods reread passed exact source
  `c3177eb7cc5abe87cca6e1781262925b50e0f6b2` with no remaining finding after
  four local precision defects from its first pass were corrected.
- Checkout-local deterministic and manual style passes, structure and
  figure-introduction checks, the all-widget contract, targeted HTML render,
  24 rendered presence/absence assertions, executable-block preservation,
  scoped source diff, and closeout checks all passed. No separately registered
  later Chapter 6 work changed, and no new forward-relevant effect was found.

The accepted chapter source state is
`chapter:sha1-c3177eb7cc5abe87cca6e1781262925b50e0f6b2`; the durable evidence is
`notes/reports/p1a-c06-methods-review-2026-08-03.md`.

## P1A-C07 closeout

- No incoming handoff targeted `P1A-C07`; the single ratified Chapter 7 item
  and the exact packet instruction defined its surgical boundary.
- Chapter 7 now states the introductory central-limit-theorem conditions as a
  stable common distribution, independent observations, and finite variance.
  It notes that broader variants permit appropriately weak but not arbitrary
  dependence.
- The Bernoulli widget is explicitly a bounded demonstration rather than a
  universal guarantee for arbitrary data, sample sizes, dependence, or
  infinite-variance populations.
- Clean-session reproduction confirmed every Chapter 7 value and source
  relationship. An independent methods reread passed exact source
  `8deb7a2b686754bdb3bc6d0ddfca2c7ade472f76` with no finding or requested
  change.
- Checkout-local deterministic and manual style passes, structure and
  figure-introduction checks, the all-widget contract, targeted HTML render,
  rendered-claim assertions, executable-block preservation, scoped source
  diff, and closeout checks all passed. No separately registered later Chapter
  7 work changed, and no new future-relevant effect was found.

The accepted chapter source state is
`chapter:sha1-8deb7a2b686754bdb3bc6d0ddfca2c7ade472f76`; the durable evidence is
`notes/reports/p1a-c07-methods-review-2026-08-03.md`.

## P1A-C08 closeout

- No incoming handoff targeted `P1A-C08`; the three ratified Chapter 8 items
  and the exact packet instruction defined its surgical boundary.
- Chapter 8 now names the simple-random-sampling assumptions behind its
  standard-error, margin, and sample-size formulas and explains when the
  finite-population correction matters.
- Unequal selection probabilities, sampling weights, clustering, design
  effects, effective sample size, and design-aware uncertainty are explained
  at literacy level without importing a complex-survey variance course.
- The roughly-thousand-person heuristic is bounded by estimand, design,
  selection and response, subgroup size, and desired precision; it no longer
  implies that sample size repairs coverage or nonresponse.
- Clean-session reproduction confirmed every affected result. After four
  first-pass precision points were corrected, an independent methods reread
  passed exact source `b9a435a2ebb1e1371f4069cc8f9a4250459e419f` with no
  remaining finding and scores of 4/4 throughout.
- Checkout-local deterministic and manual style passes, structure and
  figure-introduction checks, the all-widget contract, targeted HTML render,
  rendered-claim assertions, scoped executable-block comparison, source diff,
  and closeout checks all passed. No separately registered later Chapter 8
  work changed, and no new future-relevant effect was found.

The accepted chapter source state is
`chapter:sha1-b9a435a2ebb1e1371f4069cc8f9a4250459e419f`; the durable evidence is
`notes/reports/p1a-c08-methods-review-2026-08-03.md`.

## P1A-C09 closeout

- No incoming handoff targeted `P1A-C09`; the three ratified Chapter 9 items
  and the exact packet instruction defined its surgical boundary.
- Mean plus or minus 1.96 sample standard deviations is now a descriptive
  normal-rule range conditional on approximate normality. It is explicitly
  distinguished from an individual prediction interval and from the
  confidence interval for a mean.
- The bootstrap-median example now demonstrates construction of one
  percentile range, not coverage. It explicitly separates that procedure from
  the earlier repeated z-interval experiment for a mean.
- The ordinary bootstrap now names empirical representativeness,
  independence/exchangeability, and the correct resampling unit, together with
  small-sample, discreteness, missing-tail, heavy-tail, and
  extreme-percentile limits.
- Clean-session reproduction confirmed every affected result. A first methods
  reading passed the three repairs but found a 10,000-versus-2,000 count
  mismatch in the comparison passage. After correction, an independent fresh
  reread passed exact source `67380c04d31d3370b1ff63e2533d70a12338ba0d`
  with no remaining finding and scores of 4/4 throughout.
- Checkout-local deterministic and manual style passes, structure and
  figure-introduction checks, the all-widget contract, targeted HTML render,
  rendered-claim assertions, scoped executable-block comparison, source diff,
  and closeout checks all passed. No separately registered later Chapter 9
  work changed, and no new future-relevant effect was found.

The accepted chapter source state is
`chapter:sha1-67380c04d31d3370b1ff63e2533d70a12338ba0d`; the durable evidence is
`notes/reports/p1a-c09-methods-review-2026-08-03.md`.

## P1A-C13 closeout

- No incoming handoff targeted `P1A-C13`; the two ratified Chapter 13 items
  and the exact packet instruction defined its surgical boundary.
- The source now computes, defines, names, prompts, summarizes, and interprets
  adjusted standardized residuals. The absolute-value-near-two orientation is
  conditioned on a suitable hi-kvadrat approximation and is not presented as
  separate cell-level evidence.
- Null runs now estimate type-I-error calibration under independence, while
  distinct alternative runs estimate power for a predeclared population
  Cramer's V of 0.20. Threshold, repetition count, no-Yates rule, exceptional
  tables, displayed values, widget, and print twin are aligned.
- Clean-session reproduction confirmed every affected result. An independent
  methods reader passed exact source
  `9242e057c6602b273368164de6193b08eba5eeb8` with no fatal, major, or minor
  concern and scores of 5/5 throughout.
- Checkout-local deterministic and manual style passes, structure and
  figure-introduction checks, the all-widget contract, targeted HTML render,
  rendered-claim assertions, scoped executable-block comparison, source diff,
  and closeout checks all passed. No separately registered later Chapter 13
  work changed, and no new future-relevant effect was found.

The accepted chapter source state is
`chapter:sha1-9242e057c6602b273368164de6193b08eba5eeb8`; the durable evidence is
`notes/reports/p1a-c13-methods-review-2026-08-03.md`.

## P1A-C18 closeout

- No incoming handoff targeted `P1A-C18`; the single ratified Chapter 18 item
  and the exact packet instruction defined its surgical boundary.
- The aggregate and age-adjusted estimates now appear with their intervals.
  The interpretation retains the small effects of either sign compatible with
  the adjusted interval and does not infer absence from a threshold crossing.
- The known simulation generator remains distinct from what the fitted model
  and interval can establish. Data, models, displayed tables, figures,
  exercises, citations, AI callouts, and privacy passages did not change.
- Clean-session reproduction confirmed every affected result. An independent
  methods reader passed exact source
  `f291e63173892eca483ed9c9e89df70be5bb1bd1` with no fatal, major, or minor
  concern and scores of 5/5 throughout.
- Checkout-local deterministic and manual style passes, structure and
  figure-introduction checks, the all-widget contract, targeted HTML render,
  rendered-claim assertions, scoped executable-block comparison, source diff,
  and closeout checks all passed. No separately registered later Chapter 18
  work changed, and no new future-relevant effect was found.

The accepted chapter source state is
`chapter:sha1-f291e63173892eca483ed9c9e89df70be5bb1bd1`; the durable evidence is
`notes/reports/p1a-c18-methods-review-2026-08-03.md`.

## P1A-METHODS closeout

- All 12 named prerequisite packets are `accepted`. Each has exactly three
  structured required-evidence receipts, two structured output receipts, and
  three passed exit-test receipts; no generic completion token stands in for
  packet evidence.
- All 12 live chapter blobs match the source state declared by the packet,
  item records, durable report, independent methods reading, and handoff packet
  review. The gate is tied to commit
  `7832b07ee92e98a962fc79b291389118e95f29b6` and tree
  `7168b933c16b92ccb3d5c3de13e1dd4a7f30a538`.
- Every approved or ratified correction specification, clean-session numerical
  reproduction, exact-source independent methods reading, required output, and
  packet exit test passed the gate-specific matrix. `H-G-A1A-001` and
  `H-G-A1B-001` were already consumed correctly by Chapters 10 and 14; no
  handoff targets P1A-METHODS.
- No bounded gate blocker remains. `R09-C15-variance-ratio` is explicitly still
  `ratified` and outside the accepted P1A-C15 dependent-revalidation scope; it
  and all other later-wave obligations remain open rather than being hidden by
  this aggregate gate.
- The checkout-local workflow validator passed. Both required negative
  fixtures failed as required, and the source-diff and packet exit checks
  passed. No chapter prose changed, no future-relevant effect beyond existing
  dependencies was found, and `G-A1c` was not started.

The accepted gate source state is
`commit:7832b07ee92e98a962fc79b291389118e95f29b6`; the durable evidence is
`notes/reports/p1a-methods-verification-2026-08-03.md`.

## G-A1c closeout

- Author and licence or data-lane policy owner Luka Sikic accepted three
  independently closable dispositions on 2026-08-03.
- Under amended D11, the first-edition objective is to minimise and wherever
  practicable eliminate Navarro reliance. Nonessential Navarro-specific
  analogies, argumentative sequences, and citations are removed; necessary
  explanations are rebuilt independently and supported with primary or other
  independently verified sources where evidence is needed. Provenance is not
  concealed: materially derived content that survives retains scholarly
  attribution and any verified ShareAlike obligation.
- Under D12, every generated teaching dataset receives CC BY 4.0, subject to
  reconciliation with the final book licence.
- Under D08, only licence-cleared files may be bundled; uncertain
  redistribution stays portal-mediated, restricted sources stay external, and
  every required pathway receives a cleared bundled or aggregate fallback. No
  package-specific exception was approved, and access was not treated as
  redistribution authority.
- The three canonical G-A1c asks are `done`; no external message was sent and
  no third-party permission was inferred. The original Navarro handoff
  `H-G-A1C-001` was superseded before packet claim by `H-G-A1C-004`, which
  carries the stricter reduced-reliance decision to `P1B-NAVARRO`.
  `H-G-A1C-002` and `H-G-A1C-003` carry the generated-data and lane decisions
  to `P1B-DATA-LIC`.
- No chapter prose or code was changed, and neither evidence/licence packet was
  started.

The accepted decision source state is
`conversation:G-A1c-owner-dispositions-as-amended-2026-08-03-Luka-Sikic`.

## P1B-NAVARRO closeout

- `H-G-A1C-001` was explicitly acknowledged as the superseded required
  baseline, and its stricter replacement `H-G-A1C-004` was consumed before the
  first substantive edit. The zero-use owner disposition in
  `OA-G-A1C-NAVARRO-BOOK-LICENCE` is now fully reconciled with the completed
  audit.
- The authoritative version 0.6 PDF, its CC BY-SA 4.0 notice, attribution and
  ShareAlike terms, official compatible-licence list, and the expression-versus-
  idea boundary were verified. The audited PDF has SHA-256
  `CEB73307B5B0D310120E3E1470917B80189AFA11BEC3487F3910C8B1FA5BFE16`.
- All four candidates in Chapters 1, 2, and 4 received a passage-level source
  correspondence and disposition. One unsupported candidate was removed;
  three necessary explanations were rebuilt independently. No materially
  derived Navarro expression, distinctive structure, name, citation, or
  reader-facing reference survives.
- `LICENSE`, `README.md`, `references.bib`, the three chapter provenance
  records, both project plans, and AI-export licence metadata now agree: the
  repository's original text, code, and associated documentation use MIT,
  while datasets and other third-party materials retain separately verified
  terms.
- Checkout-local deterministic style lint and the complete manual H1–H10 pass
  succeeded for all three changed chapters. Targeted HTML renders succeeded;
  visible-source, citation-key, bibliography-record, and source-diff checks
  also passed. Generated pre-render artifacts were restored and are absent
  from the packet diff.
- `H-P1B-NAVARRO-001` carries the verified book-licence boundary to
  `P1B-DATA-LIC` and prevents `P1B-BIB` from restoring the unreliable Navarro
  record without a new scoped need, authoritative metadata, and rights review.
  No later packet was started.

The accepted implementation source state is
`state:sha256-fc7f6536b53df8080f209bcba8505cd8d09d96047a5e3e88cc58a7db2664402c`;
the durable evidence is
`notes/reports/p1b-navarro-provenance-and-licence-audit-2026-08-03.md`.

## P1B-DATA-LIC closeout

- `H-G-A1C-002`, `H-G-A1C-003`, and `H-P1B-NAVARRO-001` were acknowledged
  and consumed before the first substantive edit. The accepted owner
  dispositions are now implemented without a package-specific exception.
- The durable inventory records source, version, licence, attribution,
  access, and redistribution separately for all four current and thirteen
  proposed packages. Every package has exactly one `bundled`,
  `portal-mediated`, or `external-only` lane and a lawful fallback for every
  required student pathway.
- Technical availability was never promoted into redistribution authority.
  DIP, unselected Eurostat, and ESS remain portal-mediated under the recorded
  conditions; R built-ins and every other source without authoritative
  exact-package rights evidence remain external-only. DZS tourism,
  ParlaMint-HR, and ParlaSent retain later exact-package gates despite their
  verified general bundled basis.
- `anketa_mreze`, `populacija_medija`, and every future materialised snapshot
  now carry one consistent CC BY 4.0 notice. The generator code and original
  book remain MIT, while all third-party data terms stay separate.
- `R/fetch-podaci.R` now fails closed unless a package is `bundled` with
  verified redistribution. The public data page, Appendix C, repository and
  data README files, generator, and download-adjacent notice agree.
  `data/katalog.yml` was not created before P3-CATALOG.
- Checkout-local style lint and the full manual H1–H10 pass succeeded for the
  two reader-facing files. Both targeted HTML renders passed, both R sources
  executed, the 17-of-17 lane check and six-location licence check passed,
  and generated pre-render artifacts were restored outside the packet diff.
- `H-P1B-DATA-LIC-001`, `H-P1B-DATA-LIC-002`, and
  `H-P1B-DATA-LIC-003` carry the generated-snapshot, canonical-catalogue, and
  package-gate constraints to their exact later consumers. `P1B-BIB` was not
  started.

The accepted implementation source state is
`state:sha256-2e0f065b18182f1ccce781a48458cebf49d0e3e9c59790e64fb97f776a110c32`;
the durable evidence is
`notes/reports/p1b-data-licence-access-inventory-2026-08-03.md`.

## P1B-BIB closeout

- `H-P1B-NAVARRO-001` was consumed before the first substantive edit. The
  verified zero-Navarro result remains intact, and neither `@navarro2019` nor
  a Navarro bibliography record was restored.
- All 121 live citation uses in 21 manuscript files were read in context. The
  resulting 35 unique keys resolve one-to-one to 35 maintained bibliography
  records; the sole unused seed record was removed.
- Blanket `nocite: @*` and its obsolete temporary commentary were removed.
  Pandoc citeproc rendered exactly the 35 actually used references.
- All 29 DOI-bearing records resolve through Crossref with matching titles.
  Every journal and proceedings record now carries a verified DOI. The six
  works without DOI have verified publisher, author, library, or institutional
  records and explicit no-DOI dispositions.
- Gelman and Loken's working paper now has its verified 14 November 2013
  version and stable Columbia locator. Three page ranges formerly omitted
  because Crossref exposed only a starting page were added from authoritative
  publisher, source-document, or government bibliographic records.
- The exhaustive claim-source fit pass found one defect. Chapter 17 had
  substituted equal overall accuracy for one of Chouldechova's error-rate
  criteria. The sentence now states the supported calibration, false-positive,
  and false-negative incompatibility without introducing a new source.
- Checkout-local style lint and the complete manual H1-H10 pass succeeded for
  Chapter 17. A targeted HTML render contained the corrected sentence;
  generated pre-render artifacts were restored outside the packet diff.
- No new future-relevant constraint remains. The whole-book evidence audit is
  already assigned to P6-EVIDENCE, and P1B-META already depends on this packet,
  so no duplicate outgoing handoff was created. No later packet was started.

The accepted implementation source state is
`state:sha256-8e9a96cf20573f7f96f95155189f20dfdb6e4e26de773545b415683ce102abd0`;
the durable evidence is
`notes/reports/p1b-bibliography-metadata-audit-2026-08-03.md`.

## P1B-META closeout

- No incoming handoff targeted P1B-META. The full documentation contract,
  R06-META-readme, README, every public status or pathway promise it makes,
  its governing documents, and the corresponding live repository paths were
  read before the public edit.
- README no longer describes an empty skeleton. It now identifies a
  substantive draft under comprehensive review, keeps all 19 ledger units at
  `draft`, and labels the website, PDF, and DOCX as development artifacts
  rather than evidence of a published edition.
- The unsupported complete-installation claim was removed because no
  `renv.lock` exists. The `kolegij` row now promises only its implemented open
  code behavior; no solution gate exists in the current source.
- The PDF and DOCX instructions now match their actual wrappers. The current
  nonblocking CI PDF risk is stated without pre-empting P1C-PDF, and no
  version, citation, archive, errata, tag, deployment, or release mechanism was
  inferred before G-A1d and P1B-GOV.
- Navigation now distinguishes editing existing chapter drafts, consulting
  fail-closed data rules, and checking the fixed canonical order. STYLE's
  public rule count is corrected from H1-H9 to H1-H10, and the design
  provenance sentence agrees with DESIGN.md.
- All ten relative README links resolve. The ledger check found 19 present
  source units, all `draft` and with `last_render: ok`; the widget checker
  passed all 17 records; obsolete-promise, wrapper, workflow, source-diff, and
  whitespace checks passed.
- `H-P1B-META-001` through `H-P1B-META-004` carry the exact later
  reconciliation work to P1C-LOCK, P1C-PDF, P5-ROUTES, and P2-DOCS. No later
  packet was started.

The accepted implementation source state is
`state:sha256-11be9838488aaa37c614ff0980b66883146a1caae57eaa6230e751420b1ef206`;
the durable evidence is
`notes/reports/p1b-public-metadata-audit-2026-08-03.md`.

## G-A1d closeout

- Luka Sikic explicitly accepted the recommended edition/version, Croatian
  changelog, citation, provenance, archive-plan, term-freeze, and errata
  mechanism on 2026-08-03 and accepted the release, archive, and errata owner
  responsibilities.
- D14 remains in force: *Osnove statistike za društvene znanosti* is the
  working release title unless the author changes it before citation metadata
  is frozen. G-A1d does not freeze final title, authorship, version, date,
  citation, or release artifacts.
- The register records the considered alternatives, the complete blocked
  dependency set, and the boundary that no push, merge, tag, archival deposit,
  deployment, publication, or other external action is authorised.
- `OA-G-A1D-EDITION-MECHANISM`, `OA-G-A1D-ARCHIVE-OWNER`,
  `OA-G-A1D-ERRATA-OWNER`, and `OA-G-A1D-RELEASE-OWNER` are `done`; no
  external message was sent.
- `H-G-A1D-001` carries the accepted decision, ownership, D14, and authority
  boundary to `P1B-GOV` at its `before_start` gate. Later G-A5c, G-A5d, G-A6,
  and exact external-action gates remain mandatory.
- No chapter prose, code, public release mechanism, or later packet was
  started.

The accepted decision source state is
`conversation:G-A1d-four-owner-dispositions-2026-08-03-Luka-Sikic`.

## P1B-GOV closeout

- `H-G-A1D-001` was acknowledged and consumed with an exact disposition and
  evidence before the first substantive edit.
- `release/governance.yml` is the canonical pre-release state. It retains the
  D14 working title, keeps final authorship, edition, version, date, citation,
  persistent identifier, tag, archive identifier, term edition, and public
  errata target unset, and records zero persisted release transitions.
- Luka Sikic is recorded as release, archive, and errata owner. Term-freeze
  ownership remains explicitly gated by `G-A5c`.
- `CHANGELOG.md`, the landing-page and colophon citation boundaries, the
  SHA-256 provenance manifest, archive plan, term-freeze policy, and the dated
  Croatian errata page and log are implemented locally.
- The non-persisting demonstration attempts the first metadata transition and
  is blocked by missing `G-A5b` as designed. All seven external or inferred
  authority flags remain `false`; no final or immutable release state exists.
- The release-governance validator, checkout-local style lint, manual Croatian
  pass, token check, targeted landing/errata renders, workflow validator, and
  both required negative fixtures passed. Generated pre-render artifacts were
  restored outside the packet diff.
- `H-P1B-GOV-001` carries the canonical paths and exact later gate boundaries
  to the release-candidate, metadata, archive, term-freeze, and deployment
  packets. No later packet was started or accepted.

The accepted implementation source state is
`governance:sha256-dcfcc7d7d8ac052546711f45d38a79b97a52a4d9d3c8a71f06c4d7f92c1ea002`;
the durable evidence is
`notes/reports/p1b-release-governance-2026-08-04.md`.

## P1C-LOCK closeout

- `H-P1B-META-001` was acknowledged before the first substantive edit and
  consumed with an exact disposition and evidence before closeout.
- Commit `945e7cc` pins R 4.6.0, renv 1.2.4, Node 24.15.0, npm 11.12.1,
  Playwright 1.62.1, and Playwright Chromium revision 1234 through committed
  R and browser lock inputs. CI no longer has an ad hoc no-lock R fallback.
- The single public command `python scripts/restore-dependencies.py` rebuilt
  the R library and Playwright browser from a detached clean worktree with new
  cache, library, npm, and browser paths. The proof worktree remained clean.
- The deliberate `missing-browser-lock` fixture exited 2 before installation;
  no unlocked fallback ran. README's temporary warning was replaced only after
  that cold positive and negative evidence existed.
- PDF behavior, integrity checks, and the live browser audit were not changed.
  `H-P1C-LOCK-001` carries the exact locked-browser boundary to
  `P1C-BROWSER` and the lock/provenance boundary to `P7-FREEZE`.

The accepted dependency source state is
`dependencies:sha256-aaf12f9d337efd342cf13a6db37d30b437cf351e19b6c68a78ae528fbabf49e8`;
the durable evidence is
`notes/reports/p1c-lock-dependency-restore-2026-08-04.md`.

## P1C-PDF closeout

- `H-P1B-META-002` was acknowledged before the first substantive edit and
  consumed with an exact disposition and evidence before closeout.
- Commit `f2c4f82` makes the approved wrapper the workflow's only PDF entry
  point. The step is blocking, precedes generated HTML changes, and has no bare
  profile, conditional copy, warning branch, or stale fallback.
- The wrapper invalidates both old PDFs, leaves `_quarto.yml` unchanged,
  validates the fresh `%PDF-` artifact, copies it only after success, and
  requires identical source and served SHA-256 hashes. Every failure removes
  both eligible outputs.
- A detached clean worktree restored the committed R and browser locks into
  fresh paths. Its real build replaced old hash `b5b18b…` with a new
  2,570,017-byte artifact at `cb5791…`; no prior PDF supplied the result.
- Isolated fixtures proved positive replacement plus deliberate wrapper,
  render-command, and stale/missing-artifact failures. All three negative cases
  returned nonzero, preserved configuration bytes, and left zero PDFs.
- README's warning was replaced only after those proofs. No PDF was committed
  or published, and `P1C-INTEGRITY`, `P1C-EXPORT`, and later packets were not
  started.
- `H-P1C-PDF-001` carries the stale AGENTS.md deployment description to
  `P2-DOCS`; no other future-relevant effect was found outside existing
  release-proof gates.

The accepted PDF-path source state is
`pdf-path:sha256-28360c3532803d3f8b32198335f783747bce84223ba2fbe94a6b3a89ae1d4866`;
the durable evidence is
`notes/reports/p1c-pdf-release-path-2026-08-04.md`.

## P1C-INTEGRITY closeout

- `H-P0-REGISTER-005` was acknowledged before the first substantive edit and
  consumed with an exact disposition and evidence before closeout.
- Commit `919b0b1` makes token, deterministic hard-style, fixed-core
  manuscript structure, figure-introduction, citation, concept, and current
  data-integrity checks blocking. Every command remains independently
  callable and every Bookwright diagnostic runs from checkout-local paths.
- A detached worktree restored R 4.6.0, Node 24.15.0, npm 11.12.1,
  Playwright 1.62.1, and Chromium revision 1234 into fresh paths. All seven
  positive lanes passed on the exact commit and the worktree stayed clean.
- Seven deliberate defects independently returned exit 1: token drift, a hard
  style violation, a missing vignette, an unregistered figure without an
  introduction, an unknown citation key, a duplicate definition ID, and a
  duplicate data key. The aggregate fixture harness passed only because all
  seven failed as required.
- The gate admits only two exact pre-existing registered debts under
  cryptographic fingerprints: `fig-anscombe` for `R28-C05-introduction`, and
  the pre-ratification concept-ledger/graph gap for
  `R04-TERMS-concept-regeneration`. Any new, changed, or stale exception fails.
- `H-P1C-INTEGRITY-001` and `H-P1C-INTEGRITY-002` route retirement of those
  exact debt entries to `WB-C05` and `P2-TERMS`. No other future-relevant
  effect was found.
- PDF, export, browser, parity, and configuration-driven inventory work did
  not enter the packet. No render, upload, deployment, or publication action
  occurred.

The accepted integrity source state is
`integrity:sha256-8699a3b2dbd07be1b39a75bd800fafc00e4162c0188ce027aa6139e7b00f4147`;
the durable evidence is
`notes/reports/p1c-integrity-gates-2026-08-04.md`.

## P1C-EXPORT closeout

- No incoming handoff targeted `P1C-EXPORT`; that absence was recorded before
  the first substantive edit.
- Commit `ac7c34f` adds an independently callable `--release` mode that makes
  build errors, protected-content leaks, metadata drift, missing outputs, and
  unexpected stale AI Markdown artifacts fatal. Local pre-render use remains
  best-effort outside the release path.
- The publish workflow now builds and validates AI exports before HTML render,
  runs all three deliberate failure fixtures, and validates final artifacts
  after render. Those steps are blocking and contain no fallback or
  `continue-on-error`.
- Every `content-visible when-profile` body is excluded. The release audit
  covers all 19 chapter inputs and all appendix sources, found 20 protected
  regions, and confirmed that none occurs in the public artifacts.
- Export metadata comes from `release/governance.yml` and its declared
  authorship source. The generated manifest and Markdown headers agree on the
  working title, `pre_release` state, site URL, and both authors.
- A detached copy of the exact implementation commit restored the locked R,
  Node, npm, Playwright, and Chromium inputs into fresh paths. Its positive
  release build, post-build validation, and all three negative fixtures passed
  without publishing; the worktree remained clean.
- `H-P1C-EXPORT-001` carries the protected-route constraint to `P2-ASSESS` and
  `P5-ROUTES`. `H-P1C-EXPORT-002` records the pre-existing clean-checkout
  `_quarto.yml` provenance checksum mismatch for `P7-FREEZE` and `P8-META`.
- Browser, parity, inventory, catalogue, assessment-policy, chapter, upload,
  deployment, and publication work did not enter the packet.

The accepted export source state is
`export-path:sha256-3453f828e47b5d3895295b7dd092de730cbe7e0eda7c0fc8cdc1ddd7fde9b4de`;
the durable evidence is
`notes/reports/p1c-export-release-path-2026-08-04.md`.

## P1C-BROWSER closeout

- `H-P1C-LOCK-001` was consumed with the exact accepted manifest, versions,
  hashes, and implementation boundary before packet claim.
- Commit `8b04c6c` makes the rendered-HTML browser smoke audit resolve only the
  checkout-local Playwright 1.62.1 package and launch its installed Chromium
  revision 1234. `NODE_PATH`, the developer-local Chrome path, and any
  executable override are absent.
- The independent command starts its own loopback server and verifies one
  representative widget at widths 1280 and 390 in light and dark modes. It
  operates the panel, slider, reset, and theme toggle by keyboard and verifies
  a nonempty polite live region and the absence of horizontal overflow.
- A detached worktree restored fresh R, npm, `node_modules`, and browser paths
  from the accepted locks. The smoke passed even with an invalid `NODE_PATH`,
  the missing-route fixture returned HTTP 404 and exit 1 as required, and the
  proof worktree remained clean.
- The workflow installs Chromium from the locked local Playwright CLI and runs
  both browser checks after HTML render and before Pages setup or upload. Both
  steps are blocking, have no fallback, and do not publish.
- The accepted P1C-LOCK inputs are unchanged. Browser parity, exports,
  inventories, catalogue, assessment policy, chapters, and general browser or
  assistive-technology coverage were not changed.
- No new future-relevant effect was found. Existing P7-A11Y, P7-HTML,
  P1C-PARITY, P1C-INVENTORY, and H-P1C-LOCK-001 already own every later
  consequence, so no duplicate outgoing handoff was created.

The accepted browser-smoke source state is
`browser-smoke:sha256-c76a872c9bbf374c3ed9e28b8f952636bbad2448bdfbb0a265494bc941c03ba7`;
the durable evidence is
`notes/reports/p1c-browser-smoke-audit-2026-08-04.md`.

## Findings that constrain later packets

- `WB-C05` must retire the exact `fig-anscombe` integrity-debt entry after the
  approved introduction is added; a fixed figure with a stale exception fails.
- `P2-TERMS` must reconcile the live definitions, concept ledger, and generated
  graph and retire both exact concept-debt fingerprints; changed debt fails.
- All 18 displayed chapter reading times must ultimately be measured against a
  relevant source state, visibly labelled as estimates, or removed.
- Chapter 17's live spine must settle whether Chapter 13 is a prerequisite
  before either advertised route is published.
- Identity-pillar prose waits for its governed evidence package and approved
  brief; Chapter 17 retains the fairness widget and uses text analysis as its
  worked example.
- Any material chapter edit invalidates an older six-critic panel for final
  acceptance purposes.
- P7-FREEZE must record the accepted Node, npm, Playwright, Chromium, R, and
  renv locks and hashes in the release-candidate provenance record.
- P2-ASSESS has ratified the structural public-export boundary for every future
  solution or instructor route. P5-ROUTES must implement it from the one-record
  contract and rerun the release leak proof against the final route set.
- P7-FREEZE and P8-META must repair and clean-check the pre-existing
  `_quarto.yml` provenance checksum mismatch; final metadata may not introduce
  a competing source or worktree-specific line-ending hash.
- `scripts/check-concepts.py` moved to blob `a1f78624…` and new
  `scripts/r_env.py` was added in out-of-packet fix commit `13dee63`. The
  concept check ran `build-concept-graph.R` in a temporary working directory,
  where the checkout `.Rprofile` never loads and renv therefore never
  activates, so the subprocess lost the locked library and failed on missing
  `yaml` despite a correct `renv.lock`. The same defect silently satisfied the
  concept negative fixture, which asserts only a nonzero exit, so the injected
  duplicate definition went untested from `P1C-INTEGRITY` closeout until this
  fix. The accepted `integrity:sha256-8699a3b2…` state and the seven-lane
  evidence in `notes/reports/p1c-integrity-gates-2026-08-04.md` predate the
  repair. P7-FREEZE must record the then-current blobs, and any later packet
  re-proving the integrity lanes must treat the pre-fix concept-fixture result
  as unproven rather than passed.
- `.github/workflows/publish.yml` moved from blob `1665d320…` to `8483793c…`
  in out-of-packet CI commit `1bc1963`, which installs `librsvg2-dev` for the
  pinned `rsvg` source build and raises the checkout action to v5. The
  `P1C-INVENTORY` manifest and its accepted `inventory:sha256-1cc773c5…` state
  remain true of commit `8731a9d` but no longer describe the live file, and the
  `P1C-PARITY` record already carried an older blob. P7-FREEZE must record the
  then-current blob rather than any of these historical values, and P1C's
  workflow-behaviour claims should be reconfirmed against the amended file
  before the release-candidate provenance record is populated.
- The ratified Part I spine approves exactly three new `#def-` blocks —
  `jedinica analize` and `Simpsonov paradoks` in Chapter 1 and `temeljna stopa`
  in Chapter 3 — but none was written, because the concept gate is frozen until
  `P2-TERMS`. `P2-TERMS` must expect them, `WA-C01` and `WA-C03` must add exactly
  those and no others, and neither may define a term the spine placed in prose
  or deferred.
- P2-DOCS must reconcile AGENTS.md's stale description of the former
  nonblocking PDF workflow with the accepted wrapper-only blocking path.
- P5-ROUTES must re-audit every public route promise; absent solution gates and
  unfinished no-code or other pathways may not be advertised as complete.
- P2-DOCS must reconcile stale internal comments about profile solutions,
  visual-identity selection, and provisional structural conventions.
- P7-FREEZE and P7-CLEAN-BUILD must populate the canonical provenance record
  with the accepted source, locks, data, tools, and cross-format artifact
  hashes rather than create a competing record.
- G-A5c must confirm the term-freeze owner. P8-META must replace the null
  release fields only from the accepted metadata decision, while P8-ARCHIVE
  and P8-DEPLOY retain their exact immediate G-A6 authority gates.

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

Paste this into a new thread:

```text
Continue the ratified comprehensive-review implementation from the repository's
canonical state. Read AGENTS.md and fully read:
- notes/reports/comprehensive-review-implementation-plan-2026-08-03.md
- notes/reports/comprehensive-review-implementation-register.yml
- notes/reports/comprehensive-review-dashboard.md
- notes/reports/comprehensive-review-forward-handoffs.yml
Also fully read the checkout-local book-conductor instructions and its bounded
outside-ask reference. Do not rely on prior chat or the installed plugin cache
for mutable state.

Execute the dashboard's next permitted packet, G-A2b-III, only. Claim the write
lock, do the work, close the packet, and stop. Do not start P2-SPINE-III or any
later packet, and do not edit chapter prose.

Before the first substantive edit, acknowledge every applicable incoming handoff
and say so explicitly; consume each with a concrete disposition and evidence
before closeout. Read the G-A2b-III packet contract, outside ask
OA-G-A2B-III-SPINE, governed item R04-SPINE-III, the accepted P2-CLAIMS,
P2-ASSESS and P2-IDENTITY registries, the ratified preface and Part I and II
spines, and the recorded author intent in
notes/reports/author-pre-dispositions-2026-08-04.md in full.

Draft the complete Part III spine for Chapters 7 to 9 to the recorded author
intent, then close the gate against that drafted source state with a dated
disposition, named owner, alternatives, authority boundary, and blocked
dependencies. Keep probability, then sampling, then estimation; preserve Chapter
8 as the book's pedagogical hinge; and organise the part around what
generalisation can and cannot reach. This is where Chapter 3's planted poll and
margin-of-error debts are paid off: H-P0-REGISTER-008 targets WC-C08, WC-C09 and
WD-C17, so state the debt in the spine and do not consume the handoff. If the
draft departs from the recorded intent in any respect, stop and present the exact
difference for an explicit decision.

Update the register, handoff ledger, and dashboard together at closeout, then
run scripts/check-review-workflow.R through the project launcher and prove both
required negative fixtures still fail.
```
