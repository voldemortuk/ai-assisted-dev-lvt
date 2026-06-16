# Executable Spec Template (reusable)

Point the agent at your existing PRD and tech spec, then add this thin layer on
top. The test of a good spec: the agent can be *tested against it*, and a defect
traces back to a line you can see.

```markdown
# Spec — <feature>

## Endpoints / interfaces
<method · path · auth · exact return shape, or function signatures>

## Acceptance criteria (each one is a test)
1. <a behaviour stated as a contract: given X, when Y, then Z>
2. ...
   # If you can't write it as a test, it isn't an acceptance criterion yet.

## Constraints
<what to reuse, what not to do, security/style rules the agent must follow>

## Non-goals
<what this explicitly does NOT do — closes the door on scope creep>

## Definition of done
<the gate: all AC tests pass, lint green, plus at least one human-authored
assertion on the critical path>
```

## The four silences to check before you call a spec done
- Does every "X works" criterion say what happens **after** (revoke → 404)?
- Is anything security-relevant (tokens, ownership) left **implicit**?
- Does "tests cover X" actually **assert the contract**, or just that it ran?
- Are the **non-goals** written down, so the agent doesn't gold-plate?

> The chain: **spec → plan → implement → verify.** When the build is wrong, walk
> it back up the chain. Most defects trace to a spec gap, not agent mystery.
