---
packet: P1A-C16
date: "2026-08-03"
decision: G-A1b
items:
  - R02-C16-dependent-revalidation
  - R09-C16-estimand
  - R09-C16-uncertainty
  - R09-C16-leakage-time
source_state: "chapter:sha1-ba93f9a62965dc1a9ae1c67a3c54d536976773cb"
status: passed
---

# P1A-C16 correction and methods evidence

## Bounded scope

This packet implements only the four registered Chapter 16 corrections. No
incoming handoff targets `P1A-C16`; the accepted D02 correction and the
completed `P1A-C14` and `P1A-C15` packets define the dependent-revalidation
boundary. The corrected source:

- preserves the shared group-mean model and exact point-estimate identities
  while limiting the binary inferential identity to pooled Student and ordinary
  homoskedastic OLS, and the five-group identity to classical homoskedastic
  ANOVA and OLS;
- identifies Welch as a distinct uncertainty procedure with group-specific
  variances and adjusted degrees of freedom in both bridges;
- chooses finite-population least-squares coefficients for the recorded outcome
  among all 50,000 generated units as the main estimand;
- separates those descriptive coefficients from the latent pre-rounding and
  pre-truncation generator parameters;
- states that the chosen census estimand has no sampling uncertainty, removes
  ordinary `confint` intervals for that target, and carries the distinction
  through the tables, worked example, summary, and exercises;
- defines prediction time immediately before the trust response, excludes
  post-outcome willingness to pay as target leakage, and retains a disjoint
  held-out set for predictive evaluation; and
- leaves the widget and print twin, Chapters 14 and 15, and every separately
  registered later Chapter 16 repair unchanged.

The causal-limit paragraph changed only where it had judged the observed
coefficient against the latent generator rule. The separately registered
causal-adjustment contract, interaction, binary-outcome reading, published
table or paragraph, retrieval, reachback, dependence, and later Wave D work
were not started.

## Clean-session numerical reproduction

R 4.6.0 was resolved through the checkout launcher. A fresh R process extracted
the final Chapter 16 R chunks with `knitr::purl`, executed them without cache,
and reproduced every numeric value in the chapter's `s16` receipt. Assertions
also checked the exact point-estimate identities, the distinct Welch and
classical statistics, disjoint learning and held-out units, predictor-column
availability in both sets, and the direction of the leakage and overfitting
comparisons.

| Quantity | Reproduced value |
|---|---:|
| Finite-population age-only slope | 0.036723816393760 |
| Finite-population adjusted age slope | 0.026885173178123 |
| Latent pre-measurement age rule | 0.028000000000000 |
| Recorded source coefficient; latent rule: social media | -0.533533786572297; -0.55 |
| Recorded source coefficient; latent rule: TV | 0.311646662154144; 0.35 |
| Recorded source coefficient; latent rule: radio | 0.595079781147283; 0.60 |
| Recorded source coefficient; latent rule: print | 0.486393753674010; 0.50 |
| Within-source age-slope range | 0.025479869074142 to 0.028054221774353 |
| Binary mean difference; OLS coefficient | 1.185714285714286; 1.185714285714287 |
| Ordinary OLS / pooled Student t; df | 3.208648372705724; 118 |
| Welch t; df | 3.182192655868046; 102.471131550669 |
| Classical five-group F; df | 8.381812957408979; 4 and 295 |
| Welch five-group F; df | 7.320807631165560; 4 and 112.425284937609 |
| Classical five-group R squared | 0.102053183237969 |
| Valid descriptive-model R squared; leakage R squared | 0.122277516285767; 0.131956275921432 |
| Learning size; held-out size; random columns | 150; 2,000; 25 |
| Held-out RMSE: modest; rich; mean baseline | 1.880142878709776; 2.061987662423383; 1.991200084817640 |

The binary mean difference and OLS coefficient differ only by floating-point
rounding, approximately `1.1e-15`; their analytical point-estimate identity is
preserved. The reproduced inferential statistics remain distinct.

## Independent statistical-methods reading

An independent read-only `critic_methods` review checked exact source blob
`ba93f9a62965dc1a9ae1c67a3c54d536976773cb` before and after its reading. The
hash matched both times. It scored correctness, assumptions, interpretation,
and precision 5/5, with no fatal, major, or minor finding and no requested
source change.

The critic passed all four registered items. It confirmed that the Chapter
14–16 bridge preserves point estimates without inheriting a Welch/OLS
inferential identity; that data, coefficients, uncertainty, tables, worked
example, summary, and conclusion use the finite-population recorded-outcome
estimand; that the absence of sampling uncertainty is coherent for the census
target; and that every predictive example has a declared time boundary and
held-out logic. It also confirmed that the AI-error box retains exactly one
mistake, evaluation on the training data.

## Style, render, and exit evidence

- Checkout-local deterministic `book-style` lint passed with zero candidates.
- The final source received a complete top-to-bottom Croatian prose pass against
  H1–H10. The corrected surface adds no governed colon, mid-sentence em dash,
  mechanical transition, unsupported citation or empirical claim, bold misuse,
  unexplained notation, or assessed code-production task. The visible worked
  receipt is below the twelve-line ceiling.
- Structure lint passed with 12 top-level sections, 3,924 prose words, body
  evenness 0.22, and zero candidates. The structure scan retained the vignette,
  four definitions, three conceptual figures, one HTML/static twin pair, one
  divljina callout, both AI callouts, and all four exercise tiers.
- Figure-introduction check passed for all three conceptual figures and four
  source variants. The all-widget contract passed for all 17 registered pairs.
  Chapter 16's widget and print-twin sources remained byte-for-byte unchanged,
  with normalized SHA-256
  `9eefa6f2c9528876af6c225429a855b9af961d289b7576e489c813f03d295bf3`.
- `quarto render chapters/16-regresija.qmd --to html` passed from the exact
  source state in an isolated output directory. Rendered assertions found the
  finite-population target, absence of sampling uncertainty, pooled Student and
  Welch distinction, classical and Welch F values, target-leakage diagnosis,
  prediction-time boundary, held-out logic, and worked-example uncertainty
  label. The two removed false claims were absent. Generated AI-export changes
  were inspected and restored to their pre-packet state.
- Source-diff and whitespace checks passed. Chapters 14 and 15 retain blobs
  `449c88f25e032fd8d4a9066deb45c8648497e8e5` and
  `0eadfd02627a95aed614a005f93f81878249ea10`. Source assertions found no active
  `confint` call, old truth/recovery variable, old false-equivalence sentence,
  or old prediction-gain claim.
- The comprehensive-review workflow validator and its two negative fixtures
  passed at closeout with no active packet and `P1A-C02` as the next permitted
  packet.

## Forward-effects declaration

No new future-relevant effect was discovered. The later Chapter 16 work retains
its stable registered items and `OA-C16-ACCEPTANCE`; none is a blocker for this
packet. No outgoing handoff was created because the existing register already
contains every known downstream Chapter 16 obligation and duplicating it would
add no information.
