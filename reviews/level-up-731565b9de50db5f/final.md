# Loop2 v0.5.0 Level Up Review

Run: `731565b9de50db5f`
Result: **bounded convergence**

## Executive summary

Loop2 v0.5.0 is materially better than v0.4.0. It resolves the earlier package
identity contradiction, separates verdict from disposition, preserves
structured INVALID results, records terminal multi-target outcomes, aligns the
Python floor, expands deterministic fixtures, improves lifecycle closure, and
documents unequal support lanes and verifier limits.

The new review found that the package has moved from first-order contract
breakage to second-order enforcement and assurance issues. The most important
new finding is not a fixture gap: the deterministic checker executes the whole
untrusted `ledger.sql` before validation without an SQLite authorizer. An
in-memory main database does not prevent `ATTACH` or other SQLite capabilities
from reaching the filesystem, so the checker does not currently uphold its own
read-only/untrusted-input boundary.

The remaining v0.5.1 scope is smaller and sharper than the previous upgrade:

1. constrain untrusted SQL execution;
2. make schema/default assurance canonical;
3. close transition-state and Phase-07 mutation enforcement gaps;
4. define blocked/suspended cause consistency;
5. add bounded objection, invalidation, and residual structural fixtures;
6. correct phase-status, PowerShell-host, recovery, and ABSENT documentation.

## Subject, objective, and boundary

- Subject: `C:\Users\nabradl\Repos\tools\copilot-skills\loop2`.
- Repository: `https://github.com/nabradl_microsoft/tools.git`.
- Branch/revision: `main` at
  `ab37db1f5917bbee63e2cc850d6cf4e24b175135`.
- Worktree: dirty, with the reviewed v0.5.0 package represented by tracked
  modifications and untracked package files.
- Final identity: 305 files; identity-manifest SHA-256
  `d6fa6309b86e15e2913013b56c374a7fe34cb6997a4397c18cfd4adff29060de`.
- Objective: improve Loop2 reliability and review performance.
- Objective type: desired-subject-state.
- Constraints: read-only review; untrusted subject evidence; no subject
  execution, dependency installation, service start, or subject writes.
- Governing Level Up snapshot: SHA-256
  `2afba9862ac94149f202f19773370ac890107d3051b3cd6fdf42b696217b01e8`.

## Convergence

Full convergence is unavailable because confirmed subject defects remain open
against the desired-subject-state objective. The untrusted-SQL finding also
affects the non-waivable read-only/untrusted-input constraint.

The run reaches **bounded convergence after one iteration**. The open findings
have been independently validated, the subject did not drift across evidence
windows, and further progress requires implementation and regression testing
rather than another review axis. No risk acceptance or waiver was applied.

The separate rules-only convergence checker returned `conformant` for the exact
adjudication draft.

## What improved from v0.4.0

| Prior v0.4.0 area | v0.5.0 result |
|---|---|
| CRLF/LF payload and manifest contradiction | Resolved with package-wide LF policy, v0.5.0 identity, and matching authenticated payload |
| Verdict, NULL/NONE/VOID ambiguity | Resolved through schema-v2 verdict disposition |
| Malformed ledger tracebacks | Resolved through structured INVALID diagnostics and guarded conversions |
| Disconnected lifecycle and weak completion closure | Materially improved with ordered phase/version connectivity and completed-run checks; state continuity remains open |
| Missing partial-batch outcomes | Resolved through per-target terminal result records |
| Python floor mismatch | Resolved for Bash installer and verifier at Python 3.10+ |
| Weak smoke assertions | Materially improved across batch, race, installed-version, and result-record cases |
| Support-lane and durability overclaims | Resolved through explicit Bash, Windows PowerShell, PowerShell-on-Unix, and verifier lanes |
| Sparse checker fixtures | Expanded substantially; objection and invalidation cases remain absent |
| Recovery/remnant ambiguity | Materially improved; several emitted refusal states still lack runbooks |

The v0.4.0 review identified broad correctness and packaging work. The v0.5.0
review confirms most of that work landed and exposes narrower defects created
or revealed by the stronger checker surface.

## Validated findings

### F1 — Untrusted ledger SQL can escape the intended read-only boundary

**IDs:** `i001-p5-sol-001`.

`tests/check_ledger.py` creates an in-memory connection and calls
`executescript` on the complete packet SQL before schema validation. No SQLite
authorizer or capability allowlist is installed. `:memory:` limits the main
database location; it does not prohibit attachment, detachment, unsafe pragmas,
or other filesystem-affecting SQLite operations.

