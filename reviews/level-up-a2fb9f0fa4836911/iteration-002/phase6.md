# Level Up — Iteration 002, Phase 6

## Validation and independence

- Run: `a2fb9f0fa4836911`; objective `O1` is review-output.
- All 309 subject files matched the recorded manifest immediately before Phase 6.
- Four validators received neutral candidate partitions. One independently opened the sealed ledger, reducing its blindness; a fresh fifth validator re-audited those rows without phase artifacts. A dispatch omitted failed-row neutral fields; the fifth validator corrected that completeness gap.
- A separate tie-break validator resolved the only mechanism disagreement: Bash exit 18 is deterministically testable without a production hook by making the parent directory non-writable after installation.
- No subject code, test, installer, or fixture was executed.

## Reconciled material findings

### Ledger identity, lifecycle, and replacement

| Phase 5 ID | Reconciled result | Effect on handoff |
|---|---|---|
| `i002-p5-sol-002` | confirmed | Validator declarations must bind REVISE target and packet digest; gate and transition must match all four. |
| `i002-p5-sol-003` | confirmed | Active ancestry must invalidate/reject stale pre-back-edge gates before apply/completion credit. |
| `i002-p5-sol-006` | confirmed | Load every table, reject every foreign-run child row, and validate references before claiming coverage. |
| `i002-p5-sol-008` | confirmed | Add a parent-generated attempt identity/state so failure-before-artifact is representable without fabricated scratchpads. |
| `i002-p5-opus-001` | partially confirmed/prospective | Schema 3 needs an explicit historical-packet policy; dual support is justified only if archived audit is an actual requirement. |
| `i002-p5-opus-003` | confirmed | One machine-readable schema-version source must drive SKILL, checker, generator, diagnostics, and verification. |
| `i002-p5-opus-007` | confirmed | Objection candidate identity is under-specified; separate candidate coordinates from where/when raised. |
| `i002-p5-opus-008` | confirmed | Objection lineage and gate blocking have no positive/negative fixture coverage. |
| `i002-p5-opus-011` | confirmed | Replacement must be an exact, reciprocal immediate-predecessor chain over the full cohort key. |
| `i002-p5-opus-013` | confirmed | Checker-type-specific result vocabularies are required. |

Merged confirmations: `opus-005/006/009/010/012` reinforce the already validated state, gate, replacement, identity and checker-generation defects. `opus-002/004` are bounded release-maintenance qualifications.

### Completion, packet, advisory, and runtime ownership

| Phase 5 ID | Reconciled result | Effect on handoff |
|---|---|---|
| `i002-p5-sol-001` | confirmed | A checker cannot verify a packet containing its own result; use immutable completion-ready input plus detached result receipt. |
| `i002-p5-sol-004` | confirmed | Evidence packet and contract need separate digests; excluding contract bytes without binding them permits substitution. |
| `i002-p5-sol-005` | confirmed | Advisory constraint/candidate/missing-information universes must be scoped per adjudication. |
| `i002-p5-sol-009` | confirmed | Containment covers packet root, ledger, manifest, every read/digest input and all ancestors, not only referenced artifacts. |
| `i002-p5-sol-011` / `opus-037` | confirmed | Mandatory runtime checkers are absent from the installed one-file payload. Either package typed owned tooling or make a pinned host checker an explicit preflight dependency; mandatory-but-undelivered is invalid. |
| `i002-p5-opus-025` | confirmed | Portable packet names need collision rules for case, trailing-dot/space, reserved and alias forms. |
| `i002-p5-opus-027` | confirmed | Advisory v2 must enforce the normative NOT_CHECKABLE minimum from a shared versioned source. |
| `i002-p5-opus-029` | confirmed | Advisory CLI arguments, streams and exit codes require direct tests. |
| `i002-p5-opus-030` | partially confirmed | Model pin/user invocation semantics are host-sensitive; define supported parent invocation and avoid unnecessary model pinning while preserving `tools: []`. |
| `i002-p5-opus-032` | confirmed | Separate packet root, packet manifest, and human packet document; the current `packet_path` pointer does not identify the consumed directory. |
| `i002-p5-opus-033` | confirmed | Required advisory execution metadata needs a durable versioned path/schema and structural validation. |

`opus-024/026/031` merge into the containment/digest findings. `opus-028` is non-material until a second advisory version exists but its explicit unsupported-version behavior belongs in v2 design.

### Apply, coverage, parser, and CI

