# The Agential Cut Diagnostic

> Every act of generation is an act of cutting.  
> Every cut enacts a world and discards another.  
> This instrument makes the cut visible.

---

## I. The Theory

### 1.1 — The Problem

Generative AI systems produce worlds. But they do so by performing **cuts** — distinctions that separate what is included from what is excluded, what is salient from what is noise, what is pattern from what is anomaly. These cuts are structural, not accidental:

- **Training cuts**: what data is collected, cleaned, tokenized, kept, discarded.
- **Model cuts**: what features are learned, what dimensions compressed.
- **Prompt cuts**: what the operator specifies, what is left implicit.
- **Content-policy cuts**: what outputs are blocked, filtered, nudged away.
- **Interface cuts**: what the user can see, edit, contest, override.
- **Ranking cuts**: what is shown first, what is buried, what never surfaces.

Before any AI system can be evaluated for accuracy, coherence, or beauty, it has already **enacted a world** through these cuts. The agential cut is prior to quality; it is the *condition* of quality.

### 1.2 — The Lineage

| Theorist | Key Contribution | Operative Translation |
|----------|-----------------|----------------------|
| **Karen Barad** | Agential realism: cuts are not made by pre-existing subjects on pre-existing objects. The cut *produces* both subject and object. Intra-action, not inter-action. | Every worldtext generation simultaneously produces the artifact and the operator who reads it. You cannot design a neutral system — only a system with visible cuts. |
| **Vilém Flusser** | Apparatus theory: the camera is not a tool; it is a programmed system of possibilities. The photographer chooses *within* the program; the functionary *executes* the program without awareness. | The generative AI model is an apparatus. The question is not "what did the user produce?" but "was the user playing *against* the apparatus or merely functioning *for* it?" |
| **James C. Scott** | Legibility and metis: states destroy local knowledge by imposing administrative grids. The map replaces the territory; the territory dies. | Every training set, tokenizer, and classification scheme performs a Scott-ian simplification. The question: what *metis* — what local, embodied, practice-based knowledge — was destroyed in the conversion? |
| **Stafford Beer** | Requisite variety: a controller must possess enough internal variety to respond to environmental complexity. Simplification always loses signal. | A prompt that reduces a world to three keywords has failed the requisite variety test. A worldtext that maintains the full complexity of the world it describes passes it. |
| **Gilles Deleuze** | Societies of control: modulation replaces enclosure; the dividual replaces the individual; continuous variation replaces discrete confinement. | Generative AI doesn't discipline the user (say yes/no); it *modulates* them (adjusts probability surfaces, reshapes suggestions, nudges creative trajectories). The user is not censored; they are *steered*. |
| **Seymour Papert** | Constructionism: knowledge is built through making, not receiving. Objects-to-think-with. Debugging as epistemology. | The worldtext is an object-to-think-with. If the user can debug a worldtext — inspect it, revise it, contest its cuts — they learn. If not, they are functionaries. |
| **Gregory Bateson** | Mind is the circuit, not the skull. The blind person's cane is part of the mind. Ecology of mind: ideas live in systems, not skulls. | The worldtext ecosystem *is* the mind. Operator + worldtext + LLM + wiki + lint = the cognitive unit. Cutting any element severs cognition. |

### 1.3 — The Core Principle

> **The Apparatus Principle**: A generative system is not a tool that the operator uses. It is an apparatus that operates *on* the operator. The operator's only defense is to make the cuts visible, contestable, and revisable.

---

## II. The Cut Taxonomy

Every generative worldtext system performs cuts at six levels. Each level must be auditable.

| Level | Cut Type | What It Does | Who Controls It | Worldtext Audit Question |
|-------|----------|-------------|----------------|-------------------------|
| **L0** | Training Cut | Selects, cleans, tokenizes, compresses the raw world into training distribution | OEM (model builder) | What world-knowledge was excluded at training? What biases were encoded? |
| **L1** | Architecture Cut | Determines what representations are possible (attention heads, context windows, modality support) | OEM | What structural limitations constrain what the model can even *think*? |
| **L2** | Policy Cut | Filters, blocks, or steers outputs away from certain domains | OEM / Service Provider | What outputs are forbidden? What creative possibilities are foreclosed? |
| **L3** | Prompt Cut | The operator selects what to ask, how to ask it, what context to provide | Operator | What local knowledge did the operator simplify or omit? (→ Metis Test) |
| **L4** | Interface Cut | The platform determines what the user sees, what controls are available, what is editable | Service Provider | Can the user inspect the full output? Can they contest? Can they override? |
| **L5** | Interpretation Cut | The user reads the output, selects what to keep, what to discard, how to integrate | Operator | Is the operator treating the output as finished artifact or as raw evidence for theory-building? |

---

## III. The Seven Commitments

Worldtext systems that take the agential cut seriously must commit to these seven protocols:

### Commitment 1: Cut Visibility
> Every cut the system makes must be inspectable by the operator. This includes: what sources were consulted, what was excluded, what policy filters engaged, what alternatives were suppressed.

**Implementation**: The `ritual-cut-visibility` mandates that every ingest, query, and lint operation logs its cut decisions. The lint report must include a "Cuts Made" section.

### Commitment 2: Provenance
> Every artifact must carry a trace of the path by which it was produced — the trail, not just the answer.

