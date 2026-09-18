# Level Up Phase 2 — Research validation

## Run record

- Run `731565b9de50db5f`, iteration `001`.
- Subject and objective are unchanged from Phase 1.
- Phase 2 opening identity: 305 files, aggregate identity-manifest SHA-256
  `d6fa6309b86e15e2913013b56c374a7fe34cb6997a4397c18cfd4adff29060de`.
- Closing comparison found zero changed file identities; no subject drift was
  observed during this evidence window. This does not prove continuity.
- Three fresh validators reconstructed checker, installer, and assurance claims
  from primary evidence. They did not receive prior ratings or advocacy.

## Validated research record

### Supported material findings

- `i001-p1-research-a-001` — **supported/material**. The checker implements
  objection lineage and open-objection gate behavior, but generated fixtures
  and tests contain no objection rows or objection-focused assertions.
  Evidence: `tests/check_ledger.py::_validate_objections`,
  `_applicable_open_objection_count`;
  `tests/fixtures/ledger/generate_fixtures.py`; and
  `tests/test_ledger_checker.py`. Affects the reliability objective; no
  non-waivable constraint; open.
- `i001-p1-research-a-002` — **partially supported/material**. The supported
  portion is that `invalidated_by_*`, permanent invalidated-PASS suppression,
  and nonzero `invalidated_pass_count` lack fixture coverage. The broad claim
  that all back-edge behavior is untested is unsupported because REVISE source
  and version-gap negatives exist. Affects anti-laundering reliability; open
  only for invalidation coverage.
- `i001-p1-research-a-003` — **partially supported/material**. Many core
  branches remain unasserted, including objection, scratchpad, model-profile,
  suspended/blocked, and selected cohort paths. The mechanical headline that
  core gate logic has no assertions was overgeneralized: candidate pairing,
  ancestry, apply prerequisites, and related gate branches have coverage.
  Affects checker assurance; open in qualified form.
- `i001-p1-research-a-004` — **supported/material**. `SKILL.md` requires each
  transition's phase, version, and state to connect to the preceding
  destination; `_validate_transition_order` checks only phase and version.
  Per-row legality does not establish inter-row state continuity. Affects
  checker truthfulness; open.
- `i001-p1-research-a-006` — **supported/material**. Suspended and blocked run
  states can be structurally accepted without a recorded blocking reason or
  consistent resource observation. Validator claim
  `i001-p2-validator-a-011` is merged into this finding because it identifies
  the same missing lifecycle semantics. Affects lifecycle truthfulness; open.
- `i001-p1-research-a-007` — **supported/material**. Non-planned apply units
  outside `07-execute` can use the generic "any earlier qualifying PASS" path,
  although the normative contract confines mutation to Phase 07. Affects
  parent-only mutation discipline; open.
- `i001-p1-research-a-009` — **supported/material**. Fixture DDL omits normative
  defaults and `IF NOT EXISTS`; `_validate_schema` does not inspect defaults.
  The current suite therefore does not prove that the canonical normative DDL
  is the schema under test or detect default drift. Affects schema assurance;
  open.
- `i001-p1-research-a-010` — **supported/material**. Normative DDL, generator
  DDL/columns, and checker schema constants are manually duplicated and already
  differ on defaults. Affects drift resistance; open.
- `i001-p1-research-b-001` — **supported/qualified materiality**.
  `#requires -Version 7.3` fails before installer code can emit a structured
  refusal, while Bash emits a structured Python-runtime refusal. Both lanes
  fail closed and the PowerShell choice intentionally replaces a parse cascade
  with an actionable engine error. Open only as a machine-readable contract and
  coverage question, not as an installation-safety defect.
- `i001-p1-research-b-006` — **supported/qualified**. PowerShell smoke cannot
  exercise an unsupported interpreter because both installer and smoke script
  require 7.3 before execution. This is a structural consequence of B001.
  Affects runtime-floor assurance; open if structured parity is desired.
- `i001-p1-research-c-005` — **supported/qualified materiality**. Dedicated
  recovery procedures are absent for codes 15, 16, 17, 19, and 20. ABSENT needs
  no recovery, but mixed refusal, race, SOURCE_INVALID, and OWNED_OTHER would
  benefit from explicit next steps. Affects operator recovery; open.

### Supported positive confidence records

