# Day 1 — AI-Native Software Engineering · Live Session Content

Full 6-hour delivery package for **Day 1** of the LVT AI-Assisted Development
Program (4 content days + a Day 5 Agentic Fest). Day 1 builds the mental model of
what a coding agent does and where it fails, then spends it: every engineer ships
one reviewed, tested, committed change on the shared bootcamp repo.

Built to the `Live_Session_Deck_Skills.md` template (cream · navy #2C3F8E · cyan
#5BC4D2). Host: **Kyle Cheng** (MTS @ Anthropic).

## What's in here
```
Day 1/
├── day1-session-deck/index.html   ← the live session deck (31 slides, 5 parts)
├── lab-pack/
│   ├── bootcamp-repo/             ← Day 1 starting repo (users + notes; pytest → 2 passed)
│   │   └── BACKLOG.md             ← small changes for the first-commit lab
│   ├── participant/
│   │   ├── diff-review-drill/     ← 3 AI diffs of rising subtlety + worksheet
│   │   ├── prompt-rewrites/       ← weak prompts + anatomy reference
│   │   ├── responsible-ai/        ← prompts/transcripts to flag
│   │   ├── WILL_IT_FAIL_CARDS.md · CONTEXT_AUDIT.md
│   │   ├── PROMPT_PATTERN_LIBRARY_v0.md · RESPONSIBLE_AI_CHECKLIST.md
│   └── facilitator/               ← 5 answer keys (one per part)
├── INSTRUCTOR_RUNSHEET.md         ← minute-by-minute 6-hour guide
└── README.md
```

## Run the deck
Open `day1-session-deck/index.html`. `← →` navigate · `F` fullscreen · `.` notes · `?s=N` deep-link.

## Run the repo
```bash
cd lab-pack/bootcamp-repo
pip install -r requirements.txt
pytest -q          # 2 passed
```
The missing-fields 500 (BACKLOG item 1) is a real, reproducible bug — it's the
first-change target, not a broken repo.

## The five labs
| Part | Lab | Builds |
|------|-----|--------|
| 1 · How Agents Work (60m) | same-prompt-twice, will-it-fail, token budget | a shared mental model |
| 2 · First Contact (70m) | first committed change + 3-diff review drill | one shipped change + review reps |
| 3 · Context (70m) | bloated vs curated + audit | a personal context checklist |
| 4 · Prompting (60m) | rewrite weak prompts + seed library | Prompt Pattern Library v0 |
| 5 · Responsible AI (30m) | flag risky prompts + checklist | a responsible-AI checklist |

The diff-review drill (Part 2) deliberately foreshadows Day 3: the missing-owner
filter and the assert-nothing test are the same failure modes the Trust Triad
catches. See `facilitator/PART2_DIFF_REVIEW_KEY.md`.
