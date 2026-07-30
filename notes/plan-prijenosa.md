# Plan prijenosa — from the kolegij lectures into the book spine

Working document, 30 July 2026. Companion to [struktura-knjige.md](struktura-knjige.md),
which owns scope and chapter order, and to `STYLE.md` H10, which owns what
happens to code. This file owns **sequence** — what gets ported, in what order,
and what each round is actually buying.

Source: `https://lusiki.github.io/Osnove-statistike/` (13 lectures + practical
project). This plan covers **only material that exists**. Chapters with no
source are listed at the bottom and scheduled later.

## Evidence base

Inspected in detail: weeks **1, 2, 5, 8, 10** and the practical project.
Weeks 3, 4, 6, 7, 9, 11, 12, 13 are sized by extrapolation from the syllabus
plus the very consistent pattern in the five inspected lectures. **Confirm the
numbers at port time** — every estimate below marked *(procj.)* is an
extrapolation, not a measurement.

Measured pattern across the five inspected lectures:

| Lecture | Prose | Code share | Figures | Sections |
|---|---|---|---|---|
| W1 Zašto statistika | ~8 250 | **0 %** | none | 12 |
| W2 Uvod u R | ~6 000 *(procj.)* | 35 % | few | 21 |
| W5 Deskriptivna | ~8 500 | 30 % | **none** | 13 |
| W8 Uzorkovanje | ~8 750 | 35–40 % | many | 21 |
| W10 Hi-kvadrat | ~8 500 | 35 % | some | 21 |

Three facts fall out of this table and they drive the whole plan.

**A lecture is roughly 8 000–8 500 prose words.** That is larger than one
chapter target and smaller than two. So every port is either a cut or an
expansion, never a translation.

**Week 1 contains no code at all.** The decision that Dio I is code-absent is
not a constraint being imposed on the source — the source is already there.

**Week 5 produces no figures**, deferring them to week 6. Chapter 4's figures
were therefore all made fresh, and the same will be true elsewhere. **Figures do
not come across in a port.**

## The two shapes of a port

| Shape | Weeks | Arithmetic | The work is |
|---|---|---|---|
| **One week → two chapters** | 1, 5, 8, 9 | source **short of** target | expansion |
| **One week → one chapter** | 6, 7, 10, 11, 12, 13 | source **exceeds** target | selection and cutting |

Chapter 16 is the exception that belongs to neither. Week 13 feeds one chapter,
but that chapter is the summit at 6 000 words and needs the reveal that chapters
14 and 15 were regression all along — which no lecture contains.

Knowing which shape you are in before you start is most of the discipline. A
cutting port that drifts into expansion produces a bloated chapter; an expansion
port treated as a cut produces a stub.

## The fixed overhead nobody budgets for

The course supplies **two of the seven skeleton parts** — *Izgradnja pojma* and
*Razrađeni primjer*. The vignette, the widget, the divljina box, both AI boxes,
the summary, the terms and the four exercise tiers are new work in **every**
chapter, sourced or not. Reckon roughly 800–1 200 words per chapter, so about
14 000 words of fresh writing hidden inside the word "porting".

The hardest single item is the **divljina box**, which needs a genuine published
claim with a verifiable source. The lectures supply exactly one — the Berkeley
admissions case in week 1, and `@bickel1975` is already in the bibliography.
The other twelve sourced chapters need their divljina case found independently.
Treat it as a parallel sourcing project, not a by-product of the port.

## Rounds

Each round is a coherent unit of risk. Do not start the next one until the
current one renders and passes both linters.

### Round 1 — the two ends of the spectrum

**W1 → ch1 + ch2.  W2, W3, W4 → Dodatak A.**

These two jobs are first because **neither requires the concept/code
separation** that makes every other port hard. Week 1 is pure prose with no code
to strip. Weeks 2–4 are pure code with no concept to extract. Everything in
between demands the separation discipline, and it is better learned on jobs
where it is not also being invented.

Two further reasons to front-load the praktikum. It is the destination for
everything H10 evicts from later chapters, so if it does not exist, evicted
material silently stays put. And it already carries **two outstanding IOUs** —
the *Računski* tiers of chapters 4 and 5 both promise a procedure "u
praktikumu" against a 110-line stub.

| Job | Source | Target | Shape |
|---|---|---|---|
| ch1 Zašto statistika | W1 §1–3 | 4 500 | expansion |
| ch2 Mjerenje i dizajn | W1 §4–12 | 5 500 | expansion |
| Dodatak A | W2+W3+W4 | 12 000 | heavy cut |

W1's split point is clean. Sections 1–3 (izbor, zašto komunikolog treba
statistiku, kad nas intuicija iznevjeri) are chapter 1. Sections 4–12
(mjerenje, razine, pouzdanost, valjanost, varijable, eksperimentalni i
neeksperimentalni dizajn, eksterna valjanost) are chapter 2.

