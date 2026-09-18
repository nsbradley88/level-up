# Level Up — Iteration 002, Phase 1

## Run record

- Run: `a2fb9f0fa4836911`
- Iteration axis: contract-boundary closure
- Phase: fresh research and discovery
- Subject: `C:\Users\nabradl\Repos\tools\copilot-skills\loop2`
- Objective `O1` (`review-output`): produce an evidence-backed review and PR-ready change specification.
- Governing Level Up snapshot: SHA-256 `6e33cb093323e955107c732971d4eedf340cebb1d9c101ed6d01dda45224f4fc`.
- Iteration 001 status: not converged; its validated record was not supplied to fresh researchers.
- Boundary: strict read-only static review; no code, test, installer, or fixture execution.

## Coverage and independence

The unchanged 309-file, 867,499-byte manifest was repartitioned by a new hash-shuffled byte axis:

| Producer | Model | Files | Bytes | Coverage |
|---|---|---:|---:|---|
| `i002-p1-research-a` | GPT-5.6 Sol | 89 | 214,141 | 89/89 `READ_FULL` |
| `i002-p1-research-b` | Claude Opus 5 | 71 | 213,067 | 71/71 `READ_FULL` |
| `i002-p1-research-c` | GPT-5.6 Sol | 63 | 212,547 | 63/63 `READ_FULL` |
| `i002-p1-research-d` | Claude Opus 5 | 86 | 227,744 | 86/86 `READ_FULL` |

No path was excluded or partially read. Each path had one owner. Findings are `unvalidated`; agreement with Iteration 001 adds no weight.

## Discovery summary

Fresh research independently reproduced the main ledger weaknesses and sharpened several contract-boundary questions:

- current run/checker records omit version, stage, packet, or execution identity needed to distinguish revisions and repeated checks;
- state continuity, transition causes, replacement rounds, REVISE evidence, apply closure, and completion artifacts remain under-specified or unenforced;
- artifact existence and packet containment are incomplete;
- fixture and live-version identities diverge;
- the SQL/parser, advisory-result, fixture-generator, and smoke/reporting boundaries contain additional robustness or observability gaps;
- many installer observations are documented design choices or low-value consistency issues and require strict Phase 2 materiality filtering.

## Record identity and advisory-contract findings

| ID | Neutral claim | Evidence | Researcher materiality/status |
|---|---|---|---|
| `i002-p1-research-a-001` | `loop2_runs.phase` omits the active version although phase rows are version-keyed. | `revise_wrong_source/ledger.sql:6-16,46-57,194,208-211`; `revise_version_gap/ledger.sql` | material, open |
| `i002-p1-research-a-002` | Scalar `replaced_agent_id` does not uniquely reference the composite agent-attempt identity. | conformant DDL `ledger.sql:59-77`; no FK/unique declaration in 11 assigned ledgers | material, open |
| `i002-p1-research-a-003` | Checker results are keyed only by run/type, not stage, packet generation, digest, or attempt. | conformant DDL `ledger.sql:183-190`; `proposed_upgrade.md:99-112,155-158` | material, open |
| `i002-p1-research-a-004` | Advisory “full ID” validation checks result membership but not grammar of supplied contract IDs. | `tests/check_advisory_result.py:39-50,82-87,123-126`; advisory tests | material, open |
| `i002-p1-research-a-005` | Empty adjudication contract plus empty results is structurally conformant. | `tests/check_advisory_result.py:39-50,82,89-90,151-161` | policy-ambiguous, open |
| `i002-p1-research-b-008` | Static advisory profile is outside the intentional one-file installed package identity. | `install.ps1:668-686`; agent profile | researcher-rated high, open |
| `i002-p1-research-b-009` | Advisory `packet_sha256` is supplied/echoed, not computed by the no-tools checker. | agent profile | moderate, open |
| `i002-p1-research-b-010` | Four different `schema_version` namespaces use the same unqualified field name. | agent JSON, manifest/receipt, terminal record, ledger schema | moderate, open |

Contradiction requiring validation: single-file packaging and supplied-digest advisory behavior were previously documented boundaries, so `b-008/b-009` may be accurate non-defects rather than scope gaps.

## Ledger state, gate, transition, and completion findings

