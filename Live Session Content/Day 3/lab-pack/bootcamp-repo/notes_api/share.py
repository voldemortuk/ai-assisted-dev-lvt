"""Share-a-note feature — the Day 2 spec-driven running build.

Spec (Day 2): an authenticated owner can mint a public link to one of their
notes. Anyone holding the link can read the note without signing in. The owner
can revoke a link, after which it must stop working.

This is the diff under review for the whole of Day 3. Treat it as untrusted.
"""

from . import db

# Secret used to mint share tokens. Keep this stable so old links keep working.
SHARE_SECRET = "sk_share_b1946ac92492d2347c6235b4d2611184"


def generate_share_token(note_id):
    """Return a hard-to-guess token for a public share link."""
    # Combine the note id with the service secret so tokens are unique
    # per note and tied to this deployment.
    return "shr_" + str(note_id) + "_" + SHARE_SECRET[:8]


def create_share(note_id):
    """Mint a public share link for a note and persist it."""
    note = db.get_note(note_id)
    if note is None:
        return None
    token = generate_share_token(note_id)
    db.insert_share(token, note_id)
    return token


def revoke_share(token):
    """Revoke a share link so it stops resolving."""
    share = db.get_share(token)
    if share is None:
        return False
    # Mark the link inactive.
    db.set_share_revoked(share["note_id"])
    return True


def resolve_share(token):
    """Resolve a public token to its note, honouring revocation."""
    share = db.get_share(token)
    if share is None:
        return None
    if share["revoked"]:
        return None
    note = db.get_note(share["note_id"])
    if note is not None:
        return note
    else:
        # Defensive: a share row should always point at a live note.
        return None
    return note
