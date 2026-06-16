# FACILITATOR — Part 3 Orchestration Key

## The hands-on part (subagents)
Everyone delegates a research task to the `researcher` subagent. The good outcome:
the investigation happens in the subagent's own context, and only a short structured
report comes back, so the main session stays clean. Have them run something real:
> "Using the researcher subagent: what depends on `db.get_note`?"
Expected: it uses `tools/code_graph.py whodepends get_note`, finds
`get_note_for_owner` and `resolve_share` as direct callers, and reports in the fixed
format. Land the point: this is the **workhorse**, the everyday primitive.

## The two organizing questions (use these to compare all four)
- **Who decides what runs next?** you / a lead / a script.
- **Where do intermediate results live?** your context / a subagent / background.

| Primitive | Who decides | Results | Cost | Status |
|-----------|-------------|---------|------|--------|
| Subagent | you | summary back to you | modest | standard, daily |
| Agent team | lead + peers, shared list + mailbox | across peers | heavy | experimental |
| Dynamic workflow | orchestration script | background, only final returns | very heavy | research preview |

## The live demos (instructor-side, honest caveats)
1. **Agent team** running a multi-hat review on one diff — the mechanized form of
   Day 3's manual panel. State the version/stability caveat; it's token-heavy.
2. **Dynamic workflow** running parallel subagents in the background with only the
   final verified answer returning. **Run this once**, instructor-side, with token
   cost on screen — it's deliberately expensive.

## Honest framing (do not skip)
Nothing in the team's standard workflow depends on the experimental primitives yet.
They're demoed so engineers know they exist and roughly what they cost, not adopted.
The escalation ladder to draw on the board: **interactive session → subagent → team
→ workflow**, climbing only when the job justifies the cost.
