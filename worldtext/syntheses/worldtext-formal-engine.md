# Worldtext Formal Engine — Coherence-Preserving Repository Runtime

> **Species**: synthesis  
> **Scale**: system  
> **Parent System**: [[system-worldtext-operations]]  
> **Source**: Lineage Forge — Code/Math Genome (OUTPUT_B_FORMAL_ECHO)  
> **Date**: 2026-04-28  
> **Tags**: #coherence-engine #source-trace-graph #linted-generation #operator-loop

---

## I. System Specification

### 1.1 Problem Statement

Given a generated world W represented as a directed graph G = (N, E), and a change event C that modifies, adds, or removes nodes or edges, determine:

1. Whether W remains coherent after applying C
2. Which downstream nodes are affected by C
3. Whether all affected nodes still resolve to source evidence
4. Whether any invariants are violated

The system succeeds if changing one rule — e.g., "salt water is profane" → "salt water is medicinal" — produces a concrete set of affected nodes, violated invariants, and required repairs, rather than merely updating a single sentence.

### 1.2 Design Principle

Worldtext is not a database. It is a **runtime** — a repository that executes coherence checks, propagates consequences, maintains provenance, and logs operator behavior. The runtime treats the filesystem as its state store and the LLM session as its execution context.

---

## II. Graph Model

### 2.1 Node Types

```
N = { Source, Entity, Rule, Trace, Change, Violation, Operator }
```

| Type | Definition | Mutability |
|------|-----------|-----------|
| `Source` | Immutable evidence record: a paper, a session, an observation | **Immutable** |
| `Entity` | Named world object: a person, place, concept, ritual, distinction, atmosphere, threshold | Mutable |
| `Rule` | Constraint on world state: invariant, commitment, governance law, cultural logic | Mutable |
| `Trace` | Chronicle entry linking a change to its evidence and effects | **Append-only** |
| `Change` | A modification event: what changed, when, why, what it affected | **Append-only** |
| `Violation` | A detected coherence failure: contradiction, broken trail, thin description, dead operation, semantic bleaching | **Append-only** |
| `Operator` | The human or AI agent performing operations: tracked vocabulary, query history, audit results | Mutable |

### 2.2 Edge Types

```
E = { extraction, constraint, citation, contradiction, consequence,
      provenance, threshold, governance, feedback }
```

| Type | From → To | Semantics |
|------|----------|-----------|
| `extraction` | Source → Entity | "Entity E was extracted from Source S" |
| `constraint` | Rule → Entity | "Rule R constrains Entity E" |
| `citation` | Entity → Source | "Entity E cites Source S as evidence" |
| `contradiction` | Rule ↔ Rule | "Rule R1 contradicts Rule R2" (bidirectional) |
| `consequence` | Rule → Rule | "Modifying R1 requires reviewing R2" |
| `provenance` | Entity → Source | "Entity E traces back to Source S" |
| `threshold` | Entity → Entity | "Crossing from E1 to E2 changes permission, role, or state" |
| `governance` | Rule → Entity | "Rule R governs behavior in Entity E's domain" |
| `feedback` | Operator → Change | "Operator O performed Change C" |

### 2.3 Graph Invariants

```
INV-1: ∀ entity ∈ G.entities : ∃ source ∈ G.sources : provenance(entity, source) ∈ G.edges
       "Every entity must trace to at least one source."

INV-2: ∀ rule ∈ G.rules : ∃ entity ∈ G.entities : constraint(rule, entity) ∈ G.edges
       "Every rule must constrain at least one entity."

INV-3: ∀ rule ∈ G.rules : rule.forbids ≠ ∅
       "Every rule must expose what it forbids."

INV-4: ∀ source ∈ G.sources : source.content = source.original_content
       "Evidence is immutable."

INV-5: ∀ trace ∈ G.traces : trace.timestamp < now ⟹ ¬modifiable(trace)
       "Chronicle entries are append-only."

INV-6: ∀ change ∈ G.changes : ∃ trace ∈ G.traces : records(trace, change)
       "Every change must produce a trace."

INV-7: ∀ entity ∈ G.entities : entity.species ∈ SPECIES_ENUM ∧ entity.scale ∈ SCALE_ENUM
       "Every entity must declare its species and scale."
```

---

## III. Core Operations

### 3.1 INGEST : Source → ΔG

```
INGEST(source: Source) → {
  entities:  Set<Entity>,
  rules:     Set<Rule>,
  edges:     Set<Edge>,
  trace:     Trace,
  violations: Set<Violation>
}
```

