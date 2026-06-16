# Diff 2 — review this (accept / reject / amend?)

**The prompt that produced it:** "Add a `GET /notes` endpoint that lists the
caller's own notes (id and title)."

**The diff:**
```diff
--- a/notes_api/db.py
+++ b/notes_api/db.py
@@ -55,3 +55,9 @@ def get_note(note_id):
         "SELECT * FROM notes WHERE id = ?", (note_id,)
     ).fetchone()
     conn.close()
     return row
+
+def list_notes():
+    conn = _connect()
+    rows = conn.execute("SELECT id, title FROM notes").fetchall()
+    conn.close()
+    return rows
--- a/notes_api/app.py
+++ b/notes_api/app.py
@@ -28,6 +28,13 @@ def read_note(note_id):
     return jsonify(title=note["title"], body=note["body"]), 200
+
+@app.get("/notes")
+def list_notes():
+    user = current_user(request.headers)
+    if user is None:
+        return jsonify(error="unauthorized"), 401
+    rows = db.list_notes()
+    return jsonify(notes=[dict(r) for r in rows]), 200
```

---

**Your call:**  ☐ Accept   ☐ Reject   ☐ Amend

**Why (defend it to your pair):**


_It runs, it returns 200, the shape is right. Whose notes does it return? Read the
SQL. What does "the caller's own notes" require that this is missing?_
