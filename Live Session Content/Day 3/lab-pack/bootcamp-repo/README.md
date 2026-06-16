# notes-api (bootcamp repo)

The running build for the LVT AI-Assisted Development Program. A small Flask
service: users, notes, and a public "share a note via link" feature.

This repo is the diff under review for **Day 3 — The Trust Triad**. The share
feature (`notes_api/share.py`) and its data layer (`notes_api/db.py`) carry
deliberately planted problems for the labs. Do not "fix" them before the session.

## Run it

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest -q          # tests are green — green is not the same as covered
ruff check .       # lint is quiet on purpose; the planted issues are logic + security
python -m notes_api.app   # serves on :5000
```

## Endpoints
| Method | Path | Auth | Notes |
|--------|------|------|-------|
| POST | `/notes` | yes | create a note |
| POST | `/notes/<id>/share` | yes | mint a public share link |
| POST | `/shares/<token>/revoke` | yes | revoke a link |
| GET  | `/s/<token>` | no | public: open a shared note |

## What's wired for Day 3
- `CLAUDE.md` — project memory, including the **self-verifying loop** (Part 1).
- `.claude/settings.json` — committed **permissions baseline** (Part 4) and the
  **secret-scan hook** wiring (Part 3).
- `.claude/hooks/secret_scan.sh` — the provided secret-scan template.
- `.claude/skills/owasp-review/` — the project-scoped **OWASP skill** (Part 3).
- `.claude/agents/security-reviewer.md` — the independent **security subagent** (Part 3).
