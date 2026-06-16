# Permissions Baseline + Debate (Part 4)

Goal: leave with a `.claude/settings.json` posture the team would actually trust on
a real LVT repo, and the reasoning recorded for the rules people argued about.

## Step 1 — three buckets
Sort the agent's common actions into:

| Bucket | Meaning | Examples on this repo |
|---|---|---|
| **allow** | run without asking | read files, `pytest`, `ruff`, `git diff`, `git status` |
| **ask** | prompt every time | `git commit`, `git push`, `pip install`, `gh` |
| **deny** | never, no prompt | `rm -rf`, `curl … \| sh`, reading `.env`/keys, raw web fetch |

Start from the committed baseline in `.claude/settings.json` and adjust it to what
*your* team would sign.

## Step 2 — auto mode (decide as a team)
Auto mode replaces manual prompts with a background classifier that decides allow
vs ask for you.
- **Upside:** flow — far fewer interruptions on routine work.
- **Risk:** the classifier can misjudge; you've moved a human gate to a model gate.
- **Position to reach:** on this repo, do we enable it? With what `deny` floor
  underneath it as a hard backstop? Write the team's answer here: ______________

## Step 3 — the contested rule (debate to a position)
Pick **one** rule the room disagrees on and argue it to a decision. Suggested
flashpoints:
- Should `git commit` be **allow** or **ask**? (Flow vs. a human seeing the diff.)
- Should `pip install` ever be **allow**? (Supply-chain risk vs. friction.)
- Should `Bash(git push)` ever be allowed without a prompt?

**Rule debated:** ______________
**Position reached:** allow / ask / deny because ______________
**Dissent (record it):** ______________

## Step 4 — commit it
The whole team inherits this file. A permissions posture that lives on one laptop
isn't a posture. Commit `.claude/settings.json` with the contested rule's reasoning
in the commit message.
