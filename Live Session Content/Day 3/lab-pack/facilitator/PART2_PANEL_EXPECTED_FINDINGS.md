# FACILITATOR — Part 2 Multi-Hat Expected Findings

The experiment: three single-hat sessions vs one all-in-one reviewer, same diff.
What you want the room to SEE is not a longer list — it's that independence surfaces
findings the single reviewer resolves silently.

## What each hat should surface

| Finding | Security | Design/DRY | Black-box | Single reviewer (typical) |
|---|---|---|---|---|
| SQL injection (`get_note`, `%`-format) | ✅ leads with it | sometimes | n/a (blind) | usually catches |
| Broken access control (`create_share` no owner check) | ✅ | rarely | partially (non-owner mint test) | **often misses** |
| Guessable token | ✅ | ✅ (as determinism) | ✅ (forge-a-link test) | sometimes |
| Copy-paste drift in `revoke_share` | rarely | ✅ leads with it | ✅ (proves via contract) | sometimes |
| Dead branch in `resolve_share` | no | ✅ | no | sometimes |
| Hardcoded secrets | ✅ | sometimes | no | sometimes |
| **Revoked link still resolves** | maybe | ✅ finds cause | ✅ **proves from contract** | **frequently resolved silently** |

## The money moment
The **black-box hat** is implementation-blind, so it cannot rationalise the revoke
bug away — it just mints a link, revokes it, requests it again, and the contract
breaks. The **design hat** independently finds the *cause* (wrong argument). Neither
defers to the other. The single all-in-one reviewer, juggling six concerns, tends to
note "revoke looks fine" and move on — it silently resolved a tradeoff it should have
surfaced.

## Run notes
- Insist on **separate sessions**. If the black-box hat can see `share.py`, it will
  anchor and weaken its own test — demo this failure if a pair does it by accident.
- The hard line: each engineer commits **one human-authored assertion** on the
  critical path. The canonical one is the revoke contract
  (`participant/multi-hat/human-assertion-example.py`) — it FAILS on the current
  code, which is the proof the AI's green suite was covering air.
- Debrief question to bank for the wrap: "Which finding would you have missed
  reviewing alone?"
