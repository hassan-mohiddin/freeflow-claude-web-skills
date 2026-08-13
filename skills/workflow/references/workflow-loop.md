# Workflow Loop

Read this when the complete lifecycle, named skill edges, re-entry route, or possible exits are unclear. [Workflow](../SKILL.md) owns routing; each available focused skill owns its method.

The **Interaction Lifecycle** contains the recurring **Feedback Loop**.

## Complete Lifecycle

```text
[1. ENTRY] -- work needed --> [2. FEEDBACK LOOP] -- supported --> [3. EXIT]
    |                              ^       |                         |
    +--------- direct exit --------+       +------ feedback --------+
    ^                                                               |
    +---------------- later user turn or evidence -------------------+
```

### 1. Entry

A user turn or new evidence is interpreted through the governing Interaction Contract and current mode. Workflow may:

- answer, wait, defer, or stop directly;
- use Discuss or Decision Gate when direction is unsettled;
- choose the narrowest owner when work is needed.

Questions, criticism, examples, hypotheses, and recommendations are not action authority unless the whole turn clearly requests or approves the bounded action.

### 2. Feedback Loop

```text
Workflow chooses one owner
-> understand, decide, preserve, execute, or inspect
-> verify the resulting claim
-> self-review once when supported
-> route from evidence
   -> continue or correct locally
   -> diagnose an unsupported or repeated cause
   -> discuss changed direction
   -> revise the owning artifact
   -> gather evidence or a user decision
   -> use an approved checkpoint
   -> exit
```

The loop may recur many times inside one coherent Track Work slice. Re-entry preserves accepted decisions, valid work, evidence, and task state. A new method, finding, or review does not create a new slice by itself.

### 3. Supported Exit

A supported exit may answer, wait, pause, hand off, defer, stop, preserve an approved boundary, or complete the task. A later user turn or new evidence begins the lifecycle again.

## Skill Edges

- `discuss` shapes open direction. `decision-gate` owns one blocking user choice or source conflict. `bypass` reduces optional pressure inside accepted work.
- `track-work` decides whether continuity needs a Working Record and may surround any part of the loop. `write-spec` and `write-plan` own stable accepted content and ordered strategy; `review-artifact` handles selected artifact review.
- `execute-work` owns bounded changes. `tdd`, `simplify-code`, `diagnose-failure`, and `design-for-depth` compose only when their conditions apply.
- `verify-work` establishes what evidence proves. `review-work` and `review-artifact` guide self-review and selected independent judgment. Reading either review skill creates no independence.
- `commit-work`, `handoff`, `finish-branch`, `migration-work`, `release-work`, and `launch-work` own separately controlled boundaries. None authorizes the next stage automatically.

These are names of separately installed skills. Use one only when it is available and relevant. If it is absent, follow the route directly when possible or stop at the capability boundary.

Use [domain skill composition](domain-skill-composition.md) when specialized engineering guidance must operate inside one of these routes.

## Authorization Edge

The governing Interaction Contract distinguishes discussion from authority. The separately installed `mode-contract` skill constrains whether mutation is permitted when available; mode does not authorize work.

A clear request or approval may authorize one bounded outcome. An accepted Spec or Plan supplies direction unless its approval explicitly authorizes an action or checkpoint. A Working Record preserves authority but does not create it.

When a mutation or separately controlled action is not covered, Workflow recommends the exact action and waits for the user's response. It does not begin the action or a dependent next step. Existing authority covers contained implementation, tests, verification, and reversible local choices; do not ask again unless the boundary changes. Authority does not supply missing tools or permissions.

## Evidence And Re-entry

- A supported execution path is execution → observation → factual verification → silent self-review → Workflow.
- A clear local defect returns to its owner for correction and re-verification.
- Failed or inconclusive evidence with an unsupported cause routes to diagnosis before another patch.
- New options or invalid assumptions route to discussion.
- A user-owned choice or source conflict routes to a decision gate.
- Changed accepted content or strategy returns to the owning Spec or Plan.
- A coherent accepted correction may remain in the current Working Record slice; a distinct result, authority, or evidence boundary requires Workflow to establish the next slice.

Preserve valid work and revise only the affected layer. Do not continue because implementation started, redesign because an ordinary mistake occurred, or patch repeatedly when evidence points to one shared cause.

## Review And Checkpoint Edges

Select independent artifact or work review after self-review for an explicitly requested, sensitive, hard-to-reverse, architecture-bearing, strongly interacting, or plan-selected boundary—not simply because work ended. Require an actually independent reviewer or review capability; otherwise disclose the gap.

Independent review returns **Pass**, **Non-blocking**, **Inconclusive**, or **Blocking**. The active agent adjudicates every item. Review findings do not authorize edits, and a review budget does not authorize another dispatch. Corrections return to Execute Work or the artifact owner; focused follow-up occurs only when needed and authorized. Review 2 and Review 3 relationship and diagnosis rules live in the review skills.

A useful but unapproved review, correction, commit, or other checkpoint returns to Workflow to recommend and wait. Push, integration, migration, release, and launch remain separately controlled even when earlier work was authorized. Do not offer to perform a boundary unless the needed tool and access are available.

## Context And Completion

Before an expected context boundary, reconcile changed Working Record state. After summarization, context loss, or session navigation, read the complete record before continuing and compare it with the conversation and live state. Another conversation branch may contain memory, not authority.

Completion requires fresh observed evidence, supported self-review, resolved selected reviews or disclosed review gaps, accurate task memory, synchronized required artifacts, and no hidden user-owned decision or source conflict. Never report an unperformed tool action as completed.
