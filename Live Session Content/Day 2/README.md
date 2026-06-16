# Day 2 — Workflow Discipline · Live Session Content

Full 6-hour delivery package for **Day 2** of the LVT AI-Assisted Development
Program (4 content days + a Day 5 Agentic Fest). Day 2 turns Day 1's loop into a
repeatable workflow with gates that fire before any code exists: sizing, plan
mode, spec-driven builds, and CLAUDE.md project memory.

Built to the `Live_Session_Deck_Skills.md` template (cream · navy #2C3F8E · cyan
#5BC4D2). Host: **Kyle Cheng** (MTS @ Anthropic).

## The through-line
Part 3 builds the **running build**: the share-a-note feature. That exact feature
carries through Day 3 (trust gates) and Day 4 (automation). The spec written here
decides what Day 3 finds, so the spec gaps and the Day 3 planted bugs are the same
four issues, by design.

## What's in here
```
Day 2/
├── day2-session-deck/index.html   ← the live session deck (27 slides)
├── lab-pack/
│   ├── bootcamp-repo/             ← Day 1 baseline (users + notes, NO share yet; pytest → 2 passed)
│   │   └── specs/                 ← the PRD, gapped spec v0, executable spec v1
│   ├── participant/               ← backlog, sizing rubric, flawed plan, spec template, CLAUDE.md lab
│   └── facilitator/               ← 4 answer keys (sizing, plan defects, spec gaps, CLAUDE.md)
├── INSTRUCTOR_RUNSHEET.md         ← minute-by-minute 6-hour guide
└── README.md
```

## Run the deck
Open `day2-session-deck/index.html`. `← →` navigate · `F` fullscreen · `.` notes · `?s=N` deep-link.

## Run the baseline
```bash
cd lab-pack/bootcamp-repo
pip install -r requirements.txt
pytest -q          # 2 passed — the pre-share baseline
```

## The four labs
| Part | Lab | Builds | Deliverable |
|------|-----|--------|-------------|
| 1 · Sizing (55m) | classify + chunk | a defended 12-item backlog | sizing rubric kept by the team |
| 2 · Plan Mode (75m) | drive + flawed-plan drill | a corrected planted-defect plan | plan-review habit |
| 3 · Spec-Driven (90m) | PRD → spec → build | the share feature + its spec | **the running build for Day 3** |
| 4 · CLAUDE.md (65m) | before / after / trim | project memory with evidence | a trimmed, load-bearing CLAUDE.md |

See `INSTRUCTOR_RUNSHEET.md` and `facilitator/PART3_SPEC_GAPS_KEY.md` for how the
Day 2 spec gaps become the Day 3 planted bugs.
