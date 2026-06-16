"""Note CRUD — Day 1 baseline."""

from . import db


def create_note(owner_id, title, body):
    conn = db._connect()
    cur = conn.execute(
        "INSERT INTO notes (owner_id, title, body) VALUES (?, ?, ?)",
        (owner_id, title, body),
    )
    conn.commit()
    note_id = cur.lastrowid
    conn.close()
    return note_id


def get_note_for_owner(note_id, owner_id):
    """Fetch a note only if it belongs to owner_id, else None.

    This is the ownership-checked accessor. The Day 2 share lab should reuse it
    so the share feature inherits the access check for free.
    """
    note = db.get_note(note_id)
    if note is None:
        return None
    if note["owner_id"] != owner_id:
        return None
    return note
