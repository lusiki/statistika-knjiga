# October PDF audit revision — 23 October 2026

The PDF was revised from the current October manuscript, using all four supplied audit documents, the implementation handoff, and `mechanical_checks.R`. This report distinguishes the delivered corrections from recommendations that remain open. It is not a declaration that all audit findings are closed or that the book is ready for publication.

## Delivered artifact

`pdf/Statistika.pdf` contains **531 pages** and **5,828,245 bytes**. Its SHA-256 is `1fc147a491ad4dc7271294ba6115eabc8877e3150afc42ca9c5d5ccb63fd3ae2`. The copy at `docs/pdf/Statistika.pdf` is byte-identical. Both derive from the staged source manifest, which verifies 144 current files without drift.

The finding register currently records 381 implemented, 2 already resolved, 39 rejected with evidence, 79 partially implemented, 131 not implemented, 0 awaiting verification, and 1 awaiting an author decision. These counts are reported to make the remaining scope explicit, not to imply that all supplied recommendations were completed.

## Inputs and preservation

- `Audit_chapter_audits.md`, including the independent reruns for chapters 5, 9 and 11.
- `Audit_structural_round.md`.
- `Audit_mechanical_round.md` and its supplied R script.
- `Audit_reader_logs.md`, including narrative observations beyond the severity tables.
- The attached handoff beginning “The audited book is Osnove statistike za društvene znanosti”.

The original working manuscript and PDF were backed up in `tmp/audit-2026-10-23/before-revision.zip`. The baseline PDF SHA-256 is `ff063a4bb2027d9bab792ae55f8c36a9a5b9ab83970ffaec62938fa667949d21`. The baseline contained substantial uncommitted work; it was not replaced with Git HEAD.

This is the separately authorised October editorial revision. It does not close the earlier P6-VERIFY packet or change the comprehensive-review register. No push, release or deployment was performed.

## Implemented corrections

All seven P0 problems in the handoff were repaired.

| Handoff | Result |
|---|---|
| P0-01 | Chapter 5's truncated-axis panel genuinely starts at 15, retains every bar, and marks the break. |
| P0-02 | The four-display example now renders four actual displays from the same 72 observations. |
| P0-03 | Chapter 9's interval figure, preset table and answer use the same stored simulation. The three preset miss counts are 3, 0 and 1. |
| P0-04–05 | Chapter 11 retains the logical significance mask, counts detections correctly, and regenerates power and dependent prose. Counts are 68, 107, 170, 239, 281 and 299 out of 300 valid studies. Exclusions remain explicit. |
| P0-06 | Chapter 13 has a complete explanation of its static printed scenarios. Interactive instructions remain format-gated. |
| P0-07 | Shared number formatting/font handling and affected figures were rebuilt; thousands separators are legible. |

Additional substantive repairs include the Berkeley aggregate and department evidence; all twelve measurement-example rows; the election denominators; the Pearson construction; restricted-range illustration; t critical values and Welch degrees of freedom; interval-method identification; pooled-SD calculation; reconstructed replication estimates; sparse-table cautions; paired-data figures; multiple-comparison intervals; the full regression equation; logistic-model interpretation; classification metric denominators; and the capstone's age adjustment, residuals and scope.

Printed exercises now include direct calculation of spread, sampling error, normal interval bounds, a complement probability and a hand bootstrap. Their canonical answer records were updated, and the printed answer apparatus was regenerated. There is at least one printed check for every numbered chapter; this is not a claim that every exercise has a printed solution.

The print apparatus now includes chapter navigation, a bilingual term list with chapter/page locators, a dictionary of the two recurring teaching datasets, and a notation list. A named-example map connects Berkeley, Anscombe, DigiKat, ParlaSent and the registered replication to their chapters. The six part-divider pages have short reading introductions. The glossary points honestly to chapter-end term lists; it is not a comprehensive defining-page index.

The final reconciliation moves the corrected two-axis demonstration into the initial graphics explanation, defines the detector before its first calculation, and narrows the election verification to inputs actually printed. It completes all three ANOVA illustration states and chapter 14's pooled-SD arithmetic. Optional survey-design detail moves from chapter 8 to the practicum, with a compact explanation and pointer retained in print. Chapter 18 now presents the dated course policy explicitly as an example.

Typography repairs include decimal commas in formulas, grouped thousands, prose minus signs, readable short tables, continuation captions and repeated table heads. A rendering defect in the Shmueli bibliography title was corrected without changing the title. Printed URL footnotes retain the complete clickable target while keeping the filename together.

## Verification

