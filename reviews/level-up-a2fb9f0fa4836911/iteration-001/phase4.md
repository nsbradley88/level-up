# Level Up — Iteration 001, Phase 4

## Run record

- Run: `a2fb9f0fa4836911`
- Phase: independent scope validation
- Subject: `C:\Users\nabradl\Repos\tools\copilot-skills\loop2`
- Objective `O1` (`review-output`): produce an evidence-backed review and PR-ready change specification.
- Governing Level Up snapshot: SHA-256 `6e33cb093323e955107c732971d4eedf340cebb1d9c101ed6d01dda45224f4fc`.
- Phase 3 candidate scope: SHA-256 `91b70963fa01a5ca6ccd830e8c08a680283f4fd0efbad0fe5f8e12c7c8640591`.
- Pre-validation subject identity: 309/309 manifested files remained SHA-256-equal; no drift detected.
- Boundary: validation was static and read-only. Recommendations below are specifications, not implemented changes.

## Validation method

Three fresh validators inspected the candidate mechanisms against current source, schema, tests, fixtures, and documentation:

| Validator | Model | Recommendations |
|---|---|---|
| `i001-p4-validate-a` | Claude Opus 5 | `i001-p3-scope-a-001` through `a-005` |
| `i001-p4-validate-b` | GPT-5.6 Sol | `i001-p3-scope-b-001` through `b-006` |
| `i001-p4-validate-c` | Claude Opus 5 | `i001-p3-scope-c-001` through `c-003` |

One recommendation is `validated`, twelve are `qualified`, one is `rejected`, and none are unresolved. Qualified recommendations proceed only with the exact supported conditions below.

## Adjudicated recommendations

### `i001-p3-scope-c-001` — deletion-bounded fixture regeneration

- Phase 4 status: `qualified`.
- Supported outcome: centralize cleanup as `clean_owned(root, owned_names)`; pre-scan before deletion; remove only declared direct-child fixture directories and recognized generated cache directories; preserve and report unknown entries; reject link/reparse entries before any deletion.
- Required correction: current `shutil.rmtree` generally refuses directory symlinks/junctions rather than traversing them. The demonstrated risk is partial deletion before an abort, not link-target deletion.
- Required mechanism: derive or declare the owned set before cleanup, parameterize the root for isolated tests, and include `__pycache__` or other explicitly generated cache directories in removable generated entries so cleanup does not create a predictable inventory failure.
- Required tests: owned replacement; unknown sentinel preserved and reported; link/reparse pre-scan refusal with target unchanged; idempotent repeat. Windows link setup may skip only when privilege-independent creation is unavailable.
- Effects: resolves `i001-p1-research-d-002`; enables safe fixture regeneration for later changes.
- Dependencies: first implementation step.
- New mechanism findings incorporated: `i001-p4-validate-c-001`, `i001-p4-validate-c-002`.

### `i001-p3-scope-a-001` — uniform single-run child scoping

- Phase 4 status: `validated`.
- Mechanism: after exactly one run is established, report every child row whose `run_id` differs and build all semantic indices from same-run rows only. Reuse or replace `foreign_run_transition` to avoid duplicate reports.
- Result semantics: foreign rows are `NON_CONFORMANT`, not silently ignored and not format-invalid.
- Tests: inject one foreign row per child table and prove it cannot satisfy required evidence; preserve current positives.
- Effects: resolves `i001-p2-validate-a-001` and `i001-p1-research-a-007`.
- Dependencies: precedes every semantic validator.

### `i001-p3-scope-b-001` — declare one normative skill-version policy

- Phase 4 status: `qualified`.
- Supported policy: the packet declares its producing protocol version; current support is an explicit set containing only `0.6.0`. This is a structural declaration, not authenticated provenance.
- Source of release identity: `skill.manifest.json.version`, pinned by verification to both `SKILL.md` version fields and literal checker/generator constants. The standalone checker must not dynamically trust packet input or require runtime manifest access.
- Update order: bounded cleanup, generator constant, current fixtures, current checker text, `SKILL.md`/README, manifest digest/size. Preserve deliberate historical v0.5.0 text.
- Effects: resolves the merged version cluster.
- Dependency: precedes `i001-p3-scope-b-002`.

