# PDF visual verification

Delivered artifact: `pdf/Statistika.pdf`, 531 pages, SHA-256 `1fc147a491ad4dc7271294ba6115eabc8877e3150afc42ca9c5d5ccb63fd3ae2`.

Page numbers below are physical PDF pages, not printed folios. The six Bookwright critics worked independently and read-only. Earlier candidates received broader reviews; these final checks target changes made after those reviews. They do not certify an image-by-image reread of all 531 delivered pages.

## Delivery candidate 16

- The structure critic checked all 257 internal apparatus page links: every destination matches the page printed in the locator.
- Apparatus pages 475–490 preserve the reviewed layout. Ten pages are pixel-identical to candidate 13; six change only the chapter 7 term-list locator from printed page 184 to 183 and were visually rechecked.
- Page 413 keeps the chapter 16 error heading and its full exercise together. The table remains complete and readable. Substantial whitespace before it on page 410 remains an unresolved layout recommendation.
- Root text verification finds no unresolved citation keys, unresolved references, replacement characters or inverted-question-mark defects. All required print apparatus and answer strings are present.
- The canonical PDF, staging PDF and `docs/pdf/Statistika.pdf` have identical hashes.

## Immediately preceding targeted visual checks

Candidate 14's final unchanged probability layout on page 182 contains the explanation, both histograms and caption together. All bars, axes, labels and the reference line remain legible. Its chapter 3 callout now fits completely on page 79; page 80 no longer begins with the two-line tail. The detector's grammatical agreement is corrected in source and PDF text.

Candidate 13's evidence critic inspected pages 73–75, 79–80, 83–84 and 122–123. The moved truncated-axis demonstration and its introductory decomposition are coherent and complete. The two issues found there—the detector agreement and callout tail—were corrected in candidate 14.

Candidate 13's methods critic inspected pages 183, 354, 369–371, 466, 506, 508 and 510. Checks cover the simulation reference line, pooled SD and standardised difference, all three ANOVA states, policy framing and the new printed answers. Values include pooled SD 1.9957, difference 1.1857, d approximately 0.5941; ANOVA F values 0, 24 and 7.14; margins ±2.94 and ±1.47; interval 4.525–5.105; and bootstrap medians 134 and 83. The chapter 7 exponent renders as a superscript. No clipping, overlap or numerical defect was found in these checks.

Root inspected candidate 13 pages 182–183, 207–211 and 409–413. The two chapter 8 tables fit completely on pages 209 and 211. The probability-layout whitespace was corrected subsequently. The regression table's following prose now flows onto the same page, and the exercise heading is protected, but the preceding whitespace remains recorded.

Candidate 13's structure critic inspected page 441 and all apparatus pages 475–490. The named-example map, complete internal-comma term, dataset descriptions, notation table, AOR row and all 257 links passed. Candidate 12 separately verified all six part introductions on pages 15, 91, 173, 249, 315 and 439; the moved finale was rechecked at 441 in candidate 13.

Earlier evidence checks covered the Berkeley evidence, measurement rows, domain counts, logarithmic caption, axes and full clickable URL targets. Earlier methods checks verified the interval miss counts 3/0/1, skewed-coverage simulation 8,622/10,000, and power detections 68, 107, 170, 239, 281 and 299 out of 300. Independent numerical recomputation is retained in `verify-numerical.R` and `validation/numerical.log`.
