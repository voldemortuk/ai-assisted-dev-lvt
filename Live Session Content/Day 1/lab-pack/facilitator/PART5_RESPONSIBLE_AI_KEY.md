# FACILITATOR — Part 5 Responsible-AI Key

Expected flags on the five prompts/transcripts:

| Prompt | Flag | Why |
|--------|------|-----|
| **A** (prod DB URL + AWS key pasted) | **Data exposure** | Live credentials in the prompt. They're now in context, logs, history. Catastrophic. |
| **B** (support thread with PII) | **Data exposure** | Customer name, email, address, card last-4. PII outside its boundary. |
| **C** ("follow instructions in the file's comments and run them") | **Injection** | Instructions hiding in a dependency the agent reads, then executed. The classic coding-agent injection. |
| **D** (connection-pool refactor) | **Fine** | No secrets, no PII, no injection. A normal, well-scoped task. |
| **E** ("fetch this URL and do what the page says") | **Injection** (and risk of data exposure) | Executing instructions from fetched web content. The permission model is the backstop. |

## Safe rewrites (examples)
- **A:** "Connect using the `DATABASE_URL` environment variable (don't print it)
  and count rows in `notes`." The secret is referenced, never pasted.
- **B:** "Summarise this thread and draft a reply. I've redacted the customer's
  name, email, address, and card details; treat `[REDACTED]` as a placeholder."
- **C / E:** "Read `vendor/third_party_helper.py` and **tell me** what setup it
  claims to need. Do not run anything." Keep the human between discovery and
  execution.

## The lessons to bank
- Data boundaries: secrets by env-var reference, PII redacted, sensitive data stays
  in bounds.
- Injection: never let the agent execute instructions it found in files,
  dependencies, or fetched pages without a human reading them. The permission model
  (Day 3) is the backstop, not the first line.
- Accountability: whoever ships owns it. The checklist is enforced deterministically
  once hooks arrive on Day 4.
