# Level Up — Iteration 002, Phase 3

## Scope record

- Run: `a2fb9f0fa4836911`; subject: Loop2 v0.6.0 working tree.
- Objective `O1` (`review-output`): a PR-ready, evidence-backed change specification.
- Three fresh scopers derived recommendations from validated Phase 2 findings only.
- Recommendations are unvalidated until Phase 4.
- Preserved boundaries: installed payload remains one `SKILL.md`; profile registration stays external; advisory checking stays optional, tool-less, supplied-evidence-only, and non-authoritative.

## Ranked candidate scope

### `i002-p3-scope-001` — Define an atomic schema and release-version policy

- **Sources:** `i002-p2-validate-b-007`, `i002-p2-validate-c-002`.
- **Outcome:** distinguish skill version, ledger schema, deterministic-result contract, and advisory contract; stop silently interpreting v0.5.0 records as current v0.6.0 semantics.
- **Scope:** `SKILL.md`, checker diagnostics/compatibility gate, generator/fixtures/tests, README, manifest verification.
- **Mechanism:** freeze ledger schema 2 as legacy; introduce schema 3 for required identity/key changes below. Reject unsupported skill/schema combinations as `INVALID`; retain archived schema-2 audit only under an explicit compatibility matrix.
- **Tradeoff:** coordinated fixture/consumer churn; no automatic migration.
- **Success:** diagnostics name actual supported versions; mismatches have deterministic classification/exit behavior; release files change atomically.

### `i002-p3-scope-002` — Make lifecycle position and transition causality authoritative

- **Sources:** `i002-p2-validate-a-001`, `i002-p2-validate-b-001`, `b-002`, `b-004`.
- **Outcome:** no advancement from an unrelated gate, dormant maximum version, disconnected state string, or unclosed REVISE.
- **Scope:** run/phase/gate/transition vocabularies and checker validation.
- **Mechanism:** derive active `(phase, version, state)` from the connected transition tail; run fields are checked projections. Chain phase, version, and state. Forward/back transitions bind an exact gate key. REVISE requires four active declarations for one candidate/round/target plus an immutable revision packet before the edge.
- **Schema:** schema 3 adds only causal gate/REVISE identity that cannot be inferred reliably; do not add a redundant optional active-version field.
- **Success:** decoy higher versions, state mismatch, orphan pass, target disagreement, 3/4 REVISE, and missing packet fail.

### `i002-p3-scope-003` — Treat replacement as a cohort lifecycle event

- **Sources:** `i002-p2-validate-a-002`, `i002-p2-validate-b-003`, `b-010`.
- **Outcome:** eliminate ambiguous replacement references and mixed stale/new ballots.
- **Scope:** agent identity, attempt lineage, review rounds, scratchpad agreement, gates and fixtures.
- **Mechanism:** unique run-scoped agent-attempt identity; contiguous same-coordinate attempt chain; successor references exact predecessor. Replacing one validator voids the whole review round and all four redeclare in the next round. Inactive rows retain and agree with immutable verdict/candidate/round artifacts.
- **Non-goal:** freshness, independence, or model identity proof.
- **Success:** duplicate IDs, gaps, cross-coordinate replacement, mixed rounds, and inactive scratchpad disagreement fail; a complete next-round cohort passes.

### `i002-p3-scope-004` — Preserve checker generations and enforce completion closure

- **Sources:** `i002-p2-validate-a-003`, `i002-p2-validate-b-009`, `i002-p2-validate-c-B001-D019`.
- **Outcome:** retain both mandatory deterministic checks and prevent artifact-poor completion.
- **Scope:** checker-result key, stage/generation packet identity, Phase 09 closure and fixture artifacts.
- **Mechanism:** immutable `(checker_type, stage, generation)` records for prefix/completion checks, each bound to packet and summary. Completion requires active ancestry syntheses/snapshots, required producer/reviewer cohorts, final synthesis, not-checkable artifact, apply closure, fixed root records, and successful completion-stage deterministic result. Singular run paths point to the authoritative completion generation only.
- **Success:** prefix/completion coexist; duplicate generation or missing cohort/artifact/result fails; in-flight prefixes remain valid.

### `i002-p3-scope-005` — Enforce apply-unit execution invariants

- **Sources:** `i002-p2-validate-b-005`.
- **Outcome:** prevent non-Phase-07 or stale-design evidence from authorizing mutation and require terminal physical disposition.
- **Scope:** Phase 07/08 rules and apply-unit checker/tests.
- **Mechanism:** units only in Phase 07; sequence unique/contiguous per execution version; exact status-dependent field obligations; prerequisite credit from active Phase-06 ancestry; expected/actual paths equal and allowlisted; every superseded mutated unit has one terminal physical disposition.
- **Non-goal:** prove preflight truth or rollback success.
- **Success:** phase violations, sequence gaps, stale passes, evidence/path mismatches, and undispositioned superseded units fail.

### `i002-p3-scope-006` — Make structural coverage claims exact

- **Sources:** `i002-p2-validate-b-012`, `i002-p2-validate-c-B002`.
- **Outcome:** `checked` means evaluated, not merely invoked over zero rows; required tables are not decorative.
- **Scope:** checker table loading, report contract, coverage modes, generator/tests.
- **Mechanism:** load and validate evidence-adjudication and failed-challenge tables or remove them normatively. Report each check as evaluated/not-applicable/indeterminate with row counts. Total coverage requires a machine-structured unique path manifest.
- **Success:** invalid table references and false coverage claims fail; vacuous checks report not-applicable.

### `i002-p3-scope-007` — Replace physical-line SQL framing and normalize loader failures

