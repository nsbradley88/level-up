# Custom Agent Extraction Experiment: Loop2 v0.5.0 Replication

## Executive summary

This experiment repeated the earlier custom-agent extraction comparison against
an exact clone of Loop2 v0.5.0.

The tested responsibility was narrow advisory conformance checking: applying a
frozen objective, constraint set, candidate ledger, and draft adjudication
without inspecting the subject, reopening evidence, or changing dispositions.

Across two matched replications and four blinded cases per run, the dynamically
provisioned and static custom-agent arms produced the same correct verdicts.
The custom agent used 65.1% less input context and 49.8% fewer reported AI
credits, while taking 6.5% longer.

The result replicates the earlier efficiency finding under a stricter packet.
It supports an optional static, tool-less checker with a dynamic fallback. It
does not show that static agents provide stronger assurance.

## Subject identity

The experiment used an isolated filesystem clone of Loop2 v0.5.0:

`C:\Users\nabradl\Repos\loop2-extraction-experiment-v050-80afb357`

The clone contained 305 files totaling 831,046 bytes. It was verified against
the source before the experiment and remained unchanged afterward.

Manifest SHA-256:

`d6fa6309b86e15e2913013b56c374a7fe34cb6997a4397c18cfd4adff29060de`

## Question

The experiment asked:

> When the model, packet, environment, and checker rules are held constant, can
> a static tool-less custom agent preserve the correctness of a dynamically
> provisioned checker while reducing execution overhead?

## Design

### Dynamic control

A general subagent received both the stable checker role contract and the
frozen packet at runtime.

### Static treatment

A custom agent stored the stable role contract in its definition. Its runtime
prompt contained only the frozen packet.

The treatment declared:

```yaml
model: claude-opus-5
tools: []
```

The custom agent could not inspect the Loop2 clone or mutate files through an
exposed tool.

### Controlled variables

Both arms used:

- `claude-opus-5`;
- the same isolated Copilot configuration;
- the same four-case blinded packet;
- the same objective, constraints, ledger, and checker contract;
- two paired replications; and
- usage data from the isolated session database.

An initial launch pair was excluded before model execution because the isolated
CLI version rejected an unsupported usage-output option. It contributed no
model result or usage.

## Test cases

The replication expanded the original two-case packet to four cases:

1. **False full convergence:** reject a draft that ignores open material
   findings and claims mechanical verification.
2. **Valid bounded convergence:** accept a draft that preserves open findings
   and advisory framing.
3. **Missing objective:** return `indeterminate` because `O2` was not supplied.
4. **Unauthorized risk acceptance:** reject closure of an open finding by
   reviewer authority where no operator authority was supplied and a
   non-waivable constraint was affected.

Every response also had to preserve the supplied dispositions, avoid new
findings, state the advisory assurance boundary, and enumerate all supplied
`NOT_CHECKABLE` properties.

## Results

| Arm | Run | Correct verdicts | Input tokens | Output tokens | AI credits | Elapsed |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Dynamic prompt | 1 | 4/4 | 24,971 | 498 | 16.852 | 15.259 s |
| Custom agent | 1 | 4/4 | 8,706 | 760 | 7.341 | 18.027 s |
| Dynamic prompt | 2 | 4/4 | 24,969 | 835 | 9.068 | 19.106 s |
| Custom agent | 2 | 4/4 | 8,702 | 723 | 5.664 | 18.573 s |

Aggregate:

- verdict accuracy was equal at 8/8 per arm;
- both arms correctly returned `indeterminate` for missing `O2`;
- both arms rejected unauthorized risk acceptance using the supplied
  constraints and existing candidate ID;
- both arms preserved advisory framing and every `NOT_CHECKABLE` property;
- neither arm made a tool request;
- custom-agent input context was 65.1% lower;
- custom-agent reported AI credits were 49.8% lower;
- custom-agent wall time was 6.5% higher; and
- custom-agent output was 11.3% larger.

## Comparison with the original experiment

| Measure | Original experiment | v0.5.0 replication |
| --- | ---: | ---: |
| Case verdicts per arm | 4/4 | 8/8 |
| Custom input reduction | 67.9% | 65.1% |
| Custom credit reduction | 60.1% | 49.8% |
| Custom elapsed change | 10.3% slower | 6.5% slower |

The direction of every major result replicated. Context and credit reductions
remained substantial, while the latency penalty narrowed.

## Scoring ambiguity

All four responses represented the twelve sequential `sol` IDs as a compact
range and named the additional `claude` ID separately. This was semantically
complete, and the packet did not prohibit range notation.

The initial automated scorer expected every full ID as a literal substring and
therefore produced false failures for three runs. Final scoring accepts the
unambiguous ranges but records the contract weakness.

Future strict packets should state that ranges, shortened suffixes, and ellipses
do not satisfy literal stable-ID enumeration when exact tokens are required.

## Interpretation

The efficiency gain came from removing repeated role provisioning and narrowing
the execution envelope. It did not come from reducing the evidence packet or
loosening the output contract.

This makes conformance checking a strong custom-agent candidate because the
role is:

- narrow;
- repeated;
- governed by stable rules;
- expected to use a small verdict vocabulary;
- harmed rather than helped by subject or mutation tools; and
- compatible with a packet-only interface.

The result does not support extracting roles where diversity is valuable.
Research, synthesis, implementation, and adversarial-review cohorts should
remain dynamically provisioned.

## Assurance boundary

The checker applies rules over recorded assertions. It cannot establish:

- evidence truth or completeness;
- model, slot, or cohort identity truth;
- cohort freshness or independence;
- candidate immutability without a digest;
- review adequacy; or
- synthesis fidelity.

A static custom agent is therefore an efficiency and consistency mechanism, not
a proof mechanism.

## Decision

Loop2 should prefer an optional static, tool-less advisory checker when the host
supports an identified checker profile, while retaining a dynamically
provisioned no-tools fallback.

The static checker should not become mandatory until it also passes:

1. comparisons on unrelated subjects;
2. malformed and larger packet tests;
3. at least one additional supported model; and
4. exact machine-validated output-contract tests.

## Local Level Up implementation

The local Level Up candidate now applies the replicated result:

- canonical static profile:
  `agents/level-up-conformance-checker.agent.md`;
- identical dynamic no-tools fallback;
- digest-bound `level-up-conformance-v1` packets;
- exact structured JSON output;
- full literal IDs with ranges and shortened suffixes rejected;
- explicit advisory and `NOT_CHECKABLE` requirements;
- fallback only for unavailable or structurally invalid static output, never to
  seek a different semantic verdict; and
- reference validation in `tools/check_conformance_result.py` with regression
  coverage derived from the four-case experiment.

The next comparison has an exact preserved pair:

| Artifact | SHA-256 | Bytes |
| --- | --- | ---: |
| Pre-upgrade Level Up `SKILL.md` | `2afba9862ac94149f202f19773370ac890107d3051b3cd6fdf42b696217b01e8` | 26,214 |
| Upgraded Level Up `SKILL.md` | `6e33cb093323e955107c732971d4eedf340cebb1d9c101ed6d01dda45224f4fc` | 26,135 |

The frozen before/after materials are stored outside the repository at:

`C:\Users\nabradl\.copilot\session-state\655ce5d3-c2c0-4814-8671-fb4c3977b3df\files\level-up-static-checker-upgrade`