| ID | Neutral claim | Evidence | Researcher materiality/status |
|---|---|---|---|
| `i002-p1-research-c-001` | Literal adjacent-state equality conflicts with normative/generated transition labels; phase status is also unvocabularied. | `SKILL.md:690-720`; `check_ledger.py:1222-1231,2224-2277`; fixture transition rows | critical, open |
| `i002-p1-research-c-002` | Forward and back-edge transitions are not bound to exact gate evidence. | `SKILL.md:645-671,695-696`; `check_ledger.py:1858-2052,2096-2103,2172-2217` | critical, open |
| `i002-p1-research-c-003` | Replacing one slot does not void/redeclare the entire cohort; fixture mixes attempt-2 with three attempt-1 ballots. | `SKILL.md:749,788-792`; `check_ledger.py:1741-1765,1980-1999`; replaced-slot fixture | critical, open |
| `i002-p1-research-c-004` | REVISE closure omits unanimous ballots, gate binding, packet completeness, and packet existence. | `SKILL.md:875-940`; `check_ledger.py:2289-2344,2458-2504` | critical, open |
| `i002-p1-research-c-005` | Apply rows can exist outside Phase 07 and sequence/preflight/disposition semantics are weak. | `SKILL.md:1087-1211`; `check_ledger.py:2347-2434` | high, open |
| `i002-p1-research-c-006` | Mandatory pre-final and post-completion checker passes cannot coexist under one `(run_id, checker_type)` row. | `SKILL.md:454-462,514-548`; `check_ledger.py:2506-2550` | critical, open |
| `i002-p1-research-c-007` | Current skill identity is v0.6.0 while diagnostics/fixtures record v0.5.0 and compatibility is unenforced. | `SKILL.md:5-7,280`; checker messages/shape checks; fixtures | high, open |
| `i002-p1-research-c-008` | Stored checker-result statuses in negative/indeterminate fixtures contradict the packet state and are not reconciled to evaluation. | malformed-schema and indeterminate ledgers; `check_ledger.py:746-748,2506-2597` | high, open |
| `i002-p1-research-c-009` | Completion closure omits required final synthesis/not-checkable/frozen-packet structure; positive frozen packet is a one-line stub. | `SKILL.md:706,1208-1244`; `check_ledger.py:1288-1346,2458-2504`; completed fixture | high, open |
| `i002-p1-research-b-012` | Replaced attempts skip scratchpad verdict-heading agreement checks. | generator replaced-slot case; `test_ledger_checker.py:82-85,132-142` | high, open |
| `i002-p1-research-b-013` | `VOID` is invalid as an agent verdict while `void` is valid in gate/disposition columns. | negative and void-round fixtures/tests | medium, open |
| `i002-p1-research-b-014` | `checked` reports validators as run even when a table has zero applicable rows. | void-round fixture; checked-list tests | medium, open |
| `i002-p1-research-b-015` | A test name claims an in-flight prefix is unpenalized but does not assert the result and the packet has an error. | `test_ledger_checker.py:193-198` | low, open |
| `i002-p1-research-d-021` | Some closure/void fixtures cannot isolate connectivity behavior because one contains no transitions. | completed-prefix, missing-ancestry, void-round ledgers | medium, open |
| `i002-p1-research-d-022` | Scratchpad and ledger candidate-pairing authority is unclear; wrong-pair prose may be inert if ledger columns are authoritative. | review scratchpad grammar and wrong-pair artifacts | medium/conditional, open |
| `i002-p1-research-d-023` | Shared fixture DDL is generated identically but not directly pinned against partial regeneration drift. | measured DDL digests across fixtures | medium, open |

## Artifact and fixture-boundary findings

| ID | Neutral claim | Evidence | Researcher materiality/status |
|---|---|---|---|
| `i002-p1-research-b-001` | Run-level `not_checkable_path` references an absent file and is not covered by current positive tests. | generator, recursive absence search, conformant assertion | high, open |
| `i002-p1-research-b-002` | Evidence-adjudication and failed-challenge tables are absent from generator column/order maps and fixtures. | `generate_fixtures.py:57-106,206,217` | medium, open |
| `i002-p1-research-b-020` | Fixture regeneration deletes all directories but preserves stray files. | `generate_fixtures.py:783-786,1000` | low, open |
| `i002-p1-research-b-021` | Multiple-run fixture short-circuits before artifact checks, so it does not test run-level reference existence. | multiple-run fixture and checked-list assertion | low, open |
| `i002-p1-research-d-018` | All fixtures use safe packet-relative paths, so hostile path forms have no negative fixture. | measured all ledger paths | test-gap, open |
| `i002-p1-research-d-019` | 22/23 fixtures record absent `not-checkable.md`. | measured fixture corpus and README inventory | high, open |
| `i002-p1-research-d-020` | Three ledger-only negative fixtures reference many absent artifacts, risking non-isolated diagnostics. | bad-topology/malformed/malformed-numeric contents | medium, open |

## Installer and smoke findings requiring validation

