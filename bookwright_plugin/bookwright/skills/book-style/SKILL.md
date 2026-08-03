---
name: book-style
description: Enforce the editorial style of the Osnove statistike za društvene znanosti book. Use whenever chapter prose is edited, swept, polished, or prepared for commit, or when the user mentions STYLE.md or manuscript style. Run the deterministic R linter, interpret only genuine prose hits, then perform the manual Croatian-language pass that a linter cannot do.
allowed-tools: Read, Edit, Bash
---

# Book Style

Make a chapter read like a continuous Croatian manuscript rather than assembled
notes. Read the current `STYLE.md` before every sweep; it is authoritative and
may grow.

Resolve `<plugin-root>` from the installed environment or this `SKILL.md` path.
Run R checks through `<plugin-root>/scripts/run_rscript.py` with concrete paths.

## Modes

- `lint` — Run the linter and report candidates without editing.
- `sweep` — Run the linter, repair genuine hits, then read the whole chapter for
  problems no regex can judge.

Infer the mode when omitted and state it.

## Workflow

1. Read `STYLE.md` and the target chapter.
2. Run:

   ```text
   python <plugin-root>/scripts/run_rscript.py <plugin-root>/skills/book-style/scripts/style_lint.R chapters/<file>.qmd
   ```

3. Treat output as candidates, not instructions. The linter excludes YAML,
   code, headings, div fences, and HTML comments, but context still decides.
4. Enforce all hard rules H1–H10. Restructure colons and mid-sentence em-dash
   appositions without deleting meaning; avoid list scaffolding in running
   prose; remove mechanical openers and restatement padding including
   `Štoviše`; keep bold for first concept anchors rather than emphasis; anchor
   citations to the claims they support; and put intuition before notation.
   H6 requires a nominal, unnumbered heading without a colon. Use an em dash only
   when a separator is actually needed. Under H10 and D05, the preface and Part
   I contain no visible code in the book edition, hidden plumbing is exempt from
   the twelve-line visible-block ceiling, later receipts contain only the
   inspectable idea, and no assessed task requires code production.
5. Read top to bottom for slide-like fragments, decorative callouts, headings
   restated by their first sentence, unexplained jargon, and abrupt transitions.
6. Preserve Croatian (`hr-HR`), pedagogical callouts, Quarto syntax, citations,
   and the chapter's statistical meaning.
7. Perform a targeted Quarto verification appropriate to the edit.

Use `assets/checklist.json` as the blocking mechanical gate. The linter never
edits; judgment owns the prose.
