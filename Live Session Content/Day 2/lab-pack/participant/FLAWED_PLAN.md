# Plan-Mode Lab — the flawed plan drill (Part 2)

Below is a plan an agent produced for backlog **item 9**: *"Add a `created_at`
timestamp to notes and backfill existing rows."* It looks reasonable. It contains
planted defects. Find them before you would approve it. Do not let the tidy
numbering lull you.

---

## Agent's plan: add `created_at` to notes

1. Add a `created_at` column to the `notes` table in `notes_api/db.py`,
   type `TEXT`, default `CURRENT_TIMESTAMP`.
2. Update `create_note()` in `notes_api/notes.py` to set `created_at`.
3. Update the `GET /notes/<id>` response in `notes_api/app.py` to include
   `created_at`.
4. Update `tests/test_share.py` to assert the new field is present.
5. Run the app to confirm it starts.

---

## Your job
Read it as a reviewer. Mark every defect with the step number and a one-line fix.
There are at least three. Consider:

- Does every step touch the **right file**?
- Is there a step the task needs that the plan **omits**?
- Is there an **unstated assumption** that will bite on real data?
- Does the **verification** step actually verify the change?

Then: re-plan it yourself in two or three corrected steps, and only approve a plan
you would defend to your pair.
