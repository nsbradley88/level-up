# Level Up — Iteration 001, Phase 3

## Run record

- Run: `a2fb9f0fa4836911`
- Phase: refinement and scope
- Subject: `C:\Users\nabradl\Repos\tools\copilot-skills\loop2`
- Objective `O1` (`review-output`): produce an evidence-backed review and PR-ready change specification.
- Governing Level Up snapshot: SHA-256 `6e33cb093323e955107c732971d4eedf340cebb1d9c101ed6d01dda45224f4fc`.
- Validated Phase 2 aggregate: SHA-256 `c78cd397c1ec9582c814d65b75bb9f32f928155333210999f1222265c39c1aa1`.
- Boundary: recommendations are design scope only. No subject change was made or executed.

## Scoping method and separation

Three fresh scopers consumed the validated Phase 2 record and primary source:

| Scoper | Model | Scope |
|---|---|---|
| `i001-p3-scope-a` | GPT-5.6 Sol | ledger causality, lifecycle, cohorts, run scoping, apply closure |
| `i001-p3-scope-b` | Claude Opus 5 | version policy, not-checkable artifact, SQL regression depth |
| `i001-p3-scope-c` | GPT-5.6 Sol | fixture cleanup and installer smoke reliability |

All recommendations remain `unvalidated`. Prior non-material findings were not promoted into work. The installed payload remains one file; advisory checking remains structural; installer lane differences remain explicit; no automatic rollback, semantic-truth proof, cryptographic provenance, or platform-parity project is proposed.

## Candidate change sequence

The proposed train is:

1. P0 foundational safety and identity: bounded fixture cleanup, single-run scoping, current version identity, required not-checkable artifact generation/checking.
2. P0 protocol semantics: deterministic gate derivation, evidence-backed canonical transitions, coherent lifecycle closure.
3. P1 execution and assurance: apply-unit invariants, skill-version enforcement, hostile-SQL regression depth, native installer smoke gaps.
4. P2 usability/coupling: Bash smoke invocation diagnostics and an optional NOT_CHECKABLE contract pin.

Recommendations are listed individually to preserve stable IDs. Dependencies identify the implementation order.

## P0 recommendations

### `i001-p3-scope-c-001` — deletion-bounded fixture regeneration

- Status: `unvalidated`.
- Sources: `i001-p1-research-d-002`.
- Desired outcome: regeneration removes only explicitly generator-owned direct-child fixture directories; unknown directories and link/reparse entries are never recursively removed.
- Benefit: eliminates silent loss of local or hand-authored packets while preserving deterministic regeneration.
- Affected areas: `tests/fixtures/ledger/generate_fixtures.py` cleanup path and focused tests in `tests/test_ledger_checker.py`.
- Mechanism: define and validate an explicit owned-name set before deletion; remove only matching direct children; reject symlink/reparse entries; preserve unknown directories.
- Alternatives: marker files or refuse on any unknown directory. The allow-list best preserves local extensions while bounding authority.
- Risks/tradeoffs: fixture names and retirement cleanup entries must be maintained.
- Dependencies: none; land before fixture-wide regeneration.
- Non-goals: transactionality, automatic rollback, or deleting unknown inventory.
- Reversal: remove the helper/owned-name set and associated tests; no format migration.
- Evaluator and success checks: unit tests in an isolated fixture root prove unknown sentinel preservation, owned replacement, link target preservation/refusal, and deterministic repeated generation.
- Qualification: deletion authority is limited to direct children of the fixed fixture root.

### `i001-p3-scope-a-001` — uniform single-run child scoping

- Status: `unvalidated`.
- Sources: `i001-p2-validate-a-001`, including `i001-p1-research-a-007`.
- Desired outcome: no foreign-run child row can satisfy, alter, or bypass validation for the sole declared run.
- Benefit: restores the packet's exactly-one-run boundary across every table.
- Affected areas: `tests/check_ledger.py` row loading/index construction and all child validators; fixture generator/tests.
- Mechanism: immediately after confirming one run, enumerate every table with `run_id`; emit `foreign_run_child` for each mismatched row with table/primary-key location; construct all downstream indices from same-run rows only. Foreign rows remain errors rather than being silently ignored.
- Alternatives: per-validator filtering risks omissions; SQL query filtering hides injected rows; foreign keys do not enforce a single-run packet.
- Risks/tradeoffs: a packet may report both foreign evidence and missing same-run evidence.
- Dependencies: none; precedes every semantic validator.
- Non-goals: multi-run packet support or evidence-truth proof.
- Reversal: remove the central scope stage atomically; do not leave partial filters.
- Evaluator and success checks: table-driven negatives inject a foreign row into every child table and prove it cannot satisfy capabilities, slots, cohorts, gates, apply units, artifacts, or checker closure; current positive fixtures remain conformant.
- Qualification: depends on retaining the documented exactly-one-run contract.