| Phase 5 ID | Reconciled result | Effect on handoff |
|---|---|---|
| `i002-p5-sol-007` / `opus-019` | confirmed | Define coverage vocabulary, conditional manifest requirement, structured dispositions and checked existence. |
| `i002-p5-sol-010` | partially confirmed, downgraded | Add bounded untrusted-input limits as robustness hygiene; no small-input amplification was validated. |
| `i002-p5-sol-013` | confirmed | CI does not run ledger/advisory unit tests or checker/fixture schema-equivalence checks. Workflow evidence is outside the 309-file subject and is labelled accordingly. |
| `i002-p5-opus-015` | confirmed | Halted-before-write and command-only units need a representable empty path effect. |
| `i002-p5-opus-016` | confirmed | The design allowlist has no machine-readable apply representation; add one or explicitly keep the rule prompt-only. |
| `i002-p5-opus-020` | confirmed | Unknown recorded checks are silently filtered and the existing known-check test is vacuous for that direction. |
| `i002-p5-opus-021` | confirmed, Python-3.10-bounded | Same-line multi-statement input can escape structured handling via `sqlite3.Warning`. |
| `i002-p5-opus-022` | partially confirmed, low | `INSERT ... SELECT` reaches the authorizer but is denied by `SQLITE_SELECT`; tighten to VALUES-only for deterministic attribution, not security amplification. |
| `i002-p5-opus-023` | confirmed, expanded | Normalize OSError/decoding failures for ledger and scratchpad reads. |
| `i002-p5-opus-036` | confirmed | Verifier hard-refuses without Bash although README lists only Python as prerequisite; align prerequisite/docs or graceful partial behavior. |
| `i002-p5-opus-041` | confirmed, partially mitigated | Literal `/tmp` scanning is explicitly disclosed but does not enforce a runtime temp-root policy. |

`opus-014/017/018` were decomposed: unchecked run paths and omitted tables are confirmed; transition sequence is already enforced, apply-unit sequence is not.

### Installer and lane reporting

| Phase 5 ID | Reconciled result | Effect on handoff |
|---|---|---|
| `i002-p5-sol-012` | confirmed subject fact, bounded | `action='noop'` already distinguishes effect, but `outcome='applied'` overstates mutation. Choose and version an explicit success/effect contract; do not imply single-target terminal records exist. |
| `i002-p5-opus-035` | confirmed | Document USERPROFILE precedence and align/disclose existence plus canonicalization differences for dangling and linked personal roots. |
| `i002-p5-opus-039` | confirmed as reporting/prerequisite behavior | Report/skip unsupported FIFO capability explicitly rather than claiming race coverage; README already states the prerequisite. |
| `i002-p5-opus-040` | confirmed/merged | v0.6.0 diagnostics and fixture version remain stale and unvalidated. |

`opus-034` is excluded as a false premise. `opus-038` is substantially documented; retain exact per-lane race/exit coverage rather than equivalence claims.

Independent tie-break result: a hook-free Bash exit-18 smoke case is supported. Install, make the parent `skills` directory `0555`, uninstall as non-root, allow target-file unlink through the writable target fd, and assert final parent-relative `rmdir` failure/exit 18 and residue. This reuses existing prerequisites and permission-denial patterns.

## Failed challenges retained as confidence

- ATTACH and sqlite-master escape challenges failed; hostile standalone statements remain rejected before useful execution.
- Basic absolute/empty/traversal forms are rejected, though dot normalization and Windows-specific forms still need the broader portable resolver.
- Frozen slot profile prevents intra-run family/model drift; actual model identity remains NOT_CHECKABLE.
- Bash FIFO covers selected pre-apply races; it does not prove PowerShell hook-window parity.
- Installer target ancestry links/reparse points are rejected after each lane's canonicalization.
- Scratchpad traversal and apply-path order-sensitivity challenges failed.
- Extra nullable columns are accepted by current schema validation.
- Verifier PASS explicitly reports partial/skipped/refused status.

## Refined implementation handoff required

The validated Phase 4 direction remains sound, but the next refinement must incorporate:

1. detached completion-ready packets and result receipts;
2. exact active ancestry, REVISE declaration binding, objection coordinates, and full-run row scoping;
3. failure-before-artifact and reciprocal replacement identity;
4. machine-readable apply allowlist plus empty effects;
5. structured coverage and unknown-check rejection;
6. root-wide portable packet resolution;
7. separate evidence/contract/result identities and per-adjudication advisory universes;
8. explicit runtime checker ownership/preflight;
9. CI execution of checker suites and schema-equivalence tests;
10. versioned installer success/effect semantics and exact lane coverage, including hook-free Bash exit 18.

## Convergence adjudication

**Decision: not converged.**

Material new knowledge changed the Phase 4 handoff and actionable refinement/scope-validation paths remain. Confirmed subject defects do not themselves block review-output, but the PR-ready specification cannot yet freeze mechanisms or success criteria without another focused pass.

Separate dynamic convergence checker result: `conformant`. It agreed that material Phase 6 changes plus actionable validation require `NOT CONVERGED`. The checker was instructed to use no tools; host-enforced tool isolation was unavailable. An initial invocation failed before any turn because an unsupported reasoning-effort setting was requested; the successful retry made no substantive draft change.

## Next iteration

Iteration 003 axis: **release and attestation closure**. It must test the refined handoff against producer obligations, circularity, compatibility, packet identity, runtime ownership, and executable acceptance gates rather than repeat broad defect discovery.

<!-- level-up-complete -->
