# iDempiere specialists for Codex

Two optional personal agents (`idempiere-designer`, `idempiere-reviewer`) reuse three release-aware shared skills. Start with direct skills for small changes; delegate bounded design or independent review when it adds value. Model and reasoning settings are inherited rather than pinned.

See the [Spanish practical guide](GUIA.es.md) for the transferred context, prompts, token-efficiency guidance, installation, verification and measurement.

With Python 3.11+, from the repository root:

```bash
python3 codex/install.py          # dry run
python3 codex/install.py --apply
```

Skills are symlinked into `~/.agents/skills`; rendered agent TOML files go into `~/.codex/agents`. Existing conflicting files are never overwritten. Keep this checkout at its installed path. Test role discovery in a new Codex chat; parsing TOML alone does not prove client activation. A read-only role instruction does not create separate sandbox permissions.

Use `--uninstall --apply` to remove matching installed entries. Changed templates or personalized installed files require manual comparison before replacement/removal. No global config, model, permission or other project files are changed.

Edit design/review rules in `shared/`, then run `python3 codex/sync_design_skills.py`. Version directories retain standalone copies for distribution. Check with `--check` and run `python3 -m unittest discover -s codex/tests -v`.

Official references: [custom agents](https://learn.chatgpt.com/docs/agent-configuration/subagents), [skill discovery](https://learn.chatgpt.com/docs/build-skills). Subagents can improve independence or elapsed time but increase tokens over comparable single-agent runs; this pilot makes no measured savings claim.
