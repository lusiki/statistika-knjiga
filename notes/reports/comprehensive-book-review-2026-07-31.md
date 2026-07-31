# Comprehensive review of *Osnove statistike za društvene znanosti*

**Review date:** 31 July 2026  
**Primary object reviewed:** the deployed HTML book at
[lusiki.github.io/statistika-knjiga](https://lusiki.github.io/statistika-knjiga/),
the downloadable PDF, and the corresponding source tree at commit
`ad9caec84c40ec60d769233bd68649f19fbffa93`  
**Author shown by the book:** Luka Šikić  
**Review mode:** read-only Bookwright review; no chapter prose, ledger, registry,
data, figure, or build file was changed  
**Overall status:** **substantial draft; not ready for final or publication
status**

## 1. How to read this report

The report uses four evidence labels:

- **[Text]** describes what the manuscript, source, metadata, or build system
  explicitly contains.
- **[Inference]** is a direct conclusion from those materials.
- **[External benchmark]** compares the book with an authoritative source or
  accepted practice.
- **[Assessment]** is the review panel's editorial or technical judgment.

Severity is ranked before frequency:

- **Blocker** — a load-bearing correctness, publication, or reproducibility
  problem that should be fixed before the book is presented as complete.
- **Major** — materially weakens a core promise, chapter, pathway, or
  interpretation.
- **Moderate** — important but locally repairable.
- **Minor** — polish, rhythm, or local consistency issue.

All judgments about final definition coverage remain **provisional** because
every chapter spine in Bookwright is currently unratified.

## 2. Source and edition verification

### What the book currently is

**[Text]** The canonical title is *Osnove statistike za društvene znanosti*,
with the subtitle *Udžbenik za studente koji moraju razumjeti istraživanje*.
The author field names Luka Šikić. The project has no publisher statement,
edition number, ISBN, or fixed print pagination. It is therefore best described
as a self-published, continuously deployed Quarto draft rather than a formally
issued edition.

**[Text]** The primary online version reviewed here was successfully rebuilt
and deployed by GitHub Actions from commit
`ad9caec84c40ec60d769233bd68649f19fbffa93`. The landing page, flagship
chapters, references page, and PDF all returned HTTP 200 after deployment. The
current [PDF](https://lusiki.github.io/statistika-knjiga/pdf/Statistika.pdf) is
served from the same deployment.

**[Assessment]** The online book is the correct primary source because it is
the current public delivery format and contains the interactive widgets. The
source files remain the more reliable object for exact structural, code,
citation, and provenance checks. Since the book has no stable edition or page
numbers, future scholarly review should cite the commit and chapter section,
not only the mutable URL.

### Scope actually reviewed

The review covered:

- the preface and all 18 numbered chapters in canonical order;
- appendices A–F;
- the chapter blueprint, editorial rules, enrichment rules, and design rules;
- the Bookwright chapter ledger, chapter spines, concept ledger, and shared
  conventions;
- data generators, data catalogue, bibliography, widget registry, and build
  workflow;
- the current deployed HTML and PDF;
- eight independent Bookwright perspectives: statistical methods,
  skepticism, pedagogy, evidence, Croatian manuscript style, structure,
  whole-book voice, and narrative arc.

### External comparison set

The review did not treat external sources as a substitute for reading the
manuscript. They were used to test high-stakes or contemporary claims and to
benchmark the teaching design:

- The [ASA statement on p-values](https://doi.org/10.1080/00031305.2016.1154108)
  supports the book's resistance to threshold ritual, but not an unfair
  dismissal of every legitimate frequentist question.
- The Open Science Collaboration's
  [2015 replication project](https://doi.org/10.1126/science.aac4716) supports
  the need for Chapter 12 and the broad claim that reproducibility became a
  central problem, but the chapter still needs fuller evidence for reforms,
  incentives, and their limits.
- Cumming's
  [“new statistics” article](https://doi.org/10.1177/0956797613504966) supports
  the book's estimation-first orientation.
- The current
  [GAISE College Report](https://amstat.quarto.pub/college-gaise/index.html)
  supports conceptual understanding, real data, technology, active learning,
  and multivariable thinking. Against that benchmark, this book is especially
  strong on simulation and interactivity but currently too dependent on
  simulated rather than empirical social-science data.
- Chouldechova's
  [fairness analysis](https://pubmed.ncbi.nlm.nih.gov/28632438/) and
  Barocas, Hardt, and Narayanan's
  [*Fairness and Machine Learning*](https://fairmlbook.org/) support the
  conflict-among-metrics discussion in Chapter 17. They also make the chapter's
  unexamined “ground truth” or outcome label more consequential.
- The W3C technique on
  [using color and pattern](https://www.w3.org/WAI/WCAG22/Techniques/general/G111.html)
  supports the project's black-and-white-first and redundant-encoding design
  principles.

## 3. Executive overview

### Short assessment

*Osnove statistike za društvene znanosti* already has a stronger pedagogical
architecture and technical production system than many completed introductory
texts. Its best sequence—probability, sampling, estimation, testing, effect
size, and power—turns repeated simulation into a cumulative model of
statistical inference. Chapter 8 is a genuine hinge, Chapter 16 a convincing
summit, and Chapter 18 a credible capstone. The book's voice is largely unified,
its widgets are structurally well integrated, its generated data are seeded,
and its insistence on estimates, uncertainty, design limits, and responsible AI
use is distinctive.

The manuscript is nevertheless not close to publication-ready in content
terms. Its chapter prose totals about 43,507 words against an explicit
approximately 86,000-word blueprint, or roughly 51%. More importantly, the
three chapters intended to define the book's contemporary identity—3, 12, and
17—stand at only 11–14% of their planned lengths. Their skeletons, widgets,
callouts, and exercises are present, so the book looks mechanically complete
while the central arguments remain outline-thin.

Two statistical errors are publication blockers: Chapter 10 presents raw-label
permutation as a test of equal means without the necessary exchangeability
qualification, and Chapter 14 says default Welch's `t.test()` is inferentially
identical to ordinary homoskedastic `lm`, which is false outside special cases.
The empirical evidence layer is also incomplete: most sustained analyses use
simulated populations; the promised ESS/DZS/Eurostat layer is absent; several
contemporary AI, open-science, privacy, and fairness claims lack primary
support; and data licences are unfinished.

### Readiness verdict

| Dimension | Current state | Readiness |
|---|---|---|
| Statistical correctness | Strong concepts, two load-bearing errors, several major qualifications needed | **Blocked** |
| Pedagogical architecture | Excellent central sequence; incomplete beginner pathways and flagship chapters | **Major revision** |
| Writing and voice | One convincing authorial voice; thin chapters read like briefing notes | **Major revision** |
| Evidence and citations | No fabricated keys found; claim-level support and metadata incomplete | **Major revision** |
| Data consistency | Seeded simulations are coherent; catalogue and empirical layer incomplete | **Major revision** |
| Figures and widgets | Strong system, all 17 twins present; one intro gap; no reproducible browser audit | **Good with repairs** |
| Transitions and flow | Strong within the main methods arc; weak at 3→4, 12→13, and 17→18 | **Moderate revision** |
| Build and deployment | Current HTML/PDF deploy successfully; dependency and CI governance gaps remain | **Operational, not fully reproducible** |
| Publication/legal | No formal edition; unresolved licence warning and data licences | **Blocked** |

The recommended decision is **retain the architecture, deepen and correct the
manuscript**. A wholesale reorganization would discard one of the project's
greatest strengths without solving its actual problems.

## 4. Technical state of the book

### Deterministic audit results

| Check | Result | Interpretation |
|---|---|---|
| Chapter structure scan | All chapters have required callouts and four exercise tiers; chapters 1–17 have widgets/twins | Skeleton compliance is high |
| Widget contract check | 17/17 pass | HTML interaction, static twin, and registry are present |
| Rendered HTML check | 36 canonical pages pass freshness/completeness checks | Current public HTML is structurally deployable |
| Design token synchronization | Pass | Design sources agree mechanically |
| Croatian deterministic style lint | 0 candidates across chapters and appendices | No known hard-rule violations; manual style findings still matter |
| Figure-introduction detector | One failure, Chapter 5 `fig-anscombe` | Add a prose reading cue immediately before the figure |
| Concept graph build | 46 concepts represented | Generator works, but final selection is not ratified |
| Citation key resolution | 36 cited keys, all resolve; 37 bibliography entries | No missing or invented key detected; one uncited item is forced into references |
| Browser-level visual audit | Could not start because `playwright` is undeclared/uninstalled | Visual runtime audit is not reproducible from the repository |
| Current CI deployment | Success for HTML, PDF, Pages | Operational status is green, but green does not cover editorial correctness |

### Build and dependency risks

1. **[Text]** There is no `renv.lock`. CI pins an R release but installs current
   package versions when it runs. **[Assessment: Major]** A future package
   release can change numerical or rendering output without a source change.

2. **[Text]** The workflow invokes `quarto render --profile pdf`, while the
   project operating manual explicitly forbids that command because Quarto
   merges appendices additively. The approved PowerShell wrapper is not used.
   **[Assessment: Blocker for release engineering]** A successful job does not
   prove the PDF was assembled by the project's declared safe path.

3. **[Text]** PDF rendering is configured as non-blocking, and a failed PDF
   build can leave an older download in place. **[Assessment: Major]** The site
   may present HTML and PDF from different source states while the deployment
   remains green.

4. **[Text]** Token checking is non-blocking, and CI does not run the
   Bookwright style, structure, figure-introduction, citation-policy, or
   concept-consistency checks. **[Inference]** The production pipeline verifies
   file construction more thoroughly than manuscript integrity.

5. **[Text]** The browser audit requires Playwright, but the repository has no
   package manifest declaring it. **[Assessment: Moderate]** Add a pinned
   JavaScript toolchain or remove the unactionable audit command from the
   release checklist.

### Metadata and publication hygiene

- The README still describes the project as an empty skeleton even though it
  contains more than 43,000 words of chapter prose and 17 widgets.
- `_quarto.yml` still contains the temporary `nocite: @*` instruction. It
  causes the uncited `ioannidis2005` entry to appear and contradicts the comment
  that it should be removed after real citations exist.
- `references.bib` still describes itself as a seed bibliography. Ten cited
  journal articles lack DOI fields, and one important local item lacks a stable
  URL/version.
- The repository's MIT licence contains a warning that Navarro-derived
  material may require a ShareAlike licence. This is unresolved and should be
  treated as a publication blocker, not a future copy-edit.
- The chapter ledger marks all 19 chapter units as `draft`. All recorded
  renders succeed, but all chapter spines remain `ratified: false`.

## 5. Complete content and progress map

The word counts below measure chapter prose, excluding code and widget
implementation. The target is taken from the book blueprint.

| Ch. | Title | Words | Target | Approx. completion | Structural role |
|---:|---|---:|---:|---:|---|
| 00 | Predgovor | 564 | 1,500 | 38% | Reader contract and route map |
| 01 | Zašto statistika | 3,623 | 4,500 | 80% | Comparison, context, Simpson's paradox |
| 02 | Mjerenje i dizajn | 4,184 | 5,500 | 76% | Measurement, design, confounding |
| 03 | Kako brojke zavode | 537 | 5,000 | 11% | Critical-literacy identity pillar |
| 04 | Sažimanje podataka | 2,230 | 5,000 | 45% | Distribution and numerical summaries |
| 05 | Vizualizacija | 3,040 | 4,500 | 68% | Graphs as arguments |
| 06 | Povezanost | 2,706 | 4,000 | 68% | Association, form, aggregation |
| 07 | Vjerojatnost | 2,591 | 4,500 | 58% | Repeated randomness and conditionality |
| 08 | Uzorkovanje | 3,042 | 4,500 | 68% | Sampling distribution and standard error |
| 09 | Procjena | 2,397 | 4,000 | 60% | Intervals and bootstrap |
| 10 | Logika testiranja | 2,260 | 4,500 | 50% | Null-world reasoning and p-values |
| 11 | Veličina učinka i snaga | 2,024 | 4,000 | 51% | Magnitude, precision, planning |
| 12 | Kriza i obnova | 681 | 5,000 | 14% | Open-science identity pillar |
| 13 | Kategorički podaci | 2,494 | 4,500 | 55% | Categorical association |
| 14 | Dvije grupe | 2,196 | 4,500 | 49% | Binary predictor and group comparison |
| 15 | Više grupa | 2,069 | 4,000 | 52% | Omnibus comparison and multiplicity |
| 16 | Regresija | 3,568 | 6,000 | 59% | Model-family summit |
| 17 | Statistika u doba algoritama | 697 | 5,500 | 13% | Algorithmic-literacy identity pillar |
| 18 | Vaše prvo istraživanje | 2,604 | 5,000 | 52% | Extended capstone |
|  | **Total** | **43,507** | **86,000** | **51%** |  |

**[Assessment]** Completion is not uniformly distributed. Chapters 1–2 and the
middle teaching sequence contain developed prose; the three identity pillars
contain the largest absolute and conceptual deficits. This matters more than a
simple 51% figure because those chapters are the book's stated answer to “why
this textbook rather than another introductory statistics book?”

## 6. Structural architecture and dependency graph

```text
00 reader contract
 │
 ├─ Part I: statistical thinking
 │  01 comparison and context
 │   → 02 measurement, design, confounding
 │   → 03 skeptical claim audit [identity pillar; currently thin]
 │
 ├─ Part II: describing data
 │  04 distributions and summaries
 │   → 05 graphs as claims
 │   → 06 association, shape, subgroups
 │
 ├─ Part III: sample to population
 │  07 repeated randomness
 │   → 08 sampling distributions and SE [hinge]
 │   → 09 estimates, intervals, bootstrap
 │
 ├─ Part IV: inference
 │  10 null-world testing
 │   → 11 effect size, precision, power
 │   → 12 incentives, replication, reform [identity pillar; currently thin]
 │
 ├─ Part V: models
 │  13 categorical branch
 │  14 binary predictor
 │   → 15 several groups
 │   → 16 simple/multiple regression [summit]
 │   → 17 deployed prediction, fairness, LLMs [identity pillar; currently thin]
 │
 └─ 18 complete research workflow
    design → description → graph → model → uncertainty → audit trail → AI protocol
```

### Strongest cumulative paths

1. **Causality:** Chapter 1's aggregate warning → Chapter 2's design and
   confounding → Chapter 6's subgroup reversal → Chapter 14's group imbalance →
   Chapter 16's adjusted association and causal limits → Chapter 18's applied
   interpretation.

2. **Inference:** Chapter 7's repeated randomness → Chapter 8's sampling
   distribution → Chapter 9's interval → Chapter 10's null world → Chapter
   11's magnitude and power. This is the most successful part of the book.

3. **Unified models:** Chapter 14's binary predictor → Chapter 15's categorical
   predictor → Chapter 16's regression synthesis. The sequence successfully
   reduces method-list fragmentation.

4. **Critical/AI identity:** Preface promise → Chapter 3 claim audit → Chapter
   12 research-system audit → Chapter 17 algorithm audit → Chapter 18
   collaborator protocol. The intended path is excellent, but the three middle
   nodes are too thin and Chapter 18 barely harvests Chapter 17.

### Weak transitions

- **3→4:** The book moves from media skepticism to describing one's own data
  without explicitly stating that honest production is the answer to dishonest
  or careless presentation.
- **12→13:** The research-system crisis ends without a contract for how the next
  methods will embody reformed practice. Chapter 13 consequently feels like a
  procedural restart.
- **17→18:** Chapter 17 develops out-of-sample prediction, thresholds, error
  allocation, and fairness; Chapter 18 returns mainly to Chapters 2, 6, and 16.
  The algorithmic thread is left open.

## 7. Chapter connection matrix

| Ch. | Main incoming dependency | Main outgoing payoff | Connection judgment |
|---:|---|---|---|
| 00 | None | Four promises and route map | Strong promise; too manifest-like |
| 01 | Preface | 02, 06, 13 | Excellent opening engine |
| 02 | 01 | 06, 14, 16, 18 | One of the strongest seeds |
| 03 | 01–02 | Critical reading across 4–18 | Correct position, inadequate weight |
| 04 | 01–03 | 05–09 | Clean new-part entry |
| 05 | 04 | 06 and graph-first habit in 18 | Strong continuation |
| 06 | 04–05 plus 01–02 | 14, 16, 18 | Strong Part II climax |
| 07 | 04 | 08, 10, 17 | Purposeful, somewhat overloaded |
| 08 | 04 and 07 | 09–11 and all later inference | Exceptional hinge |
| 09 | 08 | 10–18 | Excellent handoff |
| 10 | 07–09 | 11–15 | Strong sequence; method correction needed |
| 11 | 09–10 | 12, 14–15, 18 | Strong conceptual bridge |
| 12 | 03, 10–11 | Reformed practice in 13–18 | Right location, outline-thin |
| 13 | 04, 08, 10 | Categorical branch and 17 denominators | Useful branch, weak Part V opening |
| 14 | 09–11 | 15–16 | Strong seed; inference contradiction |
| 15 | 10, 12, 14 | 16 | Excellent ascent |
| 16 | 02, 06, 14–15 | 17 and 18 | Convincing summit |
| 17 | 07, 13, 16 | Responsible prediction in 18 | Strong premise, weak payoff |
| 18 | Whole book in practice | Reproducible first study | Strong capstone, incomplete closure |

## 8. Chapter-by-chapter content review

### 00 — Predgovor

**Strength.** The reader contract is unusually clear: understand research,
inspect computation, keep judgment, and do not mistake delegated calculation
for delegated responsibility.

**Problem.** The “worked example” describes the seven-part template instead of
working through a statistical claim. The prose consequently reads as an
institutional manifesto, and the first computational exercise sends a novice
forward to Chapter 4. The claim that code is “evidence” should be narrowed to
“a checkable trace of calculation”; code does not validate data, design, or
interpretation.

**Priority:** Moderate.

### 01 — Zašto statistika

**Strength.** Berkeley and Simpson's paradox give the book a strong opening
engine. Context, denominator, comparison, and unit of analysis are introduced
as matters of judgment rather than arithmetic.

**Problem.** Some foundational terms enter without a stable definition
hierarchy, though this should be fixed only after spine ratification. Repeated
returns to Berkeley later in the book need to begin from what the prior reading
could not answer.

**Priority:** Minor/provisional.

### 02 — Mjerenje i dizajn

**Strength.** This is one of the strongest substantive chapters. It makes
operationalization, reliability, validity, design, and confounding constraints
on every later calculation.

**Problems.**

- A confounder is defined too broadly by observed association with exposure and
  outcome. Mediators and colliders can satisfy that description but require
  different treatment.
- Random assignment is described too nearly as actual group equality and a
  single remaining explanation. It should say “in expectation” and name
  adherence, spillover, attrition, and measurement conditions.
- A negative item–total relation is said to be “almost always” forgotten
  reverse coding. That is only a first diagnostic; multidimensionality,
  translation, wording, and inattentive response remain possible.
- The traditional Stevens measurement levels are presented too much like a
  complete current rule rather than a historically influential convention with
  limitations.

**Priority:** Major.

### 03 — Kako brojke zavode

**Strength.** Source, denominator, comparison, and uncertainty form a memorable
audit card. The widget clearly separates bias from precision.

**Problem.** At 537 prose words, this is not yet the promised public face of the
book. Misleading axes, base-rate neglect, cherry-picking, poll interpretation,
synthetic media, and AI provenance are absent or only named. Four consecutive
“first/second/third/fourth check” paragraphs sound like slides rather than a
developed argument. The chapter also relies on margin-of-error reasoning before
Chapters 8–10 explain it, without clearly marking that conceptual debt.

The computational exercise asks students to modify `sim_ankete`, violating the
book's rule that assessed work assumes neither R nor code production. The
worked-example code is hidden and 13 idea-lines long rather than a visible
receipt of at most 12 lines.

**Priority:** Major; first content-development priority.

### 04 — Sažimanje podataka

**Strength.** Distribution, center, spread, robust summaries, transformation,
and standardization are tied to interpretive loss rather than presented as a
list of formulas. The visible code receipt is concise and pedagogically useful.

**Problems.** The chapter is dense for the first quantitative chapter, and it
contains six canonical definition blocks, one above the current Bookwright
band. A claim that engagement metrics “regularly” have a certain shape needs a
source or should be stated as a property of the simulation. Some widget-based
assessed work lacks enough static information for print-only students.

**Priority:** Moderate.

### 05 — Vizualizacija

**Strength.** The chapter's central proposition—that a graph is an argument
made of checkable choices—is excellent. Anscombe, perceptual encoding, omitted
content, and the limits of blanket chart rules form a mature visual-literacy
chapter.

**Problem.** `fig-anscombe` lacks an immediate prose introduction because code
intervenes between the reading cue and the figure. This is the only failure
found by the deterministic figure-introduction detector. The fix is a single
sentence naming the cross-panel comparison and its importance.

**Priority:** Minor.

### 06 — Povezanost

**Strength.** Shape, Pearson and Spearman coefficients, range restriction,
subgroups, ecological inference, and causal caution form a coherent spiral
from Chapters 1, 2, 4, and 5.

**Problems.** Agreement between Pearson and Spearman does not establish
linearity, and disagreement does not uniquely identify curvature. Range
restriction often attenuates correlation under familiar conditions, but can
also increase or reverse it under nonlinearity or selection. The scatterplot
must remain the diagnostic, with coefficient comparison only a clue.

**Priority:** Major but local.

### 07 — Vjerojatnost

**Strength.** Probability is experienced as repeated behavior before being
named. The hot-hand dispute is presented with both the original result and its
later correction, which is exemplary evidence practice.

**Problems.** The chapter carries high intrinsic load: long-run probability,
conditionality, independence, binomial reasoning, normality, QQ plots, and
selection effects. The elementary CLT account needs independence or weak
dependence and finite-variance conditions. A planned degree-of-belief
interpretation is barely developed.

**Priority:** Moderate.

### 08 — Uzorkovanje

**Strength.** This is the book's strongest chapter. It changes the unit of
attention from people to estimates, distinguishes SD from SE, builds the
sampling distribution through simulation, and shows why larger biased samples
do not fix selection.

**Problems.** The simple \(\sigma/\sqrt{n}\) logic is attached to a definition
of probability sampling broad enough to include unequal probabilities,
clustering, and sampling without replacement. Weights, design effects,
effective sample size, and finite-population correction need a compact
qualification. The claim that a survey of about a thousand people describes a
city and a country “equally well” holds only within the simplified
simple-random-sample comparison.

**Priority:** Major qualification, no structural rewrite.

### 09 — Procjena

**Strength.** The interval catcher correctly moves confidence from the
probability of a fixed parameter to the long-run success of a procedure. The
bootstrap is motivated as a resampling solution rather than announced as a
magic method.

**Problems.**

- Mean ± 1.96 SD is not a general 95% prediction interval; here it is at most a
  normal-rule descriptive range.
- The chapter's prior coverage experiment validates a z interval for a mean,
  not a percentile-bootstrap interval for a median. Capturing the median once
  does not validate the procedure.
- The bootstrap is described too nearly as assumption-free. Exchangeability,
  representation by the empirical distribution, and known failure cases must
  be named.
- The model-revision exercise drops the code-reading progression established
  by the book.

**Priority:** Major.

### 10 — Logika testiranja

**Strength.** The null world is built through simulation before the p-value is
named. The chapter is especially good at distinguishing
\(P(\text{data}\mid H_0)\) from \(P(H_0\mid\text{data})\) and at resisting a
single threshold as a conclusion.

**Blocker.** Raw group-label permutation is presented as a test of equality of
means with no shape assumption. It is exact under exchangeability or a sharp
no-association/full-distribution null, not merely equal means. Unequal shapes
or variances can preserve equal means while invalidating that reference
distribution. The observational labels were not randomized.

The chapter should either:

1. define and defend the full-distribution/exchangeability null; or
2. target mean equality with Welch inference or a studentized permutation
   statistic.

The Monte Carlo p-value should use the standard correction
\((b+1)/(B+1)\).

The short Bayesian contrast is useful, but its rhetoric is asymmetric. It
should acknowledge legitimate long-run error-control questions, meaningful
point nulls, and Bayesian dependence on likelihood and model assumptions.

**Priority:** Blocker.

### 11 — Veličina učinka i snaga

**Strength.** The sequence estimate → interval → substantive importance →
prospective precision is exactly right for this audience. The simulation of
selected, underpowered studies makes winner's-curse logic visible.

**Problems.** The power calculations inherit Chapter 10's unqualified
permutation problem. The worked simulation also assumes independent normal
groups, an equal known SD, and a two-sided z cutoff while saying that it adds
nothing new. A particular simulated exaggeration factor is generalized too
far, and the advice not to “trust” an effect size from an underpowered field is
stronger than its cited support. The worked example appears before the wild
statistics and AI blocks, breaking the stable chapter contract.

**Priority:** Major.

### 12 — Kriza i obnova

**Strength.** The chapter refuses a morality play. It correctly distinguishes
deliberate p-hacking, garden-of-forking-paths flexibility, publication systems,
replication, and reforms that improve process without guaranteeing truth.

**Problem.** At 681 words, it is an outline of a flagship chapter. It does not
develop the lifecycle connecting selective analysis, incentives, publication,
replication, preregistration, registered reports, open materials, privacy
tradeoffs, and the risk that reform itself becomes ritual. Many contemporary
claims lack primary sources.

The computational exercise asks students to rerun `sim_putovi`; the
worked-example code is hidden and exceeds the visible-receipt ceiling. The
suspect and revision tasks do not sustain the planned code-reading ladder.
There is no effective transition into Part V.

**Priority:** Major; second content-development priority.

### 13 — Kategorički podaci

**Strength.** Expected counts, observed deviations, reference distributions,
effect size, and sparse cells are introduced through denominator discipline.
The text openly treats category construction and reference distributions as
research decisions.

**Problems.** `(O-E)/sqrt(E)` and `chisq.test$residuals` are Pearson residuals,
not adjusted standardized residuals. Their variance is not generally one under
fixed margins, so a simple ±2 rule is not calibrated as stated. Use
`$stdres` or rename and interpret the Pearson residuals without z-like
thresholds. A sparse-null simulation evaluates type-I calibration, not power
under a relationship. The chapter also needs a stronger opening contract that
connects Part V to Chapter 12.

**Priority:** Major.

### 14 — Dvije grupe

**Strength.** Design precedes test choice, pairing is made memorable, estimates
and intervals lead, and the binary-predictor representation sets up the model
sequence.

**Blocker.** The worked example recommends Welch's test as the default and then
states that default `t.test()` and ordinary `lm` are identical. Their point
estimate is the same, but default Welch inference and homoskedastic OLS use
different standard errors and degrees of freedom and are not generally
inferentially identical.

Either compare `lm` with `t.test(..., var.equal = TRUE)` while explicitly
naming the equal-variance condition, or preserve Welch and use
heteroskedasticity-robust regression inference.

**Priority:** Blocker.

### 15 — Više grupa

**Strength.** Omnibus logic, within/between variation, multiplicity, planned
comparisons, and the relation to a common model form a clean ascent from
Chapter 14.

**Problems.** Informal variance-ratio screening is not sufficient to declare
ANOVA assumptions adequate. The suspect/revision artifact again lacks code
despite the book's code-reading ladder. The chapter partially spends Chapter
16's planned “these were regression all along” reveal, though this is a
narrative rather than correctness problem.

**Priority:** Moderate.

### 16 — Regresija

**Strength.** This is the book's conceptual summit. It unifies correlation,
two-group comparison, multi-group comparison, adjustment, residuals,
prediction, and causal limits while keeping coefficients conditional and
interpretations modest.

**Problems.**

- A hard-coded generator coefficient is treated as the truth for a rounded and
  truncated observed outcome, even though the finite-population OLS coefficient
  need not equal the latent generator value.
- Confidence intervals are interpreted as sampling uncertainty after fitting
  all 50,000 members of the declared finite population. The chapter must choose
  a finite-population, latent, or superpopulation estimand and demonstrate
  uncertainty consistently.
- Willingness to pay may be unavailable at prediction time and can therefore be
  target leakage. Prediction time must be explicit.
- The causal-adjustment conditions are too compressed. Total and direct effects
  require different adjustment choices, and positivity, consistency,
  interference/selection, time order, and functional specification matter.
- At roughly 32 minutes, the chapter needs a deliberate midpoint retrieval
  pause, even if its overall length is justified.

**Priority:** Major; preserve architecture.

### 17 — Statistika u doba algoritama

**Strength.** The chapter correctly carries prediction out of the model and
into institutional decisions. Its widget makes thresholds, base rates, and
unequal consequences inspectable. The language-model section returns to
provenance and verification rather than treating fluent output as evidence.

**Problems.** At 697 prose words, prediction/test splits, overfitting,
classification, infrastructure, feedback, fairness, and language models read
like a policy briefing rather than a chapter. The prerequisites omit Chapter
13 even though conditional denominators and confusion tables depend on it.
Technical claims about recommender systems, feedback loops, and LLMs lack
primary support.

Most seriously, the fairness example accepts a “true outcome” as clean ground
truth. In social systems, recorded recidivism, risk, success, or need may
reflect selective observation, policing, measurement, and institutional
history. The chapter begins its fairness analysis after the most important
normative decision has already been hidden. Rename it a recorded reference
outcome, state the idealization, and add label construction, selective labels,
procedural fairness, and appeal.

The computational exercise asks students to modify `sim_klasifikacija`. The
48-line worked-example block is hidden; it is plumbing, not a readable receipt.

**Priority:** Major; third content-development priority.

### 18 — Vaše prvo istraživanje

**Strength.** The extended example successfully integrates question, design,
immutable raw data, description, visualization, modeling, interval-first
reporting, confirmatory/exploratory distinction, reproducibility, privacy, and
AI disclosure. It is a persuasive finale.

**Problems.** The text first describes an adjusted interval around zero as
absence or disappearance of association, then correctly says that small
effects of either sign remain compatible. Keep only the latter logic. The
chapter's stated prerequisites understate its dependence on the whole book.
Its privacy rule is a defensible conservative policy for beginners, but should
be named as the book's policy rather than a universal technical/legal fact.
The finale should explicitly close all four promises and either use Chapter
17's prediction/fairness concepts or explain why this study remains
explanatory.

**Priority:** Major but bounded.

## 9. Appendices and alternative learning pathways

### Appendix A — R practicum

This is the most developed appendix. Its explanations of pipes, debugging,
clean sessions, missing values, and reproducible scripts are useful. However,
it says `library(tidyverse)` is the only prerequisite and then uses
`anketa_mreze` without a visible acquisition or creation step. A novice
following the appendix independently will fail at the first sustained dataset
example. Its “procedures from chapters” coverage also stops before most of the
inferential sequence.

**Required action:** add a visible, reproducible data-loading step and extend
the chapter-indexed bridge through Chapters 6–16.

### Appendix B — no-code/jamovi path

The principles are sensible, but the appendix is currently an orientation note,
not the promised parallel path. It does not map each book analysis to a
versioned menu route, required settings, expected output, export, and
verification.

**Required action:** either build the full companion or stop advertising the
no-code route as complete.

### Appendix C — data catalogue

The distinction between empirical and simulated data is transparent, and the
reason for known simulated populations is pedagogically sound. The catalogue
is nevertheless stale:

- `anketa_mreze` omits Chapter 18 and Appendix A from its usage list;
- `populacija_medija` omits Chapters 7, 10, 11, and 16;
- `UCBAdmissions` and `anscombe` lack complete licence, variable, version, and
  path records;
- the empirical ESS/DZS/Eurostat wave remains future work;
- the fetch registry is empty.

**Required action:** derive usage from source, complete licences and persistent
provenance, and add the empirical data layer.

### Appendix D — which test when

The text commendably starts with question and design, not software output. The
promised visual decision tree and quick formula/reference spread are absent.
The current tree also risks reducing analysis to variable type → named test;
estimand, missingness, weights, complex sampling, and generalization must
precede the procedure.

### Appendix E — glossary

The manually presented glossary contains 16 terms while the generated concept
ledger/graph contains 46. The file says it will be generated, but it is not
currently synchronized. Final repair must wait for spine ratification; until
then, the mismatch is a known incompleteness rather than evidence that the
chapter definitions themselves are wrong.

### Appendix F — AI protocol

The core rubric—privacy, traceability, reproduction, and disclosure—is strong.
It needs a copyable checklist/template, institutional and temporal context for
privacy claims, and a more nuanced account of levels of reproducibility. The
distinction between public, contractually protected, and locally approved tools
should be explicit.

## 10. Writing style, voice, rhythm, and transitions

### What already works

**[Assessment]** The book convincingly sounds like one Croatian author. Its
authority comes from limiting claims rather than issuing verdicts. Chapters 1,
4–11, and 13–16 are especially successful: concrete cases lead, formulas arrive
after intuition, and every technical result returns to an allowed
interpretation.

The style linter found no deterministic hard-rule candidates. This is evidence
that the editorial system works; it is not evidence that all prose is mature.
Manual review found:

- controlled use of metaphor;
- no patronizing mathematics register;
- a consistent authorial *mi*;
- disciplined uncertainty language;
- successful planned register shifts in Chapter 18 and Appendix A.

### Where the manuscript voice breaks

Chapters 3, 12, and 17 have many short, parallel, declarative paragraphs. They
name concepts but seldom develop a scene, mechanism, reversal, or
counterexample. Chapter 17 is the clearest drift: it reads like a competent
policy brief written by the book's author, not a fully developed chapter of the
same book.

The preface similarly reveals scaffolding. Its worked example tells the reader
that a vignette, widget, wild claim, and AI box will occur, instead of giving
the reader a miniature experience of the book's method.

### Repeated templates

Several local formulas become visible across 19 chapters:

- “The next display…” introduces widgets in seven technical chapters.
- “The task is…” or “The whole analysis…” repeatedly opens worked examples.
- AI boxes often use “We check three things. First… Second… Third…”.
- “Not X but Y” is an effective authorial signature but becomes mannered in
  concentrated passages.

These are not hard-rule violations. The fix is syntactic and argumentative
variation inside the fixed skeleton, not abandoning the skeleton.

### Redundancy and recurring cases

Berkeley/Simpson is a useful spiral when each return asks a new question.
Anscombe similarly develops from summaries to graphs to association. The ASA
p-value episode is less well distributed: it appears in the preface, Chapter
3, and Chapter 10, diluting Chapter 3 while Chapter 10 has the strongest claim
to it.

**Recommendation:** keep recurring motifs, but make every recurrence begin
with the question the previous appearance could not answer. Give Chapter 3 its
own public claim, poll, or manipulated graphic.

## 11. Figures, graphs, widgets, and accessibility

### Strong system-level findings

- All 17 interactive chapters contain an HTML widget and a registered static
  print twin.
- The design token audit passes.
- Figures generally have informative captions and alt text.
- Widgets usually state what the reader changes, what to watch, and why the
  change matters.
- The palette and print strategy are aligned with non-color-dependent
  interpretation.

### Main graph issues

1. **Immediate introduction:** Chapter 5's Anscombe figure needs a prose cue
   directly before it.

2. **Conceptual balance:** Chapter 5 contains six conceptual figures while most
   chapters contain one to three. That density is defensible for a visualization
   chapter, but the final sequence should be checked for redundancy once prose
   is complete.

3. **Widget domination:** Chapter 17's largest section is about 3.1 times the
   size of its smallest substantive section, largely because the widget and
   worked machinery carry more weight than the prose. The visual is currently
   substituting for an argument it should demonstrate.

4. **Print-equivalent assessment:** Several computational exercises require
   changing widget states without giving print readers the necessary preset
   tables or static alternatives. Chapters 4, 9, and 11 are clear examples.

5. **Runtime visual assurance:** Source contracts and static rendering pass,
   but the intended browser-level audit cannot run from a clean repository
   because Playwright is undeclared. Responsive layout, keyboard behavior, live
   regions, and dark-mode regressions therefore lack a reproducible release
   check.

6. **Fairness visualization:** Chapter 17 should label the outcome as recorded
   reference data rather than unqualified truth, and the visual explanation
   should expose how changing the label-generating process could alter every
   fairness rate.

## 12. Data, notation, and internal consistency

### What is consistent

- `anketa_mreze` and `populacija_medija` are created by deterministic seeded
  generators.
- The generator restores random-number state, and the common setup fixes a
  book-wide seed for stable figures.
- Simulated datasets are usually labeled as simulated before numerical claims.
- Croatian decimal formatting and shared visual scales are centralized.
- Citation keys used in the text all resolve.
- The concept ledger contains a coherent set of 46 entries and the generated
  graph matches that count.

### What is inconsistent or incomplete

1. **Data catalogue versus use:** usage rows omit multiple actual consumers, as
   described in Appendix C above.

2. **Glossary versus concept registry:** 16 displayed terms versus 46 registered
   concepts.

3. **Code policy versus chapters:** H10 requires visible receipts in every
   worked example, no more than 12 idea-lines, and no student code production.
   Chapters 1, 2, 3, 12, and 17 have hidden worked-example code. Their first
   worked chunks contain approximately 23, 44, 13, 14, and 48 idea-lines,
   respectively. Chapters 3, 12, and 17 explicitly ask students to manipulate
   R objects.

4. **Code-reading ladder:** several later `callout-greska` and model-revision
   tasks contain no suspect code, so the progression disappears as inference
   becomes harder.

5. **Chapter contract:** Chapter 11 places the worked example before wild
   statistics and AI sections, unlike the fixed sequence.

6. **Definitions:** Chapter 4 has six definition blocks against a current
   maximum band of five, while Chapters 1, 3, 12, 17, and 18 have none. Because
   spines are unratified, the correct remedy is first to decide which concepts
   genuinely carry later reasoning.

7. **Current-product claims:** jamovi behavior, public-model privacy, and AI
   product behavior are not versioned or dated.

## 13. Evidence and factual integrity

### Positive result

No fabricated citation key or demonstrably fabricated empirical number was
found. All 36 distinct cited keys resolve to bibliography entries. The
manuscript is particularly careful when presenting Berkeley, *Literary
Digest*, confidence-interval misconceptions, independent-observations errors,
the hot-hand debate, and the conflict among fairness measures.

### Main evidence problems

1. **Claim-level H7 anchoring.** The book often cites the first sentence about a
   study and leaves a numerical result or related empirical claim in the next
   sentence without its own citation. This violates the project's stricter rule
   that every number, study, or named finding carry a citation in the same
   sentence.

2. **Unsupported contemporary claims.** Chapters 12 and 17, Chapter 18's
   privacy material, and Appendix F make claims about publication bias,
   preregistration, registered reports, paper mills, recommender systems,
   feedback loops, LLM mechanisms, reidentification, and public AI services
   without sufficient primary or official sources.

3. **Overclaiming from sources.** Chapter 11 turns evidence about low power and
   exaggerated published estimates into blanket distrust. Chapter 2 turns a
   historical measurement taxonomy and one diagnostic pattern into near-rules.

4. **Bibliographic metadata.** DOI/URL verification is incomplete and
   `nocite: @*` masks the difference between used and unused evidence.

5. **Data licences and provenance.** The empirical datasets bundled through R
   need source version, persistent URL, variables, licence, and redistribution
   status. Generated data also need an explicit licence rather than “not
   applicable”.

### Interpretation

**[Assessment]** The book has a culture of evidence but not yet a closed
evidence system. Its local safeguards have prevented obvious fabrication; they
have not yet guaranteed sentence-level support, current technical sourcing, or
publication-ready data provenance.

## 14. Panel synthesis: agreement, disagreement, and scores

### Critic scores

| Perspective | Scores | Summary |
|---|---|---|
| Statistical methods | correctness 2/5; assumptions 2/5; interpretation 3/5; precision 2/5 | Two blockers and several major assumption/estimand issues |
| Skepticism | contestation 4/5; fairness to other views 3/5; normative honesty 4/5 | Strong boundaries; weak NHST/Bayes balance and ground-truth critique |
| Pedagogy | clarity 4/5; scaffolding 3/5; prerequisites 3/5; exercises 3/5 | Excellent inference sequence; beginner pathways incomplete |
| Evidence | citation integrity 3/5; claim support 2/5 | No fabrication found; contemporary support and licences incomplete |
| Manuscript style | manuscript feel 3/5; rhythm 3/5; restraint 4/5 | Mature core, outline-like flagship prose |
| Structure | vignette 4/5; definitions 2/5 provisional; figure intros 4/5; exercises 4/5 | Strong skeleton and architecture; content weight uneven |
| Whole-book voice | consistency 4/5; register evenness 3/5 | One authorial voice, with briefing-register drift |
| Narrative arc | cumulative build 4/5; sequencing 4/5; non-redundancy 3/5 | Keep macro-order; repair three transitions and pillars |

### Strong agreement

All relevant critics agree that:

- the macro-order should be preserved;
- Chapter 8 is the pedagogical hinge;
- Chapter 16 is the conceptual summit;
- Chapter 18 is substantially successful;
- Chapters 3, 12, and 17 are structurally present but substantively
  underdeveloped;
- the simulation-first design is a major strength;
- simulation must be paired with more real social-science data;
- Chapter 17 must question the construction of its reference outcome;
- appendices A/B/D do not yet provide the promised reproduction routes;
- unratified chapter spines prevent a final claim of conceptual completeness.

### Productive disagreements or tradeoffs

- **Simulation:** pedagogically excellent for revealing mechanisms, insufficient
  alone for empirical breadth. The answer is addition, not replacement.
- **Fixed skeleton:** helpful orientation for beginners, but it creates false
  completeness when prose is thin. Keep it and measure content weight
  separately.
- **Recurring cases:** useful for spiral learning, repetitive when a later
  appearance merely restates setup.
- **Strict privacy rule:** appropriate as a conservative course policy, not as
  an undated universal legal claim.
- **Estimation first:** a central strength, but it should not be defended by
  caricaturing legitimate frequentist aims.
- **Unified linear model:** conceptually powerful, but it cannot erase
  inferential distinctions such as Welch versus homoskedastic OLS.

## 15. Ranked master issue list

### Blockers

1. Correct Chapter 10's permutation-test null and assumptions.
2. Correct Chapter 14's Welch/OLS equivalence claim and implementation.
3. Resolve the licence warning for Navarro-derived material and complete data
   licences.
4. Ratify chapter spines before declaring the concept system final.
5. Make the release PDF use the project's approved render path and fail safely
   rather than silently retaining an old artifact.

### Major

6. Develop Chapters 3, 12, and 17 into full arguments, not expanded lists.
7. Add a verified empirical social-science data layer while retaining
   simulations for mechanism discovery.
8. Repair assumption and estimand language in Chapters 2, 6–9, 11, 13, 16, and
   18.
9. Add label construction, selective observation, procedural fairness, and
   appeal to Chapter 17.
10. Complete Appendix A's standalone data path and inferential coverage.
11. Build Appendix B as a true versioned no-code companion or narrow its claim.
12. Complete Appendix D's decision/recovery aids.
13. Restore the H10 code-reading ladder and remove code-production requirements
    from assessed chapter exercises.
14. Source contemporary open-science, AI, privacy, and algorithmic claims with
    primary or official materials.
15. Synchronize data catalogue, glossary, concept ledger, bibliography
    metadata, README, and actual source use.
16. Close the 12→13 and 17→18 narrative transitions.

### Moderate and minor

17. Add the missing Chapter 5 figure introduction.
18. Give Chapters 7 and 16 explicit midpoint retrieval pauses.
19. Vary recurring widget, worked-example, and AI-box opening formulas.
20. Reassign the ASA episode chiefly to Chapter 10 and give Chapter 3 its own
    public case.
21. Provide static preset data for widget-dependent print exercises.
22. Replace the preface's meta-example with a genuine miniature inquiry.

## 16. Recommended revision sequence

### Phase 1 — protect correctness and publication integrity

1. Fix Chapters 10 and 14.
2. Correct closely connected major method statements in 8, 9, 11, 13, 16, and
   18.
3. Resolve the project and dataset licences.
4. Pin R and browser-audit dependencies; make PDF production safe and
   fail-closed.
5. Remove `nocite: @*` and complete bibliography metadata verification.

### Phase 2 — ratify the book's intellectual spine

6. Ratify the chapter spines, especially the terms and aspects for 3, 12, and
   17.
7. Decide canonical definitions and regenerate the glossary/concept graph.
8. Make Chapter 18's prerequisites and closing promises reflect the actual
   dependency graph.

### Phase 3 — build the identity pillars

9. Expand Chapter 3 around one traceable public claim tested through an axis or
   denominator, a base-rate problem, and an AI-produced number.
10. Expand Chapter 12 around one research lifecycle: attractive finding →
    flexibility → selection/incentives → replication → reform → reform limits
    → student practice.
11. Expand Chapter 17 around one consequential decision: held-out prediction →
    threshold → confusion table → unequal error burdens → disputed label →
    feedback → language models as prediction systems.

### Phase 4 — fulfill the data and pathway promises

12. Introduce verified ESS/DZS/Eurostat or equivalent datasets in at least one
    final example per major part, with complete provenance.
13. Complete Appendix A and build Appendix B in parallel around the same
    questions, outputs, and verification checks.
14. Derive Appendix D from those two pathways.
15. Add print-completable alternatives to widget-dependent exercises.

### Phase 5 — whole-book editorial pass

16. Repair 3→4, 12→13, and 17→18 transitions.
17. Rebalance recurring cases and repetitive micro-templates.
18. Run the six-critic panel again on every substantively changed chapter.
19. Run whole-book continuity, figure, style, evidence, and deployment checks.
20. Only then consider moving ledger status from `draft` toward `final`.

## 17. Alternative structures

### Preferred structure — preserve the current order

This is the recommended option. Strengthen the three identity pillars and add
explicit part-boundary transitions. It preserves the successful hinge, summit,
and capstone.

### Alternative A — a visible two-track reading map

Keep the chapter order but add two routes in the preface:

- **Critical literacy route:** 1 → 2 → 3 → 5 → 8 → 10 → 12 → 17 → 18.
- **Analysis route:** 1 → 2 → 4 → 5 → 6 → 7 → 8 → 9 → 10 → 11 → 13–16 → 18,
  with A or B in parallel.

This solves navigation without restructuring the book.

### Alternative B — distributed identity chapters

If Chapters 3, 12, and 17 cannot be expanded to full weight, their material
could be distributed as recurring “critical checkpoints” across nearby
chapters. This would reduce the contrast between full method chapters and
briefing-like identity chapters, but it would weaken the book's explicit public
identity. It is therefore a fallback, not the preferred design.

### Structure not recommended

Do not reorder the book into a conventional catalogue of tests. That would
break the simulation-to-inference ascent and the model-family reveal while
doing nothing to solve the evidence, correctness, or data problems.

## 18. Final synthesis

**[Text]** The book is a 19-unit, five-part-plus-finale Quarto textbook with 17
interactive/static widget pairs, a working HTML/PDF deployment, a deterministic
simulation layer, an estimation-first inferential sequence, AI literacy
throughout, and a structured editorial control system.

**[Inference]** The production system and chapter skeleton have advanced faster
than the manuscript's content and evidence layers. The book can therefore look
finished in navigation, callouts, widgets, and generated output while remaining
roughly half-length and carrying unresolved load-bearing claims.

**[Assessment]** Its strongest existing achievement is not any individual
widget or chapter. It is the cumulative idea that statistical judgment moves
from question and design, through description and repeated uncertainty, to a
modest claim whose computation, assumptions, and provenance remain
inspectable. Chapters 8, 16, and 18 prove that this idea can sustain a
distinctive, humane, technically serious textbook for non-specialists.

The next revision should not broaden the topic list. It should make the current
promises true. Correct the two procedural blockers. Decide and ratify the
concept spine. Give Chapters 3, 12, and 17 the narrative and evidential weight
the blueprint assigns them. Add real social-science data without sacrificing
the clarity of known simulations. Complete the R and no-code reproduction
paths. Then align the glossary, data catalogue, citations, licences, CI, and
public metadata with the manuscript that actually exists.

**Final verdict:** **a technically sophisticated and pedagogically promising
substantial draft with an excellent central spine, but not yet a trustworthy
final textbook.** The book should remain in `draft` status until the statistical
blockers, identity chapters, empirical data layer, evidence provenance,
reproduction pathways, and release governance are closed.

