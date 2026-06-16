# FACILITATOR — Part 1 Mental Models Key

## Same-prompt-twice demo (make non-determinism concrete)
Run the identical prompt against the repo twice in two fresh sessions, for example:
> "Add a `GET /notes` endpoint that lists the caller's notes. Add a test."

Show the two diffs side by side. They'll differ: variable names, whether a helper
is added, test phrasing, sometimes the SQL approach. Land it: same prompt, two
diffs, because generation samples over a distribution. This is why you review every
diff and why reproducibility comes from specs and tests, not from hoping.

## "Will it fail?" drill — expected calls
| # | Task | Expected | Why |
|---|------|----------|-----|
| 1 | Docstrings everywhere | **Succeed** | Boilerplate, mechanical |
| 2 | Multi-region failover strategy | **Fail** | Novel architecture, judgment |
| 3 | Migrate to parameterised SQL | **Succeed** | Mechanical migration, clear pattern |
| 4 | "Make the app faster" | **Struggle** | Ambiguous; no definition of done |
| 5 | Tests for `get_note_for_owner` | **Succeed** | Test generation on a clear contract |
| 6 | Fix intermittent race condition | **Fail/Struggle** | Subtle concurrency, hard to reproduce |
| 7 | Explain `auth.py` | **Succeed** | Comprehension of unfamiliar code |
| 8 | Decide on microservices | **Fail** | A decision, not a change |
| 9 | Rename `body`→`content` everywhere | **Succeed** (with review) | Mechanical, wide but clear |
| 10 | Keep a 600-line refactor consistent | **Struggle** | Long-horizon consistency |

The pattern: strong on boilerplate, migrations, test-gen, comprehension; weak on
novel design, ambiguity, concurrency, long-horizon consistency. Failures are
structural, so they're predictable.

## Token-budget exercise
Have engineers itemise what's in context mid-session: system prompt, project memory
(CLAUDE.md), file reads, tool output, conversation history. Then rank what they'd
evict first. There's no single right answer; the point is that context is finite
and crowding it degrades output. This seeds Part 3 and gets priced in dollars on
Day 4.
