# FACILITATOR — Part 2 Flawed-Plan Key

The plan for "add `created_at` + backfill" (backlog item 9) has four planted
defects. Participants should catch at least three.

### Defect 1 — Step 4 edits the wrong file
"Update `tests/test_share.py`" — there is **no share feature on Day 2's repo**, and
the change is to notes, so the test belongs in `tests/test_notes.py`. Classic
wrong-file defect, easy to miss because the step *reads* fine.

### Defect 2 — the backfill is missing entirely (the actual task)
The ticket says "**and backfill existing rows**." The plan adds the column with a
default for *new* rows and never backfills the existing ones. The headline
requirement is silently dropped. A `DEFAULT CURRENT_TIMESTAMP` does nothing for
rows already in the table.

### Defect 3 — unstated assumption about existing data
Adding a `NOT NULL` timestamp column to a table with existing rows fails or leaves
NULLs, depending on how it's written. The plan assumes an empty table. On real
data it breaks. The plan should state the migration strategy for existing rows.

### Defect 4 — verification doesn't verify
Step 5 "run the app to confirm it starts" proves nothing about `created_at`. The
app starting says the syntax is fine, not that the column exists, is populated, or
shows up in the response. Verification should be a test asserting the field on
both a new row and a backfilled old row.

## Re-plan (model answer)
1. Add `created_at TEXT` to `notes`; **backfill** existing rows in the same
   migration (set to a sentinel or `CURRENT_TIMESTAMP`), then enforce the default
   for new rows.
2. Set `created_at` in `create_note()`; include it in the `GET /notes/<id>` response.
3. Add a test in **`tests/test_notes.py`** asserting the field on a freshly
   created note *and* on a pre-existing (backfilled) row.

## Teaching beat
Plan mode is the cheapest place to catch all four. Each defect, caught here, costs
one line of correction. Caught after the code is written, it costs a re-run; caught
in review, it costs a round trip; caught in prod, it costs an incident.
