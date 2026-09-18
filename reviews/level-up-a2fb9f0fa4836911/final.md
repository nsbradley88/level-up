# Loop2 v0.6.0 — PR-ready reliability and attestation upgrade

## Executive summary

Loop2's refusal-first installers and structural ledger checker have strong foundations, but the v0.6.0 package cannot yet provide the release and run-record guarantees its normative skill describes. The main defects are not semantic model quality; they are representational:

- the mandatory deterministic checker is not installed;
- prefix and final checker results are self-referential and cannot coexist;
- transitions, gates, replacement rounds, completion and apply effects are not causally closed;
- several required tables, paths and coverage claims are structurally ignored;
- packet identity and artifact containment are incomplete and platform-dependent;
- SQL/error handling has supported-version and framing gaps;
- advisory contracts are caller-defined rather than bound per adjudication;
- core checker unit suites are absent from PR gating;
- fixture generation is destructive-first;
- release/version, installer and documentation surfaces drift.

This specification resolves those issues without claiming evidence truth, authorship, model identity, independence, hostile-local integrity, rollback success or deployment verification.

## Subject and convergence

- Subject: `C:\Users\nabradl\Repos\tools\copilot-skills\loop2`
- Repository revision observed: `ab37db1f5917bbee63e2cc850d6cf4e24b175135`
- Worktree: heavily modified/untracked; revision alone does not pin reviewed content.
- Final content identity: 309 files, 867,499 bytes, zero SHA-256 drift against the run manifest.
- `SKILL.md`: SHA-256 `761f0955e663e8b21a0adb2853fce16d7e7b32799031fdf24ef06d03f29d374c`.
- Governing Level Up snapshot: SHA-256 `6e33cb093323e955107c732971d4eedf340cebb1d9c101ed6d01dda45224f4fc`.
- Objective: `O1` review-output.
- Result: **converged for review-output** after three complete iterations.

Confirmed defects remain open as implementation work; this document does not claim the subject is fixed.

## Required changes

### 1. Freeze a reviewable baseline and make runtime ownership explicit

First import/freeze the current 309-file reviewed tree as a baseline before functional migration.

Evolve the manifest/installers/receipts to own typed payloads:

- `SKILL.md`;
- deterministic checker;
- shared ledger/contract version data;
- advisory-result structural validator.

Install them under the isolated skill target with digest/size/version checks and exact uninstall ownership. Keep advisory profile registration external and optional; never mutate a shared host registry.

If typed ownership is rejected, the only acceptable alternative is an explicit pinned host-checker preflight with resolver, command, digest, contract version and fail-closed availability result. Do not retain “mandatory but unavailable.”

### 2. Establish one version contract

Use one machine-readable source for:

- skill version;
- ledger schema version;
- deterministic result contract;
- advisory contract;
- manifest/receipt schema.

The current checker supports the current ledger schema only. Older schemas produce `INVALID/unsupported_schema_version`. In-flight runs pin the checker identity/version recorded at preflight. Archived-schema audit is a non-goal unless a versioned checker is deliberately retained.

Remove v0.5.0 diagnostics/fixture identity from the v0.6.0 release or label explicit compatibility fixtures and test the compatibility matrix.

### 3. Replace self-referential completion with detached attestations

Define a canonical packet member manifest containing sorted portable relative paths, byte sizes and SHA-256 digests. It excludes itself, contracts, results and execution receipts.

Use this acyclic graph:

1. packet manifest identifies evidence bytes;
2. contract binds packet-manifest digest and adjudication universe;
3. deterministic/advisory result binds packet, contract and checker identity;
4. execution receipt binds result bytes and observed runtime metadata;
5. run outcome binds the completion-ready packet and mandatory deterministic receipt.

The core run reaches `completion-ready`, not `completed`. Final completion requires a detached deterministic result that is structurally conformant. Non-conformant, indeterminate, missing or invalid results prevent completion. Advisory absence/fallback never blocks completion.

Digests prove byte self-consistency only; they do not prove authorship, truth, model use, isolation or hostile-host continuity.

### 4. Make lifecycle causality authoritative

Derive the active head from the terminal connected transition, never `MAX(version)`.

