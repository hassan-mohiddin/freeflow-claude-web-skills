# Execute Work Loop

Read this when execution spans multiple bounded actions or slices, resumes from prior state, needs a specialized method, reaches a selected checkpoint, or reveals follow-on work. [Execute Work](../SKILL.md) owns the normal method; this reference expands its directed routes.

## Directed Execution Graph

```text
[Requested or approved concrete work; effective mode permits mutation]
-> [Orient]
   source + authority + live state + current slice + stop conditions
-> [Choose one bounded action]
-> [Load one needed method or reference]
-> [Execute]
-> [Test or observe]
-> [Verify the claim at its required boundary]
   -> clear local defect
      -> [Correct within authority]
      -> [Test or observe]
   -> unclear or repeated failure
      -> [Diagnose Failure]
      -> [Workflow routes from the cause]
   -> contradicted, inconclusive, or route-changing evidence
      -> [Workflow]
   -> supported
      -> [Silent self-review]
      -> [Correct clear local issue and re-verify, or freeze]
-> [Route from the supported state]
   -> more accepted work for the same coherent result
      -> [Choose the next bounded action]
   -> accepted extension to result / scope / authority / evidence / stop conditions
      -> [Record write-ahead when a Working Record exists]
      -> [Choose the next bounded action]
   -> distinct result, authority, or independently useful evidence boundary
      -> [Workflow establishes current slice outcome]
      -> [Select a new authorized slice; use Track Work when present]
   -> approved checkpoint due
      -> [Use checkpoint owner]
      -> [Return its result to Workflow]
   -> unapproved follow-on work
      -> [Recommend exact scope and wait]
   -> supported pause or exit
      -> [Preserve state and report]
```

The graph may recur many times inside one Track Work slice. An action, verification run, self-review, review report, or owning-skill call does not create or close a slice by itself.

## Select A Method For The Action

Use only the separately installed method needed by the concrete boundary when it is available:

- Use `tdd` for test-first behavior work.
- Use `simplify-code` for behavior-preserving simplification.
- Use `design-for-depth` when direct evidence shows design-bearing ownership, interface, state, failure-unit, or coordination pressure.
- Use `diagnose-failure` when a failure lacks a supported cause.

These names are not files inside this package. If a focused skill is unavailable, apply the needed direct method when possible or state the capability gap. Do not stack methods because several descriptions match.

## Route Selected Checkpoints

A user-approved Plan or explicit discussion may select review, local commit, user-decision, or continuity checkpoints. When one becomes due, do not begin the next bounded action first. Use its owner and return the result to Workflow. If its conditions no longer hold, return the deviation rather than forcing the checkpoint.

Use these separately controlled routes only when already requested or approved and their required tools are available:

- `commit-work` for a commit or explicitly authorized push;
- `migration-work` for migration units, compatibility, cutover, recovery, or removal proof;
- `finish-branch` for merge, pull request, preservation, or discard;
- `release-work` for versioned release preparation, publication, or verification;
- `launch-work` for production rollout, rollback, or recovery;
- `handoff` for an authorized point-in-time transfer artifact.

A checkpoint result may support continuation, correction, another route, deferment, or stopping. It does not authorize the next lifecycle stage automatically.

## Resume Or Return

When resuming, reopen the source that established the work and inspect live state when accessible. If a Working Record exists, read its complete current context and slice through `track-work` when available; do not reconstruct authority or progress from a summary alone.

Continue only while accepted authority and evidence support the execution basis. Return to `workflow` when available when direction, authority, scope, source truth, strategy, or the intended result changes, or when no worthwhile safe continuation remains.