- `i001-p1-research-a-008` — **partially supported/closed confidence record**.
  The manifest's v0.5.0 payload path, size, and digest are internally and
  on-disk consistent. Its manifest schema version is distinct from ledger
  schema version 2, so the original word "all surfaces" was too broad.
- `i001-p1-research-c-001` — **supported/closed confidence record**. README,
  verifier logic, and the observed package tree agree on 305 files.
- `i001-p1-research-c-002` — **supported/already disclosed**. LF assurance is
  policy-declaration based rather than a byte scan; README states that limit.
- `i001-p1-research-c-003` — **supported/already disclosed**. Manifest identity
  intentionally covers only `SKILL.md`; README states that boundary.
- `i001-p1-research-c-004` — **supported/outside subject boundary**. Structured
  fields and explicit CI guidance exist; misuse of the stable PASS token is a
  downstream integration risk, not a subject defect.

### Qualified, contradicted, or non-material installer claims

- `i001-p1-research-b-002` — **partially supported/already disclosed**. A real
  asymmetry exists: Bash resolves a repository symlink before classification,
  while PowerShell's lexical normalization followed by reparse checks refuses
  it. The claim that PowerShell alone rejects linked target ancestry or that
  the asymmetry is unsafe is contradicted; both lanes reject unsafe target
  chains, and README intentionally documents PowerShell as stricter. Closed as
  accepted design.
- `i001-p1-research-b-003` — **supported but non-material**. PowerShell ships
  inert, allowlisted, dual-environment-gated synchronization hooks; Bash uses
  external IPC. The extra surface is real, but no meaningful production risk
  was established and README discloses the limitation. Closed.
- `i001-p1-research-b-004` — **supported/already disclosed**. PowerShell's
  non-Windows fallback is path-based and lacks Bash descriptor binding. The
  package explicitly labels this lane best-effort and directs Unix use to Bash.
  Closed as accepted bounded support.
- `i001-p1-research-b-005` — **supported but non-material**. Receipt JSON key
  order differs, but all product comparisons are structural and no byte-parity
  contract exists. Closed.
- `i001-p2-validator-b-001` — **supported but non-material/already disclosed**.
  Parent-directory crash durability is not guaranteed equivalently across
  lanes. README already states the limitation. Closed.

### Other supported but lower-priority schema clarity

- `i001-p1-research-a-005` — **supported/qualified**.
  `loop2_phases.status` is free-form while `gate_status` is enumerated. This can
  be valid as descriptive state, but the contract should say so or define a
  vocabulary. Affects clarity more than current behavior; open for scoping.

## Historical reconciliation

The prior v0.4.0 review package, run `a044b8357dda3c32`, is history rather than
fresh evidence. Current relations are:

- Prior F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, and the implemented portions
  of F11/F12 are observed resolved or materially improved by v0.5.0's package
  identity, terminal outcomes, runtime floor, support-lane documentation,
  recovery semantics, cause-specific verifier reporting, verdict disposition,
  structured INVALID handling, connected phase/version transitions, and
  expanded fixtures.
- `i001-p1-research-a-004` is a residual child of prior F11: phase/version
  connectivity improved, but state connectivity remained unenforced.
- `i001-p1-research-a-001`, `-002`, `-003`, `-009`, and `-010` are second-order
  assurance findings exposed by the larger F12 fixture/checker surface, not
  evidence that the earlier implementation failed wholesale.
- `i001-p1-research-b-001` and `-006` refine prior F3: the Bash/Python floor is
  fixed, while PowerShell's pre-execution refusal remains intentionally
  unstructured and un-smokeable.
- `i001-p1-research-c-005` extends prior F5 from remnant-state accuracy to
  complete operator recovery guidance.

No prior agreement adds evidentiary weight. Current dispositions rely on the
v0.5.0 subject evidence above.

## Phase 3 inputs

Only supported or explicitly qualified findings proceed. Scoping should
prioritize: canonical-schema assurance; transition-state connectivity;
Phase-07-only apply enforcement; suspended/blocked consistency; targeted
objection, invalidation, cohort, scratchpad, and model-profile negatives; and
missing recovery runbooks. It should treat PowerShell structured runtime
refusal as an explicit product choice with alternatives, not an assumed defect.

<!-- level-up-complete -->
