---
name: book-enrich
description: Strengthen an under-developed chapter of the Osnove statistike za društvene znanosti book with focused one- or two-paragraph additions that follow ENRICHMENT.md. Use when a chapter feels thin or the user asks to enrich, deepen, or strengthen it. Diagnose asymmetries, assign each proposal to one of the five value slots, verify every empirical claim against references.bib, and present drafts for approval before editing.
allowed-tools: Read, Edit
---

# Book Enrich

Add substance without uniform expansion or restatement. Read the target chapter,
`ENRICHMENT.md`, `STYLE.md`, `references.bib`, and the relevant chapter plan
before drafting.

## Five value slots

Each insertion must fill exactly one slot:

1. `mechanism` — unpack what a procedure does to the data and why it works.
2. `empirical evidence` — add a verifiable published social-science finding,
   including magnitude and uncertainty when reported.
3. `comparative / methodological context` — compare the procedure with its
   neighbours, assumptions, or historical alternatives.
4. `failure mode / counterview` — show where the procedure breaks, which
   assumption carries it, or the principled objection.
5. `interpretation` — state what the result licenses the reader to conclude and
   what it does not.

## Workflow

1. Read the chapter top to bottom and mark asymmetries defined in
   `ENRICHMENT.md`.
2. Rank the strongest two to four candidates. Reject generic padding.
3. For each kept candidate, identify one slot and one exact insertion point.
4. Verify every cited key in `references.bib`. Never rely on remembered study
   details, numbers, effect sizes, sample sizes, pages, or findings. If the
   necessary source is absent, describe the evidence needed and stop that
   proposal before drafting empirical prose.
5. Draft one or two Croatian paragraphs. Put intuition or simulation before
   formalism and follow `STYLE.md`.
6. Present each proposal with its slot, anchor point, draft, and citation key,
   plus one or two rejected candidates and why they were rejected.
7. Apply only proposals the user approves. Run `book-style` on changed prose and
   perform a targeted Quarto verification appropriate to the edit.

Croatian empirical examples are welcome when they name a verifiable source such
as a survey wave, DZS/Eurostat table, dataset, or published paper. Apply the same
evidence standard to domestic and international examples.

## Modes and boundary

Use `scan` for ranked candidates without prose and `draft` for proposals shown
in chat. Infer the mode when omitted. Never edit silently and never fabricate
evidence. Follow `assets/checklist.json`; load `reference/value-slots.md` only
for the compact slot checklist.
