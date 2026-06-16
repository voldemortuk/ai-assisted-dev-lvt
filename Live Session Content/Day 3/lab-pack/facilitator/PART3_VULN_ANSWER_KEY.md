# FACILITATOR — Part 3 Security / OWASP Answer Key

The OWASP skill (`.claude/skills/owasp-review/`) and the security subagent
(`.claude/agents/security-reviewer.md`) should surface all of the below when run
against the share diff. The secret-scan hook is the deterministic backstop.

## Planted vulnerabilities

### A03 Injection — `notes_api/db.py:65` `get_note`
```python
query = "SELECT * FROM notes WHERE id = %s" % note_id
```
String-formatted SQL. `note_id` arrives from the URL (`/notes/<int:note_id>/share`
coerces to int, but `get_note` is also reachable from `resolve_share` and is the
team's shared accessor — the pattern is the vuln). **Fix:** parameterise:
`conn.execute("SELECT * FROM notes WHERE id = ?", (note_id,))`.

### A01 Broken Access Control — `notes_api/share.py:23` `create_share`
```python
note = db.get_note(note_id)          # no owner check
```
The route authenticates the caller but never checks they own the note. Any
signed-in user can mint a public link to **any** note by id. The owner-checked
accessor `notes.get_note_for_owner` exists and is deliberately not used.
**Fix:** mint only if `notes.get_note_for_owner(note_id, user["id"])` is not None;
thread `user["id"]` through `create_share`. Same gap on `revoke_share`.

### A02/A07 Predictable token — `notes_api/share.py:20` `generate_share_token`
Deterministic token (see Part 1). A security finding too: the public link is the
only thing gating an unauthenticated read, and it's guessable. **Fix:**
`secrets.token_urlsafe(24)`.

### A05 Hardcoded secrets — `db.py:17` `DB_PASSWORD`, `share.py:13` `SHARE_SECRET`
Literal credentials in source. **Fix:** `os.environ[...]`. The secret-scan hook
blocks the commit until they're gone.

## Lab checkpoints
- **Install at project scope** so every engineer inherits identical checks (it's in
  `.claude/skills/`, committed). Note the real-world substitute: a vetted community
  skill such as `agamm/claude-code-owasp` — installed the same way, *read before
  installing*, version-pinned.
- **Secret-scan hook fires:** `bash .claude/hooks/secret_scan.sh` exits **2** and
  names `db.py:17` + `share.py:13`. (It's wired PreToolUse on `git commit` and
  PostToolUse on Write/Edit in `settings.json`.)
- **Triage one finding end to end** with `TRIAGE_TEMPLATE.md`. Best demo: the
  broken-access-control finding — reproduce it (Mallory shares Alice's note), then
  fix and re-run.
- **Marketplace as attack surface:** drive the point that a skill/plugin runs with
  the agent's privileges. Prefer reputable sources, read before install, pin
  versions, treat adoption as its own security review.