Transitions must:

- chain exact phase, version and normalized state;
- cite an exact gate/cause/check receipt;
- reject stale, sibling, void, mixed or unrelated gates;
- retain append-only historical branches without allowing them to qualify.

Forward gates require:

- exact candidate phase/version/round;
- four declarations from one cohort generation;
- a structurally conformant deterministic check receipt over that generation;
- zero applicable open objections;
- resolved resource/evidence predicates.

REVISE declarations must bind the same target phase and immutable revision-packet digest. Back-edges must match those four declarations and invalidate affected downstream ancestry.

### 5. Treat replacement as a new review round

Any validator replacement starts a new round and requires four fresh declarations.

Use a parent-generated non-null assignment/attempt identity. Replacement is a reciprocal immediate predecessor/successor relation over run, phase, version, round, slot and attempt. Preserve failure-before-artifact with an explicit inactive state and conditional scratchpad requirements; never fabricate a missing artifact.

Inactive artifacts that exist must still agree with their immutable verdict, candidate and round.

### 6. Load and validate the complete ledger

Every child row must belong to the sole run. Load and validate evidence-adjudication and failed-challenge tables.

Add exact vocabularies and references for:

- phase/run/gate states;
- objection candidate coordinates and raised-in coordinates;
- evidence/challenge generation and disposition;
- checker-type-specific result values;
- coverage mode;
- check status.

Unknown check names must be an internal error, not silently filtered. Report each check as evaluated, not-applicable or indeterminate with row counts.

### 7. Normalize coverage without overclaiming

For total coverage, require structured items with one disposition per manifested path:

- `READ_FULL`;
- `READ_PARTIAL` with read/unread ranges;
- `EXCLUDED` with a named rule.

Reject duplicates, overlaps, unknown items and undisclosed unread ranges. Targeted mode cannot claim total coverage.

Keep evidence truth/completeness, live-copy provenance and content adequacy in NOT_CHECKABLE. Do not add a generalized claim/evidence graph in this release.

### 8. Close apply plans and effects

Represent the design allowlist separately from observed effects.

Apply units:

- belong only to the active Phase 07 plan;
- have unique contiguous sequence;
- cite the active design/gate generation;
- carry validated preflight state;
- use an explicit status/disposition matrix.

Support:

- mutation units with nonempty allowlists and exact expected/actual effects;
- verification-only units with empty effects;
- halted-before-write units with empty effects and failure evidence.

Completion-ready rejects planned, halted, unreviewed or undispositioned active units. Back-edges require explicit physical disposition for prior effects.

### 9. Harden packet paths and restricted SQL

Use one packet-input resolver for the packet root, ledger, manifest and every artifact/digest input.

Reject:

- traversal;
- absolute, drive-relative, UNC, device and ADS forms;
- case-fold/trailing-dot/trailing-space/reserved-name collisions;
- symlink/reparse components and special files;
- hardlinks according to an explicitly documented policy.

Hostile-local tamper resistance remains NOT_CHECKABLE.

Retain relational SQL interchange, but replace prefix-only framing with a bounded tokenizer grammar:

- one BEGIN;
- required CREATE statements;
- literal VALUES-only INSERTs;
- one COMMIT;
- no SELECT, expressions, comments or extra statements.

Normalize ledger/scratchpad I/O, decoding, `sqlite3.Error` and `sqlite3.Warning` into fixed `INVALID` diagnostics. Bound file, statement, row, list and string sizes. Never emit raw untrusted SQLite text or host paths.

### 10. Release advisory contract v2

Define:

- bounded typed ID grammar;
- per-adjudication candidate/constraint/missing-information universes;
- shared mandatory NOT_CHECKABLE minimum;
- explicit zero-adjudication/not-run mode;
- separate packet and contract digests;
- direct CLI/stdout/stderr/exit tests.

Enforce the existing execution receipt fields: selected mode, requested profile, profile digest, requested/resolved model labels and source, exposed tools, packet/result/contract digests and contract version.

The profile remains optional, tool-less and non-authoritative. Remove unnecessary hard model pinning or define it as a host-overridable default. Structural validity never upgrades advisory output into semantic proof.

