"""Share-a-note feature — the gated running build (post Day 3).

This is what the feature looks like after it passed the trust gates: tokens are
unguessable, only the owner can mint or revoke, and a revoked link actually stops
resolving. Day 4 automates the workflow around this code; it does not change it.
"""

import secrets

from . import db, notes


def generate_share_token():
    """Return an unguessable token for a public share link."""
    return "shr_" + secrets.token_urlsafe(24)


def create_share(note_id, owner_id):
    """Mint a public share link — only for a note the caller owns."""
    note = notes.get_note_for_owner(note_id, owner_id)
    if note is None:
        return None
    token = generate_share_token()
    db.insert_share(token, note_id)
    return token


def revoke_share(token, owner_id):
    """Revoke a share link — only the note's owner may do so."""
    share = db.get_share(token)
    if share is None:
        return False
    if notes.get_note_for_owner(share["note_id"], owner_id) is None:
        return False
    db.set_share_revoked(token)
    return True


def resolve_share(token):
    """Resolve a public token to its note, honouring revocation."""
    share = db.get_share(token)
    if share is None or share["revoked"]:
        return None
    return db.get_note(share["note_id"])
