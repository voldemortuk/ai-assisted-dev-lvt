# FACILITATOR — Part 1 Sizing Key

There's defensible spread on a few of these — the point is the *reasoning* from
blast radius / ambiguity / reviewability, not a single right label. Suggested
classification:

| # | Item | Approach | Why |
|---|------|----------|-----|
| 1 | Typo in error string | **Quick** | Zero blast radius, obvious done, glance-reviewable |
| 2 | Share-a-note feature | **Spec** | Multi-step, contract matters, becomes the running build |
| 3 | Rename `body`→`content` everywhere | **Plan** | Wide blast radius, mechanical but easy to miss a site |
| 4 | Bump Flask one minor | **Quick** (verify with tests) | Low ambiguity; the test suite is the reviewer |
| 5 | Decide Postgres before next quarter | **No agent** | A decision, not a change. Judgment + tradeoffs |
| 6 | Add `GET /notes` list | **Quick** or **Plan** | Single endpoint; Plan if you want the contract pinned |
| 7 | Add pagination | **Plan** | Edge cases (defaults, max, off-by-one) reward a plan |
| 8 | Investigate intermittent 500 | **No agent first**, then Quick | Diagnosis is judgment; the fix may be small once found |
| 9 | Add `created_at` + backfill | **Plan** | Migration + existing-data backfill = real blast radius |
| 10 | README test badge | **Quick** | Trivial, reversible |
| 11 | OAuth2 re-architecture | **Spec** (+ chunking) | High blast radius, high ambiguity, multi-week |
| 12 | Input validation 400 | **Quick** or **Plan** | Small, but Plan if validation rules are contested |

## Chunking item 11 (model answer)
A clean break with explicit seams:
1. **Token model + storage** — add refresh-token table and model. Interface: a
   `TokenStore` with `issue / validate / revoke`.
2. **Auth middleware** — swap bearer-check for OAuth2 access-token validation
   behind the *same* `current_user(headers)` interface, so callers don't change.
3. **Token endpoints** — `/oauth/token` (grant) and refresh, against `TokenStore`.
4. **Migration + dual-run** — accept old bearer tokens during a deprecation window.
5. **Cutover + cleanup** — remove the old path once clients migrate.

The seam that matters: keep `current_user()` stable so every route is insulated
from the swap. That clean interface is what makes each chunk independently
reviewable.