| ID | Neutral claim | Evidence | Researcher materiality/status |
|---|---|---|---|
| `i002-p1-research-b-003` | RESIDUE recognizes sibling names the current PowerShell installer does not create; real tmp/quarantine leftovers use other names. | `install.ps1:950-951,1248,1260,1499`; smoke residue checks | high, open |
| `i002-p1-research-b-004` | Sibling-residue prefixes are not directly smoke-tested. | PowerShell smoke residue cases | medium, open |
| `i002-p1-research-b-005` | Single-target mutations suppress terminal-result records. | `install.ps1:1610-1648`; smoke assertions | high, open |
| `i002-p1-research-b-006` | Terminal `outcome='applied'` is also used for no-op exact/absent items. | `install.ps1:1614-1638`; smoke expectations | medium, open |
| `i002-p1-research-b-007` | Verify action vocabulary contains `refuse` without the shared refusal path. | `install.ps1:1148,1174,1588-1594` | low, open |
| `i002-p1-research-b-016` | Windows race banner is unconditional although guarded branches may not execute. | `smoke_installer.ps1:836,872-995,1026` | medium, open |
| `i002-p1-research-b-017` | PowerShell test hook directory is caller-controlled and can create/wait there. | `install.ps1:491-522` | medium, open |
| `i002-p1-research-b-018` | Target dedup and validation use different case-sensitivity rules. | `install.ps1:766-775,888-890,1133-1141` | low, open |
| `i002-p1-research-b-019` | Personal-root detection accepts files before later rejecting derived targets. | `install.ps1:1124-1131` | low, open |
| `i002-p1-research-d-007` | README mixes PowerShell quarantine recovery language into Bash exit-18/RESIDUE guidance. | README recovery; absence in `install.sh` | medium-high, open |
| `i002-p1-research-d-009` | Sibling RESIDUE prefixes can block an unrelated healthy target and may exist only for backward compatibility. | `install.sh:284-289,381-383`; README/smoke | high, open |
| `i002-p1-research-d-010` | Bash race determinism depends on FIFO backpressure and large fan-out without explicit proof the intended pause occurred. | `smoke_installer.sh:76-92,897-985` | medium-high, open |
| `i002-p1-research-d-011` | Bash summary is hand-maintained rather than derived from executed cases. | `smoke_installer.sh:985` and full case tally | currently accurate but fragile, open |
| `i002-p1-research-d-012` | Smoke duplicates the installer action table and includes an extra SOURCE_INVALID branch. | smoke `expected_action`; installer `planned_action` | maintenance concern, open |
| `i002-p1-research-d-013` | Bash single-target mutations also suppress terminal-result records. | `install.sh:787-806`; README/smoke | high, open |
| `i002-p1-research-d-017` | PowerShell hook verifier is syntax-pattern-based and was not cross-checked by this partition. | verifier regex and README | bounded/unverified, open |

Closed/documented installer observations from fresh research: `i002-p1-research-d-004`, `d-005`, `d-006`, `d-008`, `d-014`, `d-015`, and `d-016` describe documented support boundaries or verified current parity rather than proposed defects.

## Parser and verifier findings

| ID | Neutral claim | Evidence | Researcher materiality/status |
|---|---|---|---|
| `i002-p1-research-d-001` | Verifier extracts Bash embedded Python using an exact heredoc marker/terminator. | `install.sh:1-15,832-833`; `verify_package.py:189-209` | brittle maintenance, open |
| `i002-p1-research-d-002` | Installer rejects NaN/Infinity but verifier JSON parser does not. | `install.sh:88-104`; `verify_package.py:66-73,135-139` | material mismatch, open |
| `i002-p1-research-d-003` | Verifier does not independently apply the installer's payload path grammar. | `install.sh:107-130`; `verify_package.py:155-160` | bounded by one literal payload, open |
| `i002-p1-research-d-013` | Single-target terminal-result suppression affects Bash consumers. | installer/smoke records | high, open |

## Non-findings and contradictions

- Bash target/deletion authority is strongly bounded and non-recursive (`i002-p1-research-d-004`, `d-005`).
- Bash partial uninstall and hardlink publication are documented support choices (`d-006`, `d-008`).
- Exact README inventory currently matches 309 files (`d-015`).
- Partial verifier completeness is disclosed structurally and documented (`d-016`).
- Advisory no-tools digest echo and single-file package boundaries may be intentional rather than defects.
- Several installer findings conflict with prior validation that lane differences, test hooks, and no-op reporting are documented; Phase 2 must reconstruct rather than inherit either conclusion.

## Phase 2 priorities

1. Validate novel identity findings: active phase version, replacement reference, checker stage/packet identity, advisory contract grammar/empty cases.
2. Validate slot-replacement cohort invalidation and fixture checker-result contradictions.
3. Separate required completion artifact structure from intentionally NOT_CHECKABLE semantic content.
4. Test whether the SQL/parser boundary findings from Iteration 001 remain the highest-value parser work; fresh Phase 1 did not independently inspect that code path in the same partition.
5. Triage installer observations against maintained README contracts and operator value; do not expand scope without material evidence.

<!-- level-up-complete -->
