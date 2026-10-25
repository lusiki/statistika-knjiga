# Uputa za urednički prolaz „podatkovna nit”

Brief for a separate editorial pass on how the book introduces, reuses and
connects its datasets. Prepared on 2026-10-25 from a full read of all 19
chapters, the data catalogue, the ratified spines and the three most recent
editorial passes. Instructions are in English. Every sentence added to the book
is written in Croatian (hr-HR).

---

## 0. Purpose and diagnosis

**Goal.** At every point in the book the reader knows which dataset they are
looking at, who made or published it, what one row is, what it cannot support,
and how it connects to what they saw earlier. No analysis result changes in
Stage 1.

**Diagnosis (established 2026-10-25).**

1. Two simulated sets carry the computation. `populacija_medija` (50.000
   imagined adults, seed 8001) is the known truth for Parts III–V. `anketa_mreze`
   (300 imagined respondents, seed 4001) carries Part II and returns in
   Chapter 18. Observed sources enter at fixed points: Berkeley (1, 2, 13),
   DIP 2024 (3), DigiKat (4, 5, mentioned in 16), Eurostat (6), ESS Round 11
   (8, optional exercise only), the 17-lab facial-feedback RRR (12), the
   Kleppang/Ungdata table (16, inside a divljina box), ParlaSent (17, 18).
2. Parts IV–V draw a new sample from `populacija_medija` in almost every
   chapter: 300 print and portal readers (10), all print and portal readers
   (11), 800 people (13), 120 TV and social-media users (14), 300 people across
   five sources (15), then the full population plus reuse of the 14 and 15
   samples (16). The prose seldom says why a new sample is drawn, and nowhere
   says that these chapters are answering one substantive question about media
   trust, news source and age. The Part V spine already ratifies that one
   person-level dataset is reused across model families
   (`notes/reports/g-a2b-v-spine-decision-2026-08-05.md`, lines about 60–110).
3. Observed datasets enter without one sentence saying what they show that the
   simulated sets cannot.
4. The field balance leans toward media and communication. DZS tourism is
   bundled and unused in chapters. The GDP long series, the state-aid register
   and V-Dem are registered but blocked.
5. Hygiene. Chapters 7–8 give willingness to pay in kuna. Chapter 10 and 11
   draws lack catalogue teaching variants. The Chapter 12 lab file is not in
   `data/katalog.yml`, which calls itself the sole machine-readable data
   record. Some `consumer_sources` lists do not match actual use.

**Two stages.** Stage 1 (this thread) implements communication and hygiene
changes that existing rules already require, and writes decision proposals.
It ends with a stop. Stage 2 runs in a later thread, only for the proposals the
author approves by name.

---

## 1. Authority, governance, branch, environment

1.1 **Authority.** This is a separate editorial pass under the author's direct
instruction. Quote the launching message verbatim in the report's
`authorization` field. It follows the same mode as
`notes/reports/divljina-revision-2026-10-21.json`,
`notes/reports/humanization-full-2026-10-24.json` and
`notes/reports/literature-redaction-2026-10-25.json`. It is **not** a
comprehensive-review packet and claims no gate.

1.2 **Do not modify** the four comprehensive-review control files
(`notes/reports/comprehensive-review-implementation-plan-2026-08-03.md`,
`comprehensive-review-implementation-register.yml`,
`comprehensive-review-forward-handoffs.yml`,
`comprehensive-review-dashboard.md`). Do not modify the Bookwright shared
registries in `bookwright_plugin/bookwright/shared/` (`chapter-ledger.json`,
`chapter-spine.json`, `concept-ledger.json`, `conventions.json`) or any chapter
stage. Read only the dashboard's "Current state" table to confirm that
`P6-VERIFY` still holds the sole write lock and that `next_permitted_packet` is
null. If that has changed, stop and ask the author before editing.

1.3 **Branch and worktree.** The main checkout at
`C:\Users\lsikic\Desktop\Statistika` may hold another session's uncommitted
work. Never edit, stage, stash or switch branches there. Create an isolated
worktree from the latest `origin/main`:

```powershell
git -C C:\Users\lsikic\Desktop\Statistika fetch origin
git -C C:\Users\lsikic\Desktop\Statistika worktree add C:\Users\lsikic\Desktop\Statistika-podatkovna-nit -b copy/podatkovna-nit-<YYYY-MM-DD> origin/main
```

