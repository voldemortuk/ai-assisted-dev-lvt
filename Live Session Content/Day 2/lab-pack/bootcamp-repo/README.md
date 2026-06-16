# notes-api (bootcamp repo) — Day 2 starting state

The running build for the LVT AI-Assisted Development Program. On Day 2 this repo
is at its **Day 1 baseline**: users, notes CRUD, and token auth. No share feature
yet.

In the Day 2 spec-driven lab (Part 3) you turn `specs/SHARE_NOTE_PRD.md` into an
executable spec and build the **share-a-note feature** from it. That feature
becomes the running build Day 3 reviews and Day 4 automates.

## Run it
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest -q          # 2 passed (baseline)
ruff check .
python -m notes_api.app   # serves on :5000
```

## Endpoints (baseline)
| Method | Path | Auth | Notes |
|--------|------|------|-------|
| POST | `/notes` | yes | create a note |
| GET  | `/notes/<id>` | yes | read your own note |

The share endpoints (`POST /notes/<id>/share`, `POST /shares/<token>/revoke`,
`GET /s/<token>`) are what you build from the spec in Part 3.
