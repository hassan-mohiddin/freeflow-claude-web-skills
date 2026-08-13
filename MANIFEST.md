# Freeflow Claude Web Skills Manifest

- Release version: **0.1.1**
- Web skill packages: **22**
- Authoritative upstream: [hassan-mohiddin/freeflow](https://github.com/hassan-mohiddin/freeflow)
- Authoritative source revision used during preparation: `11740bc6137b21a896a4ab4aae1f85f7d22ccd4b`

## Provenance

This distribution was adapted from the web-safe Freeflow skill packages and checked against the authoritative Freeflow source. The upstream project already ships a Claude Code plugin, but Claude Code marketplace metadata and lifecycle hooks are intentionally not used as evidence or packaging for Claude web.

The public repository has no dependency on the maintainer's local checkout. The upstream GitHub repository and recorded source revision are the durable public source references.

## Distribution boundary

Included:

- 22 web-focused workflow skills under `skills/`;
- package-local references;
- repository documentation, validation, tests, and release tooling.

Intentionally excluded from Claude skill archives:

- `evaluate-skill` and `write-skill`, because their primary contributor workflows require terminal-oriented capabilities not reliably available in ordinary Claude web conversations;
- `agents/openai.yaml` and ChatGPT interface icons;
- `.claude-plugin/`, lifecycle hooks, `setup-freeflow`, Pi extension code, Output Router, and host configuration because Claude web does not execute those adapters;
- `.freeflow/` and `.serena/` local state;
- repository documentation, tests, and scripts.

The canonical Freeflow Interaction Contract remains in `INTERACTION_CONTRACT.md`. The copy-ready `CLAUDE_INSTRUCTIONS.md` adds a Claude-web Skills Bootstrap and is installed through Claude's account-wide or project instructions as described in `README.md`.

## Packages

| Skill | Package contents beyond `SKILL.md` |
| --- | --- |
| `bypass` | — |
| `commit-work` | `references/staging-decisions.md` |
| `decision-gate` | — |
| `design-for-depth` | `references/design-pressure-signals.md`, `references/interface-design-loop.md`, `references/software-design-philosophy.md` |
| `diagnose-failure` | `references/diagnostic-loop-catalog.md`, `references/flaky-and-performance.md` |
| `discuss` | `references/checkpoints.md` |
| `execute-work` | `references/code-practices.md`, `references/execution-loop.md` |
| `finish-branch` | `references/integration-options.md` |
| `handoff` | `references/templates.md` |
| `launch-work` | `references/launch-readiness.md` |
| `migration-work` | `references/migration-lifecycle.md` |
| `mode-contract` | — |
| `release-work` | `references/release-evidence.md` |
| `review-artifact` | `references/reviewer-prompt.md` |
| `review-work` | `references/reviewer-prompt.md`, `references/security-risk-lens.md` |
| `simplify-code` | `references/simplification-patterns.md` |
| `tdd` | `references/test-design.md` |
| `track-work` | `references/working-record-schema.md` |
| `verify-work` | `references/browser-runtime-evidence.md`, `references/integration-evidence.md`, `references/performance-evidence.md` |
| `workflow` | `references/domain-skill-composition.md`, `references/workflow-loop.md` |
| `write-plan` | `references/plan-shapes.md` |
| `write-spec` | `references/artifact-standards.md`, `references/decision-records.md`, `references/spec-shapes.md` |

## Release artifacts

`scripts/package.py` creates:

- `freeflow-claude-web-skills.zip`: stable-name download bundle containing the 22 individual ZIPs, an extraction notice, and inner skill checksums;
- `skills/<skill>-0.1.1.zip`: one top-level skill directory per Claude upload archive;
- `CHECKSUMS.sha256`: the SHA-256 digest for the externally published bundle.

The bundle contains `SKILL_CHECKSUMS.sha256` for all 22 inner skill ZIPs.

The download bundle is not itself a Claude skill. Users extract it and upload each ZIP from its `skills/` directory separately.

The packaging process uses stable ordering and ZIP metadata so identical source content produces identical archives.

## Verification status

Repository structure, individual ZIP shape, package reproducibility, and checksums are verified locally. Authenticated Claude-web upload and activation were confirmed by the maintainer; Claude still requires each skill ZIP to be uploaded separately.
