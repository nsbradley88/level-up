# Level Up — Iteration 002, Phase 2

## Run and evidence window

- Run: `a2fb9f0fa4836911`; iteration axis: contract-boundary closure.
- Subject: `C:\Users\nabradl\Repos\tools\copilot-skills\loop2`.
- Objective `O1` (`review-output`): evidence-backed review and PR-ready change specification.
- Immediately before validation, all 309 manifested files matched their SHA-256 identities.
- Four fresh validators independently reconstructed neutral claims. No project code, tests, fixtures, or installers were executed.
- This aggregate reconciles the frozen validation record with Iteration 001 only after current determinations were made.

## Validated material record

### Identity, cardinality, and advisory ingress

| Validation ID | Phase 1 alias | Determination | Validated finding and evidence | Historical relation |
|---|---|---|---|---|
| `i002-p2-validate-a-001` | `i002-p1-research-a-001` | supported, material | `loop2_runs.phase` lacks an active `phase_version`, although phase identity is composite and multiple versions can coexist. `SKILL.md:278-329`; `check_ledger.py:2562-2569`; `verdict_void_round/ledger.sql:194,210-211`. | New material refinement of Iteration 001 lifecycle/state-coherence findings. |
| `i002-p2-validate-a-002` | `a-002` | supported, material | Scalar `replaced_agent_id` cannot reliably reference composite agent-attempt identity; the checker's `agent_id` dictionary can collide. `SKILL.md:331-349`; `check_ledger.py:1018,1573-1593`. | New identity defect underlying the previously validated replacement-round weakness. |
| `i002-p2-validate-a-003` | `a-003` | supported, material | `(run_id, checker_type)` retains only one deterministic result although prefix and post-completion checks are mandatory. `SKILL.md:455-462,544-553`; `check_ledger.py:2506-2515`. | Reconfirms and sharpens Iteration 001 checker-stage finding. |
| `i002-p2-validate-a-004` | `a-004` | supported, material | Advisory contract IDs are checked for sorted membership but not full-ID grammar. `check_advisory_result.py:39-50,82-85,110-124`; `SKILL.md:621-630`. | New material contract-ingress gap. |
| `i002-p2-validate-a-005` | `a-005` | supported, material | Empty adjudication and result arrays can return `STRUCTURALLY_CONFORMANT`; no explicit zero-case outcome exists. `check_advisory_result.py:39-50,89-91,151-160`. | New material contract-boundary gap. |
| `i002-p2-validate-a-007` | `b-009` | supported, material/qualified | No-tools digest echo is intentional, but parent-side exact-byte digest computation and linkage are not normatively specified. Agent profile lines 18-22; validator lines 76-80. | Qualifies Iteration 001's already disclosed no-tools limitation; do not require the advisory agent to hash. |

### Ledger causality, lifecycle, replacement, and closure

