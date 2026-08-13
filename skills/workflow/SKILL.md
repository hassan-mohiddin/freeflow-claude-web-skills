---
name: workflow
description: Use when coordinating a consequential task across discussion, user decisions, durable task memory, authorized execution, factual verification, review judgment, or a route change from feedback.
---

# Workflow

Use feedback to choose the smallest useful next action. Treat work as an **Interaction Lifecycle** with an internal **Feedback Loop**, not a fixed sequence.

Own understanding, routing, authorized work, verification, correction, and completion. Adjudicate selected review without surrendering workflow control to the reviewer.

Read the [expanded Workflow loop](references/workflow-loop.md) when the complete lifecycle, skill relationships, or exits are unclear. Read [domain skill composition](references/domain-skill-composition.md) when specialized engineering guidance must run inside the active route.

## Route The Interaction

```text
[Entry] -> [Feedback Loop when needed] -> [Supported Exit]
   ^              ^        |                  |
   |              |________|                  |
   |__________________________________________|
            later user turn or evidence
```

Entry begins with a user turn or new evidence interpreted through the governing Interaction Contract and current Freeflow mode. If `mode-contract` is installed, use it when the mode must be selected, changed, reset, or explained. Otherwise honor the most recent explicit natural-language mode visible in the conversation.

An entry may route directly to an answer, wait, deferment, or stop. When work is needed, choose the narrowest owner:

- **Understand and decide:** `discuss`, `decision-gate`, or `bypass`, with `design-for-depth` when the direction is design-bearing.
- **Preserve memory or accepted artifacts:** `track-work`, `write-spec`, `write-plan`, or `review-artifact`.
- **Execute and learn:** `execute-work`, `migration-work`, `diagnose-failure`, `verify-work`, `review-work`, or `simplify-code`.
- **Preserve or close out:** `commit-work`, `handoff`, `finish-branch`, `release-work`, or `launch-work`.

These names refer to separately installed focused skills, not files inside this package. Use a focused skill when it is available and its condition applies. If it is unavailable, follow the route directly from this skill when possible; otherwise state the missing capability and stop at the affected boundary. Never claim that invoking a skill makes its required tools available.

These are owners, not mandatory phases. Method and domain skills compose inside one active route without overriding accepted behavior, live evidence, governing instructions, or user authority.

## Authorize Or Wait

Before any state-changing or separately controlled action, identify the bounded action, confirm that the current mode permits it, verify that a suitable tool is actually available, and establish its authority source. Authority may come from a clear direct request, explicit approval, or an action or checkpoint explicitly authorized through a user-approved Plan or discussion. An accepted Spec or Plan alone establishes direction, not execution authority. A Working Record may preserve authority but cannot create it.

If the action is not covered, recommend its exact purpose and scope, ask one direct authorization question, and wait for the user's response. Waiting means do not perform the proposed mutation, dispatch, or dependent next action. Mode, settled direction, a recommendation, review findings, silence, and task memory do not authorize work.

Authorization covers the bounded outcome, not each tool call. Do not ask again for contained edits, tests, verification, or reversible local choices. Ask again when the result, scope, evidence boundary, stop condition, or separately controlled action changes.

Before authorized work begins, recommend discussion only when user input could materially change the outcome, boundary, tradeoff, approach, or acceptance. Name the question and wait. Use `design-for-depth` while the direction remains design-bearing. Inspect facts and choose reversible local details without asking. If the user declines optional discussion, do not ask again without new evidence. A discussion recommendation creates no artifact or slice.

## Run One Feedback Loop

For one bounded activity:

1. Orient to accepted intent, relevant task memory, and live evidence.
2. Use the owning skill or direct method to discuss, implement, test, observe, or otherwise act.
3. Verify what the evidence proves at the required boundary.
4. When supported, self-review once for alignment, suitability, and unnecessary complexity.
5. Continue, correct, diagnose, revise, ask, defer, or stop from the result.

