"""Flask routes for the Notes API.

Endpoints:
  POST /notes                 create a note (auth required)
  POST /notes/<id>/share      mint a public share link (auth required)
  POST /shares/<token>/revoke revoke a share link (auth required)
  GET  /s/<token>             public: resolve a share link to its note (no auth)

The /notes/<id>/share and /s/<token> paths are the Day 2 feature and the focus
of the Day 3 trust gates.
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


@app.post("/notes/<int:note_id>/share")
def share_note(note_id):
    user = current_user(request.headers)
    if user is None:
        return jsonify(error="unauthorized"), 401
    # Mint and persist a public link for this note.
    token = share.create_share(note_id)
    if token is None:
        return jsonify(error="note not found"), 404
    return jsonify(share_url="/s/" + token), 201


@app.post("/shares/<token>/revoke")
def revoke_share(token):
    user = current_user(request.headers)
    if user is None:
        return jsonify(error="unauthorized"), 401
    ok = share.revoke_share(token)
    if not ok:
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
