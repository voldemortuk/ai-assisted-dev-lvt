# Context Audit + Eviction Rule (Part 3)

The context window is the agent's entire working memory. What's in it competes for
space, and crowding degrades output. This worksheet makes your own context visible
and gives you a rule you'll reuse on real repos.

## The centerpiece lab — bloated vs curated
1. **Bloated run:** take a backlog task and deliberately pollute the session
   first: read five unrelated files, paste a long log, ask two off-topic
   questions, then ask for the change. Save the diff. Watch it drift or stall.
2. **Curated run:** start a **fresh session**. Reference only the files the task
   needs, point the agent at the interface (not the whole implementation), and
   ask for the same change. Save the diff.
3. **Compare** the two diffs side by side. The difference is the lesson.

## Mid-session audit — what is my session actually carrying?
List what's occupying context right now and rank by cost:

| Item in context | Roughly how big | Still needed? |
|-----------------|-----------------|---------------|
| project memory (CLAUDE.md) | | |
| files I've read | | |
| tool output / logs | | |
| conversation history | | |
| exploration that's now done | | |

## Your personal eviction rule (write it, keep it)
> "I clear/compact when ______, and I never let ______ stay in a build session."

Examples to adapt: *"I start a fresh session per task"* · *"I evict exploration
reads once I start building"* · *"I compact when the agent repeats itself or drifts
off the task."*

## Reset discipline
- **Clear** vs **compact:** clear when the task changes; compact when the thread is
  long but still relevant.
- **Signs of a poisoned context:** the agent repeats itself, re-asks what you told
  it, edits the wrong file, or drifts. When you see them, a fresh session usually
  beats persisting. Day 4 prices this habit in tokens.
