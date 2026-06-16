# Sizing Rubric (keep this — it leaves with the team)

Match the approach to the task. Score three signals, then read the row.

| Signal | Ask |
|--------|-----|
| **Blast radius** | If this is wrong, how much breaks? One string, or auth for everyone? |
| **Ambiguity** | Is "done" obvious, or does it need a contract written first? |
| **Reviewability** | Can you check the result in seconds, or only by reading every line? |

## The approaches

| Approach | Reach for it when | Example |
|----------|-------------------|---------|
| **Quick** (interactive, no plan) | Low blast radius, low ambiguity, high reviewability | typo, version bump, a one-endpoint add |
| **Plan mode** | Real blast radius OR ambiguity; you want to catch mistakes before code | a cross-file rename, pagination, a refactor |
| **Spec-driven** | Multi-step, the contract matters, it becomes a running artifact | the share feature, a new auth flow |
| **No agent** | Novel architecture, a judgment call, or a decision not a change | "should we move to Postgres?", a one-character call you'd agonise over |

## The cost of getting it wrong
- Too small an approach on a big task → drift, rework, review fatigue.
- Too big an approach on a small task → ceremony that wastes everyone's time.
- The skill is not "always plan" or "always spec". It's reading the three signals
  and stopping at the cheapest approach that's safe.
