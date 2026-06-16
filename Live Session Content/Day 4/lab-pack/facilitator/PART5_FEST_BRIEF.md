# FACILITATOR — Part 5: Ship the Build + the Sealed Fest Brief

## A. Ship the running build through the full machinery
Each engineer wires **one hook and one subagent** into their running build and ships
it through the Day 3 gates: panel review, security pass, the human-authored
assertion, and a named sign-off. The good end state: a gated, automated build with
every gate's trail visible. Confirm each engineer's build has:
- [ ] at least one hook firing (format or guard)
- [ ] one subagent delegation pattern in use
- [ ] the Day 3 gate trail (panel + security + human assertion + signature)

## B. Form teams + hand out the sealed brief
Teams of 3–4 for Day 5. Hand each team the brief below. Keep it sealed until you
form teams; the point is they scope it fresh on Fest day.

---

## SEALED FEST BRIEF — Day 5 Agentic Fest

> **PRD: "Share with an expiry."**
> Build on the notes-api running build. Extend the share feature so a public link
> can carry an **expiry**: when an owner mints a link, they may set a lifetime
> (e.g. 24 hours). After it expires, the link returns `404`, exactly like a revoked
> one. Links with no expiry behave as today.
>
> **In scope:** an optional expiry on mint; expired links stop resolving; the
> existing security properties hold (owner-only mint/revoke, unguessable tokens,
> parameterised SQL).
> **Out of scope:** changing the token format, link passwords, view counts.
>
> **Success criteria (the Fest gate):**
> - Working code: expired links 404, non-expired links resolve, no-expiry links
>   behave as before.
> - The full gate trail: a black-box test, a multi-hat review (security + design),
>   at least one **human-authored** assertion on the expiry contract, and a named
>   sign-off.
> - At least **one hook firing** and **at least one orchestration primitive** in use.
>
> This is a deliberate continuation of the running build, so every habit from Days
> 1–4 applies: size it, spec it, gate it, automate it.

---

## C. Programme retro checkpoint
Each team lists the **three practices it intends to standardize first**. Capture
these; they're the real ROI conversation for LVT.

## Why this brief works
It's a small, well-specified extension of the exact feature they've carried all
week, so no time is lost on unfamiliar code. It naturally exercises every gate
(expiry is a contract that's easy to under-assert, which is why the human-authored
assertion matters), and it has clean seams for delegating to a subagent.
