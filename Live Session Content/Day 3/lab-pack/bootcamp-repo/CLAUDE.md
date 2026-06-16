# notes-api — bootcamp repo (LVT AI-Assisted Development Program)

A small Flask service with users, notes, and a public "share a note via link"
feature. This is the running build the programme carries from Day 2 through the
Day 3 trust gates and Day 4 automation.

## Project conventions
- Python 3.11, Flask. Data access lives in `notes_api/db.py`; routes in `notes_api/app.py`.
- Parameterised SQL only. Never build a query with string formatting or f-strings.
- Secrets come from the environment, never literals in source.
- Every endpoint that touches a note must check the caller owns it, unless the
  route is explicitly public (only `GET /s/<token>` is public).

## Self-verifying loop (Day 3 · Part 1)
Before presenting any diff to the human, you MUST:
1. Run the test suite: `pytest -q`
2. Run the linter: `ruff check .`
3. Report the results of both in your summary. If either fails, fix it or say
   why you are presenting the diff anyway. Do not present a diff as "done"
   without having run these.

Green tests are necessary, not sufficient — a passing suite can still under-assert.
Call out any test that exercises a path without asserting its contract.

## Definition of done for the share feature
- A revoked link stops resolving (returns 404).
- Share tokens are not guessable from public information.
- Only a note's owner can mint or revoke a link for it.
- At least one human-authored assertion guards the critical path.
