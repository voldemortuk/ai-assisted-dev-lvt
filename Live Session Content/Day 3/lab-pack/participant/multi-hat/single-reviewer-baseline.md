# Baseline — the all-in-one reviewer (run once, for comparison)

Run this in **one** session. This is the control in the experiment: a single
reviewer asked to do everything at once. Keep its output next to the three hats'
output and mark which findings the panel surfaced that this one missed or muddied.

---

You are an expert code reviewer. Review the diff for `notes_api/share.py`,
`notes_api/db.py`, and `notes_api/app.py`. Make sure it is secure, well-architected,
DRY, performant, correct, and well-tested. Give me your findings.

---

## After you run both, fill this in

| Finding | Single reviewer | Security hat | Design hat | Black-box hat |
|---|---|---|---|---|
| SQL injection in `get_note` | | | | |
| Broken access control in `create_share` | | | | |
| Guessable share token | | | | |
| Copy-paste drift in `revoke_share` | | | | |
| Dead branch in `resolve_share` | | | | |
| Hardcoded secrets | | | | |
| Revoked link still resolves (contract) | | | | |

**The point of the exercise:** the single reviewer, asked to hold six concerns at
once, tends to surface the loud ones and resolve the quiet tradeoffs silently. The
panel disagrees out loud — the black-box hat proves the revoke bug from the
contract while the design hat finds its cause in the code, and neither defers to
the other. Write down the one finding you would have missed reviewing alone.