### `i001-p3-scope-b-002` — enforce supported skill versions

- Phase 4 status: `qualified`.
- Mechanism: for exactly one run row, perform exact membership in `SUPPORTED_SKILL_VERSIONS = {"0.6.0"}` before semantic validation. Raise `LedgerFormatError("unsupported_skill_version", ...)`, producing `INVALID` and CLI exit 3.
- Preserve existing zero/multiple-run handling.
- Do not require an INVALID result to contain the normal `checked` list; current format omits it.
- Tests/fixtures: unsupported version returns exactly `INVALID`; fixture addition updates cleanup ownership and exact README inventory; current fixtures remain conformant.
- Widening condition: add another version only with differential evidence that the relevant protocol rule tables are compatible.
- Effects: closes silent wrong-protocol evaluation.
- Dependencies: `b-001`.

### `i001-p3-scope-b-004` — generate `conformance/not-checkable.md`

- Phase 4 status: `qualified`.
- Mechanism: after all fixture mutation/fault shaping is complete, final packet writing inspects the deterministic checker row. For recognized non-`not-run` results, render deterministic property IDs and reasons from `check_ledger.NOT_CHECKABLE`; do not render for `not-run`.
- The generator, not the checker, owns fixture artifact rendering.
- Tests may compare property IDs exactly; production validation remains existence-only.
- Effects: repairs positive fixture completeness.
- Dependencies: `c-001`; precedes `b-003`.

### `i001-p3-scope-b-003` — validate the not-checkable artifact

- Phase 4 status: `qualified`.
- Exact trigger: a same-run deterministic checker row exists with a recognized result other than `not-run`.
- Then `not_checkable_path` must be non-null, safely relative, and resolve to an existing regular file using the existing artifact-boundary helper. Runtime validation must not parse content.
- Prefix compatibility: current checker cardinality requires one deterministic row; a prefix remains compatible by using `result='not-run'`, not by omitting the row.
- Effects: resolves the merged missing-artifact finding.
- Dependencies: `a-001`, `b-004`.
- New mechanism finding incorporated: `i001-p4-validate-b-001`.

### `i001-p3-scope-a-002` — derive gate statuses and relevant counters

- Phase 4 status: `qualified`.
- Supported portion: normatively define `pending`, `mixed`, `revise`, and `suspended`; derive `pass_count` and `invalidated_pass_count` for every applicable status; retain existing derived objection count; preserve void reconciliation; bind suspension to resource evidence; keep absent current gate as `INDETERMINATE`.
- Revision target mechanism: prefer parsing the existing scratchpad `## Final declaration` using current section-parser precedent, or add one optional agent-level field. Do not add gate-level cause fields solely for target derivation.
- Revision packet: use and existence-check `loop2_phases.revision_packet_path`.
- Precedence must make `void` and `suspended` mutually unambiguous.
- Unsupported portion removed: a blanket “derive every counter” claim and unnecessary gate-level schema expansion.
- Effects: resolves the supported portion of `i001-p1-research-a-004`.
- Dependencies: `a-001`; normative text before enforcement.

### `i001-p3-scope-a-003` — evidence-backed transition validation

- Phase 4 status: `qualified`.
- Supported mechanism: bind forward edges to a non-invalidated qualifying pass for the edge's existing `from_phase/from_version`; bind revise edges to the derived revise gate, `to_phase/to_version`, `revision_of`, and existing revision packet; require producer completion to have the exact same-version four-slot cohort.
- State continuity: default to a checker-side successor map from current closed `to_state` labels to permitted next `from_state` labels. Canonical wire-format IDs are optional and justified only if phase status and transition state are unified in one coordinated redesign.
- Schema expansion: existing columns recover phase/version/target/lineage/packet; add only fields whose ambiguity is demonstrated, such as gate round when multiple rounds matter.
- Unsupported portion removed: mandatory canonical wire IDs and broad cause-column expansion.
- Effects: resolves transition causality, state continuity, and producer-cohort omissions.
- Dependencies: `a-001`, `a-002`, and the schema decision below.

