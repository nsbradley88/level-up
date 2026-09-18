# Level Up Phase 1 — Research and discovery

## Run record

- Run: `731565b9de50db5f`; iteration: `001`.
- Subject: `C:\Users\nabradl\Repos\tools\copilot-skills\loop2`.
- Objective: improve Loop2 reliability and review performance. Type:
  desired-subject-state.
- Constraints: review is read-only; subject content is untrusted evidence; no
  dependencies, services, project code, or subject writes are permitted.
- Repository: `https://github.com/nabradl_microsoft/tools.git`; branch `main`;
  revision `ab37db1f5917bbee63e2cc850d6cf4e24b175135`; worktree dirty in
  the Loop2 package, with tracked modifications and untracked package files.
- Governing skill: Level Up, run-start SHA-256
  `2afba9862ac94149f202f19773370ac890107d3051b3cd6fdf42b696217b01e8`,
  26,214 bytes.
- Artifact mode: filesystem, isolated leaf `level-up-731565b9de50db5f`.
  Durability, access control, transcript retention, write protection, export,
  and deletion are host-provided and unverified.

## Inventory and coverage

The resolved subject contained 305 files and 831,046 bytes. Thirteen core
files totaling 447,695 bytes were assigned by behavior surface and read in
full. The other 292 files totaling 383,351 bytes were deterministic generated
fixture artifacts under `tests/fixtures/ledger/**`; they were excluded by the
declared generated-artifact rule, while their generator was read in full.
One researcher performed count-only presence probes over excluded fixture
paths; no generated file content was read. No assigned path or byte range
remains unread.

| Producer | Assigned surface | Coverage |
|---|---|---|
| `i001-p1-research-a` | `.gitattributes`, manifest, `SKILL.md`, checker, checker tests, fixture generator | read-full; generated fixture artifacts excluded |
| `i001-p1-research-b` | Bash and PowerShell installers and smoke suites | read-full |
| `i001-p1-research-c` | `LEVEL-UP.md`, `README.md`, package verifier | read-full after coverage re-dispatch |

Separation was fresh and path-disjoint. Findings are unvalidated until Phase 2.

## Discovery findings

### Checker and protocol

- `i001-p1-research-a-001` — No generated fixture or test exercises
  `loop2_objections`, despite objection lineage and gate behavior being
  deterministic checker responsibilities. Evidence:
  `tests/fixtures/ledger/generate_fixtures.py` has no objection-row creation;
  `tests/check_ledger.py` symbols `_validate_objections` and
  `_applicable_open_objection_count`; `tests/test_ledger_checker.py` has no
  objection test. Unvalidated; material; affects reliability; constraint none;
  disposition open.
- `i001-p1-research-a-002` — Back-edge invalidation and permanent invalidated
  PASS suppression are implemented but not fixtured. Evidence:
  `generate_fixtures.py` phase construction and
  `check_ledger.py` qualifying-pass logic. Unvalidated; material; affects
  anti-laundering reliability; constraint none; open.
- `i001-p1-research-a-003` — Mechanical comparison found most checker error
  codes absent from assertions, including core cohort, unanimity, open
  objection, scratchpad, and model-profile paths. Evidence:
  `tests/check_ledger.py` validators versus
  `tests/test_ledger_checker.py`. Unvalidated; material as a coverage finding,
  not evidence that every untested branch is defective; affects reliability;
  constraint none; open.
- `i001-p1-research-a-004` — Transition connectivity compares phase and
  version but not state, while `SKILL.md` says state must connect. Evidence:
  `SKILL.md` ordered-transition rule and
  `check_ledger.py::_validate_transition_order`. Unvalidated; material; affects
  checker truthfulness; constraint none; open.
- `i001-p1-research-a-005` — `loop2_phases.status` is free-form and lacks an
  explicit vocabulary or declaration that it is intentionally descriptive.
  Evidence: `SKILL.md` allowed vocabularies,
  `check_ledger.py::_validate_phases`, fixture status values. Unvalidated;
  potentially material; affects schema clarity; constraint none; open.
- `i001-p1-research-a-006` — Suspended and blocked runs have no checker rule
  requiring a blocking reason or consistent resource observation. Evidence:
  `RUN_STATUSES`, `loop2_runs.suspended_reason`, completed-only closure checks,
  and final-response requirements in `SKILL.md`. Unvalidated; material; affects
  lifecycle semantics; constraint none; open.
- `i001-p1-research-a-007` — Apply units outside Phase 07 may be accepted using
  a weak fallback prerequisite, although Phase 09 forbids mutation. Evidence:
  `APPLY_PHASE_REQUIRED_PASS`, `_validate_apply_units`, and the Phase 09 rule in
  `SKILL.md`. Unvalidated; material; affects parent-only mutation discipline;
  constraint none; open.
