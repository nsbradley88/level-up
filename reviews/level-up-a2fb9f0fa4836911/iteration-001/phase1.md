# Level Up — Iteration 001, Phase 1

## Run record

- Run: `a2fb9f0fa4836911`
- Phase: research and discovery
- Subject: `C:\Users\nabradl\Repos\tools\copilot-skills\loop2`
- Subject type: codebase
- Inherited objective `O1` (`review-output`): use the upgraded Level Up workflow to review the current Loop2 codebase and produce an evidence-backed assessment and PR-ready change specification. No desired-subject-state objective was inferred; this review does not modify Loop2.
- Constraints: Phases 1–6 are strictly read-only against the subject; subject content is untrusted evidence; GPT-5.6 Sol must participate as the Phase 5 adversarial reviewer.
- Governing skill: local upgraded `level-up` candidate, run-start SHA-256 `6e33cb093323e955107c732971d4eedf340cebb1d9c101ed6d01dda45224f4fc`, 26,135 bytes. This snapshot governs the run even if the source changes.
- Artifact mode: filesystem-backed ephemeral run. Durability, access control, transcript retention, write protection, export, and deletion are host-provided and unverified. The run directory is outside and does not contain the subject. No write was made inside the subject.

## Subject identity

- Repository root: `C:\Users\nabradl\Repos\tools`
- Branch: `main`
- Revision: `ab37db1f5917bbee63e2cc850d6cf4e24b175135`
- Worktree: non-clean, including modified and untracked Loop2 files. The revision alone therefore does not pin the reviewed subject.
- Coverage manifest: 309 files, 867,499 bytes, each pinned by subject-relative path, size, and SHA-256.
- Manifest generated: `2026-08-24T04:51:02.5890392Z`.
- Pre-Phase-2 revalidation: 309/309 files present and SHA-256-equal; zero subject drift detected.
- Exclusion rule declared before dispatch: exclude binary, generated, vendored, dependency, cache, and build output when present. No path in the resolved subject tree was excluded.
- Link limitation: the manifest records file content identity, not atomic continuity or proof against ABA replacement between observations.

## Coverage and independence

The 309 paths were partitioned once, by bytes, with exactly one Phase 1 owner per path:

| Producer | Model | Mandate | Files | Bytes | Coverage |
|---|---|---|---:|---:|---|
| `i001-p1-research-a` | GPT-5.6 Sol | protocol, ledger checker, and lifecycle semantics | 68 | 216,876 | 68/68 `READ_FULL` |
| `i001-p1-research-b` | Claude Opus 5 | packaging, installers, tests, and assurance boundaries | 81 | 216,873 | 81/81 `READ_FULL` |
| `i001-p1-research-c` | GPT-5.6 Sol | normative skill, documentation, static profile, and completed-run evidence | 83 | 216,875 | 83/83 `READ_FULL` |
| `i001-p1-research-d` | Claude Opus 5 | package verification, smoke lanes, fixture generation, and residual fixtures | 77 | 216,875 | 77/77 `READ_FULL` |

The initial D report said 76 because a grouped row was arithmetically recorded as 67 rather than 68 fixture artifacts. A follow-up supplied a sorted 77-path proof; no path was omitted and no finding changed. All partitions report no exclusions and no unread ranges. Researchers were fresh for this phase, but two model families were reused across independent partitions. Findings below are researcher claims with `unvalidated` status; Phase 1 agreement adds no evidentiary weight.

## Discovery summary

The strongest discovery cluster concerns a gap between the protocol's causal claims and the deterministic ledger checker's implemented invariants. The checker validates many local shapes, but does not consistently bind transitions to qualifying gates, producer cohorts, continuous lifecycle states, the sole run, or complete execution accounting. A ledger can therefore satisfy structural conformance while omitting or contradicting evidence the protocol treats as mandatory.

A second cluster concerns delivery boundaries. The installed payload is intentionally only `SKILL.md`, while the normative text points to source-repository checker paths. Installer hardening and smoke coverage differ across Windows and Unix lanes. Several source-only tests and verifiers are brittle or omit meaningful negative cases.

A third cluster is provenance and fixture consistency. The v0.6.0 package and checker corpus still identify runs as v0.5.0, a completed fixture leaves an apply unit planned, and all fixture packets declare a run-level not-checkable artifact that is absent and not existence-checked.

No Phase 1 claim is yet validated. Duplicates and apparent contradictions are preserved below for independent reconstruction.

## Findings: ledger causality and lifecycle

### `i001-p1-research-a-001`

