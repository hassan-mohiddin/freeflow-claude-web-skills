---
name: mode-contract
description: Use when choosing, changing, resetting, or explaining Freeflow's conversation, workflow, and strict-workflow modes in Claude.
---

# Mode Contract

Apply one of exactly three Freeflow modes: `conversation`, `workflow`, or `strict-workflow`.

A mode changes how work proceeds. It does not authorize an action, resolve a user-owned decision, override live evidence, expand scope, or make an unavailable tool available.

## Establish The Active Mode

Use the most recent explicit natural-language mode selection that remains visible in the current conversation. The user may select a mode with wording such as:

- “Keep this in conversation mode.”
- “Use workflow mode and implement it.”
- “Use strict-workflow for this migration.”
- “Reset the Freeflow mode.”

When no explicit selection is visible, use `workflow` as the default for work routed through Freeflow. Resetting the mode returns to that default.

Do not infer a mode change from task shape. A question during Workflow remains in Workflow. An implementation request during Conversation remains in Conversation until the user changes mode.

Treat the selection as conversation state, not durable application configuration. Do not claim that it persists across unrelated chats, survives missing context, or changed a hidden setting. When resumed context does not establish the mode and the distinction changes the next action, ask one direct question.

## Follow The Effective Mode

### Conversation

Answer, discuss, critique, explore, draft in the response, and perform requested read-only inspection.

Do not mutate files, repository state, external systems, or durable artifacts. If the user requests mutation, answer any accompanying questions, explain the mode boundary, and ask whether they want to switch to `workflow` or `strict-workflow`.

Ask only what the answer needs. Conversation mode does not require workflow artifacts, checkpoints, plans, specs, or independent review.

### Workflow

Use the installed `workflow` skill when it is available and the task needs coordination across discussion, decisions, execution, verification, or review. Otherwise follow the same adaptive method directly: inspect or ask when ambiguity changes the next action, create durable artifacts only when they preserve needed state or decisions, and verify claims against fresh evidence.

A clear direct request or explicit approval may authorize its bounded outcome. Workflow mode alone does not authorize work, and it does not require every lifecycle phase.

Within an authorized outcome, do not repeatedly ask for contained edits, checks, verification, or reversible local choices. Ask again when the outcome, scope, evidence boundary, stop condition, destructive effect, or separately controlled action changes.

### Strict Workflow

Use the same adaptive Workflow with stronger decision, evidence, and checkpoint pressure at high-risk or hard-to-reverse boundaries.

Apply that pressure when work materially affects security, privacy, billing, permissions, data loss, migrations, public interfaces, compatibility, deployment, or architecture.

Use the installed `decision-gate` skill when it is available and a user-owned choice or source conflict blocks progress. Otherwise state the exact decision, explain why it matters, and wait. Gather evidence for the relevant risk surface before crossing a consequential boundary or claiming success.

Select artifacts, checkpoints, verification, and independent review when they reduce material risk. Do not add them automatically merely because Strict Workflow is active.

Strict Workflow does not grant authority, bypass safety, or turn every implementation detail into a user decision.

## Change Mode Deliberately

The user owns mode changes. Accept explicit natural-language equivalents; do not require commands, menus, configuration files, or exact syntax.

Recommend `strict-workflow` when risk warrants it, but continue under the active mode unless the user changes it or another workflow boundary blocks progress. A recommendation is not a mode change.

A task type, risk classification, direct skill invocation, or workflow route does not switch mode. Invoking an execution skill during Conversation still does not permit mutation.

When the user selects or resets a mode, acknowledge it briefly only when confirmation is useful. Do not claim to have changed an application setting.

Mention the active mode only when the user asks, changes it, or it materially changes the next action.

## Keep Authority And Capability Separate

In every mode:

- questions, criticism, examples, hypotheses, and tentative ideas do not authorize mutations;
- an accepted Spec or Plan establishes direction, not execution authority;
- review findings do not authorize corrections;
- tool availability and permissions must be checked before relying on a tool;
- claims about commands, tests, builds, files, repositories, messages, releases, or deployments require direct observed evidence.

If a requested action cannot be performed with available capabilities, preserve the selected mode, state the limitation, and provide the smallest useful alternative. Do not simulate completion.
