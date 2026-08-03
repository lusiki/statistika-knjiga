# Agenda and characteristics

*Osnove statistike za društvene znanosti* — what the book is for, what it is,
how well it is doing it, and where the leverage is.

**Written:** 3 August 2026, against the manuscript reviewed in
[reports/comprehensive-book-review-2026-07-31.md](reports/comprehensive-book-review-2026-07-31.md)
and the blueprint in [struktura-knjige.md](struktura-knjige.md).

This document is strategic, not operational. The blueprint says what the book
contains; `AGENTS.md` says how to work on it; the review says what is wrong with
it. This says what it is *for*, and how the work should be prioritised when
everything cannot be done.

---

## 1. The agenda

### The thesis

**The scarce skill has moved, and the book is built for where it moved to.**

When computation was expensive, teaching computation was the point of a
statistics course, and every introductory textbook is still shaped by that
assumption. Computation is now free. It became cheap through software, and then
it became instantaneous through an assistant that writes a correct-looking call
in seconds from a one-sentence description.

What did not become free is the judgment around the computation: deciding what
to compute, knowing what the output is permitted to mean, and being able to tell
whether it is true. The book's wager is that this residue — not the arithmetic,
not the software — is now the entire teachable content of an introductory
statistics course for people who will not become analysts.

The corollary is sharper and is the book's strongest contemporary
justification: **the cost of producing a plausible-looking analysis has
collapsed, so the burden of verification has risen.** This is not an argument
for an AI chapter. It is an argument for a differently-shaped book, and it is
why the AI material is a thread rather than an appendix.

### The wager

A student who never runs a regression but reads one correctly is worth more —
to themselves, to their discipline, and to public argument — than a student who
runs twenty and interprets none.

Most textbooks assent to this in the preface and then organise themselves
around procedures anyway. This one organises around judgment and treats
procedures as instruments. The commitment is structural rather than rhetorical,
and three things prove it:

- reading code is taught as a subject; writing it is never required;
- the fourth exercise tier grades an AI-produced analysis rather than producing
  one;
- "literacy as content" is design principle 3, and Chapters 3, 12, and 17 exist
  only because of it.

### The four promises, restated as claims about the reader's world

The blueprint states four abilities. Underneath each is a factual claim about
what will happen to the reader, and the claim is what justifies the chapter
weight.

| Promise | The claim underneath it |
|---|---|
| Judge statistical claims critically | You will meet such claims weekly, and a detectable share of them are wrong in ways a trained non-specialist can catch. |
| Describe and visualise data honestly | Dishonesty in description is rarely fraud; it is the accumulation of default choices nobody was taught to see. |
| Read and modestly reproduce published analysis | The published literature runs on a small, learnable vocabulary of methods, and its results arrive in a fixed genre. |
| Work with an AI assistant in a disciplined way | You will do this whether or not anyone teaches you. Being taught is strictly better than not being taught. |

### What the book refuses, and why the refusal is content

The out-of-scope list — time series, psychometrics, multilevel models, the
mathematics of machine learning, full Bayesian inference — is a pedagogical
position, not an apology. A book that covers everything teaches that everything
matters equally, which is the opposite of statistical judgment.

Three further refusals are not in the blueprint's list but are just as
load-bearing:

- **The test catalogue.** Chapters 14 → 15 → 16 ascend into one model family
  instead of enumerating procedures. A student who learns the family can place
  a method they have never met; a student who learns the list cannot.
- **The ritual of significance.** Estimation leads, testing is taught with its
  history and its abuses. This is a position in a live disciplinary dispute,
  taken deliberately.
- **Decoration.** Air separates sections, never a box or a shadow; ochre means
  "you can touch this" and is never a data colour; the palette is ordered by
  lightness so the print edition degrades to distinguishable grays. The visual
  system argues the same thing the prose argues.

---

## 2. Characteristics

### Identity card

| | |
|---|---|
| Form | 19 units (preface + 18 chapters), five parts and a finale, six appendices |
| Language | Croatian, for Croatian social-science undergraduates |
| Editions | Web (primary), PDF, print interior, DOCX manuscript, teaching profile with code unfolded |
| Interaction | 17 browser widgets, each with a registered static print twin |
| Target scale | ~86,000 words main text, ~17,000 appendices, 350–380 printed pages |
| Access | Free, continuously deployed, self-published |
| Authorship | Single author, with an automated editorial apparatus standing in for a publishing house |

### The eight characteristics that make it this book

**1. Simulation before formulas — as epistemology, not as a teaching trick.**
Every inferential idea is experienced through resampling before it is named.
The claim is that a reader who has watched a sampling distribution assemble
itself understands something a reader who has been handed σ/√n does not, and
the blueprint states the payoff exactly: the whole apparatus of inference is a
loop. Chapter 8 is where this is proven, and it is the strongest chapter in the
book.

