# The chapter panel

Five critics, a synthesizer, a reviser.

Critics. Dispatch each at `${CLAUDE_PLUGIN_ROOT}/agents/`. They read the chapter and return a structured critique (scores, strengths, concerns with severity and location and fix, a one line verdict). They write nothing.
`critic-economist`, `critic-skeptic`, `critic-pedagogy`, `critic-evidence`, `critic-style`.

Synthesizer. Collect the five critiques. For each concern, count how many critics raised the same point and rank high agreement first. Where two critics disagree, present it as an explicit trade off rather than averaging. Produce one ranked panel report.

Reviser. Implement only the changes the user approves. Hold the rails, no citation absent from `references.bib`, no Croatian empiric. Show a before and after for each edit and wait for confirmation before writing.

Calibration. The book is a second year undergraduate textbook in public economics with a public choice spine. Critics flag errors, overclaims, and gaps, not the absence of graduate depth.
