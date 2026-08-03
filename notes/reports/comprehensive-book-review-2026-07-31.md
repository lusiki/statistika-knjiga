# Comprehensive review of *Osnove statistike za društvene znanosti*

**Review date:** 31 July 2026  
**Strategic integrations:** data, data science, text analysis, AI, and cross-book continuity;
assessment closure, published-research literacy, statistical communication,
implementation parity, and release governance (3 August 2026)

**Primary object reviewed:** the deployed HTML book at
[lusiki.github.io/statistika-knjiga](https://lusiki.github.io/statistika-knjiga/),
the downloadable PDF, and the corresponding source tree at commit
`ad9caec84c40ec60d769233bd68649f19fbffa93`  
**Author shown by the book:** Luka Šikić  
**Review mode:** read-only Bookwright review, subsequently supplemented with a
book-wide empirical-data strategy; no chapter prose, ledger, registry, data,
figure, or build file was changed

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

Two limits of the review are themselves findings rather than silent exclusions.
The teaching layer — `predavanja/`, `silabus.qmd`, `raspored.qmd`, and the
`kolegij` render profile — was not reviewed, and its relationship to the
assessment gap described in §12 should be settled when that gap is closed. More
importantly, the review contains no evidence from a single reader of the
intended audience, because none exists anywhere in the project. §14 treats that
absence as a recommendation.

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
support; and data licences are unfinished. This is not primarily a shortage of
files. The book lacks a governed portfolio in which a probability survey, an
administrative count, official aggregates, an expert-coded measure, a digital
trace, a volunteer sample, and a simulation teach visibly different kinds of
claims.

The contemporary-methods layer also has a substantive gap. Nearly all examples
treat data as an already rectangular table, while text—the material of much
political, communication, media, and AI research—is absent as a measurement
problem. Chapter 17 can close that gap without becoming an NLP manual if it uses
one Croatian-language corpus to connect corpus construction, coding,
validation, and algorithmic classification. Likewise, the existing `Pitajte
model` and AI error boxes are a strong mechanism but do not yet form a
cumulative competence sequence. AI should become a disciplined statistical
workflow across the book, not a repeated prompting aside.

Several further omissions matter more than adding another classical test. The
main text does not yet adequately teach how an analysis table is constructed,
how missingness and survey weights change the represented population, how to
read a binary-outcome model, how causal adjustment can help or harm, how
average associations can hide heterogeneity, how conclusions respond to
reasonable alternative decisions, or how a single study enters a cumulative
body of evidence. Repeated and clustered observations are acknowledged but not
turned into a clear stop rule. These are bounded literacy additions, not calls
for new chapters on data engineering, survey sampling, logistic regression,
causal inference, meta-analysis, or multilevel modelling.

Three further omissions are structural rather than topical, and none of them is
a missing subject. First, the book has no closure layer for its own assessment:
the four exercise tiers, the planted-error boxes, and the model-revision tasks
carry no solutions, rubrics, or statements of the intended error, so a reader
working alone cannot discover whether they succeeded. Second, the book teaches
the reading of numbers in media but never walks through the genre its third
promise actually names — a published regression table with model columns,
stars, reference categories, and parenthesised standard errors. Third, it
teaches the auditing of claims without ever teaching the making of one; no
thread carries the honest reporting sentence from Chapter 4 to Chapter 18, even
though the AI strand repeatedly asks students to judge an assistant's write-up.

### Readiness verdict

| Dimension | Current state | Readiness |
|---|---|---|
| Statistical correctness | Strong concepts, two load-bearing errors, several major qualifications needed | **Blocked** |
| Pedagogical architecture | Excellent central sequence; incomplete beginner pathways and flagship chapters | **Major revision** |
| Writing and voice | One convincing authorial voice; thin chapters read like briefing notes | **Major revision** |
| Evidence and citations | No fabricated keys found; claim-level support and metadata incomplete | **Major revision** |
| Data consistency | Seeded simulations are coherent; catalogue, empirical portfolio, licensing lanes, and student downloads are incomplete | **Major revision** |
| Figures and widgets | Strong system, all 17 twins present; one intro gap; no reproducible browser audit; no numeric parity check between a widget and its print twin | **Good with repairs** |
| Assessment and feedback | Four tiers, a planted-error box, and a model-revision task in every chapter; no answers, rubrics, or planted-error keys anywhere | **Major revision** |
| Transitions and flow | Strong within the main methods arc; weak at 3→4, 12→13, and 17→18 | **Moderate revision** |
| Build and deployment | Current HTML/PDF deploy successfully; dependency and CI governance gaps remain | **Operational, not fully reproducible** |
| Publication/legal | No formal edition, tag, changelog, citation instruction, or errata route; unresolved licence warning and data licences | **Blocked** |
| Reader evidence | Eight expert perspectives and deterministic checks; no contact with a reader of the intended audience | **Untested** |

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
| HTML/print widget parity | No such check exists | Nothing verifies that the OJS widget and its R twin produce the same numbers from the same parameters |
| Exercise closure check | No such check exists | No solutions, rubrics, or planted-error keys exist to check |
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

6. **[Text]** Every widget's statistical logic exists twice: once in OJS for the
   browser and once in R for the print twin. The widget contract check confirms
   that both exist and that the registry knows about them. Nothing anywhere
   compares what they produce. **[Assessment: Major]** Different generators,
   different parameterisations, different rounding, or a default that drifted in
   one implementation and not the other can make the interactive demonstration
   and its static twin tell different quantitative stories while both contracts
   pass and both renders succeed. A digital reader and a print reader would then
   be taught different numbers from the same figure, and the discrepancy would
   surface only if someone compared the two editions by hand.

   In a book whose central thesis is that computation must remain inspectable,
   silent divergence between its two computational paths is a first-order
   failure rather than a build detail. The repair is a golden-values test: for
   each widget, a small set of fixed parameter combinations, the expected
   outputs committed to the repository, and a tolerance-checked comparison of
   the OJS and R paths as part of the release checklist. Where the two paths
   legitimately cannot agree — a browser pseudo-random generator against R's —
   the test should compare distributional summaries rather than exact values,
   and the widget registry should record that the twin is a distributional
   rather than an exact match.

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

### Edition, citation, and errata

**[Text]** The book is continuously deployed from `main`. There is no tag, no
changelog, no archived snapshot, no instruction for citing the book, and no
route by which a reader can report a mistake.

**[Assessment: Major]** §2 records this as the reason a reviewer must cite a
commit hash rather than a page. The consequence for the book's actual users is
larger than a citation inconvenience. A lecturer cannot assign a version that
will still say the same thing at the exam. A student cannot cite the book in
coursework in a way that another reader can verify. A reader who finds an error
— which, at 51% completion with two known statistical blockers, is a certainty
— has nowhere to send it, and the project has no way to demonstrate that it was
fixed.

The remedy is small, standard, and independent of the manuscript work:

- tag a release whenever chapter prose changes materially, and keep a Croatian
  `CHANGELOG.md` written for readers rather than derived from Git history;
- archive each tagged release to obtain a persistent identifier, and publish a
  short *Kako citirati ovu knjigu* block on the landing page and in the
  colophon;
- freeze one snapshot per teaching term, so a course cites a fixed edition
  while `main` continues to move;
- open a reader-facing errata route and publish the dated log of reported,
  accepted, and corrected errors.

**[Assessment]** The errata log is not administrative hygiene in this project.
A textbook whose subject is the checkability of claims should visibly practise
correction. A public, dated list of its own repaired mistakes is the strongest
demonstration of its own thesis available to it, and it costs a page.

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

**Required action:** replace the manually duplicated inventory with one
machine-readable catalogue from which the public data page and Appendix C are
generated. Each entry needs the unit of analysis, source table or query,
version, retrieval date, licence, redistribution status, refresh policy,
transformation script, committed path, variables, missing-value conventions,
known caveats, and actual chapter consumers. Where it adds pedagogical value,
publish both an analysis-level file and a small derived aggregate so that a
student can reproduce the aggregation in R or jamovi and a print-only reader
can still work with the same question.

The catalogue also needs two explicit access lanes. **Bundled data** may be
redistributed directly with the book. **Portal-mediated data** remain at their
official archive and ship only with a selection recipe and transformation
script. Accessibility on the web is not, by itself, permission to rehost a
teaching extract.

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

### Two missing pathway components

**[Assessment]** The appendix set promises two things implicitly that it does
not contain.

**A numeracy floor.** The book states that it assumes no mathematics beyond
secondary school. That is a claim about the reader, not a service to them.
Percentages against percentage points, a proportion read as a rate, the
equation of a straight line and the meaning of its slope, and the logarithm as
a change of scale are all load-bearing in Chapters 1–6 and 16, and all are
precisely what a returning, anxious, or non-quantitative student has lost. The
audience is defined by not being analysts; assuming the floor holds is the one
place where the book's generosity toward its reader lapses.

The cheap repair is a short refresher appendix plus marginal `podsjetnik`
recalls at first use, so that the chapters themselves stay uncluttered and the
reader who needs the reminder is not made to feel addressed. This is a genuine
appendix G rather than an expansion of an existing one, because its function is
lookup, not sequence.

**Answers.** No appendix, chapter, companion, or teaching file contains
solutions, worked answers, or grading rubrics for any of the four exercise
tiers. Because this is a design gap rather than a missing file, it is treated
in §12.

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

### Terminology against Croatian convention

**[Assessment]** The glossary pairs every Croatian term with its English
equivalent, which serves a reader moving outward toward international
literature. Nothing checks the other direction: whether the book's Croatian
terms match established usage in Croatian statistical teaching and in the
domestic methodological literature. A student who leaves this book for another
Croatian course, or opens a Croatian methods text, needs the vocabulary to be
recognisable. A defensible coinage unique to this book imposes a translation
cost that the book never warns about, and it does so at exactly the moment the
student is least able to tell a terminological difference from a conceptual
one.

One deliberate pass by someone familiar with the domestic literature should
confirm each glossary term, record accepted alternatives where usage is
genuinely divided, and state in the glossary where this book has chosen among
competing conventions and why. Where the book deliberately departs from a
common Croatian rendering — which may be right, since some current renderings
are calques — the departure should be visible to the reader rather than silent.

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

7. **Twin parity:** the interactive widget and its printed twin are two
   independent implementations of the same statistical idea, in two languages,
   with two random-number generators, and nothing verifies that they agree
   numerically. The contract check confirms existence, not equivalence. See §4
   for the proposed golden-values test; the editorial consequence is that no
   figure caption or prose number derived from a widget can currently be
   trusted to describe both editions.

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

### Data-layer diagnosis

**[Assessment]** The book should not solve its empirical deficit by collecting
as many topical datasets as possible. That would increase maintenance while
leaving the central pedagogical weakness intact. A strong introductory text
needs a small number of memorable data stories and a deliberate contrast among
the processes that produced them.

The existing simulations are not an embarrassment to be replaced. The known
population in Chapters 8–11 is what makes repeated sampling, coverage, error,
and power visible. Simulations should remain wherever the lesson requires known
truth or repeated worlds. Empirical data should enter where the lesson concerns
measurement, provenance, selection, weighting, interpretation, or the fact that
the truth is not available for inspection.

The strongest portfolio would therefore expose students to these distinct
designs:

| Data-generating design | What the student can learn that another design cannot |
|---|---|
| Seeded simulation with known population | Repeated sampling, coverage, error rates, power, and a known target |
| Probability survey with weights | Representativeness, nonresponse, weighting, measurement, and person-level association |
| Administrative or electoral count | Complete recorded events, denominators, classification, and the difference between records and people |
| Official aggregate statistics | Suppression, revisions, mixed geographic levels, comparability, and ecological limits |
| Expert-coded latent index | Operationalisation, model-based measurement, disagreement, and uncertainty around a score |
| Digital trace or selected corpus | Platform dependence, selection into observation, heavy tails, changing collection systems, and missing context |
| Volunteer open survey | Why a very large sample does not repair self-selection and why openness does not imply representativeness |
| Restricted commercial/administrative source | The boundary between an interesting result and one a reader can independently reproduce |

This design diversity is more substantively important than nominal coverage of
sociology, political science, psychology, communication, and economics. A
single well-chosen survey can touch all five fields; five datasets generated in
the same way teach only one epistemic lesson.

### Dataset admission rule

A new dataset should enter the core book only if it passes all of the following
tests:

1. It contributes a data-generating design or substantive question not already
   represented.
2. Its unit of analysis can be explained in one sentence, including what one
   row does and does not represent.
3. It serves at least two chapters, or it is indispensable to one of the three
   identity chapters.
4. Its source, version, exact query or table, licence, and redistribution status
   are explicit.
5. A student-ready extract is small enough for browser download and jamovi,
   while the source data remain reachable for verification.
6. Refreshing it is a manual, tested publication action rather than a network
   dependency of rendering.
7. It contains a genuine complication worth teaching: weights, missingness,
   suppression, selection, denominators, measurement uncertainty, or a
   classification break. A perfectly polished CSV with no epistemic role is
   decoration.

As a default governance limit, the core should contain about six bundled
empirical packages, the two existing simulated datasets, and no more than two
portal-mediated survey sources. Frozen landmark datasets such as Anscombe and
Berkeley sit outside that cap because they are tiny, stable, and conceptually
specific.

### Recommended empirical portfolio

The portfolio below is ranked by pedagogical value relative to acquisition and
maintenance cost. It incorporates the data already available on the author's
disk and a short list of external sources whose current access conditions were
checked on 3 August 2026.

| Priority and access lane | Package | Natural unit | Distinctive role | Refresh |
|---|---|---|---|---|
| Core now, bundled | DZS tourism | month, county, or published category | Croatian official statistics; records versus persons; totals, missing flags, suppression, spatial hierarchy, and classification breaks | deliberate semiannual snapshot |
| Core now, bundled | DIP elections 2024 | municipality or electoral unit × list/result | census of recorded ballots; turnout denominators, percentages, categorical association, and ecological limits | frozen per election |
| Core now, bundled | DigiKat media actors | media actor × platform | Croatian communication data; skew, reach versus interaction, median splits, platform selection, and collection breaks | frozen dated snapshot until source pipeline is rebuilt |
| Core next, bundled | DZS population, migration, employment, pay, or poverty | county/year/category | demography, sociology, and labour economics through the same public PxWeb system already audited for tourism | annual snapshot |
| Core next, bundled | Eurostat EU society | country × fixed common year, or country-year | cross-European employment, education, poverty, demography, and digital participation; comparability and ecological inference | annual snapshot |
| External core, portal-mediated | ESS Round 11, Croatia | respondent | probability sampling, survey weights, attitudes, wellbeing, trust, media use, groups, and regression | pinned ESS edition |
| Core next, bundled | ParlaMint-HR teaching extract with ParlaSent companion | speech or sentence | text as data; corpus construction, relative frequency, coding, annotation disagreement, training/test separation, and AI classification | pinned corpus editions |
| Second wave, bundled after licence check | V-Dem v16 core extract | country × year | political science, expert-coded latent measurement, rankings, and uncertainty intervals | annual versioned release |
| Second wave, bundled | COVIDiSTRESS II teaching extract | respondent | psychology, stress, resilience, trust, open data, and a large non-probability sample | frozen |
| Optional global extension | World Bank WDI compact extract | country × fixed year, or country-year | a non-European development comparison with strong API metadata and visible missingness | annual snapshot |

The DZS tourism dump is the best first addition. It already contains a
self-documenting catalogue and reproducible PxWeb provenance. The full 137 MB
CSV tree should remain outside the repository. A first teaching package should
contain only:

- national monthly arrivals and nights from BS_TU11, with complete years and a
  clear distinction between monthly rows and annual totals;
- one complete county cross-section from BS_TU12;
- the three tiny experimental-platform tables T01–T03 in one consistent long
  file;
- optionally the small resident-travel tables T21/T22 for hand-computable and
  print exercises.

The source complications are themselves curriculum: an arrival is a
registration rather than a distinct tourist, `Ukupno` is mixed into the month
dimension, geography mixes levels, confidential and unpublished cells differ
from zero, and classifications change. The
[DZS reuse policy](https://dzs.gov.hr/o-zavodu/pravo-na-pristup-informacijama/otvoreni-podaci/1812)
permits copying, adaptation, and commercial or non-commercial reuse with
attribution.

DIP adds a data-generating design that DZS tourism cannot. Its
[open-data page](https://www.izbori.hr/site/en/general-information/open-data-1840/open-data/1851)
publishes election results in CSV and XLSX. A municipality/list extract from
the 2024 parliamentary election should be frozen as a historical dataset, not
silently replaced after the next election. It gives Chapters 1, 3, and 13 a
domestic case for turnout, denominators, vote shares, categorical tables, and
the ecological fallacy.

The DigiKat full Determ corpus must remain external. Its redistributable
aggregate actor tables are suitable only as a dated snapshot with the 2024
collection-method break and incomplete Instagram/TikTok coverage stated
prominently. Convert the selected RDS files to portable CSV and include the
actor-label dictionary needed to interpret them. The useful question is not
which outlet is “largest,” but whether posting volume, reach, and interaction
rank the same actors and how the answer changes when a median split creates
four named quadrants.

Eurostat should be a narrow, question-led extract rather than a warehouse. A
coherent candidate is material conditions and participation in contemporary
European societies, using perhaps five to seven indicators such as employment,
risk of poverty or social exclusion, tertiary education, early school leaving,
internet use, and age structure. Use one fixed common year and preserve missing
values. Do not create a false cross-section by selecting a different “latest
available” year for every country-indicator pair. Eurostat's
[API documentation](https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access/api-introduction)
states that the live database contains only the latest versions and does not
retain past versions, so committed snapshots and checksums are necessary. Its
[reuse policy](https://ec.europa.eu/eurostat/help/copyright-notice) allows
adaptation with source acknowledgement, subject to stated exceptions.

ESS is the strongest person-level dataset for the main empirical methods arc,
but it belongs in the portal-mediated lane unless the author obtains explicit
permission for a teaching extract. [Round 11 edition
3.0](https://www.europeansocialsurvey.org/data-portal) includes Croatia and
questions on trust, politics, health, wellbeing, media and internet use,
gender, employment, education, and demographics. The
[ESS conditions](https://www.europeansocialsurvey.org/contact/disclaimer)
license data CC BY-NC-SA 4.0 and recommend linking to the official portal
rather than placing datasets on external sites. The book should provide a
variable-selection recipe and a transformation script for a locally downloaded
file, or obtain written permission before bundling. Any extract must retain the
relevant design and analysis weights; removing them for simplicity would
undercut the reason to use a representative survey.

The text-analysis addition should use one compact teaching package built from
two linked sources rather than make the book ingest a full language corpus.
[ParlaMint 5.0](https://www.clarin.si/repository/xmlui/handle/11356/2004)
includes Croatian
parliamentary debates, speech-level text, dates, speakers, party and role
metadata, and automatically assigned broad topics. It is publicly available
under CC BY 4.0. The full Croatian archive is about 398 MB, so the book should
pin the source edition and redistribute only a documented, question-led
teaching extract such as `parlament_govori.csv`.

[ParlaSent 1.0](https://www.clarin.si/repository/xmlui/handle/11356/1868) is a
useful labelled companion under CC BY-SA 4.0. It contains 18,200 parliamentary
sentences across seven languages, including a Bosnian/Croatian/Serbian
component, with two human annotations, reconciliation, and train/test fields.
The training examples were sampled with sentiment lexicons to over-represent
sentiment-bearing language, while the test construction differs. That is a
feature for teaching selection, annotation, and validation, but it prevents
casual prevalence claims from the training file. Preserve the country field,
the individual coder labels, the reconciled label, and the split indicator.
Never present the reconciled label as unqualified ground truth.

V-Dem should enter only after the political-science use is explicit. Version
16, published in March 2026, ships with data, codebook, changes, cautionary
notes, and suggested citations in several formats on the
[official dataset page](https://v-dem.net/data/the-v-dem-dataset/). A useful
student extract would contain a handful of high-level indices, their
uncertainty intervals, country, region, and year. Its strongest role is to show
that a country ranking is an estimate built from expert judgments and a
measurement model, not a directly observed physical quantity.

COVIDiSTRESS II is preferable to a difficult clinical or psychometric dataset
if the book needs a redistributable psychology example. The cleaned open file
contains 15,740 respondents from 137 countries and measures stress, resilience,
trust, information, and behavior. It is available under CC BY 4.0 through the
[data descriptor](https://pmc.ncbi.nlm.nih.gov/articles/PMC9213519/). Its
volunteer recruitment makes it unsuitable for population prevalence claims,
but ideal for the question “Can an enormous sample still be badly selected?”
That question belongs in Chapters 2, 8, and 12.

World Bank WDI is an optional global extension, not a mandatory sixth source
family. The official
[Indicators API](https://datahelpdesk.worldbank.org/knowledgebase/articles/889392)
requires no authentication and exposes data and metadata programmatically;
World Bank open datasets are generally licensed under
[CC BY 4.0](https://datacatalog.worldbank.org/public-licenses). Use a fixed
year, a short indicator list, and the source organisation for every indicator.
If Eurostat and V-Dem already supply enough country-level work, WDI should wait
rather than duplicate the same ecological design.

### Empirical-data spine through the book

Real data should be distributed by rhetorical function, not forced into every
widget or every calculation.

| Book location | Primary data role | Recommended source |
|---|---|---|
| Chapters 1–3 | What was counted, what denominator was used, and how provenance or aggregation changes a claim | DZS tourism and DIP elections |
| Chapters 4–6 | Describe, visualise, and compare recognisable empirical distributions without causal overreach | DigiKat, DZS tourism, and a compact Eurostat extract |
| Chapters 7–11 | Experience repeated randomness and known targets before formulas | keep the seeded simulations; use empirical data only in short transfer exercises |
| Chapter 12 | Follow an auditable research lifecycle from raw/cleaned data through decisions, openness, and limits | COVIDiSTRESS or a separately verified licensed replication-results table |
| Chapters 13–16 | Reuse one person-level survey for crosstabs, two groups, several groups, and regression | ESS Round 11 Croatia, with weights and a fixed variable set |
| Chapter 17 | Contrast model performance with corpus and label construction, institutional context, and measurement uncertainty | retain known-truth simulation where needed; use a ParlaMint-HR extract and ParlaSent labels for the worked empirical analysis |
| Chapter 18 | Demonstrate the full workflow with known generated truth, then transfer judgment to a real unknown-truth case | retain `anketa_mreze`; add a bounded DZS/DIP/DigiKat/Eurostat/ParlaMint transfer task |

This spine resolves a false choice. The simulation sequence remains the best
way to build inferential intuition, while the empirical sequence teaches why
real social-science claims are never simply simulations with messier numbers.

### Text as data and the cumulative AI strand

#### Curricular judgment

Text analysis now belongs in a statistics textbook for social scientists, but
its reason for inclusion is not that every student must learn a modern NLP
pipeline. Its statistical contribution is to reveal that data do not arrive as
variables: researchers choose the corpus, unit, preprocessing rules, coding
scheme, labels, comparison groups, and validation standard. The governing
proposition should be that text analysis is measurement before it is
computation.

Chapter 17 is the correct home for one substantial module because it can join
prediction, labels, fairness, language models, and institutional use. The
module should cover:

- the distinction among word, sentence, speech, document, and speaker as units;
- corpus inclusion and exclusion, dates, missing speech, and selection;
- counts and relative frequencies with explicit denominators;
- a document–term table and a restrained introduction to TF–IDF;
- dictionary, human, and model coding as alternative measurement procedures;
- annotator disagreement, reconciliation, and a held-out validation set;
- confusion tables and subgroup error patterns for automated labels;
- negation, irony, context, Croatian morphology, and construct validity;
- topic models, embeddings, and generative classification as literacy topics,
  not required implementation techniques.

The worked example should begin with an interpretable social-science question,
such as whether the vocabulary used around a public issue differs across
periods or political groups. It should then show how the answer changes when
speech length is normalised, corpus boundaries move, or a human, dictionary,
and AI coding scheme disagree. A final held-out comparison should separate
model performance from substantive validity.

Because the book assumes no programming, students should not be required to
build a tokenizer or Croatian lemmatisation pipeline. The downloadable package
should include raw text for inspection, a documented analysis-ready table of
selected term counts or lemmas, and the labelled sentences. Folded R code in
Appendix A can reproduce the transformation; the main chapter and Appendix B
should work from the prepared tables and ask students to judge units,
denominators, coding, and validation. Computation remains delegated, while the
decisions remain visible.

The module should not add a second unrelated central widget. If the present
fairness simulation remains the Chapter 17 widget, text analysis should be the
`Razrađeni primjer`. A later redesign could instead make one integrated
`laboratorij kodiranja teksta` in which readers inspect sentences, compare
human and automated labels, and see a confusion table update. That decision
must be made before widget production, not after prose is written.

#### Cross-chapter preparation

Text as data should be concentrated in Chapter 17 but prepared earlier so it
does not arrive as a new subject in the final methods chapter.

| Location | Cumulative contribution |
|---|---|
| Chapter 2 | A coding rule turns language into a variable; categories are measurements with exclusions and ambiguity. |
| Chapters 4–5 | Word counts require denominators; skewed frequencies and group comparisons can be described and visualised. |
| Chapters 6 and 13 | A coded textual category can enter an association or contingency table without becoming an objective property of the speaker. |
| Chapters 8–10 | Corpus selection and a labelled test sample determine what can be generalised and how uncertain performance estimates are. |
| Chapter 17 | Corpus construction, human/dictionary/AI coding, held-out validation, subgroup errors, feedback, and language models become one complete argument. |
| Chapter 18 | A real-data transfer task requires a corpus passport, an audit trail, and a claim whose limits follow from the collection and coding process. |

#### AI as a book-wide statistical practice

The book should state a stable thesis in the preface and return to it at part
boundaries: AI has not replaced the logic of statistical evidence; it has
greatly reduced the cost of producing a plausible-looking analysis and
therefore increased the burden of verification. AI then appears in three
roles:

1. **Instrument:** an assistant for explanation, transformation, simulation,
   calculation, visualisation, and code reading.
2. **Fallible analyst:** a producer of claims whose data, assumptions,
   calculations, citations, and uncertainty must be audited.
3. **Object of social research:** a classification and decision system whose
   labels, incentives, error distribution, feedback, and social consequences
   are themselves empirical questions.

The fixed `Pitajte model` and `callout-greska` pattern should therefore become a
competence ladder. Each chapter adds one failure mode rather than repeating
generic advice:

| Book stage | AI practice to add |
|---|---|
| Chapters 1–3 | Verify provenance, denominators, units, citations, and apparently precise numbers. |
| Chapters 4–6 | Reproduce summaries and plots; detect hidden exclusions, inappropriate scales, and transformed variables. |
| Chapters 7–9 | Distinguish generated certainty from sampling uncertainty; refuse population claims unsupported by the design. |
| Chapters 10–12 | Check the null, multiplicity, researcher flexibility, evidential asymmetry, and reproducibility. |
| Chapters 13–16 | Audit reference groups, assumptions, omitted variables, causal language, diagnostics, and sensitivity. |
| Chapter 17 | Separate training from evaluation; inspect labels, leakage, threshold choice, subgroup errors, distribution shift, and text-coding validity. |
| Chapter 18 | Specify, delegate, reproduce, challenge, document, and disclose the complete AI-assisted workflow. |

Appendix F should turn that ladder into one copyable protocol: define the
question and target quantity before prompting; state what data may be shared;
request assumptions and reproducible steps; independently check key results;
run one sensitivity or counterexample; record the prompt, tool, date, and
material transformations; and disclose the division of responsibility. The
chapters should reference this protocol progressively rather than restating it.

Model-specific interfaces and claims should be dated and kept out of the
conceptual spine. Exercises should use short frozen AI-output snapshots where a
stable comparison is required, while allowing students to repeat the task with
their current assistant. No exercise should require uploading personal,
restricted, or identifiable research data to a public model.

This proposal should replace lower-value breadth rather than expand the data
portfolio indefinitely. The ParlaMint/ParlaSent package adds an unstructured
data-generating process that none of the proposed rectangular datasets can
teach. It therefore has priority over the optional World Bank package and, if
scope remains tight, over COVIDiSTRESS. V-Dem should remain conditional on a
specific political-measurement question.

### Data science as the evidence workflow, not a fifth promise

#### Scope judgment

Data science should be strongly integrated as a way of working with evidence
and lightly integrated as a technical discipline. The book should not promise
to make its non-programming social-science reader a data scientist, and it
should not add a survey chapter on SQL, cloud systems, scraping, dashboards, or
machine-learning packages. Data science should instead make visible how a
question becomes data, how data become an analysis object, and how an output
becomes a reproducible and appropriately limited claim.

As an editorial budget rather than a page-count formula, approximately 70% of
the conceptual attention should remain statistical reasoning and methods, 20%
should concern the data-science lifecycle and reproducibility, and 10% should
concern AI and algorithmic systems. These domains overlap: text coding,
predictive validation, fairness, and AI-assisted analysis belong to more than
one category. The point of the ratio is to keep statistics as the epistemic
centre while giving real-data workflow enough weight to stop the methods from
appearing to begin with an immaculate table.

The [National Academies' undergraduate data-science
report](https://www.nationalacademies.org/projects/DEPS-CSTB-16-01/publication/25104)
describes data science as an interdisciplinary field spanning computation,
statistics, domain knowledge, communication, and ethics. That conception fits
this book. A narrow “more algorithms” conception does not.

#### Four related but distinct activities

The book should define the relationship once and use the distinction
consistently:

| Activity | Governing question | Distinctive contribution |
|---|---|---|
| Statistics | What do these data justify believing? | design, sampling, estimation, uncertainty, inference, and causal restraint |
| Data science | How can real data sources become a reliable and reproducible analysis? | acquisition, validation, joining, transformation, computation, documentation, and communication |
| Machine learning | Will a learned pattern perform on genuinely new observations? | training/validation/test separation, prediction, classification, regularisation, and evaluation |
| AI system | Can learned patterns be used to generate, recommend, classify, or act in an institutional setting? | automation and interaction at scale, including feedback, monitoring, and consequences |

A concise book-level formulation is:

> Statistics judges whether an answer deserves belief. Data science makes the
> path from source to answer inspectable and reproducible. Machine learning
> asks whether a pattern generalises. AI turns learned patterns into systems
> that produce outputs or influence decisions.

This distinction prevents two common mistakes. A reproducible data pipeline
does not make an invalid inference valid, and high predictive accuracy does not
turn a model into a causal explanation. Conversely, excellent statistical
reasoning cannot rescue unknown provenance, duplicated rows, outcome leakage,
or an irreproducible transformation.

#### How data-intensive practice enabled modern AI

Data science did not historically create AI; AI and statistical learning
predate the contemporary disciplinary label. Modern AI grew from the
combination of statistical learning, machine-learning algorithms, digital data,
optimisation, computing hardware, human annotation, software infrastructure,
and systematic evaluation. The shift from predominantly hand-written rules to
systems trained on examples is chiefly a machine-learning shift. Data science
made the surrounding process operable at scale by organising acquisition,
cleaning, labelling, versioning, experimental splits, evaluation, deployment,
and monitoring.

The current [OpenAI overview of foundation-model
development](https://help.openai.com/en/articles/7842364-how-chatgpt-and-the-language-models-are-developed)
describes stages of training-data preparation, pre-training, post-training, and
continuing evaluation. It explains text generation as successive prediction of
tokens from learned relationships. The pedagogical point is not the product
detail: a fluent response is generated by a predictive system, not retrieved
as a certified statement from an evidence database.

The book can represent the relationship as a lifecycle with feedback:

```text
social question and institutional context
                 ↓
      data-science pipeline
                 ↓
 statistical or machine-learning model
                 ↓
       AI system and interface
                 ↓
 human use, decisions, new data, and feedback
                 └───────────────────────────↺
```

Every arrow can change the represented population, construct, objective, error
distribution, or social consequence. Chapter 17 should therefore treat an AI
system as more than a fitted model: it is a model embedded in a data pipeline,
interface, institution, and feedback process.

#### How AI changes data science

Generative AI sharply reduces the cost of producing transformations, code,
graphs, model specifications, and plausible prose. It does not remove the need
for statistical or domain judgment. The practical bottleneck moves:

- from writing a command to specifying the correct task;
- from obtaining an output to validating it;
- from recalling software syntax to understanding the data-generating process;
- from producing one analysis to comparing defensible alternatives;
- from presenting an answer to documenting provenance and responsibility.

An assistant can execute flawless syntax after an incorrect join, leak outcome
information into predictors, optimise the wrong target, or translate an
association into causal language. Fluency can make these failures less visible.
Data-science education in the AI era must therefore include evaluation of the
human–AI workflow, not only evaluation of the final model.

The [NIST AI Risk Management
Framework](https://airc.nist.gov/airmf-resources/airmf/) treats risk management
as continuous across the AI lifecycle and emphasises testing, evaluation,
verification, validation, data suitability, construct validation, and
monitoring. The book does not need to reproduce that governance framework, but
its statistical lessons should share the lifecycle view: training is not the
endpoint and a model cannot be judged independently of its data and use.

#### One lifecycle distributed through the existing book

Introduce one stable data-science lifecycle near the preface or Chapter 1 and
highlight the relevant stage as the reader advances:

```text
question → acquire → validate → prepare → explore → model
         → evaluate → communicate → monitor
```

| Book location | Data-science contribution |
|---|---|
| Part I | provenance, units, measurement, eligibility, sampling frames, consent, and differences among designed, administrative, platform, and generated data |
| Part II | identifiers, raw and derived variables, joins, recodes, missingness, transformations, exploratory displays, and the audit trail from source to figure |
| Part III | distinction among a probability sample for population generalisation, a training sample for estimation, and validation/test data for predictive evaluation |
| Part IV | analytical flexibility across the entire pipeline; versioning, preregistration, reproducibility, sensitivity, and evidence synthesis |
| Part V | explanation versus prediction, leakage, overfitting, calibration, thresholds, subgroup evaluation, distribution shift, text as data, deployment, and feedback |
| Chapter 18 | one reproducible evidence package: dataset passport, source/version record, transformation log, analysis, sensitivity check, claim boundary, AI-use record, and disclosure |

Sampling and train/test separation must not be conflated. Random sampling
supports a particular kind of population generalisation; a held-out test set
estimates performance on observations drawn under a specified predictive setup.
Neither operation automatically supplies the guarantee provided by the other.
That distinction is a particularly valuable Chapter 8→16→17 bridge.

#### What remains outside scope

The main book should not teach SQL, database administration, cloud
infrastructure, web scraping, dashboard engineering, package comparison,
hyperparameter tuning, neural-network mathematics, or production deployment.
Those belong in a separate data-science course or optional practical material.
The reader should understand how such systems affect provenance, evaluation,
and claims without learning to build them.

Data science should therefore remain a delivery mechanism for the existing
four promises, not become a fifth promise. The minimum concrete implementation
is one lifecycle map near the beginning, a substantial raw-to-analysis-table
example in Part II, an explicit sampling-versus-test-data bridge, workflow-wide
reproducibility in Chapter 12, prediction and deployment literacy in Chapters
16–17, and a reproducible evidence package in Chapter 18.

### Further high-value gaps and connective architecture

The next substantive pass should not become a catalogue of additional methods.
It should address the places where an introductory procedure meets the
conditions of actual social research. The following additions are ranked by
their contribution to the book's four promises and can be made without changing
the chapter order.

#### The analysis table is constructed, not found

The main text currently reaches missing values chiefly in the practical
appendix and the final project. It should show earlier that every clean table is
the result of consequential decisions. A single recurring pipeline would make
those decisions visible:

```text
source data → eligibility and units → joins and recodes → analysis table
            → aggregate or model → displayed result → claim
```

The reader does not need to become a data engineer. The reader does need to
recognise duplicate identifiers, a join that multiplies rows, totals mixed with
components, zero confused with missing or suppressed, changing category codes,
complete-case deletion, and a filter that silently changes the target
population. Chapter 2 should establish units and eligibility; Chapter 4 should
show one raw-to-analysis transformation; Chapter 12 should treat that pipeline
as part of researcher flexibility and reproducibility; Chapter 18 should audit
it. A planted AI error should eventually perform correct arithmetic on a table
created by an incorrect join.

Missingness should be taught as information about the data-generating process,
not as a software nuisance. The minimum main-text treatment is to count it,
locate it, compare observed cases with omitted cases where possible, state the
chosen rule, and test whether a defensible alternative changes the conclusion.
Multiple imputation can remain outside scope.

#### Survey realism beyond the ideal simple random sample

Chapter 8's repeated-sampling mechanism should remain untouched, but the book
needs a bridge from that ideal to ESS, polls, web panels, and actual survey
reports. Students should be able to explain:

- coverage: who had a chance to enter the sampling frame;
- unequal selection probabilities and design weights;
- nonresponse and nonresponse adjustment;
- post-stratification or calibration to known population margins;
- weighted versus unweighted percentages;
- probability samples versus opt-in or volunteer samples;
- why sample size alone cannot repair selection bias.

[AAPOR's survey-error guidance](https://aapor.org/standards-and-ethics/standard-definitions/)
distinguishes coverage, measurement, and nonresponse effects from sampling
error, while its
[disclosure standards](https://aapor.org/standards-and-ethics/disclosure-standards/)
require enough information about recruitment, response, weighting, wording,
and fieldwork to judge a published result. The book should turn those fields
into a compact poll-reading card used in Chapters 2, 3, 8, and the ESS examples
in Chapters 13–16. One small weighted/unweighted table is enough; survey-
sampling variance formulas are not required.

#### Binary-outcome and odds-ratio literacy

Chapter 16 currently states that a categorical outcome requires an extension
outside the book. That boundary is defensible computationally but too strong
for a book promising to help students read published social science. Binary
outcomes, logistic regression, odds ratios, and predicted probabilities are too
common to remain unnamed.

Add a short reading bridge near the end of Chapter 16 or at the Chapter 16→17
boundary. It should teach students to:

- recognise a binary outcome and why an unconstrained straight-line model is
  awkward for probabilities;
- distinguish probability, odds, odds ratios, and risk ratios;
- avoid translating an odds ratio as a percentage change in probability;
- read predicted probabilities and their intervals across groups;
- recognise reference categories and adjusted versus unadjusted comparisons;
- prefer a predicted-probability display when log-odds obscure the substantive
  result.

Maximum likelihood, the logit derivation, and software production can remain
outside scope. This is model-reading literacy, not another full method chapter.
It also creates a clean bridge to classification probabilities and thresholds
in Chapter 17.

#### Causal literacy beyond “correlation is not causation”

The current Chapter 2→6→16 seed is sound but should carry one stable visual and
vocabulary. A simple causal diagram can distinguish exposure, outcome, common
cause, mediator, and collider or selection variable. The important lesson is
not diagram syntax. It is that adding every available control variable can
create bias as well as remove it.

The sequence should be:

- Chapter 2: design, temporal order, common cause, and the question “what would
  have happened under another condition?”;
- Chapter 6: association remains descriptive even when it is strong;
- Chapter 8: sampling determines population reach, not causal identification;
- Chapter 16: adjusted association is not automatically an intervention effect;
- Chapter 17: a predictive feature may be useful without being causal, while
  deployment can itself change the data-generating process.

No propensity scores, instrumental variables, difference-in-differences, or
causal estimators are needed. The gain comes from preventing the routine error
that regression “controls away” all causal doubt.

#### Heterogeneity and interactions: an average is not everyone

The book moves effectively from distributions to average group differences,
but it needs a bounded account of conditional relationships. An association or
effect can differ by age, prior attitude, institution, period, or another
social context. Students should learn to read an interaction through predicted
values or lines, not by memorising a product-term coefficient.

The concept is already latent across the book: small multiples in Chapter 5,
Simpson's paradox in Chapters 1 and 6, group comparisons in Chapters 14–15,
regression in Chapter 16, and unequal error patterns in Chapter 17. Chapter 16
should provide the explicit harvest. The minimum standard is one interaction
plot, a clear distinction between subgroup description and exploratory
subgroup searching, and the sentence that an overall average need not describe
any particular group.

#### Sensitivity analysis as the positive answer to researcher flexibility

Chapter 12 explains how reasonable choices can become a garden of forking
paths. The rest of the book should teach the constructive response: disclose a
primary analysis and ask whether the conclusion survives one defensible
alternative. Each substantial empirical example can vary one choice suited to
its chapter:

- mean versus median or original versus transformed scale;
- weighted versus unweighted estimate;
- inclusion versus exclusion of an influential observation;
- one operational definition versus another;
- complete cases versus another transparent missing-data rule;
- unadjusted versus adjusted model;
- one classification threshold or coding scheme versus another.

This should be named **sensitivity analysis** in ordinary language and should
not be reduced to “the result stayed significant”. Compare effect estimates,
intervals, substantive conclusions, and represented populations.

#### From one study to a body of evidence

Chapter 12 names meta-analysis and publication bias but does not yet teach the
reader how to interpret a synthesis. One carefully chosen forest plot would
materially improve research literacy. Students should be able to identify the
study estimates and intervals, the pooled estimate, visible heterogeneity, and
the possibility that precise synthesis of selected or biased studies remains
misleading. The chapter should distinguish replication as cumulative evidence
from a winner–loser contest between an original and a repeat study.

The book need not calculate a meta-analysis, choose between estimators, or
teach funnel-plot diagnostics. It should teach that a single study is rarely
the final evidential unit and that uncertainty across studies includes context,
measurement, and design—not only sampling error within each study.

#### Dependence as a recognition and stop rule

Paired data appear in Chapter 14, and Chapters 15–16 acknowledge grouped and
repeated observations, but the boundary should become operational. A row is not
automatically an independent unit when pupils share a school, residents share a
municipality, posts share a media outlet, the same person is observed again,
countries recur across years, or actors are connected in a network.

The book should not add multilevel, longitudinal, time-series, or network
models. It should teach a red flag: if rows share a person, organisation, place,
period, or network relationship, ordinary standard errors and tests may not be
appropriate. Appendix D should therefore answer both “which method in this
book?” and “when is no method in this book adequate without an extension?”

#### Ethics throughout ordinary statistical practice

Ethics should not be confined to privacy, open science, and algorithmic
fairness. It begins when categories are defined and continues through omission,
small-cell disclosure, proxy variables, model choice, communication, and the
distribution of error. Every dataset passport should ask who defined the
categories, who is absent, who can be identified, who benefits from the
analysis, who bears a false positive or false negative, and whether an affected
person can challenge a classification.

The [ASA Ethical Guidelines for Statistical
Practice](https://www.amstat.org/your-career/ethical-guidelines-for-statistical-practice)
explicitly extend ethical responsibility across data collection, processing,
analysis, communication, and model or algorithm development and deployment,
including responsibilities to data subjects and people directly affected. The
book can operationalise that standard through recurring questions rather than
an isolated ethics chapter.

#### Simulation, synthetic data, and fabricated evidence

The book's simulation-first identity makes it especially important to
distinguish four objects:

1. a simulation with a known generating mechanism, used to reveal a concept;
2. synthetic data designed to resemble protected or inaccessible observations;
3. model-generated hypothetical answers used for exploration or testing;
4. fabricated observations presented as empirical evidence.

Chapters 3, 8, 12, 17, and 18 should state the boundary appropriate to their
task. In particular, LLM-generated “respondents” cannot substitute for sampled
people when making claims about a population. Synthetic data may protect
privacy or test a workflow, but fidelity to selected statistical patterns does
not establish substantive validity or representativeness.

#### Reading published research, not only public claims

`Statistika u divljini` teaches the reader to dissect a media claim, a poll, a
headline, or a chart, and it does that well. The book's third promise, however,
is that the student can read the inferential analyses that dominate published
social science, and the genre in which those analyses actually arrive is not a
headline. It is the journal results table: numbered model columns, coefficients
with standard errors in parentheses, significance stars, an implied reference
category, N, R² or a pseudo-R², and a note about robust or clustered errors.
Neither the manuscript nor the rest of this review contains a single walkthrough
of that artifact.

One annotated real table, placed as a harvest at the end of Chapter 16, would
serve the third promise more directly than any additional method. After it the
reader should be able to say what one row is and what one column is, which
comparison a coefficient makes and against which reference category, why the
same predictor changes across model columns and what that movement means, what
the parenthesised number is, what the stars do and do not license, which
quantity is missing — usually the predicted values that would make the estimate
substantive — and which sentence from the abstract the table does not actually
support. A second, much shorter pass over a results *paragraph* teaches the
matching prose conventions, including the ones that hide a weak result inside a
confident sentence.

The source should be a published Croatian or regional social-science article
whose topic or data the book already touches, reproduced under quotation with a
full citation. This is reading literacy, not reproduction: the book does not
need the data and must not refit the model. The natural companions are the
odds-ratio bridge recommended above, since many published tables in this
literature are logistic, and Chapter 12's evidence-synthesis reading, since a
forest plot is the other genre a student will meet without preparation.

#### Writing the honest sentence

The book teaches the reader to audit a claim and never to produce one. Every
chapter ends in an interpretation, Chapter 18 requires a written report, and
the AI strand repeatedly asks the student to judge an assistant's write-up, but
nowhere is statistical communication taught as a skill with standards of its
own. The GAISE outcomes name communication explicitly, and this book has an
additional reason of its own: a reader who has never been shown what an honest
sentence looks like cannot reliably recognise a dishonest one, and cannot audit
the fluent, well-formed paragraph an assistant returns in seconds.

The material is small, and almost all of it is already latent in the manuscript
as authorial practice rather than as taught content:

- report an estimate with its interval and its units, never a bare point;
- name the population the number describes before naming the number;
- let the grammar of the sentence distinguish a description, an association,
  and a causal claim, rather than relying on a hedge word;
- state what is uncertain without either false modesty or hedging that carries
  no information;
- describe a table or figure in prose that adds the reading instead of
  restating the cells;
- close with the specific limitation that would change the conclusion, not a
  generic paragraph of limitations.

This should be a thread rather than a section: planted in Chapter 4 with a
single sentence about a summary, developed in Chapters 9, 11, and 16 where
estimates, intervals, and coefficients become reportable, and harvested in
Chapter 18, where the student writes the report and then audits an assistant's
version of the same report against the same standards. It is the missing
seventh thread in the ratification table below. The six threads already
proposed are all about judging someone else's claim; none is about making one's
own, even though making one is what the capstone, the coursework, and the
student's eventual thesis all require.

#### Assessment closure: the answer, the rubric, and the planted error

**[Text]** Every chapter carries four exercise tiers, a `callout-greska`
containing one deliberate mistake, and a `revizija modela` task in which the
student grades an AI-generated solution. No file in the repository contains a
solution, an expected answer, a grading rubric, or a statement of what the
planted error was.

**[Assessment: Major]** The book's primary delivery is a public website, and
its stated audience includes students working through it without an instructor
beside them. Without closure, the most original assessment in the book is also
the least usable. A reader who cannot find the planted error learns nothing
from having failed to find it. A reader who finds a *different* plausible
objection — and a well-written AI analysis usually offers several — has no way
to discover whether it was the intended one, and may leave with a
misapprehension the exercise itself created. The `revizija modela` tier carries
the same problem in stronger form, because grading an analysis is exactly the
task in which a beginner's confidence is least calibrated and most in need of a
reference standard.

The minimum closure layer:

- for each `callout-greska`, an author's key naming the single planted error,
  the diagnostic that reveals it, and at least one plausible-but-wrong reading
  that should not count as a find;
- for the conceptual and critical tiers, a short model answer stating what a
  complete response contains, rather than one correct string;
- for the computational tier, the numerical answer and the check that confirms
  it;
- for `revizija modela`, a ranked rubric of the small number of things a
  competent review must notice, separating the fatal objection from the merely
  worthwhile ones.

Delivery is a policy decision the project must make deliberately, not a
technical one. A collapsed `<details>` block inside the chapter is the most
useful arrangement for self-study and the least useful for assessed coursework;
a solutions appendix excluded from the `kolegij` profile, or per-chapter keys
rendered only into the teaching edition, preserves both audiences. The build
system already supports profile-conditional content, so the engineering is
trivial and only the editorial choice is open. That choice interacts with the
teaching layer excluded from this review's scope, and the two should be settled
together.

**[Assessment]** This should be ratified before Chapters 3, 12, and 17 are
expanded. Their exercises are being written now, and writing a key alongside a
planted error costs minutes, while retrofitting keys across nineteen units
afterwards is a separate project — and one that requires reconstructing what
each planted error was originally meant to be.

#### Retrieval across chapters, not only within them

The book spirals its cases well. Berkeley, Anscombe, and the sampling machine
each return with something new to ask. Its assessment does not spiral at all.
Every exercise tier examines the chapter that contains it, so the reader
practises each idea exactly once, at the moment of maximum recency, and then
never again. For a one-semester course this is probably a larger threat to
retention than several of the moderate-priority items in §15.

Two bounded additions would close the gap without touching the chapter
contract. First, one exercise per chapter from Chapter 6 onward should require
material from at least two chapters earlier; the ideal form is a task that
cannot be completed with the current chapter's method alone, so the reader must
first recognise which earlier tool applies. That recognition step is the actual
skill, and the current design never tests it. Second, each part boundary should
carry a short self-check of what the whole part now permits, aligned with the
exit bridges recommended in §16. Both are far cheaper than new prose, and both
depend on the closure layer above, since a self-check without an answer is a
prompt rather than a check.

### A visible claim map for the whole book

The most powerful connective intervention would be to label the kind and reach
of the claim in every sustained example. A simple claim map is more accurate
than a single method ladder because population reach and claim type are partly
independent.

| Claim dimension | Questions for the reader |
|---|---|
| Description | What is present in these data? |
| Association | What varies together, and within which groups or conditions? |
| Generalisation | From which observed units to which target population, place, or period can the result travel? |
| Prediction | How well does the rule perform on genuinely new observations? |
| Causation | What would change under an intervention, and what design supports that contrast? |
| Decision | What action follows, what errors matter, and who bears their consequences? |

Each vignette, worked example, wild claim, and AI audit should locate itself on
this map and name the unavailable claims. A result can be a strong description
and a poor population generalisation, or a useful prediction without identifying
a cause. That distinction is the substance of statistical literacy.

Six questions can then become the book's recurring judgment protocol:

1. What does one row or observation represent?
2. Who or what could not enter these data?
3. What quantity and type of claim is being targeted?
4. Which sources of uncertainty are represented, and which remain outside the
   calculation?
5. Which reasonable alternative decision could materially change the answer?
6. Who may be affected if the conclusion or decision is wrong?

These questions should appear in full at part boundaries and in abbreviated
form inside dataset passports, worked examples, and Appendix F. They connect
statistical and AI literacy without creating a second parallel textbook.

### Cross-chapter threads to ratify

The empty, unratified chapter-spine registry means these connections are not yet
editorially guaranteed. Before substantive rewriting, ratify a small set of
book-wide threads and record where each is planted, developed, and harvested.

| Thread | Planted | Developed | Harvested |
|---|---|---|---|
| Unit of analysis | Chapters 1–2 | Chapters 4, 8, 13–14 | text units in 17; full audit in 18 |
| Selection and absence | Chapters 2–3 | range restriction in 6; sampling/nonresponse in 8; publication selection in 12 | training data and platform selection in 17; recruitment audit in 18 |
| Denominator | percentages and Simpson in 1–3 | summaries and graphs in 4–5; row/column percentages in 13 | relative term frequency and error rates in 17 |
| Uncertainty budget | measurement and design in 2 | sampling, intervals, testing, power, and researcher choice in 8–12 | model, coding, distribution-shift, and decision uncertainty in 16–18 |
| Consequences of error | public claims and base rates in 3 and 7 | Type I/II errors and smallest important effect in 10–11 | thresholds, unequal error burdens, and appeal in 17–18 |
| Reproducibility and provenance | visible transformation in 4–5 | analytic flexibility and open practice in 12 | complete audit trail and AI disclosure in 18 |
| Communication of a claim | first reported summary in 4 | estimate, interval, and magnitude language in 9 and 11; conditional interpretation in 16 | the student's own written report, then an audit of an assistant's report on the same analysis, in 18 |

The seventh thread is new to this review and is argued above. The first six all
train the reader to judge a claim that someone else has made; only the seventh
requires the reader to make one, which is what the capstone and any subsequent
coursework actually demand.

Part-ending bridges should state what the reader can now claim, what remains
unavailable, and which thread the next part develops. This is a more substantive
connection device than repeating previews or adding another callout type.

### Scope control for these additions

These recommendations do not justify new numbered chapters or additional
central widgets. A thread should receive a short seed where first needed, one
substantial harvest, and later retrieval rather than repeated mini-lectures.
Binary-outcome material is for reading predicted probabilities and odds ratios,
not fitting a full family of generalised models. Causal diagrams support claim
discipline, not estimator instruction. Dependence, time series, networks, and
multilevel structure receive recognition-and-routing guidance only.

Where chapter length becomes constrained, remove redundant test mechanics,
threshold catalogues, and repeated assumption prose before cutting the claim
map, data-construction audit, sensitivity comparison, or evidence-synthesis
reading. The new material should increase the proportion of the book devoted to
judgment rather than enlarge its menu of procedures.

The four additions introduced by this pass are bounded on the same terms. The
published-results-table walkthrough is one annotated artifact in Chapter 16 and
one shorter pass over a results paragraph, not a course in econometric
reporting. The communication thread is a seed, three developments, and a
harvest, not a writing appendix. The closure layer is authored alongside
existing exercises rather than as new content, and its size is fixed by the
exercises that already exist. The retrieval additions replace one exercise per
chapter rather than adding a tier. None of them requires a new chapter, a new
widget, or a new callout type.

### What would make the integration outstanding

1. **Organise around recurring questions, not file names.** DZS tourism can ask
   whether more arrivals mean more people. DIP can ask whether higher turnout
   means stronger support. DigiKat can ask whether reach means engagement. ESS
   can ask whether media use and institutional trust are associated after age
   and education are considered. V-Dem can ask how certain a country ranking
   really is. ParlaMint can ask whether a vocabulary difference reflects
   political language, unequal speech length, a shifted corpus, or the coding
   method. Students remember the question and encounter progressively better
   answers as their methods expand.

2. **Compare the same construct across designs.** Media use in ESS is a
   respondent's reported behavior; DigiKat records platform-visible content and
   interactions. Political trust in ESS is an individual response; V-Dem is an
   expert-coded country-level institutional measure. Putting such pairs next to
   each other teaches construct validity and the ecological fallacy more deeply
   than another definition paragraph.

3. **Give every dataset a one-page passport.** Before analysis, the student
   should be able to answer who or what is represented by one row, who is
   absent, how the data were produced, which values mean missing or suppressed,
   whether weights are required, when the snapshot was taken, and which claims
   remain out of reach. This becomes a reusable pre-analysis ritual across the
   entire book and aligns directly with the AI verification protocol.

4. **Publish paired analysis and aggregate views.** The analysis-level file
   supports R and jamovi; the aggregate file supports hand calculation, print,
   and verification. Students should occasionally reproduce the aggregate and
   explain any discrepancy. This makes the downloadable data part of the
   pedagogy rather than a resources-page ornament.

5. **Make “what would change your mind?” a recurring closing move.** Every
   substantial empirical example should name the additional observation,
   design, comparison, or measurement that would materially change the
   conclusion. This is a stronger habit than merely appending a limitations
   paragraph and gives the book an unusually coherent epistemic voice.

6. **Use a two-pass finale without adding a second full worked example.** Keep
   Chapter 18's simulated study because its generating rule can be inspected.
   End with a short transfer challenge in which the reader chooses one bundled
   empirical package and repeats only the question–design–claim audit. The
   contrast between known simulated truth and unknown empirical truth closes
   the book's central promise without overloading the finale.

### File, download, and refresh architecture

One machine-readable catalogue should govern the data layer:

```text
data/
├── katalog.yml
├── dzs-turizam/
│   ├── analiza.csv
│   ├── agregati.csv
│   └── rjecnik.csv
├── dip-izbori-2024/
├── digikat-akteri/
├── eurostat-eu-drustvo/
├── parlamint-hr/
│   ├── parlament_govori.csv
│   ├── parlament_pojmovi.csv
│   ├── parlament_oznake.csv
│   └── rjecnik.csv
└── [later packages]
R/podaci/
├── fetch_dzs.R
├── fetch_eurostat.R
├── fetch_worldbank.R
├── build_*.R
└── validate_data.R
```

The catalogue fields should include at least `id`, Croatian title, disciplinary
domains, unit of analysis, level (micro/aggregate), source URL, source table or
query, source version, retrieval date, licence, redistribution status, refresh
class, analysis path, aggregate path, codebook path, build script, checksum,
known caveats, and chapter consumers. The public `podaci.qmd` page should show a
short generated view; Appendix C should show the full generated record.

Each aggregate percentage must retain its numerator or denominator. Each
survey extract must retain its weights. Original variable codes should remain
beside student-facing Croatian names. Full precision belongs in analysis files;
rounding belongs in displayed tables, not in the stored measurements. Croatian
text should be distributed as UTF-8, and filenames should use stable ASCII
slugs even when labels inside the file use diacritics.

Refresh classes should be explicit:

- **frozen landmark:** Anscombe, Berkeley, a particular election, and any
  replication-results table;
- **pinned edition:** ESS Round 11 edition 3.0, ParlaMint 5.0, ParlaSent 1.0,
  and V-Dem v16;
- **scheduled snapshot:** DZS and Eurostat, refreshed once or twice per year;
- **manual derived snapshot:** DigiKat and any CroAIcon output;
- **external only:** restricted Determ and GFI/FINA source data.

No refresh runs during Quarto rendering. A refresh fetches to a temporary or
raw cache, transforms a small committed file, runs schema and reconciliation
checks, displays a human-readable diff, and only then allows prose numbers to
be updated. At minimum, validation should test primary-key uniqueness, expected
row-count ranges, recognised category and missing-value codes, no mixing of
totals with components, unit/currency consistency, weight presence, and
reconciliation of selected aggregates with the official source.

### Decisions on data already available to the author

- **DZS tourism:** admit immediately as the first bundled empirical package,
  but vendor only compact extracts rather than the full dump.
- **DigiKat aggregates:** admit one stable actor-level snapshot after conversion
  to CSV and completion of its public labels and caveats. Keep the full corpus
  external.
- **GFI/FINA via CroAIcon:** do not connect the book to the remote database and
  do not make its derived aggregates core student practice data. The two
  conflicting codebooks, incomplete coverage, live credentials, and lack of
  reader access make this an excellent provenance or `Statistika u divljini`
  case. A vetted aggregate may support a cited figure if it is clearly labelled
  as derived from restricted-access data and its published method is linked.
- **Existing CroAIcon public-source loaders:** reuse their Eurostat and World
  Bank query logic where appropriate, but move book-specific selections and
  validation into this repository. The book must not depend on another working
  checkout at render time.

### Minimal first empirical release

The first release should remain bounded:

1. Create the single catalogue and validation contract.
2. Add DZS national monthly tourism, one county cross-section, and the
   experimental-platform series.
3. Add one frozen DIP 2024 election extract.
4. Add one dated DigiKat actor extract.
5. Add one compact Eurostat EU-society extract.
6. Add a compact ParlaMint-HR speech extract and its ParlaSent labelled
   companion after fixing the Chapter 17 question and sampling rule.
7. Resolve whether ESS remains portal-mediated or receives explicit permission
   for redistribution before writing chapter prose around a local file.

Only after those packages work across the book, Appendix A, Appendix B, print,
and direct student download should V-Dem, COVIDiSTRESS, or World Bank be added.
This sequence creates disciplinary breadth and design diversity without
turning the textbook into a data-maintenance project.

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
   need source version, persistent URL, exact query or table, variables,
   licence, redistribution status, refresh class, and transformation record.
   “Freely downloadable” must not be treated as permission to rehost. Generated
   data also need an explicit licence rather than “not applicable”. ESS in
   particular requires a deliberate portal-mediated or permission-based route,
   while restricted GFI/FINA and Determ sources must not be presented as
   independently reproducible student data.

### Current standards informing the added recommendations

The [published GAISE College
Report](https://www.amstat.org/education/guidelines-for-assessment-and-instruction-in-statistics-education-%28gaise%29-reports)
continues to emphasise statistical thinking, multivariable reasoning, real data
with context and purpose, active learning, and technology. The ongoing College
GAISE revision is not yet a final standard, but its
[draft learning outcomes](https://community.amstat.org/collegegaiserevision/slo)
explicitly include predictive models, ethical evaluation, communication, and
the connection between data collection and permissible conclusions. The
recommended claim map, real-data portfolio, sensitivity habit, and ethics
thread therefore update the book without chasing a transient software fashion.

The [National Academies' data-science education
report](https://www.nationalacademies.org/projects/DEPS-CSTB-16-01/publication/25104)
supports treating data science as an interdisciplinary combination of
computation, statistics, domain knowledge, communication, and ethics rather
than as a machine-learning catalogue. The [NIST AI Risk Management
Framework](https://airc.nist.gov/airmf-resources/airmf/) supports the proposed
lifecycle emphasis on data suitability, testing, evaluation, validation,
monitoring, and effects after deployment. OpenAI's current
[foundation-model development overview](https://help.openai.com/en/articles/7842364-how-chatgpt-and-the-language-models-are-developed)
supports the bounded explanation of data preparation, pre-training,
post-training, continuing evaluation, and token prediction used to connect data
science with contemporary generative AI.

[AAPOR survey standards](https://aapor.org/standards-and-ethics/best-practices/)
support the proposed treatment of probability and non-probability recruitment,
coverage, response, weighting, wording, and transparent reporting. The
[ASA ethical guidelines](https://www.amstat.org/your-career/ethical-guidelines-for-statistical-practice)
support treating data processing, communication, modelling, deployment, and
effects on data subjects as parts of statistical practice rather than external
professional etiquette.

The European Commission's current
[AI-literacy guidance](https://digital-strategy.ec.europa.eu/en/policies/ai-talent-skills-and-literacy)
also makes the book's AI strand institutionally relevant: Article 4 of the EU
AI Act applies an AI-literacy duty to providers and deployers, while not
prescribing a universal individual proficiency level. The manuscript should
date any legal description and retain its model-independent protocol, because
the durable educational content is specification, provenance, verification,
privacy, consequence, and responsibility.

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

### What the panel cannot supply

**[Assessment]** This review is eight expert perspectives and a set of
deterministic checks. It contains no evidence from a single reader of the
intended audience, and no such evidence exists anywhere in the project. For a
book whose entire argument is that claims should be checked against data, that
absence is conspicuous. Every judgment above about clarity, scaffolding,
cognitive load, and pacing is an expert's prediction of a novice's experience,
which is the least reliable prediction experts make.

The gap is cheap to close and should be closed before Phase 3 rather than
after. A think-aloud pilot with five students on Chapters 1, 8, and 16 — the
opening, the hinge, and the summit, all already developed enough to test —
would report where readers actually stall, which widget controls they misread
or never touch, whether the vignettes land as intended, and which sentences
they reread. It would also settle a number the book publishes prominently and
this review never questioned: the `.chapter-meta` reading times are asserted
per chapter, and nothing in the repository indicates whether they were measured
or estimated. If they are estimates, they are estimates presented without
uncertainty in a book about presenting numbers honestly.

Five readers will not settle a pedagogical dispute, and this recommendation
does not pretend otherwise. Five readers reliably identify the places where a
text fails for reasons neither its author nor its critics can predict. Doing
that before the large Phase 3–5 investment, rather than after the book is
finished, is the most statistically-in-character decision available to this
project.

## 15. Ranked master issue list

### Blockers

1. Correct Chapter 10's permutation-test null and assumptions.
2. Correct Chapter 14's Welch/OLS equivalence claim and implementation.
3. Resolve the licence warning for Navarro-derived material, complete data
   licences, assign an explicit licence to generated teaching data, and decide
   which empirical sources are bundled versus portal-mediated.
4. Ratify chapter spines before declaring the concept system final.
5. Make the release PDF use the project's approved render path and fail safely
   rather than silently retaining an old artifact.
6. Give the book a citable edition before it is assigned to students or cited
   in coursework: a tag, a reader-facing changelog, an archived snapshot with a
   persistent identifier, a citation block, a per-term frozen edition, and a
   public errata route with its log. A continuously mutating text cannot be
   assigned, cited, or publicly corrected.

### Major

7. Develop Chapters 3, 12, and 17 into full arguments, not expanded lists.
8. Add a verified empirical social-science data layer organised by
   data-generating design, while retaining simulations for mechanism discovery.
   The first bounded portfolio should be DZS tourism, DIP elections, DigiKat
   actors, a compact Eurostat extract, a ParlaMint-HR/ParlaSent text package,
   and an explicit ESS access route.
9. Repair assumption and estimand language in Chapters 2, 6–9, 11, 13, 16, and
   18.
10. Ratify the claim map, the book-wide data-science lifecycle, and the seven
    cross-book threads—unit, selection, denominator, uncertainty, consequences
    of error, reproducibility, and communication of a claim—with explicit
    planting, development, harvest, and part-boundary bridges. Treat data
    science as the evidence workflow supporting the four promises, not as a
    fifth promise or a separate algorithm catalogue.
11. Bring the question→acquire→validate→prepare→explore→model→evaluate→
    communicate→monitor lifecycle, construction of the analysis table, and
    missingness into the main text through the preface or Chapter 1 and Chapters
    2, 4, 12, and 18; include one joins/duplication audit and one
    conclusion-level sensitivity to a missing-data decision.
12. Connect the ideal sampling model to survey practice through coverage,
    nonresponse, probability versus opt-in recruitment, weights, and one
    weighted/unweighted ESS or poll comparison. Explicitly distinguish random
    sampling for population generalisation from training/validation/test splits
    for predictive evaluation.
13. Build Chapter 17's text-as-data worked example around corpus construction,
    human/dictionary/AI coding, held-out validation, label construction,
    selective observation, subgroup errors, procedural fairness, and appeal.
14. Add bounded model-reading literacy for binary outcomes, odds ratios, and
    predicted probabilities at the Chapter 16→17 boundary; harvest causal
    diagrams and interaction/heterogeneity literacy in Chapter 16 without
    adding a full logistic- or causal-inference course.
15. Add an assessment closure layer: a planted-error key for every
    `callout-greska`, model answers for the conceptual and critical tiers,
    numerical answers with their checks for the computational tier, and a
    ranked rubric for every `revizija modela`. Ratify the delivery policy —
    in-chapter, solutions appendix, or teaching-edition-only — before Chapters
    3, 12, and 17 are written.
16. Teach the genre the third promise names: one annotated published results
    table as a Chapter 16 harvest, plus a shorter pass over a published results
    paragraph. Reading literacy only; the book must not refit the model.
17. Build the communication thread — estimate with interval, named population,
    claim-type grammar, honest uncertainty, figure-reading prose, and the
    decisive limitation — planted in Chapter 4, developed in 9, 11, and 16, and
    harvested in Chapter 18 where the student writes a report and then audits
    an assistant's version of it.
18. Add golden-values parity tests between every OJS widget and its R print
    twin, and record in the widget registry which twins are exact matches and
    which are distributional.
19. Make one defensible sensitivity comparison standard in sustained empirical
    examples and teach one forest plot in Chapter 12 as evidence-synthesis
    literacy.
20. Complete Appendix A's standalone data path and inferential coverage using
    the same downloadable files and variable names as the chapters.
21. Build Appendix B as a true versioned no-code companion or narrow its claim.
22. Complete Appendix D's decision/recovery aids and add dependence stop rules
    for repeated, clustered, longitudinal, and network-linked observations.
23. Restore the H10 code-reading ladder and remove code-production requirements
    from assessed chapter exercises.
24. Turn the chapter AI boxes into a cumulative verification ladder, complete
    Appendix F's reusable protocol, and source contemporary open-science, AI,
    privacy, and algorithmic claims with primary or official materials. Thread
    ethical responsibility and the distinction among simulation, synthetic
    data, hypothetical model output, and fabricated evidence across the book.
    Define statistics, data science, machine learning, and deployed AI systems
    once, and preserve those distinctions through Chapters 8, 12, 16–18.
25. Replace the duplicated data inventories with one machine-readable catalogue
    that generates the public data page and Appendix C, then synchronize the
    glossary, concept ledger, bibliography metadata, README, and actual source
    use.
26. Run a five-reader think-aloud pilot on Chapters 1, 8, and 16 before the
    identity chapters are expanded, and either validate or correct the
    `.chapter-meta` reading times it tests.
27. Close the 3→4, 12→13, and 17→18 narrative transitions.

### Moderate and minor

28. Add the missing Chapter 5 figure introduction.
29. Give Chapters 7 and 16 explicit midpoint retrieval pauses.
30. Vary recurring widget, worked-example, and AI-box opening formulas.
31. Reassign the ASA episode chiefly to Chapter 10 and give Chapter 3 its own
    public case.
32. Provide static preset data for widget-dependent print exercises.
33. Replace the preface's meta-example with a genuine miniature inquiry.
34. Add a numeracy refresher appendix — percentages against percentage points,
    proportions and rates, the straight line and its slope, the logarithm as a
    change of scale — with marginal `podsjetnik` recalls at first use rather
    than extra explanation inside the chapters.
35. Make one exercise per chapter from Chapter 6 onward reach at least two
    chapters back, and add a short self-check at each part boundary.
36. Verify the book's Croatian terminology against domestic convention, record
    accepted alternatives where usage is divided, and mark deliberate
    departures in the glossary.

## 16. Recommended revision sequence

### Phase 1 — protect correctness and publication integrity

1. Fix Chapters 10 and 14.
2. Correct closely connected major method statements in 8, 9, 11, 13, 16, and
   18.
3. Resolve the project and dataset licences.
4. Pin R and browser-audit dependencies; make PDF production safe and
   fail-closed.
5. Add golden-values parity tests between every OJS widget and its R twin, fix
   any divergence found, and put the check on the release path. Until this
   passes, no number derived from a widget can be trusted to describe both
   editions.
6. Remove `nocite: @*` and complete bibliography metadata verification.
7. Stand up release governance: a tag, a Croatian `CHANGELOG.md` for readers, an
   archived snapshot with a persistent identifier, a *Kako citirati ovu knjigu*
   block, a per-term frozen edition, and a public errata route. This costs a
   day and immediately makes every later phase citable and correctable.

### Phase 2 — ratify the book's intellectual spine

8. Ratify the claim map, one stable data-science lifecycle, and seven book-wide
   threads, then ratify each chapter's small set of load-bearing aspects and
   terms. Record where unit, selection, denominator, uncertainty, consequences
   of error, reproducibility, and communication of a claim are planted,
   developed, and harvested. Ratify data science as a delivery mechanism for
   the four promises rather than a fifth curricular promise.
9. Decide canonical definitions and regenerate the glossary/concept graph. Add
   new definitions only where later chapters genuinely rely on them; do not
   convert the claim map into a glossary of slogans. Verify the Croatian terms
   against domestic convention in the same pass.
10. Ratify the assessment closure policy: what a planted-error key contains,
    what a model answer contains, what a `revizija modela` rubric ranks, and
    which edition carries each. Do this before Phase 3, because the identity
    chapters' exercises are written there.
11. Run the five-reader think-aloud pilot on Chapters 1, 8, and 16, and correct
    the `.chapter-meta` reading times against what it measures. Feed its
    findings into Phase 3 rather than discovering them after it.
12. Give each part a short exit bridge stating what the reader can now claim,
    what remains unavailable, and what the next part adds, followed by a short
    self-check. Make Chapter 18's prerequisites and closing promises reflect
    the resulting dependency graph.

### Phase 3 — build the identity pillars

13. Expand Chapter 3 around one traceable public claim tested through an axis or
    denominator, a base-rate problem, and an AI-produced number.
14. Expand Chapter 12 around one research lifecycle: attractive finding →
    flexibility → selection/incentives → replication → reform → reform limits
    → evidence synthesis through one forest plot → student practice.
15. Expand Chapter 17 around one consequential text-classification decision:
    corpus and unit → human/dictionary/AI label → held-out prediction →
    threshold → confusion table → unequal error burdens → disputed label →
    feedback → language models as prediction systems. Use ParlaMint-HR and
    ParlaSent for the empirical worked example while retaining simulation where
    known truth is necessary.
16. Write each pillar's exercises with its keys and rubrics attached, under the
    policy ratified in step 10.

### Phase 4 — close the high-value statistical-literacy gaps

17. Introduce the question→acquire→validate→prepare→explore→model→evaluate→
    communicate→monitor lifecycle near the preface or Chapter 1, then add the
    constructed analysis-table pipeline to Chapters 2, 4, 12, and 18. Teach
    duplicate units, joins that multiply rows, recodes, filters, suppression,
    and missingness through inspection and one sensitivity check, not through a
    new data-engineering chapter.
18. Extend the Chapter 2→3→8 survey path with coverage, nonresponse,
    probability versus opt-in recruitment, design/nonresponse/post-stratification
    weights, and one weighted/unweighted empirical comparison. Preserve Chapter
    8's simple-random-sampling simulation as the inferential mechanism, then
    distinguish its population-generalisation purpose from the predictive
    purpose of training, validation, and held-out test data in Chapters 16–17.
19. Give Chapters 2, 6, and 16 one stable causal-diagram vocabulary and show why
    adjustment for every available variable can create bias. Keep causal
    estimators outside scope.
20. Add an interaction/heterogeneity harvest and a short binary-outcome bridge
    to Chapter 16. Teach predicted probabilities and cautious odds-ratio reading
    rather than logit derivation or software production, then connect them to
    Chapter 17's classification thresholds.
21. Add the annotated published-results-table walkthrough at the end of Chapter
    16, immediately after the odds-ratio bridge, and the shorter results-
    paragraph pass with it. One real, cited, quoted table; no refitting.
22. Build the communication thread across Chapters 4, 9, 11, 16, and 18, ending
    with the student's own written report and an audit of an assistant's report
    on the same analysis.
23. Make one alternative analytical decision a routine sensitivity comparison
    in sustained empirical examples. Compare estimates, intervals, represented
    populations, and substantive conclusions rather than significance alone.
24. Add the dependence red flag to Chapters 14–16 and Appendix D: shared people,
    organisations, places, periods, or network ties can invalidate ordinary
    independence. Route the reader outward without teaching the excluded model
    families.
25. Thread ordinary statistical ethics and the simulation/synthetic/fabricated
    distinction through dataset passports, chapter examples, Chapter 17, and
    Appendix F. State explicitly that generated respondents cannot support
    empirical population claims. Establish the stable sequence statistics →
    data-science workflow → machine-learning evaluation → deployed AI system,
    including institutional use, monitoring, and feedback.

### Phase 5 — fulfill the data and pathway promises

26. Establish `data/katalog.yml` as the single source for provenance, licence,
    redistribution, refresh, download paths, caveats, and actual chapter use.
    Generate the public data page and Appendix C from it.
27. Publish the first bundled empirical packages in this order: compact DZS
    tourism extracts, one frozen DIP 2024 election extract, one dated DigiKat
    actor extract, one compact fixed-year Eurostat extract, and a linked
    ParlaMint-HR/ParlaSent text package. Give each a student analysis file, a
    codebook, and a small aggregate where useful.
28. Decide the ESS route before depending on it in chapter prose. Either keep
    Round 11 Croatia portal-mediated with a selection recipe and transformation
    script, or obtain explicit permission to redistribute a pinned teaching
    extract. Retain the relevant weights.
29. Build the empirical-data spine by function: DZS/DIP for Chapters 1–3,
    DigiKat/DZS/Eurostat for 4–6, simulations for 7–11, a verified open-data
    lifecycle for 12, ESS for 13–16, and ParlaMint-HR/ParlaSent for Chapter 17.
    Add V-Dem, COVIDiSTRESS, or World Bank only after a chapter demonstrates a
    non-duplicative need.
30. Complete Appendix A and build Appendix B in parallel around identical
    questions, files, variable names, outputs, and verification checks. Derive
    Appendix D from those pathways and the new dependence stop rules.
31. Add the numeracy refresher appendix and its `podsjetnik` recalls, so that
    the no-mathematics-assumed promise is served rather than merely stated.
32. Add aggregate and print-completable alternatives to widget-dependent
    exercises, and finish Chapter 18 with a bounded real-data transfer task
    rather than a second full worked example. Its deliverable should be a small
    reproducible evidence package: dataset passport, source/version record,
    transformation log, analysis, sensitivity check, claim boundary, AI-use
    record, and disclosure.

### Phase 6 — whole-book editorial pass

33. Complete the closure layer for every chapter written before step 10, so
    that keys, model answers, and rubrics exist for all nineteen units.
34. Convert one exercise per chapter from Chapter 6 onward into a
    reach-back task, and verify each part-boundary self-check against the
    ratified threads.
35. Repair 3→4, 12→13, and 17→18 transitions and verify every part-boundary
    claim bridge against the ratified spines.
36. Rebalance recurring cases and repetitive micro-templates, and verify that
    the AI boxes form a genuine competence progression rather than repeated
    prompting advice.
37. Run the six-critic panel again on every substantively changed chapter.
38. Run whole-book continuity, figure, style, evidence, data-reconciliation,
    widget-parity, and deployment checks.
39. Only then consider moving ledger status from `draft` toward `final`, and
    tag the release that carries that status.

## 17. Alternative structures

### Preferred structure — preserve the current order

This is the recommended option. Strengthen the three identity pillars and add
explicit part-boundary transitions. It preserves the successful hinge, summit,
and capstone. Distribute the new analysis-table, survey, causal, heterogeneity,
sensitivity, evidence-synthesis, and dependence literacy through the existing
chapters according to the ratified threads; do not create a sixth part or turn
Chapter 16 into a second methods handbook.

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
the blueprint assigns them. Build a small empirical curriculum rather than a
large dataset collection: probability survey, electoral or administrative
count, official aggregate, digital trace, expert-coded measure, volunteer
sample, unstructured text, and known simulation should visibly permit different
claims. Make Chapter 17's text-as-data case the bridge from measurement to
algorithmic evaluation, not a detached NLP survey. Turn AI literacy into a
cumulative practice of specification, delegation, reproduction, challenge,
documentation, and disclosure. Integrate data science as the visible lifecycle
from question and acquisition through validation, preparation, modelling,
evaluation, communication, and monitoring—not as a fifth promise or a new
algorithm chapter. Define the distinct roles of statistics, data science,
machine learning, and deployed AI systems, and use the Chapter 18 evidence
package to reunite them. Make the constructed analysis table, missingness,
survey selection and weights visible in the main text. Add bounded literacy for
binary outcomes, odds ratios, causal diagrams, interactions, sensitivity,
evidence synthesis, and dependence without opening new method chapters. Use a
claim map and six recurring judgment questions to connect those additions to
the existing arc. Add real social-science data without sacrificing the clarity
of known simulations. Complete the R and no-code reproduction paths. Then align
the glossary, data catalogue, citations, licences, CI, and public metadata with
the manuscript that actually exists.

Four further things follow from the same principle rather than from a longer
topic list. Close the assessment loop: a book that asks nineteen times for a
planted error to be found must say, somewhere, what it planted. Teach the
genres the promises name — the published results table the student will meet in
a seminar, and the honest sentence the student must eventually write and must
be able to demand from an assistant. Verify that the book's two computational
paths, browser and print, actually agree, because a text arguing for
inspectable computation cannot leave its own duplicated implementations
unchecked. And give the book an edition: a tag, a citation, a frozen teaching
snapshot, and a public log of its own corrected errors. The last of these is
the cheapest item in this report and the most exact demonstration of what the
book is arguing for.

One methodological note about this report. It is eight expert perspectives and
a set of deterministic checks, and it contains no evidence from a reader of the
intended audience. Before the large content investment begins, five students
reading Chapters 1, 8, and 16 aloud would tell the project things no panel can,
and would be entirely in keeping with what the book teaches.

**Final verdict:** **a technically sophisticated and pedagogically promising
substantial draft with an excellent central spine, but not yet a trustworthy
final textbook.** The book should remain in `draft` status until the statistical
blockers, identity chapters, empirical data layer, evidence provenance,
cross-book claim and data-science spine, reproduction pathways, and release
governance are closed.

