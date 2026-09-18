# Level Up — Iteration 002, Phase 5

## Frozen candidate ledger

- Run: `a2fb9f0fa4836911`; objective `O1` is review-output.
- Required adversary: GPT-5.6 Sol (`i002-p5-sol`). Independent second adversary: Claude Opus 5 (`i002-p5-opus`).
- Reviewers received neutral recommendations A–L, not Phase 4 ratings.
- Rows below freeze neutral claims/evidence plus sealed Phase-5 materiality and aggregation disposition. They gain no evidentiary weight until Phase 6.

### GPT-5.6 Sol candidates

| ID | Target | Neutral challenge and evidence | Sealed materiality | Disposition |
|---|---|---|---|---|
| `i002-p5-sol-001` | D,J | Post-completion result cannot be inside the packet it verifies without self-reference. `SKILL.md:514-517,544-547,706`; checker-result PK. | critical | carried |
| `i002-p5-sol-002` | B,C | Validator REVISE rows do not bind target and packet digest, so parent-selected values can masquerade as unanimous agreement. `SKILL.md:331-349,882-885`; `_validate_revise_transition`. | high | carried |
| `i002-p5-sol-003` | B,D,E | Completion/apply credit reduces ancestry to phase names and can reuse stale pre-back-edge passes. `check_ledger.py:1306-1326,2408-2418`. | critical | carried |
| `i002-p5-sol-004` | I,J | Excluding contract bytes from packet digest leaves authoritative ID universes substitutable. `SKILL.md:582-594`. | critical | carried |
| `i002-p5-sol-005` | I | Flat global advisory ID sets permit cross-adjudication swaps. `SKILL.md:590-593`; advisory validator membership logic. | high | carried |
| `i002-p5-sol-006` | F | Loading omitted tables alone does not reject foreign-run rows or run-blind indexes. `_evaluate_content`; transition-only foreign-run check. | high | carried |
| `i002-p5-sol-007` | F,D | Total coverage has no structured item rows and its manifest path is unchecked. `SKILL.md:959-971`; run schema/artifact validation. | high | carried |
| `i002-p5-sol-008` | C | Nullable host agent IDs and mandatory scratchpads cannot represent failure-before-artifact safely. `SKILL.md:331-349,783-795`. | high | carried |
| `i002-p5-sol-009` | H,J | Resolver must cover packet root, ledger, digest inputs and ancestors; referenced-artifact-only hardening is incomplete. Packet reads in `check_ledger.py`. | high | carried |
| `i002-p5-sol-010` | G,H | Untrusted packet sizes/row counts/path counts are unbounded; framing alone does not address CPU/memory exhaustion. Loader/table/duplicate code. | high | carried |
| `i002-p5-sol-011` | A,D–J | Installed payload excludes checker tools, so specification/checker release semantics and archived packets can diverge. Manifest, installers, README integrity boundary. | critical | carried |
| `i002-p5-sol-012` | K,L | Separate success from physical effect; `outcome=applied` plus `action=noop` corrupts mutation telemetry. Installer emitters. | high | carried |
| `i002-p5-sol-013` | D–J | CI runs verifier/smokes but not ledger/advisory unit tests or fixture-regeneration drift. workflow `validate-skills.yml`. | critical | carried |
| `i002-p5-sol-FC001` | G | ATTACH escape challenge failed: rejected before execute and test checks no file creation. | non-material confidence | excluded-failed-challenge |
| `i002-p5-sol-FC002` | H | Basic absolute/empty/dot/traversal lexical paths are already rejected. | non-material confidence | excluded-failed-challenge |
| `i002-p5-sol-FC003` | C | Replacement model/family drift challenge failed; frozen slot profile is checked. | non-material confidence | excluded-failed-challenge |
| `i002-p5-sol-FC004` | L | Missing Bash race mechanism challenge failed; FIFO/backpressure covers selected races. | non-material confidence | excluded-failed-challenge |
| `i002-p5-sol-FC005` | K | Installer symlink-ancestor escape challenge failed; installers reject target ancestry links/reparse points. | non-material confidence | excluded-failed-challenge |

### Claude Opus 5 candidates

