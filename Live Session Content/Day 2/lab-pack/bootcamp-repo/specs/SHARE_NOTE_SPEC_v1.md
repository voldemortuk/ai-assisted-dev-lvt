# Spec v1 — Share a note (executable, gaps closed)

The iterated spec. Every acceptance criterion is a contract the agent can be
tested against. This is what a spec looks like when the silences are closed.

## Endpoints
| Method | Path | Auth | Returns |
|--------|------|------|---------|
| POST | `/notes/<id>/share` | yes | `201 { "share_url": "/s/<token>" }` |
| POST | `/shares/<token>/revoke` | yes | `200 { "revoked": true }` |
| GET | `/s/<token>` | no | `200 { "title", "body" }` or `404` |

## Acceptance criteria (each is a test)
1. **Mint:** an owner shares their note and receives a `/s/<token>` URL. `201`.
2. **Open:** `GET /s/<token>` returns the note's title and body. `200`.
3. **Revoke stops resolution:** after `revoke`, `GET /s/<token>` returns `404`.
   *(The link must actually stop working, not merely report success.)*
4. **Tokens are unguessable:** a token must be generated from a cryptographically
   secure random source (`secrets.token_urlsafe`), not derived from the note id
   or a static value. Holding one link must not let you construct another.
5. **Owner-only mint:** a user who does not own the note gets `404` from share.
6. **Owner-only revoke:** only the note's owner may revoke its links.

## Constraints
- Reuse `notes.get_note_for_owner(note_id, owner_id)` for the ownership check.
- Parameterised SQL only. No secrets in source; config from the environment.
- New `shares` table: `token` (PK), `note_id`, `revoked`.

## Non-goals
- Edit-through-link, expiry, link passwords, view counts, folder sharing.

## Definition of done
- All six acceptance tests pass, including a **human-authored** assertion that a
  revoked link returns `404` (the contract from AC #3).
- `pytest` and `ruff` are green. No hardcoded secrets.

---

> Notice what changed from v0: every vague line became a testable contract.
> The spec now *fails the build* if revoke doesn't 404, if a token is guessable,
> or if a non-owner can share. The agent can't pass by writing tidy code that
> asserts nothing — the spec tells it what to assert.