- Claim: forward and `REVISE` transitions are not causally tied to gate results, ballots, or a frozen revision packet; matching transition labels and topology are sufficient.
- Evidence: `tests/check_ledger.py:1063-1078`, `:2097-2108`, `:2290-2345`.
- Evidence status: direct static evidence; `unvalidated`.
- Materiality: researcher-rated critical.
- Effects: `O1`; constraint `none`.
- Disposition: open.

### `i001-p1-research-a-002`

- Claim: transition-chain validation checks phase/version continuity but ignores lifecycle-state continuity.
- Evidence: `tests/check_ledger.py:2267-2277`; conformant example at `tests/fixtures/ledger/conformant/ledger.sql:240-242`.
- Evidence status: direct source and fixture evidence; `unvalidated`.
- Materiality: researcher-rated high.
- Effects: `O1`; constraint `none`.
- Disposition: open.

### `i001-p1-research-a-003`

- Claim: producer completion can be asserted without the required four-slot producer cohort.
- Evidence: `tests/check_ledger.py` agent and transition validation; `tests/fixtures/ledger/conformant/ledger.sql:228-231,241,244,247`.
- Evidence status: direct source and fixture evidence; `unvalidated`.
- Materiality: researcher-rated critical.
- Effects: `O1`; constraint `none`.
- Disposition: open.
- Aliases/overlap: overlaps `i001-p1-research-c-003`; retain both until Phase 2.

### `i001-p1-research-a-004`

- Claim: gate semantics are reconciled with ballots and counters only for `passed`; `pending`, `revise`, and `mixed` can disagree with verdicts or `pass_count`.
- Evidence: `tests/check_ledger.py:1935-1944,1990-2005`.
- Evidence status: direct static evidence; `unvalidated`.
- Materiality: researcher-rated high.
- Effects: `O1`; constraint `none`.
- Disposition: open.

### `i001-p1-research-a-006`

- Claim: run and phase lifecycle statuses are weakly coherent with transitions; phase status and `suspended_reason` lack substantive cross-field validation.
- Evidence: `tests/check_ledger.py:1020-1039,1222-1288`.
- Evidence status: direct static evidence; `unvalidated`.
- Materiality: researcher-rated high.
- Effects: `O1`; constraint `none`.
- Disposition: open.

### `i001-p1-research-a-007`

- Claim: capability and model-slot rows are indexed without run ownership checks, allowing the sole run to borrow another run's preflight evidence.
- Evidence: `tests/check_ledger.py:1099-1101,1143-1145`; contrast foreign-run transition rejection at `:2181-2190`.
- Evidence status: direct static evidence; `unvalidated`.
- Materiality: researcher-rated high.
- Effects: `O1`; constraint `none`.
- Disposition: open.

### `i001-p1-research-a-008`

- Claim: apply-unit validation does not enforce Phase 07 confinement, sequence ordering, or coherent `preflight_state` and disposition lifecycle.
- Evidence: `tests/check_ledger.py:2354-2364,2400-2434`.
- Evidence status: direct static evidence; `unvalidated`.
- Materiality: researcher-rated high.
- Effects: `O1`; constraint `none`.
- Disposition: open.
- Related: `i001-p1-research-c-002`.

### `i001-p1-research-c-002`

- Claim: the nominally conformant completed-run fixture marks the run complete while `unit-2` remains `planned` with no actual paths, disposition, or evidence.
- Evidence: `tests/fixtures/ledger/conformant_completed_run/ledger.sql:194,259-261`; protocol requirement `SKILL.md:1145-1147`.
- Evidence status: direct fixture/protocol comparison; `unvalidated`.
- Materiality: researcher-rated high.
- Effects: `O1`; asserted non-waivable protocol requirement that every intended mutation be accounted for before Phase 07 completion.
- Disposition: open.

### `i001-p1-research-c-003`

- Claim: the completed-run fixture has no agent rows for required Phase 01, 03, and 05 four-agent producer cohorts.
- Evidence: `SKILL.md:508-509,947-948,989-990,1018-1019`; `tests/fixtures/ledger/conformant_completed_run/ledger.sql:217-240`.
- Evidence status: direct omission claim; `unvalidated`.
- Materiality: researcher-rated high.
- Effects: `O1`; asserted fixed-cohort and durable-ledger constraints.
- Disposition: open.
- Aliases/overlap: overlaps `i001-p1-research-a-003`.

## Findings: version and artifact provenance

### `i001-p1-research-a-005`

