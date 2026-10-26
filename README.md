# Silverwing — Commercial Experience

Live: https://lordjeferies.github.io/silverwing-public/

Start with [HANDOFF.md](HANDOFF.md), [the complete brief](docs/PRODUCT-BRIEF-2026-10-26.md), [validation](docs/VALIDATION.md) and [publishing](docs/PUBLISHING.md).

## Maintenance

- `index.html`: page structure; `design.css` preserves the existing art direction; `components.css` supplies accessible components and responsive layout fixes.
- `app.js`: current application logic; `i18n.js` + `translations.json`: shared language preference and keyed copy. New modules render their own explicit bilingual strings. Some legacy Studio copy still needs translation review.
- `playground.html`: isolated CSS material experiment; exports visual settings without changing the public site.
- `catalog.json`: approved public catalog; `inner-circle.html` + `member-demo.js`: public explainer and local delivery/date/link registry.
- `sw.js`: versioned, exact-route offline cache; code and catalog use network first, large images cache on demand.

Run `python3 scripts/validate.py` and `python3 scripts/package.py`. The latter builds `_site/` from an explicit runtime allowlist. GitHub Actions validates then publishes that folder.

This repository is public. It contains only the commercial runtime, approved offer and public documentation. The original private `silverwingabraxas` repository and private Sites deployment are separate and were not modified.