### `i001-p3-scope-b-001` — declare one normative skill-version policy

- Status: `unvalidated`.
- Sources: `i001-p1-research-a-005` and aliases `b-006`, `c-004`, `d-003`.
- Desired outcome: package, generated ledgers, checker output, and documentation agree on the producing version and accepted versions.
- Benefit: turns `skill_version` from decorative stale data into usable provenance.
- Affected areas: `SKILL.md`, `README.md`, `tests/fixtures/ledger/generate_fixtures.py`, regenerated ledgers, stale checker messages, manifest digest/size.
- Mechanism: declare a supported-version set whose only member is the current package version; generated fixtures stamp a single current-version constant; out-of-set records are later treated as rule-set-inapplicable. Remove “normative v0.5.0” text from current checker messages.
- Alternatives: label fixtures historical or remove the field. Both preserve ambiguity or lose provenance.
- Risks/tradeoffs: `SKILL.md` edits require manifest digest/size and smoke re-baselining.
- Dependencies: precedes `i001-p3-scope-b-002`.
- Non-goals: historical-ledger migration, per-version rule branching, or an implied backward-compatible range.
- Reversal: revert text, constant, generated fixtures, and manifest together.
- Evaluator and success checks: current fixtures stamp v0.6.0; current files contain no unintended v0.5.0 assertion; package verification and native smoke lanes pass after re-baseline.
- Qualification: if maintainers declare fixtures frozen historical evidence, Phase 4 must replace this with an explicit historical-corpus policy.

### `i001-p3-scope-b-004` — generate the required not-checkable artifact

- Status: `unvalidated`.
- Sources: `i001-p1-research-b-001`, alias `d-004`.
- Desired outcome: positive fixture packets contain the required `conformance/not-checkable.md` they record.
- Benefit: makes reference packets faithful to the protocol's assurance-boundary output.
- Affected areas: fixture generator and regenerated fixture directories.
- Mechanism: when a deterministic checker result is emitted, also emit `not-checkable.md` from the checker's stable NOT_CHECKABLE property set.
- Alternatives: hand-authored copies are rejected as drift-prone.
- Risks/tradeoffs: broad fixture churn; use bounded cleanup first.
- Dependencies: `i001-p3-scope-c-001`; precedes `i001-p3-scope-b-003`.
- Non-goals: machine judgment of content truth or prose adequacy.
- Reversal: revert generator output and regenerate.
- Evaluator and success checks: every fixture with a non-`not-run` deterministic row contains the file and its listed property IDs match the emitted checker boundary.
- Qualification: if fixtures intentionally model partial prefixes, trigger output from checker-row presence rather than run completion.

### `i001-p3-scope-b-003` — validate the required not-checkable artifact reference

- Status: `unvalidated`.
- Sources: `i001-p1-research-b-001`, alias `d-004`.
- Desired outcome: a packet cannot be structurally conformant after claiming but omitting its not-checkable disclosure.
- Benefit: protects the artifact that prevents structural output from being over-read as total assurance.
- Affected areas: `_validate_referenced_artifacts`, checker-result closure, `SKILL.md` checker-scope list, fixtures/tests.
- Mechanism: when a deterministic checker row exists with result other than `not-run`, require non-null `not_checkable_path` and resolve it through the existing safe artifact checker. Use a specific null-path code and existing missing-artifact code.
- Alternatives: schema-level `NOT NULL` would break legitimate prefixes; semantic content validation exceeds the boundary.
- Risks/tradeoffs: current positive fixtures fail until `b-004` lands.
- Dependencies: `i001-p3-scope-b-004`.
- Non-goals: authorship, adequacy, or completeness verification.
- Reversal: remove the two checks; no schema migration.
- Evaluator and success checks: negatives cover null and absent files; preflight/blocked prefixes without a checker row remain valid; positive packets pass.
- Qualification: trigger on checker-row presence, not completed status, unless Phase 4 establishes a different normative lifecycle.

### `i001-p3-scope-a-002` — derive every gate status and counter

