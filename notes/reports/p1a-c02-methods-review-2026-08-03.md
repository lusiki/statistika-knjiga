---
packet: P1A-C02
date: "2026-08-03"
items:
  - R09-C02-randomisation
  - R09-C02-item-total
  - R09-C02-stevens
  - R14-C02-confounder
source_state: "chapter:sha1-ccae632a5d5adcb0e30d69ed3705b6e9f5a74a00"
status: passed
---

# P1A-C02 correction and methods evidence

## Bounded scope

This packet implements only the four registered Chapter 2 corrections. No
incoming handoff targets `P1A-C02`, and the ratified register plus the exact
packet instruction define the correction boundary. The corrected source:

- states that random assignment balances pre-treatment characteristics in
  expectation rather than guaranteeing equality in one realised allocation;
- distinguishes the effect of assignment or offer from the effect of receiving
  treatment when adherence is incomplete, and names spillover, differential
  attrition, and differential measurement as post-assignment threats;
- treats a negative item-rest association as a diagnostic, not proof of
  forgotten reverse coding, and names multidimensionality, translation,
  wording, and inattentive response as alternatives;
- presents Stevens's 1946 levels as a historically situated and practically
  useful description of recorded information rather than a complete timeless
  rule for permissible analysis; and
- defines a confounder as a common prior cause, distinguishes it from a
  mediator and collider, and rejects indiscriminate adjustment.

The widget, print twin, R/OJS code, generated data, exercises, references, and
all separately registered later Chapter 2 work remain unchanged. The later
units/eligibility, text-coding, survey, assessment, spine, and full `WA-C02`
vertical-slice work were not started.

## Clean-session numerical reproduction

R 4.6.0 was resolved through the checkout launcher. A fresh R process extracted
the final Chapter 2 R chunks with `knitr::purl`, executed them without cache,
and asserted every displayed value affected by the measurement correction. It
also reproduced the static confounder twin at zero shift and at its initial
shift of four.

| Quantity | Reproduced value |
|---|---:|
| Item-rest associations before recoding, items 1–4 | 0.749900; 0.595437; 0.760856; -0.951625 |
| Item-rest associations after recoding, items 1–4 | 0.951625; 0.847337; 0.832965; 0.951625 |
| Naive score range | 1.750000 |
| Corrected score range | 3.500000 |
| Aggregate widget slope at zero shift | -0.555279 |
| Within-group widget slopes at zero shift | -0.574985; -0.574985 |
| Aggregate widget slope at shift four | 0.274939 |
| Within-group widget slopes at shift four | -0.574985; -0.574985 |

The zero-shift aggregate and within-group fits carry the same negative
conclusion but are not numerically identical because the deterministic
within-group deviations are mildly related to exposure. The final prose says
exactly that. At the initial shift of four, the aggregate slope reverses while
both within-group slopes remain negative. The OJS and R constructions use the
same rows and formula, and the independent reader confirmed their exact parity
for these values.

## Independent statistical-methods reading

An independent read-only `critic_methods` review checked exact source blob
`ccae632a5d5adcb0e30d69ed3705b6e9f5a74a00` before and after its final reading.
The hash matched both times. The critic scored correctness, assumptions,
interpretation, and precision 5/5, with no fatal, major, or minor finding.

All four registered items passed. The critic confirmed the expectation versus
realised-balance distinction, the assignment-versus-receipt estimand boundary,
and the adherence, spillover, attrition, and measurement qualifications. It
also confirmed that the item-rest result remains a diagnostic with all required
alternatives, that Stevens's scheme has both a practical role and a stated
limit, and that common cause, mediator, and collider are distinguished without
recommending control of every available variable.

The critic's first pass identified one minor precision issue in the existing
zero-shift widget guidance. The aggregate and within-group slopes share a
negative direction but are not identical. The sentence was corrected, the
clean-session reproduction was rerun, and the critic issued the final pass on
the new exact source state with no remaining finding.

## Style, render, and exit evidence

- Checkout-local deterministic `book-style` lint passed with zero candidates.
- The final source received a complete top-to-bottom Croatian prose pass
  against H1–H10. The correction adds no governed colon, mid-sentence em dash,
  mechanical transition, unsupported citation or empirical claim, bold misuse,
  unexplained notation, visible Part I code, or assessed code-production task.
- Structure lint passed with 10 top-level sections, 4,281 prose words, body
  evenness 0.23, and zero candidates. The structure scan retained the vignette,
  four definitions, one conceptual figure with HTML/static variants, one
  divljina callout, both AI callouts, and all four exercise tiers.
- Figure-introduction check passed for the logical widget/static-twin pair. The
  all-widget contract also passed for all 17 registered pairs.
- `quarto render chapters/02-mjerenje-i-dizajn.qmd --to html` passed from the
  exact source state in an isolated output directory. Eighteen required
  rendered-claim assertions were present and five removed overclaims were
  absent. Generated AI-export changes were inspected and restored to their
  pre-packet state.
- Source-diff and whitespace checks passed. All eight R/OJS source blocks are
  byte-for-byte unchanged from `HEAD`, with combined SHA-256
  `cf0950a5e14f0f7057ffccca7cbaa25ca64eab9c113a030f2717a181aaf8541d`.
  No TODO or placeholder token remains in the chapter.

## Forward-effects declaration

No new future-relevant effect was discovered. The later Chapter 2 work already
has stable register items, packet dependencies, and `OA-C02-ACCEPTANCE`; none
is a blocker for this correction. No outgoing handoff is created because
duplicating those obligations would add no information.
