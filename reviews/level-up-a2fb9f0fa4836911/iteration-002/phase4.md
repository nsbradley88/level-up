# Level Up — Iteration 002, Phase 4

## Validation record

- Run: `a2fb9f0fa4836911`; objective `O1` is review-output.
- All 309 subject files matched the evidence manifest immediately before Phase 4.
- Three independent validators audited need, mechanism, feasibility, alternatives, hidden dependencies, evaluation, and scope inflation.
- Only validated or explicitly qualified recommendations proceed.

## Adjudicated recommendations

### `i002-p3-scope-001` — **Qualified**

Hard-bump ledger schema 2 to 3 for key changes, but do not build a dual legacy ruleset without an installed-base requirement. Schema-2 inputs remain unsupported/`INVALID` under the current one-version checker unless a future archived-audit use case funds separate dispatch and fixtures.

Required conditions:

- name each version namespace explicitly;
- define the accepted `loop2_runs.skill_version` matrix or remove compatibility claims;
- update DDL, checker constant, all fixture ledgers/tests, SKILL identity, manifest digest/size, README and diagnostics atomically;
- schema/key changes must not ship piecemeal.

### `i002-p3-scope-002` — **Qualified and decomposed**

Proceed as four independently testable changes:

1. define closed run/phase/gate/transition state vocabularies and correct the unsatisfiable state-chain rule;
2. when transitions exist, derive/check active lifecycle position against the connected tail; preserve legitimate in-flight packets with no transitions;
3. bind forward transitions to exact gate evidence and reconcile gate-level deterministic result with the checker-result record;
4. require exact unanimous REVISE gate/target/packet evidence before a back-edge.

New lifecycle absence should initially classify as `INDETERMINATE` when required evidence is missing, not be silently promoted to structural falsehood. Existing conformant and intentional prefix fixtures must retain their intended result except where they embody the validated defect.

### `i002-p3-scope-003` — **Qualified; cohort restart condition unresolved**

Validated now:

- make `agent_id` required and unique within a run or replace it with an explicit unique attempt key;
- reject duplicate/ambiguous replacement references;
- validate predecessor identity across run, phase, version, round, slot, and attempt;
- require inactive scratchpads to retain ledger verdict/candidate/round agreement.

Whole-cohort redeclaration proceeds only after the normative text chooses one representation: four new attempts in the same round or a new round. The existing positive replacement fixture and the rule “replacing any slot voids the current round and all four validators declare again” cannot both remain. The chosen rule must update prose, gate semantics, fixture, and tests together.

### `i002-p3-scope-004` — **Qualified and split**

- **Validated schema-3 slice:** stage/generation becomes checker-result identity so prefix and completion results coexist immutably; include the missing recorded checker mode if it remains normative.
- **Qualified schema-2-safe slice:** strengthen completion now by requiring Phase-09 producer evidence, final/not-checkable/advisory artifacts where declared, active ancestry closure, non-planned apply state, and a successful completion check.

Do not hold cheap closure fixes behind the schema release. Status-gate artifact requirements for legitimate prefixes.

### `i002-p3-scope-005` — **Validated**

Apply units are Phase-07-only. Enforce unique contiguous sequence, exact status-dependent obligations, active-design prerequisite evidence, path equality/allowlisting, and terminal disposition after supersession or completion. Define when `disposition='none'` is valid so current in-progress/apply fixtures are not rejected indiscriminately.

### `i002-p3-scope-006` — **Validated**

Load and validate evidence-adjudication and failed-challenge tables or remove them from the normative schema. Preserve the existing `checked` list for compatibility and add a structured parallel coverage record containing check, status, and rows evaluated. Define that a per-check `indeterminate` coverage status does not itself change the top-level result/exit mapping.

### `i002-p3-scope-007` — **Validated**

