# Day 2 — Workflow Discipline · Instructor Runsheet (6 hours)

Host: **Kyle Cheng** · Programme: LVT AI-Assisted Development · Deck: `day2-session-deck/index.html`

Day 2 turns Day 1's loop into a workflow with gates before code exists. The
centerpiece (Part 3) builds the **running build**: the share-a-note feature that
Day 3 reviews and Day 4 automates. The spec written here decides what Day 3 finds.

**Timing model:** 360 min wall-clock = 300 focused min + 2 breaks + buffer.

---

## Block-by-block

| Time | Block | Deck | Lab pack |
|------|-------|------|----------|
| 0:00–0:15 | **Open** — cover, Kyle, day map, through-line, warm-up, house rules | 1–6 | — |
| 0:15–1:10 | **Part 1 · Sizing** (55m): four approaches, the 3-signal rubric, chunking | 7–9 | — |
| 0:45–1:10 | ↳ **Lab 1** (25m): classify the 12-item backlog + chunk the OAuth ticket | 10 | `participant/BACKLOG_12.md` · `SIZING_RUBRIC.md` · key: `facilitator/PART1_SIZING_KEY.md` |
| 1:10–1:25 | **Break** | — | — |
| 1:25–2:40 | **Part 2 · Plan Mode** (75m): review economics, reading a plan, intervening | 12–14 | — |
| 2:00–2:40 | ↳ **Lab 2** (40m): drive a change through plan mode + flawed-plan drill | 15 | `participant/FLAWED_PLAN.md` · key: `facilitator/PART2_PLAN_DEFECTS_KEY.md` |
| 2:40–4:10 | **Part 3 · Spec-Driven** (90m): light vs full, executable spec, the chain | 17–19 | — |
| 3:20–4:10 | ↳ **Lab 3** (50m): PRD → spec → build the share feature, watch gaps surface | 20 | `bootcamp-repo/specs/*` · `participant/SPEC_TEMPLATE.md` · key: `facilitator/PART3_SPEC_GAPS_KEY.md` |
| 4:10–4:25 | **Break** | — | — |
| 4:25–5:30 | **Part 4 · CLAUDE.md** (65m): belongs/doesn't, context cost, multi-dir | 22–23 | — |
| 5:00–5:30 | ↳ **Lab 4** (30m): write CLAUDE.md, before/after, trim a third | 24 | `participant/CLAUDE_MD_LAB.md` · `CLAUDE_MD_BLOATED_EXAMPLE.md` · key: `facilitator/PART4_CLAUDE_MD_KEY.md` |
| 5:30–5:45 | **Wrap** — running build status + reflection + Day 3 bridge | 25–26 | — |

---

## The continuity hinge (read `facilitator/PART3_SPEC_GAPS_KEY.md` before Part 3)
The four gaps in `SHARE_NOTE_SPEC_v0_GAPPED.md` map one-to-one onto the four
defects Day 3 catches:
- vague revoke contract → revoke that doesn't 404 (Day 3 black-box hat)
- unspecified token randomness → guessable token (Day 3 security/OWASP)
- unstated ownership → broken access control (Day 3 OWASP A01)
- "tests cover X" with no contract → a test that asserts nothing (Day 3 slop hunt)
Land the line: **spec gaps surface as build gaps.**

## What every engineer leaves with
- [ ] A defended 12-item sizing classification + a chunked oversized ticket
- [ ] A change driven through plan mode with one recorded intervention; the flawed plan corrected
- [ ] The share feature committed **with its spec** (the running build for Day 3)
- [ ] A CLAUDE.md with measured before/after, trimmed by ≥33%

## Pre-flight
- `cd lab-pack/bootcamp-repo && pip install -r requirements.txt && pytest -q` → 2 passed (clean baseline, no share feature yet).
- `ruff check .` → clean.
- Open `day2-session-deck/index.html`, press `.` for notes, walk all 27 slides, check print preview.
- Read all four `facilitator/` keys, especially Part 3.
