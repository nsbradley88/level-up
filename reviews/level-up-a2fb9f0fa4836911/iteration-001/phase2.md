# Level Up — Iteration 001, Phase 2

## Run record

- Run: `a2fb9f0fa4836911`
- Phase: independent research validation
- Subject: `C:\Users\nabradl\Repos\tools\copilot-skills\loop2`
- Objective `O1` (`review-output`): produce an evidence-backed review and PR-ready change specification for the current Loop2 codebase.
- Constraints: read-only subject review; untrusted subject evidence; GPT-5.6 Sol participates in Phase 5 adversarial review.
- Governing Level Up snapshot: SHA-256 `6e33cb093323e955107c732971d4eedf340cebb1d9c101ed6d01dda45224f4fc`.
- Phase 1 aggregate identity: SHA-256 `e26c3b482bf2646632e8e0938c5e3d7bf6f51f187cf63a368efd442f0168cf93`.
- Pre-validation subject identity: all 309 manifested files remained present and SHA-256-equal; no drift detected.
- Artifact-mode limitations remain as recorded in Phase 1.

## Validation method and independence

Four fresh validators independently reconstructed neutral claim groups from primary subject evidence. They received claim text and starting evidence but not Phase 1 ratings or dispositions:

| Validator | Model | Scope |
|---|---|---|
| `i001-p2-validate-a` | Claude Opus 5 | ledger causality, lifecycle, cohorts, and apply units |
| `i001-p2-validate-b` | GPT-5.6 Sol | version provenance, artifacts, packaging, and advisory boundary |
| `i001-p2-validate-c` | Claude Opus 5 | installer hooks, platform guarantees, links, and case behavior |
| `i001-p2-validate-d` | GPT-5.6 Sol | SQL tests, fixture generation, smoke lanes, and verifier behavior |

No validator executed project code or modified the subject. Validators inspected relevant surrounding implementation, tests, fixtures, and documentation rather than accepting starting citations. The main agent resolved classification boundaries from their primary-evidence reports. Agreement is not used as proof.

## Validated material record

### `i001-p1-research-a-001` — transitions are not causally bound to gates

- Validation: `supported`; material.
- Evidence: `_validate_transitions` is called without gates, ballots, active cohorts, or qualifying passes (`tests/check_ledger.py:1063-1078`). Forward legality is topology-only (`:2096-2098`). `REVISE` legality and lineage checks do not inspect unanimous `REVISE` ballots or a revision packet (`:2101-2106,2289-2345`); `revision_packet_path` is declared but not validated.
- Effect: `O1`; non-waivable constraint `none`.
- Residual uncertainty: completed-run closure requires some qualifying review passes, but does not bind the pass to the transition edge/version/round. If transition rows are intended as syntax-only history, the protocol must say so; current event labels assert causal predicates.
- Disposition: open.

### `i001-p1-research-a-002` — transition chains ignore state continuity

- Validation: `supported`; material.
- Evidence: chain checks compare only phase/version endpoints (`tests/check_ledger.py:2267-2277`). The conformant fixture contains unequal adjacent `to_state`/`from_state` values and is asserted conformant (`tests/fixtures/ledger/conformant/ledger.sql:240-242`; `tests/test_ledger_checker.py:59-61`).
- Effect: `O1`; constraint `none`.
- Residual uncertainty: the protocol defines closed transition labels but no explicit state-normalization map, so the repair requires a normative state model rather than string equality alone.
- Disposition: open.

### `i001-p1-research-a-003` with alias `i001-p1-research-c-003` — required producer cohorts can be absent

- Validation: both `supported`; material; merged under `i001-p1-research-a-003`.
- Evidence: cohort validation checks only groups that exist (`tests/check_ledger.py:1729-1770`), while producer-completion transitions do not count agent rows (`:2087-2093`). Conformant fixtures claim four scratchpads for Phase 01/03/05 but contain no corresponding producer rows (`tests/fixtures/ledger/conformant/ledger.sql:216-247`; `conformant_completed_run/ledger.sql:217-252`). Protocol cohort requirements appear at `SKILL.md:947-948,1003-1005,1018-1019`.
- Effect: `O1`; constraint `none`.
- Residual uncertainty: none affecting the omission.
- Disposition: open.

### `i001-p1-research-a-004` — non-passed gate semantics are incompletely reconciled

