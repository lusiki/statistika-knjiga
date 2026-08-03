---
packet: P1A-C11
date: "2026-08-03"
source_state: "chapter:sha1-2aaede845c2a93fcad5d473d6466f938285cd7b6"
status: passed
---

# P1A-C11 correction and methods evidence

## Bounded scope

This packet revalidates only the Chapter 11 follow-through from the accepted
Chapter 10 permutation correction. It closes
`R01-C11-inherited-permutation` and its packet-linked assumption criterion
`R09-C11-power-assumptions` without taking any work assigned to `WC-C11`.
The corrected source:

- uses `(b + 1) / (B + 1)`, including ties, for its only finite random-
  permutation p-value;
- states the empirical curve's full-distribution null, exchangeability
  condition, two-sided raw difference-in-means statistic, independent-unit
  boundary, finite-population alternative, without-replacement sampling, and
  two Monte Carlo layers;
- bounds that curve to its declared data-generating mechanism and procedure;
- distinguishes the widget and print twin as an idealized two-sided known-
  variance z procedure for independent equal-size normal groups;
- states the worked example's zero-difference null, known-standard-error z
  statistic, independence, normality, common known standard deviation,
  two-sided cutoff, target effect, and repetition count; and
- leaves the chapter's estimation-first and precision-planning role intact.

The known `WC-C11` work on winner's-curse wording, blanket distrust, fixed
section order, print presets, and retrieval remains unchanged.

## Clean-session numerical reproduction

The chapter was purled and sourced in a fresh R process through the checkout
launcher. Assertions verified that every retained finite-permutation p-value
lies on the corrected `1 / 201` grid, no value can be zero, every stored result
is finite, and the empirical curve and worked planning simulation reproduce.

| Quantity | Reproduced value |
|---|---:|
| Empirical curve power at total n = 60 | 22.666666666667% |
| Empirical curve power at total n = 100 | 35.666666666667% |
| Empirical curve power at total n = 200 | 56.666666666667% |
| Empirical curve power at total n = 300 | 79.666666666667% |
| Empirical curve power at total n = 500 | 93.666666666667% |
| Empirical curve power at total n = 800 | 99.666666666667% |
| True raw difference | 0.743644165673 |
| Pooled standard deviation | 1.912184863285 |
| Standardized difference | 0.388897632207 |
| Probability-of-superiority expression | 60.682% |
| Interval width at n = 100 per group | 1.060061204829 |
| Interval width at n = 300 per group | 0.612026621966 |
| Interval width at n = 800 per group | 0.374788233204 |
| Mean estimate across small studies | 0.737223285279 |
| Mean selected small-study estimate | 1.497906720700 |
| Small-study exaggeration factor | 2.014278857879 |
| Small-study wrong-sign share | 0.147492625369% |
| Large-study exaggeration factor | 1.026707820037 |
| Corrected minimum stored p-value | 0.004975124378 |
| Selected small studies | 678 / 3000 |
| Selected large studies | 961 / 1000 |
| Worked plan power at n = 100 per group | 46.2% |
| Worked plan power at n = 150 per group | 63.5% |
| Worked plan power at n = 200 per group | 75.05% |
| Worked plan power at n = 250 per group | 83.25% |

The corrected p-value grid leaves the strict `< 0.05` selection boundary
unchanged for 200 random permutations, but it removes impossible zero
p-values and makes the finite-simulation calculation valid. The rendered
values are 22.7%, 79.7%, and 99.7% for the three power values cited in prose,
and 46.2%, 63.5%, 75.0%, and 83.2% in the planning table.

## Independent statistical-methods reading

An independent read-only `critic_methods` review verified exact source blob
`2aaede845c2a93fcad5d473d6466f938285cd7b6`. Its scores were 5/5 for
correctness, assumptions, interpretation, and precision, with zero fatal,
major, or minor findings.

All four bounded gates passed. The critic confirmed the finite-permutation
correction, the full empirical-curve assumption set and scope boundary, the
separate z-model assumptions for the widget/twin and worked example, and the
preserved estimation-first role. The already registered `WC-C11` issues were
unchanged and were not counted as failures of this packet.

## Style, render, and exit evidence

- Checkout-local deterministic `book-style` lint passed with zero candidates.
- The final source received a top-to-bottom manual Croatian prose pass against
  H1-H10. The corrected surface adds no colon, mid-sentence em dash,
  mechanical transition, unsupported citation or number, bold misuse,
  unexplained symbol, visible-code expansion, or unrelated prose change.
- Structure lint passed with 10 top-level sections, 2,273 prose words, body
  evenness 0.16, and zero candidates.
- Figure-introduction check passed for both conceptual figures and all three
  source variants.
- `quarto render chapters/11-velicina-ucinka-i-snaga.qmd --to html` passed from
  the final source state. The rendered assumptions and reproduced table values
  were inspected; generated AI-export changes were then excluded from the
  source packet.
- Source-diff and whitespace checks passed. The chapter source blob is
  `2aaede845c2a93fcad5d473d6466f938285cd7b6`, Chapter 10 is unchanged, and
  only the accepted P1A-C11 surface changed.
- The comprehensive-review workflow validator and its two negative fixtures
  passed at closeout with no active packet and `G-A1b` as the next permitted
  packet.

## Forward-effects declaration

No new future-relevant effect was discovered. The remaining Chapter 11 work is
already represented by stable `WC-C11` items and dependencies, so duplicating
it as a new handoff would add no information.
