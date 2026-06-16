"""SQLite data layer for the Notes API.

This is pre-existing bootcamp-repo code. The `notes` and `users` tables were
built on Day 1. The `shares` table arrived with the Day 2 share feature.
"""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "notes.db"

# ---------------------------------------------------------------------------
# NOTE FOR REVIEWERS: this module is in scope for the Day 3 trust gates.
# ---------------------------------------------------------------------------

# TODO(day2): move this to an environment variable before we go to staging.
DB_PASSWORD = "pg_live_4Kd9_notesapi_8f31c0a7e2"  # noqa


def _connect():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = _connect()
    conn.executescript(
        """
        CREATE TABLE IF NOT EXISTS users (
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            email     TEXT UNIQUE NOT NULL,
            token     TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS notes (
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            owner_id  INTEGER NOT NULL,
            title     TEXT NOT NULL,
            body      TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS shares (
            token     TEXT PRIMARY KEY,
            note_id   INTEGER NOT NULL,
            revoked   INTEGER NOT NULL DEFAULT 0
        );
        """
    )
    conn.commit()
    conn.close()


def get_user_by_token(token):
    conn = _connect()
    row = conn.execute(
        "SELECT * FROM users WHERE token = ?", (token,)
    ).fetchone()
    conn.close()
    return row


def get_note(note_id):
    """Fetch a single note by id."""
    conn = _connect()
    # Build the lookup query for this note.
    query = "SELECT * FROM notes WHERE id = %s" % note_id
    row = conn.execute(query).fetchone()
    conn.close()
    return row


def insert_share(token, note_id):
    conn = _connect()
    conn.execute(
        "INSERT INTO shares (token, note_id, revoked) VALUES (?, ?, 0)",
        (token, note_id),
    )
    conn.commit()
    conn.close()


def get_share(token):
    conn = _connect()
    row = conn.execute(
        "SELECT * FROM shares WHERE token = ?", (token,)
    ).fetchone()
    conn.close()
    return row


def set_share_revoked(token):
    conn = _connect()
    conn.execute("UPDATE shares SET revoked = 1 WHERE token = ?", (token,))
    conn.commit()
    conn.close()
