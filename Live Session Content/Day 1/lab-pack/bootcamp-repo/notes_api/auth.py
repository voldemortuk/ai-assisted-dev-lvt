"""Minimal token auth for the Notes API.

A request carries an Authorization header: `Authorization: Bearer <token>`.
We resolve the token to a user row, or return None.
"""

from . import db


def current_user(headers):
    """Resolve the caller from the Authorization header, or None."""
    auth = headers.get("Authorization", "")
    if not auth.startswith("Bearer "):
        return None
    token = auth[len("Bearer "):].strip()
    if not token:
        return None
    return db.get_user_by_token(token)
