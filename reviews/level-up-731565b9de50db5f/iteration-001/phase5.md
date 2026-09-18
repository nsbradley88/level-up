# Level Up Phase 5 — Adversarial review

## Run record

- Run `731565b9de50db5f`, iteration `001`.
- Separate GPT-5.6 Sol and Claude Opus 5 reviewers received a neutral extract of
  all eleven retained scope items and primary evidence locations, without prior
  ratings, dispositions, or advocacy.
- Both reviewers remained read-only. Every scope item received an
  evidence-bearing challenge or an evidence-bearing failed challenge.

## Frozen candidate ledger

The neutral claim and evidence columns are the Phase 6 input. Materiality and
aggregation disposition are sealed Phase 5 fields.

| Candidate ID | Neutral claim | Evidence location | Phase 5 materiality | Aggregation disposition |
|---|---|---|---|---|
| `i001-p5-sol-001` | Loading the untrusted ledger before schema validation may permit SQLite operations outside the in-memory database; constrain SQL before execution. | `tests/check_ledger.py` ledger load around lines 612–626 | critical | carried |
| `i001-p5-sol-002` | Use one canonical structural schema representation and verify derived consumers semantically. | `SKILL.md` DDL; generator DDL; checker `REQUIRED_*` constants | high | carried |
| `i001-p5-claude-001` | Three independent schema representations lack an equivalence check. | same three schema surfaces; verifier marker checks | high | merged-into-`i001-p5-sol-002` |
| `i001-p5-sol-003` | Validate normalized SQLite defaults and drift. | normative defaults, generator omissions, `_validate_schema` | high | carried |
| `i001-p5-claude-002` | Safety-relevant defaults are documented but unenforced. | `SKILL.md` defaults; checker `PRAGMA table_info`; conformant fixtures | high | merged-into-`i001-p5-sol-003` |
| `i001-p5-sol-004` | Define semantic destination-to-next-source state continuity rather than literal prose equality. | `SKILL.md` transition rule; `_validate_transition_order`; generator transition states | high | carried |
| `i001-p5-claude-003` | Adjacent transition validation omits state despite the normative rule. | `_validate_transition_order`; `_legal_transition` | high | merged-into-`i001-p5-sol-004` |
| `i001-p5-claude-004` | REVISE legality and REVISE-specific validation use separate predicates that can drift. | `_legal_transition`, `_is_revise_transition`, `_validate_revise_transition` | medium | carried |
| `i001-p5-sol-005` | Define mutation-bearing apply-unit statuses and restrict those rows to Phase 07. | Phase 07/09 rules; `_validate_apply_units` generic fallback | high | carried |
| `i001-p5-claude-005` | Non-07 non-planned units can satisfy a weaker earlier-PASS rule. | apply mapping and fallback; Phase 09 no-mutation text | high | merged-into-`i001-p5-sol-005` |
| `i001-p5-claude-006` | Planned-row shape and exemptions are already represented and tested. | `_validate_apply_units`; positive apply tests | low confidence record | carried |
| `i001-p5-sol-006` | Blocked/suspended cause consistency needs a taxonomy, but operator-initiated suspension is not currently normative. | state rules; `suspended_reason`; resource states | high | carried |
| `i001-p5-claude-007` | Blocked/suspended states and `suspended_reason` have no checker consistency rule. | schema, run status vocabulary, resource validation | high | merged-into-`i001-p5-sol-006` |
| `i001-p5-sol-007` | Add bounded objection-lineage and gate fixtures. | objection and gate logic; generator scenario list | high | carried |
| `i001-p5-claude-008` | Substantial objection logic has no direct test. | `_validate_objections`; tests and fixture names | high | merged-into-`i001-p5-sol-007` |
| `i001-p5-sol-008` | Add invalidation fixtures including downstream and cross-phase cases. | invalidation rules; generator default null fields; qualifying-pass logic | high | carried |
| `i001-p5-claude-009` | Back-edge invalidation checks have no direct test. | phase invalidation and completed-run checks; test search | high | merged-into-`i001-p5-sol-008` |
| `i001-p5-sol-009` | Select one genuinely uncovered structural branch per cohort, scratchpad, and model-binding area rather than apply a numeric quota. | `NOT_CHECKABLE`; existing substitution tests | medium | carried |
| `i001-p5-claude-010` | Scratchpad negatives are absent while model-profile coverage partly exists. | scratchpad path/heading validators; model tests | medium | merged-into-`i001-p5-sol-009` |
| `i001-p5-sol-010` | Vocabulary omission does not prove `loop2_phases.status` is non-normative; describe it as opaque/not currently checked unless semantics are established. | phases DDL, vocabularies, `_validate_phases` | medium | carried |
| `i001-p5-claude-011` | If phase status remains free-text, documentation must explicitly say the deterministic checker does not validate it. | phase status DDL and missing vocabulary/check | medium | merged-into-`i001-p5-sol-010` |
| `i001-p5-sol-011` | Document unsupported direct PowerShell invocation as host-native failure with no guaranteed installer JSON or installer exit code. | `install.ps1` prologue; README prerequisite; Bash runtime guard | medium | carried |
| `i001-p5-claude-012` | The PowerShell pre-execution boundary is real, but the exact claimed “13-error” cascade is untested. | installer comment; README; verifier and smoke prerequisites | medium | merged-into-`i001-p5-sol-011` |
| `i001-p5-sol-012` | Recovery guidance is missing, and README may incorrectly group ABSENT with list behavior. | recovery section; exit table; installer list/verify exits | medium | carried |
| `i001-p5-claude-013` | Codes 15, 16, 17, and 19 lack runbooks; ABSENT needs no destructive cleanup. | README exit and recovery sections | high operational | merged-into-`i001-p5-sol-012` |
| `i001-p5-claude-014` | Behavioral checker defects should outrank documentation-only items. | demonstrated CONFORMANT gaps versus S9–S11 documentation changes | high prioritization | carried |

## Source accounting and scope coverage

- All 26 evidence-bearing source candidates are admitted or explicitly merged;
  none is silently dropped.
- Evidence-free repetition count: `0`.
- S1 received `sol-002`, `claude-001`, and the cross-cutting prerequisite
  `sol-001`.
- S2 received `sol-003`, `claude-002`.
- S3 received `sol-004`, `claude-003`, `claude-004`.
- S4 received `sol-005`, `claude-005`, with failed challenge/confidence record
  `claude-006` for the planned-row half.
- S5 received `sol-006`, `claude-007`.
- S6 received `sol-007`, `claude-008`.
- S7 received `sol-008`, `claude-009`.
- S8 received `sol-009`, `claude-010`.
- S9 received `sol-010`, `claude-011`.
- S10 received `sol-011`, `claude-012`.
- S11 received `sol-012`, `claude-013`.
- Cross-scope prioritization received `claude-014`.

## Adversarial implications

The new untrusted-SQL candidate is outcome-changing if confirmed because the
review and checker both claim a read-only/untrusted-evidence boundary. The
adversaries otherwise reinforce the behavioral core but narrow three items:
operator suspension should not be invented; phase status should not be declared
non-normative merely from vocabulary absence; and ABSENT guidance must
distinguish verify from list behavior. Phase 6 must independently establish
materiality and classification before seeing or relying on these sealed
judgments.

<!-- level-up-complete -->
