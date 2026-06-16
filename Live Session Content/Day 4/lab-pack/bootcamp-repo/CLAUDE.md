# notes-api — bootcamp repo (post Day 3, Day 4 automation)

Flask service: users, notes, token auth, and a public share-a-note feature that
passed the Day 3 trust gates. Day 4 wires team infrastructure around this build:
skills, hooks, a subagent, and a cost model.

## Commands
- test: `pytest -q`   ·   lint: `ruff check .`   ·   format: `ruff format .`
- run:  `python -m notes_api.app`
- code graph: `python tools/code_graph.py whodepends <function>`

## Conventions
- Parameterised SQL only. Reuse `notes.get_note_for_owner` for note access.
- Secrets from the environment, never literals in source.
- New endpoint = a route in `app.py`'s style + a contract-asserting test in `tests/`.

## What's wired (committed, team-inherited)
- `.claude/settings.json` — permissions baseline + three hooks.
- `.claude/hooks/` — `format_on_edit.sh` (PostToolUse), `block_dangerous.sh`
  (PreToolUse), `secret_scan.sh` (commit + write).
- `.claude/skills/` — `repo-conventions` (the worked-example skill) + `owasp-review`.
- `.claude/agents/` — `researcher` (scoped delegation) + `security-reviewer`.

## Self-verifying loop
Before presenting any diff, run `pytest -q` and `ruff check .` and report both.
