# Comprehensive review implementation plan

**Book:** *Osnove statistike za društvene znanosti*

**Plan date:** 3 August 2026

**Status:** ratified at Gate A0 on 3 August 2026

**Primary requirements source:** `comprehensive-book-review-2026-07-31.md`

This is the operational plan for turning the comprehensive review into a
coherent, verified first edition. It preserves the existing five-part order,
treats Chapters 3, 12, and 17 as the book's identity pillars, and orders the
work by curricular and evidential dependency rather than by file number or by
the review's original phase labels.

The plan does not authorise silent chapter rewriting. It defines what Codex can
execute, what requires an author or external decision, the order of execution,
and the evidence required before any item or chapter may be called complete.

---

## 1. Outcome and non-negotiable constraints

The implementation is complete only when all 36 ranked review items have a
recorded disposition and all accepted first-edition items are implemented and
verified. A successful render is necessary but never sufficient.

The finished edition must satisfy these conditions.

1. The two statistical blockers and all connected assumption or estimand
   problems are corrected and independently reviewed.
2. The claim map, lifecycle, cross-book threads, chapter spines, definitions,
   terminology, prerequisites, and assessment policy are ratified.
3. Chapters 3, 12, and 17 are complete arguments rather than expanded lists.
4. The first governed empirical portfolio is available through licensed,
   documented, validated teaching packages or an explicit portal-mediated
   route.
5. Data science functions as the book's evidence workflow. It does not become a
   fifth promise or a catalogue of tools.
6. Text analysis is taught in Chapter 17 as measurement, validation, and social
   consequence, not as an NLP programming course.
7. AI forms a cumulative verification ladder across the book and remains both
   an instrument and an object of study.
8. Every assessment has an agreed feedback path, every widget-dependent task
   has a print-completable path, and no assessed chapter exercise requires the
   student to write R.
9. HTML, the teaching profile, PDF, and DOCX make the same statistical claims
   from the same source state; all 17 widget/static-twin pairs pass exact or
   distributional parity tests.
10. The edition is licensed, citable, archived, frozen for teaching, and
    correctable through a public errata route.

The following scope boundaries remain binding.

- Preserve the current chapter order and five-part architecture.
- Add no numbered methods chapter and no additional central widget.
- Do not add full courses in survey statistics, logistic regression, causal
  inference, meta-analysis, multilevel modelling, NLP, machine learning,
  databases, dashboards, scraping, or cloud infrastructure.
- Keep known-truth simulations where they reveal mechanisms. Add empirical
  data to teach provenance, design, transfer, and claim limits rather than
  replacing the simulations.
- Label simulation, synthetic records, hypothetical model output, and
  fabricated evidence distinctly. Generated respondents are teaching aids and
  can never support an empirical population claim.
- Do not admit a dataset merely for topical variety. It must add a distinct
  data-generating design or be indispensable to a ratified chapter argument.
- Treat the approximate 84,000–86,000-word target as a diagnostic, not a quota.
  Chapters 3, 12, and 17 retain their planned argumentative weight; all other
  chapters finish when their role is complete and their prose passes the
  structural bands.

---

## 2. Ratified defaults

These defaults resolve the review's open branches in the way that best protects
accuracy, coherence, self-study value, and maintenance cost. On 3 August 2026,
the author approved D01–D16 without amendment. The author also approved the
planning checkpoint, the dedicated revision branch, and bounded verified local
packet commits. Push, merge, tag, archive, and deployment were not authorised.

| ID | Recommended default | Reason and consequence | Blocks |
|---|---|---|---|
| D01 | Keep raw-label permutation in Chapter 10 only as an exchangeability/full-distribution null; stop calling it an assumption-free test of equal means; add the Monte Carlo correction `(b + 1) / (B + 1)`. | Preserves the simulation-first teaching device without introducing an unnecessarily advanced studentised permutation procedure. | Chapters 10–12 |
| D02 | Keep Welch inference as the Chapter 14 default. Teach that a binary-predictor coefficient equals the difference in means, while its ordinary homoskedastic OLS uncertainty is not generally Welch uncertainty. | Preserves the Chapter 16 model reveal without making a false equivalence claim. | Chapters 14–16 |
| D03 | Preserve the macro-order. Add an optional two-route reading map for navigation, not a reordered book. | The existing hinge, summit, and capstone are strengths. | Spines and preface |
| D04 | Put the full data-science lifecycle in Chapter 1; let the preface state the promise and point to it. | Keeps the preface from becoming a manifesto and gives the lifecycle an instructional home. | Chapters 00–2 |
| D05 | Preserve the ratified Part I rule of no visible code. Hidden plumbing is permitted; assessed code production is not. | Resolves the review's overbroad H10 wording without breaking the established code-reading ladder. | Chapters 00–3 and assessment |
| D06 | Use one canonical solution record per exercise and render it in two layers. The self-study edition receives concise checks, intended planted errors, and answer components in a deliberately separated solutions route; the `kolegij` profile receives full rubrics, alternatives, and instructor notes. Exclude protected solutions from public AI exports. | Satisfies self-study feedback without duplicating answer maintenance or making instructor material indistinguishable from the student text. Requires a coordinated change to `STYLE.md`, rendering, and exports. | All new exercises and Phase 5 |
| D07 | Retain Chapter 17's existing fairness widget and make the ParlaMint-HR/ParlaSent text analysis the worked example. | The widget already exists and passes its contract; text analysis adds the missing contemporary measurement problem. | Chapter 17 data and prose |
| D08 | Use an ESS Round 11 portal-mediated route by default, with a pinned selection recipe, transformation script, codebook, weights, and checksum instructions. Bundle an extract only after written permission. Until then, ESS microdata is optional empirical replication rather than core assessment; every required R/jamovi/print task uses a licence-cleared bundled file or aggregate alternative. | Avoids making the book or CI depend on data it may not redistribute while preserving a complete student pathway. | Chapters 13–16 and appendices |
| D09 | Build Appendix B as a bounded, versioned no-code route for the book's core analyses, using the same files and expected values as Appendix A. Narrow any broader public promise. | Delivers a real path without an unmaintainable screenshot for every possible menu. | Appendix B and pathway claims |
| D10 | Add a compact Appendix G for percentages/percentage points, proportions/rates, slope, and logarithmic scale, with sanctioned `podsjetnik` links at first use. | Directly serves the no-mathematics-assumed audience. It requires an explicit A–G architecture update before the file is added. | Book inventory and wrappers |
| D11 | Prefer original rewriting of materially Navarro-derived prose while retaining proper scholarly attribution; adopt ShareAlike terms only if the provenance audit shows that rewriting cannot remove the obligation. | Minimises licensing complexity without evading attribution or licence duties. | Book licence and release |
| D12 | Give generated teaching data an explicit licence compatible with the final book licence; use CC BY 4.0 as the provisional default subject to the full licence audit. | “Not applicable” is not an adequate data licence. | Data catalogue and downloads |
| D13 | Keep Chapter 18's main study explanatory and explicitly state why it does not use every Chapter 17 predictive tool; make the empirical transfer task apply the full data/AI audit. | A capstone should integrate judgment without forcing an artificial algorithm into the main study. | Chapter 18 |
| D14 | Keep *Osnove statistike za društvene znanosti* as the working release title unless the author changes it before citation metadata is frozen. | Prevents title drift across DOI, colophon, site, and teaching editions. | Release governance |
| D15 | State privacy and AI-use rules as a dated, conservative course policy and distinguish public, contractually protected, and institutionally approved local tools. | Avoids presenting a local policy as timeless universal law. | Chapters 12, 17, 18 and Appendix F |
| D16 | Defer full V-Dem, COVIDiSTRESS, World Bank, and other second-wave packages until a chapter passes the admission rule and demonstrates a non-duplicative need. The first-edition design matrix must still give expert-coded measures and volunteer samples one explicit disposition: governed student data, verified published case, or justified omission. | Protects the book from data sprawl without making important data-generating designs invisible. | Data-design matrix and optional later work |

Two defaults also constrain editorial choices. Base-rate literacy must be
planted in Chapter 3 before Chapter 17 uses it, and Chapter 16 must retain its
synthesis reveal. Chapters 14 and 15 may prepare the general-model language but
must not spend the payoff.

---

## 3. Current baseline and control plane

The implementation begins from a deliberately conservative status.

- All 19 ledger units remain at `draft`.
- Every chapter spine is empty and `ratified: false`.
- The structural skeleton, 17 widget contracts, rendered HTML inventory, and
  design tokens currently pass their deterministic checks.
- The current style linter reports no candidates, but the rhythm check flags
  the preface and Chapter 17, and Chapter 5 lacks the required introduction to
  `fig-anscombe`.
- `data/katalog.yml` and empirical CSV packages do not exist. The public data
  page and Appendix C are currently manual/incomplete, and Appendix A refers to
  a missing `data/anketa.csv`.
- The R and browser dependencies are not locked. The release workflow uses the
  wrong PDF entry point and permits a stale PDF to survive a failed build.