- Status: `unvalidated`.
- Sources: `i001-p1-research-a-004`.
- Desired outcome: gate status and counters are deterministic projections of same-round ballots, objections, invalidation, and resource evidence.
- Benefit: prevents contradictory `pending`, `revise`, `mixed`, `suspended`, `void`, and `passed` assertions and gives transitions a trustworthy structural cause.
- Affected areas: gate schema/vocabulary in `SKILL.md`; `_validate_gate_results`; fixture generator/tests.
- Mechanism: derive counters from evidence; define precedence and exact predicates for all six statuses. `passed` requires four PASS and no blockers; `revise` requires four REVISE declarations agreeing on target plus an existing revision packet; `mixed` is a complete non-pending non-unanimous cohort; `pending` requires a launched cohort with incomplete declarations; `suspended` requires matching resource evidence; `void` requires no active cohort and all attempts void. Phase and gate rows must equal the derivation.
- Alternatives: validating only impossible combinations leaves independently asserted counters.
- Risks/tradeoffs: may require a coordinated schema revision for revision target/packet fields; status precedence becomes normative.
- Dependencies: `a-001`; precedes transition causes.
- Non-goals: semantic correctness of objections, evidence, or ballots.
- Reversal: revert schema, derivation, fixtures, and docs as a unit.
- Evaluator and success checks: positive fixtures for every status; negatives for contradictory counters/ballots, blockers, mismatched revision targets, and missing packets; absent current gate remains `INDETERMINATE`.
- Qualification: `pending` applies to a recorded launched cohort; wholly absent evidence remains missing evidence.

### `i001-p3-scope-a-003` — evidence-backed canonical transition machine

- Status: `unvalidated`.
- Sources: `i001-p1-research-a-001`, `a-002`, `a-003`, alias `c-003`.
- Desired outcome: each transition is a continuous canonical state edge bound to the exact structural evidence that permits it.
- Benefit: closes the highest-risk gap between protocol claims and mechanical conformance.
- Affected areas: `SKILL.md` transition/state/cohort schema; `_legal_transition`, `_validate_transitions`, order/revise checks, cohort indices; generator/tests.
- Mechanism: define stable state and event IDs plus a declarative transition-rule table covering topology, state edge, version rule, and required cause. Add exact cause references for gate phase/version/round and optional artifact. Producer completion requires an exact four-slot same-version cohort and scratchpads. Gate advance and revise cite the exact derived gate; revise also binds target, lineage, and packet. Adjacent states must be equal.
- Alternatives: raw current string equality preserves inconsistent prose; implicit latest-gate selection is ambiguous; separate rules duplicate semantics.
- Risks/tradeoffs: broad fixture and schema churn; current human-readable labels need migration to stable IDs.
- Dependencies: `a-001`, `a-002`.
- Non-goals: proving agent independence, scratchpad quality, evidence truth, or parent authority beyond recorded structure.
- Reversal: restore the prior table/schema atomically; never mix canonical and prose state systems.
- Evaluator and success checks: full forward and revise fixtures bind cohorts/gates/packets; negatives cover stale or wrong-round gates, missing/reused cohorts, wrong revision target, missing packet, and state discontinuity.
- Qualification: canonicalization changes labels and references, not the phase topology.

### `i001-p3-scope-a-005` — coherent run/phase/apply closure projection

- Status: `unvalidated`.
- Sources: `i001-p1-research-a-006`, `i001-p1-research-c-002`; consumes preceding validated defects.
- Desired outcome: run status, current phase, phase rows, transition endpoint, gate results, and apply units describe one coherent lifecycle snapshot.
- Benefit: prevents completion or suspension assertions from contradicting the durable record.
- Affected areas: `SKILL.md` status vocabularies; `_validate_phases`, `_validate_completed_run_closure`; generator/tests.
- Mechanism: define producer/review phase statuses and project run status/current phase from the terminal canonical transition. Require suspension reasons exactly for suspended state. Completion consumes the connected transition chain, bound gate results, producer cohorts, Phase 09 closure, checker/artifact closure, and terminal apply-unit status. Invalidated historical versions remain history but cannot satisfy current ancestry.
- Alternatives: treating phase status as advisory leaves a required field meaningless; deleting it is a larger incompatible change.
- Risks/tradeoffs: one inconsistency may yield multiple explicit errors; in-flight prefix fixtures need expansion.
- Dependencies: `a-001` through `a-004`, plus not-checkable closure.
- Non-goals: deployment state, semantic adequacy, or provenance proof.
- Reversal: remove projection/closure rules and restore vocabularies/fixtures together.
- Evaluator and success checks: positive preflight, running, candidate, review, suspended/resumed, and completed prefixes; negatives cover endpoint mismatch, completion without final state, suspension reason mismatch, stale gate, active terminal phase, missing cohort, and unresolved apply unit.
- Qualification: connected in-flight prefixes remain valid without later phases.

