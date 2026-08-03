---
packet: P1A-C10
date: "2026-08-03"
decision: G-A1a
source_state: "chapter:sha1-a90549950c4f410f757bdec9b6ac680380ab7662"
status: passed
---

# P1A-C10 correction and methods evidence

## Bounded scope

This packet implements only accepted D01 for
`chapters/10-logika-testiranja.qmd`. `H-G-A1A-001` was acknowledged and
consumed before the packet was claimed. The corrected source:

- states the full-distribution/no-association null, exchangeability,
  independent-unit assumption, observational boundary, and absence of a
  causal claim;
- retains the two-sided unstudentized difference in means and absolute-tail
  comparison;
- uses `(b + 1) / (B + 1)`, including ties, for every finite random-permutation
  p-value and distinguishes that estimate from exact enumeration;
- replaces the old near-equal-means calibration with independent balanced
  random labels, making the full-distribution null true by construction;
- repairs the AI-error example and key so their sole planted error is the
  reversal of `p(data | H0)` into `p(H0 | data)`;
- leaves the analytic normal-p-value widget and print twin algorithmically
  unchanged and explains why the Monte Carlo correction does not apply there;
- balances the bounded Bayesian comparison while keeping the chapter
  estimation-first.

The normalized widget/print-twin block has the same SHA-256 before and after
the packet:
`b924857114b7545d147e725cd6a52d55aac0d17336d6abb6ad5bef456e5a4cd3`.

## Clean-session numerical reproduction

The chapter was purled and sourced in a fresh R process through the checkout
launcher. Assertions verified the corrected formula for the main and
known-null examples, all repeated finite-permutation p-values on the
`1 / 301` grid, and the discrete absolute 95th-percentile cutoff. The reproduced
values were:

| Quantity | Reproduced value |
|---|---:|
| Main raw difference | 0.640938989801 |
| Main interval | [0.174811193069, 1.107066786534] |
| Main extreme count / random permutations | 64 / 4000 |
| Main corrected p-value | 0.016245938515 |
| Known-null raw difference | -0.093333333333 |
| Known-null interval | [-0.543709589126, 0.357042922460] |
| Known-null extreme count / random permutations | 2784 / 4000 |
| Known-null corrected p-value | 0.696075981005 |
| Known-null rejection rate | 4.875% (39 / 800) |
| Alternative rejection / miss rate | 79.5% / 20.5% |
| Absolute 95th-percentile cutoff | 0.499607748476 |
| True source difference | 0.743644165673 |

The cutoff contains 95.3% of the discrete null draws because of ties, which is
consistent with its stated 95% summary. The rendered main p-value is 0.016 and
the known-null rejection rate is 4.9% after display rounding.

## Independent statistical-methods reading

An independent read-only `critic_methods` review examined the exact source
blob `a90549950c4f410f757bdec9b6ac680380ab7662`. Its final scores were 5/5 for
correctness, assumptions, interpretation, and precision. All eight D01 gates
passed, with no fatal, major, or minor finding remaining.

The first reading had identified two issues outside the original correction
mechanics but inside the corrected claims: overbroad Type-I/Type-II prose and
an asymmetric upper-quantile cutoff described as absolute. The final source
repairs both by describing the figure as geometry rather than a rate estimate,
qualifying the fixed-threshold trade-off and design dependence, and using the
95th percentile of the absolute null statistics. The independent reread
confirmed those dispositions and found no regression in the eight D01 gates.

## Style, render, and exit evidence

- Checkout-local deterministic `book-style` lint: passed, zero candidates.
- Manual Croatian prose pass against `STYLE.md`: passed; the chapter was read
  top to bottom after the final edits, and no unsupported empirical claim,
  number, citation, heading, callout, or unrelated prose change was found.
- Structure lint: passed; 11 top-level sections, 2,528 prose words, body
  evenness 0.36, zero candidates.
- Figure-introduction check: passed; all three conceptual figures have a prose
  paragraph immediately before them.
- Targeted `quarto render chapters/10-logika-testiranja.qmd --to html`: passed
  from the final source state. Generated `docs/` and AI-export changes were
  inspected and then excluded from the source packet.
- Source diff and whitespace check: passed; the source blob is
  `a90549950c4f410f757bdec9b6ac680380ab7662` and only the accepted D01 surface
  is changed.
- Comprehensive-review workflow validator: passed with no active packet and
  `P1A-C11` as `next_permitted_packet`; the `generic_packet_evidence` and
  `invalid_outside_ask_link` negative fixtures both failed as required.

## Forward-effects declaration

No new future-relevant effect was discovered. The already-ratified
`R01-C11-inherited-permutation` item and the dependency of `P1A-C11` on
`P1A-C10` fully represent the required Chapter 11 follow-through, so this
packet creates no duplicate outgoing handoff.
