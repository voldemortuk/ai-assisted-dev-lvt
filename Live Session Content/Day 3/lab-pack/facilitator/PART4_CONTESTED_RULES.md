# FACILITATOR — Part 4 Permissions Debate Guide

Objective: the room leaves with a committed `.claude/settings.json` posture and the
reasoning recorded for the rules people argued about. There's no single right
answer — the deliverable is a *defended* position the team would actually trust.

## The committed baseline (in `.claude/settings.json`)
- **allow:** Read/Edit/Write, `pytest`, `ruff`, `python`, read-only git, `ls/cat/grep/rg`
- **ask:** `git commit`, `git push`, `pip install`, `gh`
- **deny:** read `.env`/keys/`*.pem`, `rm -rf`, `curl … | sh|bash`, `WebFetch`

Frame this as a *starting* posture, not gospel. Have them change at least one rule.

## Flashpoints to steer the debate toward

**1. `git commit` — allow or ask?**
- *Allow* argument: flow; the diff was already reviewed; the secret-scan hook gates it anyway.
- *Ask* argument: a human should see what's being committed; hooks can be bypassed/misconfigured.
- Good landing: **ask** while trust is being built; revisit once hooks are mature (Day 4).

**2. `pip install` — ever allow?**
- Supply-chain risk (typosquats, post-install scripts) vs. friction.
- Good landing: **ask**, never allow; deny in CI contexts.

**3. Auto mode — enable it?**
- A background classifier replaces manual allow/ask prompts.
- Upside: flow. Risk: you've swapped a human gate for a model gate; misclassification
  is now silent.
- Good landing: only with a **hard `deny` floor** underneath as a non-negotiable
  backstop; enable per-repo, not globally; revisit after the team has lived with the
  baseline.

**4. `WebFetch` / raw web access**
- Prompt-injection surface (instructions hiding in fetched content). Day 1 covered
  this. Default **deny** on a repo handling real code is defensible.

## Facilitation
- Force a decision on **one** contested rule; capture the dissent in the commit
  message, not just the winning side.
- The win condition isn't consensus — it's a posture everyone will inherit and that
  the dissenters can live with. Commit `settings.json`; a posture on one laptop is no
  posture.
