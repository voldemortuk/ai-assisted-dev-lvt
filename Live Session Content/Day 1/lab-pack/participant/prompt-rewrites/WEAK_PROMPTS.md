# Weak Prompts — rewrite these (Part 4)

Three weak prompts drawn from real AI-assisted development failures. Rewrite each
to the standard of a good ticket: specificity, constraints, success criteria, and
a definition of done. Run before and after against the repo and compare the diffs.

---

### Weak prompt 1
> "Add auth to the notes endpoint."

What's missing: which endpoint, what kind of auth, what the existing pattern is,
what "done" looks like, whether a test is expected.

**Your rewrite:**

---

### Weak prompt 2
> "Make the share thing work and add some tests."

What's missing: what the share thing is, the contract, what the tests must assert,
the house test style, the definition of done.

**Your rewrite:**

---

### Weak prompt 3
> "Refactor db.py, it's messy."

What's missing: what "messy" means here, what must not change (behaviour,
interfaces), the constraints, how you'll verify nothing broke. This may not even
be an agent task as written.

**Your rewrite:**

---

## House-style pinning
Pick one rewrite and add a **worked example** from an existing repo module (for
instance, paste `get_note_for_owner` as the pattern to follow). Show that the
output now matches conventions for naming, error handling, and test structure on
the first pass. A worked example steers harder than three sentences of description.
