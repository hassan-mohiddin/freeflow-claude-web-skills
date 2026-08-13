---
name: migration-work
description: Use when replacing an existing software or data path and moving its consumers, state, or traffic safely.
---

# Migration Work

Move consumers, state, or traffic to an accepted replacement without losing compatibility, evidence, or recovery options.

A replacement existing does not prove that consumers moved. A migration unit may be complete while the old path remains under an accepted support contract. Removal is a separate claim with separate evidence and authority.

## Establish Authority And Scope

Loading this skill, discussing a migration, or approving a general implementation Plan does not authorize migration, deprecation, cutover, destructive cleanup, or removal. Execute only the stages and units explicitly requested or separately approved.

Use `decision-gate` when available when any of these remain unresolved:

- whether the old behavior should be maintained, deprecated, or removed;
- advisory versus compulsory migration, deadlines, or support windows;
- compatibility, public API, data conversion, downtime, permissions, billing, security, privacy, or data-loss behavior;
- irreversible cutover, destructive cleanup, or rollback limits.

Do not manufacture a migration because code looks old. Inspect ownership, supported consumers, runtime use, source truth, incidents, maintenance cost, and current value only through available tools and supplied evidence.

When replacement behavior, interfaces, ownership, or failure semantics remain unsettled, return that evidence to `workflow` when available. Use `discuss` for open direction, `design-for-depth` for design-bearing boundaries, and `write-spec` when accepted migration behavior needs a durable contract when those separately installed skills are available.

## Define The Migration Contract

Before moving anything, establish:

```text
Old contract and current value:
Replacement contract and known differences:
Consumers / callers / data / traffic:
Compatibility promise and support window:
Migration unit and ordering:
State written during transition:
Verification for each unit:
Rollback or forward-recovery path:
Removal proof:
Owner decisions and stop conditions:
Approved stages and scope:
```

Read [the migration lifecycle](references/migration-lifecycle.md) when choosing an API, code, configuration, dependency, feature, traffic, or data shape. Use only the stages required by the accepted migration; do not force every migration through one sequence.

Treat undocumented observable behavior as a possible consumer dependency until evidence says otherwise. Do not preserve every quirk automatically; surface consequential differences for decision.

## Prepare The Replacement

When an additive or replacement stage is approved:

- prove the replacement through the real caller path or interface;
- keep old and new ownership explicit;
- add adapters, flags, aliases, translation, or dual reads/writes only when the migration contract requires them;
- give temporary compatibility machinery an owner, purpose, failure behavior, exit condition, and removal evidence;
- do not add features to the old path unless required for safety or an explicit support decision.

If compatibility machinery starts spreading caller knowledge, public states, or exceptions, return the structural evidence to Workflow rather than building a second permanent system.

An emergency migration without a viable replacement may be necessary for security or data safety, but it requires explicit owner direction, bounded impact, and a documented failure and recovery contract.

## Move Bounded Units

Move one accepted consumer, cohort, traffic segment, configuration set, or data partition at a time.

Before changing any unit, confirm that an appropriate tool, access level, rollback or recovery capability, and evidence source are actually available. If not, stop at that boundary.

For each unit:

1. capture the relevant pre-migration state or baseline;
2. apply the migration through the intended path;
3. verify behavior, data, errors, permissions, and operational signals at the required boundary;
4. confirm rollback or forward recovery remains possible;
5. preserve evidence and account for remaining units.

Code search alone cannot prove completion when runtime, external, dormant, generated, offline, or independently deployed consumers may exist.

Stop and return evidence to Workflow when replacement behavior diverges, unknown consumers appear, a new owner decision is required, data cannot be reconciled, recovery assumptions fail, compatibility machinery spreads, or the next safe unit is unclear. Preserve completed units; do not restart the whole migration automatically.

## Remove The Old Path

Remove or disable the old path only when that stage is explicitly authorized and the accepted removal proof is satisfied.

Check, as relevant:

- supported active and dormant consumers are accounted for;
- runtime, telemetry, dependency, or owner evidence supports the absence claim;
- data and configuration are reconciled;
- compatibility, support-window, observation, and recovery obligations have ended;
- old code, adapters, flags, tests, docs, alerts, dashboards, secrets, jobs, and configuration are classified for removal or retention;
- the replacement remains verified with the old path disabled or absent.

Do not delete source truth or historical migration evidence merely to make searches clean. If current docs or contracts would become false, return them to Workflow and update them only when they are included in the approved migration or removal scope. Preserve durable history where repository policy requires it.

## Verification And Review

Use `verify-work` when available for each migration-unit, compatibility, reconciliation, and absence claim. “The new path passes” does not prove “the old path is unused.” Missing telemetry is unavailable evidence, not zero use.

Return the need for broader judgment to Workflow when the migration changes public contracts, moves consequential data, crosses security or privacy boundaries, affects many consumers, or performs irreversible cutover or cleanup. Workflow selects any independent review; this skill supplies the migration boundary and evidence.

Use `release-work` when available when the replacement must be published as a versioned artifact. Use `launch-work` when available when migration stages change production traffic, data, configuration, or exposure. Publication and production changes remain separately authorized.

## Report Completion Precisely

Report:

- approved migration scope and completed units;
- replacement and compatibility status;
- remaining consumers, state, traffic, or observation windows;
- verification and operational evidence;
- rollback or forward-recovery status;
- legacy components removed and deliberately retained;
- unresolved decisions, uncertainty, and residual risk;
- next approved unit, removal boundary, deferment, or stop route.

A migration unit is complete when its accepted consumers or state moved and its required evidence holds. A scoped migration may complete while the legacy path remains under an accepted support contract. Removal is complete only when its separate authorization and proof are satisfied.

Never claim that a migration, cutover, rollback, data move, removal, command, test, or observation occurred unless an available tool performed it and its result was observed.
