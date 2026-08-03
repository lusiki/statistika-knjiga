---
packet: P1A-C07
date: "2026-08-03"
items:
  - R09-C07-clt-conditions
source_state: "chapter:sha1-8deb7a2b686754bdb3bc6d0ddfca2c7ade472f76"
status: passed
---

# P1A-C07 correction and methods evidence

## Bounded scope

This packet implements only `R09-C07-clt-conditions`. No incoming handoff
targets `P1A-C07`, and no outside ask is required. The corrected source states
the introductory central-limit-theorem conditions as observations from one
stable distribution, independence in the elementary form, finite variance,
and appropriately weak rather than arbitrary dependence in broader variants.
It also separates the behavior seen in the chapter's independent Bernoulli
simulation from a guarantee for arbitrary data, sample sizes, dependence
structures, or infinite-variance populations.

No dataset, citation, R/OJS calculation, widget, print twin, definition,
exercise, or separately registered later Chapter 7 repair changed. The later
degree-of-belief, cognitive-load and retrieval, reach-back, spine, assessment,
and full `WC-C07` vertical-slice work was not started.

## Clean-session numerical reproduction

R 4.6.0 was resolved through the checkout launcher. A fresh R process extracted
all Chapter 7 R chunks with `knitr::purl`, ran them without cache, and asserted
every displayed source relationship,
the simulation seeds, the probability identities, monotone area counts, the
hot-hand selection result, the analytic/simulated binomial comparison, and the
print-twin row count.

| Quantity | Reproduced value |
|---|---:|
| Coin-toss rows | 6,000 |
| Cumulative share after 20 tosses, minimum to maximum | 0.250000 to 0.650000 |
| Cumulative share after 2,000 tosses, minimum to maximum | 0.498000 to 0.502000 |
| Social-media share | 26.756000 % |
| Young-person share | 24.720000 % |
| Independence product | 6.614083 % |
| Observed young-and-social-media share | 11.336000 % |
| Portal share | 30.202000 % |
| Portal-or-young share | 47.046000 % |
| Portal-and-young overlap | 7.876000 % |
| Uncorrected portal-plus-young sum | 54.922000 % |
| Social-media share among young people | 45.857605 % |
| Social-media share among older people | 20.483528 % |
| Television share overall | 21.654000 % |
| Television share at age 60 or older | 41.246027 % |
| Media minutes within 1, 2, and 3 SD | 70.104000 %; 95.912000 %; 99.138000 % |
| Payment amount within 1 and 3 SD | 87.654000 %; 97.630000 % |
| Log payment among payers within 1, 2, and 3 SD | 67.978234 %; 94.809544 %; 99.665132 % |
| Non-payers | 76.110000 % |
| Success after three successes, length 20 | 0.355921 |
| Success after three successes, length 100 | 0.458691 |
| Success after one success, length 100 | 0.495742 |
| Analytic probability of at least 14 openings | 19.416523 % |
| Simulated probability of at least 14 openings | 19.310000 % |
| Probability of no viral posts | 66.760797 % |
| Print-twin simulation rows | 4,000 |

The reproduction changes no numerical result because the packet corrects only
the conditions and interpretation of the existing simulation. All 12 R/OJS
source blocks remain byte-for-byte unchanged from `HEAD`.

## Independent statistical-methods reading

An independent read-only `critic_methods` reader checked the complete Chapter 7
source at blob `8deb7a2b686754bdb3bc6d0ddfca2c7ade472f76`. The hash was identical
before and after the reading. The critic scored correctness, assumptions,
interpretation, and precision 5/5 and returned no fatal, major, or minor
finding.

The review specifically confirmed that the elementary statement names a stable
common distribution, independence, and finite variance; that broader variants
permit appropriately weak but not arbitrary dependence; and that the widget is
bounded to independent Bernoulli trials with fixed probability and finite
variance. It also confirmed that no contradiction elsewhere in the full
chapter weakens those limits. No wording change was requested.

## Style, render, and exit evidence

- Checkout-local deterministic `book-style` lint passed with zero candidates.
- The final source received a complete top-to-bottom Croatian prose pass
  against H1--H10. The correction adds no governed colon, mid-sentence em dash,
  mechanical transition, unsupported empirical claim, bold misuse,
  unexplained notation, or code-production burden. Simulation still precedes
  the theorem's name and its conditions.
- Structure lint passed with 11 top-level sections, 2,642 prose words, body
  evenness 0.29, and zero candidates. The structure scan retained the vignette,
  five definitions, four conceptual figures with five source variants, one
  divljina callout, both AI callouts, and all four exercise tiers.
- Figure-introduction checking passed for all four conceptual figures. The
  all-widget contract also passed for all 17 registered HTML/static pairs.
- `quarto render chapters/07-vjerojatnost.qmd --to html --no-cache` passed from
  the exact source state in an isolated output directory. Five required
  rendered claims were present and three removed overbroad claims were absent.
  Generated AI-export changes were inspected and restored to their pre-packet
  state.
- Source-diff and whitespace checks passed. The chapter diff has one prose
  hunk, all 12 R/OJS blocks are unchanged, and no TODO or placeholder was added.

## Forward-effects declaration

No incoming handoff applied and no new future-relevant effect was discovered.
Later Chapter 7 work retains stable register items, packet dependencies, and
`OA-C07-ACCEPTANCE`. The correction therefore creates no duplicate outgoing
handoff.