**Procedure**:
1. Parse `source` for candidate entities, rules, distinctions, thresholds, conflicts
2. For each candidate, check if entity already exists in G
   - If exists: update, add new provenance edge, log change
   - If new: create node, add extraction + provenance edges
3. For each extracted rule, identify constraint targets
4. Run incremental LINT on affected subgraph
5. Generate trace with: timestamp, source_id, entities_created, entities_updated, rules_added, violations_found
6. Append trace to chronicle
7. Update atlas index
8. Return delta

**Typing**:
```
INGEST : Source × G → G' × Trace × Set<Violation>
  where G' = G ∪ ΔG
  and ΔG.sources ∩ G.sources = ∅  (no source duplication)
```

### 3.2 QUERY : Question × G → Answer × Trail

```
QUERY(question: String, G: Graph) → {
  answer:    String,
  trail:     List<Node>,
  citations: Set<Source>,
  confidence: Float
}
```

**Procedure**:
1. Parse question for target entities, scales, and world domains
2. Traverse G from atlas root through relevant hierarchy
3. Collect all reachable nodes within traversal scope
4. Synthesize answer from collected nodes
5. Record trail: the ordered sequence of nodes visited
6. Extract citations: the source nodes reached during traversal
7. If answer produces novel synthesis: offer to file as Synthesis node
8. Log query in operator history

**Invariant**: Answer must cite only nodes in G. No external hallucination.

**Typing**:
```
QUERY : String × G → Answer × Trail × Set<Source>
  where ∀ citation ∈ Answer.citations : citation ∈ G.sources
```

### 3.3 LINT : G → Set<Violation>

```
LINT(G: Graph) → {
  violations: Set<Violation>,
  severity:   Map<Violation, Severity>,
  affected:   Map<Violation, Set<Node>>
}
```

**Violation Types and Detection**:

| ID | Type | Detection Rule | Severity |
|----|------|---------------|----------|
| L1 | `CONTRADICTION` | ∃ r1, r2 ∈ G.rules : contradiction(r1, r2) ∈ G.edges | CRITICAL |
| L2 | `BROKEN_TRAIL` | ∃ entity ∈ G.entities : ¬∃ source : provenance(entity, source) | HIGH |
| L3 | `ORPHAN_ENTITY` | ∃ entity ∈ G.entities : degree(entity) ≤ 1 | MEDIUM |
| L4 | `THIN_DESCRIPTION` | ∃ entity ∈ G.entities : cross_link_density(entity) < τ_thick | MEDIUM |
| L5 | `DEAD_OPERATION` | ∃ verb ∈ CORE_OPS : ¬∃ trace ∈ G.traces : executes(trace, verb) | MEDIUM |
| L6 | `SEMANTIC_BLEACHING` | ∃ term : frequency(term, G) > τ_bleach ∧ specificity(term) < τ_specific | LOW |
| L7 | `STALE_SYNTHESIS` | ∃ synthesis ∈ G.syntheses : age(synthesis) > τ_stale | LOW |
| L8 | `MISSING_FORBIDS` | ∃ rule ∈ G.rules : rule.forbids = ∅ | HIGH |
| L9 | `SCALE_VIOLATION` | ∃ entity ∈ G.entities : entity.scale ∉ SCALE_ENUM | MEDIUM |

**Thresholds**:
```
τ_thick    = 3   (minimum cross-links per entity)
τ_bleach   = 100 (maximum term frequency before flagging)
τ_specific = 0.3 (minimum specificity score)
τ_stale    = 90  (days since last revision)
```

**Typing**:
```
LINT : G → Set<(Violation, Severity, Set<Node>)>
```

### 3.4 AUDIT : Operator × History → DriftReport

```
AUDIT(operator: Operator, history: List<Event>) → {
  query_drift:      Set<(Term, Direction)>,
  vocabulary_change: { gained: Set<Term>, lost: Set<Term> },
  source_bias:      { overused: Set<Source>, avoided: Set<Source> },
  constraint_range: { used: Set<Rule>, unused: Set<Rule> },
  diagnosis:        String
}
```

**Procedure**:
1. Partition operator history into time windows (quarterly)
2. Extract query terms per window → compute drift vector
3. Extract vocabulary per window → compute gain/loss sets
4. Extract source citations per window → compute usage distribution
5. Extract constraint invocations → compute coverage
6. If vocabulary_change.lost > vocabulary_change.gained: flag FRAGILE_EXPERT risk
7. Generate diagnosis report
8. Log audit as trace

