"""Flask routes for the Notes API — post-Day-3 gated build.

The share endpoints thread the caller's id through so ownership is enforced.
Day 4 wires hooks, skills, and a subagent around this; the routes are stable.
"""

from flask import Flask, request, jsonify

from . import db, notes, share
from .auth import current_user

app = Flask(__name__)


@app.post("/notes")
def create_note():
    user = current_user(request.headers)
    if user is None:
        return jsonify(error="unauthorized"), 401
    data = request.get_json(force=True)
    note_id = notes.create_note(user["id"], data["title"], data["body"])
    return jsonify(id=note_id), 201


@app.get("/notes/<int:note_id>")
def read_note(note_id):
    user = current_user(request.headers)
    if user is None:
        return jsonify(error="unauthorized"), 401
    note = notes.get_note_for_owner(note_id, user["id"])
    if note is None:
        return jsonify(error="not found"), 404
    return jsonify(title=note["title"], body=note["body"]), 200


@app.post("/notes/<int:note_id>/share")
def share_note(note_id):
    user = current_user(request.headers)
    if user is None:
        return jsonify(error="unauthorized"), 401
    token = share.create_share(note_id, user["id"])
    if token is None:
        return jsonify(error="note not found"), 404
    return jsonify(share_url="/s/" + token), 201


@app.post("/shares/<token>/revoke")
def revoke_share(token):
    user = current_user(request.headers)
    if user is None:
        return jsonify(error="unauthorized"), 401
    if not share.revoke_share(token, user["id"]):
        return jsonify(error="share not found"), 404
    return jsonify(revoked=True), 200


@app.get("/s/<token>")
def open_share(token):
    note = share.resolve_share(token)
    if note is None:
        return jsonify(error="link not found or revoked"), 404
    return jsonify(title=note["title"], body=note["body"]), 200


if __name__ == "__main__":
    db.init_db()
    app.run(port=5000)
