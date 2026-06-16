# Slop Hunt — Review Checklist (Part 1)

Use this on the share-feature diff (`notes_api/share.py`, `db.py`, `tests/test_share.py`).
Score one point per item you catch with a file:line and a one-line reason. This
checklist transfers to every AI-assisted PR you review at LVT.

## The four faces of slop

- [ ] **Plausible-but-wrong helper.** A function that reads cleanly and is named
      well but does the wrong thing. Read what it *computes*, not what it's called.
      _Hint: how is a share token actually generated? Could you generate someone
      else's?_

- [ ] **Copy-paste drift.** Code lifted from a neighbour with one field left
      pointing at the wrong thing. The shape is right; one argument is wrong.
      _Hint: when you revoke a link, what value gets marked revoked?_

- [ ] **Dead branch.** A branch or statement that can never execute — an `else`
      after a guaranteed return, an unreachable line, a condition that's always
      false. Tidy, harmless-looking, and a sign nobody read it.

- [ ] **A test that asserts nothing.** A test that runs the code and "passes" but
      never checks the contract — asserts a dict is truthy, asserts the call
      didn't throw, or asserts nothing at all. Green, but covering air.
      _Hint: which test claims to cover revoke but never checks the link stops working?_

## Calibration questions (the meta-skill)
- [ ] For each problem: is this **scaffolding** review (line-by-line, building
      intuition) or a **permanent gate** (behaviour, contract, a test per area)?
- [ ] Which of these would a passing test suite have caught? Which would it not?
- [ ] Did the tidy formatting make you *more* trusting? That's the trap.

## Self-verifying loop (do this once)
Add the loop from `CLAUDE.md` so the agent runs `pytest` and `ruff` before
presenting any diff. Re-run the agent on a small change and confirm it reports
both. Note: the loop catches *broken* tests; it does not catch *empty* ones — that
still needs you.

**Score:** ___ / 4 problems found · scaffolding-vs-gate call made for each ✅