Confirm that `origin/main` contains `f207745` (PR #13, "refine examples and
interval reasoning", which changed Chapters 9, 12 and 13). Work only in the
worktree. Copy this brief from
`C:\Users\lsikic\Desktop\Statistika\tmp\podatkovna-nit-uputa-2026-10-25.md`
into the worktree as `notes/reports/podatkovna-nit-uputa-2026-10-25.md`. It is
the instruction record and is committed with the pass.

1.4 **Commits** are local and scoped (§9). Push, pull request, merge, tag and
deployment each need a separate explicit approval from the author in chat.

1.5 **Environment.** Shell is PowerShell. Invoke R only through
`python bookwright_plugin/bookwright/scripts/run_rscript.py <script.R> [args]`.
For R processes set `$env:LC_ALL = 'English_United States.utf8'` and
`$env:LANG = 'English_United States.utf8'` (the inherited `C.UTF-8` is not a
valid Windows locale). If renv does not load, record it in the report and do
not claim a clean production reproduction. Build the PDF only through
`scripts/render-book-pdf.ps1`, never with a bare `quarto render --profile pdf`.
The worktree uses Git's LF bytes, so compute every generated route hash there,
not in the main checkout.

---

## 2. Read completely before the first edit

1. `AGENTS.md`
2. `STYLE.md`, all of it. In particular: H1 (no colons in prose), H4, H5, H7
   (including the 2026-10-25 rule that teaching datasets carry no author-year
   self-citation), S6 (cross-references name the topic, not the number), S10;
   the Structural elements sections Vinjeta, Statistika u divljini, Nađite
   grešku, Zadaci; the Provenance entries dated 2026-10-12, 2026-10-20,
   2026-10-21, 2026-10-23 and 2026-10-25.
3. `ENRICHMENT.md` (needed for proposals P2 and P3).
4. `notes/struktura-knjige.md`
5. `data/README.md`, `data/katalog.yml` (all packages and every
   `teaching_variants` block), `data/katalog.schema.json`
6. `R/podaci-nastavni.R`, `R/setup.R`
7. The spine decisions `notes/reports/g-a2b-*-spine-decision-*.md`, the
   identity briefs `g-a4-03`, `g-a4-12`, `g-a4-16`, `g-a4-17` decision packages,
   and `g-a3-dzs-selection-decision-2026-08-05.md`,
   `g-a3-ess-selection-decision-2026-08-11.md`
8. The three recent pass reports named in §1.1. Copy their report structure.
9. `scripts/build-appendix-c-views.R`, `scripts/build-print-apparatus.py`
   (section "Dva nastavna skupa podataka"), `scripts/check-teaching-variants.R`
10. Every chapter `chapters/00-predgovor.qmd` … `chapters/18-vase-prvo-istrazivanje.qmd`
    in full, both the HTML and PDF `content-visible` blocks.

---

## 3. Hard boundaries for Stage 1

3.1 **Frozen regions.** These stay byte-identical. §8.3 proves it with hashes.

- every `::: {.callout-divljina}` block (author revision 2026-10-21; Chapters
  12 and 13 changed again in PR #13 on 2026-10-25);
- every `::: {.callout-greska}` block and its separated check (author revision
  2026-10-21);
- every widget block, every print twin, `data/widgets.json`, and every
  `set.seed(...)` line in the book;
- every `#def-` block, every Sažetak and Pojmovi section, and all four exercise
  tiers under Zadaci;
- the vignette of Chapter 10 (the ASA episode is ratified as
  `R31-C10-ASA-home`).

3.2 **No result changes.** No resampling, no seed changes, no generator
changes, no new datasets, no network retrieval of data, no rights requests
sent, no promotion or lane change in `katalog.yml`, and no new citation keys.
Stage 1 adds zero entries to `references.bib`.

3.3 **No hand-typed numbers in new prose.** Every number in a new sentence is
either a design constant already stated nearby (a sample size, the 1–10
scale) or an inline `` `r ...` `` expression over an object the chapter
already computes.

3.4 **Style.** Every new sentence obeys H1–H10 and S1–S10. No lists in running
prose, no meta-structural announcements, no colons in prose, no new callout
types, no metadata strips, no raw HTML.

3.5 **Spine constraints.**
- Chapters 14 and 15 must not reveal that the two-group difference, the
  comparison of several groups and regression are one model. That discovery
  belongs to Chapter 16 (Part V contract).
- Chapter 3 keeps one traceable public claim (DIP 2024). No second dataset
  enters Chapter 3's body.
- Chapter 12 keeps one research and reform lifecycle; Chapter 17 keeps one
  text-classification decision.
- The preface keeps its ratified nine aspects and twelve exclusions
  (`g-a2b-preface-spine-decision-2026-08-04.md`).

3.6 **Word budget.** Net additions of at most 150 words per chapter and at most
1.500 words across the book. Count them with the method recorded in
`literature-redaction-2026-10-25.json` (`word_count.method`).

3.7 **Generated files are never hand-edited.** These are
`dodaci/c-katalog-podataka.qmd`, `podaci.qmd`, `rjesenja.qmd`,
`assessment/print-checks.md`, `config/appendix-*-route.json`,
`data/ai-exports.json`, `docs/`, `_freeze/` and `pdf/`. Regenerate them with
their scripts (§6).

---

## 4. Stage 1 work items

### W0 — Baseline

Before any edit, run the full ladder in §8.1 on the untouched worktree. Record
each command's status and evidence as `checks.baseline`. Any failure already
present is pre-existing (one is likely: full manuscript integrity expected two
AI boxes after the 2026-10-20 STYLE decision; confirm whether it still fails).
Every new failure after your edits is this pass's responsibility.

### W1 — Data-use audit (evidence only, no edits)

Build a table `data_use_audit` for the report with one row per chapter and
dataset or draw. Cover the preface (both editions), all 18 chapters, and
Appendices A and B where they reintroduce a dataset. Start from §10.1 and
verify everything against the worktree.

Columns:

- chapter; catalogue id, or `konstruirani primjer` for hand-built examples;
- kind (simulated, observed, constructed);
- object name in R; seed; n; selection rule;
- first-use line and the line range of its introduction;
- the four-part introduction check, each part `pass` or `missing` with the
  quoted Croatian evidence:
  - **izvor**: who made or published it, and whether it is simulated;
  - **jedinica**: what one row is;
  - **varijable**: which variables this chapter uses;
  - **granica tvrdnje**: what the data cannot support;
- every later return, with its line and the two-part return check:
  - **koji zapisi**: the same records, a new sample from the same population,
    a subset, or the whole population;
  - **zašto**: why this choice, if the text gives a reason.

Acceptance: every use listed in §10.1 has a row. Every `missing` becomes a W2
or W3 task, or a recorded "no fix" with its reason.

### W2 — Complete the first-use introductions

For each first use in a chapter that misses one of the four parts, add the
missing part in continuous prose before the first calculation. That is where
STYLE.md's Vinjeta section requires it. Add at most one sentence per missing
part, and never repeat what is already there.

- Simulated sets need the dataset name, the fact that it was generated for
  teaching, that one row is one imagined person, the variables used in this
  chapter, and the boundary that it does not describe real residents.
- Observed sets need the publisher, the version or date as recorded in the
  catalogue, the unit, the variables, and the boundary from the catalogue's
  permitted and unavailable claims.

Known candidate: Chapter 10 does not state the 1–10 trust scale. Verify it.

### W3 — Name the samples and standardise returns

3.1 **Stable descriptive names in prose.** Introduce each name at its draw and
reuse it word for word at every return. Adjust only grammatical case. These
are prose names; do not rename any R object.

| Chapter | R object | Croatian name |
|---|---|---|
| 9 | `s9_uzorak` | uzorak od 200 osoba |
| 9 | `s9_mali` | uzorak od 60 osoba |
| 10 | `s10_uzorak` | uzorak od 300 čitatelja tiska i portala |
| 11 | `s11_pod` | svi čitatelji tiska i portala u populaciji |
| 13 | `s13_uzorak` | uzorak od 800 osoba |
| 14 | `dvije_skupine` | uzorak od 120 korisnika televizije i društvenih mreža |
| 15 | `pet_izvora` | uzorak od 300 osoba s pet izvora vijesti |

3.2 **At each new draw**, add one sentence saying what the draw is relative to
earlier ones: a new draw from the same population and not a subset, which
sources it is restricted to, and how large it is. Give the reason for the draw
only where it follows from the chapter's own analysis or the catalogue's
`transformation` text. Example: Chapter 13 needs enough people for twenty age
and source cells. Where no reason is documented, state what the draw is and
list it in the report under `razlog_izvlacenja_nije_dokumentiran` for the
author. Never invent a rationale.

3.3 **At each return**, add one clause naming which familiar records are being
reused. This includes Chapter 16's reuse of the 14 and 15 samples, Chapter
18's return to `anketa_mreze`, and Chapter 13's return to Berkeley.

Acceptance: every W1 row passes both checks, and a grep shows each name used
consistently across chapters.

### W4 — The running question in Chapters 10–16

The simulated population answers one substantive question across Parts IV and
V. The catalogue words it as "Kako se povjerenje u medije mijenja s dobi i
izvorom vijesti?" (`populacija_medija.question`). Add at most one short paragraph (two to four sentences) in
each of Chapters 10, 11, 13, 14, 15 and 16, placed where the population or
sample is introduced or reintroduced. The paragraph does two things.

1. It states what earlier chapters established about that question in this
   simulated city. State it qualitatively, or with inline values from objects
   the chapter already computes.
2. It names which part of the question this chapter adds: a difference between
   two sources and its uncertainty (10), its size and the power to detect it
   (11), dependence of source on age (13), the difference between two sources
   as an estimate with an interval (14), all five sources together (15), and
   age and source jointly (16).

Rules:
- The paragraph is about the substantive question, not a method recap.
- Estimation comes first.
- S6 applies.
- The Part V exclusion in §3.5 applies to Chapters 14 and 15.
- Chapter 16 already opens with "Polazimo od svih 50.000…". Integrate the
  harvest sentence there and do not duplicate it.
- Confirm that Chapter 18's return to `anketa_mreze` names Chapters 4–6 by
  topic.

Acceptance: the arc critic (§7) confirms that the thread reads as one
investigation and that no part of Chapter 16's synthesis is spent early.

### W5 — A reader-facing map of the datasets

5.1 **Preface, both editions.** In the PDF block (about lines 61–70) and the
HTML block, write one prose passage of at most 120 words per edition. It
names the two simulated sets as a pair, names the observed sources as a group,
and promises that each dataset is introduced at its first use and named at
each return. Check the preface exclusions first. If the passage would breach
one, skip it and report.

5.2 **Appendix C and `podaci.qmd`.** Add a generated "Karta uporabe" view: a
dataset × chapter table with draw names and variant ids. Produce it with
`scripts/build-appendix-c-views.R` from `katalog.yml` (`consumer_sources` and
`teaching_variants`). Change `scripts/check-appendix-c.py` only if its
expected structure requires it, and record why.

Acceptance: the map lists every chapter use in W1 and nothing else.

### W6 — Say why each observed dataset is real

At the first body use of each observed source, make sure one sentence states
what it shows that the simulated sets cannot. Base it on the catalogue `role`
field. Add the sentence only where it is absent, and never inside a frozen
box. Targets:

| Chapter | Source | What only the real data shows |
|---|---|---|
| 1 | Berkeley | a record of decisions that was not made for research; the composition of applications |
| 3 | DIP 2024 | an official numerator and denominator; coverage of the electoral units |
| 4 | DigiKat | a skewed distribution of sources; an instrument that does not cover every platform equally |
| 6 | Eurostat | comparability across countries, quality flags, the ecological fallacy |
| 12 | 17-lab RRR | how far estimates spread across laboratories |
| 17 | ParlaSent | the human label as a fallible reference outcome |

Skip Kleppang (Chapter 16), because it sits inside a frozen divljina box.

### W7 — Catalogue hygiene (`data/katalog.yml`)

7.1 **Missing teaching variants.** Add variants for draws that a chapter's
analysis relies on and that have no entry. Read the exact code before writing
each `transformation`. The draws are:

- Chapter 10 main sample (seed 1011, n = 300, print and portal only);
- Chapter 10 calibration sample (seed 1010, random A/B labels);
- Chapter 11 subpopulation (`kind: subset`, all print and portal readers);
- Chapter 14 subgroup aged 30 to 49 (`kind: subset`, parent `c14-120`,
  55 rows).

Update `scripts/check-teaching-variants.R`. Its `observed` list and
`chapter_values()` calls currently hard-code 13 ids and require `setequal`, so
the new ids must be added there. Find the Chapter 10 and 11 setup chunk
labels. Do not add variants for repeated-sampling simulations (Chapter 8;
Chapter 10 seeds 1012–1014; Chapter 11 seeds 1111–1113; Chapter 15 seeds
1516–1517), and record that decision.

7.2 **Consumer lists.** Reconcile every package's `consumers` and
`consumer_sources` with W1. Apply the schema's own definition of a consumer;
for example, decide whether a prose-only mention of Berkeley in Chapters 6 and
13 counts. Read `notes/reports/p6-continuity-*.md` and `p6-data-*.md` for the
"catalogue-consumer defect" they mention. If it is this issue, fix it and
cite the report.

7.3 Run `check-katalog.py`, `check-data-integrity.R` and
`check-teaching-variants.R`. Regenerate the Appendix C views and run
`check-appendix-c.py`.

7.4 Record in the report that the Appendix C catalogue MD5 is part of the
stopped P6-VERIFY route matrix
(`notes/reports/p6-verify-route-stop-2026-09-28.md`), and that it will need
reconciliation when P6-VERIFY resumes. Do not edit those files.

### W8 — Currency

Replace kuna with euro wherever willingness to pay is expressed. Known sites
are Chapter 7 (about line 723), Chapter 8's axis label in `labs(x = ...)`
(about line 502), and Chapter 8 lines 1119–1120 and 1163–1164. Use "eura" and
"eura mjesečno".

The generator values stay unchanged. The catalogue unit is neutral ("novčana
jedinica na mjesec"), and monthly amounts of about 5–7 read naturally in
euros.

Grep book sources, solution records, Appendices A and B, the print apparatus
and the AI export sources for `kun` and `kn`, excluding `docs/` and `_freeze/`.
Fix the sources and regenerate the projections. If a solution record's prompt
text changes, refresh its `prompt_fingerprint` through the standard route and
rerun `check-assessment-architecture.py`.

---

## 5. Stage 1 proposals (write them; implement nothing)

Write each proposal in the report with these fields:

- `id`, `what`, `why`;
- exact files touched and estimated cost;
- risks;
- the governing decision or spine item it touches;
- a recommendation;
- for content proposals, the draft Croatian text.

### P1 — Single canonical sample: feasibility test (read-only computation)

- Work only in `tmp/podatkovna-nit/`, which is git-ignored.
- Write an R script that sources `R/podaci-nastavni.R` and re-creates Chapter
  13's existing draw exactly as its setup chunk does: seed 1313, n = 800, the
  same age cut.
- This is the **only** candidate. Do not try other seeds. Choosing a seed
  because it preserves a wanted result is the forking-paths practice Chapter
  12 teaches against. If the test fails, the remedy is redesigning an exercise,
  not shopping for a seed.
- On that draw, compute the Chapter 10, 14, 15 and 16 analyses exactly as each
  chapter does, with the same functions and options. Compare them with the
  current anchors in §10.4.
- Report group sizes by news source in the 800.
- For each planted error and directional claim in §10.4, mark `preživljava`
  or `ne preživljava`.
- Restate the cost inventory in §10.5 with line numbers verified on the
  worktree.
- Recommend one of three options, with reasons: consolidate, do not
  consolidate, or consolidate together with named exercise redesigns.

### P2 — Cleared data in new places

- **DZS tourism as a comparison across designs of one construct.** Compare
  administrative eVisitor arrivals with survey-estimated trips by residents.
  Plan step 12 of the comprehensive review asks for at least one comparison of
  a shared construct across designs. Candidate homes are Chapter 2 (how an
  observation becomes data) and Chapter 4 (unit: an arrival is not a person).
  DZS must not enter Chapter 3, and its catalogue role as Chapter 3's governed
  offline fallback must stay intact. Deliver:
  - a Croatian draft of at most 200 words;
  - the exact rows used from `data/dzs-*.csv`;
  - the ENRICHMENT.md asymmetry test;
  - what the addition displaces within the word budget.
- **Eurostat poverty or social exclusion (`ilc_peps01n`) and employment
  (`lfsi_emp_a`).** Both are already in the bundled file and loaded in Chapter
  6, but not shown. Propose one use (a figure, a table or an exercise) that
  widens the chapter toward inequality and economics. Check the unit-06
  solution records first.
- **ESS Round 11 Croatia.** Under G-A3-ESS and D08, confirm whether anything
  beyond the optional Chapter 8 exercise is permitted. The likely answer is no
  change. Report it either way.

### P3 — Opening cases that are arguments rather than cases

The vignettes of Chapters 9, 11, 14, 15 and 16 open with a methodological
argument: Cumming 2014, Cohen 1994, Cumming 2014, Simmons 2011 and Breiman
2001. STYLE.md asks for "a real case, a real decision, a question someone
actually faced". Chapter 10 is excluded (`R31-C10-ASA-home`).

For each of the five, either keep it with a stated reason, or propose a
replacement case from published social-science research that someone actually
faced. Prefer cases that connect to the running question (trust in media,
news sources), or that widen the field mix toward sociology, economics,
political science or public health.

Verify every replacement against its primary full text. Give the DOI, a draft
bib entry, the exact claim used and its boundary, in the `sources` format of
`literature-redaction-2026-10-25.json`. Make no proposal without a verified
primary source, and never cite from memory. If no verified case is found, say
so.

### P4 — Field coverage matrix

From W1, build a fields × chapters matrix of all empirical sources, covering
both datasets and cited cases. Name the gaps; for example, there is no dataset
on social inequality, and economics appears only through Eurostat columns.
Propose up to three additions from packages that are already registered, each
with its blocking item:

- `bdp_dugi_niz`: the Eurostat column's lane and the Maddison Project terms;
- `rdp_potpore`: the reuse terms of the register itself;
- `vdem_v16`: deferred under D16.

### P5 — Registering the Chapter 12 laboratory file

`notes/reports/p3-evidence12-rrr-lab-effects.csv` is used by Chapter 12 but is
absent from `katalog.yml`. Read `p3-evidence12-2026-08-13.md` and
`g-a4-12-decision-package-2026-08-13.md`. Propose whether and how to register
it (id, design, lane, promotion status, effect on the portfolio caps), or why
it should stay outside the catalogue.

---

## 6. Dependent regeneration (scripts only)

| Trigger | Regenerate | Then run |
|---|---|---|
| `data/katalog.yml` | `scripts/build-appendix-c-views.R` (writes Appendix C and `podaci.qmd`) | `check-appendix-c.py`, `check-katalog.py`, `check-data-integrity.R` |
| any chapter prose | `scripts/build-appendix-f-route.py`, `scripts/build-appendix-g-route.py`. Their text markers can go stale when a marker sentence changes; the 2026-10-25 pass had to update two. | `check-appendix-f.py`, `check-appendix-g.py` |
| any solution record | `scripts/build-solution-routes.py` (writes `rjesenja.qmd`, `assessment/print-checks.md`) | `build-solution-routes.py --check`, `check-assessment-architecture.py`, `check-pathways.py` |
| any chapter | `R/build-ai-exports.R` (also runs as the pre-render hook) | its `--release --validate-only` mode after rendering |
| print apparatus | `scripts/build-print-apparatus.py`, only if its inputs change (they should not in Stage 1) | the PDF build |

---

## 7. Independent review

After implementation, run three read-only critics in parallel. Use the prompts
in `bookwright_plugin/bookwright/agents/critic-style.md`, `critic-arc.md` and
`critic-evidence.md`. Give each critic the diff against the baseline commit,
the W1 audit and §3 of this brief.

- **Style:** every changed sentence against STYLE.md.
- **Arc:** does the data thread read as one investigation? Are names used
  consistently? Does S6 hold? Does the Part V exclusion hold? Is nothing of
  Chapter 16 spent early?
- **Evidence:** is every new statement about a dataset true to the code and
  the catalogue, with no invented rationale, every number inline and no new
  citation?

Fix the findings, then rerun each affected critic once. Record every finding,
its disposition and any unresolved disagreement.

---

## 8. Verification

8.1 **Ladder.** Run these in the worktree root (PowerShell), both at baseline
(W0) and at the end:

```text
python scripts/check-book-inventory.py
python scripts/build-solution-routes.py --check
python scripts/check-assessment-architecture.py
python scripts/check-pathways.py
python bookwright_plugin/bookwright/scripts/run_rscript.py scripts/check-tokens.R
python scripts/check-manuscript-integrity.py
python scripts/check-figure-introductions.py
python scripts/check-citations.py
python scripts/check-concepts.py
python scripts/check-katalog.py
python bookwright_plugin/bookwright/scripts/run_rscript.py scripts/check-data-integrity.R
python scripts/check-integrity-fixtures.py
python scripts/check-data-fixtures.py
python bookwright_plugin/bookwright/scripts/run_rscript.py scripts/check-teaching-variants.R
python bookwright_plugin/bookwright/scripts/run_rscript.py scripts/check-error-exercises.R
python bookwright_plugin/bookwright/scripts/run_rscript.py scripts/check-unit-16-numerics.R
python bookwright_plugin/bookwright/scripts/run_rscript.py scripts/check-unit-17-numerics.R
python bookwright_plugin/bookwright/scripts/run_rscript.py scripts/check-unit-18-numerics.R
python scripts/check-appendix-a.py
python scripts/check-appendix-b.py
python scripts/check-appendix-c.py
python scripts/check-appendix-d.py
python scripts/check-appendix-e.py
python scripts/check-appendix-f.py
python scripts/check-appendix-g.py
python scripts/check-chapter-spines.py
python scripts/check-identity-briefs.py
python scripts/check-terminology.py
python scripts/check-widgets.py .
python scripts/check-widget-parity.py .
```

If a script needs `-X utf8`, use it and record that. If a script's usage
differs from the line above, read its header and record the form used.

8.2 **Linters** for every changed chapter:

```text
python bookwright_plugin/bookwright/scripts/run_rscript.py bookwright_plugin/bookwright/skills/book-style/scripts/style_lint.R chapters/<file>.qmd
python bookwright_plugin/bookwright/scripts/run_rscript.py bookwright_plugin/bookwright/skills/book-continuity/scripts/structure_lint.R chapters/<file>.qmd
```

Triage every hit against STYLE.md's prose-zones table.

8.3 **Proof that the frozen regions are untouched.** In `tmp/podatkovna-nit/`,
write a script that extracts every frozen region listed in §3.1 from each
chapter at the baseline commit and at HEAD, and compares SHA-256 hashes. Every
pair must match. Record the hashes under `scope_verification`.

8.4 **Builds.** Build the PDF with
`powershell -NoProfile -ExecutionPolicy Bypass -File scripts/render-book-pdf.ps1`
and the HTML with `quarto render --to html --no-clean`, then run
`python scripts/check-rendered-html.py docs`. Check visually, in both PDF and
HTML, every passage you changed. Do **not** commit `docs/`, `_freeze/`, `pdf/`
or `word/` changes; restore them with `git restore` before committing. Earlier
passes left rebuilt outputs to a separate `build:` commit decided by the
author.

---

## 9. Report, commits, stop

9.1 **Report.** Write `notes/reports/podatkovna-nit-<YYYY-MM-DD>.json` plus a
short human-readable `.md` summary. Mirror the keys of
`literature-redaction-2026-10-25.json`:

- `title`, `date`, `status`, `authorization` (verbatim), `scope`;
- `baseline_commit`, `final_observed_commit`, `branch`;
- `changes` (per item: path, before, after, words);
- `word_count`, `sources` (empty in Stage 1), `data_and_pedagogy_boundaries`;
- `data_use_audit` (W1), `razlog_izvlacenja_nije_dokumentiran` (W3);
- `dependent_changes`, `independent_reviews`;
- `checks` (baseline and final), `builds`, `scope_verification`;
- `governance`: P6-VERIFY open; control files and registries untouched; no
  push;
- `proposals` (P1–P5, each with `status: awaiting_author`);
- `file_hashes`.

9.2 **Commits** in this order, each staging only its own files:

1. `docs(review): add data-thread pass brief`
2. `copy(book): name datasets and connect their returns` (W2–W6 prose)
3. `fix(data): register remaining teaching variants and reconcile consumers`
   (W7)
4. `copy(book): express willingness to pay in euros` (W8)
5. `docs(review): record data-thread editorial pass` (report)

9.3 **Stop.** Do not start any proposal. The final message to the author leads
with the outcome. It lists the changes, the check results (baseline against
final) and the critics' verdicts. Then it lists P1–P5, each with a one-line
recommendation, and the exact reply format for deciding, for example
`Odobravam P2-DZS u poglavlju 2 i P3 za poglavlje 14; odbijam P1.` No push and
no pull request without an explicit instruction.

---

## 10. Facts established on 2026-10-25

These come from the `experiment/bauhaus-interaction-ux` checkout before PR #13.
Line numbers are approximate and shift on `origin/main`. Verify every one.

### 10.1 Dataset map by chapter

| Ch | Simulated or constructed | Observed source or cited case |
|---|---|---|
| 0 | `populacija_medija` share table, hard-coded from the aggregate (HTML block) | ASA statement on p-values |
| 1 | `data/populacija-medija-agregat.csv`; `populacija_medija` rows; constructed portal table | Berkeley via `datasets::UCBAdmissions` and Bickel 1975 |
| 2 | 32 widget points; 12 hand-made respondents (`s2_odgovori`) | Berkeley again |
| 3 | hypothetical detector table; widget | DIP 2024 turnout, transcribed from the official report p. 124 |
| 4 | `anketa_mreze` (new; explicitly not a sample of the population), its CSV and aggregate | DigiKat aggregates (`digikat-platforme-*.csv`, `digikat-izvori.csv`) |
| 5 | `anketa_mreze`; six book titles; widget | DigiKat; Anscombe; Cleveland & McGill |
| 6 | `anketa_mreze`; constructed Simpson and range demos | Eurostat 2025 (6 indicators, EU-27); Anscombe; Datasaurus |
| 7 | `populacija_medija` (counts, rules, Q-Q with seed 710); coin tosses | hot hand (Gilovich 1985; Miller 2018) |
| 8 | `populacija_medija` (seed 808 stream: n=100, 3.000 samples, CLT, convenience, self-selection, 5.000 subpopulation); synthetic 16-unit weights table | Literary Digest 1936 (Squire 1988); optional ESS R11 exercise |
| 9 | `populacija_medija` n=200 (909), n=20 (923), n=60 bootstrap (505); aggregate CSV | Hoekstra 2014; Cumming 2014 |
| 10 | n=300 print and portal (1011); calibration (1010); repeated draws 1012–1014 | ASA (vignette, ratified); Greenland 2016 |
| 11 | all print and portal readers (19.956); repeated draws 1111–1113; constructed A/B clicks | Cohen 1994; Button 2013 |
| 12 | widget p-values | 17-lab facial-feedback RRR (Wagenmakers 2016) from `notes/reports/p3-evidence12-rrr-lab-effects.csv`; OSC 2015; Simmons 2011; Silberzahn 2018 (added by PR #13) |
| 13 | n=800 (1313); constructed teaching experiment; Fisher 2×2 | Berkeley; Pew 2024 "nones" (replaced the imagined library in PR #13) |
| 14 | n=120 TV and social media (1414); 30–49 subset (55); paired synthetic n=60 (1415) | Cumming 2014; Belia 2005 |
| 15 | n=300 five sources (1515); null simulations 1516–1517 | Simmons 2011; Nieuwenhuis 2011 |
| 16 | full population; reuses 1414 and 1515; n=200 + noise (1616); 150/2.000 (1618); first 200 rows; widget set of 52 | Breiman 2001; Kleppang 2021 (Ungdata, in divljina); DigiKat mention |
| 17 | widget scores (simulated groups A/B) | ParlaSent 1.0, 272 validation sentences; Chouldechova 2017 |
| 18 | `anketa_mreze` (the same 300 as in Chapters 4–6) | ParlaSent, all 2.698 sentences; Cumming 2014 |

Population shares by source: portal 15.101, social media 13.378, TV 10.827,
radio 5.839, print 4.855 (total 50.000).

### 10.2 Draws without a teaching variant (W7.1 targets in bold)

**10 main (1011)**, **10 calibration (1010)**, **11 subpopulation**, **14
subset 30–49**. Excluded by design: all draws in Chapters 7–9, the
repeated-sampling simulations in Chapters 10, 11 and 15, and Chapter 16's
1616 draw, its 30–50 subpopulation, the `[1:200]` slice and the 1619 plotting
draw. Record the reason for each exclusion.

### 10.3 How returns are currently phrased (examples)

- Chapter 8: "To je ista zamišljena populacija kojom smo se već služili,
  odvojena od manje ankete `anketa_mreze`."
- Chapter 13: "Vratimo se sada uzorku od 800 zamišljenih osoba."
- Chapter 14: "…izvukli smo 120 osoba … zasebno od ranijih 800 osoba."
- Chapter 15: "…zasebno od uzorka prethodnog poglavlja."
- Chapter 16: "Uzorak od sto dvadeset osoba iz poglavlja o dvjema grupama."

### 10.4 Sample-tied anchors that P1 must test

| Ch | Anchor | Current value | Must survive because |
|---|---|---|---|
| 10 | print minus portal | 0,64 [0,17; 1,11] | text says print is higher (about lines 269, 983) |
| 10 | permutation p (greška) | b = 64 of 4.000, p = 65/4.001 ≈ 0,016 | planted error and solution records |
| 11 | power of the Chapter 10 design | about four in five samples of 300 (seed 1013, 79,5 %) | prose at about line 356 |
| 13 | χ² test (greška) | min. expected 14,3; χ² 149,8; df 12; V 0,25 | unchanged if the 1313 draw is the canonical sample |
| 14 | TV minus social media | 1,19 [0,45; 1,92] | critical exercise premise: upper bound below 2 |
| 14 | subgroup 30–49 (greška) | n = 55; 0,77 [−0,34; 1,88] | the planted error needs an interval that includes 0 |
| 15 | ANOVA | F 8,38; η² 0,102 ("about a tenth") | prose and worked example |
| 15 | Tukey pattern | social media differs from each of the four others; one other pair does not (0,04 [−1,06; 1,14]); TV minus social media 1,59 [0,71; 2,46] | prose at about lines 730–734 and 900–907 |
| 16 | identities | `identical(s16_dvije, dvije_skupine)`, `identical(s16_pet, pet_izvora)`; "as much as the eta-squared computed earlier" | `check-teaching-variants.R`, prose at about line 1102 |

Expected group sizes in a sample of 800: portal about 242, social media about
214, TV about 173, radio about 93, print about 78.

### 10.5 Cost of consolidating Chapters 10–16 onto one sample

- **Files:** about 25–30 in total.
  - Chapters 10, 11, 13, 14, 15, 16 and `dodaci/b-jamovi.qmd`.
  - `data/katalog.yml` (replace c13-800, c14-120, c15-300, c16-dvije and
    c16-pet; add Chapter 10).
- **Solution records:** 9 records, units 10, 13 and 14.
- **Scripts and configs:**
  - `check-error-exercises.R`, `check-teaching-variants.R`,
    `check-unit-16-numerics.R`;
  - `check-assessment-architecture.py`, which holds 120 + 300 hard-coded
    person IDs for units 14 and 15;
  - `appendix-a-route.R` and `check-appendix-a.py` (25 golden values);
  - the regenerated `config/appendix-b-jamovi-route.json`.
- **Projections:** `rjesenja.qmd`, `assessment/print-checks.md`, the greška
  PDF.
- **Hand-maintained values:**
  - in the chapters: about 25 numbers, about 20 directional claims and about
    25 sample-size literals;
  - in the records: about 90–110 numeric tokens;
  - in the scripts: about 120 constants.
- **Pedagogical risks:**
  - Print readers are only 4.855 of 50.000, so groups are small and unequal.
  - Larger groups shrink intervals, so the Chapter 14 planted error, which
    needs an interval that includes 0, may stop working.
- **Seed numbers** 505, 808, 909, 1010, 1111, 1414 and 1515 are also used by
  widget print twins (and 1515 for jitter in Chapter 15), so a blind
  search-and-replace on seeds would break the widget goldens.

---

## 11. Stage 2 (later thread, after the author decides)

Launch Stage 2 with a message of this form: `Provedi odobrene prijedloge iz
notes/reports/podatkovna-nit-<datum>.json: <ids>.` Stage 2 follows the same
§1, §3 (with the frozen regions relaxed only where an approved proposal
requires it), §6, §7, §8 and §9. Each approved proposal gets its own commit,
and the report gets a `stage2` section.