- Claim: the v0.6.0 evaluation surface records but does not enforce ledger skill-version compatibility and retains v0.5.0 wording and conformant fixtures.
- Evidence: `tests/check_ledger.py:193,391,973,2220`; `tests/fixtures/ledger/conformant/ledger.sql:194`.
- Evidence status: direct static evidence; `unvalidated`.
- Materiality: researcher-rated high.
- Effects: `O1`; constraint `none`.
- Disposition: open.
- Aliases/overlap: `i001-p1-research-b-006`, `i001-p1-research-c-004`, `i001-p1-research-d-003`.

### `i001-p1-research-b-006`

- Claim: assigned ledger fixtures identify `skill_version='0.5.0'` while the manifest and installers identify v0.6.0; assigned tests do not assert skill version.
- Evidence: five assigned fixture ledgers; `skill.manifest.json:4`; installer headers; full assigned test-file absence search.
- Evidence status: direct provenance comparison; `unvalidated`.
- Materiality: researcher-rated medium.
- Effects: `O1`; asserted identity/provenance constraint.
- Disposition: open.

### `i001-p1-research-c-004`

- Claim: protocol-version compatibility is undefined because six populated v0.6.0 fixtures identify their runs as v0.5.0.
- Evidence: `SKILL.md:5-7,280,503-505`; six cited fixture ledgers.
- Evidence status: documented compatibility gap, not proof of unsafe compatibility; `unvalidated`.
- Materiality: researcher-rated moderate.
- Effects: `O1`; constraint `none`.
- Disposition: open.

### `i001-p1-research-d-003`

- Claim: fixture generation hardcodes v0.5.0 while the shipped manifest is v0.6.0, and the checker does not compare versions.
- Evidence: `tests/fixtures/ledger/generate_fixtures.py:394,1009`; `skill.manifest.json`; `tests/check_ledger.py:193,391`.
- Evidence status: direct source comparison; `unvalidated`.
- Materiality: researcher-rated low-moderate.
- Effects: `O1`; constraint `none`.
- Disposition: open.

### `i001-p1-research-b-001`

- Claim: `loop2_runs.not_checkable_path` is never existence-checked, and assigned fixtures point to absent `conformance/not-checkable.md` files while remaining capable of conformance.
- Evidence: cited fixture run rows; `tests/check_ledger.py:2468`; exact-error assertions in `tests/test_ledger_checker.py:170-176,196-200`; recursive bounded absence search.
- Evidence status: direct source, fixture, and absence evidence; `unvalidated`.
- Materiality: researcher-rated high.
- Effects: `O1`; asserted advisory/mechanical assurance boundary.
- Disposition: open.
- Aliases/overlap: `i001-p1-research-d-004`.

### `i001-p1-research-d-004`

- Claim: every generated fixture declares `conformance/not-checkable.md`, no fixture creates it, and referenced-artifact validation excludes the column.
- Evidence: `tests/fixtures/ledger/generate_fixtures.py:407`; representative ledgers; `tests/check_ledger.py:2458-2472`.
- Evidence status: direct source and corpus absence evidence; `unvalidated`.
- Materiality: researcher-rated low-moderate.
- Effects: `O1`; constraint `none`.
- Disposition: open.

## Findings: installed assurance and advisory boundary

### `i001-p1-research-b-002`

- Claim: the installable payload is exactly `SKILL.md`; deterministic and advisory tooling is not delivered or integrity-covered, although `SKILL.md` points operators to `tests/check_advisory_result.py`.
- Evidence: `skill.manifest.json:6-12`; `install.ps1:610-630,1049-1051`; `install.sh:124-127,365-370`; `SKILL.md:633`.
- Evidence status: direct packaging evidence; `unvalidated`.
- Materiality: researcher-rated high.
- Effects: `O1`; asserted advisory/mechanical assurance constraint.
- Disposition: open.

### `i001-p1-research-b-007`

- Claim: the advisory-result validator checks producer-supplied shape and echoed declarations, not evidence truth, completeness, model identity, or an independently recomputed packet digest.
- Evidence: `tests/test_advisory_result.py:22,79-82,104-107,123-132`.
- Evidence status: direct static evidence; `unvalidated`.
- Materiality: researcher-rated medium.
- Effects: `O1`; advisory/mechanical assurance boundary.
- Disposition: open.
- Qualification already observed by researcher: `STRUCTURALLY_CONFORMANT` and `advisory` naming accurately limit the claim; Phase 2 must test whether this is a defect or an intentional boundary.

### `i001-p1-research-c-001`

