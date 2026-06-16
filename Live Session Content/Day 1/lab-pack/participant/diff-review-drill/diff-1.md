# Diff 1 — review this (accept / reject / amend?)

**The prompt that produced it:** "Fix the 500 on `POST /notes` when `title` or
`body` is missing."

**The diff:**
```diff
--- a/notes_api/app.py
+++ b/notes_api/app.py
@@ -10,9 +10,13 @@ def create_note():
     user = current_user(request.headers)
     if user is None:
         return jsonify(error="unauthorized"), 401
-    data = request.get_json(force=True)
-    note_id = notes.create_note(user["id"], data["title"], data["body"])
-    return jsonify(id=note_id), 201
+    try:
+        data = request.get_json(force=True)
+        note_id = notes.create_note(user["id"], data["title"], data["body"])
+        return jsonify(id=note_id), 201
+    except Exception:
+        return jsonify(id=None), 200
```

---

**Your call:**  ☐ Accept   ☐ Reject   ☐ Amend

**Why (defend it to your pair):**


_What does this do when the body is missing? What does it do when the database
is down? What status code does the client get, and is that honest?_
