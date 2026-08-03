---
packet: P1A-C06
date: "2026-08-03"
items:
  - R09-C06-pearson-spearman-agree
  - R09-C06-pearson-spearman-disagree
  - R09-C06-range-restriction
  - R09-C06-scatterplot-primary
source_state: "chapter:sha1-c3177eb7cc5abe87cca6e1781262925b50e0f6b2"
status: passed
---

# P1A-C06 correction and methods evidence

## Bounded scope

This packet implements only the four registered Chapter 6 corrections. No
incoming handoff targets `P1A-C06`, and no outside ask is required. The
corrected source:

- makes the scatterplot the primary inspection and both coefficients secondary
  summaries;
- treats Pearson--Spearman agreement only as a clue compatible with an
  approximately linear monotonic relation, not proof of linearity, robustness,
  or the absence of influential observations;
- treats disagreement as a reason to inspect curvature, unusual observations,
  tied ranks, subgroups, and selection, not as an automatic diagnosis or an
  automatic reason to choose Spearman's coefficient; and
- states the conditions under which range restriction can attenuate an
  association while allowing weakening, strengthening, or sign reversal under
  other forms and selection rules.

The narrow-age example now distinguishes a changed target population from an
attenuated version of one unchanged relation. No dataset, citation, R/OJS
calculation, widget, print twin, or separately registered later Chapter 6
repair was changed. The later coded-association, reachback, assessment, spine,
and full `WA-C06` vertical-slice work was not started.

## Clean-session numerical reproduction

R 4.6.0 was resolved through the checkout launcher. A fresh R process extracted
all final Chapter 6 R chunks with `knitr::purl`, executed them without cache,
and asserted the displayed results and their source relationships.

| Quantity | Reproduced value |
|---|---:|
| Complete observations | 300 |
| Covariance, age and minutes | -293.113099219621 |
| Covariance after converting minutes to hours | -4.885218320327 |
| Pearson correlation | -0.559289315826 |
| Spearman correlation | -0.680150964766 |
| Pearson correlation from standardized values | -0.559289315826 |
| Same-sign share | 0.266666666667 |
| Pearson correlation with log minutes | -0.683618589271 |
| Youngest-group observations | 90 |
| Youngest-group Pearson correlation | 0.180376722321 |
| Simpson aggregate correlation | 0.757951774050 |
| Simpson within-group correlations | -0.767874022098; -0.657974159297; -0.706051400051 |

The youngest subset contains seven recorded ages from 18 through 24. In the
generator, exact age and minutes are independent within that group, so its
population correlation is zero; the observed positive coefficient is sampling
variation for a different target rather than an attenuated full-sample
coefficient. The reproduction also asserted the covariance unit conversion,
Pearson-from-z identity, Spearman-as-midrank-Pearson identity, complete-pair
counts, visible summary values, and Simpson signs.

## Independent statistical-methods reading

An independent read-only `critic_methods` reader first checked source blob
`2d716ed775e56551d624de0ea9edd8535bc90b39`. That pass confirmed the four core
corrections but withheld approval for one major and three minor local precision
defects. The AI-error box contained a second unsupported no-outlier claim; the
text called seven recorded integer ages a seven-year range; the sampling
sentence referred merely to a nonzero coefficient rather than an excursion of
the observed magnitude; and one sentence described both coefficients as unable
to see any nonmonotonic relation.

Those four bounded defects were corrected. The critic then read the complete
802-line source at blob `c3177eb7cc5abe87cca6e1781262925b50e0f6b2`, verified
that the hash was unchanged before and after the reading, reproduced all
affected values, and scored correctness, assumptions, interpretation, and
precision 5/5. All four registered items passed with no remaining fatal, major,
or minor finding.

## Style, render, and exit evidence

- Checkout-local deterministic `book-style` lint passed with zero candidates.
- The final source received a complete top-to-bottom Croatian prose pass
  against H1--H10. The correction adds no governed colon, mid-sentence em dash,
  mechanical transition, unsupported empirical claim, bold misuse,
  unexplained notation, or new code-production burden.
- Structure lint passed with 11 top-level sections, 2,897 prose words, body
  evenness 0.24, and zero candidates. The structure scan retained the vignette,
  three definitions, three conceptual figures with four source variants, one
  divljina callout, both AI callouts, and all four exercise tiers.
- Figure-introduction check passed for all three conceptual figures. The
  all-widget contract also passed for all 17 registered HTML/static pairs.
- `quarto render chapters/06-povezanost.qmd --to html --no-cache` passed from
  the exact source state in an isolated output directory. Thirteen required
  rendered-claim assertions were present and eleven removed or rejected claims
  were absent. Generated AI-export changes were inspected and restored to their
  pre-packet state.
- Source-diff and whitespace checks passed. All 13 executable R/OJS bodies are
  unchanged from `HEAD`; one hidden R block differs only in two explanatory
  comments. Twelve of thirteen raw executable fences are byte-for-byte
  unchanged. No TODO or placeholder token remains in the chapter.

## Forward-effects declaration

No incoming handoff applied and no new future-relevant effect was discovered.
Later Chapter 6 work retains stable register items and dependencies. The
eventual generated concept-view reconciliation is already represented by
`R04-TERMS-concept-regeneration` in `P2-TERMS`, so a duplicate outgoing handoff
would add no information.