- Claim: the static checker sets `user-invocable: true`, contradicting `proposed_upgrade.md` language requiring `false`.
- Evidence: `proposed_upgrade.md:59-68`; `agents/loop2-conformance-checker.agent.md:1-7`.
- Evidence status: direct configuration/document comparison; `unvalidated`.
- Materiality: researcher-rated high.
- Effects: `O1`; researcher asserted a non-waivable isolation constraint.
- Disposition: open.
- Contradiction requiring special validation: `proposed_upgrade.md` may describe an earlier proposal rather than the final normative boundary. Phase 2 must determine provenance and whether any current normative file requires `false`.

### `i001-p1-research-c-005`

- Claim: the proposal's “rollback tests pass” readiness criterion is ambiguous because documented supported behavior provides neither atomic upgrade nor multi-target rollback.
- Evidence: `proposed_upgrade.md:229-232`; `README.md:380-388,528-590`.
- Evidence status: documentation ambiguity, not a proven implementation defect; `unvalidated`.
- Materiality: researcher-rated moderate.
- Effects: `O1`; constraint `none`.
- Disposition: open.

## Findings: installer security and parity

### `i001-p1-research-b-003`

- Claim: `install.ps1` ships environment-variable-controlled test hooks that can create a file in a caller-selected directory and stall mutation for up to 30 seconds; the Unix installer has no equivalent.
- Evidence: `install.ps1:474-509,1250,1400,1462`; whole-file bounded absence search in `install.sh`.
- Evidence status: direct mechanism evidence; exploitability conditional on control of the installer process environment; `unvalidated`.
- Materiality: researcher-rated medium-high.
- Effects: `O1`; asserted installer security-boundary constraint.
- Disposition: open.

### `i001-p1-research-b-004`

- Claim: `install.ps1` drops Windows handle-binding and identity guarantees when run on non-Windows, using weaker path-based fallback behavior than `install.sh`.
- Evidence: `install.ps1:257-259,288-291,344-346,1191-1197,1355-1357,1435`; contrast `install.sh:141-146,249-253,346-349`.
- Evidence status: direct cross-platform comparison; `unvalidated`.
- Materiality: researcher-rated medium.
- Effects: `O1`; asserted identity/provenance constraint.
- Disposition: open.

### `i001-p1-research-b-005`

- Claim: `install.sh` rejects multiply-linked files while `install.ps1` declares but never checks `NumberOfLinks`.
- Evidence: `install.sh:143,254-256,349`; `install.ps1:64,1004-1009,1042-1047` and whole-file bounded absence search.
- Evidence status: direct cross-platform comparison; `unvalidated`.
- Materiality: researcher-rated low-medium.
- Effects: `O1`; constraint `none`.
- Disposition: open.

### `i001-p1-research-b-009`

- Claim: Windows filename set equality is case-insensitive while the Unix lane uses exact byte equality, weakening drift classification on case-sensitive Windows directories.
- Evidence: `install.ps1:766-772,1050,1338`; `install.sh:365-367,471-474`.
- Evidence status: direct source comparison; practical impact conditional on filesystem configuration; `unvalidated`.
- Materiality: researcher-rated low.
- Effects: `O1`; constraint `none`.
- Disposition: open.

## Findings: test, fixture, and verifier quality

### `i001-p1-research-b-008`

- Claim: restricted SQL loading is regression-tested only against `ATTACH` and `UPDATE`, omitting other relevant statement and authorizer boundaries.
- Evidence: full `RestrictedSqlLoaderTests` in `tests/test_ledger_checker.py:98-126`.
- Evidence status: direct test-coverage bound; actual loader strictness was outside this researcher's partition; `unvalidated`.
- Materiality: researcher-rated medium.
- Effects: `O1`; asserted untrusted-packet-handling constraint.
- Disposition: open.

### `i001-p1-research-d-001`

- Claim: ordinary Python test execution may create `tests/__pycache__`, causing exact package inventory verification and the smoke lane to fail unless `-B` is used.
- Evidence: `tests/verify_package.py:232-252`; imports in `tests/test_ledger_checker.py:16` and `tests/test_advisory_result.py:13`; documented invocation `README.md:485`; smoke order `tests/smoke_installer.sh:131`.
- Evidence status: static mechanism evidence only; not executed due review boundary; `unvalidated`.
- Materiality: researcher-rated moderate.
- Effects: `O1`; constraint `none`.
- Disposition: open.

### `i001-p1-research-d-002`

- Claim: fixture regeneration recursively deletes every fixture subdirectory without allow-list, dry-run, or confirmation.
- Evidence: `tests/fixtures/ledger/generate_fixtures.py:784-786`; README coverage limited to inventory mention.
- Evidence status: direct static evidence; `unvalidated`.
- Materiality: researcher-rated moderate.
- Effects: `O1`; constraint `none`.
- Disposition: open.

