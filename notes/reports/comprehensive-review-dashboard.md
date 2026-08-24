---
workflow_schema_version: 1
branch: revision/comprehensive-review
baseline_commit: c163bda524b7081ec6a41d5ab75370f1700b1748
control_implementation_commit: b3463c7b6f7dc7e03a76f74f3a297e2e158e4c6e
active_write_packet: null
last_completed_packet: P5-CLOSURE-11
next_permitted_packet: P5-CLOSURE-12
atomic_children: 371
packet_count: 189
source_coverage_sections: 18
unmapped_actionable: 0
forward_handoffs: 105
last_updated: "2026-08-24"
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
| Gate A2b-III | Accepted as drafted: Part III contract preserving Chapter 8 as the hinge, three chapter spines, and an unchanged definition load; owner Luka Sikic; 2026-08-04 |
| Gate A2b-IV | Accepted as drafted: Part IV contract leading with magnitude and error consequences, three chapter spines, and a bounded two-block Chapter 12 definition increase; owner Luka Sikic; 2026-08-04 |
| Gate A2b-V | Accepted as drafted: Part V contract preserving Chapter 16 as the synthesis payoff, five chapter spines, Chapter 13 ratified as a prerequisite of Chapter 17, and a bounded two-block Chapter 17 definition increase; owner Luka Sikic; 2026-08-05 |
| Gate A2b-FINALE | Accepted **as amended**: finale contract, one whole-book-cumulative Chapter 18 spine with all seventeen numbered chapters as prerequisites, a bounded one-block definition increase, and a bounded new-method permission under three exact limits that amends the register's no-new-method default; owner Luka Sikic; 2026-08-05 |
| Gate A2c | Accepted as recommended: canonical terminology register and reviewer route; 166 ratified spine forms confirmed, 15 load-bearing forms fixed, the R36 new-term cluster settled, four meaning collisions and three deliberate departures ruled, ten live divergences anchored; terminology review is the author's own; owner Luka Sikic; 2026-08-05 |
| Gate A4-03 | Accepted as recommended against C02 closeout commit `91a92347d93073516f6b77c3652c1f2baa5c9bee`: one portal-mediated DIP 2024 turnout audit, governed offline fallback, Tier F outline and exclusions; owner Luka Sikic; 2026-08-06 |
| Gate A4-12 | Accepted as recommended against C11 closeout commit `afd7f474700bcb2a1d63e7ea63543dc7f27dc1d5`: portal-mediated 2016 Registered Replication Report lifecycle artifact, exact P3 verification contract, Chapter 12 outline and exclusions; owner Luka Sikic; 2026-08-13 |
| Gate A4-16 | Accepted as recommended against C15 closeout commit `a9697b1808765038e1d4a176223023e363ad3c3a`: Kleppang et al. 2021 PLOS ONE Table 3 plus its first results paragraph, semantic Croatian adaptation under CC BY 4.0, bounded no-refit reading task and immediate binary-outcome reading bridge without logistic fitting or derivation; owner Luka Sikic; 2026-08-18 |
| Gate A4-17 | Accepted as recommended against C16 closeout commit `26197f84889f1b1caffc25e4bbc171631328adb4`: one bounded parliamentary-text human-review decision, grouped no-leakage split rule, three linked text layers, retained fairness widget, fixed G-A2c vocabulary, full outline and exclusions; owner Luka Sikic; 2026-08-18 |
| Gate A3-TEXT | Accepted as recommended against G-A4-17 closeout commit `7298a62a1c030f80c3d65443e8d311c76e1b1205`: exact Croatian ParlaMint-HR 5.0/ParlaSent 1.0 selection, fail-closed test-schema and unique-link boundary, asymmetric label path, grouped no-leakage split, three views and separate CC BY 4.0 versus CC BY-SA 4.0 file-level regime; owner Luka Sikic; 2026-08-18 |
| P3-TEXT | Accepted from source state `e948cf2aaae2f24fb600d44898d3fcdbc1e99e2e` under `A-P3-TEXT-ROUTE-2026-08-18`: one ParlaSent-only CC BY-SA 4.0 sentence table, 2,698 rows, all 1,336 Croatian test rows retained, 25 overlapping training rows removed, grouped SHA-256 split, output SHA-256 `0f5b4221b583c54fa6996efb33e07541896a83219541029f4c677b56fae5f0ef`; joined 1,297/24/15 failure retained as history; ParlaMint remains unpromoted |
| P3-VERIFY | Accepted against clean P3-TEXT closeout `2ef8973`; exactly P3-VERIFY-A, P3-VERIFY-B, P3-VERIFY-C, P3-VERIFY-D and P3-TEXT independently rerun; all positive and negative lanes pass; legacy C07-C12 SHA-label convention recorded in `H-P3-VERIFY-001` without obscuring exact matching Git blobs |
| WD-C17 | Accepted from clean P3-VERIFY closeout `11b2b75` on source SHA-256 `7e8ff74127f77519434b50afbce50c8354bf019b6a7a2f46684a05c2ecc37e6f`; all eight incoming handoffs consumed, 20 governed items materially pass pending C17, all deterministic checks and HTML/PDF/DOCX pass, and six final critics report zero findings |
| C17 | Accepted on the exact dated author reply for WD-C17 closeout `bff7106e156a49b51fc55ca4b11c9cd2fc6645f8`; only Chapter 17 and the 20 named C17 items advanced, with zero panel findings and no author-reading or final-stage claim |
| WD-PART | Accepted evidence-only from clean C17 closeout; Chapters 13–17 retained their exact blobs, five part items advanced, and `R27-C17-18-transition` remained ratified for the Chapter 18 receiving side and C18 author gate |
| WE-C18 | Accepted from clean WD-PART closeout on source SHA-256 `5aa91d8b4b39ed93004f0b009441cc2fb32f97a551762e51365f8171b20beb88`; all thirteen governed items materially pass pending C18, both sides of `R27-C17-18-transition` are verified, all deterministic checks and HTML/PDF/DOCX pass, and six final critics report zero fatal and zero major findings |
| C18 | Accepted on the exact dated author reply for WE-C18 closeout `be70fef341c46103b7252c3dd6b5c76c9545072e`; only Chapter 18, thirteen WE-C18 items and `R27-C17-18-transition` advanced, with all panel findings dispositioned and no author-reading or final-stage claim |
| P5-CLOSURE-00 | Accepted on assessment state `6d59ea4d13df6fa4df8f553b63083003bf7aa5a3cdd8b9c3f8b51bc4443ec1df`; five schema-valid unit 00 records cover the planted error and all four Zadaci tiers, independent numerical, profile and export checks pass, no route was assembled, and `H-P5-CLOSURE-00-001` binds the implementation rules for units 01–18 and P5-ROUTES |
| P5-CLOSURE-01 | Accepted on unit-record state `468d2505d0f233c48d83d9e08548a9d5fdd59b487e89d9485a02ae67660b2886`; five schema-valid unit 01 records and anchors pass independent numerical, print, profile and export checks, `H-P5-CLOSURE-00-001` is consumed, no route or stage change occurred and no new outgoing handoff is required |
| P5-CLOSURE-02 | Accepted on unit-record state `b6c2e6b25ca31aafbf340ad0f4115c16f02aeaa19f6c7d00ae8b661112681e49`; five schema-valid unit 02 records and anchors pass independent numerical, print, profile and export checks, `H-P5-CLOSURE-00-001` is consumed, no route or stage change occurred and no new outgoing handoff is required |
| P5-CLOSURE-03 | Accepted on unit-record state `9e4676e4d173f7a5e9df1fac73d8ec45126ddbb12cf52e70fdfd245512f35ecf`; five schema-valid unit 03 records and anchors pass independent numerical, planted-error, print, profile and export checks, `H-P5-CLOSURE-00-001` is consumed, no route or stage change occurred and no new outgoing handoff is required |
| P5-CLOSURE-04 | Accepted on unit-record state `ce1c787842dbac834e367e8339b4c0a56d3d1769321a0ec6d94c6a64d6843b7`; five schema-valid unit 04 records and anchors pass independent numerical, planted-error, print, profile and export checks, `H-P5-CLOSURE-00-001` is consumed, no route or stage change occurred and no new outgoing handoff is required |
| P5-CLOSURE-05 | Accepted on unit-record state `5249d06da045995205eecf7f61cc84bb4e8161a727a0e302f6c15c355275e0c3`; five schema-valid unit 05 records and anchors pass independent numerical, planted-error, print, profile and export checks, `H-P5-CLOSURE-00-001` is consumed, no route or stage change occurred and no new outgoing handoff is required |
| P5-CLOSURE-06 | Accepted on unit-record state `7bfef8409b75defaa07ede89f5c2ebc5b05170a9f6c65ff28aa50e884f55741e`; five schema-valid unit 06 records and anchors pass independent numerical, planted-error, print, profile and export checks, `H-P5-CLOSURE-00-001` is consumed, no route or stage change occurred and no new outgoing handoff is required |
| P5-CLOSURE-07 | Accepted on unit-record state `cdedc04f8b1e5764439ef3c8278e80d8a3392e6833badd80ed87ac79d2b3b2d2`; five schema-valid unit 07 records and anchors pass independent numerical, planted-error, print, profile and export checks, `H-P5-CLOSURE-00-001` is consumed, no route or stage change occurred and no new outgoing handoff is required |
| P5-CLOSURE-08 | Accepted on unit-record state `385fcdf5269459337c85970844473d12bd7cecda974ec0680d807c1f48f2c799`; five schema-valid unit 08 records and anchors pass independent numerical, planted-error, print, profile and export checks, `H-P5-CLOSURE-00-001` is consumed, no route or stage change occurred and no new outgoing handoff is required |
| P5-CLOSURE-09 | Accepted on unit-record state `bfe8a07efe336d48b15197e9c56abc83e7a3f1b924205ccd7a303ac1dcff5a7d`; five schema-valid unit 09 records and anchors pass independent numerical, planted-error, print, profile and export checks, `H-P5-CLOSURE-00-001` is consumed, no route or stage change occurred and no new outgoing handoff is required |
| P5-CLOSURE-10 | Accepted on unit-record state `83381cdfa7b8236539d55cc700a9f678f321e47cd12dda435b07f8b46e49abb9`; five schema-valid unit 10 records and anchors pass independent permutation, calibration, planted-error, print, profile and export checks, `H-P5-CLOSURE-00-001` is consumed, no route or stage change occurred and no new outgoing handoff is required |
| P5-CLOSURE-11 | Accepted on unit-record state `8559bfead72e2a2be7c87101957a45828ce2660457144df238ba7f60a7b6f7f1`; five schema-valid unit 11 records and anchors pass independent effect-size, power, planted-error, print, profile and export checks, `H-P5-CLOSURE-00-001` is consumed, no route or stage change occurred and no new outgoing handoff is required |
| Gate A3-DIGIKAT | Accepted as recommended with a latest-possible-snapshot directive: the three-file `digikat_mediji` aggregate, CC BY 4.0 rights confirmed explicitly, three verified defects bound to `P3-DIGIKAT`, a named substitute for official reconciliation, `digikat_akteri` closed as abandoned, and named-actor tables excluded as a permanent rule; owner Luka Sikic; 2026-08-10 |
| Gate A3-EUROSTAT | Accepted as recommended: six 2025 indicators for all EU-27 and `WB-C06`; official reuse terms, exact attribution/disclaimer text and the third-party-exception test; one author-approved bounded official retrieval outside rendering with query, source response, date, checksums and reconciliation retained; owner Luka Sikic; 2026-08-10 |
| Gate A3-ESS | Accepted as recommended: ESS Round 11 edition 3.0, Croatia-only subset, exact identity/design/teaching variables, `anweight` default, bounded vote question, consumers `WC-C08` and `WD-C13`–`WD-C16`; portal-mediated, optional and unpromoted; synthetic mandatory Chapter 8 weighted table; rights ask remains open and bundling prohibited; owner Luka Sikic; 2026-08-11 |
| WC-C08 prerequisite Route A | Accepted exactly: `G-A3-ESS` and `P3-ESS` moved immediately after C07; `WC-PARTS` replaced by C07 in `G-A3-ESS.requires`; `P3-ESS` added to `WC-C08.requires`; four item prerequisites and both separate ESS decisions retained; owner Luka Sikic; 2026-08-11 |
| Thread amendment C08-C10 | `A-THREAD-C08-C10-2026-08-12` accepted as a new, distinct decision: strict chain `C08 -> WC-C09 -> C09 -> WC-C10 -> C10`; one lock and a separate claim, evidence bundle, handoff disposition, workflow check, closeout and commit per packet; exact author replies remain mandatory for C08, C09 and C10; the older C07-C09 decision and its two live handoff deliveries are not superseded |
| Thread amendment C11-P3C | `A-THREAD-C11-P3-VERIFY-C-2026-08-11` accepted as a new, distinct decision: strict chain `WC-C11 -> C11 -> G-A4-12 -> P3-EVIDENCE12 -> P3-VERIFY-C`; each packet keeps its own lock, evidence, handoff disposition, workflow checks, closeout and commit; C11 still requires the exact author reply; both earlier thread chains have ended |
| Thread amendment C12-WD-C13 | `A-THREAD-C12-WD-C13-2026-08-13` accepted as a new, distinct decision: strict chain `WC-C12 -> C12 -> WC-PARTS -> P3-VERIFY-D -> WD-C13`; every packet remains separate; C12 requires the exact author reply and WC-PARTS must stop for the blast-radius choice before any prose edit; all earlier thread chains have ended |
| Thread amendment WC-PARTS-WD-C14 | `A-THREAD-WC-PARTS-WD-C14-2026-08-17` accepted as a new, distinct decision: strict chain now runs `WC-PARTS -> C07-C12-REACCEPT -> P3-VERIFY-D -> WD-C13 -> C13 -> WD-C14`; every packet remains separate; option B and the exact batched gate/handoff are approved, while C07-C12-REACCEPT and C13 retain their exact author-reply stops; all earlier thread chains have ended |
| Thread amendment WD-C14/C14 preparation | `A-THREAD-WD-C14-C14-PREP-2026-08-13` accepted as a new, distinct decision and recorded on 17 August: execute and commit `WD-C14`, then claim `C14` only to assemble the complete acceptance package and stop for the exact reply `C14 accepted for <commit> on <date>`; do not close C14 or start WD-C15; all earlier thread chains have ended |
| Thread amendment WD-C15–G-A4-16 | `A-THREAD-WD-C15-G-A4-16-2026-08-17` is the eighth, new and distinct thread decision: strict chain `WD-C15 -> C15 -> G-A4-16`; every packet remains separate; C15 keeps the exact author-reply stop and G-A4-16 prepares the artifact, rights and binary-outcome-bridge brief without retrieval, promotion or prose; all seven earlier thread chains have ended |
| Thread amendment C15-G-A4-17 | `A-THREAD-C15-G-A4-17-2026-08-17` is the ninth, new and distinct thread decision: strict chain `C15 -> G-A4-16 -> WD-C16 -> C16 -> G-A4-17`; every packet remains separate and committed before the next claim; C15 and C16 retain exact acceptance replies, both decision gates stop for the author, and only WD-C16 may finish unattended; all eight earlier thread chains have ended |
| Thread amendment G-A3-TEXT-C17 | `A-THREAD-G-A3-TEXT-C17-2026-08-17` is the tenth, new and distinct thread decision: strict chain `G-A3-TEXT -> P3-TEXT -> P3-VERIFY -> WD-C17 -> C17`; every packet remains separate and committed before the next claim; G-A3-TEXT and C17 retain exact author-reply stops; all nine earlier thread chains have ended |
| Thread amendment WD-PART-P5-CLOSURE-01 | `A-THREAD-WD-PART-P5-CLOSURE-01-2026-08-19` is the eleventh, new and distinct thread decision: strict chain `WD-PART -> WE-C18 -> C18 -> P5-CLOSURE-00 -> P5-CLOSURE-01`, exactly catalogue sequences 131–135; every packet remains separate and committed before the next claim; C18 retains the exact author-reply stop; WD-PART prefers an evidence-only closeout and WE-C18 is the only other unattended write packet; all ten earlier thread chains have ended |
| Branch | `revision/comprehensive-review` |
| Baseline | `c163bda524b7081ec6a41d5ab75370f1700b1748` |
| Control implementation | `b3463c7b6f7dc7e03a76f74f3a297e2e158e4c6e` |
| Active write packet | None; the write lock is free |
| Last completed packet | `P5-CLOSURE-11`; exactly `R15-CLOSURE-11` advanced, five unit 11 solution records and five source anchors were accepted, and route assembly remained deferred |
| Next permitted packet | `P5-CLOSURE-12`; not claimed |
| Review parents | 31 ratified; 5 accepted |
| Atomic child inventory | Complete: 371 stable children; 291 accepted, 5 deferred with reason and 75 ratified pending their later gates; zero in progress and zero unmapped |
| Exact packet catalogue | 189 packets: 138 accepted, 50 ratified and 1 descoped by author amendment, with stable IDs, typed contracts, unique sequence, and just-in-time dependencies |
| Review source coverage | 18 exact section manifests; their fingerprint union equals all 371 children; zero uncovered actionable findings |
| Chapter stages | 1 `draft`; `00-predgovor`, `01-zasto-statistika`, `02-mjerenje-i-dizajn`, `03-kako-brojke-zavode`, `04-sazimanje-podataka`, `05-vizualizacija`, `07-vjerojatnost`, `08-uzorkovanje`, `09-procjena`, `10-logika-testiranja`, `11-velicina-ucinka-i-snaga`, `12-kriza-i-obnova`, `13-kategoricki-podaci`, `14-dvije-grupe`, `15-vise-grupa`, `16-regresija`, `17-doba-algoritama` and `18-vase-prvo-istrazivanje` at `coauthor_review`; only `06-povezanost` remains deliberately `draft` under its separate WB-PART handoff |
| Chapter spines | **All 19 ratified**: `00-predgovor` at `G-A2b-PREFACE`; Chapters 1–3 at `G-A2b-I`; Chapters 4–6 at `G-A2b-II`; Chapters 7–9 at `G-A2b-III`; Chapters 10–12 at `G-A2b-IV`; Chapters 13–17 at `G-A2b-V`; `18-vase-prvo-istrazivanje` at `G-A2b-FINALE`. No spine remains unratified |
| Open outside asks | 20 of the 87 canonical asks remain `drafted_unsent`; 61 are `done`; 6 are `withdrawn_with_reason`. `OA-C18-ACCEPTANCE` is done on the exact dated reply; `OA-C17-ACCEPTANCE` and both G-A3-TEXT asks remain done; 0 external messages sent |
| Invalidated or reopened work | `P1A-C02` and `P1A-METHODS` were revalidated evidence-only and remain accepted. WB-PART materially changed the accepted C06 source, so only `06-povezanost` returned to `draft`; `H-WB-PART-001` requires a fresh final-state C06 panel in `P6-PANELS` |
| WC-C08 prerequisite resolution | Route A is satisfied: `G-A3-ESS` and `P3-ESS` are accepted at sequences 98 and 99, `WC-C08` is next at sequence 100 and requires both C07/P1A-C08 plus accepted P3-ESS. `H-P3-ESS-001` now carries the exact synthetic-versus-optional-ESS boundary; `OA-G-A3-ESS-RIGHTS` remains open under D08 |
| Failed gates | None in `P1-VERIFY`; all twelve prerequisites pass independently. The pre-existing `_quarto.yml` checksum mismatch remains separately recorded in `H-P1C-EXPORT-002` for `P7-FREEZE` and `P8-META` |
| Phase 2 exit condition | **4 of 5 clauses met.** `R04 is closed` is **not** met and is structurally unmeetable in Phase 2: four of its 21 required children are owned by `WC-C11` (Phase 4), `P5-ROUTES` (Phase 5) and `WE-C18` (Phase 4). Recorded as a plan-versus-register conflict in `H-P2-VERIFY-001`; not forced, not redefined |

No chapter prose was changed by `P0-OUTSIDE`.

## G-A3-ESS claim and bounded decision

- The packet was claimed from clean commit
  `10a4e9803e7738f7592ebfea4a1aca0c7692ccbe` only after the workflow
  validator confirmed no active packet, accepted C07, `G-A3-ESS` alone at
  sequence 98 and the exact Route A dependency graph.
- `H-P1B-DATA-LIC-003` and `H-WC-C07-THREAD-SEQUENCE-001` are consumed at
  `before_start`. `H-P3-CATALOG-001` is acknowledged at `before_close`. Their
  combined boundary preserves `portal-mediated`, `promoted: false`, empty
  `files`, one write lock, no microdata retrieval and no inferred
  redistribution authority.
- The bounded evidence and recommendation are recorded in
  `notes/reports/g-a3-ess-selection-decision-2026-08-11.md`. They pin Round 11
  edition 3.0 and present one exact Croatia-only variable/weight recipe,
  teaching question, consumer list and offline-table solution for author
  decision. The gate does not treat that recommendation as the author's answer.
- The recommended consumer list adds `WC-C08` to `WD-C13`, `WD-C14`,
  `WD-C15` and `WD-C16`. The ESS empirical replication remains optional and
  portal-mediated. Chapter 8's mandatory weighted table and offline task are
  proposed to use a separately labelled synthetic finite-population table with
  known inclusion probabilities; neither local generated dataset is falsely
  described as carrying survey weights.
- `OA-G-A3-ESS-SELECTION` remains `drafted_unsent` and ready for the exact
  author decision. `OA-G-A3-ESS-RIGHTS` remains a separate, open, unsent
  rights-owner inquiry. Bundling is prohibited unless that owner supplies
  written permission tied to the exact files.
- The author supplied the exact selection/role reply on 2026-08-11.
  `OA-G-A3-ESS-SELECTION` is done; `OA-G-A3-ESS-RIGHTS` stays separate and
  open, and bundling stays prohibited. `R03-ESS-permission-gate` is accepted.
- `H-P3-CATALOG-001` is consumed with the concrete portal-route disposition.
  `packet_reviews.G-A3-ESS` records every future effect and creates no new
  handoff because the accepted decision, existing catalogue and thread
  handoffs already own them.
- `G-A3-ESS` closes without changing any chapter, data file, catalogue entry,
  bibliography, shared Bookwright registry, render or generated artifact and
  without retrieving ESS data. `P3-ESS` is next but was not claimed inside
  this gate. Push, merge, tag, archive, deployment and publication remain
  unauthorised.

## P3-ESS closeout

- `H-WC-C07-THREAD-SEQUENCE-001` was consumed for `P3-ESS` before claim.
  The packet retained one write lock and did not claim `WC-C08`.
- `data/katalog.yml#ess_r11_hr` now records ESS11 integrated main file edition
  3.0, `cntry == HR`, all 18 approved variables, five exact consumers and
  `anweight` as default. It remains `portal-mediated`, unpromoted, with empty
  `files`, null local checksum and no promotion-log entry.
- `data/ess_r11_hr/PUTOVNICA.md` and `scripts/prepare-ess-r11-hr.R` provide the
  exact reader-owned route, source-exposed schema, weight roles, official
  missing-metadata reconciliation and reader-side SHA-256 instructions. The R
  recipe has no network operation and refuses repository-local input/output.
- No ESS bytes, empirical denominator, weighted percentage or local checksum
  was retrieved or invented. `OA-G-A3-ESS-RIGHTS` remains open and unsent;
  bundling remains prohibited.
- `scripts/check-ess-portal.py` passes the exact 18-variable/five-consumer
  contract and proves zero local data files; all nine route-specific negative
  fixtures fail closed. The catalogue, data-integrity and workflow checks pass.
- `R08-ESS-route` is accepted. The generic local-file test is explicitly
  `not_applicable_by_author_amendment`; the replacement portal test passes and
  does not masquerade as a local snapshot check.
- `H-P3-ESS-001` routes the complete boundary to `WC-C08` and `WD-C13`–`WD-C16`.
  Chapter 8's mandatory weighted table and offline task must use the separately
  labelled synthetic finite population; every empirical ESS route remains
  optional, and mandatory later work keeps licensed local alternatives.
- No chapter, appendix, bibliography, shared Bookwright registry, concept,
  widget, render, `docs/`, `_freeze/` or generated artifact changed. `WC-C08`
  is next but remains unclaimed; push, merge, tag, archive, deployment and
  publication remain unauthorised.

## WC-C07 claim

- The clean claim state is commit
  `9a4d18198b998037a4e00b28c4f52d1be7dc3b3d` on
  `revision/comprehensive-review`. `WB-PART`, `P2-SPINE-III` and `P1A-C07`
  are accepted, no packet was active, and `WC-C07` was the sole
  `next_permitted_packet` before claim.
- The complete handoff ledger contains 91 handoffs and no delivery targeting
  `WC-C07`. There is therefore no incoming delivery to acknowledge or consume,
  and nothing targeting another packet may be touched. In particular,
  `H-WB-PART-001` remains pending for `P6-PANELS` and Chapter 6 remains at
  `draft` exactly as intended.
- The governed items are `R10-C07-degree-belief`,
  `R29-C07-retrieval-load` and `R35-REACHBACK-07`. Each remains `ratified`
  until the separate `C07` author gate. The accepted `P1A-C07` CLT repair is a
  binding baseline, not a fourth item to reopen or weaken.
- The packet owns only Chapter 7, any same-packet concept-graph or widget-source
  reconciliation genuinely required by that chapter, its dated packet and six
  critic reports, the synthesis, and the three workflow-control views. It does
  not edit Chapter 8, advance the chapter ledger, claim author acceptance, or
  start `C07`.
- The vertical slice will preserve simulation before formalism, distinguish
  personal confidence, model probability and repeated-frequency evidence,
  reduce simultaneous novelty through a real midpoint retrieval pause, and add
  one two-chapter reach-back task without assessed code production. The final
  material hash receives all six independent read-only critics and targeted
  HTML, approved-wrapper PDF and wrapper-built DOCX verification.
- `scripts/check-review-workflow.R` passed immediately before claim with no
  active packet and `WC-C07` uniquely next. It must pass again in this claimed
  state before the first substantive edit. Push, merge, tag, archive,
  deployment and publication remain unauthorised.

## WC-C07 closeout — Chapter 7 vertical slice

- `WC-C07` is accepted at Chapter 7 SHA-256
  `900c1c8ed1b0729eb4bb2fd34421277713e4ecae534290161bc21b0d44d617d5`.
  The complete evidence record is `notes/reports/wc-c07-2026-08-11.md`.
- The chapter keeps simulation before formalisation, distinguishes model
  probability, personal confidence and repeated-frequency evidence, separates
  general multiplication from the independence shortcut, and gives
  independence a process/design justification. The CLT bridge distinguishes
  repeated rates from individual observations and preserves the accepted
  `R09-C07-clt-conditions` boundary.
- The one-arm campaign is not called an A/B test. Its analytical probability
  is 0,19416523, the seed-709 simulation and visible receipt both give 0,1931,
  and the prose rejects model confirmation, causal attribution and automatic
  action. The hot-hand example distinguishes the fixed independent null from
  form, shot difficulty, defence and selection.
- The w07 path is feasible in HTML and print. Runtime SVG semantics, labelled
  controls, reset, keyboard use and a live central-90-percent range pass at
  1.280 and 390 px in both themes. The final widget and print fingerprints are
  reconciled without changing distributional goldens.
- `R10-C07-degree-belief`, `R29-C07-retrieval-load` and
  `R35-REACHBACK-07` each materially pass their exact tests, but remain
  `ratified`; Chapter 7 remains `draft` until C07. No author reading or
  acceptance is claimed.
- Full HTML, approved-wrapper PDF and wrapper DOCX renders exited 0. Their
  SHA-256 values are respectively
  `96d125731fff09274a0e3e049158ca621ecc9dd7dba0b5e27acee27e6a22431a`,
  `d513bdb79b1ab75b8675a818ae97f168f3e77fc7601970bc9ee92af54efb8f77`
  and `c118a25adc9754381b48f7e7f30a66c00be2dec982623129bec70419465405d7`.
  All 37 routes pass and generated artifacts were restored.
- Six independent read-only critics confirmed the exact hash. There is no
  fatal or major finding. Their 20 minor and 8 useful records remain visible
  and unmodified in the reports and synthesis rather than being repaired after
  the panel.
- No handoff targeted WC-C07. `H-WB-PART-001` remains pending for
  `P6-PANELS`; Chapter 6 stays intentionally `draft` and was not edited.
  The pre-existing Chapter 7 catalogue-description drift remains owned by
  `H-P3-CATALOG-002` for `P5-C` and is not duplicated.
- `A-THREAD-C07-C09-2026-08-11` records the user's five-packet amendment.
  `H-WC-C07-THREAD-SEQUENCE-001` carries its reply and stop boundaries to C07,
  WC-C08, C08 and WC-C09. The amendment preserves one write lock, separate
  packet commits and every prerequisite, and it ends after WC-C09 before C09.
- `H-WC-C07-WC-C08-PREREQUISITE-001` records a newly verified control
  contradiction: all four governed WC-C08 items require `P3-ESS`, which remains
  `ratified` at sequence 113. C07 may proceed, but WC-C08 must not be claimed
  until a separately authorised resolution is recorded, even if the current
  validator would otherwise name it next.
- C07 is next but has not been claimed or accepted. Push, merge, tag, archive,
  deployment and publication remain unauthorised.

## C07 claim — awaiting author decision

- C07 was claimed only after the clean WC-C07 closeout commit
  `c6c7078b918a3b017b5807d51b68c83ae2d7bc2f`. The commit contains Chapter 7
  at SHA-256
  `900c1c8ed1b0729eb4bb2fd34421277713e4ecae534290161bc21b0d44d617d5`,
  all six final critic reports, the synthesis and the packet report.
- The packet owns only the Chapter 7 ledger entry, the bounded acceptance
  package and the three workflow-control views. It authorises no prose, data,
  bibliography, terminology, concept, widget, figure, render or generated
  artifact change.
- The C07 delivery in `H-WC-C07-THREAD-SEQUENCE-001` is acknowledged but will
  remain unconsumed until a real exact dated reply and closeout. The
  2026-08-05 standing delegation does not substitute for that reply, and no
  author reading is claimed.
- All six final critics confirm the exact hash with zero fatal and zero major
  finding. The acceptance package discloses all 20 minor and 8 useful records
  and the existing two catalogue descriptions already owned by
  `H-P3-CATALOG-002`.
- No disposition has been applied. `07-vjerojatnost` remains `draft`;
  `R10-C07-degree-belief`, `R29-C07-retrieval-load` and
  `R35-REACHBACK-07` remain `ratified`; `R09-C07-clt-conditions` remains
  accepted.
- The exact required reply is `C07 accepted for
  c6c7078b918a3b017b5807d51b68c83ae2d7bc2f on 2026-08-11.` C07 must stop and
  wait for it or for exact blocking revisions tied to the same commit.
- `H-WC-C07-WC-C08-PREREQUISITE-001` remains pending and is not resolved by
  C07 acceptance. WC-C08 must not be claimed without a separately authorised
  resolution of its four `P3-ESS` item prerequisites.
- `scripts/check-review-workflow.R` passed on the clean closeout state before
  claim. It must pass again in this active C07 state. WC-C08 is not started;
  push, merge, tag, archive, deployment and publication remain unauthorised.

## C07 closeout

- The author replied exactly: `C07 accepted for
  c6c7078b918a3b017b5807d51b68c83ae2d7bc2f on 2026-08-11.` Neither the
  standing delegation nor the thread amendment substitutes for that reply, and
  no author reading is claimed.
- The final Chapter 7 source commit is
  `c6c7078b918a3b017b5807d51b68c83ae2d7bc2f`; its Git blob is
  `1848767a389452f75f2d3263dd82d231940d3c53` and its SHA-256 is
  `900c1c8ed1b0729eb4bb2fd34421277713e4ecae534290161bc21b0d44d617d5`.
  The chapter has not changed after that commit.
- All six final critic reports and the synthesis address that exact material
  state. There is no fatal or major finding. The accepted disposition keeps all
  20 minor and 8 useful records visible rather than silently repairing or
  suppressing them.
- Exactly three governed Chapter 7 items advance from `ratified` to `accepted`:
  `R10-C07-degree-belief`, `R29-C07-retrieval-load` and
  `R35-REACHBACK-07`. The earlier `R09-C07-clt-conditions` remains accepted
  and no other atomic item changes status.
- Only `07-vjerojatnost` advances from `draft` to `coauthor_review`; the ledger
  explicitly records that acceptance does not claim the author read the
  chapter and is not a `final` disposition. Chapter 6 remains deliberately
  `draft` and unchanged.
- `OA-C07-ACCEPTANCE` is `done` from the in-thread reply; no external message
  was sent. The C07 delivery in `H-WC-C07-THREAD-SEQUENCE-001` is consumed only
  after that reply.
- The existing catalogue-description debt remains owned by
  `H-P3-CATALOG-002` for `P5-C` and is not duplicated.
  At C07 closeout, `H-WC-C07-WC-C08-PREREQUISITE-001` remained pending: C07
  acceptance neither consumed nor waived the unmet `P3-ESS` prerequisites of
  four WC-C08 items. `OA-WC-C08-P3-ESS-DEPENDENCY` was `drafted_unsent` as its
  bounded author/editor decision channel. The later Route A decision is
  recorded in the next section.
- No chapter prose, data, bibliography, terminology, spine, concept graph,
  widget, figure, render or generated artifact changed in C07. The register
  pointer at that closeout was WC-C08, but that packet was not claimed and
  remained operationally blocked before_start pending a separately authorised
  control resolution.
  Push, merge, tag, archive, deployment and publication remain unauthorised.

## Route A control-order amendment

- The author approved `A-WC-C08-P3-ESS-ROUTE-A-2026-08-11` exactly on
  2026-08-11. The durable decision record is
  `notes/reports/wc-c08-p3-ess-route-a-decision-2026-08-11.md`.
- `G-A3-ESS` and `P3-ESS` move from sequences 112 and 113 to 98 and 99.
  Every formerly intervening packet keeps its relative order: `WC-C08` is now
  sequence 100 and the remaining affected interval ends with `WC-PARTS` at
  sequence 113; `P3-VERIFY-D` remains 114.
- `G-A3-ESS` now requires `C07`, `P0-OUTSIDE` and `P3-CATALOG`; `P3-ESS`
  continues to require `G-A3-ESS`; `WC-C08` now requires `C07`, `P1A-C08` and
  `P3-ESS`. All four WC-C08 item prerequisites remain unchanged.
- `OA-WC-C08-P3-ESS-DEPENDENCY` is `done` from the exact in-thread reply and no
  external message was sent. `H-WC-C07-WC-C08-PREREQUISITE-001` is consumed
  only after the exact graph repair was applied; no prerequisite was waived.
- `H-WC-C07-THREAD-SEQUENCE-001` now carries the amended chain through
  `G-A3-ESS` and `P3-ESS`. Their deliveries remain pending at `before_start`.
- `OA-G-A3-ESS-SELECTION` and `OA-G-A3-ESS-RIGHTS` remain separate. Route A
  selects no ESS edition, variable, weight or consumer and grants no
  redistribution right. D08's portal-mediated boundary remains binding.
- There is no active write packet; `C07` remains last completed and
  `G-A3-ESS` is the next permitted pointer. It was not claimed, and no chapter,
  data, bibliography, shared Bookwright registry, render or generated artifact
  was changed.
  Its two `before_start` deliveries (`H-P1B-DATA-LIC-003` and
  `H-WC-C07-THREAD-SEQUENCE-001`) remain pending, as does the
  `before_close` delivery `H-P3-CATALOG-001`.
  Push, merge, tag, archive, deployment and publication remain unauthorised.
- The workflow validator passes with 188 packets and 93 handoffs. All three
  required negative fixtures fail closed with exit 1. A separate sequence
  audit proves 188 unique values, all sixteen intended moves and preserved
  relative order for every other packet; the ask inventory reconciles to
  40 `done`, 38 `drafted_unsent` and 6 `withdrawn_with_reason`.

## WB-C04 claim

- The clean source state is commit
  `7cd017a9b60e736dbaed8f507088674bb50ffdf3` on
  `revision/comprehensive-review`; `P3-VERIFY-B` and `P2-SPINE-II` are
  accepted, and `WB-C04` was the sole next permitted packet before claim.
- The packet owns only Chapter 4, its same-packet concept reconciliation,
  WB-C04 evidence reports and the three workflow-control views. It does not
  open `C04`, advance the chapter ledger, claim an author reading, or start
  `WB-C05`.
- `H-G-A3-DIGIKAT-002` was consumed before claim. Its four boundaries are now
  explicit: no trend claim across 2024; no comparison across June 2024 without
  the method break; 551712 is the denominator for any source-file share; and
  measured and unmeasured interaction or reach values are never compared.
- `H-P2-SPINE-II-001`, `H-P2-TERMS-002` and `H-P3-EXISTING-002` were
  acknowledged before the first substantive edit. Closeout requires exactly
  four Chapter 4 definition blocks with same-packet ledger/graph
  reconciliation, and a print-completable aggregate-row task derived from the
  governed aggregate file without altered values.
- The vertical slice will be reviewed against the ratified `G-A2b-II` spine
  with deterministic style, structure and figure preflight plus six independent
  read-only critics. A fatal or unresolved major methods/evidence finding stops
  the packet. Push, merge, tag, archive, deployment and publication remain
  unauthorised.

## WB-C04 closeout — Chapter 4 vertical slice

- `WB-C04` is accepted in final source commit
  `2a6ac10596a578e593e652204e06c30b6b3f1ed8`, on source SHA-256
  `7053754fad4753e3b2252463b3e8095fb43122efdeb8460bf034589d028b7c19`.
  The complete evidence record is `notes/reports/wb-c04-2026-08-10.md`.
- `H-G-A3-DIGIKAT-002` was consumed before claim. The three `before_close`
  deliveries `H-P2-SPINE-II-001`, `H-P2-TERMS-002` and
  `H-P3-EXISTING-002` are now consumed with concrete source, registry and check
  evidence.
- The visible pipeline distinguishes all three DigiKat units, requires the
  full `godina + platforma` join key, separates structural unmeasurement from
  measured zero, fixes the 2025 represented set and names 551.712 as every
  source-file share denominator. It makes no 2024 trend or forbidden
  interaction/reach comparison.
- The correct join preserves 438 rows, 438 monthly keys and 710.307 posts. The
  deliberately wrong join produces 3.571 rows, still only 438 monthly keys and
  5.959.081 posts. Assertions make both paths fail closed.
- The domain summary is locked to 3.604 domains, 551.712 posts, mean 153,0832,
  median 4 and top-ten total 148.748 or 26,96 %. The actual HTML output was
  inspected after a sequential-`summarise()` masking defect was corrected.
- Chapter 4 now has exactly four definition blocks. The checkout-local concept
  ledger and terminology count agree at 47 live definitions, and the regenerated
  graph has 47 nodes and 497 edges with zero ledger debt and a fresh graph.
- The exact widget presets work in HTML and print. The aggregate-row task reads
  `data/anketa-mreze-agregat.csv`, supplies the print arithmetic and asks the
  reader to reproduce one row from `data/anketa-mreze.csv`; no governed value,
  snapshot or checksum changed.
- Final HTML, PDF and wrapper-built DOCX renders exited 0 at the final material
  hash. Their SHA-256 values are respectively `3bad6217cb25df3b6d7b7fef12f9c1e08610fcf892c649c39bd005a584edea1d`,
  `b19d5b0b6d94803904aafbf04711c9bead918073da9528c0bed11917c7f3db31`
  and `9923070a490b734e520671bc6f344bce24ca99a84e17381728eafd5322393222`.
  Generated `docs/`, `_freeze/`, AI exports and Word output were restored.
- Six independent read-only critics confirmed the final hash. Methods,
  skepticism, pedagogy, evidence, style and structure each score 5/5 with zero
  fatal, major or minor finding. The durable synthesis is
  `notes/reports/wb-c04-six-critic-synthesis-2026-08-10.md`.
- `H-WB-C04-001` carries the only new future-relevant effect: the stale
  promotion statement in `data/README.md` must be reconciled by `P5-C` from the
  canonical catalogue.
- Chapter 4 remains `draft`. Its six governed content items remain `ratified`
  until the author-only `C04` decision. `C04` is next but was not opened, no
  author reading or acceptance was claimed, and `WB-C05` was not started.
  Push, merge, tag, archive and deployment remain unauthorised.

## C04 package preparation record

- C04 was claimed only as an author-acceptance gate against WB-C04 commit
  `2a6ac10596a578e593e652204e06c30b6b3f1ed8`. The Chapter 4 Git blob is
  `02a9c2dd88d7ffdc6e598c75ac77e9ae7801a081`, and the working-file SHA-256 is
  `7053754fad4753e3b2252463b3e8095fb43122efdeb8460bf034589d028b7c19`.
- `notes/reports/c04-acceptance-package-2026-08-10.md` cited the final commit,
  all six reports, the synthesis, the WB-C04 evidence record, the only open
  future documentation handoff and the proposed ledger disposition.
  `OA-C04-ACCEPTANCE` was ready for author decision; no external message was
  sent.
- Every critic addressed the same final material hash and scored it 5/5, with
  zero fatal, major or minor finding. `H-WB-C04-001` remains assigned to
  `P5-C`; the `fig-anscombe` introduction debt remains assigned to `WB-C05`.
  Neither is consumed or hidden by C04.
- The recommended disposition was to accept the six governed Chapter 4 items
  and advance only `04-sazimanje-podataka` from `draft` to
  `coauthor_review`, explicitly without claiming that the author read the
  chapter and without calling it `final`.
- Before the author decision, no proposed disposition had been applied. The
  chapter ledger was unchanged, all six items remained `ratified`, C04 was
  `in_progress`, and WB-C05 was blocked. No chapter prose, data, citation,
  concept, widget or render changed while assembling the package.
- No handoff targets C04. At that point, the only action required was the named
  author/editor's exact accept-or-revise reply. The 2026-08-05 standing
  delegation does not substitute for the reply explicitly required by this
  gate. Push, merge, tag, archive and deployment remain unauthorised.

## C04 closeout

- The author replied exactly: `C04 accepted for
  2a6ac10596a578e593e652204e06c30b6b3f1ed8 on 2026-08-10.` The real reply,
  not the 2026-08-05 standing delegation, supplies the author-acceptance
  evidence; no author reading is claimed.
- The final Chapter 4 source commit is
  `2a6ac10596a578e593e652204e06c30b6b3f1ed8`; its Git blob is
  `02a9c2dd88d7ffdc6e598c75ac77e9ae7801a081` and its SHA-256 is
  `7053754fad4753e3b2252463b3e8095fb43122efdeb8460bf034589d028b7c19`.
  The chapter has not changed after that commit.
- All six final critic reports and the synthesis address that exact material
  state. Every perspective scores 5/5, with zero fatal, major or minor finding.
  `notes/reports/c04-acceptance-package-2026-08-10.md` records the final commit,
  reports, synthesis, exact author reply and applied ledger disposition.
- Exactly six governed Chapter 4 content items advance from `ratified` to
  `accepted`: `R08-C04-engagement-source`, `R11-C04-raw-to-table`,
  `R11-C04-wrong-join-AI`, `R11-C04-missingness`,
  `R13-C04-denominators` and `R32-C04-static`. No other atomic item changes
  status.
- Only `04-sazimanje-podataka` advances from `draft` to `coauthor_review`; the
  ledger explicitly says that this records acceptance and does not claim that
  the author read the chapter. This is not a `final` disposition.
- `OA-C04-ACCEPTANCE` is `done` from the in-thread reply. No external message
  was sent. `H-WB-C04-001` remains pending for `P5-C`, while the
  `fig-anscombe` introduction debt remains owned by `WB-C05`.
- The thread-only author amendment is durable as
  `A-THREAD-C04-C06-2026-08-10`. It preserves the strict sequence `C04`,
  `WB-C05`, `C05`, `WB-C06`, `C06`, one write lock and a separate checked
  commit per packet. `H-C04-THREAD-SEQUENCE-001` carries its reply and stop
  boundaries to the four remaining packets.
- No chapter prose, data, bibliography, terminology, spine, concept graph,
  widget, render or generated artifact changed in C04. `WB-C05` is next and
  was not started in C04; push, merge, tag, archive and deployment remain
  unauthorised.

## WB-C05 claim

- The clean source state is commit
  `94d48ffbaddee86aa4c52eb150d5267e08d42c55` on
  `revision/comprehensive-review`. C04 is accepted against WB-C04 commit
  `2a6ac10596a578e593e652204e06c30b6b3f1ed8`, Chapter 4 is at
  `coauthor_review`, and WB-C05 was the sole next-permitted packet before the
  claim.
- `H-C04-THREAD-SEQUENCE-001` was consumed before claim. WB-C05 holds the one
  permitted write lock, stops before C05, receives its own evidence and local
  commit, and cannot treat the thread amendment as author acceptance or as
  evidence that the author read Chapter 5.
- `H-G-A3-DIGIKAT-002` was consumed before claim. WB-C05 makes no trend claim
  across 2024, no comparison across the June 2024 method break without naming
  it, no source-file share against a denominator other than 551712, and no
  comparison between structurally unmeasured and measured reach or
  interactions. A monthly display, if introduced, must show the February-May
  2024 gap.
- `H-P1C-INTEGRITY-001` and `H-P3-EXISTING-001` were acknowledged before the
  first substantive edit. Closeout must retire only the exact
  `fig-anscombe` debt, prove the positive and deliberate-failure figure lanes,
  copy or promote no Anscombe data, keep its local-R route optional, and use
  licence-clean `anketa_mreze` for every mandatory task.
- The packet owns only Chapter 5, the `w05` source fingerprint in the canonical
  widget registry, the one integrity-debt record, its dated packet, density,
  six-critic and synthesis reports, and the three workflow control views. The
  widget-registry addition is limited to reconciling the OJS fingerprint after
  the accessibility repair; adapters, tolerances and golden values remain out
  of scope. The packet leaves Chapter 5 at `draft` and all four governed items
  `ratified` until C05.

## WB-C05 closeout — Chapter 5 vertical slice

- `WB-C05` is accepted in final source commit
  `de85c7018b934bf5c6310fd4f1125f0ae65473a0`, at source SHA-256
  `db4203d6caf05a5e5e07ba841a58e3b5be7bb6916eb159be0054196d89bf14df`.
  The complete evidence record is `notes/reports/wb-c05-2026-08-10.md`.
- `H-P1C-INTEGRITY-001` and `H-P3-EXISTING-001` are consumed. The approved
  Croatian paragraph now immediately precedes `fig-anscombe`, the
  `figure_introductions` debt list is empty, and both the positive figure gate
  and deliberate-failure fixture pass. No Anscombe file was copied or
  promoted; every mandatory numerical path uses `anketa_mreze`.
- The six-title micro-corpus reproduces 36 tokens, 28 forms, 22 singletons and
  six repeated forms. It prepares the chapter on algorithms without teaching
  natural-language processing or widening its tiny purposive corpus.
- DigiKat reproduces 3,604 named domains, 551,712 posts, median 4 and maximum
  56,500. The monthly view shows partial January, the February-May gap and the
  June method break, joins only July-December and makes no trend, growth or
  before-after claim.
- The widget has four dynamic descriptions, four `aria-label` states, a live
  status and a print-completable four-row table. Its OJS fingerprint is updated
  to `602c13e3ccd0970e24989b4ae98e2ab1ee80ad704f44329731a0572803d41efa`;
  adapters, tolerances, golden values and the R fingerprint are unchanged.
- Six logical figures have six distinct argumentative roles, documented in
  `notes/reports/wb-c05-figure-density-2026-08-10.md`. The immediate Anscombe
  introduction and all other introductions pass the blocking detector.
- Final HTML, PDF and wrapper-built DOCX renders exited 0. Their SHA-256 values
  are `086d26fa3e35f51a77ad3d57b0a6c355209012b90fdbe4f0780721bc8d083c37`,
  `1c1af5b6467b3f3ae8b0f7a83662b94cf88b4cf12d308622393c55d711f47ac9`
  and `b371d20bd7f955aaeb92ba0ed40177772f076603ae3509c9beaed0582ebc821c`.
  Generated `docs/`, `_freeze/`, AI exports and Word output were restored.
- Six independent read-only critics confirmed the exact final hash. There is
  no fatal or major finding. Two nonblocking skeptical wording notes remain in
  the chapter; one documentation minor outside the chapter is already owned by
  `H-WB-C04-001` and `H-P3-CATALOG-002` for `P5-C`.
- `packet_reviews.WB-C05` declares all future effects recorded and opens no new
  handoff. Chapter 5 remains `draft` and all four governed items remain
  `ratified` pending the separate author-only C05 gate. `C05` is next; no
  author reading or acceptance is claimed. Push, merge, tag, archive and
  deployment remain unauthorised.

## C05 package preparation record

- C05 was claimed only as an author-acceptance gate against WB-C05 commit
  `de85c7018b934bf5c6310fd4f1125f0ae65473a0`. The Chapter 5 Git blob is
  `6c478a6efc6c80b44c2475849024db782d139076`, and the working-file SHA-256 is
  `db4203d6caf05a5e5e07ba841a58e3b5be7bb6916eb159be0054196d89bf14df`.
- `notes/reports/c05-acceptance-package-2026-08-10.md` cited the final commit,
  all six reports, the synthesis, the WB-C05 evidence record, the density
  memorandum, every open minor finding and the proposed ledger disposition.
  `OA-C05-ACCEPTANCE` was ready for author decision; no external message was
  sent.
- Every critic addressed the same final material hash. There is no fatal or
  major finding. Two nonblocking skeptical wording notes remain in Chapter 5;
  one pre-existing documentation minor outside the chapter remains owned by
  `H-WB-C04-001` and `H-P3-CATALOG-002` for `P5-C`.
- The recommended disposition was to accept exactly four governed Chapter 5
  items and advance only `05-vizualizacija` from `draft` to
  `coauthor_review`, explicitly without claiming that the author read the
  chapter and without calling it `final`.
- Before the author decision, no proposed disposition had been applied. The
  chapter ledger was unchanged, all four items remained `ratified`, C05 was
  `in_progress`, and WB-C06 was blocked. No chapter prose, data, bibliography,
  concept, widget, render or generated artifact changed while assembling the
  package.
- `H-C04-THREAD-SEQUENCE-001` was acknowledged for C05 but remained unconsumed
  until the real author reply and gate closeout. The 2026-08-05 standing
  delegation and the thread amendment did not substitute for that reply.

## C05 closeout

- The author replied exactly: `C05 accepted for
  de85c7018b934bf5c6310fd4f1125f0ae65473a0 on 2026-08-10.` The real reply
  supplies the author-acceptance evidence; neither the standing delegation nor
  the thread amendment substitutes for it, and no author reading is claimed.
- The final Chapter 5 source commit is
  `de85c7018b934bf5c6310fd4f1125f0ae65473a0`; its Git blob is
  `6c478a6efc6c80b44c2475849024db782d139076` and its SHA-256 is
  `db4203d6caf05a5e5e07ba841a58e3b5be7bb6916eb159be0054196d89bf14df`.
  The chapter has not changed after that commit.
- All six final critic reports and the synthesis address that exact material
  state. There is no fatal or major finding. The accepted disposition keeps
  two nonblocking Chapter 5 wording notes and one pre-existing documentation
  minor visible rather than silently repairing or suppressing them.
- Exactly four governed Chapter 5 content items advance from `ratified` to
  `accepted`: `R13-C05-frequency-visual`, `R28-C05-introduction`,
  `R28-C05-density` and `R31-C05-Anscombe`. No other atomic item changes
  status.
- Only `05-vizualizacija` advances from `draft` to `coauthor_review`; the
  ledger explicitly says that this records acceptance and does not claim that
  the author read the chapter. This is not a `final` disposition.
- `OA-C05-ACCEPTANCE` is `done` from the in-thread reply. No external message
  was sent. `H-C04-THREAD-SEQUENCE-001` is consumed for C05 and remains pending
  for WB-C06 and C06. `H-WB-C04-001` and `H-P3-CATALOG-002` remain pending for
  `P5-C`.
- No chapter prose, data, bibliography, terminology, spine, concept graph,
  widget, render or generated artifact changed in C05. `WB-C06` is next and
  was not started in C05; push, merge, tag, archive and deployment remain
  unauthorised.

## WB-C06 claim

- The clean claim state is commit
  `c697a977b2adae063349414abe8a12261c2a2097` on
  `revision/comprehensive-review`. C05 is accepted against WB-C05 commit
  `de85c7018b934bf5c6310fd4f1125f0ae65473a0`, Chapter 5 is at
  `coauthor_review`, and WB-C06 was the sole next-permitted packet before the
  claim.
- `H-C04-THREAD-SEQUENCE-001`, `H-G-A3-DIGIKAT-002`,
  `H-G-A3-EUROSTAT-001` and `H-P3-EUROSTAT-001` were consumed before claim.
  The strict thread sequence, DigiKat limits, exact Eurostat selection and
  promoted package evidence now bind the packet. `H-P3-EXISTING-001` was
  acknowledged before the first substantive edit and remains due at closeout.
- Eurostat use is limited to the six ratified 2025 indicators for all EU-27
  countries. The packet must preserve 162 keys, 161 numerical values and the
  explicit Luxembourg early-leaving absence with source flags, and may support
  only country-level comparison, association and a third-variable question.
  No new retrieval, individual, causal, trend, mixed-year or out-of-EU claim is
  authorised.
- The packet may create, copy or promote no `anscombe` file. Its local-R use is
  optional; every mandatory task must use `anketa_mreze` or the governed
  Eurostat table. Any DigiKat use retains the method break, gap, denominator
  and structural-unmeasurement boundaries.
- WB-C06 owns only Chapter 6, the six verified Eurostat bibliography entries
  needed by its aggregate example, any necessary `w06` fingerprint
  reconciliation, the generated concept graph when Chapter 6 changes its
  co-occurrence edges, its dated packet and six-critic reports, and the three
  workflow control views. Chapter 6 remains `draft`; its two WB-C06 items remain
  `ratified` and the four earlier P1A-C06 repairs remain `accepted` until the separate C06
  gate. C06 is not open, no author reading or acceptance is claimed, and push,
  merge, tag, archive and deployment remain unauthorised.

## WB-C06 closeout — Chapter 6 vertical slice

- `WB-C06` is accepted at source SHA-256
  `4b5e538138a6b385e4d970b193d2ea29e3cf71d934e2700fdf37a7e65633efa8`.
  The complete evidence record is `notes/reports/wb-c06-2026-08-10.md`.
- `H-P3-EXISTING-001` is consumed. No `anscombe` file was copied or promoted;
  the local-R route is an optional vignette check, while all mandatory
  calculations and assessed paths use `anketa_mreze` or the governed Eurostat
  extract.
- The Eurostat table preserves 162 unique EU-27/2025 keys, 161 numerical
  values and the one Luxembourg `:`/`u` absence. The exploratory country-level
  pair reproduces Pearson 0,449994 and Spearman 0,508016 without an individual,
  causal, trend, predictive, mixed-year or out-of-EU claim.
- The six-title coded category records its literal rule, purposive set and
  author ownership. Its code/year correlation is -0,046324; expanding the rule
  until every code equals one makes the correlation undefined.
- The final chapter keeps the graph before the coefficient, treats Pearson and
  Spearman agreement or disagreement as clues, qualifies range restriction,
  shows Simpson's reversal without regression lines and gives the AI box
  exactly one error. The Chapter 4 reach-back is a genuine data-integrity task.
- The w06 browser path has four labelled controls, a live 4/4 result, a hidden
  then revealed four-row solution, reset and a print-completable twin. At 390 px
  the widget frame is 320 px and its SVG 286 px, with no runtime error.
- Full HTML, approved-wrapper PDF and wrapper-built DOCX renders exited 0.
  Their SHA-256 values are respectively
  `0a988d6f763e8b493276f9ba4a1bf654160bb3d5070566402fce4921fda23f7b`,
  `445dc17b6dab9c73fb60946ef4e92d93ce1aecc7365a7a1ab10cb040f5605917`
  and `8941493f07a9ebcd9e17d29fd7f52c5be86fabe5a4d9c3b8cd24d614c53e9ac4`.
  Generated `docs/`, `_freeze/`, AI exports, PDF and DOCX were restored.
- Six independent read-only critics confirmed the exact final hash. There is
  no fatal or major finding. Pedagogy and style retain one nonblocking minor
  each; the existing public-catalogue debt remains owned by `P5-C`.
- `H-WB-C06-001` records the shared normal-generator adapter invalidation for
  seven later chapter widgets plus `P6-FIGURES` and `P7-HTML`.
  `H-WB-C06-002` routes the stale unconditional range-restriction concept-ledger
  wording to `P6-CONTINUITY`. `H-WB-C06-003` routes the 12 px mobile overflow of
  a cited Quarto `page-full` figure to `P7-HTML`; it does not invalidate w06.
- Chapter 6 remains `draft`. `R13-C06-coded-association` and
  `R35-REACHBACK-06` remain `ratified`; the four earlier P1A-C06 repairs remain
  `accepted`. `C06` is next but was not opened, no author reading or acceptance
  was claimed, and push, merge, tag, archive and deployment remain
  unauthorised.

## C06 claim

- C06 was claimed only after the author supplied the exact dated reply
  `C06 accepted for 34200ef1d723e88623e1bc9e73a47e6535a3673c on
  2026-08-10.` The cited commit is the clean current `HEAD`, contains the final
  Chapter 6 source and all eight WB-C06 review artifacts, and leaves the source
  SHA-256 at
  `4b5e538138a6b385e4d970b193d2ea29e3cf71d934e2700fdf37a7e65633efa8`.
- The packet owns only the Chapter 6 ledger entry, the bounded acceptance
  package and the three workflow-control views. It authorises no chapter prose,
  data, bibliography, terminology, concept, widget, figure, render or generated
  artifact change.
- `H-C04-THREAD-SEQUENCE-001`, the only incoming C06 delivery, is acknowledged
  after the exact reply and remains unconsumed until closeout. No handoff for
  another packet is touched.
- During claim, Chapter 6 remains `draft`, `R13-C06-coded-association` and
  `R35-REACHBACK-06` remain `ratified`, and the four earlier P1A-C06 repairs
  remain `accepted`. The accepted disposition has not yet been applied, no
  author reading is claimed and `WB-PART` remains blocked.

## C06 closeout

- The author replied exactly: `C06 accepted for
  34200ef1d723e88623e1bc9e73a47e6535a3673c on 2026-08-10.` The decision was
  recorded on 2026-08-11. Neither the standing delegation nor the thread
  amendment substitutes for that reply, and no author reading is claimed.
- The final Chapter 6 source commit is
  `34200ef1d723e88623e1bc9e73a47e6535a3673c`; its Git blob is
  `d5de2b1ff01815a4f86c78186fcc77d9a8c97994` and its SHA-256 is
  `4b5e538138a6b385e4d970b193d2ea29e3cf71d934e2700fdf37a7e65633efa8`.
  The chapter has not changed after that commit.
- All six final critic reports and the synthesis address that exact material
  state. There is no fatal or major finding. The accepted disposition keeps
  one nonblocking pedagogical retrieval note and one nonblocking lexical-style
  note visible rather than silently repairing or suppressing them.
- Exactly two governed Chapter 6 items advance from `ratified` to `accepted`:
  `R13-C06-coded-association` and `R35-REACHBACK-06`. The four earlier
  `R09-C06-*` repairs remain accepted and no other atomic item changes status.
- Only `06-povezanost` advances from `draft` to `coauthor_review`; the ledger
  explicitly says that this records acceptance without claiming that the
  author read the chapter. This is not a `final` disposition.
- `OA-C06-ACCEPTANCE` is `done` from the in-thread reply; no external message
  was sent. `H-C04-THREAD-SEQUENCE-001` is consumed for C06 only after the
  exact reply.
- `H-WB-C06-001`, `H-WB-C06-002` and `H-WB-C06-003` remain pending for their
  named later targets. The pre-existing public-catalogue debt remains owned by
  `H-WB-C04-001` and `H-P3-CATALOG-002`; C06 creates no duplicate handoff.
- No chapter prose, data, bibliography, terminology, spine, concept graph,
  widget, figure, render or generated artifact changed in C06. `WB-PART` is
  next and was not started; push, merge, tag, archive and deployment remain
  unauthorised.

## WB-PART claim

- The packet was claimed from clean commit
  `79d9fe43ee3cd53d1bc6dcce6680d7635e44faa1` only after C06 closed. Chapters
  4–6 remain at `coauthor_review` on their accepted source states; claiming the
  packet does not reopen them or presume that a prose edit is needed.
- The complete handoff ledger has no delivery targeting `WB-PART`. There is no
  incoming handoff to acknowledge or consume, and nothing targeting another
  packet may be touched.
- The packet owns only Chapters 4–6 if a bounded bridge or self-check repair is
  genuinely required, its packet report, independent voice and arc reports,
  continuity synthesis and the three workflow-control views. Shared Bookwright
  registries remain read-only unless a separately evidenced contradiction is
  found and approved.
- The four governed items are `R08-SPINE-04-06`, `R24-PARTII-thesis`,
  `R24-LADDER-PartII` and `R35-SELF-CHECK-II`. Each will be judged separately
  against the accepted Part II sources, ratified spines and thread registry;
  an evidence-only closeout is preferred when the current text already passes.
- `scripts/check-review-workflow.R` passed before claim with no active packet
  and `WB-PART` uniquely next. `WC-C07` remains blocked; push, merge, tag,
  archive and deployment remain unauthorised.

## WB-PART closeout — Part II continuity gate

- `WB-PART` is accepted on final Chapter 6 SHA-256
  `0c10a9b827651228777379826bf64f27bfc585633b0d889af2396f7a28d6ebfd`.
  Chapters 4 and 5 remain unchanged at
  `7053754fad4753e3b2252463b3e8095fb43122efdeb8460bf034589d028b7c19`
  and `db4203d6caf05a5e5e07ba841a58e3b5be7bb6916eb159be0054196d89bf14df`.
- The complete evidence record is `notes/reports/wb-part-2026-08-11.md`.
  Independent final voice and arc reports plus their synthesis confirm the
  exact source hashes with zero fatal and zero major finding. Voice,
  cumulative build and order score 5/5; register evenness and absence of
  redundant repetition score 4/5.
- A separate read-only evidence audit found the initially implicit AI-receipt
  contract, then verified the bounded repair. The final C06 table gives each
  C04–C06 assistant task all seven canonical fields, describes the actual
  visible return, names concrete checks and responsible people, remains
  readable without code and leaks no protected diagnosis or answer.
- Exactly four items advance from `ratified` to `accepted`:
  `R08-SPINE-04-06`, `R24-PARTII-thesis`, `R24-LADDER-PartII` and
  `R35-SELF-CHECK-II`. Each carries source-specific completion evidence.
- The first concept check caught a false `mediju` → `medijan` token match.
  The source now says `formatu`; the canonical graph remains unchanged at 47
  nodes and 502 edges, and `check-concepts.py` reports a fresh graph with zero
  ledger debt.
- Full HTML, approved-wrapper PDF and wrapper DOCX renders exited 0. Their
  SHA-256 values are respectively
  `2dd8ae8da9411f6f4f59b12b7ae3a09183c6b2b3cc0e020eee73a82872a79d96`,
  `b4f773ab59f1cd1774bffe9f47e17139b750bcd245da021b81207daebf362d53`
  and `76dddcac65158426a837331ffcc5d8c1e96684b88b39e2e94f2fb3b5c2ef173d`.
  All 37 HTML routes pass; generated `docs/`, `_freeze/`, PDF, DOCX and AI
  exports were restored.
- Architecture, spine, assessment, identity, terminology, citation, concept,
  manuscript, figure, catalogue, data, DigiKat, Eurostat, widget, parity,
  inventory, token, style and continuity checks pass. The four known C04
  structure-rhythm candidates remain accepted and unmodified; C05 and C06 have
  no structure-lint candidate.
- C06 author acceptance remains historical evidence for commit
  `34200ef1d723e88623e1bc9e73a47e6535a3673c` and its old source hash. Because
  the WB-PART bridge is material and lacks a new full chapter panel and author
  disposition, only `06-povezanost` is conservatively returned from
  `coauthor_review` to `draft`.
- `H-WB-PART-001` records the sole new future-relevant effect and routes the
  required fresh C06 six-critic coverage to the already-ratified
  `P6-PANELS`. The WB-PART voice/arc panel is not substituted for it.
- No handoff targeted WB-PART. The active write lock is closed, `WC-C07` is the
  sole next-permitted packet and was not claimed or started. Push, merge, tag,
  archive and deployment remain unauthorised.

## G-A3-EUROSTAT claim

- `P3-DIGIKAT` is accepted at commit
  `355aecfcb4a4d0dfda33e10438d92aba019f6081`; the worktree was clean,
  `G-A3-EUROSTAT` was the sole next permitted packet, Chapters 1-3 remained
  at `coauthor_review`, and Chapter 4 remained at `draft` before this claim.
- `H-P1B-DATA-LIC-003` was consumed before claim. Its cautious
  `portal-mediated`, `promoted: false`, empty-files boundary remains binding:
  this gate may inspect official terms and product pages read-only, but it
  retrieves no statistical data and promotes nothing.
- `H-P3-CATALOG-001` was acknowledged before the first substantive edit. It
  remains due for a concrete closeout disposition, and no catalogue lane or
  package state may change without the complete package-specific contract.
- The packet owns only its dated decision package and the three control files.
  The selected indicators, common year, countries, rights terms, exceptions,
  consumer and source-route alternatives will be recorded there; no chapter,
  dataset, catalogue entry or shared Bookwright registry is in scope.

## G-A3-EUROSTAT prepared decision and stop

- The existing author pre-disposition was consumed rather than re-asked. The
  smallest defensible selection is six indicators for reference year 2025 and
  all 27 EU Member States: employment age 20-64, AROPE, tertiary attainment
  age 25-34, early leaving age 18-24, internet use age 16-74 and the share age
  65+. Their sole current consumer is `WB-C06`; the future table has 162
  country-indicator keys, each constrained to 2025 or an explicit retained
  official missing value.
- Read-only inspection of the official Eurostat reuse notice and product
  pages resolved both original asks without retrieving statistical data. The
  decision package transcribes the official customised-dataset attribution
  template, fixes the exact modification statement and Commission disclaimer,
  and shows why the selected EU-only, non-trade tables with Eurostat named as
  source do not activate the third-party-content exceptions. Any contrary
  notice on the actual source must still stop `P3-EUROSTAT`.
- The repository has no valid source for building the package. The CroAIcon
  MySQL staging table remains rejected because it repeats rows, and read-only
  portal inspection cannot produce the retained response, checksum and
  reconciliation required by the data-package contract. No existing author
  record permits a bounded retrieval, names a supplied mirror, or amends the
  packet to remain portal-mediated and unpromoted.
- `OA-G-A3-EUROSTAT-SOURCE-ROUTE` is therefore ready for one bounded author
  disposition. The recommended route is one exact official retrieval outside
  rendering, with the query response, access date, checksum and reconciliation
  retained. Until the author decides, `G-A3-EUROSTAT` remains the sole active
  packet, `P3-EUROSTAT` is not started, and the catalogue is unchanged.
- If the author instead keeps the package portal-mediated and unpromoted,
  Chapter 6 rests on the promoted `anketa_mreze` for its computational spine
  and the promoted `digikat_mediji` for empirical transfer. It then has no
  genuine cross-country Eurostat case for comparability and ecological
  interpretation, and that absence must be stated rather than filled with an
  unverified number.

## G-A3-EUROSTAT closeout

- Author and editor Luka Sikic accepted the recommended source route on
  2026-08-10: one bounded retrieval of the exactly defined six-indicator 2025
  EU-27 slice from the official Eurostat source, outside rendering, with the
  query, unmodified response, access date, checksums and reconciliation
  retained. This is a packet-specific exception, not general network authority.
- The selection remains six indicators, one common year, all 27 EU Member
  States and sole consumer `WB-C06`. All 162 country-indicator keys must be
  2025 or an explicit retained official missing value carrying its source
  flags. A mixed-year fallback is forbidden.
- Published reuse terms, exact attribution and disclaimer text, and the
  third-party-content exception test are settled. The actual retrieved source
  must still stop the data packet if it carries a contrary individual notice.
  No rights-holder permission is claimed and none was sought.
- `H-P1B-DATA-LIC-003` was consumed before claim. `H-P3-CATALOG-001` was
  acknowledged before the first substantive edit and consumed at closeout:
  the gate changed no catalogue entry, retrieved no data and promoted zero
  packages. `eurostat_drustvo` remains portal-mediated, unpromoted and without
  files until its data packet satisfies the full contract.
- `H-G-A3-EUROSTAT-001` carries the complete accepted selection, flag,
  rights, source-route and claim boundary to `P3-EUROSTAT`, `P3-VERIFY-B` and
  `WB-C06`. The packet review declares all future effects recorded.
- `P3-EUROSTAT` is the sole next permitted packet. It was not started before
  this gate closed. Push, merge, tag, archive and deployment remain
  unauthorised.

## P3-EUROSTAT claim

- `P3-EUROSTAT` is the sole active write packet. `G-A3-EUROSTAT` is accepted
  at live commit `5c9c14cf13fd7d7903ce62372ccf1c3248e32a21`; no later packet has
  started and the one-lock invariant is intact.
- `H-G-A3-EUROSTAT-001` was consumed before claim and before the first
  substantive edit. The packet is bounded to six ratified indicators, reference
  year 2025, all 27 EU Member States and consumer `WB-C06`; a mixed-year
  substitute, scope widening, individual claim or causal claim is forbidden.
- `H-P3-DZS-003` is acknowledged before the first edit and remains due at
  closeout. Promotion must obey all six inherited external-package rules,
  including a package gate distinct from its decision gate, an own-licence
  snapshot notice, exact named promotion-log reconciliation, composite keys and
  fail-closed missing-code checks.
- The author-approved network action is one bounded six-request batch against
  the official Eurostat API outside rendering. The packet will retain the exact
  request URLs, raw response bytes, retrieval timestamp, checksums and source
  reconciliation; it will not make a reconnaissance data request first.

## P3-EUROSTAT closeout

- **One retrieval, then offline only.** One six-request batch ran against the
  official Eurostat Dissemination API between 12:39:03 and 12:39:10 UTC on
  2026-08-10. All six requests returned HTTP 200, none was retried, and no
  second network request followed. Exact URLs, unmodified responses, dates,
  HTTP metadata, MD5 and SHA-256 are retained under `data/eurostat_drustvo/`.
- **The ratified common-year grid is complete.**
  `data/eurostat-drustvo-2025.csv` contains all 162
  `geo+godina+pokazatelj` keys: 27 EU Member States, six indicators and only
  2025. There are 161 numbers and one explicit source absence: Luxembourg
  early leaving, `vrijednost = :`, API/OBS status `u`, no confidentiality
  flag. Croatia's published 2.1 in the same indicator also carries `u`, so the
  package keeps quality status distinct from missingness.
- **Source and rights survived contact with the actual responses.** Every raw
  response names `ESTAT` and `SOURCE_INSTITUTIONS = Eurostat`; none carries a
  contrary source-specific rights annotation. The adjacent notice supplies six
  datacode attributions with the actual access date plus the exact ratified
  modification and Commission disclaimer sentences. No rights-holder
  permission is claimed.
- **Promotion is fully named.** `eurostat_drustvo` is now `bundled` and
  `promoted: true` by `P3-EUROSTAT`, ratified by the separate
  `G-A3-EUROSTAT` record. The bidirectional promotion log names it; the
  catalogue now reports five promoted packages and 21 validated snapshots.
- **The release lane is offline and fail-closed.** The builder reconstructs 162
  values and statuses from the retained raw bytes with zero tolerance. The main
  R integrity lane invokes it. Both a changed raw byte and a removed `u` flag
  fail for their own reason; the complete negative harness reports 44 cases.
  A final pre-commit audit found and closed the Windows checkout risk:
  `.gitattributes` pins the derived JSON to LF and treats raw responses as
  binary, so `core.autocrlf` cannot change checksummed evidence.
- `H-G-A3-EUROSTAT-001` was consumed before claim and `H-P3-DZS-003` at
  closeout. `H-P3-EUROSTAT-001` carries the actual package, missingness,
  attribution, no-refresh and claim boundaries to `P3-VERIFY-B`, `WB-C06`,
  `P6-DATA` and `P8-META`. No chapter, shared Bookwright registry or generated
  render output changed.
- `P3-VERIFY-B` is the sole next permitted packet. Push, merge, tag, archive,
  deployment and publication remain unauthorised.

## P3-VERIFY-B claim

- `P3-VERIFY-B` is the sole active write packet. Its three prerequisites are
  accepted: `WA-PART`, `P3-DIGIKAT` and `P3-EUROSTAT`; the last is pinned to
  commit `f6d25bb30dce3f5ffe41204e87273bd166c6053b`.
- `H-P3-EUROSTAT-001` was consumed before claim. The two decision-level
  before-close constraints, `H-G-A3-DIGIKAT-002` and
  `H-G-A3-EUROSTAT-001`, were acknowledged before the first review edit and
  remain due at closeout.
- This is a read-only evidence review of both packages. It may write only its
  report and the three workflow control files; it performs no network request,
  refresh, package transformation, data edit, chapter edit or registry edit.

## P3-VERIFY-B closeout

- The three-entry gate matrix passes at source commit
  `f6d25bb30dce3f5ffe41204e87273bd166c6053b`: `WA-PART`,
  `P3-DIGIKAT` and `P3-EUROSTAT` are accepted with complete evidence and no
  active blocker.
- DigiKat was recomputed independently from its three CSVs and then reproduced
  from checkout `278a127f9170c1aca82035a4a8357b8a995f91d8`: 49/438/3.604
  rows, the visible February–May 2024 gap, January at 1.911, four complete
  years, six exact denominators, 17 divergences from +446 to −389, net zero at
  710.307, and the domain-only denominator 551.712 all agree.
- Eurostat was audited independently from its plan, manifest, six raw responses,
  CSV and notice: six official requests, zero retries, six matching raw hashes,
  162 unique 2025 keys, 161 numbers, one `LU/:/u` row, expected status counts,
  ESTAT/Eurostat source identity, no contrary rights annotation and six exact
  component attributions all agree.
- The first verification attempt is disclosed and excluded: it used three
  shorthand DigiKat labels absent from the file and omitted the builder's
  required checkout argument. The corrected audit named the literal labels and
  checkout, reran from the beginning with fail-fast handling and passed.
- Portfeljni checks remain green: `KATALOG_OK`, `DATA_INTEGRITY_OK`, 44 expected
  data failures and seven expected general-integrity failures. Commit scope
  changes no chapter, appendix, `docs/`, `_freeze/` or shared Bookwright
  registry path.
- `H-P3-EUROSTAT-001` was consumed before claim;
  `H-G-A3-DIGIKAT-002` and `H-G-A3-EUROSTAT-001` were consumed at closeout.
  No new future-relevant effect was found, so no duplicate handoff was created.
- `P3-VERIFY-C`, `P3-ESS` and `P3-TEXT` remain later ratified work and were not
  misreported as completed or hidden as Wave B blockers. `WB-C04` is now the
  sole next permitted packet. No network or external system was contacted;
  push, merge, tag, archive, deployment and publication remain unauthorised.

## P3-DIGIKAT claim

- The author amendment dated 2026-08-10 permits this thread to execute up to
  five named packets in strict sequence, while preserving the one-lock rule,
  per-packet claim, evidence, handoff, closeout, workflow-check and commit
  boundaries. The amendment will be recorded permanently in this packet's
  closeout evidence; it does not authorise any packet outside the named chain.
- `G-A3-DIGIKAT` is accepted at live commit
  `db18d2b8f66739fb92fbb4a4f3b34cbb15e081b3`. Chapters 1–3 remain at
  `coauthor_review`, Chapter 4 remains `draft`, and `P3-DIGIKAT` was the sole
  next permitted packet before claim.
- `H-G-A3-DIGIKAT-001` was consumed before claim with the exact aggregate-only,
  three-defect, reconciliation-substitute, retirement, consumer and pinned-
  checkout boundaries. `H-P3-DZS-003` was acknowledged before the first
  substantive edit and remains due for a concrete closeout disposition.
- The packet owns the bounded DigiKat extract, catalogue, schema, validators,
  fixtures, passport, evidence report and three control files. It may not read
  the master corpus, contact the network, edit chapter prose, or claim rights-
  holder permission.
- The workflow validator passed before claim and must pass again in this
  claimed state before the first substantive data edit.

## P3-DIGIKAT closeout

- The author's 2026-08-10 one-thread amendment is now durable in
  `notes/reports/p3-digikat-2026-08-10.md`: this thread may run at most five
  packets in the named strict sequence, but every packet keeps a separate lock,
  evidence record, handoff disposition, workflow check and local commit. No
  broader authority was inferred.
- `H-G-A3-DIGIKAT-001` was consumed before claim. `H-P3-DZS-003` was
  acknowledged before the first substantive edit and consumed at closeout with
  all six inherited external-package rules satisfied. Nothing targeting
  another packet was consumed.
- The source checkout did not move. It remains
  `278a127f9170c1aca82035a4a8357b8a995f91d8`, so the source date of record stays
  2026-07-22 and the separate verification date is 2026-08-10. The builder
  returns `DIGIKAT_EXTRACTS_OK extracts=3 mode=verify`; the master corpus was not
  read and the network was not used.
- D-1 is repaired in the data: `godina_potpuna` is `da` only for 2021, 2022,
  2023 and 2025; 2024 is `ne`, its February-May gap stays absent and January
  stays partial at 1.911 posts. D-2 is repaired by an exact machine-enforced
  divergence contract: 17 of 49 cells, monthly minus annual +446 at 2022/web
  and -389 at 2024/web, net 0, with both files totaling 710.307. D-3 is repaired
  by `lom_metode` in both time files, carrying TikTok's 2023-07 entry, the
  2024-06 break and Instagram's 2024-07 entry.
- The catalogue, schema and validators implement the named non-official-source
  substitute. It is satisfied only when byte reproduction, the six denominator
  identities at tolerance zero and the recorded divergence all pass together.
  The new negative fixture removes the third test and fails for that exact
  reason; the complete suite reports `DATA_NEGATIVE_FIXTURES_OK cases=42`.
- The 3.604 source rows carry 551.712 of 710.307 posts, or 77,67 %. The
  catalogue, licence notice and new `data/digikat_mediji/PUTOVNICA.md` all name
  551.712 as the denominator for a share computed from that file.
- `digikat_akteri` remains in the catalogue as
  `abandoned_with_successor`, with a reason, no live consumer and successor
  `digikat_mediji`. `digikat_mediji` is promoted by `P3-DIGIKAT`; its consumers
  are exactly `WB-C04`, `WB-C05` and `WB-C06`. No rights-holder permission is
  claimed.
- `R03-DIGIKAT-rights` and `R08-DIGIKAT-package` are accepted separately.
  Catalogue, data-integrity, builder, 42 data fixtures, seven integrity
  fixtures, inventory, manuscript, concept, citation, terminology and token
  checks pass on the final packet files. No render was needed because no book
  prose or generated public view changed.
- The packet found no new future-relevant effect. Existing
  `H-G-A3-DIGIKAT-002` already carries every downstream non-uniformity and
  denominator constraint, so no duplicate handoff was created. Chapters 1-3
  remain `coauthor_review`, Chapter 4 remains `draft`, and all shared
  Bookwright registries are unchanged.
- `G-A3-EUROSTAT` is the sole next permitted packet. It was not started before
  this packet closed and committed. Push, merge, tag, archive and deployment
  remain unauthorised.

## G-A3-DIGIKAT closeout

- Two deliveries target this gate and each was handled at its own gate.
  `H-P1B-DATA-LIC-003` is `before_start` and was consumed **before the packet
  claim**; `H-P3-CATALOG-001` is `before_close`, acknowledged before the first
  edit and consumed at closeout. The `G-A3-EUROSTAT`, `G-A3-ESS` and
  `G-A3-TEXT` deliveries of both handoffs remain `pending`.
- **The accepted selection** is `digikat_mediji`: three aggregate files with no
  named individual anywhere — 49 annual platform rows, 438 monthly platform
  rows and 3.604 source rows — derived from three of the project's fourteen
  tracked aggregate tables. The roughly 710.307-post master corpus was not read
  and stays `external-only` as `determ_korpus`.
- **The author's "as recent as possible" directive was verified as fact, not
  recorded as a rule.** `G-A3-DZS` had to leave its year unnamed because a gate
  that retrieves nothing cannot verify what was published. Here the source is
  the author's local checkout, so the gate could check without a single network
  call: HEAD `278a127f9170c1aca82035a4a8357b8a995f91d8` dated 2026-07-22 has not
  moved, and the builder returns `DIGIKAT_EXTRACTS_OK extracts=3 mode=verify`,
  so all three files still reproduce byte for byte. The 2026-07-22 state is the
  most recent state that exists.
- **The gate counted the extract instead of taking it on trust, and found three
  real defects that no earlier record contains.** The denominator identity
  passes 6 of 6 years without tolerance. **D-1:** `godina_potpuna` reads `da`
  for 2024 although February–May are absent entirely and January is partial at
  1.911 posts against a 2021–2023 monthly mean near 6.960 — a false quality flag
  in a book that teaches reading quality flags. **D-2:** the annual and monthly
  files disagree in 17 of 49 platform-year cells, largest +446 and −389, netting
  exactly zero at 710.307 posts; consistent with a year-boundary effect, which
  the gate records as unproven rather than asserting. **D-3:** no method-break
  flag exists although volume roughly triples from June 2024 and platform
  coverage grows from seven to nine. All three bind `P3-DIGIKAT` before any
  promotion.
- **The official-reconciliation condition was not waived and not weakened.** A
  proprietary corpus has no official total, so `H-P3-CATALOG-001` applied
  literally would permanently block the package the author had just approved.
  The gate ruled a named substitute for non-official sources, satisfied only by
  three tests together: byte-for-byte reproduction, the denominator identity
  without tolerance, and a recorded divergence statement carrying the exact
  largest per-cell deviation with its proven zero corpus-wide sum. The third
  test is **stricter** than what it replaces, because it forces the package to
  name its own inconsistency instead of passing over it. `P3-DIGIKAT` must
  implement it with a negative fixture.
- **Rights were read from the source's own published record, not inferred from
  access.** The project's `DATA_AVAILABILITY.md` places `data/processed/*.rds`
  under CC BY 4.0 as aggregates with no personal data. Because the book's author
  is the project lead, this is a proprietary disposition, and the gate confirms
  it explicitly so it is not tacitly inherited. The book still claims **no
  rights-holder permission** for any source because none was sought, and
  `H-P1B-DATA-LIC-003` is not superseded.
- `digikat_akteri` is **closed as abandoned** in favour of `digikat_mediji`,
  because its entry describes a cross-section of named actors the extract
  deliberately lacks; `P3-DIGIKAT` must mark it rather than delete it. The
  omission of the eleven upstream tables naming individuals becomes a
  **permanent first-edition rule**: the book publishes no table naming an
  individual even when the licence is clean, so the exclusion rests on
  editorial decision rather than on right.
- **One reconnaissance claim was corrected rather than repeated.** Ten of the
  remaining tables name actors, not eleven; `proportions_summary.rds` names
  nobody and was rejected for the separate recorded reason that this catalogue
  carries denominators rather than shares.
- Consumers are exactly `WB-C04`, `WB-C05` and `WB-C06`. Chapters 2 and 3 were
  **deliberately not assigned** despite the reconnaissance proposing them, since
  both are accepted and at `coauthor_review` and reopening them has its own
  mechanism. Two unavailable claims were added: no growth or trend claim across
  2024, and no comparison of periods before and after June 2024 without the
  method break stated.
- The author's parallel Eurostat approval was recorded as a **pre-disposition**
  in `notes/reports/author-pre-dispositions-2026-08-10.md` rather than consumed
  here, because it belongs to `G-A3-EUROSTAT`. The open Eurostat attribution
  question is explicitly left open rather than declared resolved, so it cannot
  be skipped.
- `OA-G-A3-DIGIKAT-SELECTION` and `OA-G-A3-DIGIKAT-RIGHTS` are `done` with dated
  resolutions and **no external message was sent**. No data file, catalogue
  entry or chapter prose changed, and all 19 units remain `draft`.

The durable evidence is
`notes/reports/g-a3-digikat-selection-decision-2026-08-10.md`.

## P3-EXISTING closeout

- **Four deliveries target this packet and each was handled at its own gate.**
  `H-P1B-DATA-LIC-001` and `H-P1B-DATA-LIC-002` are `before_start` and were
  **consumed before the packet claim**; the workflow validator confirmed the
  lock only after both were terminal. `H-P3-CATALOG-001` and `H-P3-CATALOG-002`
  are `before_close`, were acknowledged before the first substantive edit — the
  validator refused the claim until they were — and were consumed at closeout.
  Nothing targeting another packet was consumed, and `H-P1B-DATA-LIC-003`
  remains untouched with all six `G-A3` deliveries `pending`.
- **Two packages are promoted and fifteen lanes are unchanged.** `anketa_mreze`
  and `populacija_medija` now ship four deterministic snapshots — an analysis
  file and a paired aggregate each — declared in the catalogue **before** a
  single byte was written, so no undeclared snapshot ever existed in the tree.
  Each promotion records source, version, licence, attribution, an MD5 with its
  algorithm named, and an official reconciliation. The promotion contract was
  strengthened rather than spent: a package may now be promoted only under the
  gate it names itself, every promotion must appear in a per-packet promotion
  log, and every declared file must exist with a matching checksum.
- **`UCBAdmissions` and `anscombe` stay `external-only`, after a search rather
  than an assumption.** The local `datasets` package at R 4.6.0 records only
  `License: Part of R 4.6.0`, a package-level marker; `UCBAdmissions.Rd` has no
  `\source` field at all and cites Bickel, Hammel and O'Connell (1975) in
  *Science*, and `anscombe.Rd` names Tufte (1990), Graphics Press. Both
  documented origins are third-party copyrighted works, so nothing supports a
  repository copy. Technical access through a local R installation was not
  converted into redistribution authority.
- **Two of the four `R25-EXISTING-*` items closed and two did not.**
  `R25-EXISTING-anketa` and `R25-EXISTING-populacija` are `accepted`: each
  snapshot is byte-identical to its generator at its declared seed, and every
  manuscript file that names the package is declared and machine-reconciled in
  both directions. `R25-EXISTING-UCB` and `R25-EXISTING-Anscombe` stay
  `ratified` with one half of each test met — the metadata half is complete and
  the deterministic snapshot may not exist. No packet can close them on current
  evidence; closure needs a dated author rights determination or an explicit
  `deferred_v2_with_reason`, and `H-P3-EXISTING-001` carries that.
- **Two of the three carried items closed and one did not, each judged alone.**
  `R25-CATALOG-storage` is `accepted`, with its applicable scope written into
  the item: two packages have files, both pass all six conventions, and each
  convention is machine-enforced. `R25-CATALOG-validation` is `accepted` **on
  both halves**, not on the catalogue half alone: two accepted packages record a
  checksum and an official reconciliation, and every data-level defect class the
  review lists is exercised against bytes on disk. `R32-CATALOG-paired-views`
  was **not** closed: both pairs reconcile without tolerance, but its test also
  requires a task that reproduces an aggregate, and a task is reader prose a
  `data_package` packet may not write. `H-P3-EXISTING-002` carries that half.
- **Validation is now data-level, and every fixture must fail for its own
  reason.** `scripts/check-data-fixtures.py` proves 32 deliberate defects each
  exit 1 — seventeen catalogue defects plus an unknown fixture name, and
  fourteen data defects injected into a throwaway copy. Each case must also
  print the message belonging to its own rule, because exit status alone would
  credit a fixture that failed for something else. The `rounded_mean` fixture is
  the anti-rounding proof: a mean that has been rounded cannot equal its integer
  total divided by its count.
- The catalogue carries the codebook, so a later package is validated by
  declaring itself rather than by editing a checker: column type, unit, domain
  and missing code per column, the storage disposition including an explicit
  recorded reason for having no sampling weights, and the exact shares, totals
  and means each aggregate must reproduce.
- `data/README.md` was corrected because materialising the snapshots made its
  statement that the simulated sets are not files here untrue. `podaci.qmd` and
  `dodaci/c-katalog-podataka.qmd` were deliberately not touched: both already
  speak of a *future* snapshot rather than denying one, and generating them is
  `P5-C`. `.github/workflows/publish.yml` was deliberately not touched either —
  `check-data-integrity.R` is already blocking, so the new rules run in CI, but
  `check-katalog.py` has never been wired in and the new fixture harness is not
  either. That gap is recorded in `H-P3-EXISTING-003` rather than quietly
  accepted.
- **One real defect was found before the commit and fixed at its source.** The
  repository sets `core.autocrlf=true` and no `.gitattributes` rule covered
  `data/`, so a fresh Windows clone would have turned every LF snapshot into
  CRLF — different bytes, therefore a different MD5 — and every recorded
  checksum would have failed on a file with nothing wrong in it. `data/*.csv`
  and the snapshot notices are now pinned to `text eol=lf`. No existing file
  changed, because all were already LF. `.gitattributes` was added to the
  packet's owned paths mid-packet and the extension is recorded, not concealed,
  exactly as `P3-CATALOG` recorded its `.gitignore` extension. This is **not** a
  local-independence proof: `R08-CATALOG-local-independence` still needs the
  fresh-clone render that `P7-CLEAN-BUILD` owns.
- The 2026-08-05 rights determination holds. The catalogue still records
  `rights_holder_permission_obtained: false` and
  `rights_holder_permission_claim_permitted: false`, the fixture still proves
  the opposite claim fails, and no `G-A3` gate was pre-empted: DZS tourism,
  ParlaMint and ParlaSent remain bundled-but-unpromoted with their exact package
  records still owed to their own gates.
- No chapter or appendix prose, shared registry, spine, `#def-` block,
  terminology, route, render, generated artifact or chapter stage changed. All
  19 units remain `draft` and the live definition count remains 46.

The durable evidence is `notes/reports/p3-existing-2026-08-05.md`.

## P3-CATALOG closeout

- **Both incoming deliveries are `before_start` and both were consumed before
  the packet claim**: `H-P1B-DATA-LIC-001` (the CC BY 4.0 generated-data
  boundary) and `H-P1B-DATA-LIC-002` (one lane and one lawful fallback per
  package). Their `P3-EXISTING` deliveries deliberately remain `pending`, and
  `H-P1B-DATA-LIC-003` — which targets six `G-A3` gates — is untouched and not
  superseded.
- **`data/katalog.yml` is the sole machine-readable data record** and registers
  all 17 P1B inventory packages: 5 `bundled`, 3 `portal-mediated`, 9
  `external-only`. **Not one lane was changed.** Every entry carries source,
  version, licence, attribution, access, redistribution, lane, fallback and
  integrity, plus design, unit, question, role, consumers, refresh class,
  permissible and unavailable claims, and a six-question ethics note.
- **Zero packages are promoted, by decision.** Every entry is `promoted: false`
  and names the exact later gate that may promote it. Promotion requires seven
  conditions at once, so **availability promotes nothing** and a
  portal-mediated or external-only package cannot be promoted at all while its
  lane stands. `UCBAdmissions` and `anscombe` stay `external-only` with their
  lawful fallbacks recorded.
- `data/katalog.schema.json` and `scripts/check-katalog.py` fail closed. **Ten
  deliberate defects each return exit 1** — promoting a portal package,
  promoting without a checksum, an unknown lane, a missing fallback, a
  not-applicable licence, a duplicate id, an exceeded cap, an undeclared
  snapshot, a claimed rights permission, and a duplicated consumer role — as does
  an unknown fixture name.
- `R/fetch-podaci.R` is now candidate-first: it reads the catalogue as its only
  registry, writes **only** into the gitignored `data/_kandidat/`, and promotes
  solely through an explicit `--promote` call that verifies the recorded MD5.
  `_quarto.yml` calls it in neither hook, so a clean render fetches nothing.
- `scripts/check-data-integrity.R` no longer fails *because* the catalogue
  exists; it now **requires** the catalogue, its schema and its validator, and
  fails on any snapshot no entry declares.
- **Seven items closed and six did not, on one stated rule**: an item closes only
  when its test is fully verifiable against artefacts this packet creates or the
  live source. Closed: `R25-CATALOG-schema`, `R25-CATALOG-refresh-classes`,
  `R25-CATALOG-candidate-first`, `R08-CATALOG-admission`,
  `R08-CATALOG-portfolio-cap`, `R08-CATALOG-question-led`,
  `R03-GFI-FINA-external`. Left open with reasons in the register:
  `R25-CATALOG-single-source` and `R25-CATALOG-passport` (need the generated
  views and a chapter's first use — `P5-C`), `R25-CATALOG-validation`,
  `R25-CATALOG-storage` and `R32-CATALOG-paired-views` (need a real registered
  package — `P3-EXISTING`), and `R08-CATALOG-local-independence` (needs a
  fresh-clone render — `P7-CLEAN-BUILD`).
- The **2026-08-05 rights determination is machine-enforced**: the catalogue
  records `rights_holder_permission_obtained: false` and
  `rights_holder_permission_claim_permitted: false`, and a fixture proves the
  opposite claim fails. Each source is cited with its published terms instead.
- `.gitignore` was added to `owned_paths` mid-packet so `data/_kandidat/` is
  ignored; the extension is recorded, not concealed. `podaci.qmd` and
  `dodaci/c-katalog-podataka.qmd` were deliberately not touched.
- No package was selected, promoted, fetched or committed; no data file exists;
  no `G-A3` gate was pre-empted. No chapter or appendix prose, shared registry,
  spine, `#def-` block, route, render or chapter stage changed. All 19 units
  remain `draft`.

The durable evidence is `notes/reports/p3-catalog-2026-08-05.md`.

## P2-VERIFY closeout

- No handoff targets `P2-VERIFY`; the complete ledger was read before the first
  edit and the absence is recorded explicitly. The whole report is tied to one
  declared source state, `commit:fd4564c3d2890c80f5f865f6b386f34b29f8feea`.
- **The gate passes its own three exit tests and cannot certify the ratified
  plan's Phase 2 clause that `R04` is closed.** Those are two different things
  and the report does not blur them.
- **`R04` has four open required children, not two.** All 21 were enumerated one
  by one rather than summarised: `R04-ARCH-macro-order` (`P5-ROUTES`, Phase 5 —
  the two reading routes do not exist), `R04-C11-fixed-order` (`WC-C11`, Phase 4
  Wave C — needs the seven-part order restored in Chapter 11 prose),
  `R04-ROUTES-two-track-map` (`P5-ROUTES`, Phase 5) and
  `R04-C18-whole-prerequisites` (`WE-C18` and `P5-ROUTES`, Phases 4 and 5). Two
  need chapter prose and two need published routes; Phase 2 edits neither.
- The other four Phase 2 exit clauses are met and verified: `R10`, `R15`, `R24`
  and `R36` are ratified with their items deliberately open exactly as the clause
  intends; all 19 spines are ratified; the definition and prerequisite changes
  have an approved map; and no unresolved conflict remains between the review and
  the live governing documents.
- **The discrepancy is a conflict between two ratified documents** — the plan and
  the register — about *when* `R04` may close, not a packet's omission. `R04` was
  not forced closed, the exit gate was not redefined, and nothing was hidden by
  aggregation. `H-P2-VERIFY-001` carries the closure to `WC-C11`, `WE-C18`,
  `P5-ROUTES` and `P6-VERIFY`. Reconciling the plan's wording with the register
  is a separate author decision that no packet may take alone.
- **All 22 accepted Phase 2 packets were verified individually**, each against
  its own contract and none by aggregation, on thirteen re-derived conditions
  covering terminal status, `source_state` equal to `change_reference`, exact
  receipt coverage of `required_evidence`/`outputs`/`exit_tests`, every test
  marked `passed`, contract evidence and tests plus a packet-specific test, a
  packet review declaring `all_future_effects_recorded` with outgoing handoffs
  matching its source handoffs, and no non-terminal incoming delivery. **All 22
  satisfy all thirteen.**
- **One real coverage gap was found.** `scripts/check-book-architecture.py` has
  **no negative-fixture hook at all**, although its three consumers each carry
  two. Five Phase 2 packets record no deliberate fixture, which breaches no
  contract because no Phase 2 contract requires one — reported as coverage, not
  as a blocker. (`P2-ASSESS` and `P2-IDENTITY` do record two fixtures each, under
  a `check:` token, so the raw count of seven is really five.)
  `H-P2-VERIFY-002` carries the gap to `P6-VERIFY`.
- `P2-CLAIMS`, `P2-ASSESS` and `P2-IDENTITY` still carry the historical
  `chapter-spines-ratified-0-of-19` evidence token. It was true at their closure,
  and the live checkers now report 19 of 19 — the snapshot was replaced by an
  invariant, as `P2-SPINE-PREFACE` recorded.
- Six existing deliberate fixtures were rerun at this source state and all six
  returned exit 1. Thirteen deterministic commands were rerun and all pass. The
  only remaining registered integrity debt is the `fig-anscombe` figure
  introduction owned by `WB-C05`.
- `push`, `merge`, `tag`, `archive` and `deploy` are verified `false`, with zero
  external messages across 82 canonical asks. Both 2026-08-05 amendments were
  verified in this state: no independent-review claim exists anywhere, and no
  rights-holder permission is claimed.
- This gate closed no register item but its own packet, and changed no prose,
  registry, spine, definition, generated artifact or chapter stage.

The durable evidence is `notes/reports/p2-verification-2026-08-05.md`.

## P2-DOCS closeout

- **A process error is recorded rather than concealed.** A first pass of
  governing-document edits was made *before* the packet was claimed and before
  the two deliveries were acknowledged. The working tree was reverted to `HEAD`
  for all seven documents, the packet was then claimed, both deliveries were
  acknowledged, `check-review-workflow.R` passed with `P2-DOCS` active, and the
  work was redone. The closing source state was produced under a valid write
  lock.
- Exactly two deliveries target this packet and both were consumed with an exact
  disposition and evidence: `H-P1B-META-004` (three stale internal markers) and
  `H-P1C-PDF-001` (the stale deployment description). Nothing targeting another
  packet was consumed.
- **AGENTS.md now describes the implemented production path**, verified line by
  line against the live `.github/workflows/publish.yml`: the blocking check
  ladder and its fail-closed fixtures, `check-pdf-release-path.ps1`, then the PDF
  built only through `render-book-pdf.ps1 -RequireCleanCommit` with no
  `continue-on-error`. The implemented path itself was not changed, and the
  section closes with an explicit sentence that it promises no edition and
  authorises no release. The same paragraph's second stale instruction — that
  `SITE_URL` is edited in `R/build-ai-exports.R` — was replaced, because that
  script now reads the address from `_quarto.yml` metadata.
- The `kolegij` profile comment no longer claims revealed solutions. It records
  the ratified but **unimplemented** D06 two-layer contract, states that the
  profile currently reveals nothing, and names the packets that will implement
  it. No rejected pathway was revived, which `check-book-inventory.py` confirms
  by still reporting `solutions=0` with an unchanged checksum. `_quarto.yml` now
  says the visual identity *is* selected in DESIGN.md while the cover and favicon
  files are genuinely absent, so both lines stay commented out.
  `bookwright_plugin/README.md` no longer calls the shared state seeded or
  provisional.
- `STYLE.md`'s instruction to "run the detector and ratify the real
  distribution" was stale against its own 30 July 2026 changelog entry and was
  replaced. `STYLE.md`, `ENRICHMENT.md` and `notes/struktura-knjige.md` now state
  one rule: **a band is a floor, not a finish line, and no word target advances
  anything.**
- **Two items closed and five did not, on purpose.** `R04-BOOK-content-weight`
  and `R23-SCOPE-no-technical-ds` are `accepted`; the latter was verified by a
  whole-source search finding zero occurrences of SQL, databases, cloud,
  scraping, dashboards, hyperparameters or neural networks. The five left open
  each have exactly one half of their test unmet, recorded in the register:
  `R04-ARCH-macro-order` (the two reading routes do not exist anywhere — the
  preface advertises none); `R12-SCOPE-no-variance-course`,
  `R14-SCOPE-reading-not-fitting` and `R23-SCOPE-reading-not-production` (all
  three need routing, and `dodaci/d-koji-test.qmd` is a 47-line partial draft
  with no dependence route and no route out of the book); and
  `R23-SCOPE-no-new-chapters-widgets` (counts verified, but retrieval tasks are
  R35 work in Phases 4 and 5). `R11-SCOPE-no-multiple-imputation` was already
  terminal and untouched.
- `H-P2-DOCS-001` carries the three routing-dependent closures to `WC-C08`,
  `WD-C16` and `P5-D`; `H-P2-DOCS-002` carries the two half-satisfied closures to
  `P5-ROUTES` and `P5-CLOSURE-18`; `H-P2-DOCS-003` records that
  `scripts/check-terminology.py` is **not yet a blocking CI step** and carries
  the wiring to `P7-CLEAN-BUILD`.
- No chapter or appendix prose, shared registry, `#def-` block, spine, identity
  brief, data package, route, render or chapter stage changed. The `_quarto.yml`
  chapter order is untouched, all 19 units remain `draft`, the live definition
  count remains 46, and the book-inventory checksum is unchanged.

The durable evidence is `notes/reports/p2-docs-2026-08-05.md`.

## P2-TERMS closeout

- **Seven deliveries target this packet and all seven were consumed with an
  exact disposition and evidence.** `H-G-A2C-001` is a `before_start` delivery
  and was consumed **before the packet claim**. The six `before_close`
  deliveries — `H-P1C-INTEGRITY-002`, `H-P2-SPINE-I-001`, `H-P2-SPINE-II-001`,
  `H-P2-SPINE-IV-001`, `H-P2-SPINE-V-001`, `H-P2-SPINE-FINALE-001` — were
  acknowledged before the first substantive edit and consumed at closeout.
  `H-P2-SPINE-V-002` remains `pending` for `P5-ROUTES`,
  `H-P2-SPINE-FINALE-002` for `WE-C18` and `P5-ROUTES`, and
  `H-P1C-INTEGRITY-001` for `WB-C05`; none was consumed here.
- **The central tension was resolved explicitly, not left to the checker.** The
  live source carries 46 `#def-` blocks while six ratified maps approve 52, and
  the maps are implemented by chapter packets that have not run. The canonical
  ledger is therefore reconciled to the **live 46**, and the approved 52 is
  recorded as expected future state in the new terminology registry with its six
  implementing packets named. The reason is that writing 52 into the ledger
  before the blocks exist would make the ledger disagree with the live source and
  break the very gate this packet was sent to retire.
- **The frozen concept gate is retired.** The one stale ledger entry —
  `standardizirani rezidual` with its Pearson-form definition, which the Chapter
  13 correction had already removed from the prose — is now the canonical
  `prilagođeni standardizirani rezidual` with its marginal-share definition. The
  `e_{ij}` notation entry had to follow that rename, because the checker requires
  every notation entry to point at an existing concept; the first run failed on
  exactly that and it is recorded rather than silently fixed.
  `data/concept-graph.json` was regenerated and moved from 449 to 503 edges at an
  unchanged 46 nodes. Both debt entries are gone from
  `scripts/integrity-debt.json`; only the `WB-C05` figure debt remains.
  `check-concepts.py` now reports `ledger_debt=0 graph_fresh=true`.
- **Three `#def-` identifiers were deliberately not renamed** —
  `#def-standardizirani-rezidual`, `#def-korelacija` and `#def-mala-polja` — and
  are registered as exceptions instead, because each anchors a concept-graph node
  and a `pojmovnik.qmd` link.
- **A ratified terminology registry is now live and machine-checked.**
  `conventions.schema.json` admits `terminology_registry` with no existing field
  removed or altered, and the new key is deliberately not `required`, so every
  earlier state stays valid. The registry carries the review route, five
  principles, the spine confirmation, 13 gate-fixed forms, 12 superseded forms, 3
  deliberate departures, 4 meaning rules, 3 stable identifiers, the 46→52
  definition map, 8 live divergences, one deliberately excluded place, and the
  packet authority boundary. It **deliberately does not restate** the 166 forms
  the ratified spines carry, and the checker asserts that it never does.
- `scripts/check-terminology.py` is new and reports `TERMINOLOGY_OK`. Its three
  deliberate fixtures — `duplicate_canonical_form`,
  `superseded_form_made_canonical`, `independent_review_claimed` — each return
  exit 1, and an unknown fixture name does too. Its live-divergence assertion is
  strict in both directions, so the registry cannot go stale when a chapter
  packet repairs prose; that obligation is carried by `H-P2-TERMS-003`.
- **Two items closed and one did not, on purpose.**
  `R04-TERMS-concept-regeneration` is `accepted`, with a recorded scope note that
  the reader-visible rendering of variants and departures in Dodatak E belongs to
  `R36-BOOK-alternatives` in `P5-E`. `R04-C17-definitions` is `accepted`: `G-A2c`
  fixed the canonical forms and the terminology review is recorded as **the
  author's own**, with no independent-review claim anywhere and a fixture proving
  the ban. `R36-BOOK-new-cluster` was **not** closed and stays `ratified`: its
  acceptance test also names prose, figures and exercises, and eight divergences
  still live in Chapters 0, 8, 16 and 17, which a registry packet may not edit.
  `H-P2-TERMS-001` carries that closure to `P6-CONTINUITY`. Leaving it open does
  not stall Phase 2, because the ratified plan's own Phase 2 exit condition keeps
  R10, R15, R24 and R36 open until their book-wide implementation is verified.
- An audit of all sixteen Dodatak E entries and of `pojmovnik.qmd` found **zero
  contradictions** with the canonical register and no superseded form in either
  view. Dodatak E's stale status marker and its missing variant/departure
  rendering are carried to `P5-E` by `H-P2-TERMS-004` rather than repaired here,
  because both are appendix prose.
- Both 2026-08-05 author amendments hold. The packet makes **no
  independent-review claim** anywhere, the registry forbids one and a fixture
  proves the ban; it claims **no rights-holder permission**, selects no data
  package and does not supersede `H-P1B-DATA-LIC-003`.
- No chapter or appendix prose, `#def-` block, `#def-` identifier, chapter spine,
  identity brief, data package, route, render or chapter stage changed. All 19
  units remain `draft` and the live definition count remains 46.

The durable evidence is `notes/reports/p2-terms-2026-08-05.md`.

## G-A2c closeout

- No handoff targets `G-A2c`; the complete ledger was read before the decision,
  so there was no incoming delivery to acknowledge or consume. The six
  deliveries that target `P2-TERMS` — `H-P1C-INTEGRITY-002`,
  `H-P2-SPINE-I-001`, `H-P2-SPINE-II-001`, `H-P2-SPINE-IV-001`,
  `H-P2-SPINE-V-001` and `H-P2-SPINE-FINALE-001` — were read because they name
  exactly what this gate had to fix, and none was consumed here.
- The complete terminology register and the reviewer route were drafted first,
  and the gate then closed against that drafted state. Author and editor Luka
  Sikic accepted it as recommended on 2026-08-05, with no amendment.
- **Terminology review is the author's own editorial responsibility and nothing
  else.** The 2026-08-05 amendment is closed out here: no reviewer is sought,
  recruited or named, and the first edition may make **no independent-review
  claim** about its terminology anywhere — book, preface, colophon, release
  metadata or site copy. That binds `P2-TERMS`, `P2-DOCS`, `P6-METHODS`,
  `P6-VERIFY`, `P8-META` and every packet writing edition copy. This gate makes
  no such claim itself.
- **The 166 forms the ratified spines already carry are confirmed, not
  reopened.** The nineteen ratified spines hold 168 key-term slots and 166
  distinct Croatian forms. A terminology gate has no authority to weaken a
  ratified spine, so it confirms them and changes none. `procjena` in the
  preface and Chapter 9, and `standardizirana razlika` in Chapters 11 and 14,
  are one concept carried twice rather than a collision.
- **Fifteen load-bearing forms the spines named without canonising are fixed**,
  including the Chapter 17 split vocabulary named in `H-P2-SPINE-V-001` —
  `razdvajanje na skup za učenje, provjeru i ispitivanje` with its three
  component sets — and the finale terms named in `H-P2-SPINE-FINALE-001`:
  `paket dokaza`, `putovnica skupa podataka` and `objava uporabe asistenta`.
  `R36-BOOK-new-cluster` is settled across the four activities, the split
  vocabulary, `izgledi`, the causal terms, `osjetljivost`, `kalibracija` and
  `pomak distribucije`. Only `omjer izgleda` and `predviđena vjerojatnost` are
  fixed without a spine naming them, because the ratified plan foresees a
  bounded Chapter 16 binary-outcome bridge; whether it appears remains `WD-C16`.
- **Four meaning collisions carry rules rather than being left to the
  implementer.** `osjetljivost` never names the confusion-table rate, because a
  short name for one rate is exactly the single-metric reduction the `c17` brief
  forbids. `kalibracija` is never standalone and is always written with its
  object, which is what live Chapter 13 prose already does. `predviđanje` is the
  canonical noun and `predikcija` survives only inside the ratified compound
  `sustav predikcije`, so Chapter 17's ratified term is untouched. `referentna
  oznaka` and `zabilježeni referentni ishod` are two steps of one arc and both
  remain, and neither is ever written as *istina* or *ground truth*.
- Three deliberate departures carry recorded reasons: `tablica zabune` rather
  than a matrix, because the same object is Chapter 13's contingency table and
  two names would create two sources of truth; `kolider`; and `izgledi`.
- **Three `#def-` identifiers deliberately do not follow their term and must
  never be renamed**, because they anchor the concept-graph node and the
  `pojmovnik.qmd` link: `#def-standardizirani-rezidual`, whose canonical term is
  `prilagođeni standardizirani rezidual`; `#def-korelacija`, whose canonical term
  is `Pearsonova korelacija` beside the general key term `korelacija`; and
  `#def-mala-polja`.
- The six ratified definition maps are confirmed to take the frozen set of 46
  live blocks to 52, and none of the six is changed. This gate wrote no block;
  the live count remains 46 and `scripts/check-concepts.py` still reports
  `definitions=46 ledger_debt=2 graph_fresh=false`, unchanged.
- An independent inventory against the live source agrees with the maps: exactly
  three of the 46 bolded terms are not key terms of their own ratified spine, and
  they are precisely `varijanca` and `asimetrija` in Chapter 4, which `G-A2b-II`
  removes as separate blocks, and `Pearsonova korelacija` in Chapter 6, which
  sits one level below the key term `korelacija`. No other divergence exists.
- **Ten live-source divergences are anchored to exact files and lines and
  assigned to the packet that may edit them**, not left as prose. The stale
  concept-ledger entry `standardizirani rezidual`, still carrying the Pearson-form
  definition that the Chapter 13 correction removed, is one of the two entries the
  checker counts as `ledger_debt` and is a `P2-TERMS` obligation. `curenje
  podataka` at `chapters/02-mjerenje-i-dizajn.qmd:380` is deliberately excluded
  and must not be changed: there the words describe an actual data breach used as
  a quasi-experimental comparison, not statistical leakage.
- `R04-C17-definitions` was deliberately **not** closed here. It is a `P2-TERMS`
  item, and this gate closes no register item outside its own decision record.
  `R04-C18-whole-prerequisites` was not touched and remains an obligation of
  `WE-C18` and `P5-ROUTES`.
- `OA-G-A2C-TERMS-EDITOR` is `done`, with a dated resolution; no external message
  was sent. `H-G-A2C-001` carries the accepted register to `P2-TERMS` at its
  `before_start` gate and to `P5-E` at its `before_close` gate;
  `H-G-A2C-002` carries the ten anchored divergences to `WA-C00`, `WC-C08`,
  `WD-C16` and `WD-C17`.
- Both 2026-08-05 author amendments hold. This gate makes **no
  independent-review claim** anywhere and claims **no rights-holder permission**
  for any source; it selects no data package and does not supersede
  `H-P1B-DATA-LIC-003`.
- No chapter or appendix prose, registry, spine, `#def-` block, concept graph,
  identity brief, data package, route, render, generated artifact, chapter stage
  or external authority changed. All 19 units remain `draft` and the live
  definition count remains 46.

The durable evidence is `notes/reports/g-a2c-terminology-decision-2026-08-05.md`.

## G-A3-DZS closeout

- Two deliveries target this gate and each was handled at its own gate.
  `H-P1B-DATA-LIC-003` is `before_start` and was consumed **before the packet
  claim**; `H-P3-CATALOG-001` is `before_close`, acknowledged before the first
  edit and consumed at closeout. The five other `G-A3` deliveries of both
  handoffs remain `pending`.
- **The accepted selection** is `BS_TU11` as a complete-year national monthly
  arrivals and overnights series, one `BS_TU12` county cross-section, and a
  bounded `T01`–`T03` long extract. Totals and suppression codes are retained,
  annual and monthly rows stay separate so they cannot be double counted, and the
  full DZS stack stays external.
- **The snapshot year is a rule, not a number.** The author chose the latest
  possible year, read as the most recent **complete** calendar year published at
  retrieval, pinned by exact edition and date. An incomplete current year is
  excluded. **This gate deliberately names no year**: a gate that retrieves
  nothing cannot verify what has been published, and naming one would assert an
  unchecked publication fact. `P3-DZS` pins it, and must **stop and return the
  question** if the latest complete year is not published in a form the selection
  admits.
- **The lane stays `bundled` and promotion was explicitly withheld.**
  `data/katalog.yml` was not edited: `dzs_turizam` still carries
  `promoted: false` and `promoting_gate: G-A3-DZS`. The established basis is
  general — the Croatian Open Licence plus the author's determination — and a
  general basis is not an exact package record. `P3-DZS` must record the edition,
  retrieval date, attribution, checksum and reconciliation to the official totals
  before any promotion.
- The package serves Chapter 3 as one traceable public claim, with two
  permissible claim classes and three unavailable ones recorded, and the lawful
  fallback unchanged until the package passes.
- The book claims **no rights-holder permission**, because none was sought;
  `H-P1B-DATA-LIC-003` is not superseded.
- The author's parallel election answer — keep DIP portal-mediated, option A —
  was recorded as a pre-disposition in
  `notes/reports/author-pre-dispositions-2026-08-05.md` rather than consumed
  here, because it belongs to `G-A3-DIP`.
- No data file was retrieved, created or committed; no catalogue entry changed;
  no chapter prose changed. `OA-G-A3-DZS-SELECTION` is `done` with no external
  message sent.

The durable evidence is
`notes/reports/g-a3-dzs-selection-decision-2026-08-05.md`.

## P3-DZS closeout

- **The first package in the book to promote data that its own generator did not
  make.** `dzs_turizam` is now `promoted: true` under `P3-DZS`, with
  `promoting_gate_ratified_by: G-A3-DZS` and that gate's decision record on disk,
  so no packet appointed itself. `promoted_total` is 3.
- **No network retrieval.** The source is the author's local mirror, downloaded
  2026-07-27 from the DZS PxWeb API. The retrieval date of record is 2026-07-27
  and not the packet date, and the mirror with its refresh script is the recorded
  provenance chain.
- **The ratified selection was not viable as written and was not silently
  substituted.** `T01`–`T03` is not a unique identifier in the DZS tourism base,
  and no viable set exists under it: T01 ends at 2019, T02 reaches 2024 with 44%
  of its 2024 cells empty, and the coastal `BS_T01`–`BS_T03` tables carry roughly
  55% empty rows. The packet returned the narrowing to the author, who confirmed
  the household survey `T03` at 2024 on 2026-08-05. The accepted `G-A3-DZS`
  selection is **amended explicitly**, not overwritten.
- **Four extracts materialised**, each reproducing byte for byte from the mirror.
  Annual and monthly rows live in separate files so the published annual row can
  never be double counted against its own twelve months. Three published
  missing-value codes stay distinct from one another and from zero.
- **The promotion contract was tightened, not spent.** A decision gate may no
  longer be the `promoting_gate` of a promoted package; moving that gate requires
  naming a different existing decision record; the promotion log now carries the
  **names** of promoted packages and is compared in both directions. The
  snapshot-notice check now reads the package's own `licence_uri` instead of
  demanding a CC BY 4.0 link, which would have forced a false licence onto a
  Croatian Open Licence source. Composite keys and declared missing-value codes
  are now first-class. All six rules bind every later external package through
  `H-P3-DZS-003`.
- **Closeout re-verified the evidence independently**, recomputing every headline
  figure directly from the mirror rather than from the extracts: 2025 gives
  20.698.963 arrivals and 94.820.989 overnights, 2024 gives 20.246.060 arrivals,
  the 21 county rows sum to the national totals with residual 0 across all six
  combinations, 126 monthly-to-annual comparisons show zero mismatches, and the
  survey's largest residual is exactly 1 across 18 comparisons — a property of
  separately rounded estimates, not an error.
- **One claim was not re-verified**: the agreement with the *live* PxWeb API. The
  author's directive forbids network retrieval, so it stands as recorded. Its
  mirror half is independently confirmed, and the agreement of `BS_TU11` with
  `BS_TU12` on six independent sums gives the same figure a second, internal
  proof.
- Four outgoing handoffs created: `H-P3-DZS-001` (the unit is an arrival, not a
  person), `H-P3-DZS-002` (the source last-modified date is missing and the
  attribution obligation is not complete on its face), `H-P3-DZS-003` (the six
  tightened promotion rules), `H-P3-DZS-004` (survey and administrative figures
  measure different things and must not be added).
- The book claims **no rights-holder permission**, because none was sought. No
  chapter prose changed and all 19 ledger units remain `draft`.
- **The dashboard's own state table was stale** and is corrected here: it still
  named `P3-EXISTING` as last completed and `G-A3-DZS` as next permitted, both
  already superseded by its own front matter.

The durable evidence is `notes/reports/p3-dzs-2026-08-05.md`, whose declared
state is
`podaci:sha256-877f77292e41ae8b850fb3687c198acdb3dd9d0dfa59fcf808da3f049fc49796`.

## G-A3-DIP closeout

- `H-P1B-DATA-LIC-003` was consumed before the packet claim and
  `H-P3-CATALOG-001` was acknowledged before the first edit and consumed at
  closeout. Nothing targeting another packet was consumed.
- Author and data-policy owner Luka Sikić approved the recommended selection:
  the 2024 Croatian parliamentary election, one row per officially published
  electoral unit, with the national total used only for reconciliation. The
  semantic fields are electoral-unit identity, eligible-voter denominator,
  ballots-cast numerator, valid ballots and invalid ballots under the source's
  actual names.
- Chapter 3 uses the source only to audit turnout's numerator, denominator and
  aggregation. List-level, individual, causal and ecological claims are
  unavailable.
- The route stays genuinely `portal-mediated`: `promoted: false`, no retained
  local source, no local checksum and no promotion-log entry. The author
  approved a dated read-only official-portal inspection, exact retrieval
  instructions, source-exposed schema evidence and reconciliation against
  published totals. The existing verified DZS/generated fallback remains.
- The local-file assumptions in `P3-DIP`, `R03-DIP-rights` and
  `R08-DIP-package` are explicitly amended for this route. No local-only test is
  silently waived or falsely passed. The non-operative `promoting_gate` must be
  removed rather than moved by `P3-DIP`, because the package is not promoted.
- No rights-holder permission is claimed, because none was sought. No data file,
  catalogue entry or chapter prose changed, and all 19 units remain `draft`.
- `OA-G-A3-DIP-SELECTION` is `done`, no external message was sent, and
  `H-G-A3-DIP-001` carries the full disposition to `P3-DIP` at `before_start`.

The durable evidence is
`notes/reports/g-a3-dip-selection-decision-2026-08-05.md`.

## P3-DIP closeout

- The package closes as a **verified portal route, not a local snapshot**.
  `dip_2024` remains `portal-mediated`, `promoted: false`, `files: []`,
  `checksum: null`, `promoted_by: null`, and outside `promotion_log`. The
  non-operative `promoting_gate` was removed rather than moved.
- The official 2024 archive route and report were inspected read-only on
  2026-08-05. The archive was not downloaded. Server ETags and last-modified
  dates identify the inspected publications but are not represented as local
  checksums.
- The official turnout table has twelve electoral-unit rows. They sum exactly
  to a denominator of 3.558.089 and 2.216.763 approached voters, reproducing
  62,30%. Valid 2.154.733 plus invalid 60.476 gives 2.215.209 according to
  ballots, which is 1.554 below approached; those official labels remain
  distinct.
- The original generic local-file test remains visible and is recorded
  `not_applicable_by_author_amendment`, not passed. Its route-specific
  replacement proves local bytes and checksum absent, records source identity,
  route, displayed schema/key/missing evidence and published-total
  reconciliation, and retains the lawful DZS/generated fallback.
- `scripts/check-dip-portal.py` passes and six deliberate defects each return
  exit 1. The catalogue and data-integrity checks still report 20 packages,
  three promoted, three portal-mediated, 20 snapshots, nine reconciliations and
  zero undeclared snapshots.
- `R03-DIP-rights` and `R08-DIP-package` are accepted against the explicit
  portal amendments. No rights-holder permission is claimed because none was
  sought.
- `P3-PILOT` is now truly `descoped` under the 2026-08-05 author amendment. It
  is terminal for sequence routing but neither its outputs nor its exit tests
  are claimed; a new workflow fixture fails if its amendment record disappears.
- Three handoffs carry every future effect: `H-P3-DIP-001` to `WA-C03`,
  `H-P3-DIP-002` to `P6-DATA` and `P8-META`, and `H-P3-DIP-003` to
  `P3-VERIFY-A`. No chapter prose changed and all 19 units remain `draft`.

The durable evidence is `notes/reports/p3-dip-2026-08-05.md`, whose declared
state is
`portal:sha256-a96a01dc14ff3c7a7d6acf17a0ed577934d9b087bfecdf9c6106d6a8c5f9dca6`.

## P3-VERIFY-A closeout

- `H-P3-DIP-003` was consumed before the gate claim. Nothing targeting another
  packet was consumed.
- `P3-EXISTING`, `P3-DZS` and `P3-DIP` were verified independently against
  source state `47577dca217f0425513e7898ac65dcd6e616363b`. Four generated
  snapshots and four DZS extracts reproduce without writing, and the DIP
  checker proves the portal route with zero local files and `checksum: null`.
- The stale novice-pilot wording in the gate's scope and third exit test is
  explicitly amended under the author's 2026-08-05 record. `P3-PILOT` is
  `descoped`; no output or exit test is claimed for it.
- No blocker is hidden by aggregation. The live DZS API was not contacted under
  the author's no-fetch directive, and the DIP archive was not downloaded under
  its portal-mediated lane. Both limitations and their verified replacement
  routes are explicit.
- Every R-backed verification reports that `renv` is out of sync. The checks
  pass, but `H-P3-VERIFY-A-001` requires `WA-C00` to run `renv::status()` before
  its claim and before any preface edit, then resolve the drift or record the
  exact mismatch and why the targeted renders are safe.
- No data, chapter, appendix, render, generated artefact, definition,
  terminology or unit stage changed. All 19 units remain `draft`.

The durable evidence is `notes/reports/p3-verify-a-2026-08-05.md`, tied to
`commit:47577dca217f0425513e7898ac65dcd6e616363b`.

## WA-C00 closeout

- `H-P3-VERIFY-A-001` was consumed before the packet claim and before the first
  prose edit. `renv::status()` found five packages installed and recorded but
  unused — `brio`, `desc`, `downlit`, `fansi` and `xml2` — with no missing
  package and no installed-versus-recorded version mismatch. The unchanged
  informational warning was then tested by real renders.
- `H-P0-STATE-001`, `H-G-A2C-002` and `H-P2-TERMS-003` were acknowledged before
  the first edit and consumed at closeout. The preface now promises a
  checkable calculation trace without visible code, uses canonical
  `predviđanje`, and removes only the matching preface divergence from the
  terminology registry; seven later divergences remain.
- The final preface implements all nine aspects, five terms, zero prerequisites
  and twelve exclusions of its ratified spine. A sourced known-population
  inquiry replaces manifesto-like meta-scaffolding. It has no widget, figure,
  definition block or visible code and retains all four task levels.
- The numerical audit reconstructs five rows and 50.000 records: portal 15.101
  or 30,202%, largest but not a majority; social networks 13.378 or 26,756%.
  Citation, catalogue and data-integrity checks pass, and no unpromoted
  candidate is cited.
- HTML, PDF and DOCX each rendered with exit 0 under R 4.6.0 and Quarto 1.9.38.
  Their exact hashes and sizes are in `notes/reports/wa-c00-2026-08-05.md`.
  Render-generated `docs/`, `_freeze/` and AI exports were restored to their
  prior Git content and are outside the packet.
- Six independent read-only critics reviewed the pre-revision state. The
  exercise-coverage, measured-construct and unsupported clean-install claims
  were corrected. All six then reviewed the same final hash and passed it with
  zero remaining fatal or major finding. The synthesis recommends acceptance
  but explicitly does not record it.
- All six owned child items remain `ratified`, and all 19 chapter units remain
  `draft`, because only `C00` and the author can make the acceptance and ledger
  disposition. The author's current explicit instruction for `C00` forbids
  use of the earlier standing-delegation shortcut for this gate.
- No new future handoff is required. The renv observation is fully consumed,
  later jamovi, continuity and release-render work already has exact owners,
  and the sole final style note is optional local rhythm rather than a
  downstream constraint.

The final preface source state is
`source:sha256-60ec5feb1d8e71dc680472a403a2033ca500f6cdb4f80dc5d4f7c954bac14dbf`.
The durable evidence is `notes/reports/wa-c00-2026-08-05.md`, the six
`notes/reports/wa-c00-critic-*-2026-08-05.md` reports and
`notes/reports/wa-c00-six-critic-synthesis-2026-08-05.md`.

## C00 closeout

- No handoff targets `C00`, and nothing targeting another packet was consumed.
  The author replied exactly: `C00 accepted for
  0eb9e3c15d191bd5b88124ecf4593af7b1aed02d on 2026-08-05.`
- The final chapter source commit is
  `0eb9e3c15d191bd5b88124ecf4593af7b1aed02d`; it contains the final preface
  SHA-256 `60ec5feb…bac14dbf`. All six reports and the synthesis address that
  exact material state and record zero remaining fatal or major finding.
- `notes/reports/c00-acceptance-package-2026-08-05.md` cites the final commit,
  all six reports, the synthesis, the exact author reply and the applied ledger
  disposition.
- `00-predgovor` advances from `draft` to `coauthor_review`; the ledger
  explicitly says this records acceptance rather than a claim that the author
  read the chapter. The spine checker now permits that transition only when
  `C00` is accepted, and its injected unaccepted-gate fixture fails closed. The
  identity-brief checker retains ledger coverage and valid-stage checks but
  delegates current acceptance authority to that gate-aware checker; both of
  its existing negative fixtures still fail. The six C00 child items are
  accepted against their own source evidence.
- The fail-closed concept check exposed a stale WA-C00 co-occurrence graph.
  `data/concept-graph.json` was regenerated against the unchanged accepted
  chapter source: 46 nodes, 502 edges, zero ledger debt and a fresh graph. No
  definition, concept-ledger entry or chapter prose changed in C00.
- `OA-C00-ACCEPTANCE` is `done` from the in-thread reply. No external message
  was sent. `C00` is accepted, `WA-C01` is next, and no later packet was
  started in this thread.

## Author amendment 2026-08-05 — reader pilot removed, author reads at the end

The author removed the five-reader think-aloud pilot from the first edition and
replaced the recruited release readers with **the author's own read of the
finished book**. No reader is recruited, invited or named. The order of work is
now: draft everything, then the author reads the whole book, then revisions.

`P3-PILOT` is descoped and removed from the prerequisites of `P3-VERIFY-A` and
`G-A4-03`, so **no prose packet waits on a reader**. `P7-PILOT` is **not**
descoped, still required by `G-A5a`, and runs with the author as its reader; it
must record that reader explicitly and dispose of the `reader_evidence` clause
naming deidentified session records, which an author read cannot supply in that
form. `OA-P3-PILOT-RECRUITMENT` and `OA-P7-PILOT-RECRUITMENT` are
`withdrawn_with_reason`, and `R26-PILOT-five-reader` is `rejected_with_reason`.

**Chapter acceptance moves under a standing delegation.** The nineteen gates
`C00`–`C18` keep the six-critic panel and every deterministic check; only the
author's signature moves to the final whole-book read. The delegation covers
author acceptance alone, **no packet may record that the author read a
chapter**, and the author may reopen any chapter at the final read through the
existing invalidation mechanism.

**Reading times stay as they are.** The author kept the existing `.chapter-meta`
times unchanged and unlabelled. That is a fourth option
`R26-META-reading-time`'s test does not admit, so that item is
`rejected_with_reason` rather than satisfied.

Binding consequence: the first edition may make **no claim that its reading
times are measured, reader-tested or evidence-based**, and **no claim that the
book was validated by new readers**. Both bind `WA-C00`, every chapter packet,
`P5-ROUTES`, `P6-CONTINUITY`, `P7-PILOT` and `P8-META`.

The six-critic panel, every deterministic checker, every spine and the
prohibition on inventing a number, study, source or citation are unchanged. The
absence of readers relaxes no evidence rule.

The durable record is
`notes/reports/author-amendment-reader-route-2026-08-05.md`.

## Author amendment 2026-08-05 — terminology reviewer withdrawn

The author withdrew the independent domestic terminology reviewer from the first
edition. `OA-P6-TERMS-REVIEWER-RECRUIT` and `OA-P6-TERMS-SIGNOFF` are
`withdrawn_with_reason`, and `R36-BOOK-domestic-review` is
`rejected_with_reason`. The canonical term map itself is unchanged and is now
wholly the author's editorial responsibility.

Binding consequence: the first edition may make **no independent-review claim**
about its terminology anywhere — book, preface, colophon, release metadata or
site copy. That binds `P2-TERMS`, `P2-DOCS`, `P6-METHODS`, `P6-VERIFY`, `P8-META`
and any packet writing edition copy.

The chain `G-A2c` → `P2-TERMS` → `P2-DOCS` → `P2-VERIFY` → `P3-CATALOG` now has
no external dependency. The DZS and DIP rights asks are untouched and remain open.

The durable record is `notes/reports/g-a2c-reviewer-amendment-2026-08-05.md`.

## Author determination 2026-08-05 — DZS and DIP rights inquiries withdrawn

The author determined that the selected DZS and DIP extracts are publicly
available and require no permission, and directed that no rights inquiry be sent.
`OA-G-A3-DZS-RIGHTS` and `OA-G-A3-DIP-RIGHTS` are `withdrawn_with_reason`. This is
the author's own recorded determination as the accountable party, not an owner
reply; no external message was sent.

`H-P1B-DATA-LIC-003` is **not** superseded. It already permitted a gate to ratify
a lawful package rather than preserve the cautious lane, and it already recorded a
verified general bundled basis for DZS tourism; this determination selects that
branch. `G-A3-DZS` and `G-A3-DIP` must still consume the handoff and record exact
package evidence, and `P3-CATALOG` still requires published terms, attribution,
edition, checksum and fallback per entry.

Binding consequence: the book may **not** claim it obtained rights-holder
permission, because none was sought. It may cite the source and its published
terms. That binds `G-A3-DZS`, `P3-DZS`, `G-A3-DIP`, `P3-DIP`, `P3-CATALOG` and
`P8-META`.

The durable record is
`notes/reports/g-a3-data-rights-determination-2026-08-05.md`.

## P2-SPINE-FINALE closeout

- `H-G-A2B-FINALE-001` is the only delivery targeting this packet. It was
  acknowledged and **consumed with an exact disposition and evidence before the
  packet claim** and before the first substantive edit. Its `P6-CONTINUITY`
  delivery is `before_close` and correctly remains `pending`.
  `H-P1C-INTEGRITY-002` remains `pending` for `P2-TERMS`, `H-G-A2D-005` for
  `WE-C18`, and `H-P2-SPINE-V-001` and `H-P2-SPINE-V-002` for `P2-TERMS`,
  `WD-C17` and `P5-ROUTES`. None was consumed here.
- `chapter-spine.json` now carries the ratified finale unit
  `18-vase-prvo-istrazivanje` with 12 aspects, 12 terms, 17 prerequisites and 12
  exclusions, faithful to the accepted draft with nothing added or omitted, and
  naming its gate `G-A2b-FINALE`, its ratification date and its decision record.
  Its deterministic state is
  `spine:sha256-27e5c37481e84cefed4dde818b6d5ed13727faae56e917747916bf3ff2e93efb`.
- **All nineteen spines are now ratified and none remains unratified.** The
  three architecture consumers count them and agree on 19 of 19 with their
  accepted states unchanged; no snapshot assertion was reintroduced.
- **Chapter 18's whole-book cumulativeness is machine-checked, not asserted.**
  The prerequisite list and the ratification-order condition in
  `scripts/check-chapter-spines.py` both name all seventeen numbered chapters,
  so the finale could not be ratified before any earlier unit. The preface is
  deliberately excluded from the list with the recorded reason that it is the
  reader contract rather than content a later unit depends on.
- **The amended new-method boundary is now enforceable before any finale prose
  exists.** The two limits are written as exclusions 2 and 3 and carry the
  literal markers `popisa izvan opsega iz predgovora` and `u cijelosti
  objašnjena ondje gdje se pojavljuje`; removing either returns exit 1. This
  packet is the first of the two named enforcers, and `P6-CONTINUITY` remains
  the second and audits the finished book. One drafted word order in exclusion 3
  was adjusted from *u cijelosti je objašnjena* to *mora biti u cijelosti
  objašnjena* so the exclusion literally carries the marker the same decision
  record tabulates; both conditions are unchanged, and the change is recorded
  rather than silent.
- Both deliberate fixtures kept their identifiers and returned exit 1. For unit
  18 they exercise **all three check kinds**: `ratified_without_decision` breaks
  the gate binding, and `part_i_visible_code_admitted` breaks the exclusion
  marker, the load-bearing term **and** the ratification-order rule, because it
  un-ratifies Chapters 5 and 7, which the finale names as prerequisites. That is
  a fuller per-unit coverage than Chapters 13, 14, 15 and 17 received, whose
  order rules that fixture does not reach. No fixture was added, removed or
  renamed.
- The approved one-block Chapter 18 definition increase was deliberately **not**
  implemented: adding a `#def-` block edits chapter prose, and
  `H-P1C-INTEGRITY-002` freezes the 46 live definitions, the concept ledger and
  the generated graph until `P2-TERMS` retires that debt. Chapter 18 still
  carries zero live blocks and the total remains 46. `H-P2-SPINE-FINALE-001`
  carries the approved map and the eleven rejected blocks to `P2-TERMS` and
  `WE-C18` exactly as `H-P2-SPINE-V-001` did for Chapter 17.
- **Two governed items closed and one did not, on purpose.**
  `R04-SPINE-FINALE` and `R04-C18-definitions` are `accepted`.
  `R04-C18-whole-prerequisites` was **not** closed and stays `ratified`: its
  acceptance test requires that metadata, prose, routes and exercises do not
  suggest the capstone is standalone, and the live `.chapter-meta` row at
  `chapters/18-vase-prvo-istrazivanje.qmd:110` still reads *pogl. 2, 6 i 16*,
  which is narrower than the ratified list. This packet may not edit chapter
  prose and published no route, so closing the item would have asserted a state
  that did not happen. `H-P2-SPINE-FINALE-002` carries the metadata half to
  `WE-C18` and the route half to `P5-ROUTES`. Leaving it open does not change
  when parent `R04` can close, because `R04-ROUTES-two-track-map` is already a
  required child owned by `P5-ROUTES` in Phase 5.
- Both 2026-08-05 author amendments hold. This packet makes **no
  independent-review claim** anywhere, and claims **no rights-holder
  permission** for any source and selects no data package. The acceptance test
  of `R17-C18-two-pass` was not amended and that item was not touched.
- No `#def-` block, concept-graph edge, chapter or appendix prose, chapter
  stage, terminology, identity brief, data package, route, render, generated
  artifact or external authority changed. All 19 units remain `draft`.

The durable evidence is `notes/reports/p2-spine-finale-2026-08-05.md`.

## G-A2b-FINALE closeout

- No handoff targets `G-A2b-FINALE`; the complete ledger was read before the
  first substantive edit, so there was no incoming delivery to acknowledge or
  consume. `H-G-A2D-005` remains `pending` for `WE-C18` and carries the dated
  privacy policy this spine writes in as an obligation, `H-P1C-INTEGRITY-002`
  remains `pending` for `P2-TERMS`, and `H-P2-SPINE-V-001` and
  `H-P2-SPINE-V-002` remain `pending` for `P2-TERMS`, `WD-C17` and `P5-ROUTES`.
  This gate consumes none of them.
- The complete finale contract, the Chapter 18 spine and the definition
  hierarchy were drafted first, and the gate then closed against that drafted
  state. Author and editor Luka Sikic accepted it on 2026-08-05.
- The finale carries one arc and no more: from the whole book to one evidence
  package another person can check without talking to its author. Chapter 18
  assembles rather than introduces, and the book's estimation-first standard
  holds to the last page — estimate, interval and substantive magnitude lead the
  conclusion, and no threshold decides either the main finding or its comparison
  with the alternative.
- **This is the one gate where the recorded intent amends the register's
  recommended default, and the disposition is recorded as `accepted_as_amended`
  rather than `accepted_as_recommended`.** The default forbids any new method in
  the capstone. The author amended it: Chapter 18 **may** introduce a technique
  the worked case genuinely requires, under three exact limits — (1) never a
  method on the preface's out-of-scope list, meaning time series, factor
  analysis and psychometrics, multilevel models, the mathematics of machine
  learning, or full Bayesian inference; (2) fully explained where it appears and
  self-contained; (3) no forward dependency on anything no earlier ratified
  spine was asked to supply. The author's recorded reason for the limits is that
  an unbounded new method would reopen the scope promise the preface makes; the
  amendment itself exists so the capstone stays real research rather than a case
  truncated to fit a method list.
- The three limits are written as spine exclusions 2 and 3 with literal
  deterministic markers, not left as contract prose. **`P2-SPINE-FINALE` and
  `P6-CONTINUITY` are both named as enforcing them**: `P2-SPINE-FINALE` makes
  the boundary machine-checkable before any finale prose exists, and
  `P6-CONTINUITY` audits the finished book against it. `WE-C18` is bound through
  the ratified spine exclusion rather than a duplicate handoff delivery.
- The amendment and the ratified register are reconciled explicitly. The
  acceptance test of `R17-C18-two-pass` requires the empirical transfer to
  introduce no method, and Chapter 18's worked case is its main guided study,
  because the whole chapter body is one extended worked example. The permission
  therefore lands in the main study and the transfer stays method-free, written
  as exclusion 4, while D13 keeps the main study explanatory as exclusion 5.
  Extending the permission to the transfer would require amending that item's
  acceptance test; **this gate deliberately did not, and did not touch the
  item.**
- `R04-C18-whole-prerequisites` is settled: Chapter 18 requires all seventeen
  numbered chapters, written both as a prerequisite list and as a
  ratification-order condition, so the finale cannot be ratified before any
  earlier unit. Each prerequisite carries one named obligation. The preface is
  deliberately excluded with a recorded reason — it is the reader contract
  rather than content a later unit depends on, and no ratified spine in the book
  names it as a prerequisite. Chapter 18's existing `.chapter-meta` row still
  names a narrower prerequisite and is recorded as a `WE-C18` obligation; this
  gate changed no prose.
- `R04-C18-definitions` is settled with one explicit disposition. Chapter 18
  currently carries zero blocks and so falls below the ratified one-to-five
  band, and rises to exactly one: `paket dokaza`, the only object the finale
  creates rather than retrieves, whose contents are already fixed by the
  accepted lifecycle finale role and which five ratified register items name.
  Because no later chapter exists, the later-dependant rule was applied to the
  only downstream consumers that do — the generated glossary and concept graph,
  the Appendix F protocol, `P5-CLOSURE-18` and `P5-ROUTES` — and exactly one
  term passes it.
- Eleven further terms stay in prose under `.pojam` with a recorded reason each:
  the decision trail and reproducible workflow are already carried by Chapter
  12's approved `reproducibilnost` block, the confirmatory/exploratory
  distinction by its approved `analitička fleksibilnost` block, the dataset
  passport and transformation log are components inside the evidence package's
  own defining sentence, the sensitivity check, claim boundary and honest report
  are ratified mechanisms of the accepted architecture, and data minimisation
  and AI-use disclosure are rules of the dated D15 course policy owned by
  Appendix F, which `R24-C18-dated-policy` forbids presenting as timeless
  concepts.
- The net effect on the frozen set of 46 live definitions, with every earlier
  approved map, is 52: 46 + 3 (`G-A2b-I`) − 2 (`G-A2b-II`) + 0 (`G-A2b-III`)
  + 2 (`G-A2b-IV`) + 2 (`G-A2b-V`) + 1 here. This gate writes no block; the live
  count remains 46 and Chapter 18 still carries zero.
- Chapter 18 carries twelve aspects, twelve terms, seventeen prerequisites and
  twelve exclusions. The seventh communication thread lands here and nowhere
  else: the reader writes their own honest report to the ratified standard and
  then audits an assistant's report on the same analysis by the same measure.
- The exact exclusion markers, required load-bearing terms and
  ratification-order condition that `P2-SPINE-FINALE` must encode in
  `scripts/check-chapter-spines.py` are tabulated in the decision record.
- The draft matches the recorded author intent in every respect. Twelve
  alternatives were rejected, including keeping the unamended prohibition,
  admitting an unlimited technique, leaving the limits as prose, extending the
  permission to the transfer, stating the prerequisite without listing the
  chapters, including the preface as a prerequisite, adding no block under a
  band exception, four separate definition-block proposals, turning the main
  study predictive, and adding a central widget.
- Both 2026-08-05 author amendments were read before the decision and both hold.
  This spine makes no independent-review claim of any kind, and every finale
  term's canonical Croatian form remains a `G-A2c` decision and the author's own
  editorial responsibility. It claims no rights-holder permission for any source
  and selects no data package. Neither constraint was duplicated into a spine
  exclusion, because both durable records already name the exact packets they
  bind.
- `OA-G-A2B-FINALE-SPINE` is `done`, with a dated resolution that states the
  amendment; no external message was sent. `H-G-A2B-FINALE-001` carries the
  accepted spine, the amended method limits, the seventeen-unit prerequisite
  list and the one-block definition increase to `P2-SPINE-FINALE` at its
  `before_start` gate and to `P6-CONTINUITY` at its `before_close` gate.
- No chapter or appendix prose, registry, spine, terminology, `#def-` block,
  concept graph, identity brief, data package, route, render, generated artifact
  or external authority changed. All 19 units remain `draft` and 18 of 19 spines
  remain ratified.

The durable evidence is `notes/reports/g-a2b-finale-spine-decision-2026-08-05.md`.

## G-A2b-V closeout

- No handoff targets `G-A2b-V`; the complete ledger was read before the first
  substantive edit, so there was no incoming delivery to acknowledge or consume.
  `H-P0-REGISTER-004` remains `pending` for `P2-SPINE-V` and `P5-ROUTES`,
  `H-P1C-INTEGRITY-002` remains `pending` for `P2-TERMS`, and
  `H-P0-REGISTER-007` and `H-P0-REGISTER-008` remain `pending` for `WD-C17`.
  This gate decides what those packets must carry; it consumes none of them.
- The complete Part V contract, the five chapter spines and the definition
  hierarchy were drafted first, and the gate then closed against that drafted
  state. Author and editor Luka Sikic accepted it as drafted on 2026-08-05.
- Part V carries one arc and no more: from one table to one model to one deployed
  system. Chapter 13 shows how counting is done and what makes a denominator
  conditional, Chapters 14 and 15 read one and then several comparisons, Chapter
  16 reveals that all of it was already one model, and Chapter 17 puts that model
  into a decision about real people. The chapter order is unchanged under D03.
- **Chapter 16 is preserved as the summit and the synthesis payoff.** Chapters 14
  and 15 may prepare the general-model language but may not spend it, which is
  written into the part contract and as a binding exclusion in each of those two
  chapters. The book also stays estimation-first inside the model part: estimate,
  interval and substantive magnitude lead, and the name of a procedure comes
  after the difference rather than before it.
- **Chapter 13 is a ratified prerequisite of Chapter 17.** The conditional
  denominators and the contingency table read in Chapter 13 are what becomes the
  confusion table in Chapter 17, so fairness and classification may not be
  introduced before them. That settles the contradiction in `H-P0-REGISTER-004`
  in favour of the prerequisite: **the route changes, not the prerequisite.**
  `P5-ROUTES` must amend the advertised short critical-literacy route and may
  publish no route that sends a reader into Chapter 17 without Chapter 13, which
  is also Chapter 17's first spine exclusion.
- `R04-C17-prerequisites` is settled with seven named obligations: Chapter 2 for
  coding as measurement, Chapter 3 for base rates, Chapter 8 for corpus selection
  and the sampling-versus-splitting distinction, Chapter 10 for error kinds and
  the fallible reference label, Chapter 11 for error consequences and magnitude,
  Chapter 13 for conditional denominators and the contingency table, and Chapter
  16 for the model, prediction and prediction timing.
- Chapter 13 carries eleven aspects, eight terms, six prerequisites and seven
  exclusions; Chapter 14 nine, eight, five and seven; Chapter 15 nine, eight,
  four and seven; Chapter 16 twelve, eleven, seven and nine; Chapter 17 eleven,
  twelve, seven and ten. No prerequisite points at a later unit.
- Chapter 17's spine is explicitly subordinate to the ratified identity brief
  `c17` and does not repeat it: the brief owns the argument, its nine steps and
  the measurement-first text module, while the spine fixes what the chapter must
  carry as term, prerequisite and boundary. The brief was neither changed nor
  superseded, and its exclusion that the prerequisite metadata remains unresolved
  until `P2-SPINE-V` stays accurate — this gate decides them, `P2-SPINE-V` writes
  them.
- `R04-C17-definitions` is settled through that identity spine. Chapters 13, 14,
  15 and 16 keep their existing five, two, three and four blocks unchanged, all
  inside the ratified one-to-five band. Chapter 17, which currently has none and
  so falls below the band, rises to exactly two: `zabilježeni referentni ishod`,
  which `R24-C17-recorded-reference` requires as one consistent expression across
  prose, visual, caption and alt text and which Chapter 18's evidence package
  depends on, and `klasifikacijski prag`, which `R27-C17-18-transition` and the
  `c17` plant role hand to Chapter 18 together with the unequal error burden.
  Every other Chapter 17 term stays in prose under `.pojam`.
- Three blocks were considered and rejected with a recorded reason: the confusion
  table, because it is Chapter 13's contingency table with conditional
  denominators and a second record would create two sources of truth about one
  object and weaken the very prerequisite this gate ratifies; algorithmic
  fairness, because a defining sentence pushes toward the single-metric reduction
  the `c17` brief forbids; and overfitting with the training, validation and test
  split, because no later chapter depends on their formal definition and D13
  keeps the capstone's main study explanatory.
- The net effect on the frozen set of 46 live definitions, together with the maps
  already approved by earlier gates, is 51: 46 + 3 (`G-A2b-I`) − 2 (`G-A2b-II`)
  + 0 (`G-A2b-III`) + 2 (`G-A2b-IV`) + 2 here. This gate writes no block; the
  live count remains 46 and Chapter 17 still carries zero.
- The exact exclusion markers, required load-bearing terms and ratification-order
  conditions that `P2-SPINE-V` must encode in
  `scripts/check-chapter-spines.py` are tabulated in the decision record.
- The draft matches the recorded author intent in every respect. Ten alternatives
  were rejected, including opening Part V with regression, revealing the general
  model in Chapter 14 or 15, leaving Chapter 13 outside Chapter 17's
  prerequisites, amending the prerequisite instead of the route, three separate
  definition-block proposals for Chapter 17, a Chapter 16 estimand block,
  repeating the `c17` argument inside the spine, and introducing logistic
  regression as a fitted procedure.
- Both 2026-08-05 author amendments were read before the decision and both hold.
  This spine makes no independent-review claim of any kind, and every Part V
  canonical Croatian form remains a `G-A2c` decision and the author's own
  editorial responsibility. It claims no rights-holder permission for any source
  and selects no data package. Neither constraint was duplicated into a chapter
  spine exclusion, because both durable records already name the exact packets
  they bind and the spine registry does not own those obligations.
- `OA-G-A2B-V-SPINE` is `done`; no external message was sent. `H-G-A2B-V-001`
  carries the accepted spine, the two-block Chapter 17 definition increase and
  the route consequence to `P2-SPINE-V` at its `before_start` gate.
- No chapter or appendix prose, registry, spine, terminology, `#def-` block,
  concept graph, identity brief, data package, route, render, generated artifact
  or external authority changed. All 19 units remain `draft` and 13 of 19 spines
  remain ratified.

The durable evidence is `notes/reports/g-a2b-v-spine-decision-2026-08-05.md`.

## P2-SPINE-V closeout

- Exactly two deliveries target this packet and both were acknowledged before the
  first substantive edit. `H-G-A2B-V-001` was acknowledged and **consumed with an
  exact disposition and evidence before the packet claim**. `H-P0-REGISTER-004`
  was acknowledged before the first substantive edit and consumed at closeout
  **on the registry side only**; its `P5-ROUTES` delivery correctly remains
  `pending`. `H-P1C-INTEGRITY-002` remains `pending` for `P2-TERMS`, and
  `H-P0-REGISTER-007` and `H-P0-REGISTER-008` remain `pending` for `WD-C17`;
  none was consumed here.
- `chapter-spine.json` now carries five ratified Part V units:
  `13-kategoricki-podaci` with 11 aspects, 8 terms, 6 prerequisites and 7
  exclusions; `14-dvije-grupe` with 9, 8, 5 and 7; `15-vise-grupa` with 9, 8, 4
  and 7; `16-regresija` with 12, 11, 7 and 9; and `17-doba-algoritama` with 11,
  12, 7 and 10. Each is faithful to the accepted draft with nothing added or
  omitted, and each names its gate, date and decision record. Its deterministic
  state is
  `spine:sha256-de298deedf4b34b80bde1d39c048479b61e3f7b02b95eb9461e22dbb205fbd52`.
- No prerequisite points at a later unit, and the table → model → deployed-system
  arc is written both as prerequisites and as a ratification-order condition.
- **Chapter 13 is now a live, machine-checked prerequisite of Chapter 17.**
  Chapter 17's ratified prerequisites are Chapters 2, 3, 8, 10, 11, 13 and 16,
  and its first exclusion forbids both reading the chapter without Chapter 13 and
  any advertised route that reaches Chapter 17 without it. The order is locked
  twice over, as a prerequisite and as a ratification-order rule, so Chapter 17
  could not be ratified before Chapter 13. That discharges the registry half of
  `H-P0-REGISTER-004`. The route half was deliberately **not** claimed: this
  packet publishes and amends no route, and `H-P2-SPINE-V-002` carries the exact
  route obligation to `P5-ROUTES`.
- Chapter 16 is preserved as the summit. The discovery that the two-group
  difference, the multi-group comparison and regression are one model belongs to
  Chapter 16 and is written as a binding exclusion in Chapters 14 and 15, so the
  general-model language may be prepared but not spent. The D02 boundary is live
  in Chapter 14: the estimate is the same, but ordinary homoskedastic OLS
  uncertainty is not Welch uncertainty.
- The Chapter 17 spine is written as subordinate to the ratified identity brief
  `c17` as its second exclusion. The brief was neither changed nor superseded,
  and its exclusion that the Chapter 17 prerequisite metadata stays unresolved
  until `P2-SPINE-V` was accurate until now — the gate decided them, this packet
  wrote them.
- `scripts/check-chapter-spines.py` now enforces Part V's exact exclusion
  markers, required load-bearing terms and ratification order, and reports
  eighteen ratified and one unratified unit. Both deliberate fixtures kept their
  identifiers and returned exit 1. They prove the gate-binding, exclusion-marker
  and term checks for **all five** Part V units, but the ratification-order check
  **only for Chapter 16**, whose prerequisites include the Chapter 5 spine that
  `part_i_visible_code_admitted` un-ratifies; Chapters 13, 14, 15 and 17 have no
  prerequisite that fixture un-ratifies, so their order rules are not exercised.
  That is the same partial per-unit coverage already recorded for Parts III and
  IV. No fixture was added, removed or renamed.
- The approved two-block Chapter 17 definition increase was deliberately **not**
  implemented: adding a `#def-` block edits chapter prose, and
  `H-P1C-INTEGRITY-002` freezes the 46 live definitions, the concept ledger and
  the generated graph until `P2-TERMS` retires that debt. Chapter 17 still
  carries zero live blocks and the total remains 46. `H-P2-SPINE-V-001` carries
  the approved map, and the three explicitly rejected blocks, to `P2-TERMS` and
  `WD-C17` exactly as `H-P2-SPINE-IV-001` did for Chapter 12.
- **Two governed items closed differently, on purpose.** `R04-SPINE-V` and
  `R04-C17-prerequisites` are `accepted`; the latter's evidence states in the
  register itself which half is discharged here (the prerequisite metadata, live
  and machine-checked) and which half stays with `P5-ROUTES` (the advertised
  routes). `R04-C17-definitions` was **not** closed and stays `ratified`: its
  acceptance test requires a *terminologically reviewed* definition map, and
  under the 2026-08-05 amendment terminology review is wholly the author's own
  responsibility, taken at `G-A2c`, which has not yet run. Closing it here would
  have asserted a review that did not happen. `H-P2-SPINE-V-001` carries that
  closure obligation to `P2-TERMS`, the last Phase 2 packet able to close it
  before `P2-VERIFY` requires `R04` closed.
- The three architecture consumers count ratified spines and agree on **18 of
  19** with their accepted states unchanged; `conventions.json` was not touched
  and no snapshot assertion was reintroduced. The blocking structure lane passes
  with 19 chapters.
- Both 2026-08-05 author amendments hold. This packet makes **no
  independent-review claim** anywhere — that is precisely why
  `R04-C17-definitions` stayed open — and claims **no rights-holder permission**
  for any source and selects no data package; the Part V package and table
  selections are written as obligations of `G-A3-DIP`, `G-A3-ESS`, `G-A4-16`,
  `G-A4-17` and `G-A3-TEXT`.
- No `#def-` block, concept-graph edge, chapter or appendix prose, chapter stage,
  terminology, identity brief, data package, route, render, generated artifact or
  external authority changed. All 19 units remain `draft`.

The durable evidence is `notes/reports/p2-spine-v-2026-08-05.md`.

## P2-SPINE-IV closeout

- `H-G-A2B-IV-001` was acknowledged and consumed with an exact disposition and
  evidence before the packet claim and before the first substantive edit. It was
  the only handoff targeting this packet. `H-P1C-INTEGRITY-002` remains `pending`
  for `P2-TERMS`, and `H-P0-REGISTER-004` remains `pending` for `P2-SPINE-V` and
  `P5-ROUTES`; neither was consumed here.
- `chapter-spine.json` now carries three ratified Part IV units:
  `10-logika-testiranja` with 9 aspects, 8 terms, 3 prerequisites and 8
  exclusions; `11-velicina-ucinka-i-snaga` with 8, 7, 2 and 7; and
  `12-kriza-i-obnova` with 10, 10, 5 and 9. Each is faithful to the accepted
  draft and names its gate, date and decision record. Its deterministic state is
  `spine:sha256-d8fdbd4553d5cbf0b4d68b35a8b14d7eb8a3826cc84729125d50900add22a897`.
- No prerequisite points at a later unit, and the testing → magnitude → research
  system chain is written both as prerequisites and as a ratification-order
  condition, so Chapter 11 could not be ratified before Chapters 9 and 10, nor
  Chapter 12 before Chapters 4, 5, 9, 10 and 11.
- The mechanics never lead. Chapter 10's first exclusion states that magnitude
  and the consequences of error govern the reading of every test and that the
  testing-mechanics-first order is explicitly rejected. The decision record
  enumerates that clause second in prose but twice locates it in Chapter 10's
  *first* exclusion, so the written order follows the two explicit statements;
  the exclusion set itself is unchanged at eight clauses.
- Chapter 11 carries the `R04-C11-fixed-order` obligation as a binding exclusion:
  the worked example may not precede the wild-statistics and assistant sections.
  Chapter 12's spine is written as subordinate to the ratified identity brief
  `c12` and that subordination is its second exclusion; the brief was neither
  changed nor superseded, and the evidence-artifact selection stays with
  `G-A4-12` and `P3-EVIDENCE12`.
- `scripts/check-chapter-spines.py` now enforces the exact Part IV exclusion
  markers, required load-bearing terms and ratification order, and reports
  thirteen ratified and six unratified units. Both deliberate fixtures kept their
  identifiers and returned exit 1; together they prove the exclusion-marker and
  term checks for all three Part IV units and the ratification-order check for
  Chapters 10 and 12. Chapter 11's order rule is not exercised by either fixture,
  because its prerequisites stay ratified there — the same partial per-unit
  coverage already recorded for Part III. No fixture was added or renamed.
- The approved Chapter 12 definition increase was deliberately **not**
  implemented: adding a `#def-` block edits chapter prose, and
  `H-P1C-INTEGRITY-002` freezes the 46 live definitions, the concept ledger and
  the generated graph until `P2-TERMS` retires that debt. Chapter 12 still
  carries zero live blocks. `H-P2-SPINE-IV-001` carries the approved two-block
  map to `P2-TERMS` and `WC-C12` exactly as `H-P2-SPINE-I-001` did, so the frozen
  concept gate can accept it rather than treat it as drift.
- The three architecture consumers count ratified spines and agree on 13 of 19
  with their accepted states unchanged; no snapshot assertion was reintroduced.
  The blocking structure lane passes with 19 chapters.
- No `#def-` block, concept-graph edge, chapter or appendix prose, chapter stage,
  terminology, identity brief, data package, route, render, generated artifact or
  external authority changed. All 19 units remain `draft` and the live definition
  count remains 46.

The durable evidence is `notes/reports/p2-spine-iv-2026-08-04.md`.

## G-A2b-IV closeout

- No handoff targets `G-A2b-IV`; the complete ledger was read before the
  decision. `H-P1C-INTEGRITY-002` remains `pending` for `P2-TERMS` and freezes
  the live definitions, so this gate decides the definition map and writes no
  block.
- The complete Part IV contract, the three chapter spines and the definition
  hierarchy were drafted first, and the gate then closed against that drafted
  state. Author and editor Luka Sikic accepted it as drafted on 2026-08-04.
- Part IV carries three steps and no more: what a test can and cannot answer,
  then how large the effect is and what an error costs, then what the research
  system does to evidence. The chapter order is unchanged under D03, but the
  mechanics never lead — magnitude and the consequences of error govern the
  reading of every test, and the testing-mechanics-first order is explicitly
  rejected in the part contract and in Chapter 10's first exclusion.
- Significance testing is taught with its history and its abuses rather than as
  procedure: Chapter 10 builds a world without an effect by simulation before it
  names the null, introduces the asymmetry of the decision before any threshold,
  treats the threshold as a convention rather than a measure, and carries the ASA
  episode as its principal instructional case.
- Chapter 12 remains one evidence-led argument about the research system rather
  than a list of reforms. Its spine is explicitly subordinate to the ratified
  identity brief `c12` and does not repeat it: the brief owns the argument, its
  six required components and its evidence artifact, while the spine fixes what
  the chapter must carry as term, prerequisite and boundary.
- Chapter 10 carries nine aspects and eight terms and requires Chapters 7, 8 and
  9. Chapter 11 carries eight aspects and seven terms and requires Chapters 9 and
  10. Chapter 12 carries ten aspects, including the Part IV boundary and the
  reformed-practice contract that Chapter 13 begins to enact, and ten terms, and
  requires Chapters 4, 5, 9, 10 and 11. No prerequisite points at a later unit.
- `R04-C12-definitions` is settled through that identity spine. Chapters 10 and
  11 keep their existing four and three blocks unchanged. Chapter 12, which
  currently has none and so falls below the ratified one-to-five band, rises to
  exactly two: `analitička fleksibilnost`, on which Chapter 16's routine
  sensitivity obligation and Chapter 18's transformation log depend, and
  `reproducibilnost`, which Chapter 18 harvests as a complete trail from source
  to claim. Every other Chapter 12 term stays in prose under `.pojam`.
- The draft matches the recorded author intent in every respect. Eight
  alternatives were rejected, including opening with the mechanics, moving
  Chapter 11 ahead of Chapter 10, turning Chapter 12 into a reform survey,
  repeating the `c12` argument in the spine, giving every reform term a block,
  adding no block at all, defining p-hacking instead of analytic flexibility, and
  moving the ASA episode out of Chapter 10.
- `OA-G-A2B-IV-SPINE` is `done`; no external message was sent. `H-G-A2B-IV-001`
  carries the accepted spine and the two-block definition increase to
  `P2-SPINE-IV` at its `before_start` gate.
- No chapter or appendix prose, registry, spine, terminology, `#def-` block,
  concept graph, identity brief, data package, render, generated artifact or
  external authority changed. All 19 units remain `draft` and 10 of 19 spines
  remain ratified.

The durable evidence is `notes/reports/g-a2b-iv-spine-decision-2026-08-04.md`.

## P2-SPINE-III closeout

- `H-G-A2B-III-001` was acknowledged and consumed with an exact disposition and
  evidence before the packet claim and before the first substantive edit.
  `H-P0-REGISTER-008` remains `pending` for `WC-C08`, `WC-C09` and `WD-C17`; the
  Chapter 8 and Chapter 9 spines name it and its owning packets without settling
  it. `H-P1C-INTEGRITY-002` remains `pending` for `P2-TERMS`.
- `chapter-spine.json` now carries three ratified Part III units:
  `07-vjerojatnost` with 10 aspects, 8 terms, 2 prerequisites and 7 exclusions;
  `08-uzorkovanje` with 10, 12, 4 and 8; and `09-procjena` with 11, 9, 4 and 7.
  Each is faithful to the accepted draft and names its gate, date and decision
  record. Its deterministic state is
  `spine:sha256-465c3fe2a7a460853a1028439e39ce6420dd8d0b8cf248dfaf5017a6538f44b2`.
- No prerequisite points at a later unit, and the probability → sampling →
  estimation chain is written both as prerequisites and as a ratification-order
  condition, so Chapter 8 could not be ratified before Chapter 7, nor Chapter 9
  before Chapters 7 and 8.
- Chapter 8 carries the largest conceptual load of the part with twelve terms,
  and it alone introduces population, sample and sampling error, which Part I
  deferred to exactly this point. The ratified separation of probability sampling
  from training, validation and test splitting is written as a binding Chapter 8
  exclusion, beside the rule that a larger sample does not repair coverage,
  nonresponse or selection.
- All three chapters forbid assessed code production and invented or unsourced
  empirical material, and record sampling distributions, intervals, tests,
  models, full Bayesian inference and natural-language-processing methods as
  explicit deferrals.
- Part III's definition load is unchanged at five, three and one block, and the
  margin of error stays in prose, so no new forward constraint to `P2-TERMS` was
  needed and the live definition count remains 46.
- `scripts/check-chapter-spines.py` now enforces the exact Part III exclusions,
  required load-bearing terms and ratification order, and reports ten ratified
  and nine unratified units. Both deliberate fixtures kept their identifiers,
  returned exit 1, and together prove all three check kinds for Part III. The
  three architecture consumers agree on 10 of 19 with their accepted states
  unchanged, and the blocking structure lane passes with 19 chapters.
- No `#def-` block, concept-graph edge, chapter or appendix prose, chapter stage,
  terminology, data package, route, render, generated artifact or external
  authority changed. All 19 units remain `draft`.

The durable evidence is `notes/reports/p2-spine-iii-2026-08-04.md`.

## G-A2b-III closeout

- No handoff targets `G-A2b-III`; the complete ledger was read before the
  decision. `H-P0-REGISTER-008` remains `pending` for `WC-C08`, `WC-C09` and
  `WD-C17`: the Chapter 8 and Chapter 9 spines state its debt and name its
  owners, but the gate does not consume it. `H-P1C-INTEGRITY-002` remains
  `pending` for `P2-TERMS`.
- The complete Part III contract, the three chapter spines and the definition
  disposition were drafted first, and the gate then closed against that drafted
  state. Author and editor Luka Sikic accepted it as drafted on 2026-08-04.
- Part III keeps probability, then sampling, then estimation, and carries three
  steps and no more: what chance produces, how far a sample reaches, and what an
  estimate says together with its uncertainty. The whole part is organised around
  one question -- what generalisation can and cannot reach -- and each chapter
  answers one part of it.
- Chapter 8 is preserved explicitly as the book's pedagogical hinge. It is the
  crossing from describing the data in hand to claiming something about a
  population that was never observed, it carries the largest share of the part's
  conceptual load, and it alone formally introduces population, sample and
  sampling error, which Part I deferred to exactly this point.
- Chapter 3's planted poll-reading and margin-of-error debts are settled in
  Chapters 8 and 9. Aspects 8.8 and 9.10 name `H-P0-REGISTER-008` and its owning
  packets, so the debt is stated in the spine while the handoff stays pending.
- The ratified separation between probability sampling for population
  generalisation and training, validation and test separation binds the whole
  part. Simulation stays ahead of formalism and no assessed task requires code
  production.
- Chapter 7 carries ten aspects and eight terms and requires Chapters 3 and 4.
  Chapter 8 carries ten aspects and twelve terms and requires Chapters 2, 3, 4
  and 7. Chapter 9 carries eleven aspects including the Part III boundary and
  nine terms and requires Chapters 3, 4, 7 and 8. No prerequisite points at a
  later unit.
- Part III's definition load is unchanged: Chapter 7 keeps its five blocks,
  Chapter 8 its three and Chapter 9 its one, all inside the ratified one-to-five
  band. The margin of error stays deliberately in prose, where Chapter 8 already
  names it; a formal block would duplicate the confidence interval with no later
  chapter depending on it.
- Six alternatives were rejected, including putting sampling before probability,
  folding estimation into Chapter 8, defining the margin of error as a block,
  settling the Chapter 3 debt inside the spine, introducing complex-survey
  variance estimation, and introducing Bayesian credible intervals.
- `OA-G-A2B-III-SPINE` is `done`; no external message was sent.
  `H-G-A2B-III-001` carries the accepted spine to `P2-SPINE-III` at its
  `before_start` gate.
- No chapter or appendix prose, registry, spine, terminology, `#def-` block,
  concept graph, data package, render, generated artifact or external authority
  changed. All 19 units remain `draft` and 7 of 19 spines remain ratified.

The durable evidence is `notes/reports/g-a2b-iii-spine-decision-2026-08-04.md`.

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
- The ratified Part IV spine settles `R04-C12-definitions`: Chapters 10 and 11
  keep their four and three blocks, and Chapter 12 rises from zero to exactly two
  — `analitička fleksibilnost` and `reproducibilnost`, each with a named later
  dependant in Chapters 16 and 18 — but neither was written, because the concept
  gate is frozen until `P2-TERMS`. `P2-TERMS` must expect them, `WC-C12` must add
  exactly those two and no others and may define no term the spine left in prose
  under `.pojam`, and `WC-C10` and `WC-C11` must leave their blocks unchanged.
- The ratified Part V spine settles `R04-C17-definitions`: Chapters 13 to 16 keep
  their five, two, three and four blocks, and Chapter 17 rises from zero to
  exactly two — `zabilježeni referentni ishod` and `klasifikacijski prag`, each
  with a named later dependant in Chapter 18 — but neither was written, because
  the concept gate is frozen until `P2-TERMS`. `P2-SPINE-V` carried that map
  forward in `H-P2-SPINE-V-001` rather than implementing it; `WD-C17` must add
  exactly those two and no others, may define no term the spine left in prose
  under `.pojam`, may not reopen the three rejected blocks — the confusion table,
  algorithmic fairness, and overfitting with the train/validation/test split —
  and `WD-C13` to `WD-C16` must leave their blocks unchanged. `P2-TERMS` also
  owns the closure of `R04-C17-definitions`, which `P2-SPINE-V` deliberately left
  at `ratified` because that item's acceptance test requires a terminologically
  reviewed map and `G-A2c` had not yet run.
- The ratified Part V spine settles `R04-C17-prerequisites`: Chapter 17 requires
  Chapters 2, 3, 8, 10, 11, 13 and 16, and `P2-SPINE-V` made that live in the
  registry. Because Chapter 13 supplies the conditional denominators and the
  contingency table that become Chapter 17's confusion table, `P5-ROUTES` must
  amend the advertised short critical-literacy route and may publish no route
  that reaches Chapter 17 without Chapter 13. `H-P0-REGISTER-004` is consumed on
  the registry side by `P2-SPINE-V` and remains `pending` on the route side for
  `P5-ROUTES`, which `H-P2-SPINE-V-002` also carries.
- The ratified finale spine settles `R04-C18-definitions`: Chapter 18 rises from
  zero to exactly one block, `paket dokaza`, but it was not written, because the
  concept gate is frozen until `P2-TERMS`. `P2-SPINE-FINALE` carried that map
  forward in `H-P2-SPINE-FINALE-001` rather than implementing it; `WE-C18` must
  add exactly that one block and no others, may define no term the spine left in
  prose under `.pojam`, and may not reopen the eleven rejected blocks.
  `P2-TERMS` must expect a Chapter 18 that carries one block instead of none,
  and fixes its canonical Croatian form only after `G-A2c`.
- The ratified finale spine settles `R04-C18-whole-prerequisites`: Chapter 18
  requires all seventeen numbered chapters, as both a prerequisite list and a
  ratification-order condition, and `P2-SPINE-FINALE` made both live and
  machine-checked. The register item itself stays **open** at `ratified`,
  because its acceptance test also names metadata, prose, routes and exercises:
  `WE-C18` must reconcile the chapter's existing `.chapter-meta` row, which
  still names only chapters 2, 6 and 16, and `P5-ROUTES` may publish no route,
  map or syllabus projection that enters Chapter 18 without the whole book.
  `H-P2-SPINE-FINALE-002` carries both halves and neither packet may close the
  item until both are true of the live source.
- The amended new-method boundary binds two named packets. `P2-SPINE-FINALE`
  has made the limits machine-checkable through the exact exclusion markers
  `popisa izvan opsega iz predgovora` and `u cijelosti objašnjena ondje gdje se
  pojavljuje`, and removing either now fails the deterministic check.
  `P6-CONTINUITY` must still audit the finished book against them and report any
  technique that entered the capstone without a self-contained explanation at
  its point of appearance or with a dependency no earlier ratified spine
  supplies. Neither may weaken the limits, and neither may extend the permission
  to the empirical transfer, which `R17-C18-two-pass` keeps method-free.
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
- `UCBAdmissions` and `anscombe` may not be copied into `data/` by any packet on
  current evidence. `P3-EXISTING` searched for dataset-specific redistribution
  terms and found only the package-level `Part of R 4.6.0` marker, with both
  documented origins being third-party copyrighted works. `WA-C01` has consumed
  that constraint: Berkeley remains a cited historical case, no local
  `UCBAdmissions` computation survives, and every mandatory task uses
  `populacija_medija`. `WB-C05`, `WB-C06` and `P5-A` must likewise keep the two
  sets optional and send every mandatory task to the recorded licence-clean
  fallback. `H-P3-EXISTING-001` carries their pending deliveries, and neither
  item can close without an author decision.
- Every generated snapshot is now checksummed in `data/katalog.yml`. Any packet
  that changes an aggregate value must rerun `scripts/build-data-snapshots.R`
  and update the recorded checksums, and none may round a value in the file to
  make a print table tidier — the `rounded_mean` fixture exists to catch that.
  `WB-C04`, `WC-C09` and `WC-C11` must build their print presets from the
  aggregate file, and one of them must carry the task that reproduces an
  aggregate row so `P5-C` can close `R32-CATALOG-paired-views`.
- `scripts/check-katalog.py` and `scripts/check-data-fixtures.py` are **not**
  blocking CI steps. `scripts/check-data-integrity.R` is, so the data-level
  rules run in CI, but a catalogue defect, a checksum mismatch or an undeclared
  consumer would pass CI today. `P7-CLEAN-BUILD` must wire both into the
  blocking ladder, together with the terminology checker that `H-P2-DOCS-003`
  already carries there.

## WA-C01 closeout — Chapter 1 vertical slice

- `WA-C01` is accepted on source SHA-256
  `e16f109d399c820d65080b9da38f984aa3d68b195d73d5a30d54140ee2f7d946`.
  The complete evidence record is
  `notes/reports/wa-c01-2026-08-06.md`.
- `H-P2-SPINE-I-001`, `H-P2-TERMS-002` and `H-P3-EXISTING-001` were
  acknowledged before substantive editing and consumed at `before_close` with
  exact dispositions. No delivery for another packet was touched.
- Chapter 1 now carries exactly `#def-jedinica-analize` and
  `#def-simpsonov-paradoks`. The canonical ledger and terminology register
  reconcile at 48 live definitions; the regenerated graph has 48 nodes and 552
  edges, zero ledger debt and a fresh-state result.
- No `UCBAdmissions` file was created, copied or promoted. The final source
  contains no local UCB computation. The mandatory example, AI task and
  assessed calculations use the promoted `populacija_medija` aggregate.
- The exact numerical audit returns five rows and 50.000 records; portal has
  15.101 records, 3.514 willing to pay and share 0,232699821203894; tisak has
  4.855, 1.289 and 0,265499485066941; social media has 13.378, 2.841 and
  0,212363582000299; the last two shares differ by 5,31359030666423 percentage
  points.
- Final HTML, PDF and wrapper-built DOCX renders each exited 0. Their artifact
  sizes and SHA-256 hashes are recorded in the packet report; generated build
  products were restored and are not packet changes.
- Six independent read-only critics reviewed the initial source and then the
  same final hash. Methods, skepticism, pedagogy, evidence, style and structure
  each score 5/5 with zero remaining fatal, major or minor finding. The durable
  synthesis is `notes/reports/wa-c01-six-critic-synthesis-2026-08-06.md`.
- Chapter 1 remains `draft`; `R24-C01-modern-AI-history` and
  `R31-C01-Berkeley` remain `ratified`. Only the named author/editor may accept
  their synthesis and advance the chapter through `C01`.
- `C01` is next. `WA-C02` and every later packet remain unstarted. Push, merge,
  tag, archive and deployment remain unauthorised.

## C01 closeout

- No handoff targets `C01`, and nothing targeting another packet was consumed.
  The author replied exactly: `C01 accepted for
  3b1706d42ea1bc56f0a909d895b04641872e85fd on 2026-08-06.`
- The final Chapter 1 source commit is
  `3b1706d42ea1bc56f0a909d895b04641872e85fd`; its Git blob is
  `99313b22f7174e0b6cef284d9c4972f852ea7914` and its SHA-256 is
  `e16f109d399c820d65080b9da38f984aa3d68b195d73d5a30d54140ee2f7d946`.
  The chapter has not changed after that commit.
- All six final critic reports and the synthesis address that exact material
  state. Every perspective scores 5/5, with zero fatal, major or minor finding.
  `notes/reports/c01-acceptance-package-2026-08-06.md` records the final commit,
  reports, synthesis, exact author reply and applied ledger disposition.
- Only `R24-C01-modern-AI-history` and `R31-C01-Berkeley` advance from
  `ratified` to `accepted`, each with source-specific evidence. No other atomic
  item changes status.
- Only `01-zasto-statistika` advances from `draft` to `coauthor_review`; the
  ledger explicitly says that this records acceptance and does not claim that
  the author read the chapter. This is not a `final` disposition.
- `OA-C01-ACCEPTANCE` is `done` from the in-thread reply. No external message
  was sent. C01 creates no outgoing handoff because its accepted source and
  disposition are already direct prerequisites in the canonical register and
  ledger.
- No chapter prose, data, bibliography, terminology, spine, concept graph or
  render changed in C01. `WA-C02` is next and was not started in this thread;
  push, merge, tag, archive and deployment remain unauthorised.

## WA-C02 closeout — Chapter 2 vertical slice

- `WA-C02` is accepted on source SHA-256
  `c9f902cbe83ae6e17d743e5856252a2b4a62a409d45af084429a7af9089fcf55`.
  The complete evidence record is
  `notes/reports/wa-c02-2026-08-06.md`.
- No incoming handoff targets `WA-C02`, and nothing targeting another packet
  was consumed. The packet records no outgoing handoff because its final
  source, W02 reconciliation, panel and decision dependency are already direct
  canonical evidence for `C02`.
- Chapter 2 now makes units, eligibility, exclusions, filters, target-population
  change, missingness and coding-as-measurement explicit. The survey-reading
  card and three-part uncertainty budget keep construct, score and sampling
  uncertainty separate; the causal and quasi-experimental boundaries remain
  modest.
- All four Chapter 2 definition blocks are byte-identical to the preceding
  source and no definition was added. The shared concept ledger and concept
  graph are unchanged; the concept check reports 48 definitions, zero ledger
  debt and a fresh graph.
- `data/widgets.json` changes only W02's exact instructions and OJS source hash
  `fd8b972b2943777aea2f3e8da74bfbafb55eb6e122a3b5a4243d77bf44a46f82`.
  Widget parity passes for all 17 pairs. The chapter adds no second central
  widget or new method.
- Independent calculations reproduce all score, item-rest and widget values.
  Final HTML, PDF and wrapper-built DOCX renders each exited 0; artifact sizes,
  SHA-256 hashes and verification details are recorded in the packet report.
  Generated build products were restored and are not packet changes.
- Six independent read-only critics reviewed the same final hash. Methods,
  skepticism, pedagogy, evidence, style and structure each score 5/5 with zero
  fatal, major or minor finding. The durable synthesis is
  `notes/reports/wa-c02-six-critic-synthesis-2026-08-06.md`.
- No `digikat_mediji`, `rdp_potpore` or `bdp_dugi_niz` data entered the source;
  no rights-holder permission is claimed, and `UCBAdmissions` was not copied or
  redistributed.
- Chapter 2 remains `draft`. `R11-C02-units-eligibility` and
  `R13-C02-coding-measurement` remain `ratified` pending the author-only `C02`
  decision; the four applicable P1A-C02 items retain their earlier `accepted`
  state. The acceptance package is
  `notes/reports/c02-acceptance-package-2026-08-06.md`.
- `C02` is next but is not accepted. `G-A4-03` and every later packet remain
  unstarted. Push, merge, tag, archive and deployment remain unauthorised.

## C02 closeout

- No handoff targets `C02`, and nothing targeting another packet was consumed.
  The author replied exactly: `C02 accepted for
  0552e4a35052f7f7736b267a0f367f30df02d9c7 on 2026-08-06.`
- The final Chapter 2 source commit is
  `0552e4a35052f7f7736b267a0f367f30df02d9c7`; its Git blob is
  `492b495c636d4f9826d9aa70b30ac1e297ebacba` and its SHA-256 is
  `c9f902cbe83ae6e17d743e5856252a2b4a62a409d45af084429a7af9089fcf55`.
  The chapter has not changed after that commit.
- All six final critic reports and the synthesis address that exact material
  state. Every perspective scores 5/5, with zero fatal, major or minor finding.
  `notes/reports/c02-acceptance-package-2026-08-06.md` records the final commit,
  reports, synthesis, exact author reply and applied ledger disposition.
- Only `R11-C02-units-eligibility` and `R13-C02-coding-measurement` advance from
  `ratified` to `accepted`. The four P1A-C02 methods items were already
  `accepted` and remain so; the earlier wording that counted all six as
  ratified has been corrected without changing the accepted source or scope.
- Only `02-mjerenje-i-dizajn` advances from `draft` to `coauthor_review`; the
  ledger explicitly says that this records acceptance and does not claim that
  the author read the chapter. This is not a `final` disposition.
- `OA-C02-ACCEPTANCE` is `done` from the in-thread reply. No external message
  was sent. C02 creates no outgoing handoff because its accepted source and
  disposition are already direct prerequisites in the canonical register and
  ledger.
- `notes/reports/g-a4-03-decision-package-2026-08-06.md` now presents one
  bounded Tier F decision: evidence, recommended DIP public-claim audit, DZS or
  generated offline fallback, alternatives, exclusions, blocked dependencies
  and exact reply. The stale novice-pilot dependency is removed from
  `OA-G-A4-03-BRIEF`; the pilot remains truthfully `descoped` with no result
  claimed.
- No chapter prose, data, bibliography, terminology, spine, concept graph or
  render changed in C02. `G-A4-03` is next but is neither accepted nor claimed;
  `WA-C03` and every later packet remain unstarted. Push, merge, tag, archive
  and deployment remain unauthorised.

## G-A4-03 closeout

- No handoff targets `G-A4-03`, and nothing targeting another packet was
  consumed. The author replied exactly: `G-A4-03 accepted as recommended for
  91a92347d93073516f6b77c3652c1f2baa5c9bee on 2026-08-06.` The cited commit is
  the local C02 closeout state requested by the decision package.
- The accepted Tier F disposition uses one portal-mediated audit of the
  official DIP report for the 2024 Croatian parliamentary election. It names
  2.216.763 approached voters over 3.558.089 eligible voters at processed
  polling places and the published 62,30 %, with the exact source and the
  5 August 2026 inspection date required in Chapter 3.
- The disposition keeps all five official counts distinct. Valid 2.154.733 plus
  invalid 60.476 gives 2.215.209 voters according to ballots, which is 1.554
  fewer than approached voters. List-support, individual, causal, ecological,
  predictive and out-of-source generalisation claims remain unavailable.
- `dip_2024` remains `portal-mediated`, `promoted: false`, with `files: []` and
  `checksum: null`. The book claims neither local DIP bytes, cross-edition
  portal parity nor rights-holder permission. The promoted DZS aggregate or
  governed generated data remains the mandatory offline fallback and does not
  become a second narrative pillar.
- The accepted outline adds exactly one Chapter 3 definition, `temeljna stopa`,
  and no other. The existing simulated-election margin-of-error explorer stays
  the only central widget and is neither formal margin-of-error derivation nor
  evidence for the DIP administrative table.
- `OA-G-A4-03-BRIEF` is `done`. Its earlier readiness
  `waiting_for_PartI_evidence_and_pilot` is explicitly retired rather than
  reinterpreted. C02 supplies the Part I evidence, while the 5 August author
  amendment descoped `P3-PILOT` without claiming any pilot result.
- The gate retrieved nothing, wrote no data file, promoted nothing and accepted
  no future Chapter 3 source. It creates no outgoing handoff because its
  disposition is WA-C03's direct prerequisite and the six existing deliveries
  already carry every source, definition, terminology and DZS constraint.
- `WA-C03` is next. `C03` and every later packet remain unstarted. Push, merge,
  tag, archive and deployment remain unauthorised.

## WA-C03 claim

- The packet is active under the accepted G-A4-03 disposition. Exactly two
  `before_start` deliveries are terminal before claim. `H-P0-REGISTER-007`
  confirms that the governed DIP package and author brief are complete, while
  `H-P3-DIP-001` fixes the portal-mediated numerator, denominator, aggregation,
  unavailable-claim and offline-fallback boundaries.
- Four `before_close` deliveries were acknowledged before the first
  substantive edit. `H-P2-SPINE-I-001` limits Chapter 3 to one new definition,
  `temeljna stopa`; `H-P2-TERMS-002` requires same-packet ledger and graph
  reconciliation; `H-P3-DZS-001` preserves the arrival unit; and
  `H-P3-DZS-004` keeps survey and administrative figures separate and the
  survey rounding residual truthful.
- No chapter, data file, shared registry or generated artifact has yet changed
  in WA-C03. The workflow validator must pass in this claimed state before the
  first substantive edit.

## WA-C03 closeout — Chapter 3 identity rewrite

- `WA-C03` is accepted on source SHA-256
  `11e949a5f4bfa3f762a6b3ad4f2f3e6a36333cdd2fbfae08103d2fcd8263bad5`.
  The complete evidence record is
  `notes/reports/wa-c03-2026-08-06.md`.
- The two `before_start` deliveries were already consumed before claim. The
  four `before_close` deliveries `H-P2-SPINE-I-001`, `H-P2-TERMS-002`,
  `H-P3-DZS-001` and `H-P3-DZS-004` are now consumed with source, registry,
  check and packet-report evidence.
- One portal-mediated audit of DIP's 2024 parliamentary turnout remains the
  sole public case. The chapter distinguishes the five official quantities,
  reproduces 62,30 %, reconciles the ballot sum at 2.215.209 and preserves the
  unexplained difference of 1.554 without turning it into evidence of error.
- The source adds exactly `#def-temeljna-stopa`. The checkout-local concept
  ledger and terminology live count now agree at 49 definitions; the generated
  graph has 49 nodes and 558 edges, with zero ledger debt and a fresh graph.
- No DZS tourism value entered the prose. Arrival is never recoded as a person,
  the administrative and survey figures are not combined, and the survey's
  ±1 rounding residual is not called a data error. The offline task uses the
  governed generated `populacija_medija` package with an explicit generated-
  person unit and a registered Chapter 3 consumer.
- The existing widget code was not edited and `data/widgets.json` is unchanged.
  Digital and print instructions now match the actions available in each
  format. Part I still contains no visible code and no task requires code
  production.
- Final HTML, PDF and wrapper-built DOCX renders exited 0 on the final material
  hash. Generated `docs/`, `_freeze/`, AI exports and Word output were restored
  and are not packet changes. The PDF emitted the existing implicit-div-closure
  warnings, while the blocking manuscript-integrity check remains required.
- Six independent read-only critics confirmed the same final hash. Methods,
  skepticism, pedagogy, evidence, style and structure each score 5/5 with zero
  fatal, major or minor finding. The durable synthesis is
  `notes/reports/wa-c03-six-critic-synthesis-2026-08-06.md`.
- The packet found no new future-relevant effect. C03 directly consumes the
  final source, reports and synthesis, so no duplicate handoff was created.
- Chapter 3 remains `draft`. Its nine governed content items remain `ratified`
  until the author-only `C03` decision. `C03` is next but is not accepted.
  Push, merge, tag, archive and deployment remain unauthorised.

## C03 package preparation record

- C03 was claimed only as an author-acceptance gate against WA-C03 commit
  `72f774a3b302e6beca14730ac82727be92f29be1`. The Chapter 3 Git blob is
  `5ecef6c96379af17e03c30e6facc5a191a670618`, and the working-file SHA-256 is
  `11e949a5f4bfa3f762a6b3ad4f2f3e6a36333cdd2fbfae08103d2fcd8263bad5`.
- The prepared `notes/reports/c03-acceptance-package-2026-08-06.md` cited the final commit,
  all six reports, the synthesis, the WA-C03 evidence record and the proposed
  ledger disposition. `OA-C03-ACCEPTANCE` was ready for author decision; no
  external message was sent.
- The recommended disposition was to accept the nine governed Chapter 3 items
  and advance only `03-kako-brojke-zavode` from `draft` to `coauthor_review`,
  explicitly without claiming that the author read the chapter and without
  calling it `final`.
- Before the author decision, no proposed disposition had been applied: the
  chapter ledger was unchanged, all nine items remained `ratified`, C03 was
  `in_progress`, and WA-PART was blocked. No chapter prose, data, citation,
  concept, widget or render changed while assembling the package.
- At that point, the only required action was the named author/editor's exact
  accept-or-revise reply. Push, merge, tag, archive and deployment remained
  unauthorised.

## C03 closeout

- No handoff targets `C03`, and nothing targeting another packet was consumed.
  The author replied exactly: `C03 accepted for
  72f774a3b302e6beca14730ac82727be92f29be1 on 2026-08-06.`
- The final Chapter 3 source commit is
  `72f774a3b302e6beca14730ac82727be92f29be1`; its Git blob is
  `5ecef6c96379af17e03c30e6facc5a191a670618` and its SHA-256 is
  `11e949a5f4bfa3f762a6b3ad4f2f3e6a36333cdd2fbfae08103d2fcd8263bad5`.
  The chapter has not changed after that commit.
- All six final critic reports and the synthesis address that exact material
  state. Every perspective scores 5/5, with zero fatal, major or minor finding.
  `notes/reports/c03-acceptance-package-2026-08-06.md` records the final commit,
  reports, synthesis, exact author reply and applied ledger disposition.
- Exactly nine governed Chapter 3 content items advance from `ratified` to
  `accepted`: `R07-C03-full-argument`, `R10-C03-base-rate`,
  `R12-C03-poll-literacy`, `R12-C03-margin-debt`,
  `R23-C03-no-R-production`, `R24-C03-synthetic-media`,
  `R24-C03-AI-provenance`, `R30-C03-slide-enumeration` and
  `R31-C03-public-case`. No other atomic item changes status.
- Only `03-kako-brojke-zavode` advances from `draft` to `coauthor_review`; the
  ledger explicitly says that this records acceptance and does not claim that
  the author read the chapter. This is not a `final` disposition.
- `OA-C03-ACCEPTANCE` is `done` from the in-thread reply. No external message
  was sent. C03 creates no outgoing handoff because its accepted source and
  disposition are already direct prerequisites in the canonical register and
  ledger.
- No chapter prose, data, bibliography, terminology, spine, concept graph,
  widget or render changed in C03. `WA-PART` is next and was not started in this
  thread; push, merge, tag, archive and deployment remain unauthorised.

## WA-PART claim

- The packet was claimed only after the canonical state was reconstructed from
  all four control files and the checkout-local conductor instructions.
  `C03` is accepted against WA-C03 commit
  `72f774a3b302e6beca14730ac82727be92f29be1`, the live Chapter 3 file is
  unchanged from that commit, and `03-kako-brojke-zavode` is at
  `coauthor_review` in the checkout-local chapter ledger.
- The complete handoff ledger contains **no delivery targeting `WA-PART`**.
  There is therefore no required `before_start` delivery to consume and no
  required `before_close` delivery to acknowledge. Nothing targeting another
  packet was touched.
- The packet owns only the four Part I and transition chapter sources, its
  two critic reports and continuity synthesis, its packet report, and the three
  control files. The write lock does not authorise `G-A3-DIGIKAT`, any later
  packet, or any push, merge, tag, archive or deployment action.
- The five governed items read before claim are `R08-SPINE-01-03`,
  `R24-PARTI-thesis`, `R24-LADDER-PartI`, `R27-C03-04-transition` and
  `R35-SELF-CHECK-I`. The packet will judge each against its own acceptance
  tests and will not close one by aggregation.
- `scripts/check-review-workflow.R` passed before claim with no active packet
  and `WA-PART` as the sole next-permitted packet. It must pass again in this
  claimed state before the first substantive edit.

## WA-PART closeout

- C03 was reverified against WA-C03 commit
  `72f774a3b302e6beca14730ac82727be92f29be1`; Chapter 3 remained unchanged and
  at `coauthor_review`, without a claim that the author read it.
- No handoff targets WA-PART. There was no `before_start` delivery to consume
  and no `before_close` delivery to acknowledge or dispose. Nothing targeting
  another packet was touched.
- The only chapter-source change is the bounded Chapter 4 bridge „Od izvora do
  sažetka” at source SHA-256
  `21a5f46b0cb1e04a0ef1f336c96f510ccd3a5ddfe448ecc6e7e150869462b3ab`.
  It turns skeptical reading into honest production while leaving joins,
  missingness, transformations and the full Chapter 4 rewrite to `WB-C04`.
- `R08-SPINE-01-03`, `R24-PARTI-thesis`, `R24-LADDER-PartI`,
  `R27-C03-04-transition` and `R35-SELF-CHECK-I` are accepted with separate,
  source-specific evidence. The DZS/DIP qualification is explicit: DIP carries
  the reader-facing official-data spine; DZS supplies a verified governance
  boundary, and no DZS recurrence is falsely claimed in Chapters 1–3.
- Independent `critic_voice` and `critic_arc` reviews of the final state found
  zero fatal and zero major issue and recommended closure without another
  prose edit. Their reports and synthesis are in the three WA-PART continuity
  reports; the packet record is `notes/reports/wa-part-2026-08-06.md`.
- Targeted HTML, PDF and DOCX renders exited 0. Architecture, spine,
  assessment, identity, terminology, style, citation, concept, manuscript,
  figure, catalogue, data, DZS, DIP, widget, parity, inventory, token and
  workflow checks pass. Tracked generated files refreshed by the render hook
  were restored to their clean pre-render state and are outside the packet.
- The handoff review declares no new future-relevant effect because the bridge
  is already a governed item and WA-PART is a direct prerequisite of `WB-C04`.
  Chapter stages and shared registries are unchanged. `G-A3-DIGIKAT` is the
  only next-permitted packet and was not started. Push, merge, tag, archive and
  deployment remain unauthorised.

## WC-C08 closeout — Chapter 8 vertical slice

- `WC-C08` is accepted at Chapter 8 SHA-256
  `9c21300575573d86b60120eb54ef3d4c37acb3edb4d2bf207163c3563daf0c04`.
  The complete evidence record is `notes/reports/wc-c08-2026-08-11.md`.
- The central repeated-SRS simulation remains intact and precedes
  formalisation. The corrected sample-size relation states that ten times
  larger `n` reduces standard error by `sqrt(10)` and halving it requires four
  times larger `n`.
- The mandatory weighted table is a separately labelled synthetic finite
  population of 16 units. Its six observed rows reproduce `3/6 = 50,0 %`
  without weights and `6/16 = 37,5 %` with inverse-inclusion weights; the text
  keeps 37,5 % as an estimate and denies that weights remove sampling error or
  all selection and measurement problems.
- Survey realism covers coverage, unequal inclusion, weights, calibration,
  nonresponse, self-selection, clustering, design effect and effective sample
  size. No task derives a variance formula or claims that the future Appendix
  D recovery route already exists.
- Corpus selection explicitly names speech, platform, date, language, speaker,
  unit, denominator and coverage. Population generalisation remains distinct
  from train/validation/test separation. The Chapter 3 reach-back separates
  coverage, nonresponse and sampling variability without inventing missing
  poll evidence.
- ESS remains optional, portal-mediated and unpromoted: Round 11 edition 3.0,
  `cntry == HR`, `vote`, analysis-specific valid-response denominators and
  default `anweight`, with a self-report warning and no local empirical result.
  `OA-G-A3-ESS-RIGHTS` remains open and bundling remains prohibited.
- Canonical `težina uzorkovanja`, `procjena s težinama` and `procjena bez
  težina` replace the two WC-C08 divergences. Only their two registry records
  were removed; the terminology check passes with five later divergences. The
  concept graph is regenerated and passes fresh at 47 nodes and 511 edges.
- Targeted HTML, approved-wrapper PDF and wrapper DOCX exited 0 at the final
  hash. Their SHA-256 values are respectively
  `39fd71b04beda68c26972258144377705e9cb18fc1ee7f97c14f17a3bf2eb1ca`,
  `dea7292681fa1d97146237bc1de82a630a592189fd54a8e1f58c6ff47cf549d3`
  and `1f50252ee6d2a2adae231bac873e0729b626807c8446958fed6d1975c1e2a5ef`.
  Generated outputs were restored.
- Six independent read-only critics confirmed the exact hash after all
  prefinal blockers were resolved. The final panel records zero fatal, zero
  major, 17 nonblocking minor and zero useful findings; none was silently
  edited after the panel.
- `H-P3-ESS-001` was consumed before start. `H-P0-REGISTER-008`,
  `H-G-A2C-002`, `H-P2-TERMS-003` and `H-P2-DOCS-001` are consumed at
  closeout with exact dispositions. No delivery for another packet was used.
- No new outgoing handoff is created: the reader-facing ESS catalogue debt is
  already `H-P3-CATALOG-002` for `P5-C`, the rights boundary already has
  `OA-G-A3-ESS-RIGHTS`, and later consumer boundaries already have
  `H-P3-ESS-001`.
- `R12-C08-survey-realism`, `R12-C08-weighted-table`,
  `R13-C08-corpus-selection` and `R35-REACHBACK-08` materially pass but remain
  `ratified`; Chapter 8 remains `draft`. Chapter 6 is unchanged and `draft`.
  C08 is next but has not been claimed or accepted, and no author reading is
  claimed. Push, merge, tag, archive, deployment and publication remain
  unauthorised.

## Author amendment 2026-08-12 — C08 through C10

- `A-THREAD-C08-C10-2026-08-12` is a new, distinct author decision recorded
  before C08. For this thread only it authorises the strict chain `C08`,
  `WC-C09`, `C09`, `WC-C10`, `C10` instead of the usual stop after one packet.
- Every packet still receives its own claim, single write lock, evidence,
  handoff disposition, workflow checks, closeout and bounded commit before the
  next packet is claimed. No evidence or lock crosses a packet boundary.
- The amendment does not supersede `A-THREAD-C07-C09-2026-08-11`.
  `H-WC-C07-THREAD-SEQUENCE-001` still has its pending `before_close` delivery
  for C08 and `before_start` delivery for WC-C09; both remain mandatory at
  their original gates.
- C08, C09 and C10 each still require a separate exact dated author reply tied
  to the final chapter source commit. The 5 August standing delegation cannot
  replace any of them, and no packet may record that the author read a chapter.
- All packet prerequisites, D01, the Part III/IV spines, ESS and official-data
  claim boundaries, Chapter 6's draft status and the stated stop conditions
  remain unchanged. The durable decision record is
  `notes/reports/c08-c10-thread-amendment-2026-08-12.md`.

## C08 claim and closeout

- C08 was claimed from the clean control-only amendment commit
  `3a8f0510d225c3f5874ee7f141a41725bb1626ae` only after the workflow validator
  confirmed no active packet and C08 uniquely next. The final Chapter 8 source
  remained byte-identical to WC-C08 commit
  `39db651decc561fb082facb7feeebc40103eace8`, Git blob
  `d3fedbd809aec0ceae9a0480b7b772b99546c44a` and SHA-256
  `9c21300575573d86b60120eb54ef3d4c37acb3edb4d2bf207163c3563daf0c04`.
- The named author replied exactly: `C08 accepted for
  39db651decc561fb082facb7feeebc40103eace8 on 2026-08-12.` The standing 5
  August delegation was not substituted, and no author reading is claimed.
- All six final critic reports and the synthesis address that exact material
  state. The panel records zero fatal, zero major, seventeen nonblocking minor
  and zero useful findings. The complete acceptance record is
  `notes/reports/c08-acceptance-package-2026-08-12.md`.
- Exactly `R12-C08-survey-realism`, `R12-C08-weighted-table`,
  `R13-C08-corpus-selection` and `R35-REACHBACK-08` advance from `ratified` to
  `accepted`. Only `08-uzorkovanje` advances from `draft` to
  `coauthor_review`; the ledger says explicitly that this is not `final` and
  does not mean that the author read the chapter.
- ESS remains optional, portal-mediated and unpromoted. Chapter 8's required
  weighted comparison remains the synthetic `3/6 = 50,0 %` against
  `6/16 = 37,5 %` table. No ESS microdata, empirical result, local checksum,
  parity promise or redistribution permission is claimed;
  `OA-G-A3-ESS-RIGHTS` stays open and bundling prohibited.
- The C08 delivery in `H-WC-C07-THREAD-SEQUENCE-001` is consumed only after the
  exact reply. Its distinct `WC-C09` `before_start` delivery remains pending.
  C08 creates no outgoing handoff because all future ESS and catalogue effects
  already have one owner.
- Chapter 6 remains unchanged and `draft`; `H-WB-PART-001` remains pending for
  `P6-PANELS`. C08 changes no chapter prose, data, bibliography, terminology,
  concept, widget, figure, render or generated artifact.
- The workflow validator passed at claim. At closeout it and all three required
  fail-closed fixtures pass. `WC-C09` is uniquely next but was not claimed
  inside C08. Push, merge, tag, archive, deployment and publication remain
  unauthorised.

## WC-C09 claim — Chapter 9 vertical slice

- WC-C09 was claimed from clean commit
  `b0be3b01570eb5502db041417d9d8d386a4b17c9` after the workflow validator
  confirmed no active packet, accepted C08 and WC-C09 alone at sequence 102.
  Exactly one write lock is active; C09 and WC-C10 remain unclaimed.
- `H-WC-C07-THREAD-SEQUENCE-001` is consumed at `before_start`. It preserves
  the older thread decision through WC-C09 closeout while the distinct
  `A-THREAD-C08-C10-2026-08-12` decision carries the later C09–C10 sequence.
- `H-P0-REGISTER-008`, `H-P3-EXISTING-002` and `H-WB-C06-001` are acknowledged
  before the first substantive edit and remain pending for exact `before_close`
  dispositions. Their obligations are respectively the Chapter 3 interval
  debt, the governed aggregate print/task closure and exact w09 live/adapter
  random-generator equivalence with a fail-closed regression fixture.
- The governed Chapter 9 items are `R13-C09-coded-uncertainty`,
  `R23-C09-code-reading`, `R32-C09-static` and `R35-REACHBACK-09`.
  `R32-CATALOG-paired-views` is additionally closed here, rather than deferred
  again, under the 12 August author amendment. All remain `ratified` while the
  packet is active.
- The packet is bounded to the ratified G-A2b-III estimation spine, required
  parity support and evidence reports. Chapter 6 remains unchanged and
  deliberately `draft`; no author reading is claimed and no external or
  release action is authorised.

## WC-C09 closeout — Chapter 9 vertical slice

- The final Chapter 9 SHA-256 is
  `42c69be9eec5fa9dcfed853e95269d661ea8cf73c6ac7ddd9de431c88ae5b08f`.
  Coverage is experienced and counted before formalisation; `z*` is explained
  before the interval formula, and margin of error is an interval half-width
  restricted to sampling uncertainty.
- Interactive and static A/B and A/C comparisons share one seed-919 draw
  matrix and vary confidence level or sample size one at a time. Approved
  wrapper PDF and DOCX carry both pairs.
- The worked example uses a prespecified margin target of at most ten minutes,
  withdraws a population claim when representativeness fails and treats
  interval non-overlap only as compatibility evidence pending a direct
  interval for the difference and a design/dependence audit.
- Sampling uncertainty for coded text remains distinct from coding and
  measurement uncertainty. The bootstrap receipt asks for code reading, not
  production; a percentile bootstrap is not presented as a coverage
  validation and a normal descriptive range is not called predictive.
- The Part III boundary now has six audit questions, six claim dimensions, an
  answerable self-check and a seven-field verification receipt. The Chapter 3
  reach-back names „Istraživač margine pogreške” and both states without
  repeating Chapter 8's sampling-design debt.
- The governed aggregate table and the R-or-jamovi task reproduce the portal
  row from the paired analytical view. Exact data reconciliation passes, so
  the author-amended `R32-CATALOG-paired-views` closes here; its separate
  `P5-C` public-catalogue route remains pending.
- Live w09 and the production parity adapter now share the same non-caching
  Marsaglia-polar generator. Ordinary parity passes for all 17 pairs, both
  expected-value and asymmetric-normal-cache negative fixtures fail closed,
  and no tolerance changed.
- The concept graph is fresh at 47 nodes and 511 edges. Style, figure,
  manuscript, citation, terminology, data, widget and parity checks pass.
  Targeted HTML, approved-wrapper PDF and wrapper DOCX renders exited 0 and
  tracked generated outputs were restored.
- Six final independent read-only critics reviewed the exact same hash and
  report 0 fatal, 0 major, 5 nonblocking minor and 0 useful findings. The full
  evidence and synthesis are in `notes/reports/wc-c09-2026-08-12.md` and
  `notes/reports/wc-c09-six-critic-synthesis-2026-08-12.md`; the final source
  was not changed after their review.
- `H-P0-REGISTER-008`, `H-P3-EXISTING-002` and `H-WB-C06-001` are consumed
  with exact dispositions. No new handoff is needed because the public view
  and later affected widget obligations already have canonical owners.
- The four Chapter 9 items remain `ratified` and the chapter remains `draft`
  until C09. Chapter 6 remains unchanged and deliberately `draft` under
  `H-WB-PART-001`; no author reading, external action or release action is
  claimed.

## C09 claim and prepared author gate

- C09 was claimed only after WC-C09 closed and was locally committed as
  `6c50a9fb5389401d2bb05585d6b12feaa6010e81`. The Chapter 9 Git blob is
  `197ffe4340022d7465e797095645fb7a523863b2`, and the working-file SHA-256
  remains `42c69be9eec5fa9dcfed853e95269d661ea8cf73c6ac7ddd9de431c88ae5b08f`.
- `notes/reports/c09-acceptance-package-2026-08-12.md` cites the final commit,
  packet report, all six critic reports, synthesis and exact proposed ledger
  disposition. `OA-C09-ACCEPTANCE` is ready for the in-thread author decision;
  no external message was sent.
- The recommended disposition is to accept only
  `R13-C09-coded-uncertainty`, `R23-C09-code-reading`, `R32-C09-static` and
  `R35-REACHBACK-09`, and to move only `09-procjena` from `draft` to
  `coauthor_review` with an explicit no-author-reading and not-final note.
- `R32-CATALOG-paired-views` is already accepted under the WC-C09 amendment
  and is not reopened. The three accepted R09 correction items remain
  unchanged.
- No proposed status or chapter-ledger disposition has yet been applied. There
  is no delivery targeting C09 to consume. Chapter 6 remains unchanged and
  `draft`; ESS remains optional, portal-mediated and unpromoted, its rights ask
  remains open and bundling remains prohibited.
- C09 requires the exact dated author reply tied to the full WC-C09 commit.
  The standing 5 August delegation is not a substitute. WC-C10 is not claimed,
  and no push, merge, tag, archive, deployment or publication is authorised.

## C09 closeout

- The author replied exactly: `C09 accepted for
  6c50a9fb5389401d2bb05585d6b12feaa6010e81 on 2026-08-12.` The standing 5
  August delegation was not substituted, and no author reading is claimed.
- The final Chapter 9 source remains byte-identical to WC-C09 commit
  `6c50a9fb5389401d2bb05585d6b12feaa6010e81`, Git blob
  `197ffe4340022d7465e797095645fb7a523863b2` and SHA-256
  `42c69be9eec5fa9dcfed853e95269d661ea8cf73c6ac7ddd9de431c88ae5b08f`.
- All six final critic reports and the synthesis address that material state.
  The panel records zero fatal, zero major, five nonblocking minor and zero
  useful findings. The complete decision record is
  `notes/reports/c09-acceptance-package-2026-08-12.md`.
- Exactly `R13-C09-coded-uncertainty`, `R23-C09-code-reading`,
  `R32-C09-static` and `R35-REACHBACK-09` advance from `ratified` to
  `accepted`. `R32-CATALOG-paired-views` and the three accepted R09 correction
  items remain accepted without being reopened.
- Only `09-procjena` advances from `draft` to `coauthor_review`; the ledger
  says explicitly that this is not `final` and does not mean that the author
  read the chapter.
- `OA-C09-ACCEPTANCE` is done from the in-thread reply. No handoff targets C09,
  and C09 creates no new outgoing handoff because every future effect already
  has one canonical owner.
- Chapter 6 remains unchanged and `draft`; ESS remains optional,
  portal-mediated and unpromoted, `OA-G-A3-ESS-RIGHTS` stays open and bundling
  prohibited. C09 changes no chapter prose, data, citation, concept, widget or
  render.
- `WC-C10` is uniquely next but remains unclaimed until the separate C09
  closeout commit. Push, merge, tag, archive, deployment and publication remain
  unauthorised.

## WC-C10 claim — Chapter 10 vertical slice

- WC-C10 was claimed from clean C09 closeout commit
  `c3a8cbd0ec1da65c0e7b903b263cc4a658c73ab8` after the workflow validator
  confirmed no active packet, accepted C09 and WC-C10 alone at sequence 104.
  Exactly one write lock is active; C10 remains unclaimed.
- The complete G-A1a/D01 correction is a fixed baseline: raw-label
  permutation targets the exchangeability/full-distribution no-association
  null, the two-sided unstudentized difference in means remains the statistic,
  `(b + 1) / (B + 1)` governs random permutations, a known-null demonstration
  must satisfy the full null, analytic normal p-values do not receive the
  permutation correction, and the Bayesian frame remains bounded and balanced.
- `H-WB-C06-001` is acknowledged before the first substantive edit and remains
  pending for an exact `before_close` disposition. Live w10 and the parity
  adapter must share a generator and draw order, actual-execution golden proof
  must be retained, asymmetric cached-pair use must fail closed and tolerance
  must not widen.
- The three ratified governed items are `R13-C10-label-fallibility`,
  `R31-C10-ASA-home` and `R35-REACHBACK-10`. The three accepted R01/D01 items
  remain binding baselines and are not reopened without a real finding.
- The packet opens Part IV against G-A2b-IV with magnitude and error
  consequences before ritual. Chapter 6 remains unchanged and deliberately
  `draft`; no author reading, external action or release action is authorised.

## WC-C10 closeout — Chapter 10 vertical slice

- `WC-C10` is accepted at Chapter 10 SHA-256
  `b019a0e3c5f7845e2362aaaa3c37b33fc9e1a3430b0fcd6ccc7e8fcbc8481236`.
  The complete implementation, numerical receipt, all deterministic checks,
  three targeted renders, six final critic reports and synthesis are recorded
  in `notes/reports/wc-c10-2026-08-12.md` and the seven panel files.
- Magnitude, uncertainty and concrete error consequences now precede test
  mechanics; the full-null simulation precedes formal naming. The accepted
  D01 exchangeability null, raw mean-difference statistic, assumptions,
  `(b + 1) / (B + 1)` correction, exact-enumeration distinction, known-null
  error-rate demonstration, analytic-widget boundary and bounded Bayesian
  comparison remain intact.
- Chapter 10 is the principal instructional home of the ASA episode, introduces
  bounded fallibility of reference labels for later Chapter 17 work, and carries
  a Chapter 7/8 reach-back with both interactive and print or DOCX routes plus a
  canonical closure.
- `H-WB-C06-001` is consumed at its `before_close` gate. Live w10 and the
  production parity adapter now use the same non-caching Marsaglia-polar
  generator; ordinary parity passes for 17 pairs, and the three negative
  fixtures fail closed, including all four w10 golden values under asymmetric
  cached-pair consumption. No tolerance changed.
- The concept graph was regenerated to 47 nodes and 514 edges with zero debt.
  HTML, the approved PDF wrapper and the DOCX wrapper all exited zero; generated
  outputs were restored and are not part of the packet.
- Six independent final critics confirmed the exact final source hash. The
  panel records 0 fatal, 0 major, 4 nonblocking minor and 0 useful findings.
  The four visible minor notes concern the order of the eight closing terms, one
  stiff curricular phrase, one slide-like ordinal sequence in the AI frame and
  numeric rather than thematic references to Chapters 7 and 8. The source is
  frozen after that common panel hash.
- `R13-C10-label-fallibility`, `R31-C10-ASA-home` and
  `R35-REACHBACK-10` materially pass but remain `ratified` until C10. The three
  accepted R01/D01 items remain accepted and unmodified. Chapter 10 remains
  `draft`; no author reading or acceptance is claimed.
- No new outgoing handoff is needed. The existing P5-C owner covers the
  catalogue documentation and `H-WB-C06-001` already routes every remaining
  affected widget. Chapter 6 remains unchanged and `draft` under
  `H-WB-PART-001`. C10 is solely next but is not claimed inside WC-C10; no
  external or release action is authorised.

## C10 claim and prepared author gate

- C10 was claimed only after WC-C10 closed and was locally committed as
  `88b41d02fcea8222673f28a40938fe7db2aaffd6`. The Chapter 10 Git blob is
  `e0275e8ba85f360d238bbace6a216dcdef5283bc`, and the working-file SHA-256
  remains `b019a0e3c5f7845e2362aaaa3c37b33fc9e1a3430b0fcd6ccc7e8fcbc8481236`.
- `notes/reports/c10-acceptance-package-2026-08-12.md` cites the final commit,
  packet report, all six critic reports, synthesis and exact proposed ledger
  disposition. `OA-C10-ACCEPTANCE` is ready for the in-thread author decision;
  no external message was sent.
- The recommended disposition is to accept only
  `R13-C10-label-fallibility`, `R31-C10-ASA-home` and `R35-REACHBACK-10`, and
  to move only `10-logika-testiranja` from `draft` to `coauthor_review` with an
  explicit no-author-reading and not-final note. The three accepted R01/D01
  items remain unchanged.
- The final panel has 0 fatal, 0 major, 4 nonblocking minor and 0 useful
  findings. All four minor notes are reproduced in the acceptance package and
  no source changed after the common reviewed hash.
- No proposed status or chapter-ledger disposition has yet been applied. There
  is no handoff delivery targeting C10 to consume. Chapter 6 remains unchanged
  and `draft` under `H-WB-PART-001`.
- C10 requires the exact dated author reply tied to the full WC-C10 commit.
  The standing 5 August delegation is not a substitute. WC-C11 is not claimed,
  and no push, merge, tag, archive, deployment or publication is authorised.

## C10 closeout

- The author replied exactly: `C10 accepted for
  88b41d02fcea8222673f28a40938fe7db2aaffd6 on 2026-08-12.` The standing 5
  August delegation was not substituted, and no author reading is claimed.
- The final Chapter 10 source remains byte-identical to WC-C10 commit
  `88b41d02fcea8222673f28a40938fe7db2aaffd6`, Git blob
  `e0275e8ba85f360d238bbace6a216dcdef5283bc` and SHA-256
  `b019a0e3c5f7845e2362aaaa3c37b33fc9e1a3430b0fcd6ccc7e8fcbc8481236`.
- All six final critic reports and the synthesis address that material state.
  The panel records zero fatal, zero major, four nonblocking minor and zero
  useful findings. The complete decision record is
  `notes/reports/c10-acceptance-package-2026-08-12.md`.
- Exactly `R13-C10-label-fallibility`, `R31-C10-ASA-home` and
  `R35-REACHBACK-10` advance from `ratified` to `accepted`. The three accepted
  R01/D01 correction items remain accepted without being reopened.
- Only `10-logika-testiranja` advances from `draft` to `coauthor_review`; the
  ledger says explicitly that this is not `final` and does not mean that the
  author read the chapter.
- `OA-C10-ACCEPTANCE` is done from the in-thread reply. No handoff targets C10,
  and C10 creates no new outgoing handoff because every future effect already
  has one canonical owner.
- Chapter 6 remains unchanged and `draft`. C10 changes no chapter prose, data,
  citation, concept, widget or render.
- `WC-C11` is uniquely next but remains unclaimed until the separate C10
  closeout commit. Push, merge, tag, archive, deployment and publication remain
  unauthorised.

## Author amendment 2026-08-11 — C11 through P3-VERIFY-C

- `A-THREAD-C11-P3-VERIFY-C-2026-08-11` is a new, distinct author decision
  recorded on 12 August before WC-C11. For this thread only it authorises the
  strict chain `WC-C11`, `C11`, `G-A4-12`, `P3-EVIDENCE12`, `P3-VERIFY-C`
  instead of the usual stop after one packet.
- Every packet still receives its own claim, single write lock, evidence,
  handoff disposition, workflow checks, closeout and bounded commit before the
  next packet is claimed. No evidence or lock crosses a packet boundary, and no
  prerequisite is waived.
- The amendment is distinct from both earlier thread decisions, whose chains
  have ended. C11 still requires a separate exact dated author reply tied to
  the final WC-C11 commit; the 5 August standing delegation cannot replace it,
  and no packet may record that the author read a chapter.
- WC-C11 must consume exactly its three incoming deliveries, close only
  `R04-C11-fixed-order` among the four open R04 children, preserve governed
  aggregate values and repair w11 generator equivalence without widening
  tolerance. G-A4-12 remains decision-only; P3-EVIDENCE12 admits no remembered
  or approximate evidence; P3-VERIFY-C verifies prerequisites independently.
- Chapter 6 remains unchanged and `draft`; all DigiKat, Eurostat, ESS,
  reading-time, reader-validation and terminology-review claim boundaries
  remain binding. The durable decision record is
  `notes/reports/c11-p3-verify-c-thread-amendment-2026-08-11.md`.

## WC-C11 claim — Chapter 11 vertical slice

- WC-C11 was claimed from clean control-only amendment commit
  `64f97250f11dc2fbe6a0c69981cc9834e2c54003` after the workflow validator
  confirmed no active packet, accepted C10 and WC-C11 alone at sequence 106.
  Exactly one write lock is active; C11 and every later packet remain unclaimed.
- `H-P2-VERIFY-001`, `H-P3-EXISTING-002` and `H-WB-C06-001` were acknowledged
  before the first substantive edit and remain pending for exact
  `before_close` dispositions. They respectively bind the lone Chapter 11 R04
  child, governed aggregate print values and exact live/adapter w11 random
  generator equivalence with a fail-closed cached-pair fixture.
- The packet owns `R04-C11-fixed-order`, `R17-C11-exaggeration`,
  `R17-C11-low-power`, `R32-C11-static` and `R35-REACHBACK-11`. The accepted
  `R01-C11-inherited-permutation` correction remains a binding baseline and is
  not reopened without a real finding.
- WC-C11 may close only `R04-C11-fixed-order`. The still-open R04 children are
  `R04-ARCH-macro-order` and `R04-ROUTES-two-track-map` under `P5-ROUTES`, plus
  `R04-C18-whole-prerequisites` under `WE-C18` and `P5-ROUTES`; R04 itself may
  not be called closed here.
- Chapter 6 remains unchanged and deliberately `draft`; no author reading,
  external action or release action is authorised.

## WC-C11 closeout — Chapter 11 vertical slice

- The final Chapter 11 material is fixed at SHA-256
  `d438ba3e1c90fa6b954c6f796da4a0768ef1324352e77b3a966c934a7044e6e1`
  and Git blob `87db0124679ae2085f87c4e7cc4145f9e3191b8f`. The exact discrete
  distribution now distinguishes 53.6% strict superiority, 13.9% ties and
  the 60.6% tie-adjusted measure; the prospective power example uses the
  pre-data target 0.5, standard deviation 1.9, `d = 0.26` and 228 participants
  per group.
- All three incoming deliveries were consumed. `H-P2-VERIFY-001` accepted only
  `R04-C11-fixed-order`; `H-P3-EXISTING-002` preserved the governed aggregate
  values without re-rounding; `H-WB-C06-001` established the same non-cached
  generator for live w11 and its adapter with ordinary parity and negative
  fixture proof.
- Widget parity passes for all 17 pairs: six exact and eleven distributional.
  The w11 extension records actual goldens, retains tolerance `1e-10`, and its
  direct negative fixture fails closed with ten errors. Concept regeneration
  is fresh at SHA-256
  `673267479d0092c69297eba821184c35df4b291b6dbeaebb90f6a370dbb885e2`;
  data, citation, manuscript, figure-introduction and widget-inventory checks
  all pass.
- Targeted HTML, the approved PDF wrapper and the DOCX wrapper all pass. The
  PDF artifact is 2,686,409 bytes at SHA-256
  `20a1bb4a7b0fa53bacdea4ef3e9fe598461b92bc9ceb0dad20c358609a21da4c`;
  the DOCX artifact is 1,525,742 bytes at SHA-256
  `cd995a98e65bd364d5dd1addabd53e8f84e6b3aa8975887c1d26e2e8f8f87eae`.
- The final-hash six-critic panel reports zero fatal, zero major and thirteen
  lens-level minor findings. By the author's instruction, those nonblocking
  findings pass unchanged to C11. `R04-C11-fixed-order` alone is accepted;
  `R17-C11-exaggeration`, `R17-C11-low-power`, `R32-C11-static` and
  `R35-REACHBACK-11` remain ratified for the author gate.
- R04 remains open: `R04-ARCH-macro-order` and
  `R04-ROUTES-two-track-map` belong to `P5-ROUTES`, while
  `R04-C18-whole-prerequisites` belongs to `WE-C18` and `P5-ROUTES`.
  Chapter 6 is unchanged and remains deliberately `draft`. WC-C11 found no
  additional future-relevant effect, so it emitted no outgoing handoff.
- No write lock remains active. `C11` is the sole next permitted packet and
  must be claimed separately before its acceptance package is presented.

## C11 claim and prepared author gate

- C11 was claimed only after WC-C11 closed and was locally committed as
  `00c40c9ebc0627ec8dda9f25d1ee70465f4861c9`. The Chapter 11 Git blob is
  `87db0124679ae2085f87c4e7cc4145f9e3191b8f`, and the working-file SHA-256
  remains `d438ba3e1c90fa6b954c6f796da4a0768ef1324352e77b3a966c934a7044e6e1`.
- `notes/reports/c11-acceptance-package-2026-08-13.md` cites the final commit,
  packet report, all six critic reports, synthesis, all thirteen minor records
  and the exact proposed ledger disposition. `OA-C11-ACCEPTANCE` is ready for
  the in-thread author decision; no external message was sent.
- The recommended disposition is to accept only `R17-C11-exaggeration`,
  `R17-C11-low-power`, `R32-C11-static` and `R35-REACHBACK-11`, and to move
  only `11-velicina-ucinka-i-snaga` from `draft` to `coauthor_review` with an
  explicit no-author-reading and not-final note. `R04-C11-fixed-order` and the
  two accepted R01/R09 baselines remain unchanged; R04 itself remains open.
- The final panel has 0 fatal, 0 major and 13 nonblocking minor records. All
  thirteen are reproduced in the acceptance package, proposed as known and
  nonblocking for this edition, and no source changed after the common reviewed
  hash.
- No proposed status or chapter-ledger disposition has yet been applied. There
  is no handoff delivery targeting C11 to consume. Chapter 6 remains unchanged
  and `draft` under `H-WB-PART-001`.
- C11 requires the exact dated author reply tied to the full WC-C11 commit.
  The standing 5 August delegation is not a substitute. `G-A4-12` is not
  claimed, and no push, merge, tag, archive, deployment or publication is
  authorised.

## C11 closeout

- The author replied exactly: `C11 accepted for
  00c40c9ebc0627ec8dda9f25d1ee70465f4861c9 on 2026-08-13.` The standing 5
  August delegation was not substituted, and no author reading is claimed.
- The final Chapter 11 source remains byte-identical to WC-C11 commit
  `00c40c9ebc0627ec8dda9f25d1ee70465f4861c9`, Git blob
  `87db0124679ae2085f87c4e7cc4145f9e3191b8f` and SHA-256
  `d438ba3e1c90fa6b954c6f796da4a0768ef1324352e77b3a966c934a7044e6e1`.
- All six final critic reports and the synthesis address that material state.
  The panel records zero fatal, zero major and thirteen known nonblocking minor
  records. The complete decision record is
  `notes/reports/c11-acceptance-package-2026-08-13.md`.
- Exactly `R17-C11-exaggeration`, `R17-C11-low-power`, `R32-C11-static` and
  `R35-REACHBACK-11` advance from `ratified` to `accepted`.
  `R04-C11-fixed-order`, `R01-C11-inherited-permutation` and
  `R09-C11-power-assumptions` remain accepted without being reopened; R04
  remains open because its three other children retain their later owners.
- Only `11-velicina-ucinka-i-snaga` advances from `draft` to
  `coauthor_review`; the ledger says explicitly that this is not `final` and
  does not mean that the author read the chapter.
- `OA-C11-ACCEPTANCE` is done from the in-thread reply. No handoff targets C11,
  and C11 creates no new outgoing handoff because every future effect already
  has one canonical owner or was explicitly disposed here.
- Chapter 6 remains unchanged and `draft`. C11 changes no chapter prose, data,
  citation, concept, widget or render. `G-A4-12` is uniquely next but remains
  unclaimed until the separate C11 closeout commit. Push, merge, tag, archive,
  deployment and publication remain unauthorised.

## G-A4-12 claim and prepared Chapter 12 decision

- G-A4-12 was claimed only after C11 closed and was locally committed as
  `afd7f474700bcb2a1d63e7ea63543dc7f27dc1d5`. Exactly one write lock is
  active; `P3-EVIDENCE12` and every later packet remain unclaimed.
- `notes/reports/g-a4-12-decision-package-2026-08-13.md` presents one bounded
  Tier F decision. The recommended central artifact is the 2016 Registered
  Replication Report of the Strack, Martin and Stepper study: a portal-mediated
  primary case with 17 laboratory estimates, intervals, a pooled replication
  estimate, a registered plan, code and protocol trail.
- The proposed `P3-EVIDENCE12` contract requires exact source identity,
  per-file rights and checksums, a minimal non-identifying lab-level derived
  record, a book-native forest plot, and one comparison of the preregistered
  raw-difference analysis with its standardized-effect alternative. It forbids
  significance-only comparison, approximate or remembered values, raw
  participant-data bundling and reuse of the publisher's figure.
- The ratified outline carries one lifecycle from the original claim through
  analytic choices, multilab evidence, forest-plot reading, reform and its
  limits. Existing `w12` stays the central simulation; no second widget or
  metaanalysis-production lesson is introduced. The bridge to Chapter 13 is a
  five-part contract for a named claim, primary analysis, defensible
  alternative, provenance and conclusion boundary.
- OSC 2015 remains supporting context rather than the single pooled artifact;
  Many Analysts is rejected as a second main case because repeated analyses of
  one dataset are not independent replications; COVIDiSTRESS remains deferred
  under D16. Two new definition blocks remain exactly `analitička
  fleksibilnost` and `reproducibilnost` for later WC-C12 implementation.
- No handoff targets G-A4-12. No data, bibliography, figure, code, chapter
  prose, concept graph or registry has been edited. Chapter 6 remains
  unchanged and `draft`.
- `OA-G-A4-12-BRIEF` is ready for the exact in-thread author decision. No
  external message was sent, and no push, merge, tag, archive, deployment or
  publication action is authorised.

## G-A4-12 closeout

- Author/editor Luka Sikic accepted the recommended package exactly for C11
  closeout commit `afd7f474700bcb2a1d63e7ea63543dc7f27dc1d5` on
  2026-08-13. `OA-G-A4-12-BRIEF` is done without an external message.
- The accepted artifact, P3 verification contract, outline, definitions,
  supporting-source boundary, rejected alternatives and authority boundary are
  durable in `notes/reports/g-a4-12-decision-package-2026-08-13.md` and
  `decisions.G-A4-12`.
- No handoff targets G-A4-12 and it creates no new outgoing handoff. The direct
  prerequisite and registered item ownership already carry every later effect.
- No source was retrieved and no data, bibliography, figure, code, chapter
  prose, concept graph or shared registry changed. Chapter 6 remains unchanged
  and `draft`.
- `P3-EVIDENCE12` is uniquely next but remains unclaimed until the separate
  G-A4-12 closeout commit. Push, merge, tag, archive, deployment and publication
  remain unauthorised.

## P3-EVIDENCE12 claim

- P3-EVIDENCE12 was claimed only from clean G-A4-12 closeout commit
  `09c399173537eb958b968bb1353d2c84f473fa25`. Exactly one write lock is
  active; P3-VERIFY-C and every later packet remain unclaimed.
- No handoff delivery targets P3-EVIDENCE12. There is therefore no incoming
  delivery to acknowledge or consume, and nothing targeted to another packet
  will be touched.
- The bounded write surface is the durable evidence report, its minimal
  lab-level derived record, a fail-closed offline verifier, the verified
  bibliography specification and the three workflow control views. Raw participant
  data, publisher figures, Chapter 12 prose, the data catalogue, shared
  registries and Chapter 6 are outside the lock.

## P3-EVIDENCE12 closeout

- The verified primary chain is the SAGE article DOI
  `10.1177/1745691616674458`, APS final-article page, OSF project `pkd65` and
  OSF Data and Results component `h2f98`. Three exact OSF files were retrieved
  once and matched their API MD5 and SHA-256 metadata.
- The portal source declares no OSF node licence and an empty DataCite rights
  list. All 26 temporary files and 1.390.281 bytes were removed outside the
  checkout after verification; no participant row, source archive, plan, code
  or publisher figure is bundled.
- `notes/reports/p3-evidence12-rrr-lab-effects.csv` retains only 17
  non-identifying laboratory rows and has SHA-256
  `23ca66fd8853fe64247d41a4b48221a0e27be158431fe309ec242efbb0dccbf2`.
  Online reconstruction and offline validation both reproduce `N = 1.894`,
  raw REML `0,026766 [-0,107693; 0,161225]` and standardized REML
  `d = 0,014151 [-0,076191; 0,104493]`.
- The source discrepancy is explicit and bounded: Talarico's archived pout SD
  is `1,594894` (`1,59`), whereas Table 1 prints `1,60`. That cell is an
  unavailable claim; it is not needed for any approved book assertion.
- `H-P3-EVIDENCE12-001` carries the book-native forest-plot, sensitivity,
  rights, future citation and source-discrepancy contract to `WC-C12` before
  start. No incoming handoff targeted this packet.
- Chapter 12 prose, `references.bib`, the data catalogue, shared registries,
  figures, widgets and renders remain unchanged. Chapter 6 remains unchanged
  and `draft`.
- `P3-VERIFY-C` is uniquely next but remains unclaimed until the separate
  P3-EVIDENCE12 closeout commit. Push, merge, tag, archive, deployment and
  publication remain unauthorised.

## P3-VERIFY-C claim

- P3-VERIFY-C was claimed only from clean P3-EVIDENCE12 closeout commit
  `08cbdfa4e0120b04c0f1408d6e76284bf28b3f87`. Exactly one write lock is
  active; WC-C12 and every later packet remain unclaimed.
- No handoff delivery targets P3-VERIFY-C. The pending
  `H-P3-EVIDENCE12-001` delivery targets WC-C12 and will be verified but not
  acknowledged or consumed here.
- The gate is read-only over C11 and P3-EVIDENCE12. It may write only its
  verification report and the three workflow control views; it may not
  retrieve sources, alter the evidence artifact, add the reserved bibliography
  key, edit Chapter 12 or produce the forest plot.

## P3-VERIFY-C closeout

- The gate is tied to P3-EVIDENCE12 closeout commit
  `08cbdfa4e0120b04c0f1408d6e76284bf28b3f87`. `C11` and `P3-EVIDENCE12`
  pass separately; no aggregate status was treated as proof and no active
  blocker is hidden.
- C11's final commit `00c40c9ebc0627ec8dda9f25d1ee70465f4861c9`,
  Chapter 11 SHA-256
  `d438ba3e1c90fa6b954c6f796da4a0768ef1324352e77b3a966c934a7044e6e1`
  and git blob `87db0124679ae2085f87c4e7cc4145f9e3191b8f` reconcile. All six final
  critics address that state; the panel has 0 fatal, 0 major and 13
  author-disposed nonblocking minor records. The ledger stage remains only
  `coauthor_review`, not author-read or `final`.
- The evidence CSV retains SHA-256
  `23ca66fd8853fe64247d41a4b48221a0e27be158431fe309ec242efbb0dccbf2`.
  Offline validation reproduces 17 laboratories, `N = 1.894`, raw REML
  `0,026766 [-0,107693; 0,161225]` and standardized REML
  `d = 0,014151 [-0,076191; 0,104493]`.
- Official OSF identities and hashes, the `license: null` / empty
  `rightsList` boundary, the removed 26-file temporary audit, the Talarico
  unavailable cell and the claim-source matrix remain explicit. No network
  retrieval or new source use occurred.
- `H-P3-EVIDENCE12-001` remains `pending` for `WC-C12` at `before_start` and
  was not acknowledged or consumed here. It already carries every verified
  plot, sensitivity, rights, citation and reconstruction constraint, so the
  gate records no new outgoing handoff.
- The registered order is C09/C10/C11, G-A4-12, P3-EVIDENCE12, P3-VERIFY-C,
  then WC-C12. Chapters 9–11 remain `coauthor_review`; Chapter 12 remains
  `draft`. Chapter 6 remains unchanged and `draft`.
- Only the gate report and three control views changed. Chapter prose,
  `references.bib`, evidence artifact, catalogue, shared registries, figures,
  widgets, renders, `docs/` and `_freeze/` remain unchanged.
- `WC-C12` is now uniquely next but remains unclaimed. The authorised
  `A-THREAD-C11-P3-VERIFY-C-2026-08-11` chain stops here; no push, merge, tag,
  archive, deployment or publication action is authorised.

## Author amendment 2026-08-13 — WC-C12 through WD-C13

- `A-THREAD-C12-WD-C13-2026-08-13` is a new, distinct numbered decision for
  this thread. It authorises the strict sequence `WC-C12`, `C12`, `WC-PARTS`,
  `P3-VERIFY-D`, `WD-C13`; every earlier thread amendment has ended on its own
  boundary.
- Every packet retains its own claim, single write lock, evidence bundle,
  handoff dispositions, workflow checks, closeout and bounded local commit.
  No evidence, lock or unfinished disposition crosses a packet boundary.
- C12 still requires the exact dated reply `C12 accepted for <commit> on
  <date>.` The standing 5 August delegation cannot substitute and no author
  reading may be claimed. The thread must stop while that reply is absent.
- WC-PARTS must stop before its first prose edit and present the exact
  blast-radius list. The author then chooses between honest stage reversions
  plus fresh panels and additive bridge/self-check material that does not alter
  accepted chapter bodies.
- WC-C12 is limited to the accepted G-A4-12 brief, G-A2b-IV spine and verified
  P3-EVIDENCE12 package. P3-VERIFY-D verifies prerequisites independently, and
  WD-C13 preserves the optional, portal-mediated, unpromoted ESS boundary with
  an explicit mandatory offline alternative.
- Chapter 6 remains unchanged and deliberately `draft` under
  `H-WB-PART-001`. The durable decision record is
  `notes/reports/c12-wd-c13-thread-amendment-2026-08-13.md`.

## WC-C12 claim — Chapter 12 identity rewrite

- WC-C12 was claimed only from clean control-only decision commit `901340b`
  after the workflow validator confirmed no active packet, accepted
  P3-VERIFY-C and WC-C12 alone at sequence 111. Exactly one write lock is
  active; C12 and every later packet remain unclaimed.
- `H-P0-REGISTER-007` and `H-P3-EVIDENCE12-001` were consumed before claim.
  They bind the single verified lifecycle artifact, book-native forest plot,
  raw-versus-standardized sensitivity, portal and rights boundary, local
  reconstruction, simultaneous `wagenmakers2016` key and first citation, and
  the Talarico unavailable cell.
- `H-P2-SPINE-IV-001` and `H-P2-TERMS-002` were acknowledged before the first
  substantive edit. Exactly two approved definition blocks will be reconciled
  with the checkout-local concept ledger and regenerated graph in this packet.
- The packet owns the ten ratified WC-C12 items and only their bounded source,
  bibliography, concept, figure, assessment, panel and control evidence. It
  does not edit Chapter 6, add another central widget, bundle OSF source data,
  teach meta-analysis production or claim author acceptance.
- The complete claim record is `notes/reports/wc-c12-2026-08-13.md`. C12 is not
  claimed, and push, merge, tag, archive, deployment and publication remain
  unauthorised.

## WC-C12 closeout

- The final Chapter 12 source is SHA-256
  `47700c17b95dcccad6972eec9f1db1729ea0be42c70dc511bf2b755c2220db7a`, git
  blob `bc9bb538625e6996f116ae1fd5b1acba56dc0852`. The author approved only the
  three major panel repairs: same-sentence citations, simulation before the
  formula with format-specific guidance, and a beginner-readable visible
  receipt that preserves the primary raw versus alternative standardized
  branch.
- Six independent read-only critics reviewed the exact final hash. The final
  panel records 0 fatal, 0 major and 10 nonblocking lens-level minors. No minor
  was edited or treated as accepted; all remain explicit for the separate C12
  author disposition.
- The chapter adds exactly the ratified `analitička fleksibilnost` and
  `reproducibilnost` definition blocks. The checkout-local ledger and
  terminology state agree at 49 live definitions; the regenerated graph has
  49 nodes and 543 edges, zero ledger debt and `graph_fresh=true`.
- The verified RRR evidence remains 17 laboratories, `N = 1.894`, raw REML
  `0,026766 [-0,107693; 0,161225]` and standardized REML
  `d = 0,014151 [-0,076191; 0,104493]`. The `wagenmakers2016` bibliography key
  entered with its first citations, and the local CSV remains an editorial
  reconstruction rather than a bundled student dataset.
- `data/widgets.json#w12` now records R-source SHA-256
  `5866361511fc4549ce8506610493842ab551a78fdb0e0f219419fff0421141c9`;
  the OJS hash and contract are unchanged. Widget parity passes at 17 pairs,
  6 exact and 11 distributional, and all four negative fixtures fail closed.
- Final targeted HTML, approved-wrapper PDF and wrapper DOCX renders all exit
  zero. Their exact sizes and SHA-256 values, including the isolated Quarto
  resource-recursion recovery, are recorded in
  `notes/reports/wc-c12-2026-08-13.md`. All tracked generated outputs and every
  temporary DOCX source gate were restored before closeout.
- `H-P2-SPINE-IV-001` and `H-P2-TERMS-002` are consumed. The packet declares no
  new outgoing handoff because the 10 minors pass directly to C12 and all later
  data and continuity effects already have registered owners.
- All 10 governed Chapter 12 items materially pass but remain `ratified` until
  C12. Chapter 12 stays `draft`; no author reading or acceptance is claimed.
  Chapter 6 remains byte-identical, unchanged and deliberately `draft` under
  `H-WB-PART-001`.
- WC-C12 is accepted, its write lock is released, and `C12` alone is next but
  unclaimed. Push, merge, tag, archive, deployment and publication remain
  unauthorised.

## C12 closeout

- C12 was claimed from clean WC-C12 closeout commit
  `23282e67cf876a3d654d1465f399ce48c31baacd` only after the workflow checker
  confirmed no active packet, accepted WC-C12 and C12 alone next. No handoff
  delivery targets C12.
- The author supplied the exact dated reply `C12 accepted for
  23282e67cf876a3d654d1465f399ce48c31baacd on 2026-08-13.` The cited commit
  still contains Chapter 12 SHA-256
  `47700c17b95dcccad6972eec9f1db1729ea0be42c70dc511bf2b755c2220db7a` and git
  blob `bc9bb538625e6996f116ae1fd5b1acba56dc0852`; the source is unchanged after
  the final panel.
- All six final critics address that exact state. The panel records 0 fatal,
  0 major and 10 known nonblocking lens-level minor records. The exact minor
  list and author disposition are recorded in
  `notes/reports/c12-acceptance-package-2026-08-13.md`; none was silently
  edited after source lock.
- Only `12-kriza-i-obnova` advances from `draft` to `coauthor_review`.
  Acceptance does not claim that the author read the chapter and is not a
  `final` designation.
- Only the ten governed Chapter 12 items move from `ratified` to `accepted`:
  `R07-C12-full-argument`, `R08-SPINE-12`,
  `R11-C12-pipeline-flexibility`, `R19-C12-forest-plot`,
  `R19-C12-replication-cumulative`, `R23-C12-no-R-production`,
  `R23-C12-visible-receipt`, `R23-C12-code-ladder`,
  `R24-C12-primary-sources` and `R35-REACHBACK-12`.
- `OA-C12-ACCEPTANCE` is done from the in-thread reply; no external message was
  sent. `packet_reviews.C12` declares no new outgoing handoff because the
  accepted source is a direct WC-PARTS prerequisite and the thread amendment
  already owns its mandatory blast-radius stop.
- Chapter 6 remains unchanged and deliberately `draft` under
  `H-WB-PART-001`. No chapter prose, data, bibliography, concept, widget,
  figure, render or generated artifact changes in C12.
- C12 is accepted, its lock is released, and `WC-PARTS` alone is next but
  unclaimed. WC-PARTS must stop before its first prose edit and present the
  exact affected-unit, current-stage and proposed-change list for author
  choice. Push, merge, tag, archive, deployment and publication remain
  unauthorised.

## Author amendment 2026-08-17 — WC-PARTS through WD-C14

- `A-THREAD-WC-PARTS-WD-C14-2026-08-17` is a new, distinct numbered decision
  for this thread. It authorises the strict sequence `WC-PARTS`,
  `P3-VERIFY-D`, `WD-C13`, `C13`, `WD-C14`; every earlier thread amendment
  has ended on its own boundary.
- Every packet retains its own claim, single write lock, evidence bundle,
  handoff dispositions, workflow checks, closeout and bounded local commit.
  No evidence, lock or unfinished disposition crosses a packet boundary.
- Option B is pre-approved for WC-PARTS: proceed with the ratified bridges and
  self-checks and return every edited accepted unit honestly to `draft`.
  Before the first prose edit, enumerate the exact units and changes and state
  whether any required material can be carried without altering accepted
  chapter bodies.
- WC-PARTS must then propose exactly one batched re-acceptance gate immediately
  after itself. The proposal must name the exact ID, sequence, contract,
  required evidence, exit tests, covered units and handoff that moves their
  deferred panels away from `P6-PANELS`. The gate must not be created without
  a further explicit author approval, and no author reading may be claimed.
- P3-VERIFY-D independently verifies every prerequisite and reports draft
  versus `coauthor_review` stages and any acceptance older than named bytes.
  WD-C13 and WD-C14 preserve the portal-mediated, optional and unpromoted ESS
  route with explicit mandatory offline alternatives. WD-C14 also implements
  the ratified D02 correction without reinterpretation.
- C13 requires the exact dated reply `C13 accepted for <commit> on <date>.` The
  standing 5 August delegation cannot substitute and the thread stops while
  that reply is absent.
- Chapter 6 remains unchanged and deliberately `draft` under
  `H-WB-PART-001`. The durable decision record is
  `notes/reports/wc-parts-wd-c14-thread-amendment-2026-08-17.md`.

## WC-PARTS claim and approved batched gate

- WC-PARTS was claimed only from clean control-only decision commit
  `f4329bac42735ff1b3f5cabe0a651a47f4ce53ef` after the workflow validator
  confirmed no active packet, accepted C12 and WC-PARTS alone next at sequence
  113. Exactly one write lock is active; P3-VERIFY-D and every later packet
  remain unclaimed.
- The packet owns exactly the six chapter sources 07–12, their chapter-ledger
  records, `notes/reports/wc-parts-2026-08-17.md` and the three workflow-control
  views. Chapter 6 is outside the lock and remains deliberately `draft` under
  `H-WB-PART-001`.
- All six units still enter at `coauthor_review`; their source hashes and git
  blobs remain exactly those named by C07–C12. No chapter prose or chapter
  stage changed at claim.
- The seven owned items are `R08-SPINE-07-11`, `R24-PARTIII-IV-thesis`,
  `R24-LADDER-PartIII`, `R24-LADDER-PartIV`, `R27-C12-13-transition`,
  `R35-SELF-CHECK-III` and `R35-SELF-CHECK-IV`. They are `in_progress`, not
  implemented or accepted.
- No handoff delivery targets WC-PARTS. There is therefore no incoming delivery
  to acknowledge or consume before the first edit, and no outgoing handoff or
  closeout declaration has yet been recorded.
- The source audit finds that Chapters 7–11 already carry the required seeded-
  simulation boundary, both cumulative AI ladders and the complete Part III
  bridge/self-check. They require no byte change and remain
  `coauthor_review`. Only Chapter 12 lacks the complete Part IV boundary; its
  proposed additive section contains the claim bridge, six review questions,
  six-dimension claim map and answerable self-check, while preserving the
  existing reformed-practice transition. Its first edit would return only
  Chapter 12 to `draft`.
- The approved and created gate is `C07-C12-REACCEPT`, sequence 114, contract
  `chapter_acceptance_gate`, covering all six units with one round of six
  reports total, one synthesis and the exact reply `C07-C12-REACCEPT accepted
  for <commit> on <date>.` It shifts all prior sequences 114 onward by one and
  makes `P3-VERIFY-D` require the new gate plus `P3-ESS`.
- Created `H-WC-PARTS-REACCEPT-001` delivers the six-chapter final-state
  panel to that gate at `before_start`. No `H-WC-PARTS-001` delivery to
  `P6-PANELS` is created; P6-PANELS retains only its separate Chapter 6 duty
  under `H-WB-PART-001` and excludes Chapters 7–12.
- Luka Sikic approved the exact proposal on 17 August 2026 with the reply
  `Approve C07-C12-REACCEPT at sequence 114 with contract and handoff as
  proposed.` The pre-prose stop is therefore resolved. This is control-plane
  approval, not chapter acceptance, and it claims no author reading. The
  complete live record is
  `notes/reports/wc-parts-2026-08-17.md`.

## WC-PARTS closeout

- `WC-PARTS` closes on the six-source manifest recorded in
  `notes/reports/wc-parts-2026-08-17.md`. Chapters 7–11 remain byte-identical
  to their C07–C11 decisions. Only Chapter 12 changed; its final SHA-256 is
  `4a6d173d7e995e1f251e34003121a8eae7be2a3f7753b538634bc96a0d49a1b4`
  and it remains `draft` pending the separately approved batched gate.
- The initial arc critic's single major finding was resolved by tightening
  only the four Part IV self-check questions and their answer. The final voice
  and arc round records zero fatal, zero major and two nonblocking voice
  minors. All seven owned items materially pass and return to `ratified`; no
  chapter acceptance is inferred.
- Style, structure, figures, citations, concepts, terminology, manuscript
  integrity, spines, book and assessment architecture, data, widgets, parity
  and tokens pass. The fresh concept graph has 49 nodes and 549 edges. Final
  HTML, approved-wrapper PDF and wrapper-built DOCX hashes are recorded in the
  packet report; tracked render and cache output was restored.
- `H-WC-PARTS-REACCEPT-001` carries the exact six-chapter fresh-panel duty to
  `C07-C12-REACCEPT` before start. `H-WC-PARTS-DOCX-001` separately carries
  the discovered recursive-resource release risk to `P7-DOCX` before close.
  These are all future-relevant effects discovered by the packet.
- Chapter 6 remains byte-identical, `draft` and excluded under
  `H-WB-PART-001`. `C07-C12-REACCEPT` is now the sole next packet;
  `P3-VERIFY-D` remains unclaimed.

## C07-C12-REACCEPT claim and fresh panel

- The gate was claimed only from clean WC-PARTS closeout commit
  `ddde7f6cabc0d4335660755c6fbc7601937b4318`. Before claim it consumed
  `H-WC-PARTS-REACCEPT-001` and accepted ownership of the exact six-source
  manifest, not acceptance of any chapter. No prose or ledger stage changed.
- The preflight found zero deterministic style candidates in all six sources,
  complete structural components and all four exercise tiers, and zero figures
  without introductions. The six ratified spines were available. The only
  environment note remains the existing `renv` out-of-sync warning.
- Exactly six independent read-only critics each read all six sources tied to
  the same commit: methods, skepticism, pedagogy, evidence, Croatian style and
  structure. The result is zero fatal, zero major and eleven nonblocking
  lens-level minor records. The evidence critic reports
  `missing_or_unverified: []`.
- The complete synthesis is
  `notes/reports/c07-c12-reaccept-six-critic-synthesis-2026-08-17.md`; the
  bounded decision package is
  `notes/reports/c07-c12-reaccept-acceptance-package-2026-08-17.md`. The
  recommendation is acceptance of the locked manifest with the eleven minor
  records visible and unedited.
- Before the author reply, the gate remained active and fail-closed. Chapter 12
  remained `draft`, the seven governed items remained `ratified`, and
  `P3-VERIFY-D` was not permitted until the exact reply `C07-C12-REACCEPT accepted for
  ddde7f6cabc0d4335660755c6fbc7601937b4318 on 2026-08-17.` is received.
  No author reading is claimed.

## C07-C12-REACCEPT closeout

- Luka Sikic supplied the exact required reply on 17 August 2026, naming
  `ddde7f6cabc0d4335660755c6fbc7601937b4318`. It accepts the six-report
  synthesis with zero fatal, zero major and eleven known nonblocking minor
  records. It does not state or imply that the author read any chapter.
- All six ledger records now name the batched decision and exact source
  manifest. Chapters 7–11 remain byte-identical and in `coauthor_review`; only
  Chapter 12 advances from `draft` to `coauthor_review`. No chapter is `final`.
- Exactly seven items advance from `ratified` to `accepted`:
  `R08-SPINE-07-11`, `R24-PARTIII-IV-thesis`, `R24-LADDER-PartIII`,
  `R24-LADDER-PartIV`, `R27-C12-13-transition`, `R35-SELF-CHECK-III` and
  `R35-SELF-CHECK-IV`. No other item changes status.
- `packet_reviews.C07-C12-REACCEPT` records no new outgoing handoff because
  `P3-VERIFY-D` directly owns independent verification, while the existing
  DOCX and Chapter 6 handoffs retain their separate owners and boundaries.
- The gate closes with no prose, data, bibliography, concept, terminology,
  widget, figure, render or generated-artifact change. `P3-VERIFY-D` is the
  sole next packet and remains unclaimed inside this gate.

## P3-VERIFY-D closeout

- The evidence gate was claimed from clean C07-C12-REACCEPT closeout commit
  `339ec599a8e836d283771a0f271574ef34708993` and independently verified both
  named prerequisites. It did not rely on their aggregate `accepted` status.
- All six Chapter 7–12 sources match the manifest at commit
  `ddde7f6cabc0d4335660755c6fbc7601937b4318`; all six critic reports, the
  synthesis, exact dated author reply, six ledger records and seven accepted
  WC-PARTS items are current. The manifest audit reports `stale_acceptance=0`.
  Chapters 7–12 are `coauthor_review`, with no author-reading or `final` claim.
- P3-ESS still specifies ESS11 edition 3.0, Croatia, 18 variables and
  `anweight`: portal-mediated, optional, unpromoted, zero local ESS files and
  `checksum: null`. All four governed file blobs, the positive validator and
  nine deliberate negative fixtures match the accepted contract.
  `populacija_medija` remains the licensed local CC BY 4.0 mandatory
  alternative for `WD-C13`–`WD-C16`. The open rights ask does not block portal
  use, but bundling remains prohibited without permission.
- The full deterministic ladder passes. The initial 124-second run of the 44
  data negative fixtures hit the process timeout; the complete retry finished
  in 178.2 seconds with `DATA_NEGATIVE_FIXTURES_OK cases=44`. This is recorded
  as a timeout followed by a successful full run, not as an inferred pass.
- No handoff targets this gate. `H-P3-ESS-001` remains pending for each
  model-wave consumer, `H-WC-PARTS-DOCX-001` remains with `P7-DOCX`, and
  `H-WB-PART-001` keeps unchanged Chapter 6 `draft` for `P6-PANELS`.
  `packet_reviews.P3-VERIFY-D` declares no new future effect because those
  existing owners and the direct dependency on `WD-C13` already cover it.
- The text package remains just-in-time gated at sequences 125–128 immediately
  before `WD-C17`; these gates do not falsely make it ready now. No chapter,
  data, bibliography, concept, terminology, widget, figure, render or
  generated artifact changed. `WD-C13` is the sole next packet and remains
  unclaimed inside this closeout.

## WD-C13 claim

- `WD-C13` was claimed only from clean P3-VERIFY-D closeout commit
  `1fbda82351ac8d4889bce7a82cf564afd806a9bb`. Exactly one write lock owns the
  Chapter 13 source, its ledger/concept consequences, one packet report, six
  critic reports, one synthesis and the three workflow-control views.
- `H-P3-ESS-001` was consumed before claim. Its disposition keeps
  `populacija_medija` as the mandatory bundled local CC BY 4.0 route and limits
  ESS Round 11 edition 3.0 to an optional reader-owned portal replication for
  Croatia with an analysis-specific valid-response denominator and
  `anweight`. No ESS result, local bytes, checksum, promotion, edition-parity
  claim, redistribution authority or official-turnout claim is permitted.
- `P2-SPINE-V` was independently checked against the live ratified Chapter 13
  spine with 11 aspects, 8 terms, 6 prerequisites and 7 exclusions.
  `P1A-C13` remains exactly present at git blob
  `9242e057c6602b273368164de6193b08eba5eeb8`; adjusted standardized residuals
  and separate null-calibration and alternative-power simulations remain
  intact. Both spine and ESS deterministic checks pass.
- The packet owns exactly `R13-C13-contingency`,
  `R27-C13-partV-contract` and `R35-REACHBACK-13`. They are `in_progress`, not
  accepted. Chapter 13 remains `draft`; no author reading or acceptance is
  claimed. `C13` and `WD-C14` remain unclaimed.

## WD-C13 closeout

- The final Chapter 13 source is SHA-256
  `b52341768fd6b6e985d3e5c9d1093c9196857dee895982438e3e63ee22d586d3`, git
  blob `e7ff4e8adc9d2438461ffbddb01e193aba24b671`. It has 11 main sections,
  2,964 prose words and section-evenness coefficient 0.32.
- The author approved exactly eight combined repairs and directed all
  independent minors to `C13`. The source now has the correct p-value
  direction, bounded GOF interpretation, correct Fisher explanation,
  predeclared recoding question, 95-percent confidence interval, distinct
  Berkeley tool roles, reader-voice ESS path and a faithful static twin.
- The static twin and `data/widgets.json#w13` agree on the exact scenarios:
  with the same 20-percent relative shift, chi-square rises from 1.6 at margin
  20 to 6.4 at margin 80 while Cramer's V remains 0.20. The final R source hash
  is `130158017eff43321e8b429eefc937486c9d28459e6bbbaa06efc4a2d672479b`.
- All six final read-only critics address the same source hash and independently
  confirm all eight repairs. The panel records 0 fatal, 0 major and 14
  nonblocking lens-level minor records: methods 1, skepticism 2, pedagogy 3,
  evidence 4, style 4 and structure 0. No independent minor was edited or
  silently accepted.
- The deterministic ladder passes, including style, structure, figures,
  citations, concepts, terminology, manuscript, spines, assessment, catalogue,
  ESS portal, data, tokens, widget contract and parity. All required manuscript,
  inventory, AI-export, data, widget-parity and workflow negative fixtures fail
  closed.
- Targeted HTML succeeds at 176,785 bytes and SHA-256
  `4af9b743194266c2ad38fc1417a303564fed429d9c1be43b54bbaef410cf6b26`.
  The approved PDF wrapper succeeds at 2,752,817 bytes and SHA-256
  `858a3f1428dd5822890aad0449afd1290790b3ee8bbce3e40bdffbde4f139de6`;
  the DOCX wrapper succeeds at 1,575,666 bytes and SHA-256
  `1c22637f481bbf15c784b1fc313e29cfdf04d7764fddc8f6537c44ff77b8116a`.
  Both full renders ran in clean isolated worktrees, which were removed after
  verification; no generated artifact enters the packet commit.
- `H-P3-ESS-001` is consumed only for WD-C13. Its pending deliveries to
  WD-C14–WD-C16 remain intact, ESS remains optional and portal-mediated, and
  `populacija_medija` remains the mandatory licensed local route. No new
  outgoing handoff is needed because every later effect already has an owner.
- `R13-C13-contingency`, `R27-C13-partV-contract` and `R35-REACHBACK-13`
  materially pass but return to `ratified` pending `C13`. Chapter 13 remains
  `draft`; Chapter 6 remains byte-identical and `draft` under
  `H-WB-PART-001`. No author reading, chapter acceptance or final-stage claim
  is made.
- No write lock remains active. `C13` alone is next and requires the exact
  dated author reply naming the final WD-C13 closeout commit. `WD-C14` may not
  be claimed while that reply is absent.

## C13 claim

- The exact author reply was received as
  `C13 accepted for a88fc80ad1b323f514e3e50d51c5da49fea07bd8 on 2026-08-17.`
  It names the clean WD-C13 closeout commit and the current decision date; the
  earlier malformed reply without the `C` prefix was not used.
- Preflight confirms HEAD `a88fc80ad1b323f514e3e50d51c5da49fea07bd8`,
  Chapter 13 SHA-256
  `b52341768fd6b6e985d3e5c9d1093c9196857dee895982438e3e63ee22d586d3`, six
  final reports, one synthesis, 0 fatal, 0 major and 14 known minor records.
- No handoff delivery targets `C13`. The gate owns only the chapter-ledger
  disposition, its acceptance package and the three workflow-control views;
  it owns no chapter prose, data, bibliography, figure, widget or generated
  artifact.
- Chapter 13 remains `draft` and the three governed items remain `ratified`
  until closeout. The only permitted state change is their narrow accepted
  disposition plus `coauthor_review`; no author reading or `final` claim is
  permitted.

## C13 closeout

- The exact accepted state is WD-C13 commit
  `a88fc80ad1b323f514e3e50d51c5da49fea07bd8`, Chapter 13 SHA-256
  `b52341768fd6b6e985d3e5c9d1093c9196857dee895982438e3e63ee22d586d3` and git
  blob `e7ff4e8adc9d2438461ffbddb01e193aba24b671`. The chapter source is unchanged
  by the acceptance gate.
- `notes/reports/c13-acceptance-package-2026-08-17.md` cites the final commit,
  all six reports, the synthesis, exact reply, ledger disposition, eight
  resolved mandatory repairs and all fourteen known nonblocking minor records.
- Only `13-kategoricki-podaci` advances from `draft` to `coauthor_review`.
  This records an accepted revision state, not an assertion that the author
  read the chapter and not a `final` stage.
- Only `R13-C13-contingency`, `R27-C13-partV-contract` and
  `R35-REACHBACK-13` advance from `ratified` to `accepted`. The already
  accepted P1A-C13 residual and calibration items remain unchanged; no other
  child moves.
- Fourteen lens-level minor records are known and nonblocking for this edition.
  They were not edited, silently resolved or converted into a new obligation.
- No delivery targets `C13`, and `packet_reviews.C13` records no outgoing
  handoff because WD-C14 is the direct successor while the ESS, DOCX and
  Chapter 6 obligations already have stable owners.
- Chapter 6 remains byte-identical and `draft` under `H-WB-PART-001`.
  `H-P3-ESS-001` remains pending for WD-C14–WD-C16 and
  `H-WC-PARTS-DOCX-001` remains pending for P7-DOCX.
- No active write lock remains. `WD-C14` alone is next and is not claimed
  inside this gate. No chapter prose, data, bibliography, concept, terminology,
  figure, widget, render or generated artifact changed.

## WD-C14 closeout

- WD-C14 closes on Chapter 14 SHA-256
  `84b6c8fac8ce4eecf5474a0535ba02030dbf332a37789bcd7347c4ae9a66cfa2`
  and git blob `6ef3a218dfc61d5ad73f83e236a70e3917909d86`. The source has 11
  sections, 2.692 prose words, two definitions, one faithful HTML/PDF widget
  pair and all four exercise tiers.
- D02 is reproduced exactly: television-minus-social estimate
  `1,185714285714`; Welch SE `0,372609208160`, df `102,471131550669`,
  p `0,001935138042`; ordinary homoskedastic OLS retains the estimate but has
  SE `0,369536997510`, df 118 and p `0,001717470691`.
- H-P3-ESS-001 was consumed before claim. ESS remains optional,
  reader-owned, portal-mediated and unpromoted with `anweight` and an
  analysis-specific valid denominator; no local ESS bytes, result, checksum,
  promotion or rights claim was added. `populacija_medija` remains the
  mandatory licensed local route.
- H-WB-C06-001 is consumed. Live w14 and its production adapter share one
  explicit non-caching Marsaglia-polar stream; final OJS and R fingerprints
  are registered, all 17 parity pairs pass, the tolerance is unchanged and
  the dedicated w14 cache-asymmetry fixture fails closed. The static twin now
  faithfully carries both the group-overlap and independent-versus-paired
  arguments.
- All six final critics confirmed the same blob. The panel records 0 fatal, 0
  major and 4 nonblocking lens-level minors: one skeptical terminology note
  and three local Croatian copyedit notes. None was edited after the source
  lock; all are exposed to C14.
- Style, structure, figure introductions, spines, terminology, citations,
  concepts, catalogue, ESS, widgets, parity, data, manuscript integrity and
  tokens pass. All required negative fixture suites fail closed. Targeted
  HTML, approved-wrapper PDF and wrapper DOCX render successfully; the final
  PDF has SHA-256
  `4f863d0195c71224f74fc9295ba311c35f930841557cda9222d1d96e09cf05bd`.
- R35-REACHBACK-14 materially passes but remains `ratified` pending C14;
  R02-C14-welch-ols stays accepted and revalidated. Chapter 14's dependence
  stop rule passes, while the multi-chapter R22-C14-C16-dependence item remains
  `ratified` for WD-PART. Chapter 14 remains `draft`.
- No new outgoing handoff is required. Chapter 6 remains unchanged and
  deliberately `draft`; Chapters 7–13 remain in their accepted states. No
  author reading, C14 acceptance, external message or release action is
  claimed.
- No write lock remains active. Under
  `A-THREAD-WD-C14-C14-PREP-2026-08-13`, C14 alone may next be claimed to
  assemble its complete acceptance package and then stop for the exact reply.
  WD-C15 may not start.

## C14 acceptance-package preparation

- C14 was claimed only after the clean WD-C14 closeout commit
  `378bc362f9090e3bcdf8e9e02090c2c1d732e532` and a passing workflow
  preflight. No handoff delivery targets C14, and its ownership is limited to
  the acceptance package and three workflow-control views.
- `notes/reports/c14-acceptance-package-2026-08-17.md` cites the exact WD-C14
  commit, Chapter 14 SHA-256 and blob, all six final critic reports, their
  synthesis, D02 numerical disposition, all four known minor records and the
  complete proposed ledger disposition.
- The package proposes that an exact acceptance move only
  `14-dvije-grupe` from `draft` to `coauthor_review` and
  `R35-REACHBACK-14` from `ratified` to `accepted`. R02-C14-welch-ols would
  remain accepted with a fresh revalidation record, while the multi-chapter
  R22-C14-C16-dependence item would remain ratified for WD-PART.
- No proposed disposition has been applied. Chapter 14 remains `draft`, C14
  remains `in_progress`, its completion evidence remains empty, and WD-C15 has
  not been claimed. No author reading or `final` state is claimed.
- `OA-C14-ACCEPTANCE` is ready and awaits exactly
  `C14 accepted for 378bc362f9090e3bcdf8e9e02090c2c1d732e532 on 2026-08-17`.
  A different commit or date requires a new match check; exact blocking
  revisions may be returned instead.
- The C14 lock deliberately remains active while awaiting the reply. This is a
  clean, resumable preparation checkpoint, not a gate closeout. WD-C15, push,
  merge, tag, archive, deployment and publication remain prohibited.

## C14 closeout

- The exact author reply was received as
  `C14 accepted for 378bc362f9090e3bcdf8e9e02090c2c1d732e532 on 2026-08-17`.
  It names the final WD-C14 closeout commit and current decision date; the
  standing 5 August delegation was not used.
- The accepted source remains Chapter 14 SHA-256
  `84b6c8fac8ce4eecf5474a0535ba02030dbf332a37789bcd7347c4ae9a66cfa2`
  and git blob `6ef3a218dfc61d5ad73f83e236a70e3917909d86`. C14 changes no
  chapter prose, data, bibliography, terminology, concept, widget, figure or
  generated artifact.
- `notes/reports/c14-acceptance-package-2026-08-17.md` records the exact
  reply, final commit, all six reports, synthesis, D02 revalidation, four
  known minor records and applied ledger disposition.
- Only `14-dvije-grupe` advances from `draft` to `coauthor_review`. This
  records an accepted revision state, not an assertion that the author read
  the chapter and not a `final` stage.
- Only `R35-REACHBACK-14` advances from `ratified` to `accepted`.
  `R02-C14-welch-ols` remains accepted and gains final-state revalidation
  evidence. `R22-C14-C16-dependence` records the passing Chapter 14 slice but
  remains `ratified` for WD-PART until Chapters 15 and 16 pass.
- Four lens-level minor records are known and nonblocking for this edition.
  They were not edited, silently resolved or converted into a new obligation.
- No delivery targets C14. `packet_reviews.C14` records no outgoing handoff
  because the direct successor and every ESS, widget, dependence, DOCX and
  Chapter 6 consequence already have stable owners.
- Chapter 6 remains unchanged and deliberately `draft`. Chapters 7–13 retain
  their accepted states. No author reading, external message or release
  action is claimed.
- No active write lock remains. WD-C15 alone is next at sequence 120 but is
  not claimed inside C14. It requires a fresh clean preflight, its own handoff
  consumption, bounded evidence, closeout and local commit.

## Eighth thread amendment and WD-C15 handoff preflight

- Author and editor Luka Sikic approved the new, distinct decision
  `A-THREAD-WD-C15-G-A4-16-2026-08-17` on 17 August 2026. Its strict chain is
  `WD-C15 -> C15 -> G-A4-16`; all seven earlier thread-amendment chains have
  ended and none is treated as continuing authority.
- The amendment changes only the ordinary stop-after-one-packet rule. Each
  packet keeps its own lock, claim and closeout checks, evidence, handoff
  disposition and scoped commit. C15 still stops for exactly
  `C15 accepted for <commit> on <date>`, and G-A4-16 stops for the author's
  artifact, rights and binary-outcome-bridge decisions.
- Clean preflight at C14 closeout commit `7dc4a18f23116fdcc5cb2847d2fbd79aeed735c0`
  confirmed no active packet and WD-C15 alone at sequence 120. A complete
  target scan of all 97 handoffs found exactly one delivery to WD-C15:
  `H-P3-ESS-001` at `before_start`.
- That delivery is consumed before claim. ESS remains optional, reader-owned,
  portal-mediated and unpromoted; no local file, checksum, empirical result,
  file-parity or rights-holder-permission claim is allowed. Mandatory offline
  work uses the promoted CC BY 4.0 `data/populacija-medija.csv` or its five-row
  aggregate. `OA-G-A3-ESS-RIGHTS` remains open and bundling remains prohibited.
- WD-C15 remains unclaimed. Chapter 6 remains deliberately `draft`, Chapters
  7–12 retain their reaccepted states, and no chapter prose, registry stage,
  data file, figure, widget or generated artifact changes in this control
  record.

## WD-C15 claim

- `WD-C15` was claimed on 17 August 2026 from clean commit
  `4e482de7fd8c805d5349ed9677bc1e9898684eb9` after a fresh workflow check
  passed. It is the sole active write packet; `C15` is not claimed.
- The bounded write set is Chapter 15, its regenerated concept graph, the w15
  source fingerprints in `data/widgets.json`, the packet and six-critic
  reports, the synthesis, and the register, handoff ledger and dashboard.
  Chapter 14, Chapter 16, shared registries, datasets, AI exports and render
  artifacts are outside the lock.
- `H-P3-ESS-001` remains consumed before claim. Mandatory work uses the
  promoted CC BY 4.0 `populacija_medija` files; ESS stays optional,
  portal-mediated, unpromoted and without a local-result or rights claim.
- The claim preserves Chapter 6 at deliberate `draft`, Chapters 7–12 at their
  reaccepted states, and the exact C15 author-reply stop.

## WD-C15 closeout

- The final Chapter 15 source is SHA-256
  `fd8337520901df9bbce56e25880f12b889fd54d46e4c1bb3e8f17da3ca49d813`
  and git blob `aa644049bacb62e7fc05ab75d3b6157b83165b96`. The structural
  lint reports 10 top-level sections, 2,527 prose words and body evenness 0.21.
- The revision leads with multiplicity consequences, puts both simulations
  before formulas, interprets eta-squared before F, distinguishes omnibus from
  planned and post-hoc questions, and reports the illustrative pair with a
  simultaneous interval. It teaches the SS/MS divisors, bounds eta/omega
  uncertainty, separates Tukey from Welch and stops for dependent rows.
- `R09-C15-variance-ratio`, `R23-C15-suspect-code` and
  `R35-REACHBACK-15` materially pass but remain `ratified` for the separate C15
  author gate. `R02-C15-dependent-revalidation` remains accepted and is
  revalidated. The Chapter 15 slice of `R22-C14-C16-dependence` passes, while
  that multi-chapter item remains `ratified` for `WD-PART`.
- The final widget fingerprints are OJS
  `f9f2533eb899673a6a26ee494a149f0512c3f70d68b962df0fa27f1d54b13a73`
  and R
  `b8b3acf152646f0a8864f9a3eb64eb67636929e5c0eb8692a670af0e20c9dfc1`.
  The regenerated concept graph has 49 nodes, 608 edges, 249 displayed
  co-occurrence edges and 45 definition edges.
- A clean-session numerical reproduction confirms every classical, Welch,
  rank, Tukey, multiplicity-simulation and offline-aggregate value. Citation,
  style, structure, figure, concept, terminology, spine, assessment, catalogue,
  ESS portal, data, widget parity, token and workflow checks pass; all three
  workflow negative fixtures fail closed.
- The exact held blob rendered successfully as targeted HTML and full-wrapper
  PDF and DOCX in a disposable isolated worktree. The wrapper gates were
  restored, the worktree was removed and no generated render artifact entered
  the primary checkout.
- The mandatory final six-critic rerun records 0 fatal, 0 major and 4
  nonblocking style-minor records. The earlier diagnostic panel's six majors
  were all resolved before this rerun. The four surviving polish records were
  not silently edited after the panel and pass visibly to C15.
- `packet_reviews.WD-C15` declares no outgoing handoff. Every ESS, Chapter 16,
  dependence, DOCX and Chapter 6 consequence already has a stable owner.
- Chapter 6 remains deliberately `draft`; Chapters 7–14 retain their accepted
  states. No chapter-ledger stage changes in WD-C15, no author reading is
  claimed and no release action is authorised.
- No write lock remains. C15 alone is next at sequence 121 and must be claimed
  separately to assemble the acceptance package, cite the WD-C15 closeout
  commit and stop for exactly `C15 accepted for <commit> on <date>`.

## C15 closeout

- The exact author reply was received as
  `C15 accepted for a385ddc85c11e5d1cf63b33043c1df2a90cff6fb on 2026-08-17`.
  It names the final WD-C15 closeout commit and decision date; the standing
  5 August delegation was not used.
- `notes/reports/c15-acceptance-package-2026-08-17.md` ties the decision to
  Chapter 15 SHA-256
  `fd8337520901df9bbce56e25880f12b889fd54d46e4c1bb3e8f17da3ca49d813`,
  git blob `aa644049bacb62e7fc05ab75d3b6157b83165b96`, all six final reports and
  the synthesis.
- The panel basis is 0 fatal, 0 major and 4 known nonblocking style-minor
  records. No source edit or new panel is proposed.
- Only `15-vise-grupa` advances from `draft` to `coauthor_review`. This records
  an accepted revision state, not an assertion that the author read the
  chapter and not a `final` stage.
- Only `R09-C15-variance-ratio`, `R23-C15-suspect-code` and
  `R35-REACHBACK-15` advance from `ratified` to `accepted`.
  `R02-C15-dependent-revalidation` remains accepted and revalidated.
  `R22-C14-C16-dependence` retains the passing Chapter 15 slice but remains
  `ratified` for `WD-PART` until Chapter 16 passes.
- Four style-minor records are known and nonblocking for this edition. They
  were not edited, silently resolved or converted into a new obligation.
- `packet_reviews.C15` records no outgoing handoff because the direct
  successor and every ESS, dependence, DOCX and Chapter 6 consequence already
  have stable owners.
- The ninth distinct thread amendment is recorded in
  `notes/reports/c15-g-a4-17-thread-amendment-2026-08-17.md`; it authorises the
  strict chain only and waives no stop, gate or prerequisite.
- Chapter 6 remains unchanged and deliberately `draft`. Chapters 7–14 retain
  their accepted states. No author reading, external message or release action
  is claimed.
- No active write lock remains. `G-A4-16` alone is next at sequence 122 but is
  not claimed inside C15.

## G-A4-16 closeout

- Clean preflight at C15 closeout commit
  `a9697b1808765038e1d4a176223023e363ad3c3a` found no active packet,
  `G-A4-16` alone at sequence 122 and a passing workflow validator. The gate
  was claimed on 18 August 2026 as the sole write packet.
- The bounded write set is
  `notes/reports/g-a4-16-decision-package-2026-08-18.md` and the three control
  files. Chapter 16, bibliography, data, figures, widgets, generated artifacts
  and shared registries are outside the lock.
- A complete scan of all 97 handoffs found no delivery targeted to `G-A4-16`.
  Deliveries targeted to `WD-C16` remain unacknowledged and unconsumed until
  that separate packet is lawfully claimed.
- The complete decision package recommends Kleppang et al. (2021), PLOS ONE
  Table 3 and only the first results paragraph beneath it. The bounded task
  uses a semantically redrawn Croatian table and an adapted translated
  paragraph; it preserves three specifications, reference groups, four AOR
  estimates and 95% intervals and requires readers to mark absent model `N`,
  fit, diagnostics, risks and predicted probabilities. There is no data
  retrieval or model refit.
- The documented lawful-use basis is CC BY 4.0 for an adapted table and
  adapted paragraph in HTML, PDF and DOCX, with full attribution, DOI and
  licence links and a change notice. No separate rights-holder permission,
  fee or extension of article rights to Ungdata data is inferred or claimed.
- The recommended binary-outcome disposition is to include a bounded reading
  bridge in `WD-C16`: probability versus odds, reference group, `omjer
  izgleda`, 95% interval and why the unavailable `predviđena vjerojatnost`
  cannot be recovered from the table. It permits no logistic-model fitting or
  derivation, empirical prediction, new definition block or second widget.
- Author/editor Luka Sikic supplied all three exact replies on 18 August 2026
  against C15 closeout commit
  `a9697b1808765038e1d4a176223023e363ad3c3a`. Artifact, rights and bridge are
  accepted exactly as recommended; neither the standing delegation nor an
  inferred rights-holder permission was used.
- `OA-G-A4-16-ARTIFACT` and `OA-G-A4-16-RIGHTS` are done. The decision record,
  alternatives, blocked dependencies and authority boundary are complete;
  `packet_reviews.G-A4-16` declares no new outgoing handoff because every
  future consequence already has a direct registered owner.
- Chapter 6 remains deliberately `draft`; Chapters 7–15 retain their accepted
  stages. No chapter prose, bibliography, data, registry stage or generated
  artifact changed, and no external or release action is claimed.
- No active write lock remains. `WD-C16` alone is next at sequence 123 but is
  not claimed inside G-A4-16.

## WD-C16 closeout

- WD-C16 was claimed from clean G-A4-16 reconciliation commit
  `8e4a2c602d6acaa002d88ea8fbb00dab5e6439e5` as the sole write packet. Its
  final source SHA-256 is
  `dc31161a54058a92054e3c3d2ac78cc09bad500984be5db5cda9b4e90fcad671`
  and git blob `99e20c5885ab10a0bbdfaa8981431edf20e556a3`.
- `H-P3-ESS-001` was consumed before claim. `H-G-A2C-002`,
  `H-P2-TERMS-003`, `H-P2-DOCS-001` and `H-WB-C06-001` were acknowledged
  before substantive work and consumed before closeout with final-state
  evidence. ESS remains optional, portal-mediated and unbundled; mandatory
  work uses `populacija_medija`.
- The chapter now holds one stable finite-population OLS estimand, distinguishes
  total from source-conditional age patterns, teaches common cause, mediator and
  collider roles, adds planned interaction and a real retrieval pause, enforces
  the dependent-row stop rule and separates explanation, prediction and cause.
- The accepted G-A4-16 route is implemented as a semantic Croatian adaptation
  of Kleppang Table 3 plus its bounded paragraph. AOR 1,60, interval 1,43–1,80,
  the 80th-percentile outcome, missing model information and complete CC BY 4.0
  attribution appear without data retrieval or logistic-model refitting.
- w16 and its production adapter now consume the same explicit noncached polar
  stream. The OJS and R fingerprints are respectively
  `bdc6ffbda4b05db4825fadb0f5660dd906ad60852d51eedcc07e8d007c045c37`
  and `36fbdccd1e17bdd9b1dbc5c0cd94ad386f587215f3970d700f48fc8701c5b8df`;
  the tolerance is unchanged and the sixth cache-asymmetry fixture fails closed.
- The fresh concept graph has 49 nodes, 620 edges, 257 displayed co-occurrence
  edges and 45 definition edges. Style, structure, figures, citations, concepts,
  terminology, manuscript, spines, catalogue, ESS, assessment, data, all 17
  widgets, token and workflow checks pass.
- The exact held source rendered as targeted HTML of 235.391 bytes
  (`31be2b4b…ef7fd`), approved-wrapper PDF of 5.923.376 bytes and 471 pages
  (`6790130f…e5734`) and wrapper DOCX of 2.811.935 bytes
  (`70f6480b…fc9f`). No generated artifact enters the primary checkout.
- Two earlier panels were diagnostic. The mandatory final six-critic rerun on
  blob `99e20c5885ab10a0bbdfaa8981431edf20e556a3` records 0 fatal, 0 major and
  4 nonblocking minor records: one skeptical, one pedagogical and two style.
  There was no post-panel source edit.
- Nine C16-owned ratified items materially pass but remain ratified until C16.
  R02-C16 and the three R09-C16 items remain accepted and are revalidated. The
  Chapter 16 slice of `R22-C14-C16-dependence` passes, while that multi-chapter
  item remains ratified for `WD-PART`.
- `packet_reviews.WD-C16` declares no outgoing handoff because all future
  consequences already have owners. Chapter 6 remains deliberately `draft`,
  Chapters 7–15 retain their accepted states and no chapter-ledger stage changes
  in WD-C16.
- At WD-C16 closeout no write lock remained and C16 alone became next at
  sequence 124. That boundary was preserved until the separate C16 claim; no
  author reading, acceptance, release action or publication was claimed.

## C16 acceptance-package preparation

- C16 was claimed from the clean WD-C16 closeout commit
  `9cd5a7983d61d27fe9bb8ca77d8764b419ec857a` as the sole active packet.
  Ownership is limited to the acceptance package and three control views; no
  chapter prose, registry item, chapter-ledger stage or handoff status changed.
- The complete package is
  `notes/reports/c16-acceptance-package-2026-08-18.md`. It binds the author
  decision to Chapter 16 SHA-256
  `dc31161a54058a92054e3c3d2ac78cc09bad500984be5db5cda9b4e90fcad671`, git
  blob `99e20c5885ab10a0bbdfaa8981431edf20e556a3`, all six final reports and the
  synthesis.
- The panel disposition is fully exposed: 0 fatal, 0 major and 4 proposed
  known nonblocking minor records. There was no post-panel source edit.
- On an exact acceptance reply only, the proposed narrow disposition would
  advance `16-regresija` from `draft` to `coauthor_review` and only nine
  C16-owned ratified items to `accepted`. The accepted R02-C16 and three
  R09-C16 items would remain accepted and be recorded as revalidated;
  `R22-C14-C16-dependence` would remain ratified for `WD-PART`.
- At the preparation checkpoint C16 remained `in_progress`, Chapter 16 stayed
  `draft` and the nine items stayed `ratified`; `G-A4-17` was neither claimed
  nor permitted while the reply was absent. Chapter 6 remained deliberately
  `draft`.
- The exact required reply is
  `C16 accepted for 9cd5a7983d61d27fe9bb8ca77d8764b419ec857a on 2026-08-18`.
  No author reading, `final` state, release action or publication is claimed.

## C16 closeout

- Luka Sikic supplied the exact required reply for WD-C16 commit
  `9cd5a7983d61d27fe9bb8ca77d8764b419ec857a` on 18 August 2026. The standing
  5 August delegation was not used and no author reading is claimed.
- C16 accepts the six-report synthesis on Chapter 16 SHA-256
  `dc31161a54058a92054e3c3d2ac78cc09bad500984be5db5cda9b4e90fcad671`
  and git blob `99e20c5885ab10a0bbdfaa8981431edf20e556a3`, with 0 fatal, 0 major and 4
  known nonblocking minor records. The source was not edited.
- `16-regresija` alone advances from `draft` to `coauthor_review`. The ledger
  explicitly records that this is not `final` and does not mean that the author
  read the chapter.
- Exactly nine C16-owned items advance from `ratified` to `accepted`:
  `R08-C16-cross-design`, `R14-C16-binary-reading`, `R14-C16-interaction`,
  `R14-C16-adjustment-contract`, `R16-C16-table`, `R16-C16-paragraph`,
  `R16-C16-no-refit`, `R29-C16-retrieval` and `R35-REACHBACK-16`.
- `R02-C16-dependent-revalidation` and the three R09-C16 items remain
  accepted and gain final-state revalidation evidence.
  `R22-C14-C16-dependence` records a passing Chapter 16 slice but remains
  ratified for `WD-PART`.
- `packet_reviews.C16` declares no new outgoing handoff because every later
  consequence already has an owner. Chapter 6 remains deliberately `draft`,
  and Chapters 7–15 retain their accepted states.
- No write lock remains. G-A4-17 alone is next at sequence 125 and is not
  claimed inside C16. Push, merge, tag, archive, deployment and publication
  remain unauthorised.

## G-A4-17 author-brief preparation

- G-A4-17 was claimed from the clean C16 closeout commit
  `26197f84889f1b1caffc25e4bbc171631328adb4` as the sole write packet. Its
  bounded write set contains only
  `notes/reports/g-a4-17-decision-package-2026-08-18.md` and the three workflow
  control views. Chapter 17, data, bibliography, widget, catalogue and shared
  registries remain outside the lock.
- The complete 97-handoff ledger has no delivery targeted to `G-A4-17`.
  Deliveries and evidence owned by `G-A3-TEXT`, `P3-TEXT` and `WD-C17` are not
  acknowledged or consumed in advance.
- The recommended central question follows one decision: whether a
  parliamentary sentence is sent to human review for possible inclusion in a
  public summary. This is a bounded teaching decision over real governed text,
  not a claim that an identified institution deployed such a system. It does
  not automate publication, deletion, punishment or an inference about the
  speaker's intention.
- D07 remains intact. The existing fairness widget is the sole central widget
  and carries a simulation with a known mechanism. The linked
  ParlaMint-HR/ParlaSent package carries the empirical worked example with
  fallible recorded labels, selection and an inspectable transformation trail;
  the two roles are not interchangeable.
- The recommended selection rule keeps every unit meeting predeclared
  language, country, time and linkage conditions without outcome balancing.
  The source test portion remains an untouched `skup za ispitivanje`; only the
  original training portion is deterministically grouped by stable
  speech/document key into `skup za učenje` and `skup za provjeru`, with no
  cross-split twin or document leakage. No training-file prevalence claim is
  permitted.
- The three linked layers are inspectable speech/sentence text, prepared counts
  and labelled sentences. They support one comparison of normalization, corpus
  boundary and coding procedure, while separating predictive performance from
  construct validity and the recorded reference outcome from truth.
- The full outline follows corpus and unit, label production, split and
  evaluation, threshold and the single confusion-table object, subgroup error
  burdens, procedural fairness, system feedback and monitoring, and language
  models as prediction systems. Machine-learning mathematics, tokenization,
  lemmatization, model training and assessed R production remain excluded.
- G-A2c remains binding: `predviđanje` is canonical; `predikcija` appears only
  in `sustav predikcije`; the full split vocabulary and its three component
  names are fixed; `tablica zabune` is the Chapter 17 name for the same table
  object introduced in Chapter 13; `osjetljivost` never names a rate from that
  table. Exactly two later definition blocks remain permitted:
  `zabilježeni referentni ishod` and `klasifikacijski prag`.
- DigiKat and Eurostat are not repurposed. Any later reach-back retains the
  no-trend-across-2024 rule, the June 2024 method break, denominator 551.712,
  no measured/unmeasured reach or interaction comparison, the visible unsmoothed
  2024 gap, and Eurostat's single 2025 cross-section with source flags.
- `OA-G-A4-17-BRIEF` is ready and awaiting exactly
  `G-A4-17 accepted as recommended for 26197f84889f1b1caffc25e4bbc171631328adb4 on 2026-08-18.`
  The gate remains `in_progress`; no author decision, chapter reading,
  reader-tested validation, measured reading time or independent terminology
  review is inferred.
- `G-A3-TEXT`, `P3-TEXT` and `WD-C17` remain blocked. Chapter 6 remains
  deliberately `draft`. No external message or release action is claimed.

## G-A4-17 closeout

- Luka Sikic supplied the exact required reply on 18 August 2026 against C16
  closeout commit `26197f84889f1b1caffc25e4bbc171631328adb4`. The accepted
  preparation commit is `cc08688e021c3e2f12662b654d952bd35854c676`; no
  standing delegation was used and no author reading is claimed.
- The accepted brief follows one decision: whether a parliamentary sentence is
  sent to human review for possible inclusion in a public summary. It claims no
  deployed institutional system, automatic publication, deletion, punishment
  or inference about speaker intention.
- The selection contract keeps every unit satisfying predeclared conditions,
  preserves the source test portion as the untouched `skup za ispitivanje` and
  derives training and validation only inside the source training portion by
  stable speech/document grouping. Outcome balancing, prevalence claims and
  record, text-twin, speech or document leakage are excluded.
- The empirical package retains three linked roles: inspectable speech and
  sentence text, prepared counts and labelled sentences with individual coder
  labels, the reconciled recorded-reference label and source split. `w17`
  remains the sole central known-mechanism simulation and does not become an
  empirical ParlaSent widget.
- G-A2c remains exact: `predviđanje` is canonical, `predikcija` survives only
  in `sustav predikcije`, the three split components keep their fixed names,
  `tablica zabune` is the same table object already introduced in Chapter 13,
  and `osjetljivost` never names a confusion-table rate. Only
  `zabilježeni referentni ishod` and `klasifikacijski prag` may later receive
  new definition blocks.
- All 20 governed Chapter 17 content items remain `ratified`. The gate accepts
  no source file, rights conclusion, empirical number, bibliography entry,
  data package, widget change or Chapter 17 prose. `G-A3-TEXT`, `P3-TEXT`,
  `P3-VERIFY` and `WD-C17` retain their separate evidence gates.
- `packet_reviews.G-A4-17` declares no new outgoing handoff because the two
  G-A3-TEXT asks, later packets, 20 content items and Chapter 6 already have
  registered owners. The DigiKat and Eurostat boundaries remain unchanged.
- Chapter 6 remains deliberately `draft`. No reader test, measured reading
  time, independent terminology review, external message or release action is
  claimed.
- No active write lock remains. `G-A3-TEXT` alone is next at sequence 126 and
  is not claimed inside G-A4-17.

## G-A3-TEXT selection and rights closeout

- The tenth thread amendment,
  `A-THREAD-G-A3-TEXT-C17-2026-08-17`, records the strict chain
  `G-A3-TEXT -> P3-TEXT -> P3-VERIFY -> WD-C17 -> C17`. All nine earlier
  thread chains have ended. Every packet retains its own claim, evidence,
  handoff disposition, workflow checks, closeout and local commit; only one
  write lock may exist.
- G-A3-TEXT was claimed from clean G-A4-17 closeout commit
  `7298a62a1c030f80c3d65443e8d311c76e1b1205`. Its bounded write set contains
  only the dated decision report, the tenth amendment record and the three
  workflow-control views. No chapter, data, catalogue, bibliography, widget or
  shared registry is owned.
- `H-P1B-DATA-LIC-003` was consumed before claim. Its final delivery preserves
  both incoming `bundled`, `promoted: false`, empty-file states and does not
  convert a general public licence into a completed exact package record.
  `H-P3-CATALOG-001` was acknowledged before substantive work and consumed at
  closeout. Both catalogue entries still have `promoted: false`, empty files,
  null checksums and no promotion-log entry; a decision gate promoted nothing.
- The official records pin ParlaMint 5.0 `ParlaMint-HR.tgz` at MD5
  `b852098ae5c2561aef1de43f44e09a77` under CC BY 4.0 and ParlaSent 1.0
  `ParlaSent_BCS.jsonl`/`ParlaSent_BCS_test.jsonl` at their published MD5s
  under CC BY-SA 4.0. Only metadata and licence pages were inspected; no corpus
  byte was retrieved.
- The recommended selection keeps every row whose source field demonstrably
  marks Croatia in the two BCS files, preserves the selected source test rows
  as the untouched `skup za ispitivanje`, removes training documents that
  cross that boundary and derives grouped training/validation partitions only
  inside the remaining source-training documents. The public README documents
  the training schema but not a separate test schema, so absent test-country or
  stable-link fields fail closed at P3-TEXT. ParlaMint-HR contributes only
  uniquely linked enclosing speeches and necessary metadata, never the full
  398 MB corpus.
- The source records expose an important label-production asymmetry rather than
  a blocker to hide: training rows have two coder labels plus reconciliation,
  whereas test rows were labelled by one trained annotator. The package must
  retain `put_oznake`; it may not invent two test labels or reconciliation.
  Actual one-to-one linkage and no-leakage remain fail-closed P3-TEXT byte-level
  tests.
- The three proposed views are speech-level context, minimal prepared
  length/linkage measures and sentence-level labels. Their sole analytical
  consumer is WD-C17 across its HTML, PDF, DOCX, no-code and print routes. No
  prevalence, causal, intention or out-of-corpus generalisation claim is
  admitted.
- Rights remain separate by file. ParlaMint-only speech and measure outputs
  use CC BY 4.0. Every ParlaSent-derived labelled output and every truly joined
  derived output uses CC BY-SA 4.0 with the required ShareAlike offer. Each
  source receives its own creators/title/version/publisher/handle/licence/change
  attribution. This is compatible with the repository's existing file-level
  data licences and does not relicense MIT code, CC BY generated data, separate
  ParlaMint-only files or the whole book.
- `OA-G-A3-TEXT-SELECTION` and `OA-G-A3-TEXT-RIGHTS` remain separate and are
  both `done`. Luka Sikic accepted each recommendation by its exact dated reply
  against `7298a62a1c030f80c3d65443e8d311c76e1b1205`. No rights-holder
  permission is claimed and none was sought.
- `H-G-A3-TEXT-001` carries every source-byte, schema, Croatian-row, unique-link,
  split, label-path, checksum, reconciliation, attribution, promotion and
  fail-closed obligation into `P3-TEXT` at `before_start`. It also records that
  `G-A3-TEXT` may never be used as the promoting gate.
- Chapter 6 remains deliberately `draft`; all 20 Chapter 17 content items
  remain `ratified`; Chapter 17 and w17 remain unchanged. No author reading,
  reader-tested validation, measured reading time, independent terminology
  review, external message or release action is claimed.
- G-A3-TEXT released its lock before the separate P3-TEXT claim. P3-TEXT is now
  active from clean closeout commit `e948cf2aaae2f24fb600d44898d3fcdbc1e99e2e`;
  `H-G-A3-TEXT-001` was consumed before the first substantive edit. No source
  byte had been retrieved at claim time, and `P3-VERIFY` remains blocked.

## P3-TEXT fail-closed linkage blocker

- Only the four ratified official files were retrieved into
  `data/_kandidat/p3-text/`. Their published MD5 values all match. The candidate
  directory, the 417,667,764-byte archive and its 913,642,410-byte extracted
  plain-text view are git-ignored and do not enter the packet commit.
- The literal ParlaSent test schema does contain `country`, `document_id` and
  `sentence_id`; there are 1,336 source rows with `country = HR`. Thus the
  geographic test condition passes without inference.
- `scripts/check-text-package.py` links only within the same date, requires the
  entire normalized labelled sentence, prefers a matching source
  `document_id`, then an exact unique speaker/content link, and uses no fuzzy
  nearest match or first-row tie break.
- The reproducible audit reports `test_linked=1297`, `test_no_link=24` and
  `test_ambiguous=15`. The accepted G-A3-TEXT rule requires exactly one link
  for every selected Croatian test row and forbids dropping an inconvenient
  row, so the package fails before materialisation.
- The same audit reports 1,387 Croatian training rows, of which 1,340 link,
  18 have no link and 29 are ambiguous. Twenty numeric source document IDs and
  40 resolved ParlaMint speech IDs cross the source train/test boundary. Those
  overlaps would require grouped training removal, but cannot repair the 39
  test blockers.
- Default validation exits 1. `--expect-blocker` exits 0 only when the exact
  1,297/24/15 signature is reproduced. Missing-test-country and source-MD5
  negative fixtures each exit 1 for their injected defect.
- No teaching output was created by the failed joined route. Its audit remains
  historical evidence and was not weakened, guessed or silently filtered.
- `OA-P3-TEXT-LINKAGE-RESEARCH` is `done`. Luka Sikic supplied the exact dated
  reply tied to the observed ParlaMint-HR 5.0 and ParlaSent BCS test SHA-256
  values. `A-P3-TEXT-LINKAGE-RESEARCH-2026-08-18` now permits only bounded
  research over official, versioned and licensed ParlaMint-HR editions; it
  accepts no replacement source, right, output, promotion or row removal.
- The bounded research is complete. ParlaMint-HR 1.0 and 2.1 cover only
  2016-11-15 through 2020-05-17, while 873 selected Croatian test rows predate
  2016. ParlaMint-HR 3.0 is the only temporally possible full-range official
  edition, but its published-MD5 archive reproduces the exact 1,297/24/15
  blocker. Releases 4.0, 4.1 and 5.0 postdate ParlaSent 1.0.
- The original ParlaSent paper identifies CROCorp DOI
  `10.5281/zenodo.6521372`, not a ParlaMint-HR edition, as the Croatian source
  corpus. CROCorp was not selected or downloaded. The full evidence is in
  `notes/reports/p3-text-linkage-research-2026-08-18.md`.
- `OA-P3-TEXT-ROUTE` is `done`. Luka Sikic supplied the exact dated reply tied
  to both unchanged ParlaSent source SHA-256 values. The accepted route retains
  every Croatian test row and label-production path, removes grouped
  train/test leakage, publishes one sentence-level table under CC BY-SA 4.0,
  and removes every speech join, context field, ParlaMint-only output and
  three-layer promise. The reply accepts no finished package.
- The accepted redesign produced only `data/parlament_oznake.csv`: 2,698 rows,
  comprising 1,090 learning, 272 validation and all 1,336 Croatian test rows.
  Twenty overlapping documents remove 25 training rows before the grouped
  SHA-256 split. Output MD5 is `55b1c4263009ab783911f094907312d9` and SHA-256
  is `0f5b4221b583c54fa6996efb33e07541896a83219541029f4c677b56fae5f0ef`.
- The output preserves the asymmetric label paths and explicit source-missing
  marker. It carries no speaker, party, gender, year, term, date, ruling,
  speech or institutional deployment context. `data/parlament_govori.csv` and
  `data/parlament_mjere.csv` remain absent.
- The file-level notice records ParlaSent 1.0, its authors, title, publisher,
  handle, exact source checksums, transformations and CC BY-SA 4.0. No special
  rights-holder permission is claimed.
- `parlasent` is promoted only by P3-TEXT with the existing G-A3-TEXT
  ratification record and bidirectional promotion-log reconciliation.
  `parlamint_hr` remains unpromoted with null checksum and `promoted_by`, empty
  files and no log entry.
- Builder and normal text validation pass byte for byte. Catalogue validation
  passes with 20 packages and 6 promotions; generic data integrity passes with
  50,300 rows, 22 declared and validated snapshots and no undeclared file; all
  51 expected-failure fixtures pass, including seven text-specific corruptions.
- `H-P3-DZS-003` is consumed with all six rules evidenced. P3-TEXT records
  `H-P3-TEXT-001` for independent P3-VERIFY aggregation,
  `H-P3-TEXT-002` for WD-C17 interpretation and rights constraints, and
  `H-P3-TEXT-003` for the later cross-package `data/README.md` reconciliation.
- P3-TEXT is `accepted` and its lock is released. P3-VERIFY is the sole next
  permitted packet; WD-C17 and C17 remain blocked.

## P3-VERIFY closeout

- P3-VERIFY was separately claimed from clean P3-TEXT closeout `2ef8973`.
  `H-P3-TEXT-001` was acknowledged and consumed before substantive
  aggregation.
- The gate aggregates exactly `P3-VERIFY-A`, `P3-VERIFY-B`, `P3-VERIFY-C`,
  `P3-VERIFY-D` and `P3-TEXT`. Each structured evidence record and source state
  was read completely and each reusable deterministic check was rerun.
- Generated snapshots, DZS, DIP, DigiKat, Eurostat, Chapter 12 evidence, ESS
  and ParlaSent all reproduce their route-specific values. P3-TEXT again
  returns 2,698 rows and output SHA-256
  `0f5b4221b583c54fa6996efb33e07541896a83219541029f4c677b56fae5f0ef`.
- The shared integrity ladder passes: catalogue 20/6/22, data integrity 50,300
  rows and 22/22 snapshots, 46 citations, 49 definitions, 166 spine forms, all
  figures, 17 widgets and their parity, tokens, inventory, architecture,
  assessment and identity briefs.
- All expected failures are effective: 51 data/catalogue/text cases, 7
  integrity lanes, 6 widget-parity cases, 6 DIP, 9 ESS, 2 Chapter 12 evidence
  and 3 workflow cases.
- All six Chapter 7–12 Git blob IDs exactly match the accepted reacceptance
  manifest. The legacy values labelled SHA-256 are not raw Git-blob SHA-256
  hashes; `H-P3-VERIFY-001` assigns that nonblocking convention reconciliation
  to `P8-META` so release metadata cannot repeat an undocumented checksum
  method.
- No prerequisite source or book artifact changed. P3-VERIFY is `accepted`,
  its lock is released, and `WD-C17` is solely next; C17 remains blocked.

## WD-C17 closeout

- WD-C17 was separately claimed from clean P3-VERIFY closeout `11b2b75`.
  `H-P0-REGISTER-007` and `H-P3-TEXT-002` were consumed before claim; all six
  applicable `before_close` handoffs were acknowledged before substantive work
  and consumed with final-state evidence.
- Final Chapter 17 SHA-256 is
  `7e8ff74127f77519434b50afbce50c8354bf019b6a7a2f46684a05c2ecc37e6f`,
  git blob `86e387bbd0df139762001dd22d079d1a51a96c77`. The source has 12 sections,
  2.767 prose words, exactly two definitions, one central widget, 12 terms and
  a complete six-question/six-dimension boundary map.
- The ParlaSent-only worked example preserves 2.698 rows and the
  1.090/272/1.336 split. It makes no prevalence, speaker-intention, causal,
  deployment-effect or out-of-corpus performance claim and reconstructs no
  ParlaMint join.
- The two transparent coder-vote rules reproduce 122/16/0/134 and
  100/1/22/149. The source distinguishes those rules from a classifier
  threshold and model probability, and treats negative sentiment as an
  osporiva editorial policy rather than a data-given objective.
- All 20 WD-C17 items materially pass but remain `ratified` for C17. The
  superseding `A-P3-TEXT-ROUTE-2026-08-18` governs the amended
  boundary-sensitivity evidence; the obsolete three-layer ParlaMint route is
  not reinstated.
- w17 and its adapter use the same explicit non-caching generator. All 17
  parity pairs pass at unchanged tolerances; seven negative fixtures, including
  `w17-normal-cache-asymmetry`, fail closed as intended.
- The concept graph is fresh at 51 nodes and 642 edges; terminology has 51 of
  52 approved live definitions and zero divergences. Style, structure, figures,
  citations, concepts, terminology, manuscript, spines, inventory,
  architecture, assessment, tokens, catalogue, data, text-package, widget and
  parity checks all pass.
- Fresh isolated renders pass on the exact final source: HTML SHA-256
  `6a20927ad3d0775b08adee53858267282ef391e0a7d2e916283f23f89c183603`,
  PDF `PDF_BUILD_OK` SHA-256
  `d638223cf2c42813cfb24b35f6d631858fdd6d9a67764c6997d7283a4ec7fea1`
  and DOCX SHA-256
  `0e939a6d5cadffe2bae1ed373af9713d578a16e639727a46edb3381505e1ba86`.
  One earlier final PDF attempt failed closed on a transient Windows rename,
  removed partial/stale outputs and is not used as evidence.
- Six independent final critics confirm the same final blob and report zero
  fatal, major, minor or useful-improvement findings. Earlier diagnostic and
  intermediate rounds are recorded but are not final evidence.
- WD-C17 records no new outgoing handoff because every future effect already
  has a named owner. Chapter 17 remains `draft`; C17 is next but unclaimed and
  requires the exact author reply. No author reading, release action or
  external message is claimed.

## C17 closeout

- Luka Sikic supplied the exact reply
  `C17 accepted for bff7106e156a49b51fc55ca4b11c9cd2fc6645f8 on 2026-08-19`.
  Its commit and date exactly match the prepared gate contract.
- The accepted source remains SHA-256
  `7e8ff74127f77519434b50afbce50c8354bf019b6a7a2f46684a05c2ecc37e6f`, git
  blob `86e387bbd0df139762001dd22d079d1a51a96c77`. No chapter prose, data,
  bibliography, registry of terms, widget, figure or render artifact changed.
- All six final critics address that same blob. The panel has zero fatal,
  major, minor or useful-improvement findings, so no separate finding
  disposition is required.
- The narrow ledger disposition advances only `17-doba-algoritama` from
  `draft` to `coauthor_review` and the 20 items named in the acceptance package
  from `ratified` to `accepted`. It records neither author reading nor a
  `final` stage.
- The ParlaSent-only contract remains controlling. The 2,698-row package,
  output SHA-256 `0f5b4221b583c54fa6996efb33e07541896a83219541029f4c677b56fae5f0ef`,
  rights split and absence of a reconstructed ParlaMint join remain unchanged.
- C17 creates no new outgoing handoff. Chapter 6 and Chapter 18 remain
  `draft`; Chapters 7–16 retain their accepted states. The C17 write lock is
  released and `WD-PART` is now the sole next permitted packet, but it was not
  claimed inside C17.

## Eleventh thread amendment — WD-PART through P5-CLOSURE-01

- Author and editor Luka Sikic authorised the next five packets on 19 August
  2026 with the words "and here we go for the next five packets." The new,
  distinct decision `A-THREAD-WD-PART-P5-CLOSURE-01-2026-08-19` fixes the
  strict chain `WD-PART -> WE-C18 -> C18 -> P5-CLOSURE-00 -> P5-CLOSURE-01`,
  exactly catalogue sequences 131 through 135. All ten earlier thread chains
  have ended and supply no continuing authority.
- The amendment changes only the ordinary stop-after-one-packet rule. Each
  packet keeps its own lock, claim and closeout checks, evidence, handoff
  disposition and scoped local commit. C18 still stops for exactly
  `C18 accepted for <commit> on <date>`; no author reading is claimed.
- WD-PART owns only the Part V bridge and cumulative self-check with its six
  governed items; no delivery targets it. An evidence-only closeout is
  preferred; any genuinely required bounded repair follows the WB-PART and
  WC-PARTS precedent. WE-C18 consumes `H-G-A2D-005` before claim and handles
  its four `before_close` deliveries at their gates.
- The decision record is
  `notes/reports/wd-part-p5-closure-01-thread-amendment-2026-08-19.md`. This
  control record changes no chapter prose, registry stage, data file, figure,
  widget or generated artifact, and claims no packet.

## WD-PART closeout

- `WD-PART` was claimed separately from clean amendment commit `be36020` and
  closed evidence-only on that exact source state. Chapters 13–17 retain git
  blobs `e7ff4e8a`, `6ef3a218`, `aa644049`, `99e20c58` and `86e387bb`; no
  chapter prose, chapter-ledger entry, data, bibliography, term, widget,
  figure or generated artifact changed.
- The Part V vertical slice satisfies the one-dataset model-family spine,
  dependence stopping rule, cumulative AI thesis and competence ladder,
  Chapter 17 sending-side transition, 6 × 6 map and answerable cumulative
  self-check. Five governed items advance to `accepted`.
- `R27-C17-18-transition` returns to `ratified`: Chapter 17 explicitly hands
  threshold, error burdens, monitoring, appeal and responsible delegation to
  the finale, but the live Chapter 18 draft does not yet perform or explicitly
  bound that task. `H-WD-PART-001` assigns the receiving side to `WE-C18` and
  final item acceptance to `C18`.
- Both independent read-only continuity critics confirmed the same manifest.
  The combined panel has zero fatal, zero major and three nonblocking minor
  findings. All three are displayed and consciously declined as reasons to
  reopen an already accepted source; the synthesis records the exact
  disposition.
- Style, structure, figures, citations, concepts, terminology, manuscript,
  spines, architecture, assessment, identity, tokens, catalogue, data, text,
  widgets and parity pass. Targeted HTML, approved-wrapper PDF and wrapper
  DOCX pass on the isolated exact source; public routes exclude the protected
  self-check answer.
- `H-WD-PART-001` is the only new future-relevant effect. No delivery targeted
  `WD-PART`; nothing owned by another packet was acknowledged or consumed.
  Chapter 6 and Chapter 18 remain `draft`; Chapters 13–17 remain
  `coauthor_review`.
- The WD-PART write lock is released. `WE-C18` is solely next but remains
  unclaimed; push, merge, tag, archive, deployment and publication remain
  unauthorised.

## WE-C18 closeout

- `WE-C18` was claimed separately from clean WD-PART closeout `d1b8e8e` only
  after `H-G-A2D-005` was consumed at `before_start`. D15 is fixed as the
  course's dated policy v1.0 of 2026-08-04, not a university regulation,
  legal conclusion or empirical reidentification claim.
- All five `before_close` deliveries were acknowledged before the first source
  edit: the one-definition map, whole-book prerequisite, fail-closed concept
  reconciliation, R04 timing boundary and Chapter 17 receiving-side handoff.
- The packet owns Chapter 18, the same-packet concept ledger/live count/graph
  reconciliation, the narrow addition of WE-C18 to the existing ParlaSent
  consumer list, its report and six-critic evidence, and the three control
  views. It does not own Chapter 17, Appendix F, routes, chapter-ledger,
  assessment closure or generated render artifacts.
- The final source has SHA-256 `5aa91d8b…` and Git blob `d71b8f5…`. It keeps
  the explanatory simulated study, adds one governed ParlaSent transfer
  without a new method, remains widget-free and whole-book cumulative, and
  preserves one extended worked example.
- Exactly one `#def-paket-dokaza` block, eleven `.pojam` anchors, a matching
  concept-ledger entry, live count 52 and a regenerated 52-node graph move
  together. Concept debt is zero and the graph is fresh.
- All five `before_close` deliveries are consumed with exact final-source
  evidence. `R04-C18-whole-prerequisites` records only its source half and
  remains ratified for P5-ROUTES. `R27-C17-18-transition` records both source
  sides and remains ratified for C18.
- All thirteen WE-C18 items materially pass but return to `ratified` because
  only the author gate may accept them. Chapter 18 remains `draft` and the
  chapter ledger is unchanged.
- All six final critics read the same immutable source. The panel is unanimous
  at zero fatal and zero major; every small and useful finding is displayed and
  dispositioned in the synthesis.
- Targeted HTML, approved-wrapper PDF and wrapper DOCX pass in an isolated
  worktree. Style, structure, figures, citations, concepts, terminology,
  manuscript, spines, architecture, assessment, identity, tokens, catalogue,
  data, text package, widgets and parity pass.
- `H-WE-C18-001` is the one new future-relevant effect and targets
  P6-EVIDENCE for bibliographic types. The public catalogue-view observation
  is already owned by `H-P3-CATALOG-002` and is not duplicated.
- The WE-C18 lock is released. `C18` alone is next but is not yet claimed. No
  author reading, external action, push, merge, tag, archive, deployment or
  publication is claimed or authorised.

## C18 closeout

- Luka Sikic supplied the exact reply
  `C18 accepted for be70fef341c46103b7252c3dd6b5c76c9545072e on 2026-08-19`.
  Its commit and date exactly match the prepared gate contract.
- The accepted source remains SHA-256
  `5aa91d8b4b39ed93004f0b009441cc2fb32f97a551762e51365f8171b20beb88`, git
  blob `d71b8f511acda07986a17bb39506078458f5fe65`. No chapter prose, data,
  bibliography, terminology, spine, concept graph, widget, figure or render
  artifact changed.
- All six final critics address that same blob. The panel has zero fatal and
  zero major findings. Every minor and useful finding remains displayed in the
  synthesis and is accepted as nonblocking for this edition without reopening
  the source.
- The narrow ledger disposition advances only `18-vase-prvo-istrazivanje`
  from `draft` to `coauthor_review` and the fourteen items named in the
  acceptance package from `ratified` to `accepted`. It records neither author
  reading nor a `final` stage.
- `R09-C18-interval-conclusion` remains accepted with final-source
  revalidation. `R04-C18-whole-prerequisites` remains ratified for P5-ROUTES.
  No other item changes status.
- The C18 delivery of `H-WD-PART-001` is consumed with both exact source blobs,
  the panel and author reply. `H-WE-C18-001` remains pending only for
  P6-EVIDENCE; C18 creates no new outgoing handoff.
- Chapter 6 remains `draft`; Chapters 7–17 retain their accepted states. The
  C18 write lock is released and `P5-CLOSURE-00` is now the sole next permitted
  packet, but it was not claimed inside C18.

## P5-CLOSURE-00 closeout

- `P5-CLOSURE-00` is active from clean C18 closeout
  `5bc054217dd99019f08369285e66c0e07aa0a1f1`. It governs exactly
  `R15-CLOSURE-00` over `chapters/00-predgovor.qmd`; no chapter stage may
  advance and no route may be assembled in this packet.
- The packet and item records, `assessment_unit` contract, solution-record
  schema, D06-two-layer-v1 visibility contract, unit 00 source and assessment
  rules were read in full before claim.
- A full delivery scan of all 104 immutable handoffs found zero delivery whose
  `target_packet` is `P5-CLOSURE-00`. There is therefore no applicable incoming
  handoff to acknowledge or consume; this explicit zero result precedes the
  first substantive edit.
- The packet may settle the storage, identifier, source-anchor and validation
  rules that the ratified contract deliberately left to the first unit packet.
  Those decisions must become one explicit outgoing handoff binding
  `P5-CLOSURE-01` through `P5-CLOSURE-18` and `P5-ROUTES`.
- `config/book-inventory.json#solution_routes` remains empty. No self-study,
  print or instructor route, navigation, push, merge, tag, archive, deployment
  or publication is authorised.
- Five canonical records now live one per JSON file in
  `assessment/solution-records/unit-00/`. They cover the planted-error callout
  and the conceptual, computational, critical and model-revision tiers. Every
  record carries all six canonical components, explicit not-applicable reasons
  where needed, and the complete stable source binding.
- The first-unit decisions are ratified in the checkout-local conventions and
  schema: one-record-per-file storage, non-reused two-digit identifiers,
  matching Quarto anchors and a normalized default-visible prompt SHA-256.
  `H-P5-CLOSURE-00-001` delivers those rules before start to units 01–18 and
  P5-ROUTES.
- Independent source recomputation gives total `50000`, portal `30.202%`,
  networks `26.756%`, gap `3.446` percentage points and count gap `1723`.
  The assessment checker reports five records, five anchors, three numerical
  records, 60 protected strings and zero public-export leaks.
- Isolated targeted renders distinguish default SHA-256
  `c6106e371287353ea2a5e7797a93324cf88cda40a5655c58065588833b847f21`
  from kolegij SHA-256
  `deab6c2180c77c564fb25718e5cf844e4af47cf581ba57f7bcb40ccffb7ac852`:
  the existing protected concise key is absent by default and present only in
  kolegij. The new instructor route remains deliberately unassembled.
- The release-mode AI export rebuild passes for 19 chapters and the post-build
  leak scan proves that no solution-record rubric, alternative or instructor
  note reaches public export inputs. All packet-specific positive checks pass;
  all four assessment and all three workflow negative fixtures fail closed.
- `P5-CLOSURE-00` advances exactly `R15-CLOSURE-00` and creates no chapter-stage
  change. The write lock is released; `P5-CLOSURE-01` is the sole next permitted
  packet and remains unclaimed.

## P5-CLOSURE-01 closeout

- The workflow checker passed from clean P5-CLOSURE-00 commit `6394899` with
  no active packet and `P5-CLOSURE-01` as the sole next permitted packet.
- `P5-CLOSURE-00` changed neither the chapter ledger nor
  `config/book-inventory.json`; exactly its packet record and
  `R15-CLOSURE-00` advanced, all chapter stages stayed unchanged and
  `solution_routes` remained an empty array.
- The packet record, governed item, complete unit 01 source, assessment
  registry, solution-record schema and the sole applicable incoming handoff
  were read before claim.
- `H-P5-CLOSURE-00-001` is acknowledged and consumed at `before_start`. Its
  one-record-per-file storage, stable identifier, matching-anchor,
  normalized-prompt-fingerprint, six-component schema, D06-two-layer-v1
  visibility and no-route-assembly decisions remain binding.
- The sole write lock owns only the unit 01 source anchors, five unit 01
  records, its independent checker extension, one closeout report and the three
  canonical control files. No route, navigation, external action or chapter
  stage change is authorised.
- Five schema-valid records now close the planted-error callout and all four
  Zadaci tiers under unit-record state
  `468d2505d0f233c48d83d9e08548a9d5fdd59b487e89d9485a02ae67660b2886`.
  The chapter diff adds exactly five matching identifiers and changes no prose.
- Independent recomputation from the CSV and prompt yields portal `23.26998%`,
  print `26.54995%`, networks `21.23636%`, a print-minus-networks gap of
  `5.31359` percentage points and equal-weight Simpson aggregates of `50.00%`
  and `60.00%`. The print path is a hand calculation and the widget is only an
  optional check.
- Actual isolated full-source renders execute all thirteen blocks. Default HTML
  SHA-256 `045f70dbf8a4aaaf2f1970ac9178ba4af02c7f58b5649f129746f980994b6341`
  omits the existing protected key, while `kolegij` SHA-256
  `45ff7846961256e66202af08876b92dff8fa5d202a06314ac4e9b1bbcd02c662`
  includes it. Both carry all five anchors and neither carries record-only
  protected content.
- Release-mode AI export passes for 19 chapters and the checker finds zero
  leaks among 124 protected record strings. The generated export artifacts are
  restored to their exact pre-check Git state; `solution_routes` remains empty.
- Assessment, book architecture, style, figure and JSON checks pass. The two
  unchanged pre-existing structure candidates are recorded without expanding
  this packet. All four assessment fixtures and all three workflow fixtures
  fail closed for their injected defects.
- `packet_reviews.P5-CLOSURE-01` declares all future effects recorded with an
  empty outgoing list. The chapter ledger is unchanged, the write lock is
  released, exactly `R15-CLOSURE-01` advances and `P5-CLOSURE-02` becomes the
  sole next permitted packet without being claimed.

## P5-CLOSURE-02 closeout

- The workflow checker passed from clean P5-CLOSURE-01 commit `c7b3b72` with
  no active packet and `P5-CLOSURE-02` as the sole next permitted packet.
- `P5-CLOSURE-01` changed neither the chapter ledger nor
  `config/book-inventory.json`; exactly its packet record and
  `R15-CLOSURE-01` advanced, all chapter stages stayed unchanged,
  `solution_routes` remained an empty array and its outgoing list was empty.
- The packet record, governed item, complete unit 02 source, assessment
  registry, solution-record schema and sole applicable incoming handoff were
  read before claim.
- `H-P5-CLOSURE-00-001` was acknowledged and consumed at `before_start`. Its
  one-record-per-file storage, stable identifier, matching-anchor,
  normalized-prompt-fingerprint, six-component schema, D06-two-layer-v1
  visibility and no-route-assembly decisions remain binding.
- Five schema-valid records close the planted-error callout and all four Zadaci
  tiers under unit-record state
  `b6c2e6b25ca31aafbf340ad0f4115c16f02aeaa19f6c7d00ae8b661112681e49`.
  The chapter diff adds exactly five matching identifiers and changes no prose.
- Independent recomputation from the authored response rows gives reverse map
  `1→5`, `2→4`, `3→3`, `4→2`, `5→1`; I01 `3,75/4,25`, I02
  `3,75/4,75` and I03 `3,00/3,00`. The print path is a hand calculation from
  the rendered tables and the full-data praktikum is only an optional extension.
- Actual isolated full-source renders execute all seventeen steps. Default HTML
  SHA-256 `3334565053c8dd242ffcbec14634370c446146f35419e9628ea4e57f4855e10b`
  omits the existing protected key, while `kolegij` SHA-256
  `743f7828248df994ffb34c8fdc2d9bf92f49a142932e770de7431951d9bd8799`
  includes it. Both carry all five anchors and neither carries record-only
  protected content.
- Release-mode AI export passes for 19 chapters and the checker finds zero
  leaks among 190 protected record strings. Generated export artifacts are
  restored to their exact pre-check Git state; `solution_routes` remains empty.
- Assessment, book architecture, style, structure, figure and JSON checks pass.
  All four assessment fixtures and all three workflow fixtures fail closed for
  their injected defects.
- `packet_reviews.P5-CLOSURE-02` declares all future effects recorded with an
  empty outgoing list. The chapter ledger is unchanged, the write lock is
  released, exactly `R15-CLOSURE-02` advances and `P5-CLOSURE-03` becomes the
  sole next permitted packet without being claimed.

## P5-CLOSURE-03 closeout

- The workflow checker passed from clean P5-CLOSURE-02 commit `606bfb9` with
  no active packet and `P5-CLOSURE-03` as the sole next permitted packet.
- `P5-CLOSURE-02` changed neither the chapter ledger nor
  `config/book-inventory.json`; exactly its packet record and
  `R15-CLOSURE-02` advanced, all chapter stages stayed unchanged,
  `solution_routes` remained an empty array and its outgoing list was empty.
- The packet record, governed item, complete unit 03 source, assessment
  registry, solution-record schema and sole applicable incoming handoff were
  read before claim.
- `H-P5-CLOSURE-00-001` was acknowledged and consumed at `before_start`. Its
  one-record-per-file storage, stable identifier, matching-anchor,
  normalized-prompt-fingerprint, six-component schema, D06-two-layer-v1
  visibility and no-route-assembly decisions remain binding.
- Five schema-valid records close the planted-error callout and all four Zadaci
  tiers under unit-record state
  `9e4676e4d173f7a5e9df1fac73d8ec45126ddbb12cf52e70fdfd245512f35ecf`.
  The chapter diff adds exactly five matching identifiers and changes no prose.
- Independent recomputation gives ballot total `2.215.209`, turnout gap
  `1.554`, relative gap `0,0701 %`, portal `30,202 %`, TV `21,654 %`,
  their difference `8,548` postotnih bodova and relative difference
  `39,475 %`. The print path exposes every count, permits a calculator or
  spreadsheet and requires no code.
- Actual isolated full-source renders execute all eleven steps. Default HTML
  SHA-256 `342e758497dd0df3d65add3ef1d08b4ac255f58cc3ca3d9c3410dded28ef2e77`
  omits both existing protected regions, while `kolegij` SHA-256
  `a3f21fbbca323beba0064cdf6ba209dbef924a0fcf8293c2f8ec76998b3689d7`
  includes both. Both carry all five anchors and neither carries record-only
  protected content.
- Release-mode AI export passes for 19 chapters and the checker finds zero
  leaks among 254 protected record strings. Generated export artifacts are
  restored to their exact pre-check Git state; `solution_routes` remains empty.
- Assessment, book architecture, style, figure and JSON checks pass. The two
  unchanged structure-lint heuristics retain their accepted WA-C03 disposition.
  All four assessment fixtures and all three workflow fixtures fail closed for
  their injected defects.
- `packet_reviews.P5-CLOSURE-03` declares all future effects recorded with an
  empty outgoing list. The chapter ledger is unchanged, the write lock is
  released, exactly `R15-CLOSURE-03` advances and `P5-CLOSURE-04` becomes the
  sole next permitted packet without being claimed.

## P5-CLOSURE-04 closeout

- The workflow checker passed from clean P5-CLOSURE-03 commit `aa033ba` with
  no active packet and `P5-CLOSURE-04` as the sole next permitted packet.
- P5-CLOSURE-03 changed neither the chapter ledger nor
  `config/book-inventory.json`; exactly its packet record and
  `R15-CLOSURE-03` advanced, all chapter stages stayed unchanged,
  `solution_routes` remained an empty array and its outgoing list was empty.
- The packet record, governed item, complete unit 04 source, assessment
  registry, solution-record schema and sole applicable incoming handoff were
  read before claim.
- `H-P5-CLOSURE-00-001` was acknowledged and consumed at `before_start`. Its
  one-record-per-file storage, stable identifier, matching-anchor,
  normalized-prompt-fingerprint, six-component schema, D06-two-layer-v1
  visibility and no-route-assembly decisions remain binding.
- Five schema-valid records close the planted-error callout and all four Zadaci
  tiers under unit-record state
  `ce1c787842dbac834e367e8339b4c0a56d3d1769321a0ec6d94c6a64d6843b7`.
  The chapter diff adds exactly five matching identifiers and changes no prose.
- Independent recomputation gives the before/wrong/correct join states
  `438/438/710.307`, `3.571/438/5.959.081` and `438/438/710.307`; preset
  mean/median pairs `11,0/11,0` and `16,9/11,5`; first aggregate `81,5444`
  minutes and `30 %`; and source summary 3.604 domains, mean 153,0832,
  median 4 and top-ten share `148.748/551.712 = 26,9612 %`.
- Actual isolated full-source renders execute all 33 steps. Default HTML
  SHA-256 `e4b6efe649e951849d243fd7b6f32c54a52581b761e01802564b9f13b59e4084`
  omits the existing protected key, while `kolegij` SHA-256
  `355861d8622c48b5b6775287b4a5ba8894c08e86bfe7ff81eedb7421e87c5841`
  includes it. Both carry all five anchors and neither carries record-only
  protected content.
- Release-mode AI export passes for 19 chapters and the checker finds zero
  leaks among 318 protected record strings. Generated export artifacts are
  restored to their exact pre-check Git state; `solution_routes` remains empty.
- Assessment, book architecture, inventory, style, figure and JSON checks pass.
  Four unchanged structure-lint heuristics retain their accepted WB-C04/C04
  disposition. All four assessment fixtures and all three workflow fixtures
  fail closed for their injected defects.
- `packet_reviews.P5-CLOSURE-04` declares all future effects recorded with an
  empty outgoing list. The chapter ledger is unchanged, the write lock is
  released, exactly `R15-CLOSURE-04` advances and `P5-CLOSURE-05` becomes the
  sole next permitted packet without being claimed.

## P5-CLOSURE-05 closeout

- The workflow checker passed from clean P5-CLOSURE-04 commit `7d047fa` with
  no active packet and `P5-CLOSURE-05` as the sole next permitted packet.
- P5-CLOSURE-04 changed neither the chapter ledger nor
  `config/book-inventory.json`; exactly its packet record and
  `R15-CLOSURE-04` advanced, all chapter stages stayed unchanged,
  `solution_routes` remained an empty array and its outgoing list was empty.
- The packet record, governed item, complete unit 05 source, assessment
  registry, solution-record schema and sole applicable incoming handoff were
  read before claim.
- `H-P5-CLOSURE-00-001` was acknowledged and consumed at `before_start`. Its
  one-record-per-file storage, stable identifier, matching-anchor,
  normalized-prompt-fingerprint, six-component schema, D06-two-layer-v1
  visibility and no-route-assembly decisions remain binding.
- Five schema-valid records close the planted-error callout and all four Zadaci
  tiers under unit-record state
  `5249d06da045995205eecf7f61cc84bb4e8161a727a0e302f6c15c355275e0c3`.
  The chapter diff adds exactly five matching identifiers and changes no prose.
- Independent recomputation gives widths `0,6/0,6/0,9`, area ratio `1,5` and
  `50 %` excess area; full means `81,5444` and `16,2333`, gap `65,3111` and
  relative gap `80,0927 %`; displayed values give `81,5 - 16,2 = 65,3` and
  `80,1 %`.
- Actual isolated full-source renders execute all 37 steps. Default HTML
  SHA-256 `a997f0193e1b222d4bfbea16d3712ce59acacb88e05157bbec7ac1613bd8eedd`
  omits the existing protected key, while `kolegij` SHA-256
  `35e8c24008bc219c6ae87eba2f444d7069face7ee66c8b4fc566a6a0e8185771`
  includes it. Both carry all five anchors and neither carries record-only
  protected content.
- Release-mode AI export passes for 19 chapters and the checker finds zero
  leaks among 384 protected record strings. Generated export artifacts are
  restored to their exact pre-check Git state; `solution_routes` remains empty.
- Assessment, book architecture, inventory, style, structure, figure and JSON
  checks pass with zero unit 05 style or structure candidates. All four
  assessment fixtures and all three workflow fixtures fail closed for their
  injected defects.
- `packet_reviews.P5-CLOSURE-05` declares all future effects recorded with an
  empty outgoing list. The chapter ledger is unchanged, the write lock is
  released, exactly `R15-CLOSURE-05` advances and `P5-CLOSURE-06` becomes the
  sole next permitted packet without being claimed.

## P5-CLOSURE-06 closeout

- The workflow checker passed from clean P5-CLOSURE-05 commit `0d735dc` with
  no active packet and `P5-CLOSURE-06` as the sole next permitted packet.
- P5-CLOSURE-05 changed neither the chapter ledger nor
  `config/book-inventory.json`; exactly its packet record and
  `R15-CLOSURE-05` advanced, all chapter stages stayed unchanged,
  `solution_routes` remained an empty array and its outgoing list was empty.
- The packet record, governed item, complete unit 06 source, assessment
  registry, solution-record schema and sole applicable incoming handoff were
  read before claim.
- `H-P5-CLOSURE-00-001` was acknowledged and consumed at `before_start`. Its
  one-record-per-file storage, stable identifier, matching-anchor,
  normalized-prompt-fingerprint, six-component schema, D06-two-layer-v1
  visibility and no-route-assembly decisions remain binding.
- Five schema-valid records close the planted-error callout and all four Zadaci
  tiers under unit-record state
  `7bfef8409b75defaa07ede89f5c2ebc5b05170a9f6c65ff28aa50e884f55741e`.
  The chapter diff adds exactly five matching identifiers and changes no prose.
- Independent recomputation gives full-sample `n = 300`, Pearson
  `r = -0,559289` and Spearman `r = -0,680151`; the youngest subgroup has
  `n = 90`, ages 18–24 and Pearson `r = 0,180377`. Eurostat gives 27 and 26
  complete pairs, main `r = 0,449994` and the preserved HR-versus-LU boundary.
- W06 displayed correlations are `-0,85/-0,53/0,40/0,77`; their absolute
  deviations from the four print presets are `0,15/0,33/0,20/0,27`.
- Actual isolated full-source renders execute all 33 steps. Default HTML
  SHA-256 `6cef48e00b87c049be7dfcc71a2c8af2aeca05fbc58b3cabd54fdc578e63f76a`
  omits the existing protected key, while `kolegij` SHA-256
  `15f35081c90649b170a85f76f4e936209de4f6bfc314a2b9887cc0baf2cf8911`
  includes it. Both carry all five anchors and neither carries record-only
  protected content.
- Release-mode AI export passes for 19 chapters and the checker finds zero
  leaks among 444 protected record strings. Generated export artifacts are
  restored to their exact pre-check Git state; `solution_routes` remains empty.
- Assessment, book architecture, inventory, chapter-spine, style, structure,
  figure and JSON checks pass with zero unit 06 style or structure candidates.
  All four assessment fixtures and all three workflow fixtures fail closed for
  their injected defects.
- `packet_reviews.P5-CLOSURE-06` declares all future effects recorded with an
  empty outgoing list. The chapter ledger is unchanged, the write lock is
  released, exactly `R15-CLOSURE-06` advances and `P5-CLOSURE-07` becomes the
  sole next permitted packet without being claimed.

## Closeout P5-CLOSURE-07

- Canonical-state verification began from clean closeout commit `25d7f25` and
  confirmed that P5-CLOSURE-06 changed neither `chapter-ledger.json` nor
  `config/book-inventory.json`; exactly its packet record and
  `R15-CLOSURE-06` advanced, all chapter stages stayed unchanged,
  `solution_routes` remained an empty array and its outgoing list was empty.
- The packet record, governed item, complete unit 07 source, assessment
  registry, solution-record schema and sole applicable incoming handoff were
  read before claim.
- `H-P5-CLOSURE-00-001` was acknowledged and consumed at `before_start`. Its
  one-record-per-file storage, stable identifier, matching-anchor,
  normalized-prompt-fingerprint, six-component schema, D06-two-layer-v1
  visibility and no-route-assembly decisions remain binding.
- Five schema-valid records close the planted-error callout and all four Zadaci
  tiers under unit-record state
  `cdedc04f8b1e5764439ef3c8278e80d8a3392e6833badd80ed87ac79d2b3b2d2`.
  The chapter diff adds exactly five matching identifiers and changes no prose.
- Independent recomputation gives `0,98^5 = 0,9039207968` and complement
  `0,0960792032`, odnosno `9,60792032 %`, only under independence.
- The chapter 3 reachback reconstructs counts
  `10.000/100/90/495/585/10/9.405` and rates
  `90 %/15,3846 %/1 %`, with all six audit questions retained.
- Actual isolated full-source renders execute all 25 steps. Default HTML
  SHA-256 `b526784341ae1ef0a1d4276a903699538d99e8c3a6c111346b1578caf9c2f8c7`
  omits the existing protected key, while `kolegij` SHA-256
  `ce3a9d9a8574d70c2e30f7241c96b4bd6793a8337961704bab08f7424fa70926`
  includes it. Both carry all five anchors and neither carries record-only
  protected content.
- Release-mode AI export passes for 19 chapters and the checker finds zero
  leaks among 504 protected record strings. Generated export artifacts are
  restored to their exact pre-check Git state; `solution_routes` remains empty.
- Assessment, book architecture, inventory, chapter-spine, style, structure,
  figure and JSON checks pass with zero unit 07 style or structure candidates.
  All four assessment fixtures and all three workflow fixtures fail closed for
  their injected defects.
- `packet_reviews.P5-CLOSURE-07` declares all future effects recorded with an
  empty outgoing list. The chapter ledger is unchanged, the write lock is
  released, exactly `R15-CLOSURE-07` advances and `P5-CLOSURE-08` becomes the
  sole next permitted packet without being claimed.

## P5-CLOSURE-08 claim

- The workflow checker passed from clean P5-CLOSURE-07 closeout `bd9fd7a`
  with no active packet and `P5-CLOSURE-08` as the sole next permitted packet.
- The predecessor diff confirms that only its packet record and
  `R15-CLOSURE-07` advanced, while `chapter-ledger.json` and
  `config/book-inventory.json` retained their exact parent blobs and
  `solution_routes` remained empty.
- The packet record, governed item, complete unit 08 source, assessment
  registry, solution-record schema and sole applicable incoming handoff were
  read before claim.
- `H-P5-CLOSURE-00-001` was acknowledged and consumed at `before_start` before
  the first chapter or solution-record edit. Its storage, identifier, anchor,
  prompt-fingerprint, six-component schema, D06-two-layer-v1 visibility and
  no-route-assembly decisions remain binding.
- The only write lock now belongs to `P5-CLOSURE-08`. Its scope is five unit
  08 anchors, five canonical records, the independent checker, one closeout
  report and the three canonical control files. No chapter stage, route or
  external action is authorised.

## P5-CLOSURE-08 closeout

- Five schema-valid records close the planted-error callout and all four
  Zadaci tiers under unit-record state
  `385fcdf5269459337c85970844473d12bd7cecda974ec0680d807c1f48f2c799`.
  The chapter diff adds exactly five matching identifiers and changes no prose.
- The sole planted error is
  `smaller-standard-error-implies-smaller-individual-variation`: larger `n`
  narrows the sampling distribution and its standard error but does not make
  individual observations less dispersed.
- Independent reconstruction of the public synthetic table gives unweighted
  `3/6 = 50,0 %`, weighted `6/16 = 37,5 %` and a shift of `−12,5` percentage
  points. The mandatory print path uses no code, ESS microdata or optional
  effective-sample-size calculation.
- Actual isolated full-source renders execute all 31 steps. Default HTML
  SHA-256 `5c146ad0253053727c8143ac2d5bafffea2057740d4979b92e01b26350e53d0c`
  omits the existing protected key, while `kolegij` SHA-256
  `23ea6fc4e458f85df22e9e79f32153fc579314a067cdb8b9a4b43e272d8ba092`
  includes it. Both carry all five anchors and neither carries record-only
  protected content.
- Release-mode AI export passes for 19 chapters and the checker finds zero
  leaks among 564 protected record strings. Generated export artifacts are
  restored to their exact pre-check Git state; `solution_routes` remains empty.
- Assessment, book architecture, inventory, chapter-spine, style, structure,
  figure-introduction and JSON checks pass. All four assessment fixtures and
  all three workflow fixtures fail closed for their injected defects.
- `packet_reviews.P5-CLOSURE-08` declares all future effects recorded with an
  empty outgoing list. The chapter ledger is unchanged, the write lock is
  released, exactly `R15-CLOSURE-08` advances and `P5-CLOSURE-09` becomes the
  sole next permitted packet without being claimed.

## P5-CLOSURE-09 claim

- The workflow checker passed from clean P5-CLOSURE-08 closeout `75eae1e`
  with no active packet and `P5-CLOSURE-09` as the sole next permitted packet.
- The predecessor diff confirms that only its packet record and
  `R15-CLOSURE-08` advanced, while `chapter-ledger.json` and
  `config/book-inventory.json` retained their exact parent blobs and
  `solution_routes` remained empty.
- The packet record, governed item, complete unit 09 source, assessment
  registry, solution-record schema and sole applicable incoming handoff were
  read before claim.
- `H-P5-CLOSURE-00-001` was acknowledged and consumed at `before_start` before
  the first chapter or solution-record edit. Its storage, identifier, anchor,
  prompt-fingerprint, six-component schema, D06-two-layer-v1 visibility and
  no-route-assembly decisions remain binding.
- The only write lock now belongs to `P5-CLOSURE-09`. Its scope is five unit
  09 anchors, five canonical records, the independent checker, one closeout
  report and the three canonical control files. No chapter stage, route or
  external action is authorised.

## P5-CLOSURE-09 closeout

- Five schema-valid records close the planted-error callout and all four
  Zadaci tiers under unit-record state
  `bfe8a07efe336d48b15197e9c56abc83e7a3f1b924205ccd7a303ac1dcff5a7d`.
  The chapter diff adds exactly five matching identifiers and changes no prose.
- The sole planted error is
  `confidence-level-assigned-to-fixed-parameter-after-observed-interval`:
  confidence belongs to the long-run procedure, while a fixed parameter is
  either inside or outside the already observed interval.
- Independent checks reproduce preset widths `0,619806421393`,
  `0,814602725259` and `0,309903210697`, miss counts `3/0/1`, all five
  analytical/aggregate data values, and the chapter-03 bias reach-back with a
  `3,0965518888`-point margin and biased target `46 %` outside the interval.
- Actual isolated full-source renders execute all 25 steps. Default HTML
  SHA-256 `5d65f33348c5b89eef7203aee798244eaa740d840a240f13a728b0d8c5f8c8c5`
  omits the existing protected key, while `kolegij` SHA-256
  `582ad26617c78ee3a411e5362d95bf215d67ac8ffbcc4fdb6ed8442dac1e9cd4`
  includes it. Both carry all five anchors and neither carries any of the 61
  protected strings from the new records.
- Release-mode AI export passes for 19 chapters and the checker finds zero
  leaks among 625 protected record strings. Generated export artifacts are
  restored to their exact pre-check Git state; `solution_routes` remains empty.
- Assessment, book architecture, inventory, chapter-spine, style,
  figure-introduction and JSON checks pass. Four advisory structure candidates
  predate the packet and remain untouched by the anchor-only source diff. All
  four assessment fixtures and all three workflow fixtures fail closed for
  their injected defects.
- `packet_reviews.P5-CLOSURE-09` declares all future effects recorded with an
  empty outgoing list. The chapter ledger is unchanged, the write lock is
  released, exactly `R15-CLOSURE-09` advances and `P5-CLOSURE-10` becomes the
  sole next permitted packet without being claimed.

## P5-CLOSURE-10 claim

- The workflow checker passed from clean P5-CLOSURE-09 closeout `c938fa7`
  with no active packet and `P5-CLOSURE-10` as the sole next permitted packet.
- The predecessor diff confirms that only its packet record and
  `R15-CLOSURE-09` advanced, while `chapter-ledger.json` and
  `config/book-inventory.json` retained their exact parent blobs and
  `solution_routes` remained empty.
- The packet record, governed item, complete unit 10 source, assessment
  registry, solution-record schema and sole applicable incoming handoff were
  read before claim.
- `H-P5-CLOSURE-00-001` was acknowledged and consumed at `before_start` before
  the first chapter, solution-record or checker edit. Its storage, identifier,
  anchor, prompt-fingerprint, six-component schema, D06-two-layer-v1 visibility
  and no-route-assembly decisions remain binding.
- The only write lock now belongs to `P5-CLOSURE-10`. Its scope is five unit
  10 anchors, five canonical records, the independent checker, one closeout
  report and the three canonical control files. No chapter stage, route or
  external action is authorised.

## P5-CLOSURE-10 closeout

- Five schema-valid records close the planted-error callout and all four
  Zadaci tiers under unit-record state
  `83381cdfa7b8236539d55cc700a9f678f321e47cd12dda435b07f8b46e49abb9`.
  The chapter diff adds exactly five matching identifiers and changes no prose.
- The sole planted error is
  `p-value-interpreted-as-posterior-probability-of-null`: the permutation
  p-value gives a tail probability under the null model, not the probability
  that the null model is true after observing the data.
- Independent checks reproduce population difference `0,743644165673`,
  observed difference `0,640938989801461`, interval
  `0,174811193068577–1,10706678653434`, corrected permutation result
  `65/4001 = 0,0162459385154`, null boundaries and calibration
  `39/800 = 4,875 %`.
- Actual isolated full-source renders execute all 19 steps. Default HTML
  SHA-256 `22fa321ec38f7820afb019b57bd555232bc480e0e906b28ab90deaa9f1c45f2d`
  omits the existing protected key, while `kolegij` SHA-256
  `6b63b55062567926bbd7e98b618fb178fd23701610e16bd96b0c1a5477f4d60c`
  includes it. Both carry all five anchors and neither carries protected
  record-only content.
- Release-mode AI export passes for 19 chapters and the checker finds zero
  leaks among 686 protected record strings. The export ran in the isolated
  project; no generated export artifact is a packet output and
  `solution_routes` remains empty.
- Assessment, book architecture, inventory, chapter-spine, style and
  figure-introduction checks pass. Three advisory structure candidates predate
  the packet and remain untouched by the anchor-only source diff. All four
  assessment fixtures and all three workflow fixtures fail closed for their
  injected defects.
- `packet_reviews.P5-CLOSURE-10` declares all future effects recorded with an
  empty outgoing list. The chapter ledger is unchanged, the write lock is
  released, exactly `R15-CLOSURE-10` advances and `P5-CLOSURE-11` becomes the
  sole next permitted packet without being claimed.

## P5-CLOSURE-11 claim

- The workflow checker passed from clean P5-CLOSURE-10 closeout `8035924`
  with no active packet and `P5-CLOSURE-11` as the sole next permitted packet.
- The predecessor diff confirms that only its packet record and
  `R15-CLOSURE-10` advanced, while `chapter-ledger.json` and
  `config/book-inventory.json` retained their exact parent blobs and
  `solution_routes` remained empty.
- The packet record, governed item, complete unit 11 source, assessment
  registry, solution-record schema and sole applicable incoming handoff were
  read before claim.
- `H-P5-CLOSURE-00-001` was acknowledged and consumed at `before_start` before
  the first chapter, solution-record or checker edit. Its storage, identifier,
  anchor, prompt-fingerprint, six-component schema, D06-two-layer-v1 visibility
  and no-route-assembly decisions remain binding.
- The only write lock now belongs to `P5-CLOSURE-11`. Its scope is five unit
  11 anchors, five canonical records, the independent checker, one closeout
  report and the three canonical control files. No chapter stage, route or
  external action is authorised.

## P5-CLOSURE-11 closeout

- Five schema-valid records close the planted-error callout and all four
  Zadaci tiers under unit-record state
  `8559bfead72e2a2be7c87101957a45828ce2660457144df238ba7f60a7b6f7f1`.
  The chapter diff adds exactly five matching identifiers and changes no prose.
- The sole planted error is `observed-effect-used-for-post-hoc-power`: an
  observed effect from the finished study cannot serve as the independent
  planning effect that supposedly validates that same study.
- Independent checks reproduce portal and print means `4,774584464604993` and
  `5,518228630278064`, gap `0,743644165673071`, pooled standard deviation
  `1,912184863285`, standardized effect `0,388897632207`, four printed and
  analytic power pairs, post hoc power `0,8438926` and target plan 228 per
  group from raw n `227,64002629604767`.
- Actual isolated full-source renders execute all 23 steps. Default HTML
  SHA-256 `9536eaa3f1991f3564a6b0216e38b9b773b8a52042b5c15047e60e15e785248f`
  omits the existing protected key, while `kolegij` SHA-256
  `6bf960c513714b2f921e49f3cac96a01ae413ce926524a3bf96daef7524bafd9`
  includes it. Both carry all five anchors and neither carries protected
  record-only content.
- Release-mode AI export passes for 19 chapters and the checker finds zero
  leaks among 746 protected record strings. The export ran in the isolated
  project; no generated export artifact is a packet output and
  `solution_routes` remains empty.
- Assessment, book architecture, inventory, chapter-spine, style, structure
  and figure-introduction checks pass with zero unit 11 lint candidates. All
  four assessment fixtures and all three workflow fixtures fail closed for
  their injected defects.
- `packet_reviews.P5-CLOSURE-11` declares all future effects recorded with an
  empty outgoing list. The chapter ledger is unchanged, the write lock is
  released, exactly `R15-CLOSURE-11` advances and `P5-CLOSURE-12` becomes the
  sole next permitted packet without being claimed.

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
canonical state. Read AGENTS.md and fully read the four canonical control
files plus the checkout-local Bookwright instructions required by the packet.
Do not rely on prior chat or the installed plugin cache for mutable state.

Verify `active_write_packet: null`, `last_completed_packet: P5-CLOSURE-11` and
`next_permitted_packet: P5-CLOSURE-12`. Confirm that P5-CLOSURE-11 advanced
only `R15-CLOSURE-11`, left every chapter stage unchanged, kept
`config/book-inventory.json#solution_routes` empty, consumed required handoff
`H-P5-CLOSURE-00-001` and declared no new future-relevant effect.

Claim and execute only `P5-CLOSURE-12` as a separate packet. Fully read its
packet record, governed item, assessment registry, solution-record schema,
unit 12 source and every applicable incoming handoff. Acknowledge and consume
`H-P5-CLOSURE-00-001` before the first substantive edit, preserving its
storage, identifier, anchor, prompt-fingerprint, schema, visibility and
no-route-assembly decisions. Implement only unit 12's canonical answer,
independent check, rubric and planted-error closure under D06-two-layer-v1.

Before closeout, run every packet-specific assessment, numerical, profile and
export check; record every future-relevant outgoing handoff or an explicit
no-effect declaration; update the register, handoff ledger and dashboard
together; run the workflow checker and all three negative fixtures; close and
locally commit P5-CLOSURE-12; then stop. Do not claim P5-CLOSURE-13, push,
merge, tag, archive, deploy or publish.
```
