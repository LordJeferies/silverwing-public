# Validation — 2026-10-26

## Code checks actually executed
- `python3 scripts/validate.py`: local HTML asset paths, JavaScript syntax, bilingual dictionary shapes and 27 quote combinations per app (54 across both).
- Public approved catalog schema, counts and service limits checked. Package allowlist excludes documentation and development files from the hosted artifact.
- Explicit review download inspected: `status=approved`, complete counts, limits, no internal costs/notes. Export remains disabled until review; changing a price invalidates approval.

## Browser checks actually executed locally
- Commercial plan navigation, Maximum + Interview + Cinematic total USD 2,398, proposal rendering and ES/EN switching.
- Studio responsive menu and catalog draft/review/download flow, approval invalidation after price changes.
- Inner Circle add delivery/date, persistence after reload and language switch.
- Responsive iframe checks at 1440, 768, 390 and 320 CSS pixels for commercial landing and Studio overview: document width equals viewport, no measured visible control/heading/input overflow. This is not a full accessibility or every-section audit.
- Mobile screenshot review found floating language/help controls covering content; controls moved into document flow with wrapping and contrast fixes.

## Limits
No claim of exhaustive accessibility, native Safari/iPhone, screen reader, full offline/install/update lifecycle, print/PDF dialog or every legacy translation. Figma is not edited in this release because the current file session is a visitor. New member module is local/demo only. No real API analytics, accounts, redeemable rewards or backend permissions.

Additional browser checks: Playground Contrast preset updates blur to 36px and downloads settings JSON; commercial proposal HTML download completed; Inner Circle HTTPS post link saved and open link rendered.
