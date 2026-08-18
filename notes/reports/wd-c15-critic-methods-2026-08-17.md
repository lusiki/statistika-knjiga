# WD-C15 — final methods review

Date: 2026-08-17

File: `chapters/15-vise-grupa.qmd`

SHA-256 before and after review: `fd8337520901df9bbce56e25880f12b889fd54d46e4c1bb3e8f17da3ca49d813`

Git blob before and after review: `aa644049bacb62e7fc05ab75d3b6157b83165b96`

Mode: independent, read-only, complete 827-line reread

## Scores

| Correctness | Assumptions | Interpretation | Precision |
|---:|---:|---:|---:|
| 5/5 | 5/5 | 5/5 | 4/5 |

## Findings

- Fatal: none.
- Major: none.
- Minor: none.
- Useful improvement: lines 483–489 and 511–521 could say explicitly that
  between-group deviations are weighted by group size when group sizes differ.
  The code, formulas and all reported values are already correct.

The chapter now separates the dependent pairwise, independent-test and
omnibus simulations; puts magnitude before the test; and explicitly limits
eta- and omega-squared to point descriptions whose uncertainty is not shown.
The classical common-variance and Welch branches retain the same group means
and contrasts but not the same uncertainty. Tukey intervals are confined to
the classical branch, and Welch is not used to validate them.

## Required decisions

- `R09-C15-variance-ratio`: PASS. The ratio is an orienting indicator, never
  an inferential licence.
- `R23-C15-suspect-code`: PASS. `p.adjust.method = "none"` is the only error
  that changes the claim, and replacement code is not requested.
- `R35-REACHBACK-15`: PASS. The task genuinely retrieves design and
  smallest-important-effect reasoning and has canonical closure.
- D02: PASS. Point estimates are shared; classical and Welch uncertainty are
  not equated.
- Dependence stop: PASS. Repeated, nested and linked rows stop ordinary
  independent-row inference.

All supplied numerical controls reproduce, including `F(4,295) = 8.3818`,
eta-squared `0.1021`, omega-squared `0.0896`, four of ten Tukey contrasts,
variance ratio `1.4327`, Welch `F = 7.3208`, Kruskal–Wallis `29.8204`, the
three simulation rates and the aggregate difference `1.2973`.

## Verdict

PASS — zero fatal, major or minor findings; one nonblocking precision note.
