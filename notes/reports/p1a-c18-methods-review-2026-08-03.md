---
packet: P1A-C18
date: "2026-08-03"
items:
  - R09-C18-interval-conclusion
source_state: "chapter:sha1-f291e63173892eca483ed9c9e89df70be5bb1bd1"
status: passed
---

# P1A-C18 correction and methods evidence

## Bounded scope

This packet implements only `R09-C18-interval-conclusion`. No incoming handoff
targets `P1A-C18`, and no outside ask is required for this bounded correction.
The chapter now reports both the aggregate and age-adjusted estimates with
their intervals, describes the small effects of either sign that remain
compatible with the adjusted interval, and rejects an absence conclusion that
the sample cannot support. The known data-generating rule remains explicitly
separate from what the fitted model and interval can establish.

No data, model, executable block, displayed table, figure, exercise, citation,
AI callout, or privacy passage changed. Separately registered Chapter 18 work
on the finale spine, evidence package, sensitivity analysis, transfer,
privacy, reach-back, and final acceptance was not started.

## Clean-session numerical reproduction

R 4.6.0 was resolved through the checkout launcher. A fresh R process extracted
the complete Chapter 18 R source with `knitr::purl`, ran it without a retained
workspace or cache, and asserted the affected estimates, intervals, and source
claims.

| Quantity | Reproduced value |
|---|---:|
| Teaching sample size | 300 |
| Aggregate estimate per 30 minutes | 0.2461455994 |
| Aggregate 95% interval, lower bound | 0.0926660974 |
| Aggregate 95% interval, upper bound | 0.3996251015 |
| Age-adjusted estimate per 30 minutes | -0.0083232067 |
| Age-adjusted 95% interval, lower bound | -0.1863548332 |
| Age-adjusted 95% interval, upper bound | 0.1697084198 |
| Aggregate R-squared | 0.0323458292 |
| Age-adjusted R-squared | 0.1082928039 |
| Aggregate slope p-value | 0.0017622730 |

The aggregate interval lies above zero. The adjusted interval includes zero,
excludes effects as large as the aggregate estimate in either direction, and
retains small effects of either sign. Those facts reproduce the displayed
rounded values and support the revised conclusion without threshold-based
disappearance language.

## Independent statistical-methods reading

An independent read-only `critic_methods` reader checked the complete Chapter
18 source at blob `f291e63173892eca483ed9c9e89df70be5bb1bd1`. The reader ran
the model from a clean R 4.6.0 `--vanilla` session, reproduced the aggregate
estimate of 0.25 with interval [0.09, 0.40] and the adjusted estimate of -0.01
with interval [-0.19, 0.17], and verified their agreement with the source.

The final scores were 5/5 for correctness, assumptions, interpretation, and
precision. No fatal, major, or minor concern remained. The reader accepted the
separation between the interval-compatible conclusion and the known generator,
and found the exact source state acceptable for packet closeout.

## Style, render, and exit evidence

- Checkout-local deterministic `book-style` lint passed with zero candidates.
- The final source received a complete top-to-bottom Croatian prose pass
  against H1--H10. The affected prose introduces no governed colon,
  mid-sentence em dash, mechanical transition, unsupported empirical claim,
  invented citation or number, bold misuse, unexplained notation, or reader
  code burden.
- Structure lint passed with 12 top-level sections, 2,625 prose words, body
  evenness 0.31, and zero candidates. The structure scan retained the vignette,
  one conceptual figure, one divljina callout, both AI callouts, and all four
  exercise tiers.
- Figure-introduction checking passed for the conceptual figure. The all-widget
  contract passed for all 17 registered chapter widgets; Chapter 18 is
  deliberately exempt from the widget requirement.
- The targeted Chapter 18 HTML render passed from the exact final source state
  in a disposable project copy. Both estimates and intervals, the compatible-
  effects interpretation, the absence boundary, and the known-generator
  distinction were present; superseded disappearance language was absent. The
  checkout retained no generated render or AI-export change.
- Source-diff and whitespace checks passed. All six Chapter 18 executable R/OJS
  blocks are unchanged after newline normalization; only the registered prose
  surface changed.

## Forward-effects declaration

No incoming handoff applied and no new future-relevant effect was discovered.
Existing timing and fresh-panel invalidation handoffs cover later effects of
substantive chapter changes, while all separately registered Chapter 18 work
retains its stable items and dependencies. This correction therefore creates
no duplicate outgoing handoff.
