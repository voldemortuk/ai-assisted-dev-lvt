# Day 4 — Scaling, Orchestration & Production Economics · Instructor Runsheet (6 hours)

Host: **Kyle Cheng** · Programme: LVT AI-Assisted Development · Deck: `day4-session-deck/index.html`

Day 4 turns individual practice into team infrastructure: skills, hooks,
delegation, and a cost model. The week's running build ships through the full
machinery, then teams get their sealed Day 5 Fest brief.

**Timing model:** 360 min wall-clock = 300 focused min + 2 breaks + buffer.

---

## Block-by-block

| Time | Block | Deck | Lab pack |
|------|-------|------|----------|
| 0:00–0:15 | **Open** — cover, Kyle, day map, through-line, warm-up, house rules | 1–6 | — |
| 0:15–1:15 | **Part 1 · Skills** (60m): what good looks like, lifecycle, marketplace | 7–9 | — |
| 0:40–1:15 | ↳ **Lab 1** (35m): write one skill, prove it triggers, commit | 10 | `participant/SKILL_LAB.md` · `.claude/skills/repo-conventions/` · key: `facilitator/PART1_SKILLS_KEY.md` |
| 1:15–1:30 | **Break** | — | — |
| 1:30–2:25 | **Part 2 · Hooks** (55m): anatomy, the two hooks, hook-vs-judgment | 12–14 | — |
| 2:00–2:25 | ↳ **Lab 2** (25m): wire two hooks, prove both fire, commit | 15 | `participant/HOOKS_LAB.md` · `.claude/hooks/` · key: `facilitator/PART2_HOOKS_KEY.md` |
| 2:25–3:35 | **Part 3 · Orchestration** (70m): four primitives, the workhorse | 17–18 | — |
| 2:55–3:35 | ↳ **Lab 3** (40m): subagent delegation + the two heavyweight demos | 19 | `participant/SUBAGENT_LAB.md` · `.claude/agents/researcher.md` · key: `facilitator/PART3_ORCHESTRATION_KEY.md` |
| 3:35–3:50 | **Break** | — | — |
| 3:50–4:45 | **Part 4 · Tokenomics** (55m): where spend goes, routing, context graph | 21–23 | — |
| 4:15–4:45 | ↳ **Lab 4** (30m): instrument, route, code-graph cost, fill the model | 24 | `participant/TOKENOMICS_LAB.md` · `COST_MODEL.md` · `tools/code_graph.py` · key: `facilitator/PART4_TOKENOMICS_KEY.md` |
| 4:45–5:45 | **Part 5 · Ship + Fest** (60m): ship through machinery, form teams, sealed brief | 26–27 | `facilitator/PART5_FEST_BRIEF.md` |
| 5:45–5:55 | **Wrap** — recap + reflection + Day 5 bridge | 28–29 | — |

---

## The token-heavy demos (Part 3) — run instructor-side
- **Agent team** multi-hat review on one diff (the mechanized Day 3 panel). Token cost on screen, stability caveat stated.
- **Dynamic workflow** research run: **run once**, instructor-side, very token-heavy, cost on screen.
Nothing in the standard workflow depends on these yet — they're demoed, not adopted.

## What every engineer leaves with
- [ ] One committed team skill, proven to trigger
- [ ] Two working hooks the team inherits (auto-format + dangerous-command guard)
- [ ] A subagent delegation pattern + an informed take on teams/workflows
- [ ] A production cost model with routing rules and context-graph pilot criteria
- [ ] The running build shipped through the full machinery + a sealed Fest brief

## Pre-flight
- `cd lab-pack/bootcamp-repo && pip install -r requirements.txt && pytest -q` → 7 passed (the gated build).
- `ruff check .` → clean.
- Hooks: `echo '{"command":"rm -rf /"}' | bash .claude/hooks/block_dangerous.sh` → exit 2;
  `echo '{"file_path":"notes_api/share.py"}' | bash .claude/hooks/format_on_edit.sh` → formats.
- `python tools/code_graph.py cost get_note` → shows the ~92% reduction demo.
- Open `day4-session-deck/index.html`, press `.` for notes, walk all 30 slides.
- Keep `facilitator/PART5_FEST_BRIEF.md` sealed until teams form.
