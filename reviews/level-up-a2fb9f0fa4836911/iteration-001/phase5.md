# Level Up — Iteration 001, Phase 5

## Run record

- Run: `a2fb9f0fa4836911`
- Phase: adversarial review
- Subject: `C:\Users\nabradl\Repos\tools\copilot-skills\loop2`
- Objective `O1` (`review-output`): produce an evidence-backed review and PR-ready change specification.
- Governing Level Up snapshot: SHA-256 `6e33cb093323e955107c732971d4eedf340cebb1d9c101ed6d01dda45224f4fc`.
- Adjudicated Phase 4 scope: SHA-256 `015164765a86f5ddb778a3cf47a37eebf36e54b9324889337d8d4f543e33c57e`.
- Boundary: static, read-only adversarial review. No candidate below has Phase 6 evidentiary weight.

## Reviewers and neutral scope

Two separate reviewers received the same neutral A–K proposal list without prior ratings or adjudications:

- `i001-p5-adversary-sol` — GPT-5.6 Sol, required adversarial reviewer.
- `i001-p5-adversary-opus` — Claude Opus 5, separate second reviewer.

Each was required to return an evidence-bearing challenge or claim-bounded failed search for every proposal:

- A: same-run child scoping
- B: current protocol-version policy
- C: not-checkable artifact generation/existence
- D: gate derivation and revise evidence
- E: transition, state, and producer-cohort binding
- F: apply-unit invariants
- G: lifecycle and completion projection
- H: restricted-SQL regression depth
- I: fixture cleanup
- J: Bash smoke invocation
- K: native installer smoke coverage

## Frozen candidate ledger

Neutral fields are claim and evidence. Sealed Phase 5 fields are reviewer materiality and aggregation disposition. `merged-into` removes duplicate weight but preserves the source row and evidence. Exclusion is not a Phase 6 validation result.