- The Bookwright conductor checklist, style-skill text, and parts of
  `AGENTS.md` still name H1–H9 although `STYLE.md` now has H10. `AGENTS.md` also
  still describes an empty skeleton. The ledger has 20 schema violations: 19
  `last_render: success` values where the schema requires `ok`, plus one
  `coauthor_asks.status: resolved` value where it requires `done`. These
  state/tooling mismatches must be repaired before ledger automation is trusted.
- Checkout-local structure lint reads the ratified 7–12 section band. An
  installed cached copy can read stale conventions and produce false findings,
  so all gates must use checkout-local Bookwright paths until cache resolution
  is corrected and the plugin is reinstalled.
- At Gate A0, the `main` worktree contained the modified comprehensive review
  and two untracked files, `notes/agenda-knjige.md` and this plan. All three
  were preserved in checkpoint commit `c163bda` before the dedicated revision
  branch was created.

### Implementation register

After Gate A0, create
`notes/reports/comprehensive-review-implementation-register.yml` as the
source-controlled register. Give every actionable finding in the complete
review, especially §§4–14 and §16, one atomic child row linked to a parent
R01–R36 item and its exact review section/location. A parent is accepted only
when all required children are accepted. Gate P0 requires zero unmapped
actionable findings, not merely 36
mapped parent categories. Each row records:

Use stable child IDs such as `R09-C02-item-total` or
`R18-W08-exact-parity`; never renumber them after work begins.

- ID and review source;
- description and first-edition disposition;
- owner and approval owner;
- affected files and chapters;
- prerequisites;
- evidence/data/citation requirements;
- acceptance test;
- status and completion evidence;
- commit or pull-request reference;
- reason for any deferral.

Maintain `notes/reports/comprehensive-review-dashboard.md` as the compact human
view. At every packet closeout it records the current packet, branch/commit,
accepted/total child items, chapter stages, open outside asks, failed gates, and
next permitted packet. The register is authoritative; the dashboard is a view,
not a second task list.

Maintain
`notes/reports/comprehensive-review-forward-handoffs.yml` as the register's
append-only companion for consequential discoveries. Every handoff names a
source packet, one or more existing target packets, the constraint or finding,
its basis, the action required later, and one delivery state per target. A
source packet cannot close until it records all outgoing handoffs or explicitly
declares that it found no future-relevant effect. A target packet acknowledges
applicable handoffs before its first substantive edit and consumes them with a
disposition and evidence before closeout. Handoffs are never deleted: they are
consumed, waived with author approval, or superseded by another stable handoff
ID. If a discovery invalidates accepted work, reopen that work explicitly.

The register, handoff ledger, and dashboard form one control transaction. Run
`scripts/check-review-workflow.R` before every packet claim and closeout. The
dashboard must end with the exact copy-paste prompt for the next permitted
packet.

Use these implementation statuses:

```text
proposed → ratified → in_progress → implemented → verified → accepted
                  + blocker flag: blocked_external
                                      ↘ deferred_v2_with_reason
```

In this plan, “closed” means `accepted`. `blocked_external` is a blocker flag,
not a substitute for completion; an affected parent remains open. A first-
edition item can otherwise leave the active path only as
`deferred_v2_with_reason`, with an approved reason and no contradicted public
promise.

Do not duplicate repeated review prose as separate tasks. The canonical work
packages are correctness, intellectual spine, empirical data, lifecycle and
claim threads, text/AI, assessment, alternative pathways, parity, evidence and
licensing, editorial continuity, reader testing, and release governance.

The chapter ledger uses its existing lifecycle without skipping stages:

```text
draft → enriched → style_swept → figures_done → coauthor_review → final
```

A chapter remains `draft` while its spine is unratified. It advances only when
the applicable gate for that stage has actually passed. A panel may recommend
`coauthor_review`; only the conductor's final checklist and author sign-off may
advance it to `final`.

The recorded stage is the highest gate still valid for the current file, not a
permanent badge. A later substantive or terminology change reopens a chapter at
`draft` or `enriched`; prose changes invalidate `style_swept`; figure, data, or
widget changes invalidate `figures_done`; post-panel repairs invalidate
`coauthor_review` until the affected checks are repeated. A modified `final`
chapter is reopened conservatively.

### Baseline checkpoint

Before implementation:

1. Record the current commit, `git status --short`, word counts, ledger state,
   audit results, render status, and known failures.
2. Decide whether to checkpoint the modified review, `notes/agenda-knjige.md`,
   and this plan in one intentional documentation commit. Do not discard or
   fold them invisibly into a chapter patch.
3. After that decision, create `revision/comprehensive-review` as the dedicated
   working branch. Use `experiment/*` only for genuinely
   experimental features such as a replacement widget or a new export path.
4. Use one bounded commit per accepted work packet and the repository's commit
   prefixes. Generated artifacts get a separate `docs(...)` or `build:` commit
   only when the project convention requires them.
5. At A0, decide whether Codex may create local scoped commits. The safe default
   is edit and verify without committing until authorised. No push, merge, tag,
   archive, or deployment is authorised by plan approval alone.
6. Never use stash, reset, destructive checkout, or broad restore to recover a
   packet. Reverse an uncommitted failed packet only with an explicit scoped
   patch after inspecting the diff; commit only scoped files when authorised;
   undo an accepted committed packet with an explicit `git revert`. Return
   experiment work through selective cherry-picks and repeat all invalidated
   gates.

**Gate A0 result:** the author approved the checkpoint, branch, and bounded
local-commit defaults. The three planning files were committed as `c163bda`,
and work continues on `revision/comprehensive-review`. No external action was
authorised.

---

## 4. Dependency graph

The three identity briefs are designed together but authored only when their
prerequisites are stable.

```text
Gate A0 and baseline
        |
        v
correctness + legal/build safeguards
        |
        v
claim map + lifecycle + threads + spines + assessment policy
        |
        +-------------------- initiate external asks -------------------+
        |                 ESS / pilot / rights / terminology            |
        v                                                               |
catalogue contract + just-in-time data packages                          |
        |                                                               |
        v                                                               |
00–02 → 03 → 04 → 05 → 06                                               |
                    |                                                   |
              07 → 08 → 09 → 10 → 11 → 12                              |
                                      |                                 |
                         13 → 14 → 15 → 16 → 17                         |
                                                   |                    |
                                                   v                    |
                                                  18 <------------------+
        |
        v
appendices and pathways → whole-book pass → release candidate → final edition
```

The hard curricular chain is:

```text
00/01 reader contract and lifecycle
  → 02 unit, measurement, eligibility, survey, coding, causal seed
  → 03 claim audit and base rates
  → 04 constructed analysis table, missingness, honest-sentence seed
  → 05 visual claim
  → 06 association and causal retrieval
  → 07 probability
  → 08 sampling hinge
  → 09 estimation
  → 10 testing
  → 11 magnitude and power
  → 12 research-system and reproducibility pillar
  → 13–15 model-family preparation
  → 16 regression summit
  → 17 text, prediction, fairness, and deployed-AI pillar
  → 18 evidence-package harvest
```

---

## 5. Sequential execution phases

### Phase 0 — ratify the plan and establish control

**Purpose:** prevent work from beginning against contradictory assumptions or
an untracked review.

1. Approve or amend D01–D16.
2. Establish the register, forward-handoff ledger, dashboard, active-packet
   lock, exact next-thread prompt, and deterministic control-state validator.
3. Reconcile every review finding against the current source and mark it
   `accepted`, `already_satisfied`, `partial`, `rejected_with_reason`, or
   `deferred_v2_with_reason`.
4. Populate the register's atomic child inventory. Copy a chapter packet into
   the live chapter ledger only when its dependencies are satisfied; do not
   preload blocked downstream work. Keep appendices, release engineering,
   exports, and whole-book decisions in the implementation register.
5. Repair the H10 contract drift, stale project-status text, all 20
   ledger/schema violations, and installed-cache convention resolution. Patch
   the checkout-local Bookwright source, validate its schemas/tests, bump the
   plugin cachebuster/version, reinstall it through the project workflow, and
   start a fresh thread if skill discovery requires it. Until that succeeds,
   all commands and registry reads use checkout-local paths. Validate all
   shared JSON against its schema.
6. Capture the baseline checkpoint without changing chapter stages.
7. Start long-lead outside work immediately: recruit five novice readers,
   request or confirm dataset rights, identify a domestic terminology reviewer,
   and identify owners for the archive, errata, accessibility proof, and final
   release.

**Exit gate P0:** the implementation register covers R01–R36 with zero unmapped
actionable child findings; every open decision has one owner and due phase;
Bookwright state validates; the starting worktree is preserved; all chapters
remain `draft`.

### Phase 1 — remove correctness and publication-integrity blockers

#### Batch 1A — statistical correctness

1. Correct Chapter 10 under D01 and verify the simulation, null statement,
   assumptions, test statistic, and Monte Carlo p-value.
2. Revalidate Chapter 11 for inherited permutation ambiguity and state the
   assumptions of its power demonstration.
