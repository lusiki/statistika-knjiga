# Status report

Read the live `shared/chapter-ledger.json`. Print one line per chapter in ledger
order with its stage, count of open self items, and count of open outside asks
stored in the legacy `coauthor_asks` field.

Then:

- group the summary by stage;
- surface every failed render;
- list outside asks whose status remains `open`;
- end with the single most useful next action, normally the earliest non-final
  chapter whose open work is all self-service.

Example:

`ch 08 uzorkovanje   stage draft   self 2   outside 1`

Keep the dashboard terse enough to scan at a glance.
