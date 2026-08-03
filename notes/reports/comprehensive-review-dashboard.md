---
workflow_schema_version: 1
branch: revision/comprehensive-review
baseline_commit: c163bda524b7081ec6a41d5ab75370f1700b1748
control_implementation_commit: b3463c7b6f7dc7e03a76f74f3a297e2e158e4c6e
active_write_packet: null
last_completed_packet: P1A-C08
next_permitted_packet: P1A-C09
atomic_children: 371
packet_count: 188
source_coverage_sections: 18
unmapped_actionable: 0
forward_handoffs: 15
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
| Gate A1a | Accepted: D01 Chapter 10 correction specification; reviewer Luka Sikic; 2026-08-03 |
| Gate A1b | Accepted: D02 Chapter 14 correction specification; reviewer Luka Sikic; 2026-08-03 |
| Branch | `revision/comprehensive-review` |
| Baseline | `c163bda524b7081ec6a41d5ab75370f1700b1748` |
| Control implementation | `b3463c7b6f7dc7e03a76f74f3a297e2e158e4c6e` |
| Active write packet | None |
| Last completed packet | `P1A-C08` |
| Next permitted packet | `P1A-C09` |
| Review parents | 34 ratified; 2 accepted |
| Atomic child inventory | Complete: 371 stable children; 27 accepted, 5 deferred with reason, 339 ratified; zero unmapped |
| Exact packet catalogue | 188 packets: 17 accepted and 171 ratified, with stable IDs, typed contracts, unique sequence, and just-in-time dependencies |
| Review source coverage | 18 exact section manifests; their fingerprint union equals all 371 children; zero uncovered actionable findings |
| Chapter stages | 19 `draft` |
| Open outside asks | 80 canonical asks remain `drafted_unsent`; `OA-G-A1A-C10-SPEC` and `OA-G-A1B-C14-SPEC` are `done`; 0 external messages sent |
| Invalidated or reopened work | None |
| Failed gates | None; `P1A-C08` passed reproduction, methods, style, structure, figure, render, widget-preservation, source-diff, and closeout checks |

No chapter prose was changed by `P0-OUTSIDE`.

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

Execute only the dashboard's next permitted packet, P1A-C09. Fully read
chapters/09-procjena.qmd, STYLE.md, ENRICHMENT.md,
notes/struktura-knjige.md, the relevant comprehensive-review evidence, and the
checkout-local book-style instructions. Do not rely on the installed plugin
cache for mutable state.

Execute the exact P1A-C09 scope: `R09-C09-normal-not-prediction`,
`R09-C09-bootstrap-validation`, and `R09-C09-bootstrap-failures`. Remove or
correctly bound the generic prediction-interval language; give the bootstrap
median its own appropriate demonstration or narrow the claim; and state the
independence and representativeness assumptions together with the relevant
small-sample, discreteness, and tail limits. Do not start any later packet or
separately registered Chapter 9 repair.

Reproduce every affected result from a clean session, obtain the required
independent statistical-methods reading on the exact Chapter 9 source state,
run the checkout-local deterministic and manual book-style pass, structure and
figure-introduction checks, targeted Chapter 9 render, source-diff and packet
exit checks. Update the register, handoff ledger, and dashboard together,
create one scoped local commit only if every gate passes, and stop before
P1A-C13 or any later packet.
```
