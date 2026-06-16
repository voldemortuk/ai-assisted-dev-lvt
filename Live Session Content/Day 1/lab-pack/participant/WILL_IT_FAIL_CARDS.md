# "Will It Fail?" Drill (Part 1)

In pairs, predict for each task: will the agent **succeed**, **struggle**, or
**fail**? Say why, using the capability map (agents are strong on boilerplate,
test generation, migrations, and comprehension of unfamiliar code; weak on novel
architecture, ambiguous requirements, long-horizon consistency, and subtle
concurrency). A subset gets run live for the reveal.

| # | Task | Your call | Why |
|---|------|-----------|-----|
| 1 | "Add a docstring to every function in `notes_api/`" | | |
| 2 | "Design our multi-region failover strategy" | | |
| 3 | "Migrate all SQL string-formatting to parameterised queries" | | |
| 4 | "Make the app faster" | | |
| 5 | "Write tests for `get_note_for_owner`" | | |
| 6 | "Fix the intermittent race condition in the booking flow" | | |
| 7 | "Explain what `auth.py` does and how `current_user` is used" | | |
| 8 | "Decide whether we should adopt microservices" | | |
| 9 | "Rename `body` to `content` across the codebase and tests" | | |
| 10 | "Keep this 600-line refactor internally consistent across 12 files" | | |

## The point
The agent's failures are **structural**, not random. You plan around them the way
you plan around network latency. Knowing which column a task lands in is the
highest-leverage skill in the whole programme, and every later module builds on
it.