- Validation: `partially supported`; material.
- Supported portion: ballot verdicts and `pass_count == 4` are reconciled only when `gate_status == 'passed'` (`tests/check_ledger.py:1935-1943,1990-2006`). `revise`, `mixed`, and `pending` can carry contradictory ballots or counters.
- Unsupported overstatement: non-passed states are not wholly unchecked. Void disposition, candidate-round pairing, objection count, and phase/gate status receive broader checks (`:1918-1924,1947-1962,1974-1989,2007-2014`).
- Effect: `O1`; constraint `none`.
- Residual uncertainty: the intended semantics of in-flight `pending` and `mixed` states are not specified tightly enough to derive a complete rule.
- Disposition: open for the supported portion.

### `i001-p1-research-a-006` — lifecycle status fields are not coherently enforced

- Validation: `supported`; material.
- Evidence: `loop2_phases.status` is required but never substantively read or vocabulary-checked; run status validation is limited (`tests/check_ledger.py:1020-1039,1222-1288`). `suspended_reason`, resource state, current phase, transition state, and completion are not generally reconciled. The completed conformant fixture retains review/candidate-running-style phase statuses (`tests/fixtures/ledger/conformant_completed_run/ledger.sql:194,208-216`).
- Effect: `O1`; constraint `none`.
- Residual uncertainty: phase status may have been intended as advisory free text, but the schema and protocol do not declare that boundary.
- Disposition: open.

### `i001-p2-validate-a-001` with source subset `i001-p1-research-a-007` — child-table evidence is broadly unscoped to the sole run

- Validation: new independently derived finding; material. `i001-p1-research-a-007` is `supported` and merged into this superset.
- Evidence: explicit foreign-run rejection exists for transitions (`tests/check_ledger.py:2181-2190`) but not for capabilities, model slots, agents, gate results, apply units, resource observations, or checker results. Several validators iterate complete tables returned by `_rows()` without filtering to `run["id"]`.
- Effect: `O1`; constraint `none`.
- Residual uncertainty: some tables key later joins by `run_id`, reducing cross-run borrowing for specific checks; capabilities, slots, apply units, and checker-row counts remain directly exposed.
- Disposition: open.

### `i001-p1-research-a-008` — apply-unit invariants are incomplete

- Validation: `supported`; material.
- Evidence: `_validate_apply_units` accepts every recognized phase; only Phase 07 has a specific prerequisite (`tests/check_ledger.py:2347-2434`). `sequence` is shape-checked but not ordered or made unique, `preflight_state` is unused, and disposition/status relationships are weak. Phase 09 mutations can be structurally admitted despite `SKILL.md:712-714,1150-1156`.
- Effect: `O1`; constraint `none`.
- Residual uncertainty: none affecting the identified omissions.
- Disposition: open.

### `i001-p1-research-c-002` — completed reference fixture retains an undispositioned planned apply unit

- Validation: `supported`; material.
- Evidence: the run is completed while `unit-2` remains `planned` with null actual paths, disposition, and evidence (`tests/fixtures/ledger/conformant_completed_run/ledger.sql:194,259-261`). Planned rows bypass apply and artifact closure checks (`tests/check_ledger.py:2378-2385,2485-2498`), and tests deliberately accept planned/applied coexistence.
- Effect: `O1`; constraint `none`.
- Residual uncertainty: `SKILL.md:1145-1148` says every intended mutation must be accounted for, but the vocabulary does not explicitly say whether an abandoned plan may remain `planned`. The material defect is either fixture acceptance or specification ambiguity.
- Disposition: open.

### Version-compatibility cluster

- IDs: `i001-p1-research-a-005`, `i001-p1-research-b-006`, `i001-p1-research-c-004`, `i001-p1-research-d-003`.
- Validation: all `supported`; material; merged under `i001-p1-research-a-005`.
- Evidence: package identity is v0.6.0 (`SKILL.md:1-7`, `skill.manifest.json:1-5`), while fixture generation and all populated ledgers use `skill_version='0.5.0'` (`tests/fixtures/ledger/generate_fixtures.py:390-407`). Checker validation requires presence but does not enforce a compatibility policy and retains “normative v0.5.0” wording (`tests/check_ledger.py:389-405,965-975`). Tests assert ledger schema compatibility, not skill-version compatibility.
- Effect: `O1`; constraint `none`.
- Residual uncertainty: backward compatibility may be intended, but no accepted-version range, migration, or rejection rule is documented.
- Disposition: open.