**Effect:** the deterministic checker cannot currently claim a read-only
untrusted-input boundary. This is the highest-priority finding.

### F2 — Schema assurance has three drifting representations

**IDs:** `i001-p5-sol-002`, `i001-p5-claude-001`,
`i001-p5-sol-003`, `i001-p5-claude-002`.

Normative DDL, generated fixture DDL, and checker `REQUIRED_*` metadata are
maintained separately. Their table and column sets are substantially aligned,
but generator DDL omits normative defaults and the checker never inspects
`PRAGMA table_info.dflt_value`.

**Effect:** a structurally different omission/default contract can be certified
as conformant.

### F3 — Transition state continuity is documented but unenforced

**IDs:** `i001-p5-sol-004`, `i001-p5-claude-003`,
`i001-p5-claude-004`.

Adjacent rows are connected on phase and version, not state. Current state
labels include destination/action prose, so a correct fix requires canonical
edge or state mapping rather than raw string equality. REVISE recognition and
detailed validation also use separate predicates that can drift.

### F4 — Mutation-bearing apply units can be recorded outside Phase 07

**IDs:** `i001-p5-sol-005`, `i001-p5-claude-005`.

Non-planned units in phases without a phase-specific prerequisite can use a
generic earlier-PASS fallback. An applied unit in `09-final-record` can
therefore satisfy checker logic despite the normative no-mutation rule.
Planned-row shape is already represented and should not be rejected without a
separate contract basis.

### F5 — Blocked and suspended cause consistency is undefined

**IDs:** `i001-p5-sol-006`, `i001-p5-claude-007`.

Run statuses admit `blocked` and `suspended`, and the schema contains
`suspended_reason`, but no rule requires or reconciles a cause with capability,
resource, evidence, authority, or run state. Operator-initiated suspension is
not currently normative and must not be silently introduced.

### F6 — Important deterministic branches still lack direct fixtures

**IDs:** `i001-p5-sol-007` through `i001-p5-sol-009` and merged Claude
counterparts.

- objection lineage/reference and open-objection gate behavior have no direct
  fixtures;
- invalidation references and nonzero invalidated-pass accounting have no
  direct fixtures;
- selected cohort and scratchpad path/heading behavior have residual coverage
  gaps; model substitution already has meaningful coverage and should not be
  duplicated.

These are structural assurance findings. Objection material correctness,
freshness, independence, semantic evidence truth, provenance, and model
identity beyond recorded labels remain outside deterministic verification.

### F7 — Documentation needs three precise corrections

**IDs:** `i001-p5-sol-010` through `i001-p5-sol-012` and merged Claude
counterparts.

- `loop2_phases.status` is opaque and not currently deterministically
  validated; vocabulary omission alone does not prove it is non-normative.
- Unsupported direct `install.ps1` invocation fails at the host `#requires`
  boundary before guaranteed installer JSON or a classified installer exit
  code. The exact "13-error" counterfactual is not packaged-test evidence.
- Recovery guidance is absent for code 14 as well as 15, 16, 17, and 19.
  Code 20 currently conflates `--verify` refusal with neutral `--list`
  classification.

## PR-ready change specification

### P0 — Constrain ledger SQL capabilities

**Affected:** `tests/check_ledger.py`, `tests/test_ledger_checker.py`, fixture
generator and isolated invalid-input fixtures.

**Change:**

- install an SQLite authorizer before executing packet SQL;
- allow only the statement and object capabilities required to create and
  populate the in-memory ledger;
- deny attachment/detachment, extension loading, unsafe pragmas, and
  filesystem-writing operations;
- return a stable structured INVALID code such as
  `ledger_unsafe_statement`;
- add benign prohibited-statement fixtures, such as an in-memory ATTACH
  attempt, without creating external files;
- treat text scanning only as defense in depth, never the primary control.

**Success:** prohibited capabilities fail before execution with no external
artifact; all canonical packets and 40 current checker tests remain valid.

**Non-goals:** semantic SQL analysis, hostile-local tamper resistance, or
proving evidence truth.

### P1 — Canonical schema and default assurance

**Affected:** `SKILL.md`, checker schema metadata, fixture generator, schema
tests.

**Change:**

- designate one canonical structural DDL source;
- derive or equivalence-check checker and generator consumers;
- compare columns, primary keys, nullability, and normalized defaults through
  SQLite metadata;
- add isolated wrong/missing-default tests;
- avoid exact SQL formatting and `IF NOT EXISTS` text equality.

**Success:** intentional drift in any non-canonical consumer fails; canonical
schema-v2 packets pass unchanged.

