# Level Up — Iteration 003, Phase 6

## Reconciled adversarial validation

Independent validators confirmed the material challenges. They found no new research axis; every blocker is resolvable as a specification, acceptance, baseline, or release-order condition.

Key reconciliations:

- runtime ownership, digest graph, schema policy, replacement cardinality, per-gate receipt identity, PR triggers and executable acceptance oracles are material;
- SQL exploit amplification, mandatory archived-schema support, generalized claim/evidence modeling and lane-parity claims are rejected or narrowed;
- fixture safety needs staged/journaled recoverability, not an unqualified atomic-directory claim;
- generated fixtures are checker evidence; one producer-to-checker integration packet is required for release evidence;
- current dirty/untracked content must be frozen/imported as a reviewable baseline before staged implementation.

## Final decisions

1. **Runtime ownership:** package the deterministic checker and shared machine contracts as typed owned payloads with digest/version binding and an exact installed invocation path. Advisory profile registration remains external and optional.
2. **Schema/archive policy:** the current checker supports the current ledger schema only. Unsupported schemas are `INVALID`; in-flight runs pin their checker version. Archived audit is a non-goal unless a versioned checker is retained explicitly.
3. **Attestation graph:** packet manifest excludes itself and all contracts/results; contract binds packet digest; result binds packet, contract and checker identity; terminal receipt binds result. Every digest is recomputed from canonical files.
4. **Lifecycle cardinality:** active head is the terminal transition. Gates reference immutable check receipt IDs and exact candidate/cohort generation. Any validator replacement starts a new round with four fresh declarations. REVISE declarations bind target and packet digest.
5. **SQL boundary:** retain relational SQL interchange with a bounded tokenizer grammar: one BEGIN, required CREATE statements, literal VALUES-only INSERTs, one COMMIT; no SELECT, expressions, comments or extra statements. Normalize I/O/decoding/SQLite failures and limits.
6. **Evidence scope:** validate row ownership, references, counts, objection/evidence/challenge generations and conditional total-coverage closure. Do not add a general claim graph; truth, adequacy and provenance remain NOT_CHECKABLE.
7. **Apply closure:** explicit plan allowlists/effects, empty verification/halted effects, active Phase-07 authorization, sequence/status/disposition matrix, and no open unit at completion-ready.
8. **Fixture safety:** compare-only default; explicit write; fresh staging tree; generated-name allowlist; journal/commit marker; deterministic resume/rollback; injected-failure tests.
9. **Release integration:** freeze/import the current 309-file baseline, then use reviewable commits. The repository workflow is a required external deliverable with `pull_request` trigger, ledger/advisory suites, regeneration compare, verifier structured-field parsing, producer-to-checker integration, and native Windows path tests.
10. **Installer/reporting:** domain-specific Windows case policy; explicit preflight/post-state/effect record semantics; USERPROFILE precedence; exact per-lane coverage; hook-free Bash exit-18 permission test; no parity claim.
11. **Documentation:** demote `proposed_upgrade.md` to non-normative history; reconcile mandatory checker wording, verifier prerequisites, trust boundaries and lane recovery.

## Acceptance-oracle requirement

Every change item in `final.md` must name:

- fixture or setup;
- invocation and lane/OS;
- expected exit and result;
- exact diagnostic set;
- filesystem/digest postcondition.

Exact restored items from Iteration 002: REVISE target/digest binding, objection coordinates and fixtures, unknown-check rejection, USERPROFILE handling, checker-type result vocabularies, all-child run scoping and Windows portable-path cases.

## Convergence

**Converged for `O1` review-output.**

Confirmed subject defects remain implementation work and are not claimed fixed. No material finding remains open against the review-output objective because every validated blocker has a selected disposition and observable acceptance condition.

Separate convergence checker: `CONVERGED`; it found no violated condition. The dynamic checker was instructed to use no tools; host-enforced no-tools isolation was unavailable.

Iteration history:

- Iteration 001: not converged; core structural and SQL defects discovered.
- Iteration 002: not converged; identity, advisory, containment and attestation boundaries sharpened.
- Iteration 003: converged; release ownership, cardinality, acyclic attestation and executable gates resolved.

<!-- level-up-complete -->