Implement lexical one-statement framing that handles quoted semicolons, exactly one leading transaction begin and trailing commit, and an explicit comment policy. Normalize expected I/O, decoding, `sqlite3.Error`, and `sqlite3.Warning` failures into fixed `INVALID` codes/messages, with cleanup on every path. Do not catch broad exceptions or expose raw SQLite text/host paths.

### `i002-p3-scope-008` — **Qualified**

Use one resolver for packet-artifact references only, not repository apply paths or historical root labels. Reject traversal, drive-qualified/UNC/ADS forms, root/intermediate/final symlinks or reparse points, and special files according to an explicit policy. Hardlink rejection is a policy choice, not an inherent containment requirement; decide and document it rather than implying all multiple-link files escape.

Race-free containment against a hostile local host is unavailable under the current Python/platform boundary and remains NOT_CHECKABLE. Negative tests must cover each conditional artifact field and platform-specific form without checking live links into the repository.

### `i002-p3-scope-009` — **Qualified**

Introduce `loop2-advisory-v2`; do not silently tighten v1. Apply bounded ASCII grammar per identifier namespace, reject wrong types/booleans/oversized IDs, require nonempty normal adjudication and NOT_CHECKABLE sets, and define an explicit zero-adjudication not-run mode. Replace free-prose `missing_information` with contract-supplied typed references.

Candidates and constraints remain optional when semantically absent. Preserve advisory/non-authoritative disclosures.

### `i002-p3-scope-010` — **Qualified**

Parent-side recomputation is required, but canonicalization must avoid digest self-reference:

- hash a version/domain marker and sorted, length-delimited canonical relative paths plus raw bytes;
- exclude the digest-bearing contract, result, and execution outputs;
- reject links, special files, and portable-path collisions using recommendation 008;
- preferably bind an immutable packet manifest or canonical bundle;
- hash exact raw result bytes separately.

The profile remains tool-less and only echoes the supplied digest. This proves byte identity of the packet read by the validator, nothing about truth, model, independence, or whether the advisory agent read it.

### `i002-p3-scope-011` — **Qualified**

Terminal records already distinguish no-op via `action='noop'`; the defect is only that `outcome='applied'` overstates mutation. Choose one compatible contract:

- document `applied` as planned action completed and require consumers to inspect `action`; or
- add `noop`/`mutated` under result schema 2 with coordinated emitter, ValidateSet, smoke, README and consumer updates.

Do not claim sibling mutation precedes root refusal; both lanes already classify all targets before the global refusal gate. The actionable root issue is PowerShell silently skipping dangling recognized roots while Bash detects/refuses them. Converge on no-follow recognition and root-specific diagnostics, with tests for file, dangling-link, and directory-link roots.

### `i002-p3-scope-012` — **Validated**

Derive smoke summaries from executed cases/codes and report lane/platform/exclusions; do not claim skipped exit 18 or conditional race coverage. Split recovery guidance by Bash, PowerShell/Windows, and PowerShell/non-Windows and document actual post-exit-18 shapes.

No new production hook is justified. Existing PowerShell hooks are environment-gated, allowlisted, bounded, documented as non-security boundaries, and source-pinned. Bash already uses hook-free FIFO backpressure; adding a Bash hook would create unpinned attack surface.

## Release sequence

1. Ship schema-2-safe checker correctness: SQL framing, artifact existence/containment policy, apply restrictions, coverage reporting, completion closure.
2. Resolve the cohort-restart representation.
3. Ship one atomic schema-3 ledger release for identity, causal keys, and checker generations.
4. Ship advisory v2 ingress and canonical parent-side packet binding together.
5. Ship installer output/root behavior and lane-accurate documentation/reporting in one installer version.

## Rejected or removed scope

- no automatic schema-2 migration or dual checker without an installed-base requirement;
- no generic event-sourced ledger or artifact table;
- no claim of race-free hostile-host containment;
- no blanket hardlink rejection without policy justification;
- no silent advisory-v1 tightening;
- no digest computation inside the no-tools profile;
- no new Bash production test hooks.

<!-- level-up-complete -->
