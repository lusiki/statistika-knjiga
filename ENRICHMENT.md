# Substantive enrichment guide — Osnove statistike za društvene znanosti

Companion to [STYLE.md](STYLE.md). `STYLE.md` governs *how* to write. This
guide governs *what* to add when a chapter feels under-developed.

## What this document does

Defines how to thicken a chapter with one- or two-paragraph insertions that add
substantive value, rather than uniform expansion or restatement. Use it whenever
a chapter has content gaps and you want to fill them without diluting it.

## Hard constraint

**No invented empirics.** Every number, study, effect size, sample size or
finding introduced by an insertion is cited against `references.bib`. If the
source is not in the bib, propose adding it and wait; never draft the paragraph
around a remembered figure. This is stricter than in an ordinary textbook,
because this book's own subject is claims that cannot be checked.

Croatian empirical examples are welcome but must be verifiable — a named survey
wave, a DZS or Eurostat table, a published paper. A plausible-sounding domestic
example with no source is exactly the failure chapter 3 teaches readers to spot.

## The five value slots

Every insertion fills **exactly one** slot. If the candidate addition does not
fit a slot, it is restatement and gets cut.

1. **Mechanism unpacking.** The chapter states a result but skips why it holds.
   Add the step-by-step *how*. In this book that usually means showing what the
   procedure is actually doing to the data, not deriving it. The most common
   asymmetry — results without their gears.

2. **Empirical evidence.** The claim leans on intuition. Add the cited finding
   from published social-science research, with its magnitude and its
   uncertainty.

3. **Comparative / methodological context.** Place the procedure against its
   neighbours. When does the alternative do better, what does it assume that
   this one does not, why did the field settle where it did. One sentence of
   comparison often outperforms a paragraph of abstract argument.

4. **Failure mode / counterview.** The chapter presents a procedure as it works.
   Add the conditions under which it breaks, the assumption that quietly does
   the work, or the principled objection. Statistics especially demands this —
   almost every procedure in the book has a well-known way of misleading.

5. **Interpretation note.** Explain what the reader is entitled to conclude from
   a result, and what they are not. What the number means to a person who has
   to act on it. Raises the chapter's epistemic floor and is the slot most
   directly aimed at the book's first promise.

## Asymmetry test — where to add

Scan the chapter for points where:

- A procedure is introduced but never unpacked
- A result is stated but the mechanism is implicit
- A method is presented but no empirical study using it follows
- A procedure is taught but its failure mode is absent
- A number is produced but its interpretation is left to the reader
- A formula appears without an intuition before it (that is an H9 repair, not
  an enrichment — fix it as style, not as substance)

Each such point is a candidate. Each gets one or two paragraphs filling the
appropriate slot. **Not generic expansion.**

## Constraints on every insertion

- One to two paragraphs per insertion, never more
- Croatian (hr-HR), conforming to [STYLE.md](STYLE.md) — no colons in prose, no
  mid-sentence em-dash list intros, no mechanical takeaway formulae, no
  restatement connectives, no meta-callouts in flowing text
- Cite via `[@key]` against [references.bib](references.bib); if a source is not
  in the bib, flag it rather than fabricate
- Respect S8: if the insertion introduces an idea, the intuition or simulation
  comes before the formalism
- **Substantive test:** would a reader who already understood the chapter learn
  something new from this paragraph? If not, cut it

## Anchoring in the literature

The five slots describe *what kind* of value an insertion adds. This section
describes *what sources* it should engage with. A statistics textbook for social
scientists gains depth when it sits in dialogue with the methodological debates
its readers will meet in journals, not only with the procedures.

A non-exhaustive map of which literatures speak to which chapters. Verify every
key against `references.bib` before drafting.

- **Measurement, design and validity** (ch. 2) — classic psychometric and
  survey-methodology treatments; the causal-inference literature for the
  confounding seed.
- **Statistical literacy and graphical honesty** (ch. 3, 5) — the visualisation
  literature and the risk-communication literature on base rates.
- **Estimation and resampling** (ch. 8, 9) — the bootstrap literature and the
  "new statistics" argument for intervals over tests.
- **Testing and its critics** (ch. 10, 11) — the long history of objections to
  null-hypothesis testing, the ASA statement, and the power literature.
- **Replication and reform** (ch. 12) — the replication projects, the
  forking-paths and false-positive papers, preregistration and registered
  reports.
- **Algorithms, fairness and prediction** (ch. 17) — the prediction-versus-
  explanation debate, the impossibility results on fairness definitions, and the
  literature on recommender systems as social infrastructure.
- **AI in research practice** (ch. 3, 12, 18, Dodatak F) — the emerging
  literature on fabricated papers, paper mills, and machine-assisted
  reproducibility checking. This literature moves fast; check publication dates
  and prefer the most recent survey.

Do not invent page numbers, fabricate findings, or claim that a paper argues a
position you are not certain it actually argues. If unsure, name the claim and
ask before committing the citation.

## Workflow

1. **Read** the target chapter top to bottom.
2. **Mark** candidate asymmetric points per the test above.
3. **Identify** the appropriate slot (1–5) for each marked point.
4. **Draft** a one- to two-paragraph insertion per point. Bound the candidate
   set to the strongest two to four per chapter; if there are more, rank and
   present the best.
5. **Present** for review *before any file edit*. For each insertion show the
   slot label, the anchor point, the draft prose, and the citation key. Also
   list one or two candidates considered but rejected, with the reason.
6. **Apply** after approval.
7. **Verify** with `quarto preview chapters/<file>.qmd` — the chapter still
   renders, citations resolve, callouts display correctly.

## Provenance

- **2026-07-29** — Adapted from the enrichment guide of *Javne politike u
  Hrvatskoj*. Slots 3, 4 and 5 re-specified for a methods textbook
  (comparative → methodological context, trade-off → failure mode,
  identification note → interpretation note), the hard constraint changed from
  "no Croatian empirics" (a co-author reservation that does not apply here) to
  "no invented empirics", and the literature map rebuilt around this book's
  chapters.
