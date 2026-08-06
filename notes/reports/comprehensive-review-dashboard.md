---
workflow_schema_version: 1
branch: revision/comprehensive-review
baseline_commit: c163bda524b7081ec6a41d5ab75370f1700b1748
control_implementation_commit: b3463c7b6f7dc7e03a76f74f3a297e2e158e4c6e
active_write_packet: null
last_completed_packet: C03
next_permitted_packet: WA-PART
atomic_children: 371
packet_count: 188
source_coverage_sections: 18
unmapped_actionable: 0
forward_handoffs: 81
last_updated: "2026-08-06"
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
| Branch | `revision/comprehensive-review` |
| Baseline | `c163bda524b7081ec6a41d5ab75370f1700b1748` |
| Control implementation | `b3463c7b6f7dc7e03a76f74f3a297e2e158e4c6e` |
| Active write packet | None |
| Last completed packet | `C03` |
| Next permitted packet | `WA-PART` |
| Review parents | 32 ratified; 4 accepted |
| Atomic child inventory | Complete: 371 stable children; 155 accepted, 5 deferred with reason, 211 ratified; zero unmapped |
| Exact packet catalogue | 188 packets: 75 accepted, 112 ratified and 1 descoped by author amendment, with stable IDs, typed contracts, unique sequence, and just-in-time dependencies |
| Review source coverage | 18 exact section manifests; their fingerprint union equals all 371 children; zero uncovered actionable findings |
| Chapter stages | 15 `draft`; `00-predgovor`, `01-zasto-statistika`, `02-mjerenje-i-dizajn` and `03-kako-brojke-zavode` at `coauthor_review` |
| Chapter spines | **All 19 ratified**: `00-predgovor` at `G-A2b-PREFACE`; Chapters 1–3 at `G-A2b-I`; Chapters 4–6 at `G-A2b-II`; Chapters 7–9 at `G-A2b-III`; Chapters 10–12 at `G-A2b-IV`; Chapters 13–17 at `G-A2b-V`; `18-vase-prvo-istrazivanje` at `G-A2b-FINALE`. No spine remains unratified |
| Open outside asks | 46 of the 82 canonical asks remain `drafted_unsent`; 30 are `done`; 6 are `withdrawn_with_reason` — the terminology recruitment and sign-off asks, the DZS and DIP rights inquiries, and the two reader-recruitment asks, all withdrawn by the author on 2026-08-05 — the two methods asks, three G-A1c licence/access asks, four G-A1d governance/owner asks, the G-A2a claim-system ask, the five G-A2d policy asks, the preface, Part I, Part II, Part III, Part IV, Part V and finale spine asks, the G-A2c term-map ask, the DZS and DIP selection asks, C00, C01, C02 and C03 acceptance, and the G-A4-03 brief; 0 external messages sent |
| Invalidated or reopened work | `P1A-C02` and `P1A-METHODS` were revalidated evidence-only at the current source state and remain accepted; no prose changed |
| Failed gates | None in `P1-VERIFY`; all twelve prerequisites pass independently. The pre-existing `_quarto.yml` checksum mismatch remains separately recorded in `H-P1C-EXPORT-002` for `P7-FREEZE` and `P8-META` |
| Phase 2 exit condition | **4 of 5 clauses met.** `R04 is closed` is **not** met and is structurally unmeetable in Phase 2: four of its 21 required children are owned by `WC-C11` (Phase 4), `P5-ROUTES` (Phase 5) and `WE-C18` (Phase 4). Recorded as a plan-versus-register conflict in `H-P2-VERIFY-001`; not forced, not redefined |

No chapter prose was changed by `P0-OUTSIDE`.

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

Verify that C03 is accepted against WA-C03 commit
`72f774a3b302e6beca14730ac82727be92f29be1`, that the Chapter 3 ledger stage is
`coauthor_review`, and that `WA-PART` is the sole `next_permitted_packet`. Then
execute only `WA-PART`: Part I bridge, cumulative self-check, empirical-data
spine, and AI/data route. Read every WA-PART governed item and all applicable
incoming handoffs before claiming the packet; acknowledge each required
before-close delivery before the first substantive edit and record a concrete
disposition before closeout. Use the checkout-local shared registries as the
only mutable Bookwright state, follow STYLE.md for every prose edit, obtain the
required current part-continuity evidence, run applicable deterministic checks
and targeted renders, update the register, handoff ledger and dashboard
together, make one bounded local packet commit, and stop. Do not start
`G-A3-DIGIKAT`. Push, merge, tag, archive and deploy remain unauthorised.
```