## P1 recommendations

### `i001-p3-scope-a-004` — apply-unit phase, order, status, and terminality rules

- Status: `unvalidated`.
- Sources: `i001-p1-research-a-008`, `i001-p1-research-c-002`.
- Desired outcome: apply rows represent one serial Phase 07 plan and no accepted/completed execution retains unresolved intent.
- Benefit: aligns execution accounting with the parent-only mutation contract.
- Affected areas: `SKILL.md` execution contract; `_validate_apply_units`; completed closure; generator/tests.
- Mechanism: permit apply units only in Phase 07; require positive unique contiguous sequences per version; enforce a status matrix for `planned`, `applied`, `reviewed`, and `halted`; allow an applied/reviewed prefix, optional halted row, then only planned rows; forbid later attempts after halt; require physical disposition for superseded changed units; require all accepted-version units reviewed before a passed Phase 08 gate or completed run.
- Alternatives: deleting unfinished plans hides intent. If intentional abandonment must persist, add explicit `cancelled` with reason/evidence rather than overloading `planned`.
- Risks/tradeoffs: current positive fixture semantics change; superseded execution histories need richer fixtures.
- Dependencies: `a-001` through `a-003`; consumed by `a-005`.
- Non-goals: executing mutations or automatic rollback.
- Reversal: restore the prior matrix and fixtures together.
- Evaluator and success checks: positives for in-flight planned suffix, completed reviewed units, and dispositioned superseded versions; negatives for wrong phase, sequence gaps, attempt after halt, missing preflight/evidence, review without exact Phase 08 pass, and completion with planned/applied units.
- Qualification: Phase 4 must decide whether an explicit `cancelled` terminal state is needed.

### `i001-p3-scope-b-002` — enforce the declared supported skill-version set

- Status: `unvalidated`.
- Sources: version cluster under `i001-p1-research-a-005`.
- Desired outcome: packets produced by unsupported protocol versions are rejected as rule-set-inapplicable.
- Benefit: prevents silent evaluation under the wrong protocol.
- Affected areas: `tests/check_ledger.py`, checked-list reporting, a negative fixture, tests, and `SKILL.md` scope.
- Mechanism: add `SUPPORTED_SKILL_VERSIONS` containing the current version and an early validator adjacent to schema-version validation. Emit `unsupported_skill_version` and result `INVALID`, naming found/supported values; record that the check ran.
- Alternatives: warning-only leaves the claim unenforced; semver parsing is unnecessary; a single equality is viable but harder to widen intentionally.
- Risks/tradeoffs: each version bump must deliberately update checker/tests.
- Dependencies: `b-001`.
- Non-goals: migration or best-effort evaluation of unknown versions.
- Reversal: remove the validator, constant, fixture, and tests; no format change.
- Evaluator and success checks: unsupported version is exactly `INVALID`; current fixtures remain conformant; a pin test binds supported version to package identity.
- Qualification: widen only after differential evidence proves the relevant protocol tables are compatible.

### `i001-p3-scope-b-005` — deepen hostile-SQL regression coverage

- Status: `unvalidated`.
- Sources: `i001-p1-research-b-008`.
- Desired outcome: every documented SQL prohibition and both loader layers have deterministic regression evidence.
- Benefit: protects a high-value untrusted-input boundary without changing a loader for which no bypass is known.
- Affected areas: `RestrictedSqlLoaderTests` only unless a test discovers a real defect.
- Mechanism: add table-driven negatives for statement classes, obfuscated `ATTACH`, non-Loop2 and quoted targets, incomplete statements, non-UTF-8 input, and cases shaped to reach the authorizer/extension layer. Assert exact public error, `INVALID`, and no filesystem side effect.
- Alternatives: fuzzing is deferred; production hardening without evidence is rejected.
- Risks/tradeoffs: more tests and some internal-layer coupling.
- Dependencies: independent.
- Non-goals: claiming a bypass, returning to `executescript`, or proving hostile-local security.
- Reversal: tests only.
- Evaluator and success checks: every `SKILL.md:536-543` prohibition maps to an executing test; currently unused error codes are exercised; temporarily disabling either layer makes at least one local test fail.
- Qualification: any discovered admission becomes a new implementation defect requiring fresh scope.

### `i001-p3-scope-c-003` — close native installer smoke contract gaps

