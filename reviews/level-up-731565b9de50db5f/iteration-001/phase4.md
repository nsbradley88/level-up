# Level Up Phase 4 — Scope validation

## Run record

- Run `731565b9de50db5f`, iteration `001`.
- Phase 4 opening identity matched Phase 2 exactly: 305 files and aggregate
  identity-manifest SHA-256
  `d6fa6309b86e15e2913013b56c374a7fe34cb6997a4397c18cfd4adff29060de`.
- Three fresh validators were assigned. Two initially resolved the wrong
  repository or could not locate the external aggregate. Their first responses
  were discarded. One corrected against the exact subject; the other failed to
  produce a correction, so a separate already-fresh schema validator performed
  the operations validation from the exact subject. This reduces clean
  one-mandate separation but preserves independent validation of every retained
  recommendation.

## Adjudicated scope

### Validated

- `i001-p3-scoper-a-001` — **validated**. Canonical schema-source work is
  necessary and feasible because three representations already diverge.
  Field-level structural derivation/equivalence is preferred to brittle SQL
  text equality. No schema-v2 redesign is included.
- `i001-p3-scoper-a-002` — **validated**. SQLite exposes defaults through
  `PRAGMA table_info.dflt_value`; default assurance is mechanically sound after
  A001. Canonical packets must pass and isolated default drift must fail a
  stable diagnostic. Exact `sqlite_master` text equality is rejected.
- `i001-p3-scoper-a-006` — **validated**. Approximately four to six objection
  scenarios are right-sized for valid lineage, broken lineage, open-objection
  blocking, and non-blocking withdrawn/resolved/advice cases.
- `i001-p3-scoper-a-007` — **validated**. Two to three invalidation scenarios
  should cover permanent PASS suppression, invalidated-count accounting, and
  broken invalidation reference without duplicating existing REVISE tests.
- `i001-p3-scoper-a-008` — **validated with priority qualification**. One thin
  residual negative each for cohort, scratchpad, and model-profile behavior is
  acceptable, but existing substitution and scratchpad checks must not be
  duplicated. This remains lower priority than objection and invalidation
  coverage.
- `i001-p3-scoper-a-009` — **validated for the documentation-first path**.
  Declare `loop2_phases.status` descriptive/non-normative. The conditional
  vocabulary-enforcement branch is unresolved until compatibility evidence
  exists and does not proceed.
- `i001-p3-scoper-b-001` — **validated as documentation-only**. Direct
  `install.ps1` on an unsupported engine fails at `#requires` before in-band
  output; Bash's runtime refusal remains intentionally different. State this
  boundary and place assurance in an external host-version matrix. A wrapper is
  out of scope unless structured parity becomes a product requirement.
- `i001-p3-scoper-b-002` — **validated**. Add bounded, lane-neutral,
  inspect-first guidance for codes 15, 16, 17, and 19, and state that 20 ABSENT
  requires no recovery. No new codes, automatic cleanup, or parity promise.

### Qualified

- `i001-p3-scoper-a-003` — **qualified**. State continuity should be enforced
  only after defining canonical mapping/normalization semantics. Raw equality
  of current prose state labels is not proven coherent. Once defined, add a
  distinct diagnostic plus forward and REVISE state-break fixtures.
- `i001-p3-scoper-a-004` — **qualified**. Reject mutation-bearing/applied units
  outside `07-execute`. Do not reject planned or demonstrably non-mutating rows
  unless the normative contract explicitly prohibits them.
- `i001-p3-scoper-a-005` — **qualified**. Define accepted cause forms before
  enforcement and keep operator suspension distinct from resource/capability
  blocking. Do not require a resource row for every suspension. Reasonless
  states should fail only after this taxonomy is explicit.

### Rejected or unresolved

- Exact-text DDL equality and mandatory `IF NOT EXISTS` text matching are
  rejected as brittle; structural/default equivalence is the supported goal.
- Enumerating and enforcing `loop2_phases.status` is unresolved and excluded
  from the current scope.
- A PowerShell bootstrap wrapper is not justified by the current product
  contract and is excluded.
- No recommendation pursues exhaustive checker branch coverage, Bash/PowerShell
  false parity, automatic recovery, or stronger unsupported-lane guarantees.

## Validated sequence

1. A001 canonical schema source.
2. A002 default assurance.
3. Define semantics, then implement qualified A003–A005.
4. A006–A007 highest-value fixture batches.
5. A008 capped residual coverage and A009 contract clarification.
6. B001–B002 documentation and recovery guidance.

All retained recommendations have an evaluator, observable success condition,
bounded tradeoff, non-goal, and reversal. They proceed to adversarial review.

<!-- level-up-complete -->
