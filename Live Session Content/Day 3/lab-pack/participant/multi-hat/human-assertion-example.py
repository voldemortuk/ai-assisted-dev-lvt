"""The one human-authored assertion (Part 2 · the hard line).

Rule, non-negotiable: never ship AI code with only AI-written tests. Keep at least
one assertion a human wrote, on the critical path, on anything that matters.

This is the assertion the black-box hat told you it would refuse to author alone:
the revoke contract. Drop a version of this into the bootcamp repo's tests, written
in YOUR words, and watch it FAIL against the current planted code — that failure is
the proof the AI's green suite was covering air.

Copy into tests/, run `pytest -q`, and expect it to fail until revoke is fixed.
"""

from notes_api import notes, share


def test_revoked_link_actually_stops_resolving():
    # I am asserting the contract I care about, not the call's return value.
    note_id = notes.create_note(owner_id=1, title="launch", body="go live friday")
    token = share.create_share(note_id)

    assert share.resolve_share(token) is not None, "link should work before revoke"

    share.revoke_share(token)

    # THE assertion the feature exists to satisfy. With the planted copy-paste
    # drift in revoke_share, this fails — exactly as it should.
    assert share.resolve_share(token) is None, "a revoked link must stop resolving"
