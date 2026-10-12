# Working on Concision

Concision is a portable Markdown skill. It has no runtime dependencies or build step.

- Keep the root `SKILL.md` as the only skill entrypoint; preserve the supporting `references/` files.
- Keep installation instructions in `README.md` consistent with the package. Host-specific metadata belongs in plugin manifests or `agents/openai.yaml`.
- Keep `metadata.version` in `SKILL.md`, both plugin versions, and the newest changelog entry in sync. Record behavior changes in `CHANGELOG.md`.
- The Claude manifest points to `./`. Omit `skills` from the Cursor manifest so it discovers the root skill.
- Run `python3 scripts/validate-package.py` with `requirements-dev.txt` installed, and `npx skills add . --list` before pushing. If Claude Code is available, also run `claude plugin validate .`.
- Never change repository visibility or publish a release without a user request.
- Preserve active development servers. If work requires stopping one, restart it and verify its local URL before finishing.
