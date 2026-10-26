# Publishing

GitHub Actions `Validate and publish Pages` runs schema/asset/script checks, packages only an explicit runtime allowlist, then deploys `_site` to Pages. Pages must use GitHub Actions as its build source. No client tokens or credentials are shipped. Existing private Sites remains unchanged.

To update: pull the public repository, edit, run `python3 scripts/validate.py`, inspect the diff, commit and push main. Confirm the workflow succeeded and verify the real Pages URL and assets before reporting publication. Revert the release commit to restore earlier code if needed.

For commercial price changes use Studio's reviewed catalog export and replace only commercial `catalog.json` through an authenticated GitHub commit. A draft export is intentionally rejected by validation. Service limits and count invariants remain enforced. Keep costs, notes and full Studio backups private.
