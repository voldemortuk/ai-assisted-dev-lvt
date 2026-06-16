# CLAUDE.md Lab — before / after / trim (Part 4)

Project memory that earns its keep changes agent behaviour you can measure. This
lab makes the change visible, then trims the fat.

## Step 1 — measure "before"
Run this task on the repo with **no CLAUDE.md** present:

> "Add a `GET /notes` endpoint that lists the caller's notes."

Note what the agent gets wrong or has to ask: Does it parameterise the SQL? Does
it reuse the ownership-checked accessor? Does it match the existing route style?
Does it add a test in the house pattern? Save the diff as `before.diff`.

## Step 2 — write a CLAUDE.md that belongs
Write one for this repo. **What belongs:**
- Build/test/run commands (`pytest -q`, `ruff check .`, `python -m notes_api.app`)
- Conventions the agent keeps missing: parameterised SQL, reuse
  `get_note_for_owner`, secrets from env, route + test style
- An architecture pointer: data access in `db.py`, routes in `app.py`

**What does NOT belong:** prose essays, restating what the code already says,
stale rules, anything you'd be embarrassed to pay context cost for every turn.

## Step 3 — measure "after"
Re-run the **same task** with the CLAUDE.md in place. Save `after.diff`. Diff the
two. The behaviour change is your evidence.

## Step 4 — trim a third
Team review: which lines actually earned their context cost? Cut **at least a
third**. Every line you keep is paid for on every single turn (Day 1's lesson,
now in practice). A shorter CLAUDE.md that changes behaviour beats a long one that
mostly decorates.

**Deliverable:** a CLAUDE.md committed to the repo, with `before.diff` /
`after.diff` showing the behaviour change, trimmed by ≥33%.
