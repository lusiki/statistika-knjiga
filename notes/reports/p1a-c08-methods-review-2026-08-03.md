---
packet: P1A-C08
date: "2026-08-03"
items:
  - R12-C08-srs-boundary
  - R12-C08-complex-design
  - R12-C08-thousand-claim
source_state: "chapter:sha1-b9a435a2ebb1e1371f4069cc8f9a4250459e419f"
status: passed
---

# P1A-C08 correction and methods evidence

## Bounded scope

This packet implements only `R12-C08-srs-boundary`,
`R12-C08-complex-design`, and `R12-C08-thousand-claim`. No incoming handoff
targets `P1A-C08`, and no outside ask is required. The corrected source names
the simple-random-sampling assumptions behind the displayed standard-error,
margin, and sample-size formulas; distinguishes sampling with and without
replacement; and introduces the finite-population correction at the intended
literacy level.

The source now bounds transfer to unequal-probability and clustered designs.
It explains sampling weights, clustering, design effects, effective sample
size, and design-aware uncertainty without adding a complex-survey variance
course. It also qualifies the roughly-thousand-person heuristic by estimand,
design, selection and response, subgroup size, and desired precision.

No dataset, citation, figure, widget, print twin, empirical example, or
exercise changed. The later Chapter 8 survey-realism and weighted-table items,
the explicit no-variance-course boundary, selection/reach-back work, and full
`WC-C08` vertical slice were not started.

## Clean-session numerical reproduction

R 4.6.0 was resolved through the checkout launcher. A fresh R process extracted
all Chapter 8 R chunks with `knitr::purl`, ran them without cache, and asserted
the population-variance convention, the standard-error series, both
finite-population corrections and their predicted standard errors, every
displayed margin and inverted sample-size result, the variance-divisor
simulation, and finite values for every affected simulation result.

| Quantity | Reproduced value |
|---|---:|
| Population size | 50,000 |
| Population SD, divisor N | 1.984099867 |
| Empirical SE of mean, n = 100 | 0.198121218 |
| Formula SE of mean, n = 100 | 0.198409987 |
| Empirical SEs, n = 10, 25, 50, 100 | 0.617434779; 0.405301702; 0.282187210; 0.194162747 |
| Empirical SEs, n = 200, 500, 1,000, 2,000 | 0.140591937; 0.088209377; 0.065032988; 0.043391558 |
| Formula SEs, n = 10, 25, 50, 100 | 0.627427468; 0.396819973; 0.280594094; 0.198409987 |
| Formula SEs, n = 200, 500, 1,000, 2,000 | 0.140297047; 0.088731644; 0.062742747; 0.044365822 |
| FPC, n = 800 of N = 50,000 | 0.991977661 |
| FPC, n = 800 of N = 5,000 | 0.916606804 |
| SD of the 5,000-unit comparison population | 1.966511948 |
| Simulated / FPC-predicted SE, n = 800 of N = 50,000 | 0.069980053 / 0.069585768 |
| Simulated / FPC-predicted SE, n = 800 of N = 5,000 | 0.064017440 / 0.063728643 |
| Margins at n = 400, 800, 1,000, 2,000 | 4.900000000 %; 3.464823228 %; 3.099032107 %; 2.191346618 % |
| Required n for margins 5 %, 4 %, 3 %, 2 % | 385; 601; 1,068; 2,401 |
| Mean variance estimate, divisor n | 3.545547500 |
| Mean variance estimate, divisor n - 1 | 3.939497222 |
| Population variance, divisor N | 3.936652282 |

The corrected numerical block uses the population SD with divisor `N`, which
matches the displayed finite-population formula. It reports the realized
dispersion of the smaller comparison population and separates that difference
from the finite-population effect. The simulations agree with both analytic
benchmarks within the asserted tolerance.

## Independent statistical-methods reading

An independent read-only `critic_methods` reader first checked the complete
Chapter 8 source at blob `46ebd6141c72a880fac9a139c78f5883ae183307`.
It found no fatal defect and confirmed that all three packet corrections were
substantially successful. It requested one major wording repair and three
minor precision repairs: include population dispersion in the widget-width
claim, align the FPC variance convention and comparison, attach the normal
approximation to the 1.96 margin and inverse sample-size calculation, and make
the summary say that design-aware uncertainty uses weights, clusters, and
strata.

Those four points were corrected. The same critic then reread the complete
revised source at blob `b9a435a2ebb1e1371f4069cc8f9a4250459e419f`.
The hash matched before and after the reading, no file was modified, every
first-pass concern was resolved, and no fatal, major, or minor concern
remained. The final scores were 4/4 for correctness, assumptions,
interpretation, and precision. The critic passed all three registered items
and the P1A-C08 methods gate.

## Style, render, and exit evidence

- Checkout-local deterministic `book-style` lint passed with zero candidates.
- The final source received a complete top-to-bottom Croatian prose pass
  against H1--H10. It adds no governed colon, mid-sentence em dash, mechanical
  transition, unsupported empirical claim, invented citation or number, bold
  misuse, unexplained notation, or reader code burden.
- Structure lint passed with 11 top-level sections, 3,754 prose words, body
  evenness 0.36, and zero candidates. The structure scan retained the
  vignette, three definitions, three conceptual figures with four source
  variants, one divljina callout, both AI callouts, and all four exercise
  tiers.
- Figure-introduction checking passed for all three conceptual figures. The
  all-widget contract also passed for all 17 registered HTML/static pairs.
- The targeted Chapter 8 HTML render passed from the exact source state in an
  isolated output directory. Eleven required rendered claims and numerical
  outputs were present, and both superseded overbroad claims were absent.
  Generated AI-export changes were inspected and restored to their pre-packet
  state.
- Source-diff and whitespace checks passed. The chapter retains 14 executable
  R/OJS blocks. Only the hidden `s8-vrijednosti` block changed to reproduce the
  variance convention and FPC benchmarks; the remaining 13 figure, table,
  widget, print-twin, and worked-example blocks are unchanged.

## Forward-effects declaration

No incoming handoff applied and no new future-relevant effect was discovered.
Later Chapter 8 work retains stable register items, packet dependencies, and
`OA-C08-ACCEPTANCE`. The correction therefore creates no duplicate outgoing
handoff.
