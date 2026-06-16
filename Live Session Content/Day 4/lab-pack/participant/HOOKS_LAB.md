# Hooks Lab — two deterministic guardrails (Part 2)

Hooks fire on lifecycle events and **guarantee** something happens, rather than
hoping the model chooses to. Add two to the repo and prove both fire.

## Hook anatomy
- A hook is a **shell command, a prompt, or an agent**, fired on a lifecycle event.
- **PreToolUse** runs *before* an action. A blocking exit code (2) stops the agent.
- **PostToolUse** runs *after* an action: format, lint, test, log.
- Committed to `settings.json`, the whole team inherits the same gates.

## The two hooks (templates provided in `.claude/hooks/`)
1. **Auto-format on edit** (`format_on_edit.sh`, PostToolUse on `Write|Edit`):
   formats every Python file the agent touches, so house style is guaranteed.
2. **Block a dangerous command** (`block_dangerous.sh`, PreToolUse on `Bash`):
   refuses `rm -rf /`, `curl … | sh`, force-pushes, and similar, with a blocking
   exit code.

## Steps
1. Read both hook scripts and the wiring in `.claude/settings.json`.
2. **Prove the guard fires:**
   ```bash
   echo '{"command":"rm -rf /"}' | bash .claude/hooks/block_dangerous.sh ; echo "exit=$?"
   ```
   Expect the block message and `exit=2`. Try a safe command and confirm `exit=0`.
3. **Prove the formatter fires:** make a deliberately badly-formatted edit, then
   confirm `format_on_edit.sh` tidies it (or run it directly with a `file_path`).
4. **Commit** the settings so the team inherits both gates.

## The connection backward
Hooks are the deterministic enforcement layer behind Day 3's self-verifying loop,
the secret scan, and the Day 1 responsible-AI checklist. What was "the model
hopefully runs the tests" becomes "the tests run, guaranteed."

## What belongs in a hook vs model judgment
- **Hook:** anything that must *always* happen and can be checked mechanically
  (format, secret scan, block a destructive command).
- **Model judgment:** anything needing reasoning (is this design right? is this the
  correct fix?). Don't try to encode judgment in a hook.

**Deliverable:** two working hooks the team inherits, both proven to fire.