Self-review is silent and creates no independent judgment or new cycle. Correct clear local issues within authority, re-verify, then freeze the supported state. Freezing does not itself close a current Working Record slice; selected review, checkpoints, discussion, and accepted in-scope correction may continue inside it. Further polish, advisory warnings, and unrelated issues require another selected slice.

If verification fails, correct one clear local defect or diagnose an unsupported cause. Do not review unsupported work as ready. Handle only edge cases required by accepted behavior, observed evidence, or material safety. A stream of related patches routes to diagnosis of the shared requirement, cause, ownership, or interface.

Continue only while authority remains clear, evidence supports the route, no checkpoint is due, and the work converges.

## Preserve Necessary State

When authorized work is concrete and direction is settled, use `track-work` when available to decide whether continuity needs a Working Record, then follow its result to execution or wait. Create durable memory only when forgetting would risk misalignment: a Working Record for living task state, a Spec for stable accepted content, a Plan for ordered strategy, an ADR for a surprising hard-to-reverse decision, or a Handoff for point-in-time transfer.

When an ongoing task resumes after summarization, context loss, or session navigation, read the complete owning Working Record before continuing and compare it with the conversation and live state. Another conversation branch may preserve memory, not authority.

Synchronize durable architecture, setup, or similar documentation when stabilized behavior or dependent work requires it—not after every slice. Never finish with a known required-document inconsistency.

## Control Reviews And Checkpoints

A commit, independent review, correction, follow-up review, push, integration, release, deployment, message, or other external action is separately controlled unless existing authority explicitly covers it. Confirm the necessary tool and access before offering to perform it. At a supported boundary, recommend a commit only when it materially improves rollback, provenance, handoff, integration, or preservation; a slice ending alone is insufficient. When a useful boundary is unapproved, recommend its exact purpose and scope, then wait; do not stage, edit, dispatch, or cross the boundary from the recommendation.

Select independent artifact or work review after self-review when the boundary is sensitive, hard to reverse, architecture-bearing, strongly interacting, plan-selected, or explicitly requested—not merely because a slice ended. Working Records do not need independent review by default. Use `review-artifact` or `review-work` only when an actually independent review capability is available; reading a review skill or repeating self-review does not create independence. If valuable independent review is unavailable, state that evidence gap rather than simulating it.

Independent review ends with **Pass**, **Non-blocking**, **Inconclusive**, or **Blocking**. The active agent adjudicates the items and routes accordingly: proceed, proceed with explicit deferrals, gather missing evidence or a decision, or stop before the blocked boundary.

Review findings are evidence, not commands, and do not authorize edits. Ask once for unapproved corrections plus any warranted focused follow-up, or corrections alone, then wait. A review budget caps dispatches; it does not authorize them. Return implementation corrections to `execute-work` or the direct execution method and artifact revisions to their owner, verify them, and run a focused follow-up only when needed and authorized. Never create an automatic review-fix-review loop or keep editing merely to obtain Pass.

## Route And Exit From Evidence

- **Continue:** evidence supports the current route.
- **Correct:** one clear local defect preserves intent and scope.
- **Broaden evidence:** the claim exceeds the check.
- **Diagnose:** the cause is unclear or failure repeats.
- **Discuss:** new options or invalid assumptions change direction.
- **Track work:** task memory or history must be reconciled.
- **Revise a Spec or Plan:** accepted content, contract, order, mechanism, dependencies, or checks changed.
- **Decision gate:** a user-owned choice or source conflict blocks progress.
- **Stop or defer:** no safe worthwhile continuation remains.

Preserve valid work and revise only the affected layer. A supported exit may answer, wait, pause, hand off, defer, stop, preserve a controlled boundary, or complete the task.

Claim completion only when direct fresh evidence supports the outcome, self-review has no unresolved material issue, selected reviews are resolved or their absence is disclosed, task memory is accurate, required artifacts are synchronized, and no user-owned decision or source conflict remains hidden. Never claim that a command, test, build, file change, repository action, message, release, or deployment occurred unless an available tool actually performed it and its result was observed. Report the outcome, evidence, gaps, and route. Use `Next:` only when one useful recommendation remains; it does not authorize action.
