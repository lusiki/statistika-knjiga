---
packet: P1A-C15
date: "2026-08-03"
decision: G-A1b
source_state: "chapter:sha1-0eadfd02627a95aed614a005f93f81878249ea10"
status: passed
---

# P1A-C15 dependent revalidation and methods evidence

## Bounded scope

This packet implements only `R02-C15-dependent-revalidation` under accepted
D02. No incoming handoff targets `P1A-C15`; the dependency and correction
boundary are already recorded in the register and in the accepted `P1A-C14`
evidence. The corrected Chapter 15 source:

- preserves the common group-mean model and its exact point estimates as the
  bridge from Chapters 14 to 16;
- identifies its displayed mean-square F ratio and `aov` receipt as the
  classical homoskedastic analysis with one residual variance;
- distinguishes that inference from Welch's use of group-specific variances
  and adjusted degrees of freedom; and
- leaves formulas, code, numerical results, callouts, summary, exercises,
  widget, print twin, and all unrelated prose unchanged.

`R09-C15-variance-ratio` remains `ratified` and unmodified. The separately
registered suspect-code, narrative-payoff, dependence, reachback, and later
Wave D repairs were not started. Chapters 14 and 16 retain their pre-packet
source blobs, respectively
`449c88f25e032fd8d4a9066deb45c8648497e8e5` and
`c6443b7c111c1a6e4fb8357e772b18a7ae6f8850`.

## Clean-session numerical reproduction

R 4.6.0 was resolved through the checkout launcher, and the complete Chapter
15 seeded computation was regenerated in a fresh process from the final source
state. Assertions checked that `aov` and `lm` have identical coefficients,
that their fitted group means equal the five observed sample means to less than
`1e-12`, that classical `aov` and ordinary homoskedastic `lm` have the same F
statistic, and that this statistic is not Welch's F statistic.

| Quantity | Reproduced value |
|---|---:|
| Sample size; groups | 300; 5 |
| Group means: portal; social media; TV; radio; print | 4.818182; 3.842857; 5.428571; 5.361111; 5.468750 |
| Classical F; numerator df; denominator df | 8.381812957409; 4; 295 |
| Classical p-value | 0.000002041821360 |
| Mean square between; mean square within | 28.461272095959; 3.395598570450 |
| Sum of squares between; sum of squares within | 113.845088383838; 1001.701578282830 |
| Eta squared; omega squared | 0.102053183238; 0.089604885986 |
| Welch F; numerator df; denominator df | 7.320807631166; 4; 112.425284937609 |
| Welch p-value | 0.000028167962781 |
| Kruskal-Wallis statistic; p-value | 29.820424479989; 0.000005324184212 |
| Maximum/minimum sample-variance ratio | 1.432656498313 |
| Familywise rate for ten uncorrected pairs; omnibus rate | 27.4%; 4.25% |
| Ten independent comparisons: simulated; formula | 40.4%; 40.126306076162% |
| Tukey TV minus social media: difference; adjusted p | 1.585714285714; 0.000012029522 |
| Tukey print minus TV: difference; adjusted p | 0.040178571429; 0.999976893871 |
| Tukey print minus TV interval | [-1.057748641685, 1.138105784542] |
| Significant Tukey pairs | 4 of 10 |

The reproduced classical and Welch results therefore support the new prose
distinction rather than an inferential identity. Reproducing the existing
variance-ratio value was an integrity check only; this packet did not alter or
approve its separately registered interpretation.

## Independent statistical-methods reading

An independent read-only `critic_methods` review examined exact source blob
`0eadfd02627a95aed614a005f93f81878249ea10`; the hash matched before and after
the review. It scored correctness, assumptions, interpretation, and precision
5/5, with no fatal, major, or minor finding and no requested source change.

The critic passed every bounded surface: prose distinguishes shared model form
and point estimates from uncertainty; the formula and widget remain about the
classical mean-square ratio; classical `aov` and Tukey HSD remain separate from
Welch's `oneway.test`; the reproduced F statistics and degrees of freedom are
distinct; and the callouts, summary, and exercises do not inherit the false
equivalence.

## Style, render, and exit evidence

- Checkout-local deterministic `book-style` lint passed with zero candidates.
- The final source received a top-to-bottom manual Croatian prose pass against
  H1-H10. The correction adds no colon, mid-sentence em dash, mechanical
  transition, unsupported citation or empirical claim, bold misuse,
  unexplained notation, or unrelated prose change.
- Structure scan retained the full skeleton: vignette, three definitions, one
  conceptual figure with one HTML/static twin pair, one divljina callout, two
  AI callouts, and all four exercise tiers. Structure lint passed with 11
  top-level sections, 2,145 prose words, body evenness 0.23, and zero
  candidates.
- Figure-introduction check passed for the one conceptual figure and both
  source variants.
- The targeted Chapter 15 HTML render passed from the final source state in an
  isolated output directory. Rendered assertions found the classical F of
  8.38 with 4 and 295 degrees of freedom, Welch F of 7.32 with denominator df
  112.4, and both prose statements separating the shared mean-model form from
  the two uncertainty procedures. Pre-render AI build artifacts were inspected
  and restored to their pre-packet state.
- The all-widget contract check passed for all 17 registered widget/static-
  twin pairs. Chapter 15's widget and print twin remained unchanged.
- Source-diff and whitespace checks passed. The diff contains only the bounded
  explanatory prose in Chapter 15; no formula, code, result, callout, summary,
  exercise, or excluded repair changed, and Chapters 14 and 16 are unchanged.
- The comprehensive-review workflow validator and its two negative fixtures
  passed at closeout with no active packet and `P1A-C16` as the next permitted
  packet.

## Forward-effects declaration

No new future-relevant effect was discovered. The required Chapter 16
follow-through is already represented by `R02-C16-dependent-revalidation` and
the dependency of `P1A-C16` on this packet. The other known Chapter 15 repairs
retain their stable registered items, so a duplicate outgoing handoff would
add no information.
