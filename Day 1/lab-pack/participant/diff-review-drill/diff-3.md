# Diff 3 — review this (accept / reject / amend?)

**The prompt that produced it:** "Reject a note whose title is longer than 200
characters with a 400. Add a test."

**The diff:**
```diff
--- a/notes_api/app.py
+++ b/notes_api/app.py
@@ -9,9 +9,12 @@ def create_note():
     user = current_user(request.headers)
     if user is None:
         return jsonify(error="unauthorized"), 401
     data = request.get_json(force=True)
     note_id = notes.create_note(user["id"], data["title"], data["body"])
+    if len(data["title"]) > 200:
+        return jsonify(error="title too long"), 400
     return jsonify(id=note_id), 201
--- a/tests/test_notes.py
+++ b/tests/test_notes.py
@@ -14,3 +14,8 @@ def test_owner_check_blocks_other_user():
     assert notes.get_note_for_owner(note_id, owner_id=2) is None
+
+def test_long_title_is_rejected():
+    long_title = "x" * 250
+    note_id = notes.create_note(1, long_title, "body")
+    assert note_id
```

---

**Your call:**  ☐ Accept   ☐ Reject   ☐ Amend

**Why (defend it to your pair):**


_This one is tidy, idiomatic, and has a test. Two things to check: when does the
validation run relative to the write? And what does the test actually assert about
the 400? This is the kind of diff Day 3 is built around._