### Missing not-checkable artifact cluster

- IDs: `i001-p1-research-b-001`, `i001-p1-research-d-004`.
- Validation: both `supported`; material; merged under `i001-p1-research-b-001`.
- Evidence: `not-checkable.md` is a required output (`SKILL.md:551-558`), generated ledgers record its path, but fixtures do not create it (`tests/fixtures/ledger/generate_fixtures.py:405-448`). `_validate_referenced_artifacts` omits `run["not_checkable_path"]` (`tests/check_ledger.py:2458-2510`), and positive fixtures pass.
- Effect: `O1`; constraint `none`.
- Residual uncertainty: some not-checkable properties also appear in summaries, but that does not validate the separately required recorded artifact.
- Disposition: open.

### `i001-p1-research-b-008` — restricted SQL boundary lacks broad regression coverage

- Validation: `supported`; material as a security-regression test gap, not as a demonstrated bypass.
- Evidence: `RestrictedSqlLoaderTests` contains direct negatives for `ATTACH` and `UPDATE` only (`tests/test_ledger_checker.py:98-124`). The implementation lexically admits transaction markers, `CREATE TABLE`, and `INSERT INTO`, then applies an allow-only SQLite authorizer and disables extensions (`tests/check_ledger.py:612-710`; contract `SKILL.md:536-543`).
- Effect: `O1`; non-waivable constraint: restricted untrusted-SQL boundary.
- Residual uncertainty: static inspection found no present bypass; authorizer action coverage is not exhaustively demonstrated by tests.
- Disposition: open as assurance depth, not implementation unsafety.

### `i001-p1-research-d-002` — fixture regeneration deletes every fixture subdirectory

- Validation: `supported`; material.
- Evidence: `tests/fixtures/ledger/generate_fixtures.py:783-786` recursively removes every directory under the fixture root with no allow-list, dry-run, or confirmation.
- Effect: `O1`; constraint `none`.
- Residual uncertainty: blast radius is confined to real subdirectories under the known fixture root; directory symlinks are likely to fail rather than traverse.
- Disposition: open.

### `i001-p1-research-d-006` — Bash smoke prerequisite is undocumented

- Validation: `supported`; material.
- Evidence: `tests/smoke_installer.sh:8-15` requires either an explicit sandbox parent or non-empty `TMPDIR`; README prerequisites omit both (`README.md:420-429`).
- Effect: `O1`; constraint `none`.
- Residual uncertainty: callers supplying the optional argument are unaffected.
- Disposition: open.

### `i001-p1-research-d-009` with qualified subset `i001-p1-research-d-005` — native smoke coverage is asymmetric

- Validation: `i001-p1-research-d-009` `supported` and material; `i001-p1-research-d-005` `partially supported`, not independently material, merged as a qualification.
- Evidence: Bash covers exit codes `0,1,2,10-17,19,20` but not 18; PowerShell's exit-18 case is non-Windows-only and lacks an analogous exit-1 case (`tests/smoke_installer.sh:985`; `tests/smoke_installer.ps1:837-865`). Windows race tests condition expected installer results on whether the OS permitted replacement, so they are not content-free, but can leave one guarded branch unexecuted on a given host (`tests/smoke_installer.ps1:872-1001`).
- Effect: `O1`; non-waivable constraint: documented installer exit/race contract.
- Residual uncertainty: some asymmetry is explicitly documented and platform-specific; remediation should target native contract gaps, not artificial test parity.
- Disposition: open.

## Validated non-material record

These claims are retained for traceability but do not drive Phase 3:

| IDs | Validation | Determination |
|---|---|---|
| `i001-p1-research-b-002` | supported | Single-file installation is an explicit packaging boundary; README states checker/profile registration remains external. Standalone portability is limited, but no manifest defect is shown. |
| `i001-p1-research-b-003` | partially supported | The environment-gated hook mechanism, exclusive file creation, and bounded wait are real. The implied attacker/security-boundary framing is contradicted: both variables are process-owner controlled, writes are `CreateNew`, names are allow-listed, timeout is bounded, and README documents the test-only boundary. |
| `i001-p1-research-b-004` | supported | Non-Windows PowerShell is weaker than Bash, but this is explicitly documented as a best-effort fallback rather than the supported Unix lane. |
| `i001-p1-research-b-005` | supported | Bash enforces link count and PowerShell does not; documentation assigns different guarantees to the lanes and no privilege-crossing consequence was established. |
| `i001-p1-research-b-007` | supported | Advisory validation is structural and producer-echo-based by design; truth, completeness, model identity, and runtime isolation are explicitly not claimed. |
| `i001-p1-research-b-009` | supported | Case-insensitive Windows set comparison differs from Bash, but subsequent exact path and digest checks preserve refusal behavior; impact is conditional and non-mutating. |
| `i001-p1-research-c-001` | partially supported | A literal proposal/profile conflict exists, but current verification requires `user-invocable: true`; `false` is stale proposal text, not the executable contract. |
| `i001-p1-research-c-005` | supported | “Rollback tests” is ambiguous relative to documented non-atomic behavior, but maintained README and smoke behavior disclose the actual contract. |
| `i001-p1-research-d-001` | supported | Ordinary Python can create caches that fail exact inventory, but README prescribes `python -B` and explains the clean-tree boundary. |
| `i001-p1-research-d-005` | partially supported | Tests can miss an interference branch on a host that blocks replacement, but their expectation is conditioned on the observed fixture result; merged into material `d-009`. |
| `i001-p1-research-d-007` | supported | `PACKAGE_VERSION` is redundantly passed to a verifier that does not consume it; maintenance-only issue. |
| `i001-p1-research-d-008` | supported | Source-pattern verification is brittle, but deliberately fail-closed and separately backed by smoke behavior; maintenance-only issue. |
| `i001-p1-research-d-010` | supported | `$Matches` shadowing and sentinel 999 are real but theoretical under the current exit-code contract. |

No Phase 1 material claim was classified `contradicted` or `unverifiable` in full. Unsupported portions and non-material security framing are explicitly removed from downstream scope.

## Historical reconciliation

Available history is incomplete. No prior filesystem Level Up aggregate for Loop2 was available in the run store. The subject's `LEVEL-UP.md` is a read-only historical v0.3.0 recommendation package, not fresh evidence for v0.6.0.

Relations to that history:

- `i001-p1-research-a-001`, `a-003/c-003`, and `a-004` retest the prior contract that parent transitions require strict 4/4 consensus and complete fixed cohorts. The current checker implementation does not fully enforce those assertions; the prior recommendation did not resolve them mechanically.
- `i001-p1-research-a-008` and `c-002` retest the prior contract that Phase 09 is synthesis-only and all mutations are frozen/reviewed in Phase 08. Current apply-unit checks and the completed fixture do not fully encode that contract.
- Installer findings `b-003` through `b-005` and `b-009` concern guarantees added or documented after the v0.3.0 Linux-first package. Validation establishes these as honest lane boundaries rather than regressions.
- Version compatibility, the missing not-checkable artifact, the advisory checker, the restricted SQL loader, and current fixture/smoke issues are v0.6.0-era surfaces and therefore new relative to the available v0.3.0 history.
- Prior experiment results show static advisory checking can reduce context and credit use, but they do not validate any current ledger invariant and add no weight to these findings.

Historical convergence beyond this limited record is unavailable. Prior agreement is not treated as evidence.

## Phase 2 outcome

Validated evidence establishes eleven material change themes:

1. bind transitions to the exact qualifying gate and revision evidence;
2. define and enforce lifecycle-state continuity;
3. require producer cohorts when producer completion is asserted;
4. derive all gate statuses and counters from ballots or explicitly define in-flight semantics;
5. enforce run scoping across every child table;
6. define coherent run/phase/apply lifecycle closure;
7. define and enforce current/compatible skill versions in fixtures and checker behavior;
8. validate the required not-checkable artifact;
9. broaden hostile SQL regression coverage while preserving the existing restricted loader;
10. make fixture regeneration deletion-bounded;
11. close documented native smoke prerequisite and contract-coverage gaps.

These themes are eligible for Phase 3 scoping. Non-material observations remain recorded but cannot independently justify work.

## Phase 3 needs

Fresh scopers should derive outcome-level recommendations, affected areas, sequencing, non-goals, reversal, and observable success checks. They must avoid:

- converting the ledger into proof of semantic truth, model identity, authorship, or hostile-local security;
- bundling documented packaging/lane differences into false parity requirements;
- treating untested SQL cases as a proven loader bypass;
- using string equality as a lifecycle model without defining valid state transitions;
- introducing automatic rollback or multi-target atomicity contrary to the maintained installer contract.

<!-- level-up-complete -->