The canonical build is produced through `scripts/render-book-pdf.ps1`. A clean staging directory under `tmp/audit-2026-10-23/render` avoids the slow recursive scan of the large working tree. The final staged source hashes are recorded in `render-source-manifest.json`. After rendering, one prompt fingerprint and its generated HTML-comment checksum were reconciled; `post-render-metadata.json` preserves both hashes and proves that the printed answer projection is unchanged. No PDF-visible content changed after rendering. The generated PDF is copied byte-for-byte to `pdf/Statistika.pdf` and `docs/pdf/Statistika.pdf`; no generated HTML or execution cache was hand-edited.

`pdf-verification.json` records the delivered PDF's page count, hash and text checks. `page-map.json` maps the repaginated chapters. The durable `validation/` directory retains the build and check output.

Checks completed successfully include manuscript style/structure, citation integrity, figure introductions/contracts, data integrity, concept regeneration, design tokens, negative integrity fixtures and solution pathways. The independent numerical script `verify-numerical.R` recomputes the P0 examples and the added exercises. It also verifies the skewed-population coverage demonstration: 8,622 of 10,000 intervals cover the target at n = 20, or 86.2%, illustrating failure of the simple normal approximation in that setting.

Six independent read-only critics reviewed the changes in methods, evidence, skepticism, pedagogy, structure and Croatian style. Visual checks covered the corrected demonstrations, dense tables, figure labels, continuations, navigation and apparatus. Earlier candidates were inspected extensively, followed by targeted checks after the final rebuild. This is not a claim that every page of the final artifact was visually reread.

The assessment-architecture checker is **not green**. The final run retains eleven prompt-fingerprint mismatches from the pre-existing working tree, plus thirteen literal/content-contract failures. The original thirteen baseline fingerprint mismatches are recorded in `baseline-prompt-drift.json`; two of those prompts were subsequently changed in this revision and reconciled. Thirty prompts changed by this revision had their fingerprints updated narrowly. No blanket fingerprint reset was performed, and this report does not treat the failed architecture check as a pass.

## Supplied mechanical script

`mechanical_checks.original.R` preserves the supplied substantive checks. `prepare-mechanical-audit.py` generates a repaginated Windows-compatible run. Changes address the chapter ranges, printed-page offset, Windows locale/null sink and malformed output from the installed older Poppler text extractor. Valid surrogate pairs are reconstructed; isolated malformed code units are preserved as explicit escapes and logged in `poppler-decoding-notes.json`. The original numerical tests are retained.

The resulting report is `mechanical/results/round4_mechanical.md`. It contains known false positives, not an all-green summary:

- Repeated table numbers are intentional continuation captions.
- Three remaining hyphen-minus matches occur in executable code or console output.
- Decimal-comma matches include lists and adjacent values rather than faulty math spacing.
- The one-decimal percentages 18.0% and 0.7% correctly round 22/122 and 1/150; the old script tests them to two decimals.
- Apparent missing author names arise from text-extraction hyphenation. The source citation checker passes.
- The Greenland journal line is a normal continuation of its bibliography entry.

The script's URL regular expression does not yield a valid inventory on this extraction. Therefore `check-pdf-links.py` separately checks the actual PDF URI annotations and records HTTP results in `pdf-links.json`: 35 targets returned HTTP 200, ten returned 404, and sixteen returned 403. Some companion pages and downloadable data return 404 because the local companion resources have not been deployed. Publisher responses of 403 to automated access do not establish that a DOI is invalid. No publication was performed to change these results. The mandatory printed calculations do not depend on these downloads.

## Finding dispositions and remaining work

`findings.json` preserves 633 severity-table findings, source filenames and line numbers, with dispositions and evidence. Narrative reader logs were consulted but are not exhaustively represented by those 633 rows.

The register deliberately retains `partially_implemented`, `not_implemented` and `verification_pending` where appropriate, instead of falsely assigning one of the handoff's four closed dispositions. Compound findings often combine a repaired error with a still-unimplemented refinement. The exact original request remains available in each record.

Remaining work includes some repeated prose and citation-density proposals, further first-use and exercise refinements, a comprehensive defining-page index, more extensive chapter compression, and several optional figure/table refinements. In particular, physical page 410 retains substantial whitespace before the complete regression-example table on 411; it is recorded as unresolved. Ordinary unfinished editorial work is not relabelled as a permission requirement. Rejected proposals include blanket citation thinning contrary to STYLE H7, unsupported measurement bounds, unjustified fairness “must differ” wording, and changes that would falsify correctly generated results.

Publication metadata remains an actual author decision. The internal P8-META label was removed, but the colophon retains honest draft status. No ISBN/DOI, edition, licence, institutional policy or release approval was invented. The unpublished companion routes and assessment-architecture failures also remain release limitations.
