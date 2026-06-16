# FACILITATOR — Part 3 Spec-Gaps Key (the continuity hinge)

This is the most important key in the programme. The four gaps in
`SHARE_NOTE_SPEC_v0_GAPPED.md` are not random — each one produces a specific
defect, and **those defects are exactly what Day 3's trust gates catch.** When the
agent builds from the gapped spec, point at the build and trace each defect back
to the silent line.

| Spec v0 gap | Build defect it produces | Caught on Day 3 by |
|-------------|--------------------------|--------------------|
| "Revoke returns success" (says nothing about *after*) | `revoke_share` marks something revoked but the link still resolves | Black-box hat (Part 2) + the human-authored assertion |
| "Tokens go in the URL path" (no unpredictability) | deterministic token `shr_<id>_<secret>`, guessable | Security hat + OWASP skill (Part 3) |
| Ownership on share/revoke unstated | any signed-in user can share any note by id (broken access control) | Security hat + OWASP A01 (Part 3) |
| "Tests cover share/open/revoke" (no contract) | a revoke test that asserts success, never that the link 404s | Slop hunt (Part 1) — "a test that asserts nothing" |

## How to run the lab
1. Have them build from **v0** first. The agent produces tidy code that satisfies
   every literal line of the spec and is quietly wrong in four ways.
2. Run it, read it, surface the gaps. Ask: "the spec said tests cover revoke —
   do they?" Let them feel that *the spec, not the agent, is the problem.*
3. Iterate to **v1** (`SHARE_NOTE_SPEC_v1.md`) and re-run. Now the spec *fails the
   build* unless revoke 404s, tokens are random, and non-owners are blocked.
4. Land the line: **spec gaps surface as build gaps.** Defects trace to a spec line
   you can see and fix, not to agent mystery.

## The payoff for the week
The feature each engineer commits here is the Day 3 running build. If they ship
from v0, Day 3's gates have real planted defects to catch (the intended path). If
they ship from v1, they've pre-empted the gates — which is also a valid outcome,
and the honest framing is: *this is why you write the spec before the code.*
