"""SQLite data layer for the Notes API.

Day 1 baseline: users + notes, token auth. The Day 2 spec-driven lab adds the
`shares` table and the share feature on top of this. Keep SQL parameterised and
keep secrets in the environment.
"""

import os
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "notes.db"

# Read config from the environment — never hardcode credentials in source.
DB_PASSWORD = os.environ.get("NOTES_DB_PASSWORD", "")


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
    """Fetch a single note by id. Parameterised."""
    conn = _connect()
    row = conn.execute(
        "SELECT * FROM notes WHERE id = ?", (note_id,)
    ).fetchone()
    conn.close()
    return row