3. Correct Chapter 14 under D02 and make the distinction among the difference
   in means, Welch inference, and ordinary OLS inference explicit.
4. Revalidate Chapters 15 and 16 so neither inherits the false equivalence.
5. Repair the connected assumption and estimand statements in Chapters 2,
   6–9, 11, 13, 16, and 18. This includes CLT conditions, bootstrap limits,
   Pearson versus adjusted standardised residuals, the Chapter 16 estimand,
   leakage/prediction timing, and Chapter 18's interval-compatible conclusion.
6. Run two independent methods readings on the corrected packets and reproduce
   every affected numerical result from a clean session.

No enrichment begins until Batch 1A passes. Corrected prose may remain
editorially provisional until spines are ratified, but no known false claim may
remain in a downstream prerequisite.

#### Batch 1B — licence, evidence, and metadata safety

1. Audit every potentially Navarro-derived passage and resolve D11.
2. Inventory every current and proposed dataset's source, version, licence,
   attribution, access, and redistribution lane. Assign the generated-data
   licence under D12.
3. Remove `nocite: @*`; verify cited bibliography records, DOI/URL/version
   metadata, and the fit between each cited source and its sentence-level claim.
4. Update the README and public metadata so they no longer describe an empty
   skeleton.
5. Establish the release-governance structure now: edition/version field,
   Croatian reader-facing changelog, citation block, errata page and dated log,
   term-freeze policy, archive plan, and artifact-provenance record. Do not
   create the final tag or archive until Phase 8.

#### Batch 1C — reproducible and fail-closed production

1. Create and test the R lockfile and a pinned browser-test package/lock.
2. Make CI invoke `scripts/render-book-pdf.ps1`, never bare
   `quarto render --profile pdf`; make PDF failure blocking and prevent stale
   artifacts from being published.
3. Make token, manuscript-integrity, citation, data, and release checks blocking
   at the appropriate pipeline level.
4. Add a release mode in which AI-export failures are fatal. Ensure public AI
   exports omit protected solution/instructor content and reconcile the export's
   book metadata with the canonical metadata.
5. Add golden-value tests for all 17 OJS/R pairs. Record each pair as `exact` or
   `distributional` in the widget registry, with parameters, seed policy,
   tolerance, and expected values.
6. Replace the undeclared/hard-coded browser audit with a pinned, portable
   runtime and a blocking interaction smoke test for keyboard operation, reset,
   responsive widths, and dark mode. Full semantic and assistive-technology
   coverage remains a Phase 7 release gate.
7. Make appendix/page inventories configuration-driven before adding Appendix G
   or a solutions route.
8. Keep commands individually callable. A cross-platform runner with `chapter`,
   `batch`, and `release` modes may consolidate them later, but it is not on the
   critical path unless repeated execution proves consolidation necessary.

**Exit gate P1:** R01, R02, and R05 are `accepted`; accepted children cover the
current-material and policy portion of R03 while package-specific or externally
blocked children remain open until Phase 3; the governance mechanism for R06
exists; affected numerical results are reproduced; no release path can silently
publish stale output.

### Phase 2 — ratify the intellectual, curricular, and assessment system

This phase uses Bookwright continuity in spine mode. It edits registries and
governing documents after approval, never chapter prose.

1. Ratify the six claim dimensions: description, association,
   generalisation, prediction, causation, and decision.
2. Ratify the six recurring audit questions: observation/unit, absence and
   selection, target quantity and claim type, represented and omitted
   uncertainty, a reasonable alternative decision, and who bears the
   consequences of error.
3. Ratify the lifecycle:

   ```text
   question → acquire → validate → prepare → explore → model
            → evaluate → communicate → monitor
   ```

4. Ratify the seven cross-book threads and their plant/develop/harvest points:
   unit, selection/absence, denominator, uncertainty budget, consequences of
   error, reproducibility/provenance, and communication of a claim.
5. Ratify overlay threads for survey practice, causal reasoning, text as data,
   missingness, sensitivity, design comparison, “what would change the
   conclusion?”, and AI verification.
   The AI ladder advances by part: provenance and fabricated numbers in Part I;
   reproduced summaries, plots, and code traces in Part II; sampling and
   generalisation limits in Part III; nulls, flexibility, and reproducibility
   in Part IV; reference groups, assumptions, causal language, leakage, labels,
   subgroup errors, and shift in Part V; then complete specification,
   delegation, reproduction, challenge, documentation, and disclosure in
   Chapter 18.
6. Ratify a small spine of load-bearing aspects and terms for every unit,
   including the identity pillars and Chapter 18. Only then add or remove
   `#def-` blocks and regenerate the concept graph/glossary.
7. Canonicalise Croatian terminology, especially prediction, training/
   validation/test sets, overfitting, residuals, odds, weights, text units, and
   algorithmic labels. Record accepted alternatives and deliberate departures.
8. Correct prerequisite metadata. Chapter 17 must include Chapter 13 and the
   relevant testing/error prerequisites; Chapter 18 is whole-book cumulative;
   Chapter 12 names its interval/effect prerequisites; Chapter 14 reflects its
   real dependence on Chapters 9–11.
9. Ratify D06 and write the answer-key schema, rubric severity scale, profile
   visibility, export exclusion, and instructor/student split before new
   exercises are authored.
10. Ratify the three identity briefs together:
    - Chapter 3 uses one traceable public claim and plants base-rate literacy.
    - Chapter 12 follows one full research/reform lifecycle and includes one
      sensitivity comparison and one forest plot.
    - Chapter 17 follows one consequential text-classification decision from
      corpus construction to monitoring, appeal, and feedback.
11. Ratify D09 and D10, the two reading routes, part-ending bridge/self-check
    format, H10 ladder, AI competence ladder, privacy/tool lanes, and the
    outcome-based word-count rule.
12. Ratify the first-edition data-design matrix. Probability survey,
    administrative count, official aggregate, expert-coded measure, digital
    trace, volunteer sample, and simulation each receive a governed dataset,
    verified published case, or justified omission. Approve at least one
    cross-design comparison of a shared construct without implying that the
    units or measures are interchangeable.
13. Update `notes/struktura-knjige.md`, `AGENTS.md`, `STYLE.md`, `DESIGN.md`,
    conventions, and shared registries only where an approved decision changes
    their declared contract.

**Exit gate P2:** R04 is closed; the architectural gates for R10, R15, R24, and
R36 are ratified but those issues remain open until their book-wide
implementation is verified; all 19 spines are ratified; definition and
prerequisite changes have an approved map; there is no unresolved conflict
between the review and the live governing documents.

### Phase 3 — establish evidence, data, and novice-reader foundations

#### Batch 3A — catalogue and validation contract

1. Add `data/katalog.yml` as the sole data source of truth.
2. Give each entry an ID, domain, unit/level, source/query, edition/date,
   citation, licence, redistribution lane, refresh class, file paths, build
   script, checksum, caveats, consumers, variables, missing codes,
   transformations, permissible/unavailable claims, and a bounded ethics note
   covering category ownership, absence, identifiability, beneficiaries, error
   burdens, and appeal where applicable.
   Render a one-page student passport before the dataset's first analytical use
   so a reader can inspect the row, absences, production process, missing and
   suppressed codes, weights, snapshot date, and unavailable claims.
3. Make `podaci.qmd` and Appendix C two generated views of that catalogue.
4. Turn `R/fetch-podaci.R` into a dispatcher. Fetch only to ignored temporary
   raw storage, transform to a candidate, validate, show a human-readable diff,
   obtain acceptance, then promote committed teaching files. Never fetch during
   render.
5. Register and licence the existing `UCBAdmissions`, `anscombe`,
   `anketa_mreze`, and `populacija_medija` data. Materialise deterministic CSV
   snapshots needed by students, jamovi, and print exercises and validate them
   against their generators/seeds.
6. Apply the refresh classes consistently: frozen for Berkeley/Anscombe and
   DIP; pinned for ESS, ParlaMint, and ParlaSent; scheduled manual snapshots for
   DZS (semiannual) and Eurostat (annual); manual derived snapshots for
   DigiKat; external-only for Determ and GFI/FINA.

#### Dataset acceptance contract

A package may enter chapter prose only when all of the following pass.

1. It has a distinct curricular function and fixed consumers.
2. One row, excluded populations, and the permissible claim can each be stated
   in one sentence.
3. Source, query/table, edition, retrieval date, citation, licence,
   attribution, and redistribution lane are recorded.
4. The analysis file, codebook, notice, build/selection script, and useful
   aggregate exist.
5. Files use UTF-8 and stable ASCII names, retain original codes beside Croatian
   labels, and retain full numeric precision.
6. Percentages retain numerator and denominator; survey files retain weights;
   zero, missing, suppressed, and unpublished values remain distinct.
7. Schema, key uniqueness, row-count bands, category/missing domains, units,
   totals/components, and checksums pass.
8. Selected values reconcile to the official source or documented source
   counts.
