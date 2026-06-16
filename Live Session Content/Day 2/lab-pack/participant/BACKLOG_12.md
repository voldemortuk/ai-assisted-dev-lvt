# Sizing Lab — classify the backlog (Part 1)

For each item, pick the right approach and defend it in your pair. The four
approaches:

- **Quick** — interactive change, no plan. Small, reversible, obvious.
- **Plan** — drive through plan mode, approve the plan before code. Real blast radius or ambiguity.
- **Spec** — write an executable spec first. Multi-step, contract matters, becomes a running artifact.
- **No agent** — do it yourself. Novel design, one-character call, or judgment the agent can't hold.

Signals to weigh: **blast radius** (how much breaks if it's wrong), **ambiguity**
(how clear is "done"), **reviewability** (can you check the result quickly).

| # | Backlog item |
|---|--------------|
| 1 | Fix a typo in an error message string |
| 2 | Add the share-a-note feature (public link + revoke) |
| 3 | Rename `body` to `content` across the notes table, models, API, and tests |
| 4 | Bump the Flask version one minor and confirm tests pass |
| 5 | Decide whether notes should move to Postgres before the next quarter |
| 6 | Add a `GET /notes` endpoint that lists the caller's notes |
| 7 | Add pagination to `GET /notes` (limit/offset, default 20, max 100) |
| 8 | Investigate an intermittent 500 on `POST /notes` under load |
| 9 | Add a `created_at` timestamp to notes and backfill existing rows |
| 10 | Write a one-line README badge for the test status |
| 11 | Re-architect auth from bearer tokens to OAuth2 with refresh tokens |
| 12 | Add input validation: reject empty title or body with a 400 |

## Your call
Write your approach + one-line reason per item. Then the oversized one:

**Chunking exercise:** take **item 11** (OAuth2 re-architecture) and break it into
agent-sized pieces with an explicit interface between each. Aim for 4–6 chunks
where each is independently reviewable and the seams are clean.
