# Continuity Debt

> When generation outpaces coherence, someone pays. The question is who.

---

## Core Thesis

**Continuity debt** is the compounding accumulation of logic errors, entity contradictions, and world-state fractures that occurs when generative output scales faster than the coherence infrastructure maintaining it.

It is the worldtext equivalent of technical debt. But unlike technical debt — which can be deferred indefinitely if the software ships — continuity debt **is immediately visible to the inhabitant**. A world with continuity debt does not feel broken *eventually*. It feels broken *now*.

---

## The Economics

### The Three Debtors

| Debtor | What They Owe | What They Control |
|--------|-------------|------------------|
| **OEM** (Model Builder) | Causal coherence, persistent state, entity tracking | Architecture, training data, inference pipeline |
| **Service Provider** (Integrator) | World-state management, continuity repair, prompt conditioning | API layer, context window, retrieval-augmented generation |
| **Operator** (User) | Vigilance, prompt discipline, manual review | Input, judgment, canonization decisions |

### The Cascading Failure

1. The OEM builds a model with no persistent world-state (current paradigm).
2. The Service Provider wraps it in a thin context layer and markets "world building" capabilities.
3. The Operator generates fifty scenes and discovers that scene 3 contradicts scene 47.
4. The Operator now bears the entire labor cost of coherence — manually tracking entities, cross-referencing states, repairing contradictions.

> The continuity debt is always paid. The only variable is how far downstream the bill travels before someone catches it.

---

## Accumulation Mechanics

### How Debt Accrues

| Mechanism | Description | Rate |
|-----------|------------|------|
| **Prompt Rupture** | Generation produces spectacular but disconnected content | Immediate — one bad generation can fracture the world |
| **Semantic Drift** | Original intent erodes as prompt chains extend | Gradual — cumulative over 10-50 generations |
| **Entity Amnesia** | The system forgets previously established characters, places, rules | Proportional to context window exhaustion |
| **Physics Violations** | Generated content contradicts established physical laws | Episodic — appears randomly, compounds over time |
| **Style-Over-Logic Illusion** | Consistent aesthetics mask broken causality | Hidden — the most dangerous because it looks like coherence |

### The Compounding Problem

Continuity debt is not linear. Each unresolved fracture makes the next fracture more likely, because:

- Contradicted facts create ambiguous ground for future generation.
- The model has no mechanism to distinguish "established canon" from "error."
- Downstream prompts may reference the error, hardening it into pseudo-canon.

---

## Repair Strategies

### Prevention (Cheapest)

| Strategy | Mechanism | Cost |
|----------|----------|------|
| **Executable World Bible** | Machine-readable constraints injected into every prompt | Medium upfront, near-zero marginal |
| **Entity Ledger** | Persistent database separating identity fields from state fields | Medium upfront, low marginal |
| **Operative String Composition** | Every prompt carries Anchors + Constraints + Motion Vectors + Negative Constraints | Low per-prompt |
| **Negative Constraints** | Explicit "this must NOT happen" clauses | Near-zero |

### Detection (Moderate)

| Strategy | Mechanism | Cost |
|----------|----------|------|
| **Same-Worldness Test** | Audit every candidate artifact against Mythos, Topos, Ethos | Per-artifact |
| **Return Probe** | Periodically test backward coherence | Per-session |
| **Canary Conditions** | Automated tripwires that fire when specific continuity invariants are violated | Setup cost, then automated |

### Repair (Most Expensive)

| Strategy | Mechanism | Cost |
|----------|----------|------|
| **Manual Review** | Operator reads all generated content and cross-references | O(n²) with corpus size |
| **Retcon** | Retroactively modifying established content to accommodate new content | Destroys trust |
| **Lore Absorption** | Reclassifying a contradiction as a "myth" rather than a "fact" | Creative but risky — the lore book can only absorb so much |

---

## The Suchman Critique

Lucy Suchman's *Plans and Situated Actions* (1987) identifies the structural root of continuity debt:

- **The model treats each prompt as an isolated plan**: a self-contained instruction to be executed without memory.
- **The operator performs fluid, situated action**: a continuous thread of intent that assumes persistent context.

This mismatch is not a bug in any specific model. It is a **structural asymmetry** between how humans inhabit worlds and how current generative systems produce surfaces.

### The Closed-World Fallacy

The assumption that scaling parameters will inherently teach the model physics, causality, and persistence. This is false.

- A model with 10x more parameters still has no entity ledger.
- A model with 100x more training data still has no persistent world-state.
- A model with 1000x more compute still treats each prompt as isolated.

> Coherence is not an emergent property of scale. It is an architectural commitment.

---

## The CRI Architecture (Speculative)

**Continuity-Regulated Intelligence**: a meta-learner/governor sitting above the LLM.

```
┌─────────────────────────────────────┐
│         CRI GOVERNOR                │
│  health signals · compliance ·      │
│  quality gates · canary conditions  │
│  rollback · entity reconciliation   │
├─────────────────────────────────────┤
│         WORLD BIBLE                 │
│  identity fields · invariants ·     │
│  continuity anchors · negative      │
│  constraints · physics model        │
├─────────────────────────────────────┤
│         LLM / GENERATIVE ENGINE     │
│  produces surfaces on demand        │
│  no persistent state                │
│  no entity memory                   │
│  no self-audit capability           │
└─────────────────────────────────────┘
```

The CRI intercepts every generation, tests it against the world bible, detects violations, and either:
- **Repairs** the output (minor drift)
- **Rejects** the output (major fracture)
- **Flags** the output for operator review (ambiguous cases)
- **Rolls back** to a previous consistent state (catastrophic failure)

---

## The Labor Question

> When generation outpaces coherence, who bears the labor cost — OEM, service provider, or user?

Currently: the user. Always the user.

The entire project of worldtext operations is an attempt to shift this burden upward — to build the coherence infrastructure that makes continuity debt someone else's problem.

---

## Sources

- NATURAL SIGN Doc A: "Worldtext Coherence Theory and Design"
- NATURAL SIGN Doc B: "Worldtext and Same-Worldness"
- Lucy Suchman, *Plans and Situated Actions* (1987)
- Peter Naur, "Programming as Theory Building" (1985)
- Yann LeCun, "A Path Towards Autonomous Machine Intelligence" (2022)

---

*Synthesis compiled: 2026-04-27. Parent worlds: world-continuity-debt, world-worldtext-coherence.*
