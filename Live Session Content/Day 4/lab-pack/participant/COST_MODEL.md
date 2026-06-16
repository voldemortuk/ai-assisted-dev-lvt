# Production Cost Model (worksheet)

Fill this in for one realistic LVT workflow. The goal is a model you could take to a
budget conversation, with levers you can actually pull.

## Cost per task
| Component | Tokens (rough) | Notes |
|-----------|----------------|-------|
| Session setup (system + CLAUDE.md) | | fixed per session |
| File reads | | the biggest variable; curate it |
| Tool output (tests, logs) | | trim noisy output |
| Generation (the diff) | | |
| Retries / re-rolls | | the silent killer |
| **Total per task** | | |

## Cost per outcome (the number that matters)
> cost-per-outcome = cost-per-task × (passes to ship)

The cheapest session ships on the **first pass**. A task that costs 2× per attempt
but ships first-try beats a cheap task that takes four re-rolls.

## The levers (rank them for your team)
- [ ] **First-pass success** — good spec, clean context, worked examples
- [ ] **Model routing** — frontier for planning/review, fast for mechanical/subagents
- [ ] **Context curation** — interfaces over implementations, evict exploration
- [ ] **Prompt caching** — reuse stable context across turns
- [ ] **Context graph** — retrieve subgraphs, not whole files (pilot first)

## Budget guardrails
- Per-team attribution so the bill is visible and governable.
- A budget ceiling per workflow, alerting before it's blown.

## Context-graph pilot criteria (decide before adopting)
- **Cost threshold:** adopt only if it cuts tokens by ≥ ___% on our repos.
- **Quality threshold:** reject if retrieval misses structure and quality drops on
  ___ (name the check: test pass rate, review findings, first-pass success).
