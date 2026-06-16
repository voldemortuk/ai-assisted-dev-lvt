# Anatomy of a Strong Developer Prompt (reference)

A strong prompt reads like a good ticket. Five parts:

1. **Specificity** — the exact file, endpoint, function, and behaviour. Not "the
   notes endpoint" but "`POST /notes` in `app.py`".
2. **Constraints** — what to reuse, what not to change, the rules to follow.
   "Reuse `get_note_for_owner`. Parameterised SQL only. Don't touch the auth flow."
3. **Success criteria** — the behaviour stated as something checkable. "A missing
   `body` returns `400`, not `500`."
4. **Definition of done** — the gate. "Tests pass, ruff clean, a test covers the
   missing-field case."
5. **A worked example (when it matters)** — one canonical snippet from the repo so
   output lands in house style on the first pass.

## Anti-patterns to avoid
- **Vague asks** ("make it better") — the agent guesses, and guesses wrong.
- **Over-asking in one prompt** — five changes at once means five things to review
  and a tangled diff. One task per prompt.
- **Missing acceptance criteria** — if you can't say how you'll check it, the agent
  can't either.
- **Prompting for code when the real question is design** — if you're unsure of the
  approach, ask for a plan or a recommendation first, not an implementation.

## The test
Before you send it, ask: *could a competent engineer who's never seen this repo
produce the right change from this prompt alone?* If not, it's underspecified.
