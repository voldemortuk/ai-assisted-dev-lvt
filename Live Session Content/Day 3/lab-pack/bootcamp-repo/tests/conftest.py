"""Test fixtures — point the data layer at a throwaway SQLite file per test."""

import pytest

from notes_api import db


@pytest.fixture(autouse=True)
def fresh_db(tmp_path, monkeypatch):
    monkeypatch.setattr(db, "DB_PATH", tmp_path / "test_notes.db")
    db.init_db()
    # Seed two users so ownership tests have someone to be.
    conn = db._connect()
    conn.execute("INSERT INTO users (email, token) VALUES (?, ?)",
                 ("alice@lvt.test", "tok_alice"))
    conn.execute("INSERT INTO users (email, token) VALUES (?, ?)",
                 ("mallory@lvt.test", "tok_mallory"))
    conn.commit()
    conn.close()
    yield
