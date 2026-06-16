# Responsible-AI Checklist for Agentic Coding (team artifact)

Tuned to coding agents at LVT. Use it every session, every repo. Day 4 turns the
mechanical parts of this into deterministic hooks.

## Data boundaries — what never enters a prompt or the agent's context
- [ ] No secrets or credentials (DB URLs, API keys, tokens) pasted into prompts.
      Reference them by environment-variable name instead.
- [ ] No customer PII (names, emails, addresses, payment data). Redact before sending.
- [ ] No commercially sensitive data outside its approved boundary.
- [ ] Disciplined environment handling: secrets live in the environment, never in
      source the agent reads.

## Provenance & licensing
- [ ] Treat generated code that closely mirrors a known source as a
      license-contamination risk; check before adopting verbatim blocks.
- [ ] Follow the house policy on what generated code may be committed.

## Prompt injection
- [ ] Don't let the agent execute instructions it found in files, dependencies, or
      fetched web content without you reading them first.
- [ ] Remember the permission model is the backstop here (full strategy on Day 3).

## Hallucination as an engineering risk
- [ ] Verify invented APIs and plausible-but-wrong code. Tidy output still needs
      checking. Run it; don't trust it on sight.

## Accountability
- [ ] The engineer who ships owns the change, regardless of who or what wrote it.
      Your name on the commit is your signature on the behaviour.