| Validation ID | Alias | Determination | Validated finding | Historical relation |
|---|---|---|---|---|
| `i002-p2-validate-b-001` | `c-001` | supported, material | Normative adjacent state-string equality is incompatible with generated transition labels; phase status also lacks a vocabulary/check. `SKILL.md:770-772`; `check_ledger.py:1222-1287,2258-2280`; conformant transition rows. | Reconfirms Iteration 001 state-continuity gap with stronger direct contradiction. |
| `i002-p2-validate-b-002` | `c-002` | supported, material | Transition legality reads phases/labels but not exact gate, agent, objection, or snapshot evidence. `check_ledger.py:2058-2222`; `SKILL.md` gate predicate 8. | Same core finding as Iteration 001 transition-causality defect. |
| `i002-p2-validate-b-003` | `c-003` | supported, material | One-slot replacement can combine one attempt-2 ballot with three stale attempt-1 ballots despite the rule that replacement voids the round and all four redeclare. `SKILL.md:753,787-795`; `check_ledger.py:1560-1575,1737-1741`; `verdict_replaced_slot`. | New direct positive-fixture proof of the previously suspected cohort defect. |
| `i002-p2-validate-b-004` | `c-004` | supported, material | REVISE back-edges omit four-ballot, gate-row, and revision-packet existence/binding checks. `check_ledger.py:2289-2345,2458-2504`. | Reconfirms Iteration 001 REVISE representation and artifact-link findings. |
| `i002-p2-validate-b-005` | `c-005` | supported, material | Apply units are not confined to Phase 07; sequence, preflight, and terminal disposition invariants are weak. `check_ledger.py:2347-2434`; `SKILL.md` execution/final-record rules. | Reconfirms Iteration 001 apply closure. |
| `i002-p2-validate-b-006` | `c-006` | supported, material | One checker-result row cannot preserve both mandatory deterministic checks. | Duplicate of `i002-p2-validate-a-003`; merged there. |
| `i002-p2-validate-b-007` | `c-007` | supported, material/qualified | Checker diagnostics and generated fixtures remain v0.5.0 while package identity is v0.6.0; compatibility is unenforced. Historical v0.5.0 fixture data may remain valid only under an explicit compatibility policy. | Reconfirms Iteration 001 release-identity drift. |
| `i002-p2-validate-b-009` | `c-009` | supported with one contradicted limb, material | Completion does not require the missing `not-checkable.md`, Phase 01/03/05 producer cohorts, or final synthesis structure. Frozen packet existence is already enforced and is removed from this finding. | Reconfirms Iteration 001 absent cohorts/artifacts; corrects overbroad frozen-packet claim. |
| `i002-p2-validate-b-010` | `b-012` | supported, material | Replaced and void rows skip first-line verdict agreement with their retained immutable scratchpads. `check_ledger.py:1500-1501,1672-1682`; `SKILL.md:836-840`. | New narrow replacement-audit gap. |
| `i002-p2-validate-b-012` | `b-014` | supported, material | `checked` records validators even when no applicable rows exist, overstating exercised coverage. `check_ledger.py:990-1096,2225-2226`; `wrong_review_pair`. | New material reporting-integrity finding. |

### Artifact containment, fixture coverage, and parser framing

| Validation ID | Alias | Determination | Validated finding | Historical relation |
|---|---|---|---|---|
| `i002-p2-validate-c-001` | new Phase 2 | supported, material | Restricted SQL framing is physical-line-dependent; multiple statements on one line are not split and error classification varies by first token. `check_ledger.py:612-660,701-711`; SQL tests only cover separately lined hostile statements. | Independently confirms Iteration 001 Phase 6 SQL robustness finding. |
| `i002-p2-validate-c-002` | new Phase 2 / `c-007` | supported, material | Package/ledger `skill_version` is unbound and fixtures hardcode v0.5.0. | Merged into `i002-p2-validate-b-007`. |
| `i002-p2-validate-c-003` | `d-018` refinement | supported, material | On Windows, drive-qualified `D:artifact.md` can pass POSIX-relative checks and rebase native path resolution outside the packet. `check_ledger.py:917-926,2437-2454`; no hostile-path fixture. | New concrete platform instance of Iteration 001 packet-containment weakness. |
| `i002-p2-validate-c-B001-D019` | `b-001`, `d-019` | supported, material | `not_checkable_path` is populated but the artifact is absent and not resolved by `_validate_referenced_artifacts`. `generate_fixtures.py:407`; `check_ledger.py:2458-2503`. | Reconfirms Iteration 001 missing `not-checkable.md`. |
| `i002-p2-validate-c-B002` | `b-002` | partially supported, material | Evidence-adjudication and failed-challenge tables exist in DDL but cannot be emitted by generator maps and are never loaded by checker evaluation. | Expands Iteration 001 unloaded-table finding. |
| `i002-p2-validate-c-D018` | `d-018` | supported, material | No negative fixture covers traversal, absolute, drive-qualified, or link-mediated artifact escapes. | Supports `i002-p2-validate-c-003` and Iteration 001 containment recommendation. |

