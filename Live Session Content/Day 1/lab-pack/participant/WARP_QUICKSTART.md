# Day 1 Quickstart — Running the Lab in Warp + Claude Code

Everything you need to go from a fresh machine to your first committed change,
using **Warp** as your terminal and **Claude Code** as the agent. Follow it top to
bottom. The spine of Day 1 is one loop: **prompt → read the diff → run tests →
commit.** Every step below serves that loop.

> Warp's own built-in AI ("Agent Mode") is a separate thing. Ignore it for the
> labs. Here you run Anthropic's **Claude Code CLI** *as a program inside* Warp.

---

## Step 0 — Copy the repo to a clean workspace

The course repo sits inside a folder that is already under git. Commit in place and
you tangle with it. Copy it out so your commits are clean and the course files stay
pristine.

```bash
cp -R "/Users/voldemort/Downloads/1. PowerUp/LVT/Live Session Content/Day 1/lab-pack/bootcamp-repo" ~/lvt-day1
cd ~/lvt-day1
git init && git add -A && git commit -m "baseline: notes-api day 1 start"
```

That baseline commit is your "before" point. Every AI change now shows up as a
reviewable diff against it.

---

## Step 1 — Install and launch Claude Code in Warp

```bash
# one-time install (needs Node 18+)
npm install -g @anthropic-ai/claude-code

# launch from inside the repo
cd ~/lvt-day1
claude            # first run walks you through login
```

Claude Code takes over the Warp pane as a full-screen app while it runs. That is
expected. When it proposes an edit or wants to run a command, you get a permission
prompt. **Read before you approve.** That habit is the whole point of Day 1. Quit
any time with `Ctrl+C`.

---

## Step 2 — Set up the environment and confirm the baseline

Run these in Warp (or ask Claude Code to run them and watch the output):

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest -q          # expect: 2 passed
ruff check .       # expect: All checks passed!
```

`2 passed` means the repo is healthy. The known 500 bug is intentional, not a
broken setup.

---

## Step 3 — See the bug with your own eyes (optional but worth it)

The endpoints need a valid token, and the server starts with an empty users table,
so seed one user first:

```bash
python3 -c "from notes_api import db; db.init_db(); c=db._connect(); c.execute(\"INSERT INTO users (email, token) VALUES ('me@lvt.test','tok_me')\"); c.commit(); c.close()"
python3 -m notes_api.app        # serves on http://localhost:5000
```

Open a second Warp tab (`Cmd+T`) and hit it:

```bash
# happy path → 201
curl -s -X POST localhost:5000/notes -H "Authorization: Bearer tok_me" \
  -H "Content-Type: application/json" -d '{"title":"hi","body":"there"}'

# missing body → 500 (the bug)
curl -s -i -X POST localhost:5000/notes -H "Authorization: Bearer tok_me" \
  -H "Content-Type: application/json" -d '{"title":"hi"}'
```

The second call returns a 500. That is `BACKLOG.md` item 1. Stop the server with
`Ctrl+C`.

---

## Step 4 — Drive your first change (the core lab)

Open `BACKLOG.md` and pick **item 1** (the 500 fix). In Claude Code, prompt it like
a good ticket (see `prompt-rewrites/PROMPT_ANATOMY.md` for the shape):

> In `notes_api/app.py`, `POST /notes` returns a 500 when the JSON body is missing
> `title` or `body`, because the handler indexes the dict directly. Fix it to
> return a clean `400` with a helpful message when either field is missing, while
> letting genuine errors surface. Reuse the existing response style
> (`jsonify(error=...)`). Add a test in `tests/test_notes.py` that posts a body
> missing `body` and asserts a `400`. Run `pytest -q` and `ruff check .` before
> showing me the diff.

Then work the four beats:

1. **Read the diff in the terminal.** Does it validate *before* the write? Does it
   return a real 400, or hide the error? (Drill diff 1 is the wrong way to do this,
   so you have a foil.)
2. **Run the gate yourself:** `pytest -q` and `ruff check .`. Green is necessary,
   not sufficient. Confirm the new test asserts the 400.
3. **Re-prompt if needed.** A reject costs one re-prompt. A bad accept costs an
   incident.
4. **Commit** when satisfied:
   ```bash
   git add -A && git commit -m "fix: POST /notes returns 400 on missing fields"
   ```

That commit is your Day 1 deliverable: one reviewed, tested change you drove end to
end.

---

## Step 5 — The diff-review drill (no agent)

Read `diff-review-drill/diff-1.md`, `diff-2.md`, `diff-3.md` in order. For each,
write your call (accept / reject / amend) and a one-line reason in
`diff-review-drill/REVIEW_CALLS.md`. Read the SQL in diff 2. Read what *runs* and
what the *test asserts* in diff 3. Commit to your call **before** you check the
facilitator key.

---

## The other three labs (no extra setup)

Same repo, same Claude Code session, fill in the worksheets:

| Lab | Open this | You produce |
|-----|-----------|-------------|
| Part 1 · Will it fail | `WILL_IT_FAIL_CARDS.md` | predictions, then run a few live to check |
| Part 3 · Context | `CONTEXT_AUDIT.md` | a bloated vs a fresh-session run of the same task, compared, plus your eviction rule |
| Part 4 · Prompting | `prompt-rewrites/WEAK_PROMPTS.md` + `PROMPT_PATTERN_LIBRARY_v0.md` | 3 rewritten prompts, one library entry |
| Part 5 · Responsible AI | `responsible-ai/PROMPTS_AND_TRANSCRIPTS.md` + `RESPONSIBLE_AI_CHECKLIST.md` | 5 flagged prompts, one safe rewrite |

For Part 3: do the "bloated" run in your current session, then type `/clear` in
Claude Code to start fresh for the "curated" run. Feeling that difference is the
highest-leverage habit of the day.

---

## Warp notes

- **No inline diff view.** Unlike the VS Code extension, Claude Code prints diffs
  in the Warp pane. For Day 1 that helps, since reading the diff in the terminal is
  exactly the muscle you are training.
- **Full-screen takeover is normal.** Warp detects the TUI and hands the pane over
  while `claude` runs. If the input box or keybindings ever feel off, `Ctrl+C` and
  relaunch.
- **Tabs and panes help.** Keep `claude` in one tab and a plain shell in another
  (`Cmd+T` for a tab, `Cmd+D` to split) so you can run `git`, `curl`, or `pytest`
  without leaving the agent.

---

## One-glance cheat sheet

```bash
# setup (once)
cp -R "/Users/voldemort/Downloads/1. PowerUp/LVT/Live Session Content/Day 1/lab-pack/bootcamp-repo" ~/lvt-day1
cd ~/lvt-day1 && git init && git add -A && git commit -m "baseline"
python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt

# the loop (every change)
claude                              # prompt it
#   → read the diff it prints
pytest -q && ruff check .           # run the gate
git add -A && git commit -m "..."   # commit when satisfied
```