9. Refresh is manual, candidate-first, diff-reviewed, and render-independent.
10. For a core bundled package, R, jamovi, print, and chapter routes use the
    same files, variable names, and checked expected results. A portal-mediated
    package names the optional replication route and supplies a licence-cleared
    bundled file, aggregate, or alternative dataset for every required
    assessment/pathway; it does not pretend file parity.
11. Catalogue consumers match actual source use and all public downloads
    resolve.
12. The student passport is visible before first use, and the package provides
    paired analysis-level and aggregate views when hand/print verification is a
    curricular requirement.

#### Batch 3B — just-in-time portfolio

Build only the packages required by the next curricular wave.

| Before | Required package | Bounded content and validation |
|---|---|---|
| Wave A, Chapters 00–3 | DZS tourism and DIP 2024 | DZS BS_TU11 complete-year national monthly arrivals/nights, one BS_TU12 county cross-section, T01–T03 long extract; retain totals and suppression codes and prevent annual/month double-counting. DIP retains turnout numerators/denominators and reconciles to official totals. |
| Wave B, Chapters 4–6 | DigiKat actor snapshot and fixed-year Eurostat | One dated actor × platform aggregate with public labels, method-break caveat, and no full Determ corpus. Five to seven question-led Eurostat indicators in one common year, with flags/missingness retained. |
| Wave C, Chapter 12 | Verified research-lifecycle/evidence-synthesis source | A source package or cited artifact that supports the complete lifecycle, sensitivity example, and forest plot without inventing study results. |
| Wave D, Chapters 13–16 | ESS portal route under D08 | Pinned wave/edition and Croatia variable set, codebook, selection/transformation recipe, weights, missing codes, and checksum instructions; no committed microdata without permission. |
| Wave D, Chapter 17 | Linked ParlaMint-HR/ParlaSent package | Speech text/metadata, prepared term counts, labelled sentences, coder labels, reconciled recorded label, and original split, all tied to the ratified question and sampling rule. |

Keep the full DZS dump, Determ corpus, and GFI/FINA database external. CroAIcon
may provide verified query logic or a clearly labelled published aggregate, but
it must never become a render dependency or core student dataset.

#### Batch 3C — novice evidence

1. Freeze baseline pilot versions of Chapters 1, 8, and 16 after only the
   surgical Phase 1 corrections. Do not pre-revise them to anticipated reader
   findings or wait for their later Wave packets; the purpose is to test the
   current developed opening, hinge, and summit before the large investment.
2. Run five think-aloud sessions using one protocol and record, without
   collecting unnecessary personal data: comprehension stops, rereading,
   vignette success, widget discovery and control mistakes, code-reading,
   exercise interpretation, and actual reading time.
3. Classify findings as individual preference, repeated friction, or blocking
   comprehension failure. Do not redesign from one reader's taste.
4. Convert repeated/blocking findings into bounded tasks in the register and
   correct `.chapter-meta` time estimates only from measured evidence.
5. While reader recruitment is pending, Codex may complete non-prose QA and
   approved data-package work. Identity-chapter prose does not begin until the
   pilot findings are incorporated.

**Exit gate P3:** R26 is closed; R08 and R25 have operational foundations and
remain open until actual chapter use and both generated catalogue views are
verified; DZS/DIP are ready for Wave A; the pilot has produced an accepted
revision memo; no chapter depends on an unlicensed or unvalidated local file.

### Phase 4 — revise the main book in dependency waves

Every chapter is revised as a complete vertical slice. Its prose, data,
sources, figures, widget introduction, AI step, exercises, keys/rubrics, print
alternative, and transitions are authored together. This avoids an expensive
late retrofit of assessment and accessibility.

Chapters 3, 12, and 17 use full rewrite packets shaped by their ratified
single-argument briefs. The bounded one- or two-paragraph Book Enrich workflow
is reserved for genuine asymmetries in the other chapters; it is not a way to
inflate an identity chapter paragraph by paragraph.

#### Wave A — reader contract and first identity pillar, Chapters 00–3

1. **Preface:** replace the meta-example with a genuine miniature inquiry;
   make the novice task self-contained; state the stable AI thesis; point to the
   Chapter 1 lifecycle; describe code as a checkable calculation trace; present
   the two reading routes without manifesto register.
2. **Chapter 1:** plant the claim map, lifecycle, unit, denominator,
   provenance, and the boundary between statistics, data science, machine
   learning, and deployed AI. Ensure each Berkeley recurrence asks a new
   question.
3. **Chapter 2:** repair design claims; distinguish common causes, mediators,
   and colliders at literacy level; describe randomisation as balance in
   expectation and qualify adherence, spillover, attrition, and measurement;
   treat a negative item–total association as a diagnostic rather than proof of
   reverse coding; historicise the Stevens levels; plant eligibility, text
   coding, survey realism, missingness, ethics, and the shared causal diagram
   vocabulary.
4. **Chapter 3:** build the first identity pillar around one traceable DZS,
   DIP, or similarly verified public claim. The argument must integrate axis or
   denominator, base rates, early poll literacy with an explicit debt to
   Chapters 8–9, cherry-picking, an AI-produced number, provenance, synthetic
   media, and the simulation/synthetic/fabricated distinction. Move the main
   ASA episode to Chapter 10 and close the 3→4 transition.
5. Complete the Part I claim bridge and answerable self-check inside the
   sanctioned structure.

Wave A establishes the preface's instructional contract, but its final promise,
reading-route, edition, and citation wording is frozen only in Phase 6 after the
book it describes is stable.

**Wave A gate:** DZS/DIP packages pass; Chapter 3 reaches argumentative rather
than numerical completeness; no Part I exercise asks for R production; the
six-critic panel passes all four units; the Chapter 3 portions of R07 and R24,
plus R31, R33, and the first transition in R27, are closed.

#### Wave B — constructed data and descriptive argument, Chapters 4–6

1. **Chapter 4:** show source data becoming an analysis table through unit
   checks, joins that can multiply rows, recodes, filters, totals/components,
   duplicates, missing/suppressed values, and one visible sensitivity to a
   missing-data decision. Source the engagement-shape claim or label the data
   clearly as simulated; settle the unusually high definition count only after
   the spine decision. Plant the honest reporting sentence and add a static
   print exercise table.
2. **Chapter 5:** add the immediate Anscombe introduction; retain the graph-as-
   argument and accessibility focus; recheck figure density after prose is
   complete; use a small text-frequency view to prepare Chapter 17 without
   teaching NLP.
3. **Chapter 6:** repair correlation/range claims, make the scatterplot primary,
   treat Pearson/Spearman differences only as clues, qualify attenuation under
   range restriction, retrieve causal limits, and show how coded text
   categories can enter an association while remaining measurement decisions.
4. Complete the Part II claim bridge, self-check, first reach-back task, and
   communication-thread seed.

**Wave B gate:** DigiKat/Eurostat packages pass; the reader experiences rather
than merely hears about constructed tables and missingness; `fig-anscombe` has
an approved introduction; R11's analysis-table portion, R17's seed, R28, and
the Chapter 6 portion of R35 are closed.

#### Wave C — inference and second identity pillar, Chapters 7–12

1. **Chapter 7:** state independence/weak-dependence and finite-variance
   conditions for the CLT at the intended level, develop probability as degree
   of belief, reduce cognitive overload, and add the midpoint retrieval pause.
2. **Chapter 8:** preserve the simple-random-sampling simulation while adding
   coverage, nonresponse, probability versus opt-in recruitment, weights,
   design effects/effective sample size, unequal selection probabilities,
   clustering, the finite-population correction, and one weighted/unweighted
   comparison. Separate SRS formulas from broader probability designs and
   qualify the claim that a survey of roughly one thousand people is generally
   enough. Distinguish population generalisation from train/validation/test splitting.
   Retrieve text as a sampling problem by asking which speeches, platforms,
   dates, languages, and speakers could enter a corpus.
3. **Chapter 9:** repair interval/bootstrap claims, state failure cases, develop
   estimate + interval + population language, and add print presets. In
   particular, remove the claim that mean ± 1.96 standard deviations is a
   generic prediction interval and do not use a z-interval coverage experiment
   as validation of a percentile-bootstrap median interval. Restore the
   code-reading progression. Use one brief coded-text proportion to show that
   sampling uncertainty does not absorb coding or measurement uncertainty.
4. **Chapter 10:** integrate the approved correction, the main ASA episode,
   balanced frequentist/Bayesian framing, and the proper error/assumption
   language. Prepare Chapter 17 by distinguishing a statistical error rate from
   an infallible “ground truth” when reference labels themselves can be wrong.
5. **Chapter 11:** complete effect-size, power, error-consequence, assumption,
   and reporting-language repairs without generalising one simulated
   exaggeration factor or turning low power into a blanket verdict; restore the
   fixed chapter order and add print presets.
6. **Chapter 12:** author the second identity pillar only after Chapters 9–11
   pass. Follow one lifecycle from an attractive finding through analytic
   flexibility, incentives, selection, replication, reform, reform limits,
   auditable transformation, one sensitivity comparison, and one forest plot.
   Include primary evidence, privacy/open-material trade-offs, the AI
   verification stage, visible code as evidence of analytic branching, and no
   code-production task. Close 12→13 with a reformed-practice contract.
