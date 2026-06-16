# Day 4 — Scaling, Orchestration & Production Economics · Live Session Content

Full 6-hour delivery package for **Day 4** of the LVT AI-Assisted Development
Program (4 content days + a Day 5 Agentic Fest). Day 4 turns individual practice
into team infrastructure: reusable skills, deterministic hooks, orchestration
primitives, and a production cost model. The week's running build ships through the
full machinery, and teams get their sealed Day 5 brief.

Built to the `Live_Session_Deck_Skills.md` template (cream · navy #2C3F8E · cyan
#5BC4D2). Host: **Kyle Cheng** (MTS @ Anthropic).

## What's in here
```
Day 4/
├── day4-session-deck/index.html   ← the live session deck (30 slides, 5 parts)
├── lab-pack/
│   ├── bootcamp-repo/             ← the gated running build (post-Day-3; pytest → 7 passed)
│   │   ├── tools/code_graph.py    ← working AST context-graph demo (~92% reduction)
│   │   └── .claude/
│   │       ├── hooks/             ← format_on_edit, block_dangerous, secret_scan (all fire)
│   │       ├── skills/            ← repo-conventions (worked example) + owasp-review
│   │       └── agents/            ← researcher (delegation) + security-reviewer
│   ├── participant/               ← skill/hooks/subagent/tokenomics labs + cost model + routing
│   └── facilitator/               ← 5 keys incl. the SEALED Fest brief (Day 5 PRD)
├── INSTRUCTOR_RUNSHEET.md         ← minute-by-minute 6-hour guide
└── README.md
```

## Run the deck
Open `day4-session-deck/index.html`. `← →` navigate · `F` fullscreen · `.` notes · `?s=N` deep-link.

## Run the repo + tooling
```bash
cd lab-pack/bootcamp-repo
pip install -r requirements.txt
pytest -q                                  # 7 passed (the gated build)
python tools/code_graph.py cost get_note   # the tokenomics demo (~92% reduction)
echo '{"command":"rm -rf /"}' | bash .claude/hooks/block_dangerous.sh   # exit 2, blocked
```

## The five labs
| Part | Lab | Builds |
|------|-----|--------|
| 1 · Skills (60m) | write one skill, prove it triggers | a committed team skill |
| 2 · Hooks (55m) | wire two hooks, prove they fire | auto-format + dangerous-command guard |
| 3 · Orchestration (70m) | subagent delegation + heavyweight demos | a subagent pattern |
| 4 · Tokenomics (55m) | instrument, route, code-graph | a production cost model |
| 5 · Ship + Fest (60m) | ship through machinery, form teams | a gated build + the sealed Day 5 brief |

The repo is the **same running build** carried since Day 2, now post-Day-3 gated.
The Day 5 Fest brief ("share with an expiry") extends it, so every habit from Days
1–4 applies on capstone day.
