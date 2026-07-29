# Status report

How to turn the ledger into a dashboard.

Read `${CLAUDE_PLUGIN_ROOT}/shared/chapter-ledger.json`. Print one line per chapter, in chapter order, showing the stage, the count of open self items, and the count of open co-author asks. Then a short summary grouped by stage so the finished front and the unfinished tail are both visible.

Surface separately any chapter whose `last_render` is `failed`, and any co-author ask whose status has stayed open. End with the single most useful next action, normally the earliest chapter not yet at final whose open work is all self.

Example line.
`ch 07 stranke-izbori   stage draft   self 2   coauthor 1`

Keep it terse. The point is one glance, not a report.
