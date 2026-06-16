"""Note CRUD — pre-existing bootcamp-repo code from Day 1.

Kept intentionally small. The Day 3 review focuses on the Day 2 share feature
(`share.py`) and the data layer it leans on (`db.py`).
"""

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

    This is the ownership-checked accessor. Note that `share.create_share`
    does NOT use it — that gap is in scope for review.
    """
    note = db.get_note(note_id)
    if note is None:
        return None
    if note["owner_id"] != owner_id:
        return None
    return note