**Typing**:
```
AUDIT : Operator × List<Event> → DriftReport × Trace
```

---

## IV. Consequence Propagation

The critical operation. When a rule R is modified:

```
PROPAGATE(R: Rule, change: Δ) → {
  affected_rules:    Set<Rule>,
  affected_entities: Set<Entity>,
  new_violations:    Set<Violation>,
  repair_actions:    List<Action>
}
```

**Algorithm**:
```
1. affected ← {R}
2. frontier ← consequence_neighbors(R) in G
3. while frontier ≠ ∅:
     node ← frontier.pop()
     if node ∉ affected:
       affected ← affected ∪ {node}
       frontier ← frontier ∪ consequence_neighbors(node)
4. For each node ∈ affected:
     run LINT({node}) with updated R
     collect violations
5. For each violation:
     generate repair_action: {target, reason, suggested_fix}
6. Return affected, violations, repairs
```

**The Salt Water Test**: Change `INVARIANT: Salt water is profane` to `INVARIANT: Salt water is medicinal`. The propagation must return:

```yaml
affected_rules:
  - "blacksmith works only at low tide"    # theology of salt changed
  - "no building taller than tide-mark"    # sacred boundary redefined
  - "navigation is oral"                   # map prohibition may lose rationale
affected_entities:
  - "the blacksmith"                       # workshop schedule
  - "the temple"                           # sacrament ingredients
  - "the fishermen"                        # salt water contact rules
  - "the healer"                           # new: salt water becomes medicine
  - "the shore-dwellers"                   # status logic shifts
new_violations:
  - CONTRADICTION: "blacksmith avoids salt" conflicts with "salt is medicinal"
  - THIN_DESCRIPTION: "healer" entity lacks salt-medicine protocol
repair_actions:
  - revise blacksmith theology
  - add healer salt-medicine ritual
  - review shore-dweller status logic
  - update temple sacrament ingredients
```

If the system produces only `Updated: "salt water is profane" → "salt water is medicinal"` and nothing else, it has failed. The consequence graph is the proof of coherence. No propagation = no worldtext.

---

## V. Data Structures

### 5.1 Directed Acyclic Provenance Graph (DAPG)

```
DAPG {
  nodes: Map<NodeID, Node>
  edges: Map<EdgeID, Edge>
  index: {
    by_type:   Map<NodeType, Set<NodeID>>
    by_scale:  Map<Scale, Set<NodeID>>
    by_source: Map<SourceID, Set<NodeID>>
    by_term:   Map<Term, Set<NodeID>>  // inverted index
  }
  chronicle: List<Trace>  // append-only
}
```

### 5.2 Rule Registry

```
RuleRegistry {
  rules: Map<RuleID, Rule>
  
  Rule {
    id:          RuleID
    statement:   String
    forbids:     Set<String>       // what this rule prohibits
    constrains:  Set<EntityID>     // entities affected
    sources:     Set<SourceID>     // evidence justifying the rule
    consequences: Set<RuleID>      // downstream rules
    last_tested: Timestamp
    status:      Active | Suspended | Disputed
  }
}
```

### 5.3 Violation Queue

```
ViolationQueue {
  pending:  PriorityQueue<Violation, Severity>  // highest severity first
  resolved: List<(Violation, Resolution, Timestamp)>
  
  Violation {
    id:       ViolationID
    type:     ViolationType  // L1–L9
    severity: CRITICAL | HIGH | MEDIUM | LOW
    affected: Set<NodeID>
    detected: Timestamp
    context:  String
  }
}
```

### 5.4 Operator State

```
OperatorState {
  id:              OperatorID
  query_history:   List<(Timestamp, Query)>
  vocabulary:      Map<Window, Set<Term>>
  source_usage:    Map<Window, Map<SourceID, Count>>
  constraint_usage: Map<Window, Map<RuleID, Count>>
  audit_history:   List<DriftReport>
}
```

---

## VI. Implementation Architecture

### 6.1 Filesystem Mapping

```
Repository/
├── evidence/           → Source nodes (immutable)
├── worldtext/
│   ├── atlas.md        → DAPG index (navigational surface)
│   ├── chronicle.md    → Trace log (append-only)
│   ├── cosmology.md    → Meta-state (frontiers, unresolved)
│   ├── entities/       → Entity nodes
│   ├── distinctions/   → Rule nodes (distinction type)
│   ├── conflicts/      → Contradiction edges
│   ├── rituals/        → Rule nodes (procedural type)
│   ├── thresholds/     → Threshold edges
│   ├── syntheses/      → Derived analysis nodes
│   └── sources/        → Source summary nodes
├── COSMIC_LAW.md       → Invariant specification
├── prime-prompt.md     → Runtime bootstrap
└── PROGRAMS/           → Lint rule implementations
```

