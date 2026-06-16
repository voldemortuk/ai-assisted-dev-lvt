# FACILITATOR — Part 3 Context-Engineering Key

## The centerpiece (bloated vs curated)
Set up the **bloated** run deliberately: have engineers read several unrelated
files, paste a long log, ask a couple of off-topic questions, then ask for a
backlog change. Expected behaviour: the agent drifts, references the wrong file,
re-asks things, or produces a sprawling diff. Then the **curated** run in a fresh
session, referencing only the needed files and pointing at interfaces: tighter,
correct, faster.

What you want them to *feel*: same task, same model, same prompt for the change,
and the only variable was what else was in the window. The curated run wins. That
delta is the highest-leverage habit in AI-assisted development, and they produced
it on their own session.

## Common diagnoses when pairs swap failing transcripts
- Exploration reads never evicted, now crowding the build.
- A long log or stack trace eating the window.
- Conversation history carrying a abandoned earlier approach the agent keeps
  re-attempting.
- Too many files referenced, so the relevant one gets diluted.

## The eviction rule
There's no single correct rule. Good ones are specific and personal: "fresh session
per task", "evict exploration reads before building", "compact when the agent
repeats itself". The deliverable is that each engineer leaves with a rule written
down they'll reuse on their own repos.

## The bridge
Name it explicitly: this is a quality habit today; on Day 4 it becomes a **cost**
lever, because everything in context is paid for on every turn.