**2. Reading code as a subject, not a skill demanded.** This is the most
original piece of design in the project and it is almost unique in the genre.
The reader never writes R. The reader learns to read it, because reading code
is how a claim becomes checkable. Five patterns exist in the whole book — a
verb chain, a graph specification, a simulation loop, a model call with its
output, and their assembly — each introduced once, in the chapter that needs
it. Part I shows no code at all, because a code block on page twelve answers
"what kind of book is this?" wrongly and permanently. The suspect code in the
error boxes is the same skill in a different mood.

**3. A fixed seven-part skeleton.** Orientation for the reader, and the
project's editorial control surface: a deterministic checker can verify that
every chapter has its vignette, its wild claim, its AI box, and its four
exercise tiers. The cost is that a thin chapter looks structurally complete —
which is currently the book's most misleading property.

**4. Estimation over ritual.** Effect sizes and intervals lead; p-values are
taught with their history. The book takes a side and defends it.

**5. AI in three roles.** Instrument (delegate the computation), fallible
analyst (audit its claims), and object of social-scientific study (algorithms
are classification systems with distributional consequences). Most competing
books have at most the first, and usually only as a tool tip.

**6. Dual-edition discipline.** Every widget ships with a static twin, so the
book does not require a screen and the print reader is not given a degraded
version. This is expensive and rare, and it is the reason the book can be
assigned in a course that meets in a room.

**7. Design as argument.** Black-and-white first, one accent reserved for
interaction, monospace tabular numerals, a measure that never exceeds 66
characters. Every element must survive having its colour removed — which is the
visual restatement of the book's thesis about claims.

**8. A production engine closer to software than to publishing.** Design tokens
with a synchronisation check, a deterministic style linter, a generated concept
graph, a figure-introduction detector, a citation resolver, CI deployment, a
six-critic review panel, and machine-readable exports so that a reader's own
assistant answers from the book's text. A single author with this apparatus
approximates an editorial team.

---

## 3. How the book is executing its purpose

Graded by mechanism, against the evidence in the review rather than against
intention.

### Executing well

**The inferential arc (7 → 8 → 9 → 10 → 11) is doing exactly what it was
designed to do.** Repeated randomness becomes a sampling distribution, becomes
an interval, becomes a null world, becomes a question about magnitude. Each
chapter consumes the previous one's machinery rather than restating it. This is
the part of the book that would survive any review panel, and it is the
strongest argument that the simulation-first design is correct rather than
merely fashionable.

**The model-family ascent (14 → 15 → 16) defeats the test catalogue.** By the
time the reader reaches regression, two-group and multi-group comparison have
already been revealed as the same object. This transfers; a list does not.

**The dual-edition system holds.** All 17 widgets have registered twins, the
design tokens synchronise, and both HTML and PDF deploy from the same source.

**The editorial apparatus is not decorative.** Zero deterministic style
violations, all 36 cited keys resolve, no fabricated citation or number found
under audit. In a book whose subject is unverifiable claims, that result is
load-bearing.

**The voice works.** One Croatian author throughout, deriving authority from
limiting claims rather than issuing verdicts, with no patronising mathematics
register.

### Executing poorly

**The three chapters that justify the book's existence are its three thinnest.**
Chapters 3, 12, and 17 stand at 11–14% of planned length against a book-wide
51%. This is the single most important fact about the current manuscript. The
answer to "why this book rather than another introductory statistics text?" is
Chapters 3, 12, and 17 — and those are precisely the chapters that currently
read as briefing notes. The book's differentiation exists as an intention and a
skeleton, not yet as prose.

**A book about reading real research runs mostly on simulated data.** The
simulations are correct and pedagogically necessary where truth must be known,
and should stay. But principle 3 — literacy as content — cannot be delivered by
data whose generating process the author wrote. The empirical layer is planned
and absent.

**The fourth promise's main assessment instrument has no answer.** Nineteen
planted-error boxes and nineteen model-audit tasks exist; no key, rubric, or
statement of the intended error exists anywhere. A reader working alone cannot
find out whether they succeeded at the exercise that most directly serves the
promise the book is proudest of.

**Two statistical statements are wrong** in Chapters 10 and 14, both inside
worked examples, both in the sequence the book is otherwise best at.

**The alternative pathways are advertised and unbuilt.** Appendix B promises a
parallel no-code route and delivers an orientation note; Appendix A fails at its
first sustained dataset because the loading step is missing.

**Nobody has tested it on a reader.** Eight expert perspectives, zero students.

### The pattern behind the failures

The engine has outrun the manuscript. Everything that could be automated is
finished and working; everything requiring an author's sustained argument sits
near half. The failures are not distributed randomly across the book — they
cluster precisely where a machine cannot help.