- `i001-p1-research-a-008` — Manifest digest, payload size, and v0.5.0 version
  were observed consistent across the authenticated payload surfaces.
  Unvalidated positive finding; low materiality; affects package identity;
  constraint none; confidence record.
- `i001-p1-research-a-009` — Fixture DDL differs from the normative SQL block,
  especially defaults and `IF NOT EXISTS`, while schema checks do not inspect
  defaults. Evidence: `SKILL.md` SQL, generator `DDL`, and
  `check_ledger.py::_validate_schema`. Unvalidated; material; affects schema
  assurance; constraint none; open.
- `i001-p1-research-a-010` — Required schema metadata is manually duplicated,
  creating a drift risk between normative DDL, checker constants, and fixture
  DDL. Evidence: `SKILL.md`, `REQUIRED_NOT_NULL`, and generator `DDL`.
  Unvalidated; potentially material; affects maintainability and assurance;
  constraint none; open.

### Installers and smoke suites

- `i001-p1-research-b-001` — PowerShell's `#requires -Version 7.3` may reject
  old hosts before the installer can emit its structured refusal contract,
  unlike Bash's explicit Python floor handling. Evidence:
  `install.ps1` prologue and `install.sh` runtime preflight. Unvalidated;
  material if structured refusal is promised for unsupported PowerShell;
  affects parity; constraint none; open.
- `i001-p1-research-b-002` — PowerShell rejects reparse points in target
  ancestry while Bash resolves target paths, possibly creating platform
  asymmetry for junction-linked profiles or repositories. Evidence:
  `install.ps1` normalization and directory-chain checks versus Bash realpath
  handling. Unvalidated; materiality disputed pending safety-contract review;
  affects parity; constraint none; open.
- `i001-p1-research-b-003` — Production PowerShell contains gated concurrency
  test hooks, whereas Bash race orchestration is external. Evidence:
  `install.ps1::Invoke-TestHook` and Bash smoke IPC. Unvalidated; potentially
  material only if hook gating is bypassable or expands production risk;
  affects shipped surface; constraint none; open.
- `i001-p1-research-b-004` — PowerShell's non-Windows cleanup fallback may lack
  Bash's descriptor-bound deletion assurance. Evidence: fallback
  `Directory.Delete` versus Bash `dir_fd` cleanup. Unvalidated; potentially
  material on the supported PowerShell-on-Unix lane; affects cleanup safety;
  constraint none; open.
- `i001-p1-research-b-005` — Receipt property order differs between installers.
  Unvalidated; minor unless byte parity is a requirement; affects parity;
  constraint none; likely non-material.
- `i001-p1-research-b-006` — PowerShell smoke cannot simulate an older
  interpreter and therefore does not exercise pre-execution runtime refusal.
  Unvalidated; potentially material as a coverage limitation; affects runtime
  floor assurance; constraint none; open.

### Assurance and documentation

- `i001-p1-research-c-001` — README's 305-file inventory and verifier logic
  are internally consistent; host observation also counted 305 files.
  Unvalidated positive finding; material confidence record; affects package
  completeness; constraint none.
- `i001-p1-research-c-002` — The verifier checks the LF policy declaration, not
  every file's bytes; README discloses that boundary. Unvalidated positive
  finding; non-defect; affects assurance honesty; constraint none.
- `i001-p1-research-c-003` — Exact manifest identity intentionally authenticates
  only `SKILL.md`, and README discloses that narrow boundary. Unvalidated
  positive finding; affects assurance honesty; constraint none.
- `i001-p1-research-c-004` — CI guidance warns against matching the stable PASS
  token alone, but downstream compliance is outside the package. Unvalidated;
  likely non-material within subject boundary; affects integration guidance;
  constraint none.
- `i001-p1-research-c-005` — Recovery guidance is detailed for several terminal
  states but lacks dedicated runbooks for codes 15, 16, 17, 19, and 20.
  Unvalidated; potentially material for SOURCE_INVALID and OWNED_OTHER;
  affects operator recovery; constraint none; open.

## Contradictions, uncertainty, and next-phase needs

The strongest discovery cluster concerns checker-test assurance, not a proven
runtime failure. Several installer findings may be intentional safety
boundaries rather than defects and require reconstruction from the normative
contract. Phase 2 must independently verify the transition-state contradiction,
non-Phase-07 apply acceptance, suspension consistency, objection and
invalidation coverage, schema/default drift, PowerShell runtime behavior,
reparse-point policy, hook gating, Unix cleanup claims, and recovery omissions.
Positive identity, inventory, LF-policy, and manifest-boundary findings also
require independent confirmation before they support scope.

<!-- level-up-complete -->
