# Freeflow Skills for Claude Web

A web-focused distribution of [Freeflow](https://github.com/hassan-mohiddin/freeflow), a feedback-based control system for coding agents.

This repository packages **22 Freeflow workflow skills** for Claude's custom Skills interface. It adapts the upstream skills for Claude web without installing Freeflow's Claude Code plugin, lifecycle hooks, or other host adapters.

## Requirements

- A Claude Free, Pro, Max, Team, or Enterprise account with custom Skills available.
- **Code execution and file creation** enabled.
- **Skills** enabled by your organization owner when your workspace manages capabilities.
- Access to [Customize → Skills](https://claude.ai/customize/skills).

See Anthropic's [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude) documentation for current availability and organization controls.

## Install

### 1. Add the Freeflow instructions to Claude

Claude web does not run Freeflow's Claude Code lifecycle hook. The account-wide instructions provide an always-loaded interaction contract and skill-routing bootstrap:

1. Open Claude's settings.
2. Find **Instructions for Claude**.
3. Paste the complete block below and save it.
4. Start a new conversation before using Freeflow.

> **Global effect:** account-wide instructions apply to all Claude conversations. If you no longer want this behavior, remove the block. You may instead use project instructions when you want Freeflow limited to one Claude project.

<!-- CLAUDE-INSTRUCTIONS:START -->
```markdown
# Freeflow Interaction Contract

Work as a collaborative senior engineer. Interpret the whole user turn before
acting. Use evidence, disagree when warranted, and correct yourself when
evidence changes.

Answer questions without inferring action. Treat criticism, examples,
hypotheses, and tentative ideas as discussion, not authorization. If a question
affects consent or method, answer and wait unless the user clearly authorizes
action.

For consequential work, establish enough shared understanding for
the next sound action. If a brief discussion is likely to materially improve
alignment on the outcome, boundaries, tradeoffs, approach, or acceptance,
recommend it, name the question, and wait. Otherwise choose reversible local
details and proceed. Do not ask merely because more detail is possible.

# Freeflow Skills Bootstrap

When Freeflow skills are enabled, use them when their descriptions match the
request. For consequential work, use the `workflow` skill to select the
narrowest relevant Freeflow method. Do not invoke skills as ceremony or assume
they grant tools, permissions, or authorization.
```
<!-- CLAUDE-INSTRUCTIONS:END -->

The copy-ready text is also available in [`CLAUDE_INSTRUCTIONS.md`](CLAUDE_INSTRUCTIONS.md). The upstream Interaction Contract remains separately preserved in [`INTERACTION_CONTRACT.md`](INTERACTION_CONTRACT.md).

### 2. Download and extract the release bundle

Download:

```text
freeflow-claude-web-skills.zip
```

Permanent latest-release link:

<https://github.com/hassan-mohiddin/freeflow-claude-web-skills/releases/latest/download/freeflow-claude-web-skills.zip>

**Extract this download bundle before using it. Do not upload the bundle itself to Claude.** Anthropic documents one skill folder per upload ZIP. After extraction, the `skills/` directory contains 22 upload-ready ZIPs.

Use this release asset rather than GitHub's automatically generated **Source code (zip)**. Source archives include development files and are not Claude skill packages.

### 3. Upload each skill ZIP

For every ZIP inside the extracted `skills/` directory:

1. Open [Customize → Skills](https://claude.ai/customize/skills).
2. Select the option to add or upload a custom skill.
3. Upload one `<skill>-0.1.1.zip` file.
4. Enable the uploaded skill.
5. Repeat for the remaining skills you want to use.

Each ZIP has Anthropic's documented structure:

```text
workflow-0.1.1.zip
└── workflow/
    ├── SKILL.md
    └── references/
```


## Included skills

| Area | Skills |
| --- | --- |
| Routing and decisions | `workflow`, `discuss`, `decision-gate`, `mode-contract`, `bypass`, `design-for-depth` |
| Execution and evidence | `execute-work`, `tdd`, `diagnose-failure`, `verify-work`, `simplify-code`, `migration-work` |
| Durable artifacts and continuity | `track-work`, `write-spec`, `write-plan`, `review-artifact`, `handoff` |
| Review and delivery | `review-work`, `commit-work`, `finish-branch`, `release-work`, `launch-work` |

Contributor-only upstream packages `evaluate-skill` and `write-skill` are intentionally excluded because their primary workflows depend on terminal, Node.js, Git, process, or filesystem capabilities that are not reliably available in ordinary Claude web conversations.

Claude discovers skills from their descriptions and may compose multiple enabled skills automatically. The packages are independently installable and contain no filesystem links to sibling skills.

## Using Freeflow

- The default Freeflow mode is `workflow`.
- Say **“Use conversation mode”** for read-only discussion and exploration.
- Say **“Use workflow mode”** for ordinary consequential work.
- Say **“Use strict-workflow mode”** for security, privacy, billing, migrations, deployment, data-loss, or other hard-to-reverse boundaries.
- A mode changes how work proceeds; it does not grant tools, permissions, or authorization.
- Installed skills cannot make unavailable repository, shell, browser, deployment, or external-system tools available.

## Trust and safety

Treat third-party skills as instructions with elevated influence:

- Read the skill contents before installing them.
- Install only release artifacts from a source you trust.
- Review sensitive actions at the point of use.
- Verify the release's `CHECKSUMS.sha256` file when provenance matters.
- See [`SECURITY.md`](SECURITY.md) for reporting and safety guidance.

## Repository layout

```text
skills/                  22 independently installable Claude skill packages
scripts/                 validation and deterministic packaging tools
tests/                   repository and archive checks
CLAUDE_INSTRUCTIONS.md    copy-ready account/project instructions
INTERACTION_CONTRACT.md  canonical upstream interaction contract
MANIFEST.md              package inventory and provenance
```

Local `.freeflow/` state is retained for contributors but ignored by Git and excluded from every release artifact.

## Maintainer commands

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate.py
python3 scripts/package.py
```

Packaging produces one stable download bundle containing 22 individual skill ZIPs, plus bundle and inner checksums under ignored `dist/`.

## Provenance and license

This Claude-web distribution uses the web-safe Freeflow skill adaptations and the authoritative source at [hassan-mohiddin/freeflow](https://github.com/hassan-mohiddin/freeflow).

Freeflow and this distribution are available under the [MIT License](LICENSE).
