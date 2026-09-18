# Level Up Phase 3 — Refinement and scope

## Run record

- Run `731565b9de50db5f`, iteration `001`.
- Objective, subject, constraints, and governing skill are unchanged.
- Two fresh scopers, separate from Phase 1 and Phase 2 authors, derived this
  scope from the validated record and primary evidence.
- Every recommendation below is unvalidated until Phase 4.

## Proposed checker and protocol scope

### `i001-p3-scoper-a-001` — Canonical schema source

- Sources: `i001-p1-research-a-009`, `i001-p1-research-a-010`.
- Outcome: eliminate drift among normative DDL, fixture DDL, and checker schema
  metadata.
- Mechanism: designate one canonical DDL representation and derive generator
  and checker expectations from it, or generate a checked-in module plus an
  equivalence assertion. Prefer field-level structural parsing over brittle SQL
  text equality.
- Areas: `SKILL.md`, fixture generator, checker schema constants.
- Dependencies/sequence: foundation for schema and fixture work.
- Alternatives: retain duplication with a drift test; move DDL to a data file.
- Tradeoff/risk: Markdown extraction can be fragile; a data file changes the
  documentation shape.
- Evaluator/success: a fresh schema reviewer can inject a column/default drift
  in one non-canonical surface and observe a precise failure.
- Non-goals/reversal: no schema-v2 redesign; revert to duplicated constants if
  derivation proves less maintainable.

### `i001-p3-scoper-a-002` — Assert normative defaults and DDL identity

- Sources: `i001-p1-research-a-009`, enabled by
  `i001-p3-scoper-a-001`.
- Outcome: prove the schema under test carries the normative defaults.
- Mechanism: inspect `PRAGMA table_info` defaults, emit canonical defaults in
  fixtures, and add an isolated wrong/missing-default invalid fixture. Treat
  `IF NOT EXISTS` as a generation/property concern rather than requiring exact
  SQL text unless the contract makes it semantically necessary.
- Areas: checker schema validation, generator DDL, schema tests.
- Risk: over-strict textual comparison would reject equivalent SQLite DDL.
- Evaluator/success: default drift yields a stable code/location while existing
  canonical packets pass.
- Non-goals/reversal: no index/trigger validation; remove default checks without
  changing ledger data.

### `i001-p3-scoper-a-003` — Enforce transition state connectivity

- Source: `i001-p1-research-a-004`.
- Outcome: make adjacent transition rows connect on phase, version, and state as
  `SKILL.md` requires.
- Mechanism: define canonical state continuity semantics, add a distinct
  state-break diagnostic, and add forward and REVISE state-break negatives.
  If current destination prose cannot literally match the next source state,
  define a normalization/mapping rather than comparing arbitrary strings.
- Areas: transition contract, `_validate_transition_order`, fixtures/tests.
- Alternative: weaken the documented rule to phase/version only.
- Risk: current valid fixtures may reveal loose state names.
- Evaluator/success: state-only breaks fail; existing connected flows pass.
- Non-goals/reversal: no wholesale state-machine redesign.

### `i001-p3-scoper-a-004` — Confine mutation-bearing apply units to Phase 07

- Source: `i001-p1-research-a-007`.
- Outcome: align checker enforcement with the Phase-07-only mutation rule.
- Mechanism: reject applied or otherwise mutation-bearing units outside
  `07-execute`; retain planned/non-mutating representation only if the contract
  explicitly permits it; add one positive and one negative fixture.
- Areas: apply-unit prerequisite logic and tests.
- Alternative: explicit exception list if legitimate non-07 mutation exists.
- Risk: real historical packets may expose undocumented use.
- Evaluator/success: an out-of-07 applied unit fails a specific diagnostic.
- Non-goals/reversal: no status/disposition redesign.

### `i001-p3-scoper-a-005` — Suspended and blocked consistency

- Source: `i001-p1-research-a-006`, including merged
  `i001-p2-validator-a-011`.
- Outcome: prevent reasonless blocked/suspended packets.
- Mechanism: define accepted cause forms, such as a blocking capability,
  explicit suspended reason, or suspended/ceiling-reached resource observation,
  and require consistency with run status. Cover operator suspension separately
  from resource suspension.
- Areas: run, capability, resource, and lifecycle validation.
- Risk: requiring a resource row for operator suspension would be false scope;
  accepted cause forms must be defined first.
- Evaluator/success: reasonless cases fail and each allowed cause form passes.
- Non-goals/reversal: no new columns; checks can be downgraded if historical
  compatibility requires advisory treatment.

### `i001-p3-scoper-a-006` — Objection lineage and gate fixtures

