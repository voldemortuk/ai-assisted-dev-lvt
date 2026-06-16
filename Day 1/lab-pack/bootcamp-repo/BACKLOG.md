# Day 1 Backlog — pick one small change and drive it end to end

Each item is small, well-defined, and reviewable. Pick **one**, drive it through
Claude Code (prompt, review the diff, run tests, commit), and defend your review
calls to your pair.

## Bug fixes
1. **`POST /notes` returns a 500 on missing fields.** If the JSON body is missing
   `title` or `body`, the handler raises `KeyError` and the client gets an opaque
   500. Fix it to return a clean `400` with a helpful message. Add a test.
   *(Reproduce: `POST /notes` with `{"title": "hi"}` and no body.)*

## Small features
2. **Add `GET /notes`** that lists the caller's own notes (id + title only).
   Reuse the auth and ownership patterns already in the repo. Add a test.
3. **Add input length limits:** reject a title longer than 200 chars with a `400`.
   Add a test for the boundary.

## Tidy-ups
4. Add a module docstring to any file missing one, matching the house style.

---

## Conventions to match (read before you prompt)
- Parameterised SQL only (see `db.py`).
- Reuse `notes.get_note_for_owner(note_id, owner_id)` for any note access.
- Routes live in `app.py` in the existing style; tests mirror the module.
- Run `pytest -q` and `ruff check .` before you commit.
