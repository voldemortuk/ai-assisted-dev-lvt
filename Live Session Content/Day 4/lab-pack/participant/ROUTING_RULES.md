# Model Routing Rules (team artifact)

Write down which work goes to which model tier, and the quality gate that keeps
routing honest. Routing that silently degrades output is worse than no routing.

| Work type | Tier | Why |
|-----------|------|-----|
| Planning & spec review | **Frontier** | Judgment-heavy; mistakes here compound downstream |
| Adversarial / security review | **Frontier** | Worst place to cut corners |
| Mechanical edits (rename, format, boilerplate) | **Fast / cheap** | Low ambiguity, easy to verify |
| Subagent research / delegation | **Fast / cheap** | Scoped, report-back is checkable |
| <your workflow> | | |

## The non-negotiable
Every routed path runs through a **quality gate** (tests, the Day 3 review panel,
first-pass success rate). If a cheaper tier starts failing the gate, route it back
up. The gate is what makes routing a saving instead of a silent regression.

## Our rule (write it)
> "We route ______ to the fast tier and ______ to the frontier tier, and we revert
> any path that drops below ______ on ______ (the gate)."
