# FACILITATOR — Part 2 Diff-Review Key

The three diffs escalate in subtlety on purpose. They're the seed of Day 3's slop
work, so name the failure mode each time.

### Diff 1 — **REJECT** (obvious)
The "fix" wraps everything in `try/except Exception` and returns `200 {id: null}`
on **any** failure. It doesn't fix the bug, it hides it: a missing field now
returns a fake success, and so does a real database error. The client is lied to.
- Failure mode: **swallowing errors / dishonest status code.**
- Right fix: validate the fields explicitly and return `400` for missing input,
  while letting genuine errors surface.

### Diff 2 — **AMEND** (subtle)
`list_notes()` runs `SELECT id, title FROM notes` with **no owner filter**. It
returns *everyone's* notes to any authenticated caller. It runs, returns 200, and
the shape is right, which is exactly why it slips through.
- Failure mode: **missing access control** (the Day 3 A01 preview).
- Amend: `WHERE owner_id = ?` with `user["id"]`, and a test that creates notes for
  two users and asserts the caller sees only their own.

### Diff 3 — **AMEND / REJECT** (looks great)
Two problems under tidy, idiomatic code with a test:
1. **Order bug:** the length check runs *after* `create_note`, so an over-long
   title is **written to the database**, then the 400 is returned. The validation
   doesn't prevent the bad write.
2. **The test asserts nothing relevant:** `test_long_title_is_rejected` calls
   `notes.create_note(...)` directly (bypassing the endpoint) and asserts the row
   id is truthy. It never exercises the 400 and never checks the title was
   rejected. Green, covering air.
- Failure mode: **plausible-but-wrong + a test that asserts nothing** (the core of
  Day 3).
- Fix: validate **before** the write; test through the endpoint and assert the
  `400` plus that no note was created.

## The teaching arc
Diff 1 your eye catches. Diff 2 needs you to read the SQL. Diff 3 needs you to read
what *runs* and what the test *asserts*, past how tidy it looks. That progression is
the whole reason Day 3 exists. Bank it.