- Status: `unvalidated`.
- Sources: `i001-p1-research-d-009`, qualified subset `d-005`.
- Desired outcome: applicable native exit/race contracts have deterministic evidence, and environment-dependent branches are labeled rather than overclaimed.
- Benefit: reduces platform-specific regressions while preserving honest lane boundaries.
- Affected areas: `install.sh`, both smoke runners, README, and verifier if a new Bash test seam is pinned.
- Mechanism: add a narrowly gated Bash synchronization point after payload unlink and before receipt removal to deterministically exercise exit 18; add a Windows PowerShell exit-1 apply-failure case; label each guarded Windows race outcome as replacement-blocked or replacement-observed/refused and report tested exit codes/branches.
- Alternatives: probabilistic stress racing, mandatory both-branch coverage per host, or artificial cross-platform parity are rejected.
- Risks/tradeoffs: one more inactive production test seam; single-host branch reachability remains environment-dependent.
- Dependencies: native Linux Bash and Windows PowerShell evaluation environments.
- Non-goals: proving every race, hostile-local security, rollback, atomicity, or Windows/POSIX parity.
- Reversal: remove each seam with its test/verifier assertion.
- Evaluator and success checks: Bash deterministically returns 18 after confirmed partial mutation while preserving replacement content; Windows returns 1 for induced failure with no installer residue; summaries identify actual guarded branch and never claim unexecuted coverage.
- Qualification: Bash exit 18 is the native POSIX case; non-Windows PowerShell remains fallback-only.

## P2 recommendations

### `i001-p3-scope-c-002` — explicit Bash smoke sandbox configuration

- Status: `unvalidated`.
- Sources: `i001-p1-research-d-006`.
- Desired outcome: smoke invocation clearly states and consistently handles its sandbox-parent requirement.
- Benefit: avoids immediate opaque failure for documented/manual invocations.
- Affected areas: `tests/smoke_installer.sh` startup and README prerequisites/examples.
- Mechanism: replace parameter-expansion failure with an actionable usage diagnostic when neither positional parent nor `TMPDIR` is set; document precedence, permissions, unique-child cleanup, and both invocation forms.
- Alternatives: documentation-only repair or implicit global temp fallback. The explicit contract is safer.
- Risks/tradeoffs: minimal startup complexity.
- Dependencies: none.
- Non-goals: changing production prerequisites or matching PowerShell temp discovery.
- Reversal: restore parameter expansion and remove docs.
- Evaluator and success checks: missing configuration exits before sandbox creation with usage; explicit parent overrides `TMPDIR`; documentation shows both forms.
- Qualification: caller must be able to create an exclusive child under the chosen parent.

### `i001-p3-scope-b-006` — pin NOT_CHECKABLE data to the documented minimum

- Status: `unvalidated`.
- Sources: adjacent to material `i001-p1-research-b-001`; informed by non-material `i001-p1-research-b-007`.
- Desired outcome: the emitted structural-assurance boundary cannot silently shrink below the documented minimum.
- Benefit: cheap regression protection for Loop2's honesty boundary.
- Affected areas: checker tests and stable anchors in `SKILL.md`.
- Mechanism: a test parses or otherwise pins the documented minimum property IDs and asserts the checker set is a superset.
- Alternatives: generate prose from code would violate the single-file/source boundary.
- Risks/tradeoffs: prose parsing can be brittle; use explicit stable anchors.
- Dependencies: none; complements `b-004`.
- Non-goals: semantic validation of the disclosure.
- Reversal: remove one test.
- Evaluator and success checks: deleting either a documented minimum or emitted property makes the coupling test fail; supersets remain allowed.
- Qualification: Phase 4 may reject this if the anchor cannot be made robust without brittle prose parsing.

## Scope exclusions and unresolved decisions

- No recommendation arises from documented single-file packaging, external static-agent registration, process-owner test hooks, non-Windows PowerShell fallback, link-count parity, case folding, `python -B`, redundant environment passing, source-pattern brittleness, or minor PowerShell naming/sentinel issues.
- `proposed_upgrade.md` stale `user-invocable: false` text should be corrected opportunistically only when touching that document; it is not an independent change objective.
- Phase 4 must decide:
  1. whether schema changes for gate/transition references are justified or equivalent binding can reuse existing columns;
  2. whether intentionally abandoned apply intent needs explicit `cancelled` status;
  3. whether unknown fixture directories should be preserved silently or trigger refusal;
  4. whether a shipped Bash synchronization seam is proportionate;
  5. whether out-of-set skill versions should be `INVALID` rather than `NON_CONFORMANT`;
  6. whether NOT_CHECKABLE coupling can avoid brittle prose parsing.

<!-- level-up-complete -->