7. Complete the Part III and Part IV claim bridges, self-checks, and reach-back
   tasks.

**Wave C gate:** Chapters 8 and 12 pass full panels; the weighted/unweighted
comparison and forest plot are verified; the inference-chapter portions of R09
and R12, R18, R19, R24's open-science portion, R27's second transition, R29's
Chapter 7 portion, and the relevant portions of R32/R35 are closed.

#### Wave D — models, published results, text, and deployed AI, Chapters 13–17

1. **Chapter 13:** correct the residual/calibration statement; strengthen the
   Part V contract; use adjusted standardised residuals or correctly name
   Pearson residuals, and distinguish type-I calibration from power; use
   denominators, weights, and a governed empirical survey example; plant
   categorical/text denominator literacy.
2. **Chapter 14:** integrate the Welch/OLS repair, empirical survey comparison,
   code-reading artifact, and dependence stop rule.
3. **Chapter 15:** stop using informal variance-ratio screening as proof;
   restore suspect code; add the dependence stop rule; preserve Chapter 16's
   synthesis payoff.
4. **Chapter 16:** choose and maintain one estimand; correct latent versus
   observed truth, prediction time, and leakage; harvest the shared causal
   diagram and show why adjusting for every variable can create bias; add
   interactions/heterogeneity; add a bounded bridge for binary outcomes, odds
   ratios, and predicted probabilities; annotate one real results table and a
   shorter results paragraph without refitting; restore the planned short Bayes
   outlook; develop honest conditional reporting; add dependence and midpoint
   retrieval.
   Include one explicit cross-design comparison, preferably ESS self-reported
   media use against DigiKat platform-visible traces, to show why two measures
   with a shared everyday label do not represent the same construct, unit, or
   population.
5. **Chapter 17:** author the third identity pillar only after Chapters 13 and
   16 and the text package pass. Follow corpus and unit → coding frame → human,
   dictionary, and AI labels → held-out evaluation → thresholds and confusion
   table → subgroup errors → disputed recorded label → procedural fairness and
   appeal → monitoring, feedback, shift, and language models as prediction
   systems. Treat selective observation and label construction as sources of
   error. Use “recorded reference outcome,” not “truth.” Retain the fairness
   widget and use the empirical text package in the worked example. Remove all
   R-production tasks and close 17→18.
6. Complete the Part V bridge, self-check, reach-back tasks, and the stable
   terminology pass across Chapters 13–17.

**Wave D gate:** ESS is usable through its approved lane; ParlaMint/ParlaSent
passes the package contract; the results-table source and reproduction rights
are verified; Chapters 16 and 17 pass full panels; R13, R14, R16, R29, the
chapter-level portions of R22/R23, R24's algorithm/AI portion, R27's third
transition, and the remaining model-chapter portions of R35 are closed. R22
remains open until Appendix D passes in Phase 5.

#### Wave E — capstone harvest, Chapter 18

1. Make prerequisites explicitly whole-book cumulative.
2. Retain one known-truth guided study and do not introduce a new method.
3. Make the analysis table visibly constructed and audit units, exclusions,
   transformations, and missingness.
4. Include a substantive sensitivity check that can change the conclusion's
   boundary without reducing the comparison to significance/no significance.
5. Require the student to write an honest report and then audit an assistant's
   report on the same analysis.
6. Add one bounded empirical transfer task whose evidence package contains a
   dataset passport, source/version, transformation log, analysis, sensitivity
   check, claim boundary, AI-use record, and disclosure.
7. Explicitly close all four promises, six claim dimensions, seven threads, and
   the distinction among statistics, data science, machine learning, and a
   deployed AI system. State why the explanatory main study does not use every
   Chapter 17 tool.
8. Frame respondent privacy as the book's dated conservative policy under D15,
   not as an undated universal legal conclusion.

**Wave E gate:** Chapter 18 passes all chapter checks and its full panel; the
evidence package works in HTML, print, R, and the supported no-code route; R17's
harvest, R24's final protocol, R32's transfer task, and all prerequisite repairs
are closed.

### Phase 5 — complete assessment, appendices, and learning pathways

Most new closure material is authored with its chapter in Phase 4. This phase
finishes earlier units and verifies the system as a whole.

1. Audit all 19 units. Every `callout-greska` gets the intended error, the
   revealing diagnostic, and at least one plausible non-answer. Conceptual and
   critical tasks get model-response components; computational tasks get a
   numerical answer and independent check; `revizija modela` gets a ranked
   rubric distinguishing fatal errors from useful improvements.
2. From Chapter 6 onward, make one exercise retrieve material from at least two
   chapters back. Verify each part self-check against the ratified thread map.
3. Give every widget-dependent exercise a static preset table or aggregate that
   can be completed in print, especially Chapters 4, 9, and 11.
4. Complete Appendix A with a real standalone data loader and coverage through
   Chapters 6–16, using the same files and variable names as the chapters.
5. Implement D09. For every supported Appendix B analysis, pin the jamovi
   version/module, record import types, menu route, settings, filters/weights,
   expected output, golden values, export, verification, interpretation, and
   claim boundary. Test on a clean installation.
6. Generate Appendix C and `podaci.qmd` from `data/katalog.yml` and make all
   student downloads work.
7. Complete Appendix D's decision/recovery aid and add the explicit “no method
   in this book is adequate” route for repeated, clustered, longitudinal, and
   network-linked observations.
8. Regenerate Appendix E only after terminology and definitions are final.
9. Complete Appendix F as a copyable protocol from question and data-sharing
   decision through prompt, verification, sensitivity, provenance, disclosure,
   monitoring, and appeal. Distinguish tool-access/privacy lanes.
10. If D10 is ratified, update every configuration-driven inventory first, then
    add Appendix G and sanctioned `podsjetnik` references without improvised
    inline styling.
11. Confirm the two visible reading routes and narrow any public claim not fully
    delivered by Appendix B or the student-solution route.

**Exit gate P5:** R15, R20–R24, R32, R34, and R35 are closed; R25 reaches
`verified` and remains open until Phase 6 reconciles declared and actual source
use; Appendix G has an implemented or explicitly rejected disposition;
Appendix A/B use the same data and expected values; protected solutions do not
leak into public AI exports.

### Phase 6 — whole-book continuity, evidence, and editorial pass

1. Run continuity scans for structure, terminology, notation, prerequisites,
   definitions, and all plant/develop/harvest links.
2. Verify the claim dimension and the unavailable claim in every sustained
   vignette, worked example, wild claim, and AI audit.
3. Repair the 3→4, 12→13, and 17→18 transitions, then all part bridges, against
   the ratified spines.
4. Rebalance recurring Berkeley, Anscombe, ASA, survey, and AI cases so every
   recurrence asks a new question. Vary widget, worked-example, and AI-box
   opening formulas without replacing one template with another.
5. Run the complete H1–H10 style process, including manual Croatian voice,
   rhythm, simulation-before-formalism, notation, code register, and sentence-
   level H7/S9 evidence and uncertainty checks.
6. Check every figure introduction and alt text, every widget's prose before and
   after, every table caption/source, every definition/term relationship, and
   every print twin.
7. Reconcile actual dataset consumers with the catalogue, public data page,
   Appendix C, README, bibliography, AI exports, and chapter metadata.
8. Ensure every substantively changed chapter has one full six-critic panel
   after its last material change. Do not duplicate a still-valid packet panel.
   If Phase 6 materially changes a panelled chapter, rerun the full panel; if it
   makes only a mechanical change, rerun the invalidated deterministic checks.
   Resolve fatal and major findings first and present one revision packet for
   approval.
9. Run the whole-book voice and narrative-arc panel only after chapter panels
   are stable. Treat disagreements as explicit editorial trade-offs rather than
   averaged scores.
10. Obtain a domestic terminology review and an independent statistical review
    of the final methods spine.

**Exit gate P6:** R07, R27, R28–R31, R33, and R36 are closed; every accepted
content/editorial item due through P6 has completion evidence; reader,
artifact-proof, and final release children remain open for Phases 7–8; no
chapter remains at a stage below its actual completed gate or above its verified
gate.

### Phase 7 — release-candidate validation and reader acceptance

1. Freeze a release-candidate commit and locked environment. Run the release
   matrix from a fresh clone or clean temporary worktree, restore only declared
   lockfiles and committed data, and do not rely on `_freeze`, warm caches,
   untracked files, or the developer's installed packages.
2. Run a second focused reader validation on Chapters 3, 12, 17, and the
   Chapter 18 evidence package. Prefer fresh intended-audience readers; record
   only repeated or blocking findings as release tasks.
3. Run semantic accessibility testing, keyboard-only use, visible focus, live
   regions, 200% zoom/reflow, contrast, reduced motion, alt text, and a
   screen-reader sample. Declare HTML the primary accessible edition unless a
   stronger PDF target is explicitly approved.
