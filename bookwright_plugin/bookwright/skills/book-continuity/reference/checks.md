# Consistency battery

Run chapters in canonical `_quarto.yml` order.

## Deterministic checks

Measure:

- a non-exempt `callout-vinjeta` opener with real, non-placeholder content;
- `#def-` definition divs;
- logical figures, counting an HTML widget and static print twin once;
- `callout-divljina`;
- one `callout-model` and one `callout-greska`;
- all four exercise tiers under `## Zadaci`;
- unresolved TODO or placeholder content;
- widget registration and static-twin coverage against `data/widgets.json`.

Compare element counts with the provisional bands in `conventions.json`.
Numbered chapters 1–17 require one registered widget and a static twin. The
preface and chapter 18 are exempt.

## Reader judgments

Reconcile the chapter with its ratified spine. The vignette should frame the
chapter's central problem, `#def-` divs should be reserved for load-bearing
terms, figure introductions should say what the figure shows and why it matters,
and exercises should make the reader use the key terms.

If the spine is not ratified, report spine-dependent judgments as provisional.
Do not treat an empty key-term list as evidence that definitions are correct.

Check terminology and notation against `concept-ledger.json`: no concept is
defined twice, named inconsistently, used before introduction, or assigned a
symbol already carrying another book-wide meaning.

`critic-voice` judges whether the manuscript sounds like one author while
honouring planned exceptions. `critic-arc` judges the cumulative build, planted
conceptual seeds, five parts, and finale.

## Recalibration

Measure real chapters before changing numeric bands. Empty skeletons and HTML
comments do not establish the book's structural distribution.
