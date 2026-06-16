# Tokenomics Lab — what it costs, and the levers (Part 4)

Build a working model of what AI-assisted development costs at team scale, and the
engineering levers that control it.

## Where the spend concentrates
The token bill for agentic coding comes from: sessions, file reads, tool output,
**retries**, and conversation history. The single biggest lever is first-pass
success: the cheapest session is the one that ships without a re-roll. (This is why
Days 1–3 mattered: a good spec and a clean context buy first-pass success.)

## Exercise 1 — instrument a session
Run one running-build task and measure its token use. Identify the **two largest
cost drivers**. Usually: whole-file reads and a long retry loop. Write them down.

| Cost driver | Roughly how much | Lever to pull |
|-------------|------------------|---------------|
| | | |
| | | |

## Exercise 2 — model routing
Run one **mechanical** task (say, a rename or a formatting pass) on two model tiers
and compare cost against output quality. The pattern that emerges:
- **Frontier model** for planning and review (where judgment pays).
- **Faster, cheaper model** for mechanical edits and subagents.
- **Quality gates** (tests, the review panel) so routing never silently degrades
  output. Record your routing rule in `ROUTING_RULES.md`.

## Exercise 3 — AST context graph (live demo)
```bash
python tools/code_graph.py cost get_note
```
The graph answers "what depends on `get_note`?" from a small subgraph instead of
re-reading whole files. Compare the token counts. Community reports range around a
**70% token reduction** (with 90% claims on large monorepos), alongside reports of
**quality regressions** when retrieval misses structure. The discipline: **pilot,
measure both cost and quality, then decide.** The deep build-out is Masterclass 2.

## Session hygiene as cost control
Day 1's context discipline, now priced in dollars: everything in the window is paid
for on every turn. A clean session is a cheaper session.

**Deliverable:** a measured session with its two biggest cost drivers, a routing
rule, and context-graph pilot criteria (cost AND quality thresholds).
