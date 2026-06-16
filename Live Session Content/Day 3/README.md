# Day 3 — The Trust Triad · Live Session Content

Full 6-hour delivery package for **Day 3** of the LVT AI-Assisted Development
Program (4 content days + a Day 5 Agentic Fest capstone). Day 3 is the heart of
the programme: AI-written code ships only through gates the team trusts —
calibrated anti-slop review, adversarial multi-hat panels, secure-by-default OWASP
tooling, and a committed permissions posture.

Built to the `Live_Session_Deck_Skills.md` template (cream bg · navy #2C3F8E ·
cyan #5BC4D2). Host: **Kyle Cheng** (MTS @ Anthropic).

## The through-line
Everything runs on **one diff**: the Day 2 "share a note via a public link"
feature. It is tidy, idiomatic, and all-green — and carries every planted problem.
The same diff passes through four gates, each seeing what the others can't.

## What's in here

```
Day 3/
├── day3-session-deck/index.html   ← the live session deck (31 slides, keyboard-driven)
├── lab-pack/
│   ├── bootcamp-repo/             ← the running build under review (runs: pytest → 5 passed)
│   ├── participant/               ← checklists, hat prompts, triage + debate worksheets
│   └── facilitator/               ← answer keys for all 4 planted-issue labs (keep closed)
├── INSTRUCTOR_RUNSHEET.md         ← minute-by-minute 6-hour facilitation guide
└── README.md                      ← this file
```

## Run the deck
Open `day3-session-deck/index.html` in any modern browser. No build step.
`← →` navigate · `F` fullscreen · `.` speaker notes · `?s=N` deep-links to slide N.

## Run the labs
```bash
cd lab-pack/bootcamp-repo
pip install -r requirements.txt
pytest -q                       # 5 passed — green is not the same as covered
bash .claude/hooks/secret_scan.sh   # exits 2, flags the two planted secrets
```

## The four labs and what they prove
| Part | Lab | Planted issue it surfaces | Deliverable |
|------|-----|---------------------------|-------------|
| 1 · Anti-Slop (70m) | Slop Hunt | 4 slop problems (wrong helper, copy-paste drift, dead branch, empty test) | scored review + self-verifying loop |
| 2 · Multi-Hat (90m) | Panel vs single | revoke bug provable from the contract alone | panel-vs-single evidence + 1 human assertion |
| 3 · Security (90m) | Shift-left | SQLi, broken access control, hardcoded secrets | OWASP setup + secret-scan hook + triaged finding |
| 4 · Permissions (40m) | Baseline + debate | — (posture exercise) | committed permissions baseline |

See `INSTRUCTOR_RUNSHEET.md` for timings and the four "money moments", and the
`facilitator/` keys for exact file:line of every planted issue.