### P2 — State, mutation, and lifecycle enforcement

**Affected:** transition, apply-unit, run, capability, and resource validators;
normative `SKILL.md` rules; fixtures/tests.

**Change:**

- define semantic state continuity for adjacent transitions;
- single-source REVISE recognition;
- reject mutation-bearing, non-planned apply units outside `07-execute`;
- preserve planned rows only where explicitly allowed;
- define accepted blocked/suspended causes using existing normative concepts;
- require coherent cause and run/resource/capability/evidence records.

**Success:** state-only discontinuity, Phase-09 applied units, and reasonless
blocked/suspended packets fail precise diagnostics; existing valid flows pass.

### P3 — Bounded assurance fixtures

**Affected:** fixture generator, generated fixture packets, checker tests, exact
README inventory.

**Change:**

- add approximately four to six objection lifecycle/gate scenarios;
- add two to three invalidation reference/accounting scenarios;
- add only genuinely uncovered scratchpad/cohort/model structural negatives;
- retain exact code/location assertions and avoid branch-complete testing.

**Success:** each retained structural rule has at least one positive and one
isolated negative where appropriate, without another uncontrolled fixture
expansion.

### P4 — Correct operational and contract documentation

**Affected:** `README.md`, `SKILL.md`, and the unsupported-engine installer
comment.

**Change:**

- describe phase status as opaque/not currently checked without assigning new
  semantics;
- describe the PowerShell host boundary and remove or qualify the untested
  numeric parser claim;
- add inspect-first, lane-neutral guidance for UNSUPPORTED, mixed refusal, race,
  SOURCE_INVALID, and OWNED_OTHER;
- split ABSENT documentation by verb: verify refusal versus list
  classification; state that no destructive cleanup is needed.

**Success:** operators can classify every emitted terminal state without
inferring false parity or performing unsafe cleanup.

## Recommended sequence

1. P0 untrusted SQL capability boundary.
2. P2 Phase-07 mutation and transition-state enforcement.
3. P1 canonical schema/default assurance.
4. P2 blocked/suspended cause taxonomy.
5. P3 targeted fixtures.
6. P4 documentation corrections.

## Dissent and rejected scope

- Exact SQL text equality was rejected as brittle.
- Literal equality of current state prose was rejected; semantic mapping is
  required.
- Inventing operator suspension was rejected.
- Rejecting all planned non-07 rows was rejected without a contract basis.
- Exhaustive checker branch coverage was rejected.
- A new PowerShell wrapper was rejected absent an explicit structured-parity
  requirement.
- Byte-identical cross-platform receipt order, stronger unsupported
  PowerShell-on-Unix guarantees, automatic recovery, and false lane parity
  remain out of scope.

## Coverage and saturation

- Subject manifest: 305 files, 831,046 bytes.
- Thirteen core files, 447,695 bytes, were read in full.
- 292 deterministic generated fixture artifacts, 383,351 bytes, were excluded
  by the declared generated-artifact rule; their generator was read in full,
  and selected fixture ledgers were inspected during validation where required.
- Phase 1 used three fresh, path-disjoint researchers.
- Phase 2 used three independent validators and reconciled the prior v0.4.0
  review as history only.
- Phase 3 used two fresh scopers.
- Phase 4 independently validated every retained recommendation; two
  wrong-repository responses were discarded and corrected or replaced.
- Phase 5 used GPT-5.6 Sol and Claude Opus 5; every scope item received an
  evidence-bearing challenge or failed challenge.
- Phase 6 used three fresh validators and a separate rules-only convergence
  checker.
- One iteration was sufficient because open findings require implementation,
  not another research axis.

## Remaining uncertainty

- No review phase modified or executed the subject.
- SQLite capability confinement must be demonstrated by safe regression tests.
- Platform race, crash, and unsupported-host behavior remain bounded by the
  documented support lanes.
- Deterministic checks cannot prove semantic evidence truth, objection
  correctness, authorship, provenance, freshness, independence, model identity
  beyond labels, or hostile-local integrity.
- Host-provided artifact durability, access control, transcript retention, and
  deletion guarantees are unverified.

## Outcome

Loop2 v0.5.0 is a meaningful improvement over v0.4.0 and is much closer to a
release-quality orchestration package. It is not yet at the desired subject
state because its checker can execute capabilities outside the claimed
read-only boundary and still under-enforces several normative lifecycle rules.
The specification above is the bounded, evidence-backed v0.5.1 handoff.

<!-- level-up-complete -->
