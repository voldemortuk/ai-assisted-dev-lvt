# FACILITATOR — Part 4 Tokenomics Key

## Exercise 1 — instrument a session
Expected two largest cost drivers on this repo: **whole-file reads** (re-reading
modules instead of targeting interfaces) and **retry loops** (a vague prompt or a
poisoned context causing re-rolls). Both trace straight back to Days 1–3 habits.
The line to land: **the cheapest session is the one that ships on the first pass.**

## Exercise 2 — routing
Expected emergent rule:
- Frontier model for **planning and review** (judgment-heavy).
- Fast/cheap model for **mechanical edits and subagents** (low ambiguity, verifiable).
- A **quality gate** on every routed path so a cheaper tier can't silently degrade
  output. If the gate fails, route back up.
Watch for the failure mode: routing everything to the cheap tier to save money, then
eating it back in re-rolls and a missed review finding. Routing without a gate is a
false economy.

## Exercise 3 — the code-graph demo (run live)
```bash
python tools/code_graph.py cost get_note
```
On this repo it reports roughly a **90%+ reduction** answering "what depends on
get_note?" from a subgraph vs whole-file reads. Use the real number on screen, then
add the honest caveat: community reports cluster around **~70% reduction (up to ~90%
on large monorepos)**, with **quality regressions when retrieval misses structure**.
The discipline is **pilot → measure cost AND quality → decide**, not adopt on the
headline number. The deep build-out is Masterclass 2.

## The frame to leave them with
The token bill is an **engineering problem with known levers**: first-pass success,
routing, context curation, caching, and (piloted) context graphs, plus budget
guardrails and per-team attribution so it's visible and governable.
