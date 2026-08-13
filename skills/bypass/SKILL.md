---
name: bypass
description: Use when the user explicitly asks to skip or reduce workflow steps for the next action or current task.
---

# Bypass

Skip optional ceremony, not authority, judgment, safety, or evidence.

Bypass changes the workflow method within an already accepted action. It does not authorize work, expand scope, switch mode, resolve a user-owned decision, override source truth, or create tool access or permissions.

## Establish The Boundary

Before using bypass, identify:

- the accepted action it applies to;
- the named optional step, or whether the user selected next-action or current-task scope;
- the current mode;
- the evidence and checkpoints that still govern the action.

A natural-language request to “bypass,” “skip the process,” or “keep this lightweight” defaults to the next optional step unless the user clearly applies it to the current task. If no accepted action exists, return to `workflow` when available or explain the missing authorization; do not treat bypass itself as implementation authority.

Bypass never changes mode. In `conversation`, remain read-only and use the separately installed `mode-contract` skill when available before any proposed mutation. In `workflow` or `strict-workflow`, keep the active mode's decision and evidence pressure.

## Skip Only Optional Pressure

A bypass may remove a step that does not protect accepted intent, material risk, required evidence, or a selected checkpoint, such as:

- an unnecessary Spec or Plan;
- extended questioning whose answer would not change the action;
- an artifact created only for ceremony;
- an optional checkpoint or extra review with no remaining risk purpose.

Do not infer that a named artifact or review is optional. Inspect why it exists first.

## Preserve Non-Bypassable Boundaries

A generic or scoped bypass does not remove:

- the user's authority over product behavior, scope, public interfaces, compatibility, permissions, security, privacy, billing, data loss, migrations, deployment, or another hard-to-reverse outcome;
- a conflict with code, tests, docs, policies, requirements, accepted behavior, or another source of truth;
- platform safety, tool permission, and approval controls;
- proportionate verification and supported self-review before a factual or completion claim;
- an accepted Spec, Plan, selected checkpoint, required artifact review, selected independent review, or other accepted completion boundary;
- a stop condition or evidence that invalidates the current route.

Material risk still needs the decisions and evidence that address that risk. A domain label alone does not require ceremony, but bypass cannot erase an observed risk.

If the user wants to change an accepted requirement, evidence boundary, or selected review, treat that as a route change rather than bypass. Use `decision-gate` when available if one user-owned choice or source conflict blocks progress; use `workflow` when available if the route itself must change. Otherwise apply the same boundary directly.

## Apply The Selected Scope

### Next

Next-action scope skips one identified optional step for the current accepted action. Re-check the route immediately after skipping it.

If that step was the only remaining optional pressure, complete the bounded action and verify it. The bypass is then spent. It also expires if the action changes, another gate appears, or the route stops.

### Task

Current-task scope reduces optional workflow pressure for the accepted task. The task is the accepted request or active Working Record scope—not every repository action, future chat, or related task. If that boundary is unclear, ask before applying task scope.

The task scope ends at completion, abandonment, material scope change, or explicit withdrawal. Reassess each new risk, conflict, checkpoint, and completion claim inside that scope.

When an existing Working Record is already authorized for maintenance and task-scoped bypass must survive context loss, use `track-work` when available to record its exact source, scope, and expiry. The record preserves the instruction; it does not broaden it. Without an available durable-memory capability, do not claim bypass survives context loss.

Never convert either scope into a permanent, repository-wide, or cross-task bypass.

## Act Or Stop

When the bypass is valid:

1. skip only the selected optional pressure;
2. perform only the separately authorized bounded action;
3. use only available tools and gather the same proportionate evidence the outcome requires;
4. report what was skipped, the result, and whether the bypass is spent or still task-scoped.

When a boundary remains:

1. do not perform the blocked action;
2. name the boundary bypass cannot remove;
3. route to the owning mode, decision, discussion, or workflow step.