That diagnosis has an immediate consequence for how time should be spent: the
project does not need more tooling. It needs prose, and specifically the prose
that only this author can write.

---

## 4. Why the book is good

**It has a thesis, and the thesis is correct.** Most introductory statistics
textbooks have a table of contents where an argument should be. This one is
organised around a defensible claim about what has become scarce, and the claim
survives contact with how students and researchers actually work in 2026.

**The central sequence is demonstrated, not asserted.** Chapter 8 is evidence
that the design works; it is not a promise that it will.

**It takes positions and pays for them.** Estimation over ritual, no test
catalogue, code as reading, a declared out-of-scope list. Each position closes
off an easier book. A textbook that refuses things is one whose author has
thought about the reader rather than about coverage.

**It is honest under audit.** Disciplined uncertainty language, no invented
citations, out-of-scope stated in the preface and not smuggled back. For a book
whose subject is claims that cannot be checked, passing its own check matters
more than it would elsewhere.

**Prose, design, and infrastructure argue the same thing.** The insistence that
every element survive the removal of colour, that numerals be tabular, that
code be readable and never required, and that computation stay inspectable are
one commitment expressed in four materials. That coherence is rare and readers
feel it even when they cannot name it.

**It respects its reader.** No mathematics anxiety theatre, no apologising for
the subject, no pretending the material is easier than it is. The register
assumes an intelligent adult who was not taught this.

---

## 5. Advantages

### Structural — the strongest and least fragile

**There is no incumbent.** A free, web-native, interactive, AI-aware statistics
textbook in Croatian for social-science undergraduates has no competitor. The
alternatives are expensive translated textbooks with foreign examples and dated
technology, or lecture notes. This is not a marginal advantage over a rival
product; it is an empty field.

**Domestic examples no translated book can offer.** DZS, DIP, ESS Croatia,
ParlaMint-HR. A Croatian student arguing about Croatian turnout with Croatian
data is in a different relationship to the material than one working through
American crime statistics.

**Free and web-first removes adoption friction entirely.** No procurement, no
edition mismatch, no student deciding whether to buy it.

### Temporal — real, and decaying

**It was written at the moment AI became universal in student work.** Incumbent
textbooks can bolt on a chapter; they cannot re-shape themselves around the
change. That advantage is worth perhaps two or three years, after which
AI-aware becomes table stakes and the durable content is the protocol —
specification, provenance, verification, disclosure — rather than the novelty.
The book should bank this advantage now and design the AI material so that its
value survives the moment.

### Pedagogical

**Simulation-first plus browser widgets is genuinely better for this audience**
than formula-first, and the book commits to it rather than gesturing at it.

**The code-reading ladder solves a problem most books do not pose.** How do you
make computation inspectable to a reader who will never write any? Five
patterns, each introduced once, taught as reading. It is a better answer than
either "no code" or "learn R first."

**The model family transfers; a test list does not.**

### Production

**One source, many outputs.** Web, PDF, print, Word manuscript, teaching
edition with code unfolded, lecture decks, machine-readable exports. Each
additional format costs a filter, not a rewrite.

**Quality is enforced rather than hoped for.** Deterministic checks catch what
checks can catch, and the critic panel structures what they cannot.

**The AI exports are a real differentiator.** A reader's assistant answering
from the book's own text is both a genuine feature and a demonstration of the
book's argument about assistants.

### Institutional

**It already has a reason to exist.** The book is the backbone of a live course,
so it has a captive readership, a natural test population, and a use even if it
is never formally published.

---

## 6. Liabilities

An agenda that lists only advantages is marketing. These are the risks that
should be managed rather than discovered.

**Single author, and the remaining half is the harder half.** The 43,000 words
written are the chapters that port from existing course material. The 43,000
remaining are disproportionately the ones that must be written fresh, argued
rather than transcribed, and sourced.

**The empirical data layer is a permanent maintenance commitment.** Every
bundled dataset is a future refresh, licence re-check, schema validation, and
reconciliation of every number quoted in prose. The review's governance cap —
about six bundled packages — is not bureaucracy; it is what keeps a textbook
from becoming a data-maintenance project.

**The AI material has the shortest shelf-life in the book.** Mitigation is
already identified: keep the protocol model-independent, date every
product-specific claim, and freeze AI-output snapshots where a stable
comparison is required.

**False completeness is currently deceiving everyone, including the author.**
The skeleton makes a 537-word chapter look structurally identical to a
3,600-word one. Word counts against blueprint targets should be visible in the
ledger, not discoverable only by audit.

**The book is currently unassignable and uncitable.** No tag, no edition, no
citation instruction, no errata route. A lecturer cannot assign a version that
will still say the same thing at the exam.

**Scope creep is the live danger.** The review proposes 36 items. Adopting all
of them uncritically would produce a longer, later, less coherent book. The
book's own scope discipline must be applied to its improvement plan — which is
the point of the next section.

