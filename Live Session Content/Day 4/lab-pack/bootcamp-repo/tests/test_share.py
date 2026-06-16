"""Tests for the gated share feature (post Day 3).

These assert the contract, not just that calls return something. The revoke test
is the human-authored assertion from Day 3 — it now passes, because the feature
was fixed. Day 4 keeps this green as it wires automation around the build.
"""

from notes_api import notes, share


def test_owner_can_mint_and_open():
    note_id = notes.create_note(owner_id=1, title="launch", body="go live friday")
    token = share.create_share(note_id, owner_id=1)
    assert token is not None
    resolved = share.resolve_share(token)
    assert resolved is not None and resolved["body"] == "go live friday"


def test_non_owner_cannot_mint():
    note_id = notes.create_note(owner_id=1, title="private", body="alice only")
    # Mallory (id 2) must not be able to share Alice's note.
    assert share.create_share(note_id, owner_id=2) is None


def test_tokens_are_unguessable():
    note_id = notes.create_note(owner_id=1, title="a", body="b")
    tokens = {share.create_share(note_id, owner_id=1) for _ in range(50)}
    # 50 links for the SAME note must all differ — proof they're random, not
    # derived from the note id (the Day 3 defect was a deterministic token).
    assert len(tokens) == 50
    # And the random part carries real entropy, not a short predictable suffix.
    assert all(len(t) > 24 for t in tokens)


def test_revoked_link_actually_stops_resolving():
    # The human-authored assertion from Day 3 — now green.
    note_id = notes.create_note(owner_id=1, title="launch", body="go live friday")
    token = share.create_share(note_id, owner_id=1)
    assert share.resolve_share(token) is not None
    share.revoke_share(token, owner_id=1)
    assert share.resolve_share(token) is None


def test_non_owner_cannot_revoke():
    note_id = notes.create_note(owner_id=1, title="x", body="y")
    token = share.create_share(note_id, owner_id=1)
    assert share.revoke_share(token, owner_id=2) is False
    assert share.resolve_share(token) is not None
