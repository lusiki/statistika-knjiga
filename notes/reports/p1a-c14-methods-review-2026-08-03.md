---
packet: P1A-C14
date: "2026-08-03"
decision: G-A1b
source_state: "chapter:sha1-449c88f25e032fd8d4a9066deb45c8648497e8e5"
status: passed
---

# P1A-C14 correction and methods evidence

## Bounded scope

This packet implements only accepted D02 for
`chapters/14-dvije-grupe.qmd`. `H-G-A1B-001` was acknowledged and consumed
before the packet was claimed. The corrected source:

- retains Welch inference as the default for the two-sided population mean
  difference, TV minus social media;
- states that the binary-predictor OLS coefficient equals the raw difference
  in sample means exactly while separating that point-estimate identity from
  the uncertainty procedure;
- sources the chapter's default interval from Welch and labels ordinary
  homoskedastic OLS as a comparison;
- distinguishes Welch's group-specific standard error and
  Welch-Satterthwaite degrees of freedom from pooled ordinary OLS uncertainty
  and residual degrees of freedom;
- exposes the standard-error, degrees-of-freedom, and unrounded interval
  differences hidden by the coincident two-decimal display;
- states the independent-unit, independent-group, coding, target-population,
  small- and large-sample, homoskedastic-OLS, observational, and noncausal
  boundaries; and
- leaves the widget, print twin, paired comparison, Wilcoxon discussion,
  standardized effect, confounding example, Chapters 15 and 16, and all
  unrelated material unchanged.

The normalized Chapter 14 interaction and widget/print-twin block has the same
SHA-256 before and after the packet:
`dfc10a56739a76389209fdc345eb871a31879bc13c92bf31e896caa6d8dcf766`.

## Clean-session numerical reproduction

Rscript 4.6.0 was resolved through the checkout launcher and the Chapter 14
sample was regenerated in a fresh R process. Assertions checked the accepted
values, the exact equality of the raw difference and binary-predictor
coefficient, and the equality of pooled Student and ordinary homoskedastic OLS
test statistics and degrees of freedom.

| Quantity | Reproduced value |
|---|---:|
| Social-media group size | 70 |
| TV group size | 50 |
| Social-media variance | 3.818633540373 |
| TV variance | 4.214285714286 |
| Welch estimate, TV minus social media | 1.185714285714 |
| OLS coefficient | 1.185714285714 |
| Welch standard error | 0.372609208160 |
| Welch degrees of freedom | 102.471131550669 |
| Welch t statistic | 3.182192655868 |
| Welch p-value | 0.001935138042 |
| Welch 95% interval | [0.446686471421, 1.924742100008] |
| Ordinary OLS standard error | 0.369536997510 |
| Ordinary OLS residual degrees of freedom | 118 |
| Ordinary OLS t statistic | 3.208648372706 |
| Ordinary OLS p-value | 0.001717470691 |
| Ordinary OLS 95% interval | [0.453930424466, 1.917498146963] |

Both intervals render as 0.45 to 1.92 at two decimals. The chapter therefore
shows the standard errors and degrees of freedom to three decimals and the two
intervals to three decimals where the inferential distinction is explained.

## Independent statistical-methods reading

An independent read-only `critic_methods` review examined exact source blob
`449c88f25e032fd8d4a9066deb45c8648497e8e5`. It scored correctness,
assumptions, interpretation, and precision 5/5, with no fatal, major, or minor
finding and no requested source change.

All seven D02 gates passed. The critic confirmed the Welch default and exact
two-sided mean-difference null, the point-estimate identity, the distinct
uncertainty and degrees of freedom, the Welch-sourced default interval, the
labelled ordinary OLS contrast, all reproduced values, the assumptions and
noncausal boundary, and preservation of the packet's scope exclusions.

## Style, render, and exit evidence

- Checkout-local deterministic `book-style` lint passed with zero candidates.
- The final source received a top-to-bottom manual Croatian prose pass against
  H1-H10. The corrected surface adds no colon, mid-sentence em dash,
  mechanical transition, unsupported citation or empirical claim, bold
  misuse, unexplained notation, or unrelated prose change. The visible
  worked-example receipt remains below the twelve-line ceiling and carries
  only the comparison needed for D02.
- Structure lint passed with 11 top-level sections, 2,420 prose words, body
  evenness 0.22, and zero candidates.
- Figure-introduction check passed for the one conceptual figure and both
  source variants.
- `quarto render chapters/14-dvije-grupe.qmd --to html` passed from the final
  source state. Seven required rendered D02 claims were found, including the
  null direction, both standard errors and degrees of freedom, both unrounded
  intervals, and the point-estimate/inference distinction. Generated `docs/`
  and AI-export changes were inspected and excluded from the source packet.
- The all-widget contract check passed for all 17 registered widget/static-
  twin pairs. Chapter 14's normalized interaction block remained unchanged.
- Source-diff and whitespace checks passed. Chapters 15 and 16 are unchanged,
  and only the accepted D02 surface is changed in Chapter 14.
- The comprehensive-review workflow validator and its two negative fixtures
  passed at closeout with no active packet and `P1A-C15` as the next permitted
  packet.

## Forward-effects declaration

No new future-relevant effect was discovered. The required Chapter 15 and 16
follow-through is already represented by `R02-C15-dependent-revalidation`,
`R02-C16-dependent-revalidation`, and the dependencies of `P1A-C15` and
`P1A-C16` on this packet, so a duplicate outgoing handoff would add no
information.