### `i001-p3-scope-a-004` — apply-unit invariants and terminality

- Phase 4 status: `qualified`.
- Supported rules: Phase 07 only; positive unique contiguous sequence; use `preflight_state`; enforce status/path/evidence matrix; halt is terminal; review requires exact Phase 08 pass; derive supersession from existing invalidation/revision fields; accepted/completed execution cannot retain unresolved plans.
- Abandoned intent decision: default to retaining `planned` only when a non-null disposition explicitly records deliberate abandonment at closure. If maintainers prefer an explicit `cancelled` status, it is a vocabulary-only change and must land with documentation and evidence/disposition rules.
- Do not introduce new supersession fields.
- Effects: resolves `i001-p1-research-a-008` and the planned-unit completion ambiguity.
- Dependencies: `a-001` through `a-003`; consumed by closure.

### `i001-p3-scope-a-005` — coherent lifecycle closure

- Phase 4 status: `qualified`.
- Mechanism: first declare one phase-status vocabulary. Project current run phase/status from the maximum-sequence transition endpoint; reconcile suspension reason only at run level; validate phase status, gate/invalidation state, producer cohorts, apply terminality, final synthesis, checker/artifact closure, and current ancestry.
- Canonical transition IDs are not a dependency; projection works with the current labels plus successor map.
- Error semantics: retain accumulate-all for independent invariants. Short-circuit only dependent cascades whose prerequisite already failed.
- Effects: resolves lifecycle incoherence and completed-run closure gaps.
- Dependencies: all preceding core ledger mechanisms.

### `i001-p3-scope-b-005` — hostile-SQL regression depth

- Phase 4 status: `qualified`.
- Keep tests-only unless a bypass is demonstrated.
- Feasible coverage: lexical statement classes, target-table restrictions, incomplete input, UTF-8 failure, admitted-shape SQL function/authorizer denial, and side-effect assertions for file-bearing attacks.
- Authorizer vs extension tests: an admitted function expression can exercise authorizer denial; pin `enable_load_extension(False)` through narrow call observation. Do not require one black-box case to isolate both controls.
- Side-effect absence is required for file-bearing attacks, not every non-file statement.
- Effects: resolves `i001-p1-research-b-008` as assurance depth.
- New mechanism finding incorporated: `i001-p4-validate-b-002`.

### `i001-p3-scope-c-002` — explicit Bash smoke sandbox configuration

- Phase 4 status: `qualified`.
- Mechanism: when both positional parent and `TMPDIR` are absent/empty, print actionable usage and exit 2 before sandbox creation. Explicit parent takes precedence. Do not add implicit TMP/TEMP/global fallback.
- Verifier constraint: diagnostic source text must not introduce the literal `/tmp`; README examples may.
- Effects: resolves `i001-p1-research-d-006`.
- Dependencies: independent.

### `i001-p3-scope-c-003` — native smoke contract coverage

- Phase 4 status: `qualified`.
- Validated subparts:
  - add a deterministic native-Windows PowerShell exit-1 apply-failure case;
  - label guarded Windows race outcomes, explicitly as telemetry/reporting rather than deterministic two-branch coverage.
- Qualified Bash exit-18 mechanism: no deterministic route exists with the current stdout-FIFO seam because no output occurs between payload unlink and receipt removal. A new seam is proportionate only if it mirrors the PowerShell facility: two environment variables, fixed allow-listed name, inert when unset, bounded timeout, verifier pins, and documentation.
- Coverage summary must be accumulated from actually executed cases, not a hand-written literal.
- Preserve lane boundaries: Bash exit 18 is native POSIX evidence; non-Windows PowerShell remains fallback-only.
- Effects: resolves `i001-p1-research-d-009` with qualified `d-005`.
- New mechanism finding incorporated: `i001-p4-validate-c-003`.

### `i001-p3-scope-b-006` — pin NOT_CHECKABLE prose to checker data

