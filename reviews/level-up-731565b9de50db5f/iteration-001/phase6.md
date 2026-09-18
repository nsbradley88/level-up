# Level Up Phase 6 — Adversarial validation and convergence

## Run record and identity

- Run `731565b9de50db5f`, iteration `001`.
- Phase 6 opening identity matched prior evidence windows: 305 files,
  identity-manifest SHA-256
  `d6fa6309b86e15e2913013b56c374a7fe34cb6997a4397c18cfd4adff29060de`.
- Three fresh independent validators received only neutral candidate rows.
  They independently derived evidence status, materiality, classification,
  distinctness, and objective/constraint effects before reconciliation.
- Frozen Phase 5 ledger: SHA-256
  `90c39ae6bbc93f3ba92b11bb0550b5ec949bd9618aa8b618263321740950cb6c`,
  7,385 bytes.

## Reconciled candidate record

### Confirmed open subject defects

- `i001-p5-sol-001` — **confirmed/high/security-relevant**. The checker creates
  an in-memory SQLite connection and runs the entire untrusted `ledger.sql`
  through `executescript` before schema validation. It installs no authorizer.
  An in-memory main database does not prevent statements such as `ATTACH` or
  other filesystem-writing SQLite operations from reaching the host.
  This violates the checker's read-only/untrusted-input boundary. It remains
  distinct from schema equivalence and is the top-priority open finding.
- `i001-p5-sol-003` with `i001-p5-claude-002` —
  **confirmed/material**. Normative defaults are omitted from generated DDL and
  `_validate_schema` does not inspect `dflt_value`. This can certify a schema
  whose omission behavior differs from the normative schema.
- `i001-p5-sol-004` with `i001-p5-claude-003` —
  **confirmed/material**. Adjacent transitions are connected on phase/version
  but not `previous.to_state` to `current.from_state`, despite the normative
  state-continuity rule. Raw prose equality is not an adequate fix; canonical
  edge/state semantics are required.
- `i001-p5-claude-004` — **confirmed/narrow**. REVISE recognition, generic
  legality, and detailed REVISE validation use separate predicates. Current
  source/version cases are tested, but the duplicated predicate is a drift
  risk. It should be single-sourced while transition work is touched.
- `i001-p5-sol-005` with `i001-p5-claude-005` —
  **confirmed/material**. A non-planned mutation-bearing unit in a phase other
  than `07-execute`, including `09-final-record`, can use the generic earlier
  qualifying-PASS fallback. This contradicts the Phase-07-only mutation rule.
- `i001-p5-sol-006` with `i001-p5-claude-007` —
  **confirmed/material contract gap**. Blocked/suspended run states and
  `suspended_reason` have no cause-consistency rule. The fix must use existing
  host/resource/evidence/authority causes; operator-initiated suspension is not
  currently normative and must not be invented without a separate schema and
  state-machine decision.

### Confirmed assurance gaps

- `i001-p5-sol-002` with `i001-p5-claude-001` —
  **partially confirmed/material robustness gap**. Current table and column
  sets are substantially aligned, but normative DDL, generator DDL, and checker
  metadata are independent representations with no equivalence assurance and
  already diverge on defaults. Retain as the parent canonicity item.
- `i001-p5-sol-007` with `i001-p5-claude-008` —
  **confirmed structural coverage gap**. Objection lineage/reference and
  open-objection gate logic have no direct fixtures. Semantic correctness of an
  objection remains explicitly not checkable and is excluded.
- `i001-p5-sol-008` with `i001-p5-claude-009` —
  **confirmed fixture gap**. No fixture records non-null
  `invalidated_by_phase/version` or a nonzero `invalidated_pass_count`.
  This is assurance debt, not independently proven invalidation source logic.
- `i001-p5-sol-009` with `i001-p5-claude-010` —
  **confirmed/qualified low-priority gap**. Add only genuinely uncovered
  deterministic structure: scratchpad path/heading cases, selected cohort
  composition, and any residual model binding not already covered. Freshness,
  independence, diligence, provenance, semantic truth, and model identity
  beyond labels remain not checkable.