---

## 7. How the book can be improved

Ranked by leverage rather than by severity, and organised by what each tier
buys. The review's numbered list is the operational form of this; the ordering
below is the strategic one.

### Tier 1 — make it trustworthy (without this, nothing else matters)

Two wrong statistical statements, an unresolved licence, and no citable
edition. None is large; all are disqualifying. A textbook that is wrong about
permutation tests cannot be recommended regardless of how good its Chapter 8
is, and a book that cannot be cited cannot be assigned.

This tier is days of work, not months, and it should be finished before
anything in Tier 2 begins.

### Tier 2 — make it *this* book (the highest-leverage work in the project)

**Write Chapters 3, 12, and 17.**

If nothing else happens in the next six months, this should. Every advantage in
section 5 is an advantage of the book those three chapters describe. Right now
they describe it in outline while the surrounding chapters deliver a competent,
well-made, but not unprecedented introductory statistics text. The gap between
what the book is and what the book is *for* is almost exactly these three
chapters.

The review's shapes for them are right and should be followed: one traceable
public claim for Chapter 3; one research lifecycle for Chapter 12; one
consequential text-classification decision for Chapter 17. Each is a single
extended argument rather than an expanded list, which is what "at 13% of target"
actually means — not that words are missing, but that the argument was never
made.

### Tier 3 — make the four promises true

Each promise currently has one identifiable gap between what is claimed and
what is delivered.

| Promise | The gap | The bounded fix |
|---|---|---|
| Judge claims critically | Runs on data the author generated | The empirical portfolio, organised by data-generating design, plus the claim map that labels what each example licenses |
| Describe data honestly | The analysis table arrives already clean | The constructed-table thread and missingness as information, through Chapters 2, 4, 12, 18 |
| Read published analysis | The genre itself is never shown | One annotated published results table as a Chapter 16 harvest, plus the odds-ratio reading bridge |
| Work with AI in a disciplined way | The main assessment has no answer key, and the AI boxes repeat rather than accumulate | The closure layer, and the AI ladder where each chapter adds one failure mode |

The fourth row is the cheapest and the most urgent, because the closure layer
becomes dramatically more expensive once Chapters 3, 12, and 17 are written.
Ratify the policy before Tier 2, write the keys during it.

The book should also, at some point in this tier, teach the writing of an
honest sentence. It teaches the auditing of claims thoroughly and the making of
one nowhere, which is a strange asymmetry in a book that ends by asking the
student to write a report and to judge an assistant's version of the same
report.

### Tier 4 — make it durable

Widget/print parity tests, the single machine-readable data catalogue, pinned R
dependencies, the errata log, and five students reading Chapters 1, 8, and 16
aloud before the large content investment rather than after it.

The reader test is the item most likely to be skipped and the one most in
keeping with what the book teaches. Five readers will not settle a pedagogical
dispute, but they reliably find the places where a text fails for reasons no
author or critic predicts.

### What to resist

- **New chapters.** Every gap identified so far is a thread through existing
  chapters. Six parts would be a worse book than five.
- **More datasets than the cap allows.** Design diversity beats topical breadth;
  one well-chosen survey touches all five disciplines, and five simulations
  teach one epistemic lesson.
- **Version-specific AI material** in the conceptual spine.
- **The embedded tutor**, until the exports have proven they deliver most of its
  value at none of its cost.
- **More tooling.** The engine is ahead of the manuscript. Every hour spent on
  infrastructure is an hour not spent on the only thing that is actually behind.

### One strategic question the review does not raise

The 86,000-word target is an assumption inherited from the blueprint, not a
requirement. It is worth asking explicitly whether a **complete 60,000-word
book beats an incomplete 86,000-word one.**

The argument for the shorter target: the book's value is concentrated in
coherence and judgment, not coverage; several chapters are already at 68–80%
and could be declared finished; and a complete first edition can be taught,
cited, corrected, and revised, while a permanently half-finished one cannot.
The blueprint's per-chapter targets were set before any of the prose existed
and were never validated against how much space these arguments actually need.

The argument against: the three pillars genuinely need their planned length,
because their deficit is argument rather than padding, and cutting the target
must not become a way of shipping them thin.

The synthesis is probably: **hold the target for Chapters 3, 12, and 17, and
treat every other chapter's target as an estimate the finished prose is allowed
to overrule in either direction.** That converts the completion percentage from
a debt into a measurement, which is more in keeping with the book's own
teaching than chasing a number set in advance.

---

## 8. The one-sentence version

A Croatian statistics textbook for people who must read research rather than
produce it, built on the claim that computation has become free while judgment
has not — currently the best-engineered and second-best-written half of an
unusually good book, whose three most distinctive chapters are also its three
emptiest, and whose next six months should be spent almost entirely on writing
them.