- Sources: `i001-p1-research-a-001` and qualified
  `i001-p1-research-a-003`.
- Outcome: demonstrate the highest-value currently unexercised checker logic.
- Mechanism: add a deliberately small set of end-to-end cases covering a valid
  objection lifecycle, broken lineage, an open objection blocking PASS, and
  withdrawn/resolved/advice non-blocking behavior.
- Dependencies: preferably after canonical schema work.
- Risk/control: fixture growth; cap the set at roughly four to six scenarios.
- Evaluator/success: lineage and gate blocking each have a positive and negative
  exact code/location assertion.
- Non-goals/reversal: no exhaustive branch coverage.

### `i001-p3-scoper-a-007` — Invalidation anti-laundering fixtures

- Source: supported portion of `i001-p1-research-a-002`.
- Outcome: prove invalidated PASS results never regain credit.
- Mechanism: add focused cases for permanent invalidated-PASS suppression,
  nonzero invalidated-count accounting, and a broken invalidation reference.
- Dependencies: shares generator work with recommendation 006.
- Evaluator/success: each named behavior has an isolated assertion.
- Non-goals/reversal: do not duplicate existing REVISE source/version tests.

### `i001-p3-scoper-a-008` — Thin coverage for cohort, scratchpad, and model profile

- Source: qualified `i001-p1-research-a-003`.
- Outcome: cover three remaining core surfaces without pursuing branch-complete
  testing.
- Mechanism: one isolated negative per surface: selected-cohort composition,
  malformed scratchpad heading/path, and model-profile/substitution mismatch.
- Dependencies: lowest priority after objection and invalidation cases.
- Risk/control: cap at approximately three fixtures.
- Evaluator/success: each surface has at least one precise failing assertion.
- Non-goals/reversal: no 100-plus-code coverage campaign.

### `i001-p3-scoper-a-009` — Clarify phase status semantics

- Source: `i001-p1-research-a-005`.
- Outcome: make clear whether `loop2_phases.status` is descriptive or normative.
- Mechanism: prefer a documentation-only declaration that it is descriptive
  unless a stable vocabulary already exists; enumerate and enforce only with
  compatibility evidence.
- Risk: premature vocabulary enforcement could invalidate valid descriptive
  states.
- Evaluator/success: `SKILL.md` alone answers whether the field is enumerated.
- Non-goals/reversal: no `gate_status` change.

## Proposed operational scope

### `i001-p3-scoper-b-001` — Explicit PowerShell pre-execution boundary

- Sources: `i001-p1-research-b-001`, `i001-p1-research-b-006`.
- Outcome: preserve fail-closed `#requires` behavior while making the lack of
  in-band structured refusal explicit and testable at the host boundary.
- Mechanism: document that unsupported engines fail before script execution and
  therefore emit a host error; point assurance to an external host-version
  matrix rather than internal smoke. Do not add a wrapper unless
  machine-readable parity becomes an explicit product requirement.
- Areas: README support matrix and release/evaluator guidance.
- Alternative: separate bootstrap launcher, with added entrypoint and support
  surface.
- Evaluator/success: direct unsupported-engine behavior is classified
  consistently and is not mistaken for Bash parity.
- Non-goals/reversal: no change to accepted reparse, hook, receipt, or
  PowerShell-on-Unix differences.

### `i001-p3-scoper-b-002` — Recovery guidance for codes 15, 16, 17, and 19

- Source: `i001-p1-research-c-005`.
- Outcome: give operators bounded, lane-neutral next actions.
- Mechanism:
  - 15 mixed refusal: stop automation and reconcile ownership/refusal signals;
  - 16 race: reclassify after the competing actor settles and retry only from a
    clean state;
  - 17 SOURCE_INVALID: reacquire a trusted source before retry;
  - 19 OWNED_OTHER: hand off to the owner or use the supported ownership/removal
    path;
  - 20 ABSENT: state explicitly that no recovery is required.
- Areas: README recovery section and support playbook.
- Risk: overprescriptive text could imply guarantees across unequal lanes.
- Evaluator/success: each actionable code states what happened, next action,
  retry condition, and stop condition.
- Non-goals/reversal: no new codes or automatic cleanup.

The proposed separate evaluator matrix from the operations scoper is merged
into recommendations B001 and B002 rather than retained as a third overlapping
item.

## Recommended sequence

1. Canonical schema source and default assurance: A001–A002.
2. Contract-enforcement fixes in parallel: A003–A005.
3. Highest-value fixture batches: A006–A007.
4. Capped residual coverage and clarity: A008–A009.
5. Documentation-only operational boundaries: B001–B002.

<!-- level-up-complete -->
