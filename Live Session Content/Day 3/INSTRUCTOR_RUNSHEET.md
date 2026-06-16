# Day 3 — The Trust Triad · Instructor Runsheet (6 hours)

Host: **Kyle Cheng** · Programme: LVT AI-Assisted Development · Deck: `day3-session-deck/index.html`

The day runs on **one diff**: the Day 2 "share a note via a public link" feature in
`lab-pack/bootcamp-repo/`. It is tidy, idiomatic, and all-green — and carries every
planted problem. Keep the facilitator answer keys closed until each debrief.

**Timing model:** 360 minutes wall-clock = **300 focused minutes** + 2 breaks (15+15) +
buffer. Adjust live; the labs are the load-bearing part, not the slides.

---

## Block-by-block

| Time | Block | Deck slides | Lab pack |
|------|-------|-------------|----------|
| 0:00–0:15 | **Open** — cover, Kyle intro, day map, through-line, warm-up, house rules | 1–6 | — |
| 0:15–1:25 | **Part 1 · Anti-Slop** (70m) | 7–13 | — |
| 0:15–0:55 | ↳ teach: tidy≠correct, four faces of slop, untrusted-by-default, self-verifying loop, scaffolding→gate | 8–12 | — |
| 0:55–1:25 | ↳ **Lab 1 · Slop Hunt** (30m) | 13 | `participant/REVIEW_CHECKLIST.md` · key: `facilitator/PART1_SLOP_ANSWER_KEY.md` |
| 1:25–1:40 | **Break** | — | — |
| 1:40–3:10 | **Part 2 · Multi-Hat** (90m) | 14–19 | — |
| 1:40–2:25 | ↳ teach: why one reviewer fails, the panel, black-box independence, the hard line | 15–18 | — |
| 2:25–3:10 | ↳ **Lab 2 · Multi-Hat Panel** (45m) | 19 | `participant/multi-hat/*` · key: `facilitator/PART2_PANEL_EXPECTED_FINDINGS.md` |
| 3:10–4:40 | **Part 3 · Security/OWASP** (90m) | 20–25 | — |
| 3:10–3:55 | ↳ teach: security lens, OWASP skill, project scope + subagent, marketplace as attack surface | 21–24 | — |
| 3:55–4:40 | ↳ **Lab 3 · Shift-Left** (45m) | 25 | `bootcamp-repo/.claude/*` · `participant/TRIAGE_TEMPLATE.md` · key: `facilitator/PART3_VULN_ANSWER_KEY.md` |
| 4:40–4:55 | **Break** | — | — |
| 4:55–5:35 | **Part 4 · Permissions** (40m) | 26–29 | — |
| 4:55–5:10 | ↳ teach: allow/ask/deny, auto mode | 27–28 | — |
| 5:10–5:35 | ↳ **Lab 4 · Baseline + Debate** (25m) | 29 | `participant/PERMISSIONS_DEBATE.md` · key: `facilitator/PART4_CONTESTED_RULES.md` |
| 5:35–5:45 | **Wrap** — gate status + reflection + Day 4 bridge | 30–31 | — |

---

## What every engineer leaves with (the checklist to enforce at the wrap)
- [ ] A scored slop review (___/4) and a self-verifying loop in `CLAUDE.md`
- [ ] Panel-vs-single evidence + **one human-authored assertion** committed on the critical path
- [ ] A project-scoped OWASP skill, a triaged finding, an installed secret-scan hook
- [ ] A committed permissions baseline with the contested rule's reasoning recorded
- [ ] A running build that passed the gates — or has its findings logged

## The four money moments (don't let these slip)
1. **Part 1:** show `pytest` → *5 passed*, then ask "so is revoke tested?" The green suite is covering air.
2. **Part 2:** the black-box hat proves the revoke bug from the **contract alone**; the human-authored assertion **fails** when committed — that failure is the lesson.
3. **Part 3:** run `bash .claude/hooks/secret_scan.sh` live → it exits **2** and names the two planted secrets.
4. **Part 4:** force a decision on **one** contested rule and capture the **dissent** in the commit message.

## Pre-flight (the night before)
- `cd lab-pack/bootcamp-repo && pip install -r requirements.txt && pytest -q` → 5 passed.
- `bash .claude/hooks/secret_scan.sh` → exits 2, flags `db.py:17` + `share.py:13`.
- Open `day3-session-deck/index.html`, press `.` to confirm notes, walk all 31 slides, check print preview.
- Skim all four `facilitator/` keys so the planted issues are at your fingertips.
