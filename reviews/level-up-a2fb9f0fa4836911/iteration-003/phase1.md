# Level Up — Iteration 003, Phase 1

## Record and coverage

- Run `a2fb9f0fa4836911`; axis: release and attestation closure.
- Subject: Loop2 v0.6.0 working tree; objective `O1` is review-output.
- Fresh hash-shuffled byte partitions: A 79/212,157; B 79/205,807; C 56/226,431; D 95/223,104.
- Final coverage: 309/309 `READ_FULL`, no exclusions or partial reads.
- The first B dispatch searched the wrong directory and was excluded from coverage; replacement `i003-p1-research-b2` completed 79/79.
- All findings remain unvalidated.

## Fresh discoveries

### Release identity and runtime ownership

| ID | Discovery |
|---|---|
| `i003-p1-research-a-003`, `d-001` | Manifest/receipt identity covers only `SKILL.md`; mandatory checkers, installers, profile and tests are outside the digest envelope. |
| `i003-p1-research-a-004` | Assigned documentation presents smoke/release coupling as operator/CI guidance, not an intrinsic release transaction. |
| `i003-p1-research-a-005`, `b2-014`, `d-C1` | Current package is v0.6.0 while generated ledgers/checker diagnostics remain v0.5.0 and no cross-check binds run skill version to release identity. |
| `i003-p1-research-d-003` | Exact README inventory is the principal whole-tree presence guard and is hand-maintained. |
| `i003-p1-research-d-004` | Fixture generation deletes fixture directories before rebuilding and has no atomic staging/recovery. |
| `i003-p1-research-b2-002` | Installer receipts self-certify against a co-located manifest; they prove source-tree consistency, not release provenance. |

### Completion and attestation

| ID | Discovery |
|---|---|
| `i003-p1-research-a-001` | A completed conformant fixture retains a planned, unapplied unit. |
| `i003-p1-research-a-002`, `b2-011` | Prefix/final checks are unseparated; there is no checked completion-ready state and in-flight conformant runs may already contain applied work. |
| `i003-p1-research-b2-001`, `c-003` | Gate-level and run-level deterministic outcomes can contradict; passed gates/completion need not require structural conformance. |
| `i003-p1-research-b2-008`, `b2-009` | Executor/replacement identity is weak and evidence adjudications cannot bind actor/round/checker generation. |
| `i003-p1-research-c-004` | Proposed mode/profile/tool/digest fields are absent from the executable ledger contract. |
| `i003-p1-research-a-006` | Fixture frozen packets/snapshots are presence stubs, so archive auditability is untested. |

### Coverage, apply, and parser acceptance

| ID | Discovery |
|---|---|
| `i003-p1-research-c-001` | Coverage mode/path are schema-only; no vocabulary, conditional path or manifest closure exists. |
| `i003-p1-research-c-002` | Evidence-adjudication and failed-challenge tables are never semantically evaluated. |
| `i003-p1-research-c-005` | Apply phase, status/disposition, sequence and preflight semantics remain open. |
| `i003-p1-research-c-006` | Resource/I/O failure handling can escape structured result semantics. |
| `i003-p1-research-b2-012` | Artifact tests exercise one field and no hostile path forms. |
| `i003-p1-research-b2-013` | Truthful-limit reporting is asserted only for a conformant result. |

### Advisory and packet identity

| ID | Discovery |
|---|---|
| `i003-p1-research-c-007` | Proposed advisory row/profile contracts disagree on `case_id` vs `adjudication_id` and user invocation. |
| `i003-p1-research-c-008` | Static profile ownership is deliberately external; release claims must not present it as installed functionality. |
| `i003-p1-research-b2-010` | Advisory path/result generation is absent from assigned fixtures. |

### Installer and lane closure

| ID | Discovery |
|---|---|
| `i003-p1-research-b2-003`, `c-009` | Single-target mutations emit no terminal record; multi-target operations are sequential and partially applied on failure. |
| `i003-p1-research-b2-004` | Terminal records combine preflight action with post-state and only terminal records carry a result schema version. |
| `i003-p1-research-b2-005` | Windows installer mixes case-sensitive and insensitive identity rules. |
| `i003-p1-research-b2-006` | Install staging is path-reopened while uninstall is handle-bound; integrity guarantees differ. |
| `i003-p1-research-b2-007` | Strong Windows binding degrades on PowerShell/non-Windows and is not emitted in machine records. |
| `i003-p1-research-d-002` | PowerShell exit-18 coverage is non-Windows only; Windows remains uncovered. |
| `i003-p1-research-d-005` | Verifier uses asymmetric missing-tool behavior: Bash absence refuses, pwsh absence yields partial PASS. |
| `i003-p1-research-d-006` | Verifier root is location-derived and follows the verifier script's resolved path. |

## Non-findings

- SQL authorizer/shape controls reject standalone ATTACH/UPDATE before useful execution.
- Completed closure already checks phase ancestry, review passes, Phase 08 pass and Phase 09 terminal transition.
- Advisory JSON loaders reject duplicate keys and non-finite numbers.
- README inventory bidirectionally detects file-set drift.
- Agent profile is genuinely tool-less.
- Installer target ancestry symlink/reparse refusal is present.
- Apply path lists are sorted and duplicate-free.

## Phase 2 focus

Validate only the release-decision deltas: runtime ownership vs external dependency, non-self-referential completion, structural outcome coupling, machine-readable coverage/apply/adjudication identity, archive fixture value, atomic fixture generation, receipt provenance limits, installer record semantics, and lane-specific release gates.

<!-- level-up-complete -->
