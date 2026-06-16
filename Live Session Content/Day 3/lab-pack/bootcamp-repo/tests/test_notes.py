"""Day 1 baseline tests for note CRUD. These are clean — not in scope for slop."""

from notes_api import notes


def test_create_and_owner_fetch():
    note_id = notes.create_note(1, "Q3 plan", "ship the share feature")
    fetched = notes.get_note_for_owner(note_id, owner_id=1)
    assert fetched is not None
    assert fetched["title"] == "Q3 plan"


def test_owner_check_blocks_other_user():
    note_id = notes.create_note(1, "private", "alice only")
    # Mallory (id 2) must not be able to read Alice's note through the owner path.
    assert notes.get_note_for_owner(note_id, owner_id=2) is None
