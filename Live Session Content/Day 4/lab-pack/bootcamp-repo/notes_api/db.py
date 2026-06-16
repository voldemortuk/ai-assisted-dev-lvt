"""SQLite data layer for the Notes API.

This is the post-Day-3 state: the share feature shipped through the trust gates,
so SQL is parameterised, there are no hardcoded secrets, and the shares table is
in place. Day 4 wires automation (skills, hooks, a subagent) around this build.
"""

import os
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "notes.db"

# Config from the environment — never hardcode credentials in source.
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
    conn = _connect()
    row = conn.execute(
        "SELECT * FROM notes WHERE id = ?", (note_id,)
    ).fetchone()
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
