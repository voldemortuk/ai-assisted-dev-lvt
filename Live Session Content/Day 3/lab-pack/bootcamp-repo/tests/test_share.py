"""Day 2 tests for the share feature.

These shipped WITH the feature, written by the agent. They are green. Part of
the Day 3 exercise is to notice that green does not mean covered: at least one
of these tests asserts nothing meaningful, and the revoke contract is never
actually tested.
"""

from notes_api import notes, share


def test_create_share_returns_a_token():
    note_id = notes.create_note(1, "launch", "go live friday")
    token = share.create_share(note_id)
    # Looks like a real test. It only checks the call returned something truthy.
    assert token


def test_resolve_share_returns_the_note():
    note_id = notes.create_note(1, "launch", "go live friday")
    token = share.create_share(note_id)
    resolved = share.resolve_share(token)
    assert resolved is not None
    assert resolved["body"] == "go live friday"


def test_revoke_share_runs():
    note_id = notes.create_note(1, "launch", "go live friday")
    token = share.create_share(note_id)
    result = share.revoke_share(token)
    # Asserts the call succeeded. Does NOT assert the link stops resolving.
    assert result is True