### 11. Make fixture generation recoverable

The generator must:

- default to compare-only;
- require explicit `--write`;
- generate into a fresh staging tree;
- verify complete expected bytes before commit;
- mutate only a generated-name allowlist;
- refuse unknown files, directories and links;
- use a journal/commit marker with deterministic resume or rollback;
- support injected failure after each commit step.

It must never recursively delete unknown fixture directories.

### 12. Make acceptance and CI executable

The repository workflow is a required external integration deliverable. Add a path-filtered `pull_request` trigger.

Run:

- ledger checker unit suite;
- advisory validator unit suite;
- fixture regeneration compare;
- package verifier with parsed completeness/refusal fields;
- producer-to-checker integration over one independently captured real packet;
- Bash smoke;
- PowerShell/non-Windows smoke;
- native Windows smoke and checker path/collision cases.

Generated fixtures prove checker behavior only; they do not prove real producer compatibility.

For every change, record:

| Field | Requirement |
|---|---|
| Setup | fixture or filesystem state |
| Invocation | exact command and lane/OS |
| Exit | expected numeric exit |
| Result | expected result token/status |
| Diagnostics | exact code/location set |
| Postcondition | filesystem, row, digest or residue state |

### 13. Close installer/reporting deltas

- Use exact logical package names, but apply Windows filesystem identity rules for target discovery/deduplication; reject collisions and noncanonical on-disk spellings.
- Document/version terminal records as preflight action plus post-state/effect. Do not silently change multi-target-only emission.
- Document `USERPROFILE` precedence and dangling/linked personal-root behavior.
- Publish exact per-lane executed exit-code/race coverage; never claim parity.
- Add hook-free Bash exit-18 coverage: install, make the parent `skills` directory non-writable while leaving the target writable, uninstall as non-root, assert payload/receipt removal followed by parent-relative `rmdir` failure, restore permissions, then assert residue.
- Report unsupported FIFO capability explicitly and fail required release lanes closed.

### 14. Reconcile documentation

Demote `proposed_upgrade.md` in place to a dated, explicitly non-normative design record. Correct its contradictory profile/result examples or point only to canonical artifacts.

Reconcile README and SKILL wording for:

- mandatory deterministic checker ownership;
- optional external advisory profile;
- verifier Bash/pwsh prerequisites;
- receipt self-consistency versus provenance;
- lane-specific recovery and coverage;
- archived-schema policy.

## Release sequence

1. Freeze/import the reviewed baseline.
2. Add PR trigger, unit suites and compare-only fixture gate.
3. Select and implement package-owned deterministic tooling and canonical versions.
4. Ship one atomic ledger-schema release for lifecycle, generations, coverage, evidence and apply closure.
5. Ship packet resolver, SQL/error hardening and detached attestations.
6. Ship advisory v2.
7. Ship installer/reporting/documentation corrections.

Each step must be independently reviewable and keep the package verifier green. Schema/contract changes, fixtures, checker constants, SKILL DDL/prose, manifest identity and tests land in the same commit.

## Coverage and confidence

- Iteration 001: 309/309 files; core structural, lifecycle, apply, artifact, SQL and smoke defects.
- Iteration 002: 309/309 files; identity, replacement, advisory ingress, containment, attestation and release boundaries.
- Iteration 003: 309/309 files; release ownership, acyclic attestation, executable gates and final cardinality decisions.
- Final identity revalidation: 309/309 SHA-256 matches.
- GPT-5.6 Sol served as adversarial reviewer in every completed adversarial cycle.
- Claude Opus 5 provided independent adversarial and validation coverage.

## Residual limits

- Review was static and read-only; subject code/tests/installers were not executed.
- The working tree was dirty/untracked; the content manifest, not Git revision, pins evidence.
- The repository workflow is outside the 309-file subject root and was treated as external integration evidence.
- Dynamic convergence checkers were instructed to use no tools; host-enforced isolation was unavailable.
- Filesystem observations do not prove continuity or exclude hostile local mutation/ABA behavior.
- Final recommendations do not prove semantic correctness, evidence truth, model identity, independence, provenance, authorship, rollback success or deployment state.

<!-- level-up-complete -->
