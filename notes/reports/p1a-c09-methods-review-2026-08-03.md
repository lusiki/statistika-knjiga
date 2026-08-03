---
packet: P1A-C09
date: "2026-08-03"
items:
  - R09-C09-normal-not-prediction
  - R09-C09-bootstrap-validation
  - R09-C09-bootstrap-failures
source_state: "chapter:sha1-67380c04d31d3370b1ff63e2533d70a12338ba0d"
status: passed
---

# P1A-C09 correction and methods evidence

## Bounded scope

This packet implements only `R09-C09-normal-not-prediction`,
`R09-C09-bootstrap-validation`, and `R09-C09-bootstrap-failures`. No incoming
handoff targets `P1A-C09`, and no outside ask is required. The corrected source
relabels mean plus or minus 1.96 sample standard deviations as a descriptive
normal-rule range conditional on an approximately normal distribution of
individual observations. It explicitly distinguishes that range from an
individual prediction interval and from the confidence interval for a mean.

The bootstrap-median example now demonstrates construction of one percentile
range rather than coverage. The source states that the earlier repeated
z-interval experiment concerns a mean and cannot validate the percentile
bootstrap for a median. It also states the empirical-representativeness and
independence/exchangeability assumptions, preserves paired, grouped, and
repeated-observation units, and makes the small-sample, discreteness, missing-
tail, heavy-tail, and extreme-percentile limits visible.

The independent reading found one literal count mismatch in the earlier
coverage explanation: its code and inline counter use 10,000 intervals, while
one sentence said 2,000. That sentence was corrected as numerical coherence
needed by the packet's bootstrap-validation comparison. No dataset, citation,
widget, print twin, empirical example, or exercise changed. Separately
registered Chapter 9 work on coding uncertainty, code reading, print presets,
reach-back exercises, and assessment closure was not started.

## Clean-session numerical reproduction

R 4.6.0 was resolved through the checkout launcher. A fresh R process extracted
all Chapter 9 R chunks with `knitr::purl`, ran them without cache, and asserted
every affected sample, interval, repeated-coverage, descriptive-range, and
bootstrap result together with the relevant source-language boundaries.

| Quantity | Reproduced value |
|---|---:|
| Teaching-population size | 50,000 |
| Mean-analysis sample size | 200 |
| Sample mean | 4.815 |
| Sample SD | 2.093487149 |
| Approximate z interval for the mean | [4.524857484, 5.105142516] |
| Coverage across 10,000 mean intervals | 94.94 % |
| Misses across 10,000 mean intervals | 506 |
| Conditional normal-rule descriptive range | [0.711765188, 8.918234812] |
| Width of that descriptive range | 8.206469623 |
| Bootstrap-median sample size | 60 |
| Sample median | 173.5 |
| Percentile bootstrap-median range | [155, 194] |
| Teaching-population median | 165 |
| Unique medians among 4,000 bootstrap replicates | 74 |
| Skewness of bootstrap-median replicates | 0.262233724 |
| This one bootstrap range contains the target | yes |

The clean run confirms that the normal-rule calculation is unchanged apart
from its bounded name and interpretation. It also confirms that the one
bootstrap interval contains the known target without treating that single hit
as a coverage validation.

## Independent statistical-methods reading

An independent read-only `critic_methods` reader first checked the complete
Chapter 9 source at blob `e05ef9e8c1268033a93d61c72fd9fc8fb1a30644`.
It passed all three registered corrections and gave 4/4 for correctness,
assumptions, and interpretation, but found the pre-existing 10,000-versus-2,000
count mismatch and therefore withheld the numerical-coherence gate.

After that sentence was corrected, the same critic freshly reread the complete
source at blob `67380c04d31d3370b1ff63e2533d70a12338ba0d`.
The hash matched before and after the reading, no file was modified, and no
fatal, major, or minor concern remained. The final scores were 4/4 for
correctness, assumptions, interpretation, and precision. The critic passed
all three registered items, numerical/code coherence, and the P1A-C09 packet
gate.

## Style, render, and exit evidence

- Checkout-local deterministic `book-style` lint passed with zero candidates.
- The final source received a complete top-to-bottom Croatian prose pass
  against H1--H10. It adds no governed colon, mid-sentence em dash, mechanical
  transition, unsupported empirical claim, invented citation or number, bold
  misuse, unexplained notation, or reader code burden.
- Structure lint passed with nine top-level sections, 2,586 prose words, body
  evenness 0.26, and zero candidates. The structure scan retained the vignette,
  one definition, three conceptual figures with four source variants, one
  divljina callout, both AI callouts, and all four exercise tiers.
- Figure-introduction checking passed for all three conceptual figures. The
  all-widget contract also passed for all 17 registered HTML/static pairs.
- The targeted Chapter 9 HTML render passed from the exact final source state
  in an isolated output directory. Twelve required rendered claims and values
  were present, and five superseded or contradictory phrases were absent.
  Generated AI-export changes were inspected and restored to their pre-packet
  state.
- Source-diff and whitespace checks passed. The chapter retains ten executable
  R/OJS blocks. Only `s9-vrijednosti` and `fig-dva-intervala` changed, to rename
  and consistently display the bounded normal-rule quantity; the other eight
  executable blocks, including the widget, print twin, and bootstrap figure,
  are unchanged.

## Forward-effects declaration

No incoming handoff applied and no new future-relevant effect was discovered.
Existing timing, fresh-panel, and `WC-C09` obligations already cover the later
effects of changing Chapter 9, so this correction creates no duplicate
outgoing handoff.
