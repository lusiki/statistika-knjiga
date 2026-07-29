---
name: book-enrich
description: Thicken an under-developed chapter of the "Osnove statistike za društvene znanosti" book with one or two paragraph insertions that add real substance, following ENRICHMENT.md. Use whenever a chapter feels thin, when the user asks to enrich, deepen, or strengthen a chapter, or when a concept is stated but not unpacked. Every insertion fills exactly one of five value slots, uses international and theoretical material only, and is presented in chat for approval before any file edit. Never invents empirics; every number and study is cited against references.bib.
allowed-tools: Read, Edit
---

# Book Enrich

## Purpose
Add depth where a chapter is thin, without uniform padding or restatement. ENRICHMENT.md is the source of truth. Each addition fills exactly one of five value slots, or it is restatement and gets cut.

## The five value slots
1. Mechanism unpacking. The chapter states an outcome but skips the causal chain. Add the step by step how.
2. Empirical evidence. A claim leans on intuition. Add a cited finding from published social science research, with its magnitude and its uncertainty. Never a remembered number.
3. Comparative or cross system context. Place the topic against EU, OECD, institutional, or historical comparison.
4. Trade off or counterview. Add the principled counterview, binding constraint, or unresolved tension. Public choice especially demands this.
5. Methodological or identification note. Briefly explain how a claim is measured or identified.

## Hard constraint
No Croatian examples, no Croatian empirics, no HNB or MFin data, no domestic reform specifics. Those are the co-authors' to add. Stay on theory, mechanism, international and EU evidence, cross system comparison, and methodology. The prose is Croatian (hr-HR) and must conform to STYLE.md.

## Workflow
1. Read the target chapter top to bottom.
2. Mark asymmetric points (a concept introduced but never unpacked, a result without its mechanism, theory without empirics, one side of a debate, an opaque identification claim).
3. Identify the slot for each point. Bound the candidate set to the strongest two to four per chapter.
4. Draft a one to two paragraph insertion per kept point. Anchor recent landmark literature where natural (see ENRICHMENT.md for the topic to books map). Cite with `[@key]` against `references.bib`. If a source is not in the bib, flag it, never fabricate a finding or a page number.
5. Present in chat before any edit. For each insertion show the slot, the anchor point, the draft prose, and the citation key, plus one or two rejected candidates with the reason.
6. Apply only what the user approves. Verify with `quarto preview`.

## Modes
`scan` (find and rank candidates only), `draft` (write insertions for review). Infer if unspecified.

## Quality gates / checklist
`assets/checklist.json`. Each insertion fills exactly one slot, no Croatian empirics, no fabricated finding or page, presented before editing, cited from `references.bib` or flagged, passes the substantive test (would a reader who already understood the chapter learn something new).

## Knowledge base & references
`ENRICHMENT.md` in the book repo is authoritative, including the landmark literature map. `reference/value-slots.md` is a short in plugin restatement of the slots and the asymmetry test.

## Autonomy note
Insertions are proposals shown before any file changes. You choose which to keep. The skill never edits silently and never invents the evidence it cites.