Watch for: the lecture is written for komunikolozi, and the book serves all of
the social sciences, so the portal/TikTok framing needs widening at least once
per chapter. Stevens 1946 is cited for measurement levels and is **not in
references.bib** — add it or attribute it to a literature. Week 4's loops,
`purrr::map` and the DRY principle have no place in the book and should be cut
rather than condensed.

Round 1 output: three chapters and the appendix, plus a validated code-absent
register.

#### Round 1 — done, 30 July 2026

| Job | Target | Delivered | Shape held |
|---|---|---|---|
| ch1 Zašto statistika | 4 500 | ~4 080 | expansion |
| ch2 Mjerenje i dizajn | 5 500 | ~4 800 | expansion |
| Dodatak A | 12 000 | ~5 100 | heavy cut |

Both linters clean on all three; all three render; every executed block in the
appendix runs end to end. Provenance is recorded in each file's header comment.

**The code-absent register was not clean and is now.** `01-zasto-statistika`
carried an `echo: true` block in its worked example, which the ladder forbids in
Dio I. It is back in the plumbing register. Nothing else in Dio I had visible
code, and the rendered HTML now shows zero visible code cells in chapters 1 and
2 against 137 in the appendix.

**Dodatak A needed a document-level `execute: echo: true`.** The project default
flipped to `echo: false` when H10 landed, which silently applied to the one file
in the book whose entire purpose is showing code. Before the fix the appendix
rendered with every block hidden.

Three bibliography debts were paid rather than the one the plan anticipated.
`stevens1946` and `wickham2023` were on the list; `tversky1973` was not, and was
needed once the availability heuristic came across from W1 §3. All three were
verified against Crossref or the publisher record, none from memory. The
Cronbach alpha threshold in W1 §6 was **not** ported, because no source for it
exists in the bib; the prose names the convention without the number.

Two items are short and both are known.

The appendix is at roughly 5 100 of 12 000 words. Part of that gap is not round
1 work at all, since round 3 sends W6's ggplot2 mechanics here, and the plotting
section is currently only as deep as the chapter 5 IOU requires. The rest is
real, and the honest description is that W2–W4 were cut harder than the plan
budgeted. Loops, purrr, DRY and multi-file reading were cut outright per the
plan and are not coming back. What would genuinely thicken it is more worked
cleaning cases and more explanation per concept.

The chapters land under target because the fixed overhead absorbed less than
expected once the argument sections carried their own weight. Neither reads
thin, and padding to hit a number would be the wrong repair.

**`conventions.json` is now due for ratification.** The structure linter flags
both chapters for section count against an `essay` band of 6 to 9, while their
body evenness (0,19 and 0,23) is the best in the book, ahead of chapter 4 at
0,27. STYLE.md S7 says the bands are placeholders until four or five chapters
exist and are then measured. Four now do. The band appears to have been set
before the seven-part skeleton was populated, since the skeleton alone spends
five sections and leaves only four for argument, which no 5 500-word chapter can
respect. Measure and ratify before round 2, or the same flag fires on every
chapter from here on.

**Two new IOUs point at the praktikum.** Chapters 1 and 2 now end their
*Računski* tier the way chapters 4 and 5 already did. All four are discharged in
the appendix's closing section, each as a runnable recipe. Chapter 1's *Računski*
tier also stopped assuming an R installation, which H10 forbids; it now works
from the constructed portal example and the chapter's own rendered table.

### Round 2 — the demonstration register

**W8 → ch8 + ch9.**

The highest-value round in the plan, taken early because it is also the highest
risk. Chapter 8 is the pedagogical hinge, and the claim that the whole
inferential apparatus is a readable loop has not been tested anywhere yet.

Week 8 is the richest lecture in the course and it gives more than prose. It
already contains, as working R, the specifications for the book's **two
flagship widgets**:

- the CLT demonstration at n = 5, 15, 30, 100 over a skewed variable → **w08
  Stroj za CLT**
- the 100 repeated confidence intervals with a coverage tally → **w09 Hvatač
  intervala**

So porting week 8 converts a widget *design* problem into a widget
*translation* problem, R simulation into OJS. That is the single biggest
unblocking effect available anywhere in the plan, and the widget build order in
struktura-knjige.md already puts these two first.

The lecture also names its own split point. Sections 1–10 are chapter 8;
sections 11–18 are chapter 9.

`media_population.csv` — 50 000 simulated adults with **known** parameters
(mean trust 4,87, SD 1,98, mean daily minutes 174, portal share 0,304) — should
become a book dataset beside `anketa_mreze`, registered in Dodatak C and
labelled simulated under the same rule as `R/podaci-nastavni.R`. A population
whose truth is known is exactly what Dio III needs, and the book does not have
one yet.

Watch for: `t.test()` appears here in week 8, eight chapters before the book
introduces it. Under the ladder Dio III is the demonstration register, so the
t-test call belongs in chapter 14, not chapter 9. Bootstrap stays — the plan
already makes it "the reader's own invention" in chapter 9.

#### Round 2 — done, 30 July 2026

