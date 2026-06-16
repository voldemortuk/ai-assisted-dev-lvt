# FACILITATOR — Part 1 Skills Key

## What a good skill looks like
Point at `.claude/skills/repo-conventions/SKILL.md` as the model. Call out:
- The **description** names concrete trigger situations ("any edit to notes_api/ or
  tests/, or when adding an endpoint, query, or data access"). That's what makes it
  fire reliably.
- The instructions are **behaviour-changing**, not prose. Parameterised SQL, the
  ownership accessor, secrets from env. Each line would change a diff.
- It's **short**. Progressive disclosure means it can afford detail, but it still
  doesn't pad.

## Testing that it triggers (the step people skip)
Make them prove both directions:
- A task that **should** fire it ("add a `GET /notes` list endpoint") — confirm the
  conventions get applied.
- A task that **shouldn't** ("update the README") — confirm it stays quiet.
A skill that fires on everything is as broken as one that never fires.

## Common failure modes in their drafts
- Description too vague ("helps with code") → never triggers predictably.
- Restating the README → context clutter, no behaviour change.
- Trying to encode judgment ("write good code") → that's not what a skill is for.

## The bridge
Capturing what worked into skills is the same instinct as the Day 1 Prompt Pattern
Library, now made first-class and committed. Distribution: commit to `.claude/skills/`
so the team inherits it; keep a polyrepo coherent by committing the same skill, not
copy-pasting prose.
