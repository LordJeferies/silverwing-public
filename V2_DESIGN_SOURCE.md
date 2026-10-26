# Silverwing V2 — source of truth

**Canonical editable V2 design:** https://www.figma.com/design/lpZaeu7ssXGSgRZuxb0CSv

**Previous V1 / Atelier 02 (reference only):** https://www.figma.com/design/xvKL2Xndsi0px6F8I5BdJf

The V2 Figma file contains the authoritative visual designs for the commercial experience and Business Studio, including full desktop journeys and 320/390/768px responsive frames. Do not call a CSS-only update a full implementation of this design.

## Release verification
- Compare each production section against the matching V2 Figma frame, not V1.
- Run actual browser checks at 320, 390, 768 and 1440px.
- Verify Spanish/English, contrast, keyboard controls, form calculations, mobile menus and images.
- Verify the deployment serves the new revision on GitHub Pages; account for service worker caches.
- Inner Circle sample metrics/rewards must remain clearly labeled as demos.
- Never store tokens, internal cost data or client records in public HTML or JavaScript.
