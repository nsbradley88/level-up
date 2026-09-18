# Level Up — Iteration 003, Phase 2

## Validation record

- Stable 309/309 evidence window; three independent validators; no subject execution.
- Objective remains `O1` **review-output**. One validator incorrectly restated it as desired-subject-state; that classification is rejected without affecting its evidence determinations.

## Material validated delta

1. **Runtime ownership:** `i003-p2-validate-a-001` — mandatory deterministic checker is not installed; advisory profile externality is intentional. The final design must choose typed owned tooling or explicit pinned host preflight.
2. **Version identity:** `a-002`, `b-015` — v0.6 package versus v0.5 diagnostics/fixtures remains unbound.
3. **Atomic fixture production:** `a-004` — destructive-first regeneration is a robustness defect.
4. **Completion/apply closure:** `b-001`, `b-010` — completed conformant fixture retains planned work; completion must close or explicitly abandon every unit.
5. **Non-self-referential attestation:** `b-002`, `b-003` — one checker row cannot represent prefix/final generations and no completion-ready state gates final completion.
6. **Outcome coupling:** `b-004`, `b-005` — gate and run checker outcomes may conflict; completion rejects only `not-run`, not non-conformant/indeterminate.
7. **Identity/history:** `b-006` — `agent_id` uniqueness and adjudication/challenge generation history are weak; attempt PK itself is present.
8. **Executable attestation contract:** `b-007` — mode/profile/model/tool/digest metadata exists in prose but not machine-checkable schema/artifacts.
9. **Coverage:** `b-009`, `b-011` — coverage mode/path and two evidence tables are unenforced and unexercised.
10. **Apply representation:** `b-010` — sequence, preflight, completion and disposition semantics remain open.
11. **Input error containment:** `b-012` — link-following is disclosed as hostile-host limitation, but uncaught I/O/decode errors collide with non-conformant exit semantics.
12. **Shipped contract drift:** `b-013` — `proposed_upgrade.md` says implemented but disagrees with delivered advisory envelope/profile and test inventory.
13. **Packet interface:** `b-014` — normative frozen packet/document and checker directory/`ledger.sql` interface are not coherently specified.
14. **Installer identity:** `c-003` — Windows receipt-name comparison mixes exact and case-insensitive rules.
15. **Verifier prerequisites:** `c-007` — missing Bash hard-refuses while missing pwsh yields partial PASS; Bash prerequisite is undocumented.

## Validated boundaries/non-material items

- README exact inventory is an intentional presence guard.
- Co-located manifest receipts prove local source consistency, not provenance, and README discloses that boundary.
- CI/release orchestration is external integration, though executable checker tests still need a concrete gate in the PR specification.
- Multi-target-only terminal records and sequential partial application are documented behavior.
- Install path operations remain directory-handle protected; stronger Windows/non-Windows differences are documented.
- Exit 18 is reachable on Windows, but its deterministic smoke coverage is non-Windows-only.
- Location-derived verifier root is intentional relocation behavior.
- Archive fixture stubs are a minor test-value gap because artifact-content truth is explicitly NOT_CHECKABLE.

## Historical reconciliation

Iteration 003 independently reconfirmed the Iteration 002 handoff and added two decisive closure requirements:

- final completion must require a structurally conformant detached result, not merely result existence;
- the shipped `proposed_upgrade.md` must be corrected or removed as an implemented normative claim because it conflicts with actual profile/contract behavior.

The prior broad package-integrity concern is narrowed: whole-tree digest provenance is not required, but mandatory runtime tooling must be owned or preflighted explicitly.

<!-- level-up-complete -->
