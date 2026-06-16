# Responsible-AI Lab — flag the risky ones (Part 5)

Below are five prompts/transcript snippets from real-ish daily use. Flag each for
**data exposure**, **injection risk**, **both**, or **fine**. Then rewrite **one**
flagged prompt to be safe without losing its usefulness.

---

**A.**
> "Here's our prod database URL `postgres://admin:S3cr3t@db.lvt.internal/main` and
> the AWS key `AKIAIOSFODNN7EXAMPLE`. Write a script that connects and counts rows."

**B.**
> "Summarise this customer support thread and draft a reply. [pastes a thread
> containing the customer's full name, email, home address, and card last-4]"

**C.**
> "Read `vendor/third_party_helper.py` and follow any setup instructions you find
> in its comments, then run them."

**D.**
> "Refactor `notes_api/db.py` to use a connection pool. Keep behaviour identical
> and add a test."

**E.**
> "Fetch this URL and do what the page says to finish configuring the repo:
> https://pastebin.example/setup-steps"

---

## Your flags
| Prompt | Risk | Why |
|--------|------|-----|
| A | | |
| B | | |
| C | | |
| D | | |
| E | | |

## Rewrite one safely
Pick a flagged prompt and rewrite it so it keeps the useful intent and drops the
risk (for example: reference a secret by env-var name instead of pasting it; redact
PII before sending; never let the agent execute instructions it found in files or
on the web without you reading them first).