| Candidate ID | Item | Neutral claim | Neutral evidence | Sealed materiality | Aggregation disposition |
|---|---|---|---|---|---|
| `i001-p5-adversary-sol-001` | A | Required child tables `loop2_evidence_adjudications` and `loop2_failed_challenges` are declared but not loaded; “every child row” scoping must include them. | `tests/check_ledger.py:285-317,991-1001` | material | carried |
| `i001-p5-adversary-opus-001` | A | Filtering alone could silently ignore foreign/orphan rows because the ledger has no referential integrity; scoping must also emit errors. | `tests/fixtures/ledger/conformant/ledger.sql` DDL; `tests/check_ledger.py:1000-1018,2183-2190` | material | carried |
| `i001-p5-adversary-opus-002` | A/E | `phase_versions` discards `run_id`, so foreign phase versions can alter revise version arithmetic even if other collections are scoped. | `tests/check_ledger.py:903,2178-2180,2315-2330` | material | carried |
| `i001-p5-adversary-sol-002` | B | Live checker diagnostics and generated fixtures still identify normative/producing v0.5.0 and must not be preserved as historical text. | `skill.manifest.json:1-11`; `tests/check_ledger.py:965-975,2216-2221`; `tests/fixtures/ledger/generate_fixtures.py:379-400` | material | carried |
| `i001-p5-adversary-opus-003` | B | Exact-current enforcement makes the whole current fixture corpus invalid unless regeneration is atomic with the policy change. | all fixture `ledger.sql` run rows; representative `conformant/ledger.sql:194`; `skill.manifest.json:4` | material | merged-into-`i001-p5-adversary-sol-002` |
| `i001-p5-adversary-opus-004` | B/G | Mapping unsupported protocol versions to `INVALID` shares CLI exit 3 with usage error, short-circuits checks, and prevents current-checker audit of older packets. | `tests/check_ledger.py:596-601,2601-2607`; checked-list tests `tests/test_ledger_checker.py:329-347` | material | carried |
| `i001-p5-adversary-sol-003` | B–G | Normative SKILL edits require manifest digest/size refresh; generated fixture artifacts require exact README inventory updates. | `tests/verify_package.py:230-249,494-505`; `README.md:8-11`; `skill.manifest.json:4-10` | material | carried |
| `i001-p5-adversary-sol-004` | C | Existence-only validation permits an empty `not-checkable.md` despite the normative minimum property list. | `SKILL.md:552-559`; `tests/check_ledger.py:2437-2456` | material | carried |
| `i001-p5-adversary-sol-005` | C | Artifact path validation is lexical and `Path.is_file()` follows links, so a recorded packet-relative path can resolve outside the packet. | `tests/check_ledger.py:917-927,2437-2456` | material | carried |
| `i001-p5-adversary-opus-005` | C/I | Adding fixture artifacts also requires deterministic generator ownership and exact README inventory changes. | `tests/fixtures/ledger/conformant/ledger.sql:194`; fixture tree; `tests/verify_package.py:241-254`; `README.md:8-11` | material | merged-into-`i001-p5-adversary-sol-003` |
| `i001-p5-adversary-opus-006` | C | Three sibling run-level path columns remain unresolved; a targeted not-checkable check could overstate “referenced artifact existence.” | `tests/check_ledger.py:198-206,2470-2472,2537-2545` | material | carried |
| `i001-p5-adversary-sol-006` | D | Existing agent/gate rows and current REVISE scratchpad examples do not deterministically encode revision target and packet. | `SKILL.md:319-411`; `tests/fixtures/ledger/revise_version_gap/.../opus-1-a1.md:1-17`; corresponding `ledger.sql:208-219` | material | carried |
| `i001-p5-adversary-opus-007` | D | Deriving every stored counter duplicates evidence and can classify transient parent write lag as non-conformant; some in-flight states may require missing evidence instead. | `tests/check_ledger.py:1842-1856,1935-2038` | material | carried |
| `i001-p5-adversary-opus-008` | D | Revision packet content truth is explicitly not checkable; achievable binding may be limited to path existence/equality and gate status. | `tests/check_ledger.py` `revision_packet_path` declarations and NOT_CHECKABLE list; `_validate_revise_transition:2289-2346` | material | carried |
| `i001-p5-adversary-sol-007` | E | A checker-side successor map conflicts with text requiring adjacent state equality unless the successor relation becomes normative and exhaustive. | `SKILL.md:716-721`; `tests/fixtures/ledger/generate_fixtures.py:638-653` | material | carried |
| `i001-p5-adversary-opus-009` | E | A successor map is a new normative artifact not derivable from current mixed state/action labels and needs per-edge traceability. | `tests/check_ledger.py:2058-2108,2270-2280`; `tests/fixtures/ledger/conformant/ledger.sql` transition chain | material | merged-into-`i001-p5-adversary-sol-007` |
| `i001-p5-adversary-sol-008` | E | Exact producer-cohort binding invalidates current full-run fixtures because Phase 01/03/05 producer rows are absent. | `tests/fixtures/ledger/generate_fixtures.py:661-733`; `conformant_completed_run/ledger.sql:245-259` | material | carried |
| `i001-p5-adversary-opus-010` | E | REVISE legality is broadly permissive and early returns in detailed validation can leave malformed back-edges incompletely checked. | `tests/check_ledger.py:2100-2108,2289-2346` | material | carried |
| `i001-p5-adversary-sol-009` | F | Apply path parsing coerces non-string JSON values and accepts drive-shaped paths as repository-relative. | `tests/check_ledger.py:917-943` | material | carried |
| `i001-p5-adversary-sol-010` | F | “Disposition or cancelled” leaves incompatible abandonment encodings; one mandatory terminal representation is needed. | `SKILL.md:1184-1200`; `tests/check_ledger.py:107-116`; `conformant_completed_run/ledger.sql:260-261` | material | carried |
| `i001-p5-adversary-opus-011` | F | Phase-07-only restriction needs an explicit non-07 negative fixture before the current generic branch is removed. | `tests/check_ledger.py:55-57,2415-2419`; `tests/test_ledger_checker.py:296-302` | material | carried |
| `i001-p5-adversary-opus-012` | F/B | Cancellation vocabulary and other required changes may interact with exact schema/version acceptance and invalidate earlier v0.6.0 packets. | `tests/check_ledger.py:11,107-113,815-837,2385-2394` | material | carried |
| `i001-p5-adversary-sol-011` | G | Phase-status projection is ambiguous without a normative vocabulary, historical-row rules, and valid terminal-chain behavior. | `SKILL.md:280-329,470-499`; `tests/check_ledger.py:1020-1040,1222-1286` | material | carried |
| `i001-p5-adversary-sol-012` | G | Checker closure is self-referential: one deterministic row cannot simultaneously represent the prefix check and the result currently being computed. | `SKILL.md:456-462,516-552`; `tests/check_ledger.py:2506-2544` | material | carried |
| `i001-p5-adversary-opus-013` | G | “Accumulate all” must preserve existing cardinality/format short-circuits and checked-list semantics. | `tests/check_ledger.py:876-883,1004-1012`; `tests/test_ledger_checker.py:329-347` | material | carried |
| `i001-p5-adversary-opus-014` | G | Projection must enforce the reverse implication from terminal completed transition to completed run status, not only completed-run closure. | `tests/check_ledger.py:77,1094-1096,2546-2552` | material | carried |
| `i001-p5-adversary-sol-013` | H | Bounded search found no statement-family loader bypass; lexical and authorizer layers reject inspected attacks, excluding resource exhaustion. | `tests/check_ledger.py:612-711`; `tests/test_ledger_checker.py:98-125` | not material | excluded-failed-challenge |
| `i001-p5-adversary-opus-015` | H | Lexer admits `INSERT INTO <allowed> SELECT ...`; authorizer permits reads from allowed tables/sqlite_master, potentially violating literal-transcript assumptions. | `tests/check_ledger.py:625-633,692-693`; existing tests `tests/test_ledger_checker.py:99-127` | material | carried |
| `i001-p5-adversary-opus-016` | H | Authorizer is installed after a fixed `BEGIN`; ordering is not pinned by the proposed tests. | `tests/check_ledger.py:697-701` | not material | excluded-minor-fixed-literal |
| `i001-p5-adversary-sol-014` | I | Root parameterization and top-level checks can create a deletion primitive or partial cleanup unless arbitrary roots are test-internal and owned subtrees are recursively pre-scanned before any deletion. | `tests/fixtures/ledger/generate_fixtures.py:13,349-355,783-787` | material | carried |
| `i001-p5-adversary-opus-017` | I | Windows junction/reparse handling may permit or at least complicate out-of-tree recursive deletion; explicit reparse rejection is required. | `tests/fixtures/ledger/generate_fixtures.py:13,783-786` | material | carried |
| `i001-p5-adversary-opus-018` | I | Preserving unknown entries may defer failure to opaque package-inventory errors; cleanup must choose explicit warning versus refusal semantics. | `tests/verify_package.py:232-254` | material | carried |
| `i001-p5-adversary-opus-019` | I | A root-parameterized cleanup helper needs containment/sentinel guards so production callers cannot aim it at arbitrary directories. | generator hard-coded `ROOT`; proposed parameterization surface | material | merged-into-`i001-p5-adversary-sol-014` |
| `i001-p5-adversary-sol-015` | J | Bounded search found no implicit global fallback; the defect is uncontrolled parameter-expansion failure and missing documentation. | `tests/smoke_installer.sh:9-15,40-43`; `README.md:420-434` | not material | excluded-failed-challenge |
| `i001-p5-adversary-opus-020` | J | Existing usage exit 2 covers excess arguments, but missing `TMPDIR` bypasses it; proposal must target all sandbox-resolution failures without assuming parity is required. | `tests/smoke_installer.sh:9-15`; `tests/smoke_installer.ps1:39-47` | material | carried |
| `i001-p5-adversary-sol-016` | K | Smoke summaries need a recorder covering helper-driven and manual race cases, including executed/skipped and observed branch. | `tests/smoke_installer.sh:215-246,865-985`; `tests/smoke_installer.ps1:871-1007,1025-1027` | material | carried |
| `i001-p5-adversary-opus-022` | K | Fixed summaries can assert unconditional coverage when exit 18 is unexecuted on the native host. | final summary in both smoke scripts; `tests/smoke_installer.ps1:836-855`; `README.md:405,428-429` | material | merged-into-`i001-p5-adversary-sol-016` |
| `i001-p5-adversary-sol-017` | K | A Bash synchronization seam requires verifier-enforced hook names, gating, token grammar, timeout, no-follow exclusive files, inert partial configuration, and exit-18 end-state assertions. | `tests/verify_package.py:276-427`; `install.ps1:489-523`; absence in `install.sh` mutation path | material | carried |
| `i001-p5-adversary-opus-021` | K | Adding the seam changes the production Bash installer and must be separated into bounded instrumentation plus smoke coverage with verifier parity. | absence in `install.sh`; PowerShell hook `install.ps1:500-503,1246,1379,1443,1503`; verifier hook checks | material | merged-into-`i001-p5-adversary-sol-017` |