| ID | Target | Neutral challenge and evidence | Sealed materiality | Disposition |
|---|---|---|---|---|
| `i002-p5-opus-001` | A | A scalar one-version checker makes schema-2 runs INVALID after a schema-3 release. `check_ledger.py:815-837`; run freezes version before dispatch. | high | carried |
| `i002-p5-opus-002` | A | Extra nullable columns are already accepted; only new keys/tables force a bump. `_validate_schema`. | medium | merged-into-`i002-p5-opus-001` |
| `i002-p5-opus-003` | A | SKILL schema-version sentence and checker constant have no verifier cross-check. `SKILL.md:503`; `check_ledger.py:11`; verifier markers. | medium | carried |
| `i002-p5-opus-004` | A | Every fixture file change requires matching hand-maintained README inventory. `verify_package.py:239-253`. | medium | carried |
| `i002-p5-opus-005` | B | Current state-chain prose is unsatisfiable; enforcing it directly breaks all chains. `SKILL.md:686-719`; transition checker. | high | merged-into-`i002-p2-validate-b-001` |
| `i002-p5-opus-006` | B | Forward transitions are not tied to a passed gate. `_legal_transition`; qualifying pass use. | high | merged-into-`i002-p2-validate-b-002` |
| `i002-p5-opus-007` | B | Objection applicability depends on an unstated producer-vs-review phase convention. `_applicable_open_objection_count`; objection schema. | high | carried |
| `i002-p5-opus-008` | B | No fixture inserts an objection, so objection lineage/gate branches are unexercised. Fixture corpus. | high | carried |
| `i002-p5-opus-009` | C | Positive replacement fixture certifies the rule the SKILL says is forbidden. replacement fixture/test and `SKILL.md:749-750,783-791`. | high | merged-into-`i002-p2-validate-b-003` |
| `i002-p5-opus-010` | C | Duplicate `agent_id` rows collapse in a last-wins dictionary. `check_ledger.py:1018`. | high | merged-into-`i002-p2-validate-a-002` |
| `i002-p5-opus-011` | C | Replacement linkage omits successor back-reference and full coordinate equality. `check_ledger.py:1560-1587`. | high | carried |
| `i002-p5-opus-012` | D | Second deterministic checker generation is unrepresentable. checker-result PK and row-count rule. | high | merged-into-`i002-p2-validate-a-003` |
| `i002-p5-opus-013` | D | Flat checker-result vocabulary permits deterministic `result='conformant'`, contrary to structural-only wording. `CHECKER_RESULTS`; checker-result validation. | high | carried |
| `i002-p5-opus-014` | D | Declared not-checkable/advisory paths are not existence/cross-reference checked. artifact validation. | high | merged-into-`i002-p2-validate-c-B001-D019` |
| `i002-p5-opus-015` | E | Halted-before-write and command-only units cannot represent empty path sets. `_parse_path_list`; apply field rules; `SKILL.md:1071-1074`. | high | carried |
| `i002-p5-opus-016` | E,A | Phase-07 design allowlist has no apply-unit representation; claiming enforcement requires a field or explicit prompt-only limit. apply schema and `SKILL.md:1029-1032,1109-1113`. | high | carried |
| `i002-p5-opus-017` | E | Sequence and terminal disposition are unenforced. apply validator. | high | merged-into-`i002-p2-validate-b-005` |
| `i002-p5-opus-018` | F | Evidence-adjudication/failed-challenge tables are declared but unread and absent from fixtures. schema/evaluator/fixture corpus. | high | merged-into-`i002-p2-validate-c-B002` |
| `i002-p5-opus-019` | F | `coverage_mode` has no vocabulary and total coverage can have null manifest. run schema and SKILL coverage rules. | high | merged-into-`i002-p5-sol-007` |
| `i002-p5-opus-020` | F | Unknown recorded checks are silently filtered from `checked` unless added to `CHECK_SEQUENCE`. report finalization/tests. | high | carried |
| `i002-p5-opus-021` | G | Multi-statement line can raise uncaught `sqlite3.Warning` on supported Python. loader/framer. | high | merged-into-`i002-p2-validate-c-001` |
| `i002-p5-opus-022` | G | Prefix grammar permits `INSERT INTO ... SELECT`, including reads from allowed `sqlite_master`. insert regex/authorizer. | high | carried |
| `i002-p5-opus-023` | G | `OSError` reading ledger escapes structured INVALID handling. `_load_ledger`. | medium | merged-into-`i002-p3-scope-007` |
| `i002-p5-opus-024` | H | Windows drive-qualified artifact path escapes packet intent. path normalizer/join. | high | merged-into-`i002-p2-validate-c-003` |
| `i002-p5-opus-025` | H,J | Host case/trailing-dot semantics can make one packet differ across platforms. direct filesystem probes. | high | carried |
| `i002-p5-opus-026` | H | Packet symlinks are followed. packet/artifact/scratchpad reads. | high | merged-into-`i002-p3-scope-008` |
| `i002-p5-opus-027` | I | Empty contract can waive the mandatory NOT_CHECKABLE minimum; canonical lists are not shared. advisory validator and checker constants. | high | carried |
| `i002-p5-opus-028` | I | Exact-key validation occurs before version dispatch, so v2 looks malformed rather than unsupported. advisory validator. | high | carried |
| `i002-p5-opus-029` | I | Advisory CLI `main`/exit/stdout contract has no tests. advisory unit tests. | medium | carried |
| `i002-p5-opus-030` | I,L | Profile is user-invocable and model-pinned despite proposal/frozen-substitution assumptions; verifier pins this. profile, verifier, proposal. | high | carried |
| `i002-p5-opus-031` | J | Packet digest is undefined and only echoed. SKILL digest prose; advisory validator. | critical | merged-into-`i002-p3-scope-010` |
| `i002-p5-opus-032` | J,D | Checker `packet_path` is a pointer file while deterministic checker consumes a directory. checker evaluation and fixture row. | high | carried |
| `i002-p5-opus-033` | J | Required advisory execution metadata is absent from canonical tree/schema. `SKILL.md:230-250,634-640`. | medium | carried |
| `i002-p5-opus-034` | K | Challenge assumes always-emitting single-target terminal results, which recommendation K did not propose. current gate/smoke/docs. | non-material mismatch | excluded-not-targeted |
| `i002-p5-opus-035` | K,L | Personal-root environment/detection differs by lane and README omits USERPROFILE precedence. target discovery and README. | high | carried |
| `i002-p5-opus-036` | A,L | Verifier refuses without Bash, so Windows-only hosts cannot reach PASS. verifier missing-bash branch. | high | carried |
| `i002-p5-opus-037` | D,L | Mandatory deterministic/reference checker tools are not installed with the one-file payload. manifest/installers/SKILL. | high | merged-into-`i002-p5-sol-011` |
| `i002-p5-opus-038` | L | Hook asymmetry means lane race coverage is not equivalent and must be disclosed. PowerShell hooks/Bash FIFO. | medium | carried |
| `i002-p5-opus-039` | L | Bash FIFO race hard-fails on hosts without Linux `F_SETPIPE_SZ` instead of reporting skip. smoke prerequisite/runtime. | medium | carried |
| `i002-p5-opus-040` | A,L | v0.6.0 checker diagnostics and fixtures still name v0.5.0. checker/fixtures/package identity. | high | merged-into-`i002-p2-validate-b-007` |
| `i002-p5-opus-041` | L | `/tmp` verifier scan is literal and does not prove runtime temp-root policy. verifier/test tempfile usage. | low | carried |
| `i002-p5-opus-042` | G | ATTACH escape failed; rejected before execution and tested for no file. | confidence | excluded-failed-challenge |
| `i002-p5-opus-043` | G | sqlite_master authorizer challenge failed; allowances are CREATE side effects and direct hostile DDL is framed out. | confidence | excluded-failed-challenge |
| `i002-p5-opus-044` | H | Scratchpad traversal failed; path is reconstructed from constrained coordinates before read. | confidence | excluded-failed-challenge |
| `i002-p5-opus-045` | E | Apply path order sensitivity failed; parser sorts and rejects duplicates. | confidence | excluded-failed-challenge |
| `i002-p5-opus-046` | A | Additive-column bump challenge failed; extra columns are accepted. | confidence | excluded-failed-challenge |
| `i002-p5-opus-047` | L | Completeness-token overclaim failed; verifier explicitly reports partial/skipped/refused. | confidence | excluded-failed-challenge |

## Coverage of validated material scope

Every Phase 4 item A–L received at least one evidence-bearing challenge:

- A: schema compatibility, duplicated version source, inventory/release coupling.
- B: causality, objection convention and absent tests.
- C: ambiguous restart, identity, failure-before-artifact.
- D: generation/self-reference, result vocabulary, missing artifact links.
- E: empty-path command/halt cases and unrepresented allowlist.
- F: foreign-run scope, structured coverage, silently filtered checks.
- G: multi-statement Warning, INSERT-SELECT, OSError and resource bounds.
- H: root/all-read containment, host-name semantics and links.
- I: per-adjudication binding, canonical minimum, version dispatch and CLI/profile behavior.
- J: contract substitution, pointer-vs-root identity and execution metadata.
- K: effect telemetry and personal-root lane divergence.
- L: CI omissions, checker availability, lane asymmetry and reporting boundaries.

Evidence-free repetition was omitted. Failed challenges are retained as confidence records but excluded from the material candidate set.

<!-- level-up-complete -->
