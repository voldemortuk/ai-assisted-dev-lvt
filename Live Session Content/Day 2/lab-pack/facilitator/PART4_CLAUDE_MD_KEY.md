# FACILITATOR — Part 4 CLAUDE.md Key

## What a good CLAUDE.md for this repo looks like (model answer, ~15 lines)
```markdown
# notes-api

Flask service: users, notes, token auth. Data access in `notes_api/db.py`,
routes in `notes_api/app.py`, tests mirror the module under test.

## Commands
- test: `pytest -q`
- lint: `ruff check .`
- run:  `python -m notes_api.app`

## Conventions
- Parameterised SQL only — never f-string or `%` a query.
- Reuse `notes.get_note_for_owner(note_id, owner_id)` for any note access.
- Secrets come from the environment, never literals in source.
- New endpoint = a route in the existing style + a test in `tests/`.
```
Every line changes behaviour. Nothing restates the code or editorialises.

## Expected before/after behaviour change (the `GET /notes` task)
- **Before (no CLAUDE.md):** the agent often writes a working endpoint but may
  build the query with string formatting, skip the ownership filter, or invent a
  test style that doesn't match `test_notes.py`. It may ask clarifying questions.
- **After:** parameterised query, reuses the ownership accessor, route + test land
  in house style on the first pass, fewer questions. That delta is the evidence.

## Trim pass — what to cut
Drive the room to cut ≥33%. Cut candidates: any sentence that could appear in any
repo's README, restating the stack, philosophy lines, and **stale rules** (the
worst offenders — they spend context to mislead). Keep: commands, the four
conventions, the one architecture pointer.

## The lesson to bank
Every line is paid for on every turn (Day 1's context cost, now in dollars on Day
4). A 15-line CLAUDE.md that changes behaviour beats a 60-line one that decorates.
Conventions stop being re-typed into every prompt — that's the value.