4. Proof PDF for embedded intended fonts, grayscale encoding, figures,
   cross-references, contents, blank/truncated pages, and extracted text.
5. Proof DOCX in Word or LibreOffice for callouts, equations, captions,
   figures, styles, Croatian characters, and contents.
6. Rebuild and compare HTML, teaching HTML, PDF, and DOCX from the same commit.
   Record tool versions, commit, environment locks, dataset hashes, and artifact
   hashes.
7. Run Bookwright conductor `check` for every chapter. Advance to `final` only
   when every blocking item passes and the author signs off.

**Exit gate P7:** no unresolved blocker or major first-edition finding; all
builds and proofs pass from one source state; reader findings are incorporated;
the release candidate has legal, statistical, pedagogical, accessibility, and
editorial sign-off.

### Phase 8 — publish a citable and correctable edition

1. Freeze the final title, authorship, version, date, citation metadata, and
   colophon disclosure.
2. Write the Croatian reader-facing changelog and update the dated errata log.
3. Create the final tag from the accepted release candidate.
4. Archive that exact tag with a persistent identifier and record it in the
   citation block.
5. Publish the term-frozen teaching edition and retain a clearly identified
   moving development edition if desired.
6. Deploy and smoke-test canonical book pages, data downloads, PDF, citation,
   changelog, and errata submission route.
7. Record artifact checksums and the final review-register snapshot.

**Exit gate P8:** R06 is closed in full; the public edition is tagged, archived,
citable, downloadable, and correctable; the ledger and implementation register
match the released source state.

---

## 6. Standard operating procedure for every chapter packet

Use this sequence for each chapter. Do not combine unrelated chapters in one
write pass merely because they are in the same part.

1. **Select the packet.** Name the chapter, review IDs, ratified spine, thread
   roles, prerequisites, and intended stage transition.
2. **Read the full context.** Read the chapter top to bottom, its adjacent
   chapters, `STYLE.md`, `ENRICHMENT.md`, relevant blueprint section, spine,
   concept ledger, bibliography, and dataset passports.
3. **Run the baseline checks.** Style lint, structure scan/rhythm, figure-
   introduction detector, widget contract if applicable, and targeted render.
4. **Prepare an approval packet.** For each substantive change give the exact
   anchor, value slot, Croatian draft, verified source/data, claim boundary,
   downstream consequence, and one or two rejected additions with reasons.
   Correctness repairs state the before/after statistical claim and test.
5. **Obtain approval.** Apply only approved enrichment, empirical material,
   contested interpretation, new source, or scope change. Mechanical repairs
   within an approved packet do not require a second decision unless they alter
   meaning.
6. **Edit one owner at a time.** Preserve unrelated worktree changes and do not
   let concurrent agents edit the same chapter or shared registry.
7. **Reproduce the analysis.** Start from a clean session; verify that prose,
   tables, captions, alt text, answers, and print twins use executed numbers.
8. **Complete the vertical slice.** Add the AI step, one planted error and key,
   four exercise tiers and feedback, reach-back task where required, print
   alternative, transitions, and data/source declarations with the prose.
   Every sustained empirical example ends by naming the additional observation,
   design, comparison, or measurement that could materially change its
   conclusion.
9. **Run Bookwright style and figure workflows.** Perform both deterministic and
   manual H1–H10 review; any missing figure introduction is drafted and approved
   before editing.
10. **Render and interact.** Preview the chapter, operate widget controls and
    reset by mouse and keyboard, inspect responsive/dark states, and compare the
    static twin.
11. **Run the six-critic panel.** Methods, skepticism, pedagogy, evidence,
    style, and structure read independently. Synthesis ranks severity before
    agreement and preserves disagreements.
12. **Approve and apply panel revisions.** Show accepted before/after changes;
    never insert an unverified citation or finding.
13. **Close the packet.** Rerun checks, update the implementation register and
    ledger with evidence, then commit the bounded change.

Use three approval tiers rather than forcing every task through the same
paragraph-by-paragraph workflow.

- **Tier M — mechanical or correctness packet.** The author/reviewer approves
  the statistical or structural specification; Codex applies and verifies it.
  A second approval is needed only if implementation changes the agreed
  meaning.
- **Tier E — bounded Book Enrich insertion.** Each one- or two-paragraph draft
  is shown before editing with its slot, anchor, verified source, and rejected
  alternatives, exactly as the skill requires.
- **Tier F — full identity rewrite.** The author first approves the brief,
  evidence/data contract, outline, and scope boundary. Codex drafts the coherent
  chapter on the bounded revision branch, runs the full panel, and presents one
  consolidated revision packet for acceptance. The pillar is not assembled as
  dozens of isolated insertion approvals.

Only the conductor/root owner writes `chapter-ledger.json`,
`chapter-spine.json`, `concept-ledger.json`, or `conventions.json`. Parallel
critics and workers remain read-only on shared registries and receive disjoint
chapter files. Immediately before a registry patch, re-read the live JSON,
preserve stable IDs and history, validate the schema, and inspect a
registry-only diff.

### Chapter acceptance evidence

A chapter cannot advance to final review unless it has:

- a ratified spine and consistent prerequisites;
- no fabricated or unsupported empirical material;
- registered dataset provenance/licence and reproducible chapter numbers;
- a clean targeted render and no TODO/placeholder;
- no continuity, terminology, notation, or definition contradiction;
- a full H1–H10 deterministic and manual pass;
- an introduction and alt text for every figure and widget/twin pair;
- the required vignette, widget/twin exemption status, AI pair, worked example,
  summary, terms, and four substantive exercise tiers;
- the agreed answer/key/rubric and print-completable path;
- a resolved six-critic report and author acceptance.

---

## 7. Verification ladder and commands

### Per edit

- `git diff --check`
- targeted style lint;
- conditional figure, widget, token, citation, data, and numerical tests;
- clean-session reproduction of changed calculations;
- H7/H9/H10 and Croatian-voice judgment;
- targeted preview and interaction.

### Per chapter

- style, structure, rhythm, and figure checks;
- citation/source fit and data-passport checks;
- exercise-closure and widget/twin tests;
- top-to-bottom read and six-critic panel;
- conductor chapter check and author acceptance.

### Per batch

- checks over the entire affected part/thread;
- concept graph, AI export, and data-catalogue freshness;
- full HTML and teaching-profile render;
- browser and accessibility matrix;
- continuity review against adjacent chapters and cross-book threads;
- HTML/print claim comparison.

### Whole book and release

- locked, clean builds of HTML, teaching HTML, PDF, and DOCX;
- citation, data, parity, accessibility, link, export, glossary, and metadata
  checks;
- whole-book voice/arc, statistical, terminology, legal, proof, and reader
  review;
- deployed smoke test and artifact provenance.

The existing commands are:

```powershell
git diff --check

python scripts/check-widgets.py .
python scripts/check-rendered-html.py docs

python bookwright_plugin/bookwright/scripts/run_rscript.py scripts/check-tokens.R

python bookwright_plugin/bookwright/scripts/run_rscript.py `
  bookwright_plugin/bookwright/skills/book-style/scripts/style_lint.R `
  "chapters/*.qmd" "dodaci/*.qmd"

python bookwright_plugin/bookwright/scripts/run_rscript.py `
  bookwright_plugin/bookwright/skills/book-continuity/scripts/structure_scan.R `
  "chapters/*.qmd"

python bookwright_plugin/bookwright/scripts/run_rscript.py `
  bookwright_plugin/bookwright/skills/book-continuity/scripts/structure_lint.R `
  "chapters/*.qmd"

python bookwright_plugin/bookwright/scripts/run_rscript.py `
  bookwright_plugin/bookwright/skills/book-figure/scripts/figure_intro_check.R `
  "chapters/*.qmd"

quarto preview chapters/<chapter>.qmd
quarto render
quarto render --profile kolegij
powershell -File scripts/render-book-pdf.ps1
powershell -File scripts/render-book-docx.ps1

python bookwright_plugin/bookwright/scripts/run_rscript.py R/build-ai-exports.R
python bookwright_plugin/bookwright/scripts/run_rscript.py R/build-concept-graph.R
```

Never run bare `quarto render --profile pdf`. New parity, exercise-closure,
data, citation-metadata, link, accessibility, artifact, and release checks are
implemented before the phase that first relies on them. Fail-closed build,
dependency locks, export safety, browser smoke, and widget parity are the Phase
1 critical path; full accessibility and artifact-proof automation may mature by
Phase 7.

---

## 8. Approval and outside-ask protocol

### Responsibilities and authority

