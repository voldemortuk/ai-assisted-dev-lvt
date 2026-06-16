# notes-api (bootcamp repo) — Day 4 state

The running build after it passed the Day 3 trust gates: the share feature is
secure (parameterised SQL, unguessable tokens, owner-only mint/revoke, working
revocation), with contract-asserting tests. Day 4 wraps team infrastructure around
it: skills, hooks, a subagent, and a cost model.

## Run it
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest -q          # 7 passed (incl. the human-authored revoke assertion)
ruff check .
python -m notes_api.app
```

## Day 4 tooling
```bash
python tools/code_graph.py build                 # the AST context graph
python tools/code_graph.py whodepends get_note   # dependents, no whole-file reads
python tools/code_graph.py cost get_note         # subgraph tokens vs whole-file tokens
```

## What's committed in `.claude/`
- `settings.json` — permissions baseline + three hooks
- `hooks/` — `format_on_edit.sh` (PostToolUse auto-format), `block_dangerous.sh`
  (PreToolUse guard), `secret_scan.sh` (carried from Day 3)
- `skills/` — `repo-conventions` (the worked-example skill) + `owasp-review`
- `agents/` — `researcher` (scoped delegation) + `security-reviewer`

Test the hooks:
```bash
echo '{"command":"rm -rf /"}'             | bash .claude/hooks/block_dangerous.sh   # exit 2, blocked
echo '{"file_path":"notes_api/share.py"}' | bash .claude/hooks/format_on_edit.sh    # formats
```
