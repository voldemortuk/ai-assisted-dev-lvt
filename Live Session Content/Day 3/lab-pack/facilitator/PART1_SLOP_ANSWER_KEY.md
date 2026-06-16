# FACILITATOR — Part 1 Slop Answer Key

Four planted slop problems in the share diff. Score one point each. Participants
should produce a file:line and a one-line reason per catch.

### 1. Plausible-but-wrong helper — `notes_api/share.py:20` `generate_share_token`
```python
return "shr_" + str(note_id) + "_" + SHARE_SECRET[:8]
```
Reads fine, named "hard-to-guess". It is fully deterministic: token for note 1 is
always `shr_1_sk_share`. Anyone who holds one link can enumerate every note's link.
**Fix:** `secrets.token_urlsafe(24)`, stored, not derived. (Also a security finding
— that overlap is the point of Day 3.)

### 2. Copy-paste drift — `notes_api/share.py:39` `revoke_share`
```python
db.set_share_revoked(share["note_id"])   # should be the token
```
`set_share_revoked` matches `WHERE token = ?`. Passing `note_id` matches no row, so
**revocation silently does nothing** and the link keeps resolving. The shape is
right; one argument is wrong.
**Fix:** `db.set_share_revoked(token)`.

### 3. Dead branch — `notes_api/share.py:50-56` `resolve_share`
```python
    if note is not None:
        return note
    else:
        return None
    return note      # <- unreachable
```
The trailing `return note` can never run. Harmless, but it's a tell that nobody
read the function. **Fix:** delete the dead line (and simplify the if/else).

### 4. Test that asserts nothing — `tests/test_share.py`
- `test_create_share_returns_a_token` → `assert token` only checks truthiness of a
  string; it would pass for any non-empty token, including a guessable one.
- `test_revoke_share_runs` → asserts `revoke_share` returned `True`; never checks
  the link **stops resolving**. This is why the revoke bug shipped green.
**Fix:** assert the contract (revoked link → `resolve_share` returns `None`).

## Teaching beats
- Tests are GREEN (`pytest` → 5 passed). Green ≠ covered. Show the suite passing,
  then ask "so is revoke tested?"
- The token bug is BOTH slop and a vuln — preview of Part 3, and of why one hat
  isn't enough (Part 2).
- The self-verifying loop (CLAUDE.md) catches *broken* tests; it does **not** catch
  *empty* ones. That gap is the human's job.