- Phase 4 status: `rejected`.
- Basis: no validated shrinkage defect exists; `b-004` already pins generated fixture content to the checker set. A prose-subset test does not detect deletion from the documented set, while a hard-coded count/set or parser would duplicate or brittlely couple the contract.
- Reconsideration condition: introduce explicit machine-readable normative property IDs as a separately approved contract.

## New Phase 4 mechanism findings

### `i001-p4-validate-a-001` — schema expansion requires an explicit compatibility decision

- Status: supported and material to implementation feasibility.
- Evidence: extra columns are tolerated, but required-column additions invalidate existing packets; schema version 2 is exact with no migration/range.
- Effect: `O1`; constraint `none`.
- Disposition: addressed as a qualification across `a-002`, `a-003`, and version work.
- Required decision: optional fields may remain schema 2; any required field addition must coordinate a schema/version bump, all fixture regeneration, and supported-version policy.

### `i001-p4-validate-b-001`

- Status: supported mechanism correction, not a separate change objective.
- Claim: prefixes cannot omit the deterministic row under current cardinality; they use `not-run`.
- Disposition: merged into `b-003`.

### `i001-p4-validate-b-002`

- Status: supported mechanism correction.
- Claim: one black-box SQL case cannot separately prove extension disabling and authorizer denial under current ordering.
- Disposition: merged into `b-005`.

### `i001-p4-validate-b-003`

- Status: supported rejection basis.
- Claim: the proposed prose-subset coupling cannot detect removal from the documented set without another duplicate authority.
- Disposition: closes `b-006` as rejected.

### `i001-p4-validate-c-001`

- Status: supported mechanism correction.
- Claim: an owned-name allow-list must explicitly handle generated cache directories or regeneration predictably preserves inventory-breaking cache files.
- Disposition: merged into `c-001`.

### `i001-p4-validate-c-002`

- Status: supported mechanism correction.
- Claim: isolated cleanup tests require a root-parameterized helper and ownership planning before deletion.
- Disposition: merged into `c-001`.

### `i001-p4-validate-c-003`

- Status: supported mechanism correction.
- Claim: the Bash coverage summary is a hand-written literal and must be derived from executed cases before adding exit 18.
- Disposition: merged into `c-003`.

## Final implementation order

1. Extract and test bounded fixture cleanup (`c-001`).
2. Add central same-run child scoping (`a-001`).
3. Declare and pin current skill-version identity (`b-001`) and enforce it (`b-002`).
4. Generate not-checkable fixture artifacts (`b-004`), regenerate once, then enforce their existence (`b-003`).
5. Declare gate, phase-status, and apply terminal semantics; decide optional versus required schema additions (`a-002`, `a-004`, `i001-p4-validate-a-001`).
6. Implement gate derivation (`a-002`) and evidence-backed transition/cohort checks with a successor map (`a-003`).
7. Implement apply-unit invariants (`a-004`) and coherent closure (`a-005`).
8. Expand SQL regression coverage (`b-005`).
9. Repair Bash smoke usage (`c-002`).
10. Derive smoke summaries, add Windows exit 1 and labeled race outcomes, then add the bounded Bash exit-18 seam (`c-003`).
11. Do not implement `b-006`.

## Phase 4 outcome

The validated scope is substantial but bounded. It strengthens the ledger as a structural conformance record without claiming semantic truth or runtime identity, and it improves source-package assurance without changing the deliberate single-file installation contract. The largest design risk—an unnecessary wire-format rewrite—has been removed: current fields and checker-side maps can resolve most invariants. Any required schema expansion remains explicitly gated by version compatibility work.

## Phase 5 neutral review needs

Adversarial reviewers must challenge:

- whether central run scoping and successor-map transition binding cover every bypass;
- whether current fields truly identify the exact gate round and revise target without new required schema;
- whether `planned` plus disposition is a coherent terminal representation;
- whether exact-current skill-version rejection harms legitimate historical audit workflows;
- whether generating and existence-checking not-checkable artifacts preserves prefix semantics;
- whether the SQL corpus tests meaningful authorizer behavior rather than implementation trivia;
- whether a shipped Bash synchronization seam adds more production risk than its coverage value;
- whether the proposed implementation order can regenerate fixtures only once without masking failures.

<!-- level-up-complete -->
