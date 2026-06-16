# Spec v0 — Share a note (first pass, with gaps)

> This is the spec MOST teams write on the first pass. It looks complete. Run the
> agent against it, then read what got built. The gaps below the line are where
> the build will go wrong. Do not fix them yet — surface them first, then iterate
> to v1.

## Endpoints
- `POST /notes/<id>/share` (auth) → mints a public link, returns `{ "share_url": "/s/<token>" }`
- `POST /shares/<token>/revoke` (auth) → turns a link off
- `GET /s/<token>` (public) → returns `{ "title", "body" }` of the note

## Acceptance criteria
- A signed-in user can call share on a note and get back a URL.
- Opening the URL returns the note's title and body.
- Calling revoke returns success.

## Constraints
- Use the existing `notes_api/db.py` data layer; add a `shares` table.
- Tokens go in the URL path.

## Definition of done
- The three endpoints exist and return the documented shapes.
- Tests cover share, open, and revoke.

---

## ⚠️ The gaps in this spec (find these in the build)
This spec is silent on four things. Each silence becomes a defect:

1. **Revocation behaviour is not a testable contract.** "Revoke returns success"
   says nothing about the link *afterwards*. A build can mark something revoked
   and still resolve the link, and this spec would call it done.
2. **Token unpredictability is unspecified.** "Tokens go in the URL path" doesn't
   say they must be unguessable. A deterministic token derived from the note id
   satisfies this spec and is trivially forgeable.
3. **Ownership on share/revoke is unstated.** Nothing says only the *owner* may
   share or revoke. A build that lets any signed-in user share any note by id
   passes.
4. **"Tests cover X" without asserting the contract.** A test that calls revoke
   and asserts it returned success "covers revoke" by this spec, while never
   checking the link stops resolving.

> These four gaps are not hypothetical. They are exactly the defects Day 3's
> trust gates catch in the shipped build. **Spec gaps surface as build gaps.**
> Iterate to `SHARE_NOTE_SPEC_v1.md` and re-run.
