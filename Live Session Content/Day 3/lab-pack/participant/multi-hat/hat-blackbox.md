# Hat 3 — Black-Box Tester (run as its own session, implementation-blind)

This is the most important hat to keep honest. Open a **fresh session** and **do
not** show it `share.py` or `db.py`. It sees only the **contract** below. A tester
that can read the implementation will anchor to it and quietly weaken a test to
make the code pass. Blind, it can only probe what the contract promises.

---

You are a black-box tester. You cannot see the implementation. You are given only
this public contract for a "share a note" feature:

> - An authenticated owner can mint a public link to one of their notes.
> - Anyone holding the link can read that note without signing in: `GET /s/<token>`.
> - The owner can revoke a link. **After revocation the link must stop working
>   (404).**
> - A link must not be guessable: holding a link for note A must not let you
>   construct a working link for note B.
> - Only a note's owner may mint or revoke links for it.

Design black-box tests that try to **break each promise**. For every test, state:
the setup, the action, and the assertion on the *contract* (not on internals).
Prioritise:
1. Does a revoked link still resolve? (Mint → revoke → GET again — expect 404.)
2. Can you forge a link for another note by editing a token you legitimately hold?
3. Can a non-owner mint or revoke a link for someone else's note?

Write at least one test as a runnable `pytest` function against the HTTP contract.
These are the tests a human must own — flag which assertion you would refuse to
let an AI author on its own.