**Implementation**: Links to `ritual-trail-building` and `world-memex-trails`. Every wiki page must carry an ingest log showing what sources produced it.

### Commitment 3: Choice Amplification
> The system must amplify the operator's real choices, not simulate choice while constraining it.

**Implementation**: Flusser's functionary/player distinction. The operator must be able to play *against* the system — to override lint, contest policy, inject contradiction — not merely accept its suggestions.

### Commitment 4: Relational Adequacy
> The system must maintain enough internal complexity to honor the complexity of the world it describes. (Beer's requisite variety.)

**Implementation**: The worldtext wiki must carry more dimensions than the prompt that initiated it. The wiki expands; the prompt compresses. The worldtext lives in the expansion.

### Commitment 5: Metis Preservation
> The system must not destroy local, embodied, practice-based knowledge in the act of systematization.

**Implementation**: The `ritual-metis-test` fires on every major ingest. Question: "What situated knowledge does this systematization simplify, and who bears the cost?"

### Commitment 6: Apparatus Literacy
> The operator must understand *what the system is*, not just *what it does*. The system must teach.

**Implementation**: Each worldtext directory must carry an `apparatus-manifest.md` that describes the model, the training lineage, the policy layers, and the known structural limitations. The operator reads this before beginning work.

### Commitment 7: World-Making Accountability
> Because every generation enacts a world, the operator and the system share responsibility for *which* world is enacted.

**Implementation**: The `ritual-explanation-gate` is the constitutional mechanism. When cuts produce contradictions that cannot be resolved by the system, the operator must make a definitive theoretical ruling. The operator cannot delegate world-making to the machine.

---

## IV. The Metis Test

A formal diagnostic ritual, executable at any point during worldtext operation.

### Inputs
- The current worldtext operation (ingest, query, lint, synthesis)
- The source material being processed
- The output being produced

### Five Questions

1. **What local knowledge does this operation simplify?**
   - What distinctions present in the source are collapsed in the output?
   - What embodied, situated, or practice-based knowledge is compressed into category?

2. **Who bears the cost of this simplification?**
   - Whose knowledge is lost? Whose voice is flattened?
   - Is the cost acknowledged or invisible?

3. **Is this simplification reversible?**
   - Can the original complexity be recovered from the output?
   - Are the source documents preserved and linked?

4. **Does this simplification serve the operator or the apparatus?**
   - Is the simplification making the world more legible *to the operator* (augmentation)?
   - Or is it making the world more legible *to the system* at the cost of the operator's understanding (substitution)?

5. **What counter-narrative is suppressed?**
   - What alternative reading of this material was foreclosed?
   - Is that foreclosure documented in the lint report?

### Output
A `metis-assessment` block appended to the artifact, scoring each question and flagging unresolved costs.

---

## V. The Apparatus Audit

A periodic review (recommended: every major worldtext expansion) that assesses the system's structural cut profile.

| Dimension | Question | Health Indicator |
|-----------|----------|-----------------|
| **Training Transparency** | Can the operator identify the training data lineage? | ✓ Known / ⚠ Partial / ✗ Unknown |
| **Policy Transparency** | Are content-policy filters documented and contestable? | ✓ Documented / ⚠ Opaque / ✗ Hidden |
| **Interface Openness** | Can the operator inspect all system outputs (including suppressed alternatives)? | ✓ Full access / ⚠ Partial / ✗ Locked |
| **Override Capacity** | Can the operator override system recommendations? | ✓ At all levels / ⚠ Some levels / ✗ None |
| **Metis Preservation** | Does the system preserve source complexity beyond what it uses? | ✓ Sources preserved / ⚠ Summarized / ✗ Discarded |
| **Provenance Depth** | Does every artifact carry its full generation trail? | ✓ Full trail / ⚠ Partial / ✗ None |
| **Ecological Awareness** | Does the system model its own energy, time, and attention costs? | ✓ Tracked / ⚠ Estimated / ✗ Ignored |

---

## VI. Constitutional Integration

This synthesis connects to the existing Worldtext architecture at the following points:

| Existing Component | Connection |
|-------------------|------------|
| `ritual-lint` | Extended: lint must now include a "Cuts Made" section in every report |
| `ritual-explanation-gate` | Reinforced: the Explanation Gate is the constitutional site where cuts become contestable |
| `ritual-ingest` | Extended: every ingest must log what was simplified and what was preserved |
| `distinction-rag-worldtext` | Refined: RAG makes invisible cuts; Worldtext makes visible cuts. This is the structural difference. |
| `conflict-functionary-vs-player` | New conflict formalized in the atlas |
| `entity-epistemic-debt` | Connected: epistemic debt is the *consequence* of invisible cuts over time |
| `world-agential-cybernetic-media` | This synthesis is the primary instrument for this world |

---

## VII. Source Documents

- `PAPERS/cyber-00.md` — "Agential Cybernetic Media"
- `PAPERS/cyber-02.md` — "Agential Worlds, Cybernetic Cuts"
- `PAPERS/cyber-03.md` — "Cybernetic Ritual Narratology"

---

*Synthesis compiled: 2026-04-28. Parent worlds: world-agential-cybernetic-media, world-thick-programming. Author: Atlas registration pass.*
