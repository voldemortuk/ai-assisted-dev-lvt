# Prompt Pattern Library v0 (team artifact)

The seed of a shared asset. Each engineer contributes **one tested prompt** with a
note on when to reach for it. This grows through the week and becomes the basis for
the team skills work on Day 4.

## How to contribute
Add an entry below. Keep it to a prompt that actually worked, on a real task, with
a one-line trigger for when to use it.

```markdown
### <short name>
**When to reach for it:** <the situation this fits>
**The prompt:**
> <the prompt text, with placeholders in <angle brackets>>
**Notes:** <what it produces, any gotcha>
```

---

## Example entry (provided to seed the format)

### Bug-fix with a reproduction and a test
**When to reach for it:** a small, well-defined bug where you can state the bad
input and the right behaviour.
**The prompt:**
> In `<file>`, `<endpoint/function>` does `<wrong behaviour>` when `<input>`.
> Fix it so it `<right behaviour>`. Reuse `<existing pattern>`. Add a test in
> `tests/<file>` that asserts the new behaviour on `<the failing input>`.
> Run `pytest -q` and `ruff check .` before showing me the diff.
**Notes:** the explicit reproduction and the "add a test that asserts X" are what
keep the agent from declaring victory without covering the case.

---

## Team entries
*(add yours below)*
