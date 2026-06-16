# Day 1 — AI-Native Software Engineering · Instructor Runsheet (6 hours)

Host: **Kyle Cheng** · Programme: LVT AI-Assisted Development · Deck: `day1-session-deck/index.html`

Day 1 is sequenced for a cohort mostly new to AI-assisted development. The morning
builds the mental model; the afternoon spends it on the shared bootcamp repo. Every
block lands in a lab, and every engineer ships a committed change.

**Timing model:** 360 min wall-clock = 300 focused min + 2 breaks + buffer.

---

## Block-by-block

| Time | Block | Deck | Lab pack |
|------|-------|------|----------|
| 0:00–0:15 | **Open** — cover, Kyle, day map, through-line, warm-up, house rules | 1–6 | — |
| 0:15–1:15 | **Part 1 · How Agents Work** (60m): prediction + non-determinism, context window, agentic loop, capability map | 7–10 | — |
| 0:55–1:15 | ↳ **Lab 1** (20m): same-prompt-twice + will-it-fail + token budget | 11 | `participant/WILL_IT_FAIL_CARDS.md` · key: `facilitator/PART1_MENTAL_MODELS_KEY.md` |
| 1:15–1:30 | **Break** | — | — |
| 1:30–2:40 | **Part 2 · First Contact** (70m): the core cycle, reading AI diffs, permission prompts | 13–15 | — |
| 1:55–2:40 | ↳ **Lab 2** (45m): first committed change + diff-review drill (3 diffs) | 16 | `bootcamp-repo/BACKLOG.md` · `participant/diff-review-drill/*` · key: `facilitator/PART2_DIFF_REVIEW_KEY.md` |
| 2:40–3:50 | **Part 3 · Context Engineering** (70m): what competes for space, scoping, reset discipline | 18–20 | — |
| 3:20–3:50 | ↳ **Lab 3** (30m): bloated vs curated + context audit + eviction rule | 21 | `participant/CONTEXT_AUDIT.md` · key: `facilitator/PART3_CONTEXT_KEY.md` |
| 3:50–4:05 | **Break** | — | — |
| 4:05–5:05 | **Part 4 · Prompting** (60m): prompt anatomy, worked examples, anti-patterns | 23–24 | — |
| 4:35–5:05 | ↳ **Lab 4** (30m): rewrite 3 weak prompts + pin house style + seed library | 25 | `participant/prompt-rewrites/*` · `PROMPT_PATTERN_LIBRARY_v0.md` · key: `facilitator/PART4_PROMPT_REWRITES_KEY.md` |
| 5:05–5:35 | **Part 5 · Responsible AI** (30m): five concerns + flag-the-risky-ones | 27–28 | `participant/responsible-ai/*` · `RESPONSIBLE_AI_CHECKLIST.md` · key: `facilitator/PART5_RESPONSIBLE_AI_KEY.md` |
| 5:35–5:45 | **Wrap** — recap (5 artifacts) + reflection + Day 2 bridge | 29–30 | — |

---

## The diff-review drill foreshadows Day 3 (read `facilitator/PART2_DIFF_REVIEW_KEY.md`)
The three diffs escalate: diff 1 your eye catches, diff 2 needs you to read the SQL
(missing owner filter = the Day 3 A01 preview), diff 3 needs you to read what runs
and what the test asserts (the core of Day 3). Name the failure mode each time.

## What every engineer leaves with
- [ ] A committed, tested change on the bootcamp repo, driven end to end
- [ ] A personal context checklist from a session they watched fail and recovered
- [ ] Before/after prompt rewrites with diffs + one entry in the Prompt Pattern Library v0
- [ ] A responsible-AI checklist tuned to agentic coding at LVT

## Pre-flight
- `cd lab-pack/bootcamp-repo && pip install -r requirements.txt && pytest -q` → 2 passed.
- `ruff check .` → clean. Note: the missing-fields 500 (backlog item 1) is a real,
  reproducible bug — that's the first-change target, not a broken repo.
- Open `day1-session-deck/index.html`, press `.` for notes, walk all 31 slides.
- Read all five `facilitator/` keys.