| Role | Responsibility | Authority boundary |
|---|---|---|
| Codex | Prepare packets, inspect sources/data, edit approved scope, reproduce analyses, run checks/panels, maintain register/dashboard, and report evidence. | May not decide contested scope, rights, privacy, title/authorship, or public release; may commit only if A0 explicitly authorises local commits. |
| Author/editor | Ratify intellectual, pedagogical, voice, case, source, and first-edition decisions; accept chapter revision packets. | Owns substantive/editorial decisions and any deferral that changes a public promise. |
| Statistical reviewer | Sign off the Chapter 10/14 repairs and final methods spine. | Does not decide book voice or dataset rights. |
| Evidence/licence and data owners | Confirm provenance, reuse, redistribution, attribution, and source fidelity. | External permission cannot be inferred from technical access. |
| Course/institutional owner | Ratify assessment visibility and dated privacy/disclosure policy. | Local policy is not presented as universal law. |
| Readers, terminology reviewer, accessibility/proof reviewer | Supply novice, Croatian-convention, assistive-technology, and artifact evidence. | Findings are evidence for bounded revisions, not unsupervised edits. |
| Release owner | Create/archive the approved release and maintain the term freeze and errata route. | Push, tag, archive, and deploy require separate A6 authorisation. |

The author should not have to answer the same broad question repeatedly, but
unrelated owners and decisions must not be bundled into one blocker. Use these
independently closable approval gates.

| Gate | Decision packet | Owner | Latest safe point |
|---|---|---|---|
| A0 | This plan, D01–D16, branch/checkpoint choice, and local-commit authority | Author | Before Phase 0 closes |
| A1a | Chapter 10 correction specification | Author + statistical reviewer | Before P1A-C10 edits |
| A1b | Chapter 14 correction specification | Author + statistical reviewer | Before P1A-C14 edits |
| A1c | Navarro/book/generated-data licence decisions | Author + licence owner | Before affected prose/data publication |
| A1d | Edition/version/changelog/errata mechanism | Author + release owner | Before P1B-GOV edits |
| A2a | Claim map, lifecycle, audit questions, and cross-book threads | Author | Before spine ratification |
| A2b-I…F | One spine packet per part plus preface/finale | Author | Before that part's prose wave |
| A2c | Canonical terminology and reviewer route | Author/editor | Before definition changes |
| A2d | Answer policy, Appendix B/G scope, H10, AI ladder, and privacy/tool lanes | Author + course owner | Before new exercises/pathways |
| A3-DZS…TEXT | One selection/rights/chapter-role decision per dataset package | Author + relevant data owner | Before candidate promotion, not merely before prose |
| A4-03 | Chapter 3 brief, case, evidence, and outline | Author/editor | Before Chapter 3 full draft |
| A4-12 | Chapter 12 brief, evidence artifact, sources, and outline | Author/editor | Before Chapter 12 full draft |
| A4-16 | Published table/paragraph choice and reproduction rights | Author/editor | Before Chapter 16 artifact is added |
| A4-17 | Chapter 17 question, sampling rule, text package, and outline | Author/editor | Before Chapter 17 full draft |
| C00…C18 | One synthesised chapter/panel revision packet | Author | Before that chapter reaches `coauthor_review` |
| A5a | Accessibility target and proof disposition | Author + accessibility reviewer | Before final conductor checks |
| A5b | Final title/authorship/citation metadata | Author | Before release candidate freezes |
| A5c | Archive, errata, and term-freeze ownership | Author + release owner | Before Phase 8 |
| A5d | Release-candidate go/no-go | Author + named sign-off owners | After P7 passes |
| A6 | Explicit push/tag/archive/deploy authorisation | Author | Immediately before each external release action |

Every outside ask must contain one decision, the evidence already available,
the recommended default, what it blocks, and the exact reply needed. Do not
send an open-ended “please review the chapter” request.

External work that cannot be replaced by Codex includes:

- written redistribution permission where required;
- five-reader recruitment and consent-compliant session logistics;
- reproduction permission for a published table if quotation exceptions do not
  cover the chosen use;
- domestic terminology judgment where Croatian convention is divided;
- institutional approval of course privacy/disclosure language;
- accessibility/proof checks requiring human assistive-technology or print use;
- final archive, term-freeze, errata, and release ownership.

If one of these is delayed, continue only with work that does not presuppose its
answer. For example, portal-mediated ESS infrastructure can proceed while
permission is pending, but chapter prose must not claim a bundled local extract.

---

## 9. Review-item coverage matrix

This matrix is the minimum completeness check. The implementation register adds
owners, files, status, and evidence links.

| Review ID | Primary phase | Closure evidence |
|---|---|---|
| R01 Chapter 10 null/assumptions | 1A, Wave C | Correct claim, `(b+1)/(B+1)`, reproduced widget/example, methods review |
| R02 Chapter 14 Welch/OLS | 1A, Wave D | Same-estimate/different-inference explanation, reproduced outputs, methods review |
| R03 licences/access lanes | 1B, 3 | Provenance audit, explicit generated-data licence, per-package licence/redistribution records |
| R04 ratified spines | 2 | All 19 `ratified: true`, approved aspects/terms, regenerated concept artifacts |
| R05 safe PDF release | 1C, 7 | Wrapper-only blocking CI and stale-artifact failure test |
| R06 citable edition | 1B, 8 | Version/tag, changelog, archive identifier, citation, term freeze, errata route/log |
| R07 identity pillars | Waves A/C/D | Complete single-argument Chapters 3/12/17 and passing panels |
| R08 empirical layer | 3, Waves A–D | Accepted first portfolio, package tests, actual chapter use |
| R09 assumptions/estimands | 1A, Waves B–E | Chapter repair matrix closed and methods reviewer acceptance |
| R10 claim map/lifecycle/threads | 2, 4, 6 | Ratified map and verified plant/develop/harvest audit |
| R11 analysis table/missingness | Waves A/B/C/E | Visible pipeline, join/duplicate audit, consequential missing-data sensitivity |
| R12 survey realism | Waves A/C/D | Coverage/nonresponse/weights, weighted comparison, sampling/test-split distinction |
| R13 text as data | 2, 3, Wave D | Licensed text package and complete Chapter 17 worked example |
| R14 binary/causal/heterogeneity | Waves A/B/D | Shared DAG vocabulary, interaction harvest, odds/probability reading bridge |
| R15 assessment closure | 2, 4, 5 | Every unit has keys/answers/checks/rubrics under verified visibility policy |
| R16 published results genre | Wave D | Verified annotated table and paragraph, no refitting |
| R17 communication thread | Waves B–E | Estimate/interval/population/claim/limit progression and report/AI audit |
| R18 widget parity | 1C, 7 | 17 exact/distributional records and passing golden tests |
| R19 sensitivity/forest plot | Waves C–E | One forest plot and routine defended sensitivity comparisons |
| R20 Appendix A | 5 | Standalone loader and Chapters 6–16 route using canonical files/values |
| R21 Appendix B | 2, 5 | Versioned verified core companion or narrowed public promise |
| R22 Appendix D/dependence | Waves D, 5 | Decision/recovery aid and explicit stop/routing rules |
| R23 H10/no code production | 2, 4, 6 | Part ladder preserved, prohibited exercises removed, code artifacts audited |
| R24 AI/ethics/distinctions | 2, 4, 5 | Cumulative ladder, sourced claims, Appendix F, stable four-way distinctions |
| R25 single data catalogue | 3, 5, 6 | `katalog.yml` generates both views and reconciles all consumers |
| R26 novice pilot/times | 3, 7 | Five-reader memo, incorporated findings, measured reading-time updates |
| R27 three transitions | Waves A/C/D, 6 | 3→4, 12→13, and 17→18 verified against spines |
| R28 Chapter 5 figure intro | Wave B | Detector pass and approved contextual paragraph |
| R29 retrieval pauses | Waves C/D | Explicit midpoint retrieval in Chapters 7 and 16 |
| R30 repetitive formulas | 6 | Manual voice/rhythm pass and whole-book voice panel |
| R31 ASA/public cases | Waves A/C | Chapter 3 distinct public case; ASA chiefly Chapter 10 |
| R32 print presets | 4, 5 | Static data for every widget-dependent exercise and tested print completion |
| R33 preface inquiry | Wave A | Genuine miniature inquiry and beginner test |
| R34 numeracy refresher | 2, 5 | Ratified Appendix G or documented alternative; all first-use recalls verified |
| R35 reach-back/self-check | 4, 5 | One reach-back task from Chapter 6 onward and answerable part checks |
| R36 Croatian terminology | 2, 6 | Canonical registry, alternatives/departures, domestic expert review |

### Reconciled review contradictions

These are tracked separately so they are not accidentally reintroduced.

| Conflict | Resolution in this plan |
|---|---|
| Review implies visible Part I code; ratified H10 forbids it | Preserve no-visible-code Part I; remove assessed code production. |
| Review calls answer delivery open; `STYLE.md` currently fixes it to `kolegij` | Ratify D06 and update style, build, and exports together. |
| Review schedules data after data-dependent prose | Move governance earlier and build packages just in time before each wave. |
| Review says decide Chapter 17 before widget production; widget already exists | Retain fairness widget; text analysis becomes worked example. |
| Appendix G conflicts with fixed A–F architecture | Ratify D10 and make inventories configuration-driven before adding it. |
| Review treats title as canonical; blueprint calls it working | Freeze D14 before citation metadata and release. |
| Review and blueprint differ on 84,000/86,000 words | Use argumentative completeness and structural rhythm; preserve pillar ambition. |
| Detailed portfolio and rhetorical design-diversity list differ | First portfolio is required; second-wave datasets remain admission-rule dependent. |
| Alternative structures are mutually exclusive | Preserve current order; two-track map is navigation; distributed pillars are fallback only. |
| Release governance is needed early but a final tag would freeze unfinished work | Build mechanisms in Phase 1; tag/archive only in Phase 8. |
| Bookwright gate names H1–H9 although style has H10 | Repair the gate definition in Phase 0. |

