# Contributing

This repository adapts the upstream [Freeflow](https://github.com/hassan-mohiddin/freeflow) skills for Claude web.

Submit core workflow semantics to the upstream project first. Changes here should focus on web compatibility, Claude installation documentation, validation, and release packaging.

Before proposing a change:

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate.py
python3 scripts/package.py --output-dir /tmp/freeflow-claude-web-release
```

Keep each skill self-contained. Do not add links that escape a skill directory, OpenAI metadata, Claude Code plugin hooks, local machine paths, secrets, generated archives, or `.freeflow/` state.