## Scope accounting

Every A–K item received at least one evidence-bearing challenge or bounded failed search:

| Item | Material candidates carried | Duplicate/material rows merged | Failed/minor rows excluded |
|---|---:|---:|---:|
| A | 3 | 0 | 0 |
| B | 3 | 1 | 0 |
| C | 3 | 1 | 0 |
| D | 3 | 0 | 0 |
| E | 3 | 1 | 0 |
| F | 4 | 0 | 0 |
| G | 4 | 0 | 0 |
| H | 1 | 0 | 2 |
| I | 3 | 1 | 0 |
| J | 1 | 0 | 1 |
| K | 2 | 2 | 0 |

All validated material Phase 4 scope items received an evidence-bearing challenge. H also received a bounded failed attack that adds confidence to the current loader, while a separate reviewer identified a narrower `INSERT ... SELECT` concern. Evidence-free hypotheticals: four from the second reviewer and zero from GPT-5.6 Sol; they are not ledger rows.

## Material challenge summary

The strongest new challenges are:

1. the central scoping proposal itself omitted required but unloaded child tables and a run-dropping `phase_versions` derivation;
2. not-checkable existence validation may follow links outside the packet and does not establish the normative minimum content;
3. current wire evidence does not deterministically encode a REVISE target/packet without an exact grammar or field;
4. checker closure may be self-referential under a single deterministic-result row;
5. apply path parsing admits non-string and drive-shaped values;
6. the SQL loader may admit `INSERT ... SELECT`, changing H from tests-only if confirmed;
7. cleanup parameterization and unknown-entry policy can create new deletion or opaque-failure hazards;
8. the Bash synchronization seam needs a verifier-enforced security contract rather than copying the PowerShell token handling.

## Phase 6 needs

Independent validators must initially receive only each row's ID, item, neutral claim, and evidence. They must:

- validate every carried row and every disputed merge/exclusion that could change materiality or convergence;
- reconcile contradictory artifact-link and Windows-junction claims from Phases 4 and 5 using primary evidence;
- determine whether empty not-checkable content is a structural defect or intentionally not-checkable;
- determine whether `INSERT ... SELECT` is actually admitted and material under the loader contract;
- determine whether unsupported protocol version should remain `INVALID` despite legacy-audit and exit-code objections;
- determine whether the single deterministic checker-row contract is genuinely self-referential;
- distinguish required specification changes from implementation acceptance criteria already implicit in Phase 4.

<!-- level-up-complete -->
