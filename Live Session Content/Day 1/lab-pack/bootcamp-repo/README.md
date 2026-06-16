# notes-api (bootcamp repo) — Day 1 starting state

The shared bootcamp repo for the LVT AI-Assisted Development Program. On Day 1 it
is small on purpose: users, notes CRUD, and token auth. You'll make your **first
committed change** here through Claude Code, then carry this repo through the rest
of the week.

## Run it
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest -q          # 2 passed
ruff check .
python -m notes_api.app   # serves on :5000
```

## Endpoints
| Method | Path | Auth | Notes |
|--------|------|------|-------|
| POST | `/notes` | yes | create a note |
| GET  | `/notes/<id>` | yes | read your own note |

## Where to start
Open `BACKLOG.md`. Pick one small, well-defined change and drive it end to end:
prompt, review the diff, run the tests, commit.
