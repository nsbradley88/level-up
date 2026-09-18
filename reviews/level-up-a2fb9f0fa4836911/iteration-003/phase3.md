# Level Up — Iteration 003, Phase 3

## Candidate final scope

### `i003-p3-scope-001` — Own and version mandatory runtime contracts

Package the deterministic checker and shared machine-readable contract/schema as typed owned payloads, or define a mandatory pinned host-provided checker preflight. Keep advisory profile registration external and optional. One machine source drives skill, ledger, checker and advisory versions. Schema/key changes release atomically; archived-schema support is explicit rather than accidental.

### `i003-p3-scope-002` — Use completion-ready packets and detached attestations

Freeze an immutable `prefix` or `completion-ready` packet manifest that lists canonical relative paths, sizes and digests. Checker results and execution metadata are detached receipts binding packet, checker, contract and result digests; they never occur inside their own input. Core run state stops at completion-ready; final completed outcome requires a structurally conformant mandatory deterministic receipt. Advisory remains optional and outcome-neutral.

### `i003-p3-scope-003` — Make active ancestry, gates and generations authoritative

Represent one active run head and append-only phase ancestry. Forward/back transitions cite exact gate/cause identities. Gates cite one candidate/cohort generation and a structurally conformant deterministic check. Replacement creates a new cohort generation with four redeclarations; exact predecessor identity is reciprocal. Objections, evidence adjudications and failed challenges carry round/generation identity and remain immutable.

### `i003-p3-scope-004` — Normalize coverage and evidence records

Define structured coverage items/ranges and explicit targeted/total modes. Load and validate every child table, reject foreign-run rows, and report evaluated/not-applicable/indeterminate with row counts. Consequential claims link to structured evidence or explicit missing-evidence records; truth/completeness/provenance remain NOT_CHECKABLE.

### `i003-p3-scope-005` — Close apply plans through explicit effects

Apply units belong to active Phase 07 plans. Store plan allowlists separately from observed effects; support verification-only and halted-before-write empty effects. Enforce unique sequence, preflight/status/disposition matrices, exact active-design authorization, and no planned/unreviewed/undispositioned unit at completion-ready.

### `i003-p3-scope-006` — Harden packet and input boundaries

Use one portable, no-follow resolver for packet root, ledger/manifest and every input; reject drive/UNC/ADS, traversal, case/trailing-dot/reserved collisions, links/reparse points and special files under an explicit hardlink policy. Replace physical-line SQL framing with exact one-statement/VALUES-only restricted parsing or a strict data format. Normalize expected I/O/decoding/SQLite failures and bounded input limits into fixed `INVALID` reports.

### `i003-p3-scope-007` — Version advisory v2 around per-adjudication bindings

Use bounded typed IDs scoped per adjudication, a shared mandatory NOT_CHECKABLE minimum, explicit zero/not-run mode, direct CLI/exit tests and separate evidence-packet and contract digests. Record requested profile, profile digest, requested/resolved model labels/source, exposed tools, packet/result/contract digests and mode in a durable execution receipt. Preserve tool-less/non-authoritative limits.

### `i003-p3-scope-008` — Make fixture and CI gates release-grade

Fixture generation defaults to compare-only, writes through a fresh staging tree, replaces only generated names after complete verification, and never recursively deletes unknown directories. CI runs ledger/advisory suites, regeneration check, package verifier, both smoke lanes and schema/contract equivalence. Verifier acceptance parses completeness/refusal fields under an explicit required-lane policy.

### `i003-p3-scope-009` — Close installer/reporting deltas proportionately

Unify Windows target/name case policy, document/version preflight-action versus post-state/effect semantics, and retain documented multi-target-only terminal records unless intentionally changed. Publish exact per-lane exit coverage. Add the hook-free Bash exit-18 permission-denial smoke case; report unsupported FIFO capability explicitly. Do not claim lane parity.

### `i003-p3-scope-010` — Reconcile shipped documentation

Demote `proposed_upgrade.md` to a dated non-normative design record or make its quoted profile/contract/ownership fields mechanically match delivered artifacts. Document Bash verifier prerequisites and runtime-tool ownership. Preserve explicit trust boundaries: receipts are self-consistency records, not provenance signatures.

## Ordering and compatibility

1. Add CI/fixture safety gates.
2. Decide runtime ownership and canonical version source.
3. Release schema/ledger changes 002–006 atomically.
4. Release advisory v2 and execution receipts.
5. Land installer/reporting/doc corrections.

No recommendation claims semantic truth, authorship, model identity, independence, hostile-local integrity, rollback success or deployment verification.

<!-- level-up-complete -->
