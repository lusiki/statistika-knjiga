---
name: book-figure
description: Make sure every figure in a chapter of this book is introduced by one prose paragraph in the chapter voice. Use whenever the user mentions a figure, an infographic, a chart, a Slika, a figure caption, or asks to describe or introduce a figure, or to check that figures are explained. Runs an R detector that flags any figure lacking a paragraph before it, then drafts the missing paragraph under STYLE.md and shows it before writing. Apply before a chapter with figures reaches final.
allowed-tools: Read, Edit, Bash
---

# Book Figure

## Purpose
Hold one convention across the book. Every figure carries a single prose paragraph immediately before it that says what the figure shows and why it matters, written in the chapter voice. The caption and the rendered `Slika X.Y` prefix do not satisfy this. The paragraph does.

## When to use
On any chapter that contains figures, before it reaches final, and whenever the user asks to check or write figure introductions. The prose is Croatian (hr-HR) and conforms to STYLE.md.

## The rule
A figure is a markdown image on its own line, a `::: {#fig-...}` div, or a code chunk carrying a `#| label: fig-...` option. The block immediately above a figure must be a prose paragraph, not a heading, a list, a callout fence, a code fence, or another figure.

## Workflow, check mode
1. Run the detector. `Rscript ${CLAUDE_PLUGIN_ROOT}/skills/book-figure/scripts/figure_intro_check.R chapters/<file>.qmd`. It lists each figure and, for any that fail, the line and the reason.
2. Report the failing figures. Do not edit in check mode.

## Workflow, fix mode
1. Run the detector to find figures that lack an intro.
2. For each, read the figure (its caption, its data or content) and the surrounding text so the paragraph fits the argument at that point.
3. Draft one paragraph in Croatian that states what the figure shows and why it matters here. Keep it to a single paragraph.
4. Run the style linter on the draft. `Rscript ${CLAUDE_PLUGIN_ROOT}/skills/book-style/scripts/style_lint.R` on the chapter after insertion, or check the draft against the STYLE.md hard rules first.
5. Present each draft in chat with the figure it belongs to. Apply only what the user approves. Verify with `quarto preview`.

## Modes
`check` (detector only, list failures), `fix` (detector then draft intros for approval). Infer if unspecified.

## Quality gates / checklist
`assets/checklist.json`. A figure has a paragraph before it, the intro is a single paragraph, the intro passes the style linter. Whether the intro truly describes the figure is a judgment left to the review panel.

## Knowledge base & references
`scripts/figure_intro_check.R` is the detector. `STYLE.md` in the book repo is the voice. `book-continuity` reuses this detector when it sweeps figure coverage across the whole book.

## Autonomy note
The detector finds gaps, it never writes. Every intro paragraph is shown before it touches the file. You decide what the figure means and approve the words.
