# Finding Triage (Part 3)

Take **one** flagged finding from the OWASP skill or the security subagent and
walk it all the way down. The discipline is the deliverable: a flag you neither
fixed nor explicitly dismissed is worse than no flag at all.

---

**Finding:** _(paste the tool's output: severity, OWASP category, file:line)_

**1. Is it real?**  Real / False positive  — and how you know
> _Reproduce it or rule it out. For an access-control flag: write the request a
> non-owner would send and show it succeeds (real) or is blocked (false positive).
> For an injection flag: show an input that changes the query's structure._

**2. Blast radius if real**
> _What can an attacker reach? Whose data? How much?_

**3. Decision:**  Fix now / Fix later (ticket) / Dismiss

**4a. If fixing — the remediation**
```diff
- # before
+ # after
```
> _Re-run the test suite and the OWASP skill. Confirm the finding clears and the
> tests still pass._

**4b. If dismissing — the written justification**
> _Why is this not exploitable here? What assumption holds? A dismissal is a claim
> you are signing your name to. Write it as if it'll be read in an incident review._

**Owner / sign-off:** _your name_ — _date_