### `i001-p1-research-d-005`

- Claim: several Windows race tests accept either interference outcome without recording which branch executed, so a guarded branch may never be exercised while the lane passes.
- Evidence: `tests/smoke_installer.ps1:836,871-980,1027-1029`; related disclosure `README.md:427-429`.
- Evidence status: direct test-oracle evidence; `unvalidated`.
- Materiality: researcher-rated moderate.
- Effects: `O1`; constraint `none`.
- Disposition: open.

### `i001-p1-research-d-006`

- Claim: the Bash smoke lane requires `TMPDIR` or an explicit sandbox parent, but README smoke prerequisites do not document it.
- Evidence: `tests/smoke_installer.sh:9-14`; `README.md:420-427`.
- Evidence status: direct documentation/source mismatch; `unvalidated`.
- Materiality: researcher-rated low-moderate.
- Effects: `O1`; constraint `none`.
- Disposition: open.

### `i001-p1-research-d-007`

- Claim: the Bash lane exports `PACKAGE_VERSION` to `verify_package.py`, but the verifier never reads it.
- Evidence: `tests/smoke_installer.sh:131`; whole-file bounded absence search in `tests/verify_package.py`.
- Evidence status: direct static evidence; `unvalidated`.
- Materiality: researcher-rated low.
- Effects: `O1`; constraint `none`.
- Disposition: open.

### `i001-p1-research-d-008`

- Claim: package verification pins installer source prose and formatting through brittle regular expressions rather than behavioral outcomes.
- Evidence: `tests/verify_package.py:282-395,566-577`.
- Evidence status: direct static evidence; `unvalidated`.
- Materiality: researcher-rated moderate.
- Effects: `O1`; constraint `none`.
- Disposition: open.

### `i001-p1-research-d-009`

- Claim: Windows and Unix smoke lanes cover different exit codes and race cases; neither is a complete parity oracle.
- Evidence: `tests/smoke_installer.sh:855-985`; `tests/smoke_installer.ps1:836-1029`.
- Evidence status: direct cross-lane comparison; `unvalidated`.
- Materiality: researcher-rated low.
- Effects: `O1`; constraint `none`.
- Disposition: open.

### `i001-p1-research-d-010`

- Claim: `smoke_installer.ps1` shadows automatic `$Matches` and uses exit code 999 as a failure sentinel that could collide with a real Windows exit code.
- Evidence: `tests/smoke_installer.ps1:248,324`.
- Evidence status: direct static evidence; `unvalidated`.
- Materiality: researcher-rated low.
- Effects: `O1`; constraint `none`.
- Disposition: open.

## Non-findings, dissent, and gaps

- The manifest schema version and ledger schema version are distinct namespaces; no mismatch was found between ledger schema 2 and `tests/check_ledger.py`.
- README inventory parity was reported correct at the research window: 309 documented entries and 309 manifested files.
- Fixture SQL and generated artifact shape were spot-checked without finding unexplained divergence beyond the recorded findings.
- Several fixture artifacts are one-line placeholders. The checker explicitly treats referenced-artifact content truth as not mechanically checkable, so placeholder content alone was not raised as a defect.
- No project code, installer, fixture generator, or tests were executed. Runtime consequences remain hypotheses until allowed testing outside this read-only review or direct static proof is sufficient.
- Phase 1 did not establish whether static-agent registration is intentionally external to package installation; Phase 2 must avoid treating source-only profile presence as proof of runtime availability.
- Phase 1 did not prove exploitation of installer races or test hooks. Findings distinguish mechanism from conditional impact.

## Phase 2 validation needs

Independent validators must reconstruct all claims from primary evidence without receiving researcher ratings or dispositions. Priority questions:

1. Can a minimal ledger pass while advancing without a qualifying gate, omitting producer cohorts, borrowing another run's preflight evidence, or completing with a planned apply unit?
2. Which duplicated version and missing-artifact findings are the same defect, and what materiality follows from current normative compatibility requirements?
3. Is `user-invocable: true` a current normative violation, a stale proposal conflict, or an intentional final decision?
4. Does prose-only installation contradict the current delivery contract, or is source-repository tooling explicitly optional?
5. Do PowerShell test hooks and cross-platform differences create material security or integrity risk under the documented threat model?
6. Does the restricted SQL loader already block the untested statement classes, making the issue test-depth rather than implementation unsafety?
7. Which low-level verifier and smoke-lane observations can affect operator outcomes enough to remain material?

<!-- level-up-complete -->
