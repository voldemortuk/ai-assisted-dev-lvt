# Skills Lab — write one small skill (Part 1)

Write one genuinely useful skill for this repo and prove it triggers on the right
tasks. Model it on the worked example at `.claude/skills/repo-conventions/SKILL.md`.

## What makes a skill good
- **A description that triggers reliably.** It names the situations the skill
  applies to, in the words a real task would use. Too vague and it never fires;
  too broad and it fires on everything.
- **Progressive disclosure.** The skill loads only when relevant, so it can carry
  detail without taxing every session.
- **Instructions that earn their context cost.** Every line changes behaviour. No
  essays, no restating the README.

## Candidates (pick one)
- The **Day 1 prompt patterns** (turn a Pattern Library entry into a triggering skill)
- The **Day 2 spec template** (a skill that produces an executable spec from a PRD)
- The **Day 3 review checklist** (a skill that runs the slop/anti-slop checklist on a diff)

## Steps
1. Draft `SKILL.md` with frontmatter (`name`, `description`) and tight instructions.
2. **Test that it triggers.** Give the agent a task that should fire it and confirm
   it does; give one that shouldn't and confirm it stays quiet.
3. **Trim.** Cut any instruction that doesn't change behaviour.
4. **Commit** it to `.claude/skills/` so the whole team inherits it.

## The lifecycle (keep it in mind)
Draft → test it triggers → trim → retire when stale. A skill that doesn't trigger is
worse than none: it's context clutter pretending to be help.

## Marketplace note (Day 3's rule, applied)
Adopting a community skill or plugin is a **security decision**: it runs with the
agent's privileges. Prefer reputable sources, read it before installing, pin
versions, and treat adoption as its own review.

**Deliverable:** one committed skill, proven to trigger on the right tasks and stay
quiet on the wrong ones.