### Confirmed documentation and operational gaps

- `i001-p5-sol-010` with `i001-p5-claude-011` —
  **confirmed/low-to-moderate**. Vocabulary omission proves only that
  `loop2_phases.status` is opaque and not currently deterministically validated;
  it does not prove the field is non-normative. Documentation should say exactly
  what is and is not checked, without assigning new semantics.
- `i001-p5-sol-011` with `i001-p5-claude-012` —
  **confirmed/low**. Unsupported direct `install.ps1` invocation fails at the
  host `#requires` boundary before guaranteed installer JSON or a classified
  installer exit code. The exact "13-error" counterfactual is not demonstrated
  by packaged tests and should be removed or explicitly labeled untested.
- `i001-p5-sol-012` with `i001-p5-claude-013` —
  **confirmed/moderate with correction**. Recovery guidance is missing for code
  14 as well as 15, 16, 17, and 19. Code 20 ABSENT needs no destructive cleanup,
  but README currently conflates `--verify` refusal with neutral `--list`
  classification. The recovery and catalog text must distinguish verbs.

### Closed confidence and prioritization records

- `i001-p5-claude-006` — **confirmed confidence record**. Planned apply-unit
  shape/exemptions are represented; do not broaden the Phase-07 fix to reject
  all planned rows without a contract basis.
- `i001-p5-claude-014` — **confirmed prioritization rule**. Behavioral defects
  outrank documentation-only work. It introduces no separate subject defect.

Every Phase 5 candidate row is reconciled above through its carried ID or merge.
No materiality disagreement remains unresolved.

## PR-ready corrected scope

1. **Constrain untrusted SQL before execution.** Install an SQLite authorizer
   or an equivalent strict statement capability policy before
   `executescript`; deny attachment, detachment, extension loading, unsafe
   pragmas, and filesystem-writing operations. Return a structured INVALID
   diagnostic and add benign prohibited-statement fixtures. A text pre-scan may
   supplement but must not replace SQLite authorization.
2. **Canonicalize schema assurance.** Designate one structural schema source,
   derive/equivalence-check consumers, and validate normalized defaults through
   SQLite metadata. Avoid exact SQL formatting equality.
3. **Close state and mutation enforcement gaps.** Define semantic transition
   state continuity; single-source REVISE recognition; reject mutation-bearing
   non-07 apply units while preserving explicitly allowed planned rows.
4. **Define blocked/suspended causes.** Use only existing normative causes and
   require coherent run/capability/resource/evidence records. Do not introduce
   operator suspension implicitly.
5. **Add bounded regression evidence.** Prioritize objection and invalidation
   fixtures, then tightly capped uncovered scratchpad/cohort/model cases.
6. **Correct contract and operator documentation.** Describe phase-status
   opacity, the PowerShell host boundary without an untested numeric claim,
   recovery for 14/15/16/17/19, and verb-specific ABSENT semantics.

## Convergence adjudication

Full convergence is **not** reached:

- the objective is a desired-subject-state objective;
- confirmed defects remain open against it; and
- `i001-p5-sol-001` also affects the non-waivable read-only/untrusted-input
  constraint.

The run reaches **bounded convergence after one iteration**. The material claims
have been independently validated, subject identity did not drift, and their
remaining resolution requires implementation and regression testing rather
than another research axis. No actionable research path is identified that is
likely to change these dispositions. Semantic objection correctness, identity
truth, hostile-local integrity, freshness, and provenance remain explicitly
outside deterministic verification.

No risk acceptance or waiver is applied. The final outcome is a PR-ready change
specification and evidence package, not a claim that Loop2 is fixed.

## Rules-only convergence check

- Exact checked draft: SHA-256
  `7ab1356b1f432d576cfb61bdc8870bbd5d30c08810b15fd4f11afbad0f00a876`,
  987 bytes.
- Separate checker result: `conformant`.
- No substantive change was made to the checked adjudication.

<!-- level-up-complete -->
