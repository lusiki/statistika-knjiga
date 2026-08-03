---
packet: P1A-C13
date: "2026-08-03"
items:
  - R09-C13-residual-name
  - R09-C13-calibration-power
source_state: "chapter:sha1-9242e057c6602b273368164de6193b08eba5eeb8"
status: passed
---

# P1A-C13 correction and methods evidence

## Bounded scope

This packet implements only `R09-C13-residual-name` and
`R09-C13-calibration-power`. No incoming handoff targets `P1A-C13`, and no
outside ask is required. The chapter now computes adjusted standardized
residuals with `chisq.test(...)$stdres`, names them consistently, displays the
row- and column-margin adjustment in the definition, and limits the absolute
value near two to a qualified orientation rather than separate cell-level
evidence.

Null calibration and power are now separate simulation experiments. The null
runs estimate type-I-error calibration under independence. The alternative
runs hold the respective overall response proportions fixed and introduce one
predeclared association with population Cramer's V of 0.20. All four runs use
Pearson's statistic without Yates correction, the same chi-squared threshold,
and 4,000 repetitions. Undefined one-response-category tables count as
non-rejections and that convention is disclosed in the prose.

No dataset, citation, empirical example, widget, print twin, worked example, or
exercise changed. Separately registered Chapter 13 work on contingency-table
scope, the Part V contract, reach-back exercises, assessment closure, and later
parity or terminology reconciliation was not started.

## Clean-session numerical reproduction

R 4.6.0 was resolved through the checkout launcher. A fresh R process removed
the global environment, extracted the complete Chapter 13 R source with
`knitr::purl`, ran it without cache, and independently asserted the affected
residual, simulation, threshold, and widget/print-twin quantities.

| Quantity | Reproduced value |
|---|---:|
| Teaching sample size | 800 |
| Pearson chi-squared statistic | 149.783992784 |
| Degrees of freedom | 12 |
| Minimum expected frequency | 14.34375 |
| Cramer's V | 0.249819929 |
| Adjusted residual, oldest / television | 6.667711092 |
| Adjusted residual, oldest / social media | -6.626758501 |
| Adjusted residual, youngest / social media | 6.569448258 |
| Adjusted residual, youngest / television | -4.195589607 |
| Null dense 95th percentile | 4.001600640 |
| Null sparse 95th percentile | 3.243243243 |
| Null dense rejection rate | 5.45 % |
| Null sparse rejection rate | 4.05 % |
| Inapplicable sparse null tables | 66 of 4,000 |
| Target population Cramer's V | 0.20 |
| Dense alternative response probabilities | 60 % / 40 % |
| Sparse alternative response probabilities | 16 % / 4 % |
| Dense alternative power | 98.2 % |
| Sparse alternative power | 20.475 % |
| Inapplicable sparse alternative tables | 64 of 4,000 |
| Widget/print moderate-state chi-squared statistic | 32.4 |
| Widget/print moderate-state Cramer's V | 0.45 |

The manually recomputed margin-adjusted formula matched `$stdres` to numerical
tolerance and differed from the Pearson residuals it replaces. The widget
default and the print twin's moderate state remain arithmetically identical;
both display Pearson cell contributions, not the adjusted residual diagnostic.

## Independent statistical-methods reading

An independent read-only `critic_methods` reader checked the complete Chapter
13 source at blob `9242e057c6602b273368164de6193b08eba5eeb8`. The reader
recomputed the adjusted residuals and all four simulation regimes from a clean
session. The hash matched the requested state, no file was modified, and no
fatal, major, or minor concern remained.

The final scores were 5/5 for correctness, assumptions, interpretation, and
precision. The critic passed both registered items, confirmed that the fixed
alternatives have population Cramer's V exactly 0.20, and found the exact
source state acceptable for packet closeout.

## Style, render, and exit evidence

- Checkout-local deterministic `book-style` lint passed with zero candidates.
- The final source received a complete top-to-bottom Croatian prose pass
  against H1--H10. The affected prose introduces no governed colon,
  mid-sentence em dash, mechanical transition, unsupported empirical claim,
  invented citation or number, bold misuse, unexplained notation, or reader
  code burden.
- Structure lint passed with 11 top-level sections, 2,659 prose words, body
  evenness 0.35, and zero candidates. The structure scan retained the vignette,
  five definitions, two conceptual figures with three source variants, one
  divljina callout, both AI callouts, and all four exercise tiers.
- Figure-introduction checking passed for both conceptual figures. The
  all-widget contract also passed for all 17 registered HTML/static pairs.
- The targeted Chapter 13 HTML render passed from the exact final source state
  in a disposable project copy. Required names, values, alternative parameters,
  the no-Yates statement, and `fig-w13` were present; superseded Pearson-
  residual wording was absent. The checkout retained no generated render or AI
  export change.
- Source-diff and whitespace checks passed. The chapter retains seven
  executable R/OJS blocks. Only `s13-vrijednosti` changed; the other six,
  including the widget and print twin, are byte-equivalent after newline
  normalization.

## Forward-effects declaration

No incoming handoff applied and no new future-relevant effect was discovered.
Existing timing and fresh-panel invalidation handoffs cover the later effects
of substantive chapter changes, while already registered Chapter 13 and
terminology packets retain their stable work. This correction therefore
creates no duplicate outgoing handoff.