---

## 10. How to execute this plan with Codex

### Packet and work-in-progress rule

A “batch” in §5 is a milestone, not an edit unit. An executable packet owns one
chapter or one shared subsystem. Keep at most one write packet `in_progress`.
Independent source checks, reader recruitment, rights requests, and read-only
critics may run in parallel, but no parallel worker edits the same chapter or a
shared registry.

Use these stable packet IDs in the stated order. Items separated by commas are
executed individually from left to right unless the preceding packet's evidence
explicitly permits a harmless parallel read-only audit.

| Order | Packet IDs | Codex action and durable output | Author action / exit |
|---|---|---|---|
| 1 | `G-A0` | Present D01–D16, checkpoint/branch choice, and commit authority. | Ratify A0; no edit before reply. |
| 2 | `P0-BASE`, `P0-CONTROL`, `P0-REGISTER`, `P0-STATE`, `P0-OUTSIDE` | Baseline report; register/handoff/dashboard control layer; atomic review inventory; valid Bookwright state/plugin; bounded outside asks. | Confirm zero unmapped findings and P0. |
| 3 | `G-A1a`, `P1A-C10`, `P1A-C11`; `G-A1b`, `P1A-C14`, `P1A-C15`, `P1A-C16` | Approved method specifications, surgical corrections, reproduced values, independent methods findings. | Approve A1a/A1b before edits; accept correction evidence. |
| 4 | `P1A-C02`, `P1A-C06`, `P1A-C07`, `P1A-C08`, `P1A-C09`, `P1A-C13`, `P1A-C18` | One connected assumption/estimand correction packet per chapter. | Accept each packet; no enrichment yet. |
| 5 | `G-A1c`, `P1B-NAVARRO`, `P1B-DATA-LIC`; `P1B-BIB`, `P1B-META`; `G-A1d`, `P1B-GOV` | Provenance/licence decisions, verified bibliography/metadata, release-governance skeleton. | Ratify rights and governance separately. |
| 6 | `P1C-LOCK`, `P1C-PDF`, `P1C-EXPORT`, `P1C-PARITY`, `P1C-BROWSER`, `P1C-INVENTORY` | Locked dependencies, fail-closed PDF, safe exports, 17 parity records, portable browser smoke test, configuration-driven inventories. | Confirm P1 evidence. |
| 7 | `G-A2a`, `P2-CLAIMS`; `G-A2d`, `P2-ASSESS`; `P2-IDENTITY`; `G-A2b-I…F`, `P2-SPINE-I…F`; `G-A2c`, `P2-TERMS`; `P2-DOCS` | Ratified claim/lifecycle/thread system, assessment contract, three pillar briefs, spines by part, terms, and reconciled governing documents. | Ratify each gate before the corresponding registry/document write. |
| 8 | `P3-CATALOG`, `P3-EXISTING` | Catalogue/validator/generator and registered current datasets. | Accept contract before new package promotion. |
| 9 | `G-A3-DZS`, `P3-DZS`, `G-A3-DIP`, `P3-DIP` | Validated DZS/DIP candidate packages and passports. | Approve each exact selection/rights packet. |
| 10 | `P3-PILOT` | Five-reader baseline memo for the surgically corrected—not future Wave-rewritten—Chapters 1, 8, and 16. | Accept findings/reading-time tasks before identity prose. |
| 11 | `WA-C00`, `WA-C01`, `WA-C02`; `G-A4-03`, `WA-C03`; `WA-PART` | Part I vertical chapter packets, full Chapter 3 rewrite, panel reports, bridge/self-check. | Approve each Tier E/F packet and C00–C03 dispositions. |
| 12 | `G-A3-DIGIKAT`, `P3-DIGIKAT`, `G-A3-EUROSTAT`, `P3-EUROSTAT`; `WB-C04`, `WB-C05`, `WB-C06`, `WB-PART` | Validated packages and Part II chapter/part packets. | Approve package selections and C04–C06. |
| 13 | `WC-C07`, `WC-C08`, `WC-C09`, `WC-C10`, `WC-C11`; `G-A4-12`, `P3-EVIDENCE12`, `WC-C12`; `WC-PARTS` | Stable inference sequence, Chapter 12 evidence artifact/full rewrite, Part III/IV checks. | Approve Chapter 12 brief/sources and C07–C12. |
| 14 | `G-A3-ESS`, `P3-ESS`; `WD-C13`, `WD-C14`, `WD-C15`; `G-A4-16`, `WD-C16`; `G-A4-17`, `G-A3-TEXT`, `P3-TEXT`, `WD-C17`; `WD-PART` | Approved ESS lane, stable model chapters, published-results artifact, validated text package, full Chapter 17 rewrite. | Approve each rights/brief packet and C13–C17. |
| 15 | `WE-C18` | Final capstone/evidence package and C18 panel disposition. | Approve C18. |
| 16 | `P5-CLOSURE-00…18`, `P5-A`, `P5-B`, `P5-C`, `P5-D`, `P5-E`, `P5-F`, `P5-G`, `P5-ROUTES` | One closure audit per unit, completed/gated appendices, canonical student pathways. | Accept P5 and any narrowed promise. |
| 17 | `P6-CONTINUITY`, `P6-EVIDENCE`, `P6-STYLE`, `P6-FIGURES`, `P6-DATA`, `P6-PANELS`, `P6-ARC` | Final cross-book reconciliation and last-valid critic evidence. | Accept only required post-change chapter packets and whole-book trade-offs. |
| 18 | `P7-PILOT`, `P7-A11Y`, `P7-HTML`, `P7-PDF`, `P7-DOCX`, `P7-CLEAN-BUILD`, `P7-CONDUCTOR`; `G-A5a…d` | Reader/accessibility/proof evidence and clean release-candidate report. | Named sign-offs and A5d go/no-go. |
| 19 | `G-A6`, `P8-META`, `P8-TAG`, `P8-ARCHIVE`, `P8-DEPLOY`, `P8-SMOKE` | Citable tagged/archive/deployed edition and final dashboard/register snapshot. | Author explicitly authorises each external action. |

Use these exact prompt forms.

- Decision gate: `Prepare <gate ID> only. Show the evidence, recommended
  default, alternatives, what it blocks, and the exact reply needed. Do not edit.`
- Shared subsystem: `Execute <packet ID> only under the ratified gate. Update
  the register and dashboard, run its exit checks, and do not start the next packet.`
- Bounded enrichment: `Prepare <chapter packet ID> as Tier E. Show slot,
  anchor, Croatian draft, verified source, and rejected candidates. Do not edit.`
- Identity rewrite: `Prepare <chapter packet ID> as Tier F. Show the brief,
  evidence/data contract, outline, scope exclusions, and acceptance tests. Do not draft yet.`
- Apply an approved chapter: `Apply approved <chapter packet ID>, verify it,
  run its six-critic panel when stable, and present one Cxx revision packet.`
- Closeout: `Close <packet ID> only if every stated gate passes; otherwise keep
  it open and report the failed gate and safest next action.`

At the end of every packet, Codex returns exactly six things:

1. review and decision IDs addressed;
2. files changed;
3. substantive decisions implemented;
4. checks run and their results;
5. incoming handoffs consumed, outgoing handoffs created, and unresolved
   outside asks or risks;
6. the next permitted packet, why it is unblocked, and its exact copy-paste
   prompt.

The universal fresh-thread prompt lives in the dashboard. A new thread always
reads the four control files, resumes an existing active packet if present, or
takes `next_permitted_packet`; it never selects a later packet from memory.

If a packet fails its exit gate, fix it before starting downstream prose. If a
new recommendation appears, admit it only after identifying the thread it
serves, the existing material it replaces or extends, its evidence/data cost,
and its first-edition priority. This is how the plan remains robust without
turning the revision into an ever-expanding wish list.

---

## 11. Final go/no-go rule

The first edition is a **go** only when:

- every accepted R01–R36 item is verified;
- every deferred item has an explicit first-edition rationale and does not
  contradict a public promise;
- all 19 spines and applicable chapter gates pass;
- Chapters 3, 12, and 17 carry the promised contemporary identity;
- Chapters 8, 16, and 18 still function as hinge, summit, and capstone;
- the data portfolio, assessment feedback, appendices, and student downloads
  work from the same canonical files;
- statistical, evidence, licence, accessibility, reader, editorial, and release
  owners have signed off;
- the exact release source is tagged, archived, citable, term-frozen, and tied
  to a public errata mechanism.

Anything less remains a pre-release draft, however polished its website or
successful its render.