| Job | Target | Delivered | Shape held |
|---|---|---|---|
| ch8 Uzorkovanje | 4 500 | ~3 680 | expansion |
| ch9 Procjena | 4 000 | ~2 960 | expansion |

Both linters clean on both chapters, both render, and every number in both
chapters is computed inline from the code that is actually in the file, so prose
and data cannot drift apart. Section rhythm is the best in the book so far, with
body evenness 0,18 on chapter 8 and 0,20 on chapter 9 against chapter 4's 0,27.

**The two flagship widgets were already built**, so the unblocking this round was
supposed to buy had in fact been banked earlier. What round 2 actually delivered
is the prose the widgets were waiting for. Both chapters were skeletons of about
460 prose words each, and the widget was the only finished thing in them.

**`media_population.csv` became `populacija_medija`.** The CSV itself was not
available, so the population was rebuilt as a generator in `R/podaci-nastavni.R`
against the parameters the lecture prints. Realised values land at 4,88 mean
trust with SD 1,98, 174,5 mean daily minutes and a portal share of 0,302, against
the lecture's 4,87 / 1,98 / 174 / 0,304. It is registered in Dodatak C, labelled
simulated in both chapters before the first number, and its generator restores
the RNG state exactly as `anketa_mreze` does. Chapter 4 was re-rendered as a
control and its sixty-eight printed numbers are byte-identical, so the new
dataset perturbs nothing.

**A known population is worth more than the plan credited it.** Because the truth
is knowable, chapter 8 can show that the SE formula and three thousand repeated
draws agree to the third digit, and chapter 9 can count coverage rather than
assert it, landing at 94,9 % over ten thousand intervals. Neither claim has to be
taken on faith, which is the whole argument for the demonstration register.

**Three bibliography debts paid, one of them not on the list.** `ismay2019` was
scheduled and carries the simulation-first framing in chapter 8's vignette.
`squire1988` was not on the list and turned out to be the round's most valuable
addition, because the 1936 *Literary Digest* case is the one genuine published
claim in this material and it gives chapter 8 a divljina box that argues the
opposite of the moral it is usually told with. `hoekstra2014` gives chapter 9 its
divljina box, where the wild material is the misreading itself. All three were
verified against Crossref, and `squire1988` additionally against OpenAlex; neither
source records an end page, so the entry deliberately carries none rather than a
plausible guess.

**Two structural debts discharged.** The Bessel divisor was left in chapter 4 as
an assertion with a note in `concept-ledger.json` saying chapter 8 owed its
demonstration. Chapter 8 now pays it by simulation, and the ledger entry records
the date. And `conventions.json` was ratified against the five populated chapters
as round 1 required, moving the `essay` section band from 6–9 to 7–12; the
reasoning is in STYLE.md's provenance.

**One deliberate departure from the split.** The plan sends sections 11–18 to
chapter 9, but margin of error and sample-size planning (section 14) stayed in
chapter 8, because "why polls of 800 people work" is chapter 8's scope in
struktura-knjige.md and the arithmetic belongs beside the standard error rather
than beside the interval. Recorded in both chapter headers. The t-material was
cut as the plan directed, leaving one forward announcement in chapter 9 pointing
at the chapter on two groups. `prop.test()` went the same way.

Both chapters land under target, as all three round 1 chapters did. The gap is
real and the honest description is that the fixed overhead again absorbed less
than budgeted once the argument sections carried their own weight. Chapter 9 is
the shorter of the two and the likelier candidate for a later enrichment pass,
with the bootstrap section the natural place to thicken.

**One pre-existing gap found and closed.** Chapter 2's four `#def-` divs had
never been entered into `concept-ledger.json`. They are in now, so the ledger and
the book agree at fourteen concepts against fourteen definition divs, which is
what the ledger's own note requires. Entering them surfaced a collision worth
naming. **Pouzdanost means two different things in this book**, a property of an
instrument in chapter 2 and a property of a procedure in chapter 9, and the two
are unrelated. H9 asks for one meaning per symbol and the same discipline applies
to a term. The ledger now carries the warning on the chapter 2 entry; neither
chapter currently conflates them, and no chapter may.

**Watch the Quarto binary.** `quarto` on PATH in this checkout is 1.6.43 while
`C:\Program Files\Quarto\bin\quarto.exe` is 1.9.38, which is what `docs/` was
built with. Rendering with the one on PATH silently downgrades the boilerplate of
every file it touches. Use the explicit path.

### Round 3 — closing Dio II

**W6 → finish ch5.  W5 §9 → ch6.**

Chapter 5 is a partial draft at ~1 050 of 4 500 words with one stub section, so
this round finishes what is already started rather than opening something new.
Week 6's ggplot2 mechanics go to Dodatak A, which by now exists.

