"""Flask routes for the Notes API — Day 1 baseline.

Day 2 lab: the spec-driven share feature adds POST /notes/<id>/share,
POST /shares/<token>/revoke, and GET /s/<token>. Build them from the spec.
"""

from flask import Flask, request, jsonify

from . import db, notes
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


# --- Day 2 spec-driven lab builds the share endpoints below this line ---


if __name__ == "__main__":
    db.init_db()
    app.run(port=5000)
