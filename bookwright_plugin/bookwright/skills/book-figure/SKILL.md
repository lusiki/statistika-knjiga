---
name: book-figure
description: Check or repair figure introductions in the Osnove statistike za društvene znanosti book. Use when a user mentions a figure, chart, infographic, Slika, caption, or asks whether figures are explained. Run the deterministic detector, report figures without a prose paragraph immediately before them, and in fix mode draft one Croatian introduction per figure for approval before editing.
allowed-tools: Read, Edit, Bash
---

# Book Figure

Enforce one convention: every figure has one prose paragraph immediately before
it explaining what it shows and why it matters at that point. A caption,
rendered `Slika X.Y` prefix, heading, list, comment, callout fence, code fence,
or another figure does not satisfy the rule.

Resolve `<plugin-root>` from the installed environment or this `SKILL.md` path.
Run R scripts through `<plugin-root>/scripts/run_rscript.py` with concrete paths.

## Modes

- `check` — Run the detector and report failures without editing.
- `fix` — Run the detector, inspect each figure and its surrounding argument,
  draft one Croatian paragraph per failure, and show every draft before writing.

Infer the mode when omitted.

## Workflow

1. Run:

   ```text
   python <plugin-root>/scripts/run_rscript.py <plugin-root>/skills/book-figure/scripts/figure_intro_check.R chapters/<file>.qmd
   ```

2. In `fix`, read the caption, data or graphic, and surrounding prose. Draft one
   paragraph in the chapter voice that says both what the figure shows and why
   it matters.
3. Apply only approved paragraphs.
4. Run the style linter on the changed chapter:

   ```text
   python <plugin-root>/scripts/run_rscript.py <plugin-root>/skills/book-style/scripts/style_lint.R chapters/<file>.qmd
   ```

5. Perform a targeted Quarto verification appropriate to the edit.

Use `STYLE.md` as the voice source and `assets/checklist.json` as the gate. The
detector finds placement gaps; the review panel judges whether the paragraph
actually explains the figure.
