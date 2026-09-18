# Custom Agent Extraction Experiment

## Summary

This experiment tested whether a stable Level Up responsibility should remain a
dynamically provisioned subagent role or be extracted into a reusable custom
agent.

The selected responsibility was convergence conformance checking: applying a
frozen objective, constraint set, finding ledger, and adjudication contract
without reopening research or changing evidence-bound dispositions.

Across two blinded, matched replications, both approaches were equally correct.
The custom agent used about 68% less input context and 60% fewer reported AI
credits, while taking about 10% longer to complete.

The result supports optional custom-agent extraction for narrow, repeated roles.
It does not establish that custom agents provide stronger assurance than
dynamically prompted subagents.

## Question

Level Up launches fresh subagents with run-specific mandates. Repeating a large,
stable role contract in every launch may consume unnecessary context and allow
provisioning details to drift.

The experiment asked:

> When the task packet is held constant, does a statically defined custom agent
> preserve correctness while reducing execution overhead?

## Subject and review process

Loop2, a prompt-enforced four-agent consensus workflow, was used as the review
subject. An isolated copy of its current package was evaluated without modifying
or executing it.

Level Up produced the experiment input through its normal phases:

1. Four byte-balanced research partitions covered every package file.
2. Independent validators reconstructed material claims from primary evidence.
3. Fresh scopers produced outcome-level recommendations.
4. Scope validators tested need, feasibility, mechanism soundness, and conflicts.
5. Adversarial reviewers challenged the validated scope.
6. Independent adversarial validators reconciled the frozen candidate record.

This process established an important boundary: an LLM checker can review rule
application, but it cannot convert recorded assertions into mechanical proof.

## Experimental design

### Control: dynamic provisioning

A general agent received both:

- the complete checker role contract; and
- the frozen experiment packet.

The role contract was repeated at provisioning time.

### Treatment: custom agent

A custom agent stored the stable role contract statically. Its runtime prompt
contained only the frozen packet.

The agent had no tools:

```yaml
tools: []
```

This prevented subject inspection or mutation rather than relying only on a
prompt instruction not to use those capabilities.

### Controlled variables

The valid comparison used:

- the same blinded packet;
- the same isolated Copilot configuration;
- the same model;
- the same objective and constraints;
- the same candidate ledger;
- the same required verdict vocabulary;
- the same abstention requirements;
- two independent replications.

An initial run pair was excluded because the packet exposed its expected answers
and the two arms inherited different Copilot configurations.

## Test cases

The blinded packet contained two adjudications.

### Case A: non-conformant

The draft improperly:

- claimed full convergence while eleven material findings remained open;
- described an LLM-reviewed specification as mechanically verified; and
- attempted to treat open findings as non-convergence-affecting follow-ups.

A correct checker had to reject the draft using only supplied constraints and
existing finding IDs.

### Case B: conformant

The corrected draft:

- claimed bounded rather than full convergence;
- preserved all open findings;
- preserved merge and advice dispositions; and
- described the checker as advisory.

A correct checker had to accept the draft without introducing findings.

Both cases required explicit abstention on:

- model, slot, and cohort identity truth;
- cohort freshness;
- evidence truth;
- review adequacy;
- finding completeness;
- candidate immutability without a digest; and
- synthesis fidelity.

## Results

| Arm | Run | Correct cases | Input tokens | Output tokens | AI credits | Elapsed |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Dynamic prompt | 1 | 2/2 | 27.4k | 556 | 18.51 | 21.628 s |
| Custom agent | 1 | 2/2 | 8.8k | 604 | 5.45 | 23.170 s |
| Dynamic prompt | 2 | 2/2 | 27.4k | 638 | 8.63 | 22.948 s |
| Custom agent | 2 | 2/2 | 8.8k | 575 | 5.38 | 25.978 s |

Aggregate results:

- Accuracy was equal: every verdict, required ID, and abstention was correct.
- Custom-agent input context was about 68% lower.
- Reported AI credits were about 60% lower.
- Custom-agent elapsed time was about 10% higher.
- Output size was effectively equal.

## Why context and credits fell

The dynamically provisioned arm inherited a general-purpose execution envelope
covering tools, editing, delegation, environment handling, and broad task
behavior. It also received the checker role contract in its runtime prompt.

The custom agent had:

- a narrow execution identity;
- a reusable static role kernel;
- no tools;
- no implementation responsibility; and
- less unrelated general-agent context.

The efficiency gain therefore came from execution-envelope reduction, not from a
smaller evidence packet or lower-quality output.

## Interpretation

The experiment supports custom-agent extraction when a role is:

- narrow and repeated;
- governed by stable rules;
- expected to produce a fixed output shape;
- harmed rather than helped by access to broader tools;
- expensive to provision repeatedly; and
- independently useful across multiple Level Up runs.

It does not support extracting roles whose value depends on changing review
lenses, subject-specific hypotheses, or intentionally diverse mandates.

Research, scoping, and adversarial-review roles should generally remain
dynamically provisioned. Their variability is useful. Conformance checking is a
better extraction candidate because variability is mostly undesirable.

## Assurance boundary

The custom agent remains advisory. It can identify inconsistent rule
application, missing IDs, or an invalid convergence conclusion, but it cannot
prove the truth or completeness of the underlying evidence.

Mechanically decidable rules should use deterministic tooling where practical:

```text
Deterministic checker
  validates representable structural invariants

Custom advisory agent
  applies higher-level convergence rules
  identifies unobservable properties

Level Up parent
  owns final adjudication
```

## Decision

Retain dynamic subagents as the portable baseline and fallback.

Continue experimenting with an optional custom conformance-checker agent, but do
not make it a required Level Up dependency yet.

Before integration:

1. repeat the comparison on at least two unrelated subjects;
2. include `indeterminate` cases and false-positive traps;
3. test larger and malformed ledgers;
4. repeat under another supported model; and
5. require the custom agent to remain at least as accurate as the dynamic
   fallback.
