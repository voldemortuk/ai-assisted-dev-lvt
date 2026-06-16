# FACILITATOR — Part 4 Prompt-Rewrites Key

For each weak prompt, the rewrite should add specificity, constraints, success
criteria, and a definition of done. Model rewrites:

### 1. "Add auth to the notes endpoint."
> "In `notes_api/app.py`, require a valid bearer token on `GET /notes/<id>` using
> the existing `current_user(request.headers)` helper. Return `401` when the token
> is missing or invalid. Don't change the auth mechanism itself. Add a test that a
> request with no token gets `401` and a valid one gets `200`. Run `pytest -q` and
> `ruff check .` before showing the diff."
Why better: names the endpoint, reuses the existing helper, states the 401
contract, defines done with a test.

### 2. "Make the share thing work and add some tests."
> Not yet a prompt. First state the contract. "Implement `POST /notes/<id>/share`
> per `specs/SHARE_NOTE_SPEC_v1.md`: it mints an unguessable public token, only the
> owner may share, and a revoked link returns 404. Add tests asserting each of
> those three, including a human-authored assertion that a revoked link 404s."
Why better: points at the spec, names the three contracts the tests must assert.
(On Day 1 the spec doesn't exist yet, so the teaching point is: this is a *spec*
task, which is exactly what Day 2 Part 3 is.)

### 3. "Refactor db.py, it's messy."
> "In `notes_api/db.py`, extract the repeated connect/execute/close pattern into a
> single helper, keeping every function's behaviour and signature identical. Don't
> change the schema or the public API. Confirm `pytest -q` still passes with no test
> changes."
Why better: defines "messy" concretely, pins behaviour-preservation, gives a
verification. Also a candidate for "ask for a plan first" since the approach is
open.

## House-style pinning
The strongest single lever: paste one canonical snippet (for example
`get_note_for_owner`) and say "match this style." Output then lands on house
conventions for naming, error handling, and test structure on the first pass.
Demonstrate before/after live if time allows.

## The bridge
"Capture what worked" feeds the Prompt Pattern Library v0, which becomes the team
skills work on Day 4.
