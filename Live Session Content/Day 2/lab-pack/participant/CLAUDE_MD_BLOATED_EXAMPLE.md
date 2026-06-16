# Bloated CLAUDE.md — what NOT to ship (critique this)

This is a real-shape example of a CLAUDE.md that costs context on every turn and
buys almost nothing. Use it in the trim pass: mark every line that doesn't earn
its keep. Most of this file is fat.

---

```markdown
# Welcome to the Notes API Project!

This project is a really exciting Flask application that we have been building as
part of our journey into modern software engineering. The team has worked very
hard on it and we are proud of what we have accomplished together over the past
several sprints. Our mission is to build delightful software that our users love.

## A Brief History of This Codebase
Originally this started as a hackathon project back in the early days. Over time
it grew into the service you see today. There were many learnings along the way.

## Our Engineering Philosophy
We believe in clean code, in writing tests, in being good teammates, and in
continuous improvement. Quality is everyone's responsibility. We value simplicity.

## Tech Stack
This project uses Python. Python is a popular programming language. We use Flask,
which is a web framework. We also use SQLite for the database and pytest for tests.

## How the Code is Organised
There is a folder called notes_api. Inside it there are some Python files. There
is also a tests folder. The files contain functions. The functions do things.

## Coding Standards
Please write good code. Use meaningful variable names. Don't write bugs. Make sure
to test your code thoroughly before committing. Follow PEP 8 where reasonable.

## Deprecated Notes (do not follow)
We used to use MySQL. We used to have a payments module. Ignore the old auth flow
in v1, it was removed two quarters ago.

## Commands
To run tests, run pytest. To lint, run ruff.
```

---

## Trim-pass answer (what survives)
Almost nothing. The only lines with real value are buried at the bottom:
`pytest`, `ruff check .`, and the architecture pointer (data access in `db.py`,
routes in `app.py`). Everything else is prose the code already communicates,
philosophy that changes no behaviour, or **stale rules that actively mislead**
(the deprecated section is worse than useless — it spends context to confuse).
A good CLAUDE.md for this repo is under 20 lines and every line is load-bearing.