### Installer findings retained as material review scope

| Validation ID | Alias | Determination | Validated finding | Historical relation |
|---|---|---|---|---|
| `i002-p2-validate-d-004` | `b-006` | supported, material | Terminal `outcome='applied'` is also emitted for `action='noop'` exact/absent items; README does not define this semantic. `install.sh:812-819`; `install.ps1:1626-1635`. | New moderate reporting-contract defect. |
| `i002-p2-validate-d-006` + `d-013` | `b-016`, `d-011` | supported, material | Smoke summaries are literal/unconditional; conditional race branches may use fallback behavior while the final banner still claims race coverage. | Refines Iteration 001 smoke-reporting asymmetry. |
| `i002-p2-validate-d-009` | `b-019` | supported, material | File-shaped or dangling-link personal roots are accepted during discovery, then can turn a multi-root mutation into exit 14/15. README says roots are detected homes and no smoke covers this. | New bounded installer-input defect. |
| `i002-p2-validate-d-010` | `d-007` | supported, material | Lane-neutral recovery text tells Bash/Windows users to inspect `.loop2.quarantine.*`, which only PowerShell non-Windows fallback creates. | New documentation correctness finding. |

## Validated but non-material or intentionally bounded

- `i002-p2-validate-a-006` / `b-008`: the static profile's external registration is an intentional, documented packaging boundary.
- `i002-p2-validate-a-008` / `b-010`: repeated `schema_version` naming is non-material envelope naming debt.
- `i002-p2-validate-b-008` / `c-008`: historic checker-result rows are not reconciled to current evaluation; this is documentation/audit-model ambiguity, not a current truth claim.
- `i002-p2-validate-b-011` / `b-013`: `VOID` is intentionally a disposition, not an agent verdict.
- `i002-p2-validate-b-013`, `b-014`, `b-015`, `b-016`: prefix/void fixture isolation, authority wording, and DDL pinning are low-risk test/documentation debt.
- `i002-p2-validate-c-B020`, `B021`, `D020`, `D001`, `D002`, `D003`: cleanup, fail-fast diagnostics, heredoc framing, parser asymmetry, and literal payload grammar are bounded or low materiality.
- `i002-p2-validate-d-001`, `d-002`, `d-003`, `d-005`, `d-007`, `d-008`, `d-011`, `d-012`, `d-014`, `d-015`: residue compatibility, single-target terminal suppression, test-hook authority, action-oracle duplication, and regex verification are documented or low-risk. The Bash FIFO race has indirect assertions that prove ordering and fails loudly rather than silently passing.

## Historical reconciliation and knowledge delta

Iteration 002 did not overturn any material Iteration 001 disposition. It added material validated knowledge:

1. active phase identity needs a version dimension;
2. replacement identity must reference a unique composite attempt;
3. the current positive replacement fixture proves stale cohort ballots are accepted;
4. advisory ingress permits malformed contract IDs and a vacuous empty contract;
5. Windows drive-relative artifact paths can escape packet-root intent;
6. `checked` can overstate exercised validator coverage;
7. terminal no-op results, personal-root shape, and recovery text have bounded contract defects.

It also independently reproduced the Iteration 001 SQL framing defect and narrowed several earlier claims. This is a material increase in validated knowledge, so stagnation is not established.

## Phase 3 eligibility

Phase 3 may derive recommendations only from the material supported/qualified record above. It must merge duplicate mechanisms:

- central run identity and scoped child-table loading;
- stage/generation-aware checker records and exact packet binding;
- causal transition/gate/revision closure;
- cohort-wide replacement and immutable scratchpad agreement;
- apply/lifecycle closure;
- release/version policy;
- artifact existence and containment;
- SQL statement framing/error normalization;
- advisory contract ingress;
- truthful installer/smoke reporting.

It must not reopen external profile registration, broaden installed payload ownership, or turn documented platform support boundaries into defects.

<!-- level-up-complete -->
