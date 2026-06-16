# Diff-Review Drill — your calls (Part 2)

Three AI-authored diffs, increasing in subtlety. For each, decide **accept**,
**reject**, or **amend**, and defend the call to your pair. This is the habit Day
3 turns into a full review system.

| Diff | Call | One-line reason | If amend: the fix |
|------|------|-----------------|-------------------|
| 1 · the 500 fix | | | |
| 2 · `GET /notes` | | | |
| 3 · title limit | | | |

## What to check, in order
1. **What does it actually do?** Read the behaviour, not the intent. Run it in
   your head on the failing input.
2. **What does tidy formatting hide?** Clean code earns more scrutiny, not less.
3. **Does the test assert the contract,** or just that the call returned something?
4. **When in doubt, reject and ask.** A reject costs a re-prompt. A bad accept
   costs an incident.

The further down the list you go, the more these diffs reward reading what runs
over reading what's written. Hold that instinct. Day 3 is built on it.
