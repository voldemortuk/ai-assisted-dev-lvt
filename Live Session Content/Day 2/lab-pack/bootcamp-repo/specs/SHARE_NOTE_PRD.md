# PRD — Share a note via a public link

**Author:** Product (LVT)  ·  **Status:** ready for build  ·  **Size:** small feature

## Problem
Users want to send a note to someone who doesn't have an account. Today the only
way is to copy-paste the text into email. We want a shareable link.

## What we want
A signed-in user can turn one of their notes into a public link. Anyone who has
the link can open the note in a browser and read it, without signing in. The user
can turn a link off again when they no longer want it shared.

## Rough shape
- A "Share" action on a note that returns a URL.
- Opening the URL shows the note's title and body.
- A "Revoke" action that turns a link off.

## Out of scope (for now)
- Editing a note through the link (read-only).
- Expiry dates, passwords on links, view counts.
- Sharing whole folders.

---

> **NOTE FOR THE SPEC AUTHOR (Day 2 · Part 3).** A PRD describes intent in
> product language. It is deliberately loose. Your job is to turn it into an
> *executable* spec: acceptance criteria the agent can be tested against,
> constraints, non-goals, and a definition of done. Where this PRD is vague is
> exactly where build defects will appear if you leave it vague. Read it twice
> and notice what it does **not** pin down.