- **Sources:** `i002-p2-validate-c-001` and the independently validated Iteration 001 SQL Warning finding.
- **Outcome:** every hostile or malformed ledger returns a deterministic `INVALID` report and exit 3, never a traceback or version-dependent raw SQLite message.
- **Scope:** `_ledger_statements`, `_load_ledger`, restricted-SQL prose, load-policy tests.
- **Mechanism:** exact one-statement framing before allow-listing; explicit comment policy; catch the narrow expected SQLite exception family including `sqlite3.Warning`; rollback/remove authorizer on every refusal; fixed error vocabulary without host paths or raw untrusted text.
- **Non-goal:** general SQL parsing or stronger authorship/tamper guarantees.
- **Success:** multi-statement physical lines and comment variants classify identically on supported Python versions with no second statement executed.

### `i002-p3-scope-008` — Centralize packet-contained artifact resolution

- **Sources:** `i002-p2-validate-c-003`, `c-D018`, `c-B001-D019`, and Iteration 001 link-containment evidence.
- **Outcome:** no drive-qualified, UNC, traversal, link, or missing declared artifact can satisfy packet requirements.
- **Scope:** all ledger path consumers, artifact existence, scratchpads, fixtures/tests, not-checkable and revision-packet paths.
- **Mechanism:** one resolver rejects drive/UNC/reserved/escape forms, resolves beneath the packet root, and requires the agreed regular-file/link policy. Every path-bearing column is either status-gated and checked or explicitly classified NOT_CHECKABLE. Add inert hostile-path fixtures.
- **Tradeoff:** strict single-link policy may reject dedup-backed packets; Phase 4 must validate the exact link contract.
- **Success:** hostile forms fail without opening outside files; all declared required artifacts exist; current conformant packets stay conformant after fixture repair.

### `i002-p3-scope-009` — Fail closed at advisory contract ingress

- **Sources:** `i002-p2-validate-a-004`, `a-005`.
- **Outcome:** malformed or vacuous contracts cannot yield `STRUCTURALLY_CONFORMANT`.
- **Scope:** advisory validator, contract/profile prose and tests.
- **Mechanism:** apply explicit full-ID grammar to contract and result sides; reject compressed/range-like forms; require nonempty adjudication IDs and required NOT_CHECKABLE set or define an explicit not-run zero-case; type `missing_information` so it cannot introduce forbidden IDs.
- **Non-goal:** semantic judgment or mandatory advisory execution.
- **Success:** malformed IDs and empty contracts receive distinct fail-closed codes; valid existing ID families remain accepted.

### `i002-p3-scope-010` — Bind advisory contracts to exact packet bytes at the parent validator

- **Sources:** `i002-p2-validate-a-007`.
- **Outcome:** prove only that the contract/result pair refers to the exact packet bytes the reference validator read.
- **Scope:** canonical packet digest definition, validator CLI, tests and limitation prose.
- **Mechanism:** required packet-root input; canonical relative-path/file-byte enumeration using recommendation 008 containment rules; recompute and compare digest before result validation. The tool-less profile continues only to echo supplied digest.
- **Non-goals:** evidence truth, checker actually reading the packet, model identity, independence, or runtime isolation.
- **Success:** missing packet root or digest mismatch fails; digest is stable across supported platforms; profile remains `tools: []`.

### `i002-p3-scope-011` — Correct installer terminal and personal-root contracts

- **Sources:** `i002-p2-validate-d-004`, `d-009`.
- **Outcome:** no-op work is not described as applied and file/dangling-link home children cannot be silently ignored or poison a sibling-root mutation late.
- **Scope:** both installers, smoke cases, output contract and concise README clarification.
- **Mechanism:** add/define terminal `noop` outcome or explicitly version a processed-vs-mutated distinction; detect recognized personal-root entries without following them and refuse unsupported file/link shapes before mutation planning.
- **Non-goal:** transaction redesign, new roots, repair, or platform expansion.
- **Success:** mixed exact/absent operations distinguish noop/applied; file/link roots refuse before any sibling mutation.

### `i002-p3-scope-012` — Make smoke and recovery reporting lane-accurate

- **Sources:** `i002-p2-validate-d-006`, `d-013`, `d-010`.
- **Outcome:** PASS and recovery instructions claim only coverage/artifacts available on the current lane.
- **Scope:** smoke summaries and README recovery sections.
- **Mechanism:** derive/report lane, exercised cases/codes and exclusions; state Bash/Windows exit-18 gaps; split quarantine/recovery guidance by Bash, PowerShell/Windows, and PowerShell/non-Windows. Do not add production hooks unless a separately validated security contract exists.
- **Success:** no summary claims a skipped branch or exit code; every recovery instruction is lane-labelled, inspect-first, exact-leaf, and non-recursive.

## Sequencing

1. Approve version/schema policy.
2. Land ledger identity and lifecycle recommendations 002–006 as one schema-3 release.
3. Land SQL and containment hardening 007–008 with negative tests.
4. Land advisory ingress/binding 009–010 as one contract release.
5. Land installer behavior 011, then reporting/documentation 012.

## Dissent and alternatives preserved

- Optional schema-2 columns were rejected because absence would make normative identities ambiguous.
- A generic artifact table and event-sourced ledger were rejected as scope inflation.
- Computing digests inside the no-tools advisory agent was rejected; parent-side byte binding preserves the profile boundary.
- A regex-only Windows drive check was rejected because it leaves link and shared-resolver gaps.
- Adding Bash production test hooks solely for exit 18 remains out of scope without a validated security contract.

<!-- level-up-complete -->