Chapter 6 is the plan's most under-resourced sourced chapter and the numbers say
so plainly. Week 5 §9 is about **1 500 words** of correlation against a **4 000
word** target. Budget for enrichment from the outset rather than discovering the
deficit mid-draft. Week 10 §13 (Simpson's paradox, stratified analysis) is a
natural donor — the plan already has Simpson returning quantitatively in
chapter 6.

#### Round 3 — done, 30 July 2026

| Job | Target | Delivered | Shape held |
|---|---|---|---|
| ch5 Vizualizacija | 4 500 | ~3 850 | cut, then expansion |
| ch6 Povezanost | 4 000 | ~3 465 | expansion |
| W6 mechanics → Dodatak A | — | ~5 000 → ~6 100 | heavy cut |

Both linters clean on both chapters, all three files render, and every number in
both chapters is computed inline from the code that is in the file. Section
rhythm holds at body evenness 0,27 on chapter 5 and 0,25 on chapter 6. These are
the best target ratios in the port so far, at 86 % and 87 % against 82 % and
74 % in round 2.

**Chapter 5 was two ports, not one.** The plan calls week 6 a cutting port, and
that is true of the lecture as an artefact, since roughly two thirds of it is
ggplot2 mechanics that H10 evicts. What remains after the eviction is *smaller*
than the chapter target, so the concept half was an expansion. Naming the shape
once per job is not enough when the ladder removes a fixed fraction of the
source; the shape has to be named for what survives the eviction.

**The praktikum absorbed the mechanics and is now the book's structural
outlier.** Week 6's geometries, aesthetic mapping inside and outside `aes()`,
facets, labels, themes, scales, axis formatting and `ggsave` all landed there,
taking it from roughly 5 000 to 6 100 prose words against its 12 000 target. Two
deliberate cuts. The patchwork package went out entirely, because composing
several plots on a page is layout rather than reading, and because it would add
a build dependency that `publish.yml` does not install. Colour selection is
taught through `brewer` and `viridis` and never through a literal colour value,
since DESIGN.md forbids one outside the four design files and `check-tokens.R`
enforces it.

**`limits` against `coord_cartesian()` turned out to be the load-bearing
mechanic.** Chapter 5 argues that a truncated axis is a claim about the data.
The appendix now shows that the two ways of truncating are not equivalent, since
`limits` discards observations before anything is computed and silently moves
every fitted line, while `coord_cartesian()` changes only the visible window.
That pairing is the appendix earning its place, because the chapter can state
the principle but only the appendix can show that the honest version and the
dishonest version differ by one function name.

**Three bibliography debts paid, one of them not on the list.** `cleveland1984`
and `wilkinson2005` were both scheduled. `matejka2017` was not, and it took over
chapter 6's divljina box so that Anscombe stops carrying the vignette, the
divljina and the worked example in two consecutive chapters. Its entry
deliberately carries only the short title, because neither Crossref nor OpenAlex
records the subtitle that circulates in secondary sources, and ACM blocks
automated retrieval. Same discipline as the missing end page on `squire1988`.
`tufte2001` was already in the bib and unused; it now anchors the claim about
decoration, which had been leaning on intuition.

**The divljina boxes stopped being demonstrations.** Both chapters had been
using Anscombe, which is a constructed teaching example rather than a claim
somebody published and somebody else repeated. Chapter 5 now dissects the
absolute prohibition on pie charts against what `cleveland1984` actually
measured, and chapter 6 dissects the popular reading of the Datasaurus. Both
boxes end where the box is supposed to end, on the difference between the
finding and what was made of it.

**One deliberate departure from the plan.** The plan sends week 10 §13 to
chapter 6, and the source example there is a click-through rate by device, so a
difference of proportions. It came across as a *correlation* reversal instead,
built as three departments where the pooled coefficient is
positive and every within-department coefficient is negative. The reason is that
the quantitative return of the paradox in a correlation chapter is a question
about the sign of a coefficient, and the proportion version already belongs to
chapter 13, which carries `simpson1951` and `bickel1975` for exactly that.

**Two numbers in the draft did not survive contact with the data**, and both
were caught by computing before writing rather than after. The agreement-of-sign
figure is 27 %, not the above-half value the prose first implied, because the
relationship is negative — the draft had silently assumed a positive one.
And restricting the sample to the youngest age group does not push the
correlation toward zero, it pushes it to +0,18, the opposite sign. That is the
better illustration and it is now the honest one, since the generator gives that
subgroup no internal age effect at all, so the whole 0,18 is what noise produces
on 90 observations. The chapter says so, and the same pair of facts became the
`callout-greska`.

**`conventions.json` has no template that fits the praktikum, and this is now
blocking.** The structure linter measures every file against `essay`. The
appendix flagged 11 candidates before this round and 17 after, and switching it
to the existing `catalogue` template makes it worse at 24, because catalogue
bands expect entries of 120 to 400 words. The real conflict is that the essay
template treats any `##` carrying three or more `###` subsections as a monster,
which a syntax manual cannot avoid and should not try to. Splitting the ggplot2
material into four top-level sections was worth doing on its own merits and
removed the 1 243-word section, but it cannot remove the flag class. **Round 4
should either add a `manual` template or exempt `dodaci/` from S7 section
rhythm.** Left untouched this round rather than ratified mid-port, since the
round 2 precedent is to measure first and change the band deliberately.

### Round 4 — the instrument batch

**W10 → ch13.  W11 → ch14.  W12 → ch15.**

Three chapters of near-identical shape, all cutting ports, all in the
one-call instrument register. Establish the pattern on chapter 13 and the other
two follow it mechanically. This is the round where the port feels fastest.

Week 10 is ~8 500 words against a 4 500 word chapter, so **roughly half is
cut**. Out of scope per the plan: McNemar, Benjamini-Hochberg, odds ratios,
Yates correction. §13 Simpson goes to chapter 6 (see round 3), not here.

Watch for: chapter 14 must teach the three t-test variants as one linear model
with a binary predictor, and chapter 15 ANOVA as the linear model with a
categorical predictor. The lectures teach them as separate procedures. **This is
a restructuring, not a port**, and it is the one place in round 4 where the
source's organisation actively fights the book's.

#### Round 4 — done, 30 July 2026

| Job | Target | Delivered | Shape held |
|---|---|---|---|
| ch13 Kategorički podaci | 4 500 | ~3 690 | heavy cut |
| ch14 Uspoređivanje dviju grupa | 4 500 | ~3 520 | cut plus restructuring |
| ch15 Uspoređivanje više grupa | 4 000 | ~3 220 | cut |

Both linters clean on all three, the figure-introduction check passes, all three
render, the widget registry check passes on all seventeen widgets, and every
number in all three chapters is computed inline from the code that is in the
file. Section rhythm holds at eleven sections each with body evenness 0,32, 0,21
and 0,24.

**The batch worked because one dataset carried all three chapters.** None of the
three course datasets exists in this repository, so all three cases were
recomputed on `populacija_medija`. That turned out to be worth more than a
substitution. Chapter 13 tests whether age group and news source are associated,
chapter 14 compares two of those sources on trust, and chapter 15 compares all
five. One population, three questions, escalating — which the three separate
lecture datasets could never have given. The plan predicted round 4 would feel
fastest; the reason it did is that the register was settled in chapter 13 and
the data question was answered once.

**A known population turns three procedures into demonstrations.** Chapter 13's
goodness-of-fit section tests the sample's education distribution against a flat
reference and against the true population shares, and the same data give
χ² = 209 against the first and 1,77 against the second. Ordinary teaching has to
assert that the choice of reference distribution matters; here the book can say
which one is true. Chapter 14 does the same for confounding, where the raw gap
of 1,30 boda falls to 0,90 inside a narrow age band, so roughly a third of it is
age and that fraction is measured rather than argued.

**One lecture claim did not survive contact with the data, and it is the central
one in week 12.** The lecture computes the inflated error rate as 1 − 0,95¹⁰ and
reports about 40 %. That formula assumes independent tests, and ten pairwise
comparisons among five groups share groups. Simulation puts the real rate at
27,4 %, while ten genuinely independent tests land at 40,3 %, matching the
formula exactly. Chapter 15 reports the measured value, keeps the formula as the
independent-case upper bound, and holds the ANOVA at 4,2 %. Recorded in the
chapter header. This is the round-3 lesson repeating: compute before writing.

**The chi-square small-cell distortion also runs the other way from the usual
telling.** With expected counts near two the empirical 95th percentile of the
statistic falls *below* the theoretical cut-off and the test rejects 3,4 % of
the time rather than 5 %. Chapter 13 states what it measured in that table shape
and does not generalise. That measurement is what earns the divljina box, which
dissects the threshold of five as a recommendation traceable to one 1954 paper
rather than a mathematical condition [@cochran1954].

**Three bibliography debts paid, none of them on the list.** The plan budgeted no
sources for round 4 and all three chapters needed one, because in each the
lecture's own material supplied no genuine published claim. `cochran1954` gives
chapter 13 the threshold-of-five box, `belia2005` gives chapter 14 the error-bar
overlap box with its 473 respondents, and `nieuwenhuis2011` gives chapter 15 the
significant-here-not-there box with its 513 reviewed articles. All three were
verified against Crossref and Nieuwenhuis additionally against OpenAlex and
Europe PMC. Cochran's entry deliberately carries no end page, since neither
index records one, following the `squire1988` precedent.

**Chapter 14 was the restructuring the plan warned about, and it cost a
reordering rather than a rewrite.** The lecture teaches three t-tests in
sequence and reaches the formula interface at the very end. The chapter reverses
that. Design and unit of independence come first, the estimate with its interval
before any test, and the linear model arrives as the thing all three designs
already were. The reveal that the two-group test is the smallest case of one
framework now lands here rather than in chapter 16, which frees chapter 16 to
spend its reveal on prediction against explanation.

**The paired demonstration is the strongest single passage in the round.** One
constructed set of sixty paired measurements, analysed correctly, gives an
interval of 0,25 to 0,71 and p = 0,0001. The same numbers analysed as
independent groups give −0,14 to 1,10 and p = 0,126. Same data, same mean
change, opposite conclusions, and nothing between them but the design.

**Eight new definition divs and eleven notation entries entered
`concept-ledger.json`**, taking it to thirty-one concepts against thirty-one
definition divs. Entering them surfaced one collision. The standardized residual
is conventionally written *r*, and *r* has meant Pearson's correlation since
chapter 6. Chapter 13 writes it $e_{ij}$ and says so in the definition div
itself; the ledger carries the warning on both entries. This is the second such
catch after *pouzdanost* in round 2, and it suggests the collision check belongs
in the per-chapter procedure rather than in a later audit.

**Berkeley moved out of the vignette-and-divljina double duty.** In the previous
draft `bickel1975` carried the vignette, the divljina, the worked example and
two exercises of chapter 13. It now carries the vignette and one exercise, the
divljina went to Cochran, and the worked example went to the book's own data.
The chapter still closes the Berkeley loop, in a paragraph that names the
missing variable and hands the stratified version to chapter 6, where round 3
put it.

Three cuts are worth naming because they are permanent. McNemar, Benjamini-
Hochberg, odds ratios and Yates went out of chapter 13 per the plan. APA
reporting templates, forest plots, trimmed means and the power calculation went
out of chapter 14, the last of these because it belongs to chapter 11. Levene's
manual implementation, compact letter display, Games-Howell and two-way ANOVA
went out of chapter 15. None is coming back.

All three land under target, as every ported chapter so far has. Chapter 15 is
the shortest and the likeliest candidate for a later enrichment pass, with the
planned-contrasts material the natural place to thicken.

### Round 5 — completing Dio III and Dio IV

**W7 → ch7.  W9 → ch10 + ch11.**

Week 7 is a trimmed port and the plan is explicit that everything not used later
is cut. Week 9 splits, so it is an expansion port. The Cohen's d and power
material becomes chapter 11.

By the end of this round the demonstration and evidence registers are both
exercised and Dio III and Dio IV are complete except for chapter 12.

#### Round 5 — done, 30 July 2026

| Job | Target | Delivered | Shape held |
|---|---|---|---|
| ch7 Vjerojatnost | 4 500 | ~3 230 | cut, then expansion |
| ch10 Logika testiranja | 4 500 | ~2 890 | heavy cut plus restructuring |
| ch11 Veličina učinka i snaga | 4 000 | ~2 650 | expansion |

**These counts are not comparable to the ones recorded in rounds 1 to 4.** They
come from one counter applied uniformly, which measures chapter 13 at 3 126,
chapter 14 at 2 677 and chapter 5 at 3 693. Earlier rounds used a looser count
and their recorded figures run roughly a quarter higher. Measured against
chapters written the same way, chapter 7 is the second longest ported chapter in
the book and chapter 11 the shortest.

Both linters are clean on all three, the figure-introduction check passes, all
three render, and every number in all three chapters is computed inline from the
code that is in the file. Section rhythm holds at eleven, eleven and ten sections
with body evenness 0,27, 0,22 and 0,26.

**The two error rates stopped being definitions.** Because the population is
known, chapter 10 can pick a question whose answer it already has. Women and men
differ in trust by 0,018 of a point, so the null is true, and across eight
hundred fresh samples the permutation procedure crosses the 0,05 threshold in
5,0 % of them. Readers of print and of portals differ by 0,74 of a point, so the
null is false, and the same procedure finds it in 79,5 %. Chapter 11 then names
the second number power and measures the whole curve, from 22,7 % at sixty
people to 99,7 % at eight hundred. Ordinary teaching asserts that alpha equals
the threshold; here the book counts.

**The strongest passage in the round is the streak selection bias, and it is in
chapter 7.** A fair coin has no memory by construction, yet the average share of
heads on the flips that follow three heads is 0,459 in sequences of a hundred
and 0,356 in sequences of twenty. The gap of roughly four percentage points at
n = 100 is the same order as the effect the hot-hand literature was looking for,
so the measuring procedure itself pushes toward the conclusion that was drawn.
That measurement is what earns the divljina box, which dissects the canonical
finding [@gilovich1985] against its later correction [@miller2018] without
borrowing a single number from either.

**Chapter 11 measures the winner's curse rather than describing it.** Across
three thousand studies of sixty people the average estimate is 0,74, exactly the
truth. Among the studies that crossed the threshold the average is 1,50, twice
the truth, and 0,15 % of them carry the wrong sign. At five hundred people the
exaggeration factor falls to 1,03. The mechanism is visible in one figure and
needs no appeal to anyone's honesty, which is what the book's own rule about
statistics not being a morality play requires.

**Four bibliography debts paid, none of them on the list.** The plan budgeted no
sources for round 5 and all three chapters needed one, because in each the
lecture supplied no genuine published claim. `gilovich1985` carries chapter 7's
vignette and `miller2018` its divljina, `greenland2016` gives chapter 10 a
divljina distinct from the ASA statement that carries its vignette, and
`button2013` gives chapter 11 the underpowered-field box. All four were verified
against Crossref and OpenAlex.

**One citation was deliberately written thinner than it could have been.** The
median-power figure that circulates from `button2013` is not in any record this
checkout could verify, since the article is paywalled and neither index carries
an abstract with it. The box therefore cites only what the published abstract
states, that average power in the field is very low and that the consequences
include overestimated effects and low reproducibility. Same discipline as the
missing end page on `squire1988` and the missing subtitle on `matejka2017`.
`amrhein2019` was considered for chapter 10 and dropped for the same reason,
since nothing beyond its title could be verified.

**Cohen's d changed owner.** Round 4 put the definition div for standardizirana
razlika in chapter 14, but the plan assigns the concept to chapter 11, which
comes first. The div moved, chapter 14 keeps the formula and a back reference,
its prerequisite line changed from chapters 9, 10 and 13 to chapters 10, 11 and
13, and both the concept and the notation entry moved in
`concept-ledger.json`. **This is the first ordering collision the port has
produced, and it was invisible until the earlier chapter was written.** Worth
checking for the same pattern in round 6, where chapter 16 harvests material
planted in chapters 2, 14 and 15.

**The plan's own instruction was the one thing that had to be departed from in
chapter 10.** Week 9 teaches the whole t apparatus, and chapter 14 took it in
round 4, so the entire one-sample, two-sample, Welch and `t.test()` layer was
cut here rather than duplicated. What carries chapter 10 instead is the
permutation test, which fits the ladder's demonstration register and needs no
distributional assumption. The one-tailed test went out entirely, since no later
chapter uses it and the plan forbids porting what is not used later. Multiple
testing and the Bonferroni correction went to chapters 15 and 12, which already
own the family-wise error rate and the forking paths.

**The plan asks for a framed Bayesian box on two pages and DESIGN.md has no such
element.** STYLE.md forbids improvising one, so it became a `##` section. The
content is unchanged and the decision is recorded in the chapter header. If a
framed aside is genuinely wanted, it should be added to the design system rather
than invented in a chapter.

**Chapter 10 had a hole that only surfaced during writing.** Its vignette is the
ASA statement, whose central claim is that conclusions should not rest on whether
p crosses a threshold, and the draft then used 0,05 throughout without ever
saying what the threshold is. A new section now says it is a convention, that
0,048 and 0,052 are the same evidence, and it measures how much the p-value
itself moves under repetition. Across the eight hundred samples with a real and
constant difference the median p is 0,003, a quarter of the samples land above
0,033, and a tenth above 0,134. That instability is the strongest available
argument for reporting the estimate and its interval first, and no source is
needed for it because the book measures it.

**A round 4 drift was found and half repaired.** STYLE.md H10 says that from the
visualisation chapter onward the artifact graded in the *revizija modela* tier
includes its code, which chapters 5 and 6 do and chapters 13, 14 and 15 do not.
Chapters 7, 10 and 11 now carry a short unexecuted block inside
`callout-greska`. **Chapters 13, 14 and 15 still owe theirs**, and that is a
round 6 cleanup item rather than something to fix silently here.

**Eleven concepts and seven notation entries entered `concept-ledger.json`**,
taking it to forty-two concepts against forty-two definition divs, and the
concept graph rebuilds to the same forty-two. Entering them surfaced two
collisions. *Neovisnost* is a property of events in chapter 7 and a property of
units in chapter 14, where it is called jedinica neovisnosti, and the ledger
carries the warning on both. And the Greek letters for the two error rates
collide twice over, since alpha is also the conventional symbol for the
reliability measure named in chapter 2 and beta without an index would collide
with the model coefficients of chapter 14. The book never writes the reliability
measure as a symbol and never writes a bare beta for a coefficient, and the
ledger now records both rules. That is the third and fourth such catch after
*pouzdanost* in round 2 and the standardized residual in round 4, which confirms
the round 4 suggestion that the collision check belongs in the per-chapter
procedure.

**The widget registry needed updating and would not have failed loudly.** The
*Što isprobati* lists for w10 and w11 changed in the chapters, and
`data/widgets.json` still carried the old text. Both are now back in step. The
registry is not checked against chapter prose by any script, so this is a manual
step and belongs in the per-chapter procedure below.

All three land under target, as every ported chapter so far has. Chapter 11 is
the shortest and the likeliest candidate for a later enrichment pass, with the
distinction between planning for power and planning for precision the natural
place to thicken.

### Round 6 — the summit and the capstone

**W13 → ch16.  Practical project → ch18.**

Chapter 16 is 6 000 words, the largest in the book, and week 13 supplies perhaps
two thirds of it. The missing third is structural — the reveal that chapters 14
and 15 were regression all along, prediction against explanation, the bridge to
chapter 17, and the causal seed from chapter 2 harvested. None of that exists in
a lecture on linear regression. Cook's distance and multicollinearity are
probably cuts.

Chapter 18 is a **transformation, not a port**. The practical project assumes
students write `.qmd` files with reproducible R and ggplot2; H10 says the reader
never writes code. What survives is the project's spine — its three scenarios,
its five assessment criteria (question, analysis, visualisation,
interpretation, reproducibility) and its stage sequence. Those become the
chapter's narrative. The rubric itself is better placed in Dodatak F and in the
`kolegij` profile, where it is still an assessment instrument.

## Per-round procedure

Unchanged for every job above.

1. **Name the shape and the register before writing.** Cut or expansion; which
   part of the ladder in struktura-knjige.md.
2. **Three-way split of the lecture.** Concept prose → *Izgradnja pojma*. The
   live demo → the widget, or a figure. One representative analysis → the
   *Razrađeni primjer* receipt at twelve lines with cosmetics evicted. R
   mechanics → Dodatak A. Everything else is cut.
3. **Write the five missing skeleton parts.** Vignette, divljina, both AI boxes,
   four exercise tiers. The *Računski* tier assumes no R installation.
4. **Record provenance in the chapter header** the way chapter 4 does. Navarro
   is the course's primary reference and open decision 5 tracks ShareAlike
   exposure. **Per-chapter at port time is far cheaper than an audit of
   eighteen chapters later.**
5. **Relabel every dataset as simulated**, following `R/podaci-nastavni.R`, and
   register it in Dodatak C. No course dataset is empirical.
6. **Widen the komunikologija framing** at least once per chapter.
7. **Check the concept ledger for a collision before writing**, both on the term
   and on the symbol. Four have been caught after the fact and none before it.
8. **Check that the chapter owns the concepts the plan assigns it**, since a
   later chapter may have taken one while the earlier one was still a skeleton.
   Round 5 found Cohen's d in chapter 14.
9. **Sync `data/widgets.json` with the chapter's own *Što isprobati* text.** No
   script compares the two.
10. Render, run both linters and the figure-introduction check, read it aloud.

## Bibliography debts

Not in `references.bib` and needed by the rounds above. Never add from memory.

| Needed for | Work | Status |
|---|---|---|
| ch2, round 1 | Stevens 1946, measurement levels | paid, `stevens1946` |
| Dio III approach, round 2 | Ismay & Kim, *ModernDive* — simulation-first inference, i.e. design principle 1 | paid, `ismay2019` |
| Dodatak A, round 1 | Wickham & Grolemund, *R for Data Science* | paid, `wickham2023` |
| ch8 divljina, round 2 | Squire 1988, why the 1936 *Literary Digest* poll failed | paid, `squire1988` |
| ch9 divljina, round 2 | Hoekstra et al. 2014, misinterpretation of confidence intervals | paid, `hoekstra2014` |
| ch5, already outstanding | Cleveland & McGill, graphical perception | paid, `cleveland1984` |
| ch5, already outstanding | Wilkinson, *The Grammar of Graphics* | paid, `wilkinson2005` |
| ch6 divljina, round 3 | Matejka & Fitzmaurice 2017, identical statistics from very different data | paid, `matejka2017` |
| ch13 divljina, round 4 | Cochran 1954, where the expected-count-of-five convention comes from | paid, `cochran1954` |
| ch14 divljina, round 4 | Belia et al. 2005, researchers misreading error bars and CI overlap | paid, `belia2005` |
| ch15 divljina, round 4 | Nieuwenhuis et al. 2011, comparing effects by their significance | paid, `nieuwenhuis2011` |
| ch7 vinjeta, round 5 | Gilovich, Vallone & Tversky 1985, the hot hand as a misperception of random sequences | paid, `gilovich1985` |
| ch7 divljina, round 5 | Miller & Sanjurjo 2018, the streak selection bias that reverses the canonical finding | paid, `miller2018` |
| ch10 divljina, round 5 | Greenland et al. 2016, twenty-five misinterpretations of p-values, intervals and power | paid, `greenland2016` |
| ch11 divljina, round 5 | Button et al. 2013, low average power and what it does to published effects | paid, `button2013`, cited only for what its abstract states |

## Not available, scheduled later

No lecture source exists for any of these, and none is a port.

- **ch3 Kako brojke zavode** — the book's public face
- **ch12 Kriza i obnova** — the replication crisis
- **ch17 Doba algoritama**
- **Predgovor** — drafted, not ported
- **Dodatak B** jamovi, **C** katalog, **D** koji test, **E** rječnik, **F**
  protokol
- **17 divljina boxes** minus the two round 2 sourced independently
  (`squire1988`, `hoekstra2014`), minus the two round 3 sourced independently
  (`cleveland1984`, `matejka2017`), minus the three round 4 sourced
  independently (`cochran1954`, `belia2005`, `nieuwenhuis2011`), and minus the
  three round 5 sourced independently (`miller2018`, `greenland2016`,
  `button2013`). The Berkeley case week 1 supplies now carries chapter 13's
  vignette rather than its divljina, so it no longer counts against this list.
  Ten remain, and all of them belong to chapters with no lecture source.

Note that all three chapters carrying the book's contemporary identity are in
this list. The port delivers the spine and none of the identity, so the port
wave will feel like progress while leaving the hardest writing untouched. Plan
the calendar accordingly.