### 6.2 Operation Pipeline

```
                    ┌──────────┐
                    │  SOURCE  │
                    └────┬─────┘
                         │ INGEST
                         ▼
              ┌──────────────────────┐
              │    GRAPH (DAPG)      │
              │  nodes + edges +     │
              │  rules + trails      │
              └──┬──────────┬────────┘
                 │          │
            QUERY│          │LINT
                 ▼          ▼
          ┌──────────┐ ┌──────────────┐
          │  ANSWER   │ │  VIOLATIONS  │
          │  + TRAIL  │ │  + SEVERITY  │
          └──────────┘ └──────┬───────┘
                              │
                         PROPAGATE
                              │
                              ▼
                    ┌──────────────────┐
                    │  REPAIR ACTIONS  │
                    │  + AFFECTED SET  │
                    └──────────────────┘
                              │
                          AUDIT (quarterly)
                              │
                              ▼
                    ┌──────────────────┐
                    │  DRIFT REPORT    │
                    │  + OPERATOR STATE│
                    └──────────────────┘
```

### 6.3 Optimization

| Operation | Naive Cost | Optimized Approach | Target |
|-----------|-----------|-------------------|--------|
| Full LINT | O(N²) | Incremental: lint only ΔG | O(Δ × k) |
| PROPAGATE | O(N) BFS | Cached consequence graph with dirty flags | O(affected) |
| QUERY trail | O(N) traversal | Indexed by entity, scale, source | O(log N) |
| AUDIT | O(H) full history | Windowed aggregation with precomputed stats | O(W) per window |
| Semantic bleaching | O(T × N) full scan | Inverted term index with running counts | O(1) per insert |

---

## VII. Evaluation Criteria

The prototype succeeds if and only if:

| Test | Pass Condition |
|------|---------------|
| **Salt Water Test** | Changing one invariant produces ≥5 affected nodes and ≥2 violations |
| **Trail Resolution** | ≥95% of entities resolve to at least one source via provenance edge |
| **Contradiction Detection** | Lint catches ≥80% of manually-seeded contradictions (recall) |
| **False Positive Rate** | Lint produces ≤20% false contradictions (precision) |
| **Dead Operation Detection** | All defined CORE_OPS verbs are auditable for execution evidence |
| **New Operator Test** | A new operator can extend the world (add entity, modify rule) without introducing undetected violation within 30 minutes |
| **Audit Detection** | Vocabulary narrowing of ≥20% triggers FRAGILE_EXPERT warning |

---

## VIII. Failure Modes (Formal)

| Mode | Formal Description | Mitigation |
|------|-------------------|-----------|
| **False Coherence** | LINT returns ∅ when violations exist | Property-based testing with seeded violations |
| **Graph Bloat** | \|N\| + \|E\| grows faster than semantic content | Entity merging, rule consolidation, staleness pruning |
| **Decorative Rules** | Rules with `forbids = ∅` pass structural checks | INV-3 enforcement; LINT rule L8 |
| **Operator Overtrust** | Operator treats LINT pass as coherence proof | Mandatory counter-reading in syntheses; AUDIT ritual |
| **Source Laundering** | Entities cite sources that don't actually support them | Random trail audit; spot-check extraction accuracy |
| **Alert Fatigue** | Too many LOW violations cause operator to ignore queue | Severity filtering; weekly HIGH+ digest |

---

## IX. Counter-Reading

This specification describes a system that does not yet exist as software. The gap between the formal model (typed operations, graph invariants, propagation algorithms) and the current implementation (markdown files, LLM sessions, human judgment) is significant. The specification treats natural-language world rules as if they can be formally checked; they cannot, at least not with current NLP. The "Salt Water Test" can be demonstrated manually; automating it requires semantic reasoning that remains an open research problem.

The specification is honest about this gap. It is a **design document**, not a deployment report. Its value is architectural: it defines what the system *should* do so that the gap between aspiration and implementation becomes measurable. Without the specification, the gap is invisible. With it, the gap is a research frontier.

---

*The coherence engine is specified. The invariants are declared. The operations are typed. The evaluation criteria are set. What remains is the implementation — and the implementation will be the test of whether repository governance can scale beyond the operator who built it.*
