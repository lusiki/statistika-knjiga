# Chapter panel

Six independent read-only critics, one synthesiser, and an approval-gated
reviser review a chapter.

## Critics

1. `critic-methods` — statistical correctness, assumptions, and interpretation.
2. `critic-skeptic` — hidden assumptions, alternative explanations, and
   overclaim.
3. `critic-pedagogy` — beginner comprehension, sequencing, and all four exercise
   tiers.
4. `critic-evidence` — citation integrity, source verification, and empirical
   support.
5. `critic-style` — manuscript qualities the linter cannot judge.
6. `critic-structure` — spine fit, vignette, definitions, figures, AI boxes, and
   exercises.

Each critic returns scores, strengths, concerns with
`severity/location/reason/fix`, and a one-line verdict. The evidence critic also
returns `missing_or_unverified`. Critics write nothing.

## Synthesis

Merge equivalent concerns and count agreement, but rank severity before
agreement. A fatal methods or evidence error remains first even when clean role
boundaries mean only one critic reports it. Present critic disagreements as
trade-offs rather than averaging them away.

## Revision

Show a before-and-after proposal for each accepted finding and write only after
approval. Never insert a citation absent from or unverified in
`references.bib`, and never invent an empirical claim. Verifiable Croatian
evidence follows the same rule as evidence from any other geography.

## Calibration

The book is an introductory statistics textbook for undergraduate
social-science students who have no assumed programming and no mathematics
beyond secondary school. Critics flag incorrect methods, overclaims, evidence
failures, broken scaffolding, and violations of the book's explicit contract,
not the absence of graduate-level depth.
