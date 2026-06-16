# Subagent Lab — delegate a research task (Part 3)

Subagents are the workhorse orchestration primitive. A subagent has its **own
context window** and **scoped tools**, does a job, and reports back, keeping your
main session clean.

## The organizing questions (apply to any primitive)
- **Who decides what runs next?** (you, a lead agent, or a script)
- **Where do intermediate results live?** (in your context, or out in a subagent's)

| Primitive | Who decides | Results live | Cost | Today |
|-----------|-------------|--------------|------|-------|
| **Subagent** | you | in the subagent, summary back | modest | **hands-on** |
| **Agent team** (experimental) | a lead + peers, shared task list + mailbox | across peers | heavy | demo |
| **Dynamic workflow** (research preview) | an orchestration script | in background subagents, only final answer returns | very heavy | demo |

## The lab — delegate with a scoped tool set and a structured report-back
Use the provided `researcher` subagent (`.claude/agents/researcher.md`). It's
read-only and reports in a fixed format. Delegate a real question from the running
build, for example:

> "Using the researcher subagent: what depends on `db.get_note`, and is anything
> reaching it without an ownership check?"

The subagent should use `tools/code_graph.py whodepends get_note`, cite `file:line`,
and report back in its `FINDING / EVIDENCE / DEPENDENTS / RISKS` format, without
dumping its whole search into your context.

## Why this is the workhorse
The research happened in the subagent's window. Your main context stays clean and
focused on the build. You can also choose a cheaper model per subagent (see the
tokenomics lab). That's the everyday pattern; agent teams and dynamic workflows are
the heavyweight options you saw demoed, for when the job justifies the cost.

**Deliverable:** a subagent delegation with a scoped tool set and a structured
report-back you'd reuse on real tasks.
