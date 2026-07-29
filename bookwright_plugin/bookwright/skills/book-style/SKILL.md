---
name: book-style
description: Enforce this book's editorial style on a chapter. Use whenever you edit, sweep, or finish a .qmd chapter, or whenever the user mentions style, the style sweep, STYLE.md, polishing prose, or making a chapter read like a written manuscript rather than assembled notes. Runs an R linter that flags the STYLE.md hard rules, then guides a manual restructuring pass. Always apply before committing any chapter prose edit.
allowed-tools: Read, Edit, Bash
---

# Book Style

## Purpose
Make a chapter read like continuous written prose, conforming to STYLE.md. STYLE.md is the source of truth and it grows over time, so read it before a sweep. This skill adds a linter that finds the mechanical violations fast and a workflow for fixing the subtle ones by hand.

## When to use
Before committing any prose edit to a chapter, and whenever the user asks for a style sweep or a polish. The prose lives in Croatian (hr-HR). Do not rewrite it into English.

## The hard rules (from STYLE.md)
1. No colons in prose. Restructure into new sentences, relative clauses, or indirect formulations. YAML, code blocks, and URLs are exempt.
2. No mid sentence em dash used to introduce a list or appositive. Use `koji uključuje`, a relative clause, or a new sentence. An em dash as a title separator is fine.
3. No mechanical takeaway formulae (`Glavna poruka X glasi`, `U ovom poglavlju ćemo`). Every transition must be specific to the substance above it.
4. No meta structural callouts in flowing prose (decorative pullquotes, signpost subheaders, a heading whose first sentence restates it). The pedagogical callouts (`callout-vinjeta`, `callout-divljina`, `callout-model`, `callout-greska`) are kept.
5. Minimal restatement connectives (`Drugim riječima`, `Naime`, `Točnije`, `Ukratko`, `Jednostavnije rečeno`). At most once per chapter, and only when it sharpens something.
6. Chapter titles use an em dash separator, not a colon.

Soft conventions. Bold only for a first mention concept anchor, not mid sentence emphasis. Prefer indirect questions over a direct question introduced by a colon, except a deliberate rhetorical cluster.

## Workflow
1. Read `STYLE.md` in the book repo for the current rules and any new ones.
2. Run the linter. `Rscript ${CLAUDE_PLUGIN_ROOT}/skills/book-style/scripts/style_lint.R chapters/<file>.qmd`. It prints candidate violations with line numbers.
3. For each hit, restructure rather than delete meaning. Colons become new sentences or relative clauses, em dash lists become `koji uključuje` or a relative clause, mechanical openers get a specific transition or get cut.
4. Read the chapter top to bottom. Anything that still reads like a slide bullet, a summary box, or a structural announcement gets rewritten. The linter cannot catch these, so the human pass is required.
5. Verify with `quarto preview chapters/<file>.qmd` and read the rendered output.

## Modes
`lint` (run the linter only and report), `sweep` (run the linter then do the full editing pass). If unsure, infer and say which.

## Quality gates / checklist
`assets/checklist.json` holds the rules as blocking items. A style pass is a book checkpoint, so a chapter cannot be final while a hard rule is violated.

## Knowledge base & references
`STYLE.md` in the book repo is the authoritative, growing rule set. `scripts/style_lint.R` is the linter.

## Autonomy note
The linter flags candidates, it does not edit. Every restructuring is a writing choice you make. The skill speeds the search and protects the rules, it does not own the prose.
