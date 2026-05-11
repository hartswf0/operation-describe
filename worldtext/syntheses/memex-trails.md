# The Memex Test: Provenance Against Plausibility

> A record, if it is to be useful to science, must be continuously  
> extended, it must be stored, and above all it must be consulted.  
> — Vannevar Bush, "As We May Think" (1945)

> For mature thought there is no mechanical substitute.  
> But creative thought and essentially repetitive thought  
> are very different things.  
> — Vannevar Bush

> This instrument tests whether a knowledge system preserves  
> the path by which its conclusions were built.

---

## I. The Theory

### 1.1 — The Problem

AI systems produce answers. They do not produce **trails**.

A scholar builds an argument by leaving a path: first I found this, then I connected it to that, then I reconsidered because of this, then I committed. The path is not the answer — it is the **evidence of thinking**. Without it, the answer is plausible but unaccountable.

Vannevar Bush, in 1945, foresaw this distinction with astonishing precision. His memex was not a search engine. It was a **trail-building machine** — a system for preserving the associative logic by which a mind moves through a field of documents.

The worldtext system that fails the Memex Test is a plausibility engine. The worldtext system that passes it is a **provenance engine**.

### 1.2 — Bush's Architecture

| Component | Definition | Worldtext Analogue |
|-----------|-----------|-------------------|
| **The Memex** | A mechanized private file and library; desk-sized, with screens, keyboard, and storage | The worldtext directory (raw/ + schema/ + wiki/) |
| **The Record** | Everything the owner has seen, read, annotated | raw/ — the unprocessed source material |
| **The Trail** | A named, persistent sequence of associative links built by the user through the record | The synthesis document, the ingest chain, the wiki's wikilink topology |
| **Trail Blazing** | The act of building a trail — selecting, linking, annotating, branching | ritual-trail-building |
| **The Inheritance** | Trails are transmissible. One scholar's trail can be followed, contested, and forked by another | The worldtext archive as public inheritance |

### 1.3 — The Key Distinctions

#### Storage vs. Consultation
Bush's central insight: the problem is not storage. The problem is **consultation**.

> "The summation of human experience is being expanded at a prodigious rate, and the means we use for threading through the consequent maze to the momentarily important item is the same as was used in the days of square-rigged ships."

Storage is solved. Google, archives, databases — we can store everything. What we cannot do is *traverse* the stored material in a way that preserves the associative logic of the human mind.

**Worldtext position**: The tripartite directory (raw/ → schema/ → wiki/) is a consultation architecture. raw/ provides storage. The schema provides the indexical structure. The wiki/ provides the traversal surface. Without all three, the worldtext is a pile, not a mind.

#### Augmentation vs. Delegation
Bush distinguishes between:
- **Augmentation**: The machine reorganizes the human-machine system so that the human can do *better* work — work that was previously impossible due to the limitations of manual filing, retrieval, and cross-referencing.
- **Delegation**: The machine replaces the human's labor entirely, concealing the path.

| | Augmentation | Delegation |
|-|-------------|-----------|
| **Who builds the trail?** | The human, assisted by the machine | The machine alone |
| **Who sees the trail?** | The human (and future readers) | No one |
| **Who inherits the trail?** | Future scholars | No one — the trail dies with the query |
| **Worldtext equivalent** | Operator uses ritual-ingest to build a wiki, inspects results, contests via Explanation Gate | Operator uses RAG to get an answer, does not inspect sources or build persistent knowledge |

#### Creative vs. Repetitive Thought
Bush, anticipating Naur by 40 years:

> "For mature thought there is no mechanical substitute. But creative thought and essentially repetitive thought are very different things. For the latter there are, and may be, powerful mechanical aids."

The worldtext automates **repetitive thought** (indexing, cross-referencing, contradiction detection) to free the operator for **creative thought** (theory-building, conceptual synthesis, rival interpretation, definitive rulings).

---

## II. The Memex Test

A formal diagnostic for any AI-assisted knowledge system. Can be applied to the worldtext system itself, to external tools, or to any system the operator evaluates.

### The Five Layers of Scholarly Provenance

| Layer | Question | Pass Condition |
|-------|----------|---------------|
| **L1: Initiating Question** | Does the system preserve the *question* that initiated the inquiry, including its transformations? | The original question is stored, and all reformulations are logged |
| **L2: Evidence Field** | Does the system show what sources were consulted, what was selected, and what was ignored? | The full evidence field is inspectable; exclusions are documented |
| **L3: Associative Links** | Does the system preserve the logic of association — *why* this source was connected to that source? | Wikilinks carry annotations or at minimum temporal sequence |
| **L4: Commentary Layer** | Does the system carry the operator's marginalia — notes, reservations, highlights, objections? | The wiki supports inline commentary that is distinct from the system's own text |
| **L5: Branch Structure** | Does the system support forking — building rival trails through the same evidence field? | Alternative readings can coexist without overwriting |

### Scoring

| Score | Assessment |
|-------|-----------|
| 5/5 | **Trail-complete**: the system is a provenance engine |
| 3-4/5 | **Trail-partial**: the system preserves some provenance but conceals some path |
| 1-2/5 | **Trail-impoverished**: the system produces answers but hides most of the path |
| 0/5 | **Trail-less**: the system is a plausibility engine with no provenance |

### Application: RAG vs. Worldtext

| Layer | RAG | Worldtext |
|-------|-----|-----------|
| L1: Initiating Question | ⚠ Partially preserved (query stored, transformations lost) | ✓ Preserved in ritual-ingest log |
| L2: Evidence Field | ✗ Vector similarity selects chunks; exclusions invisible | ✓ Source documents in raw/, ingest log records selections |
| L3: Associative Links | ✗ Chunks connected by embedding proximity, not logic | ✓ Wikilinks carry semantic relationships |
| L4: Commentary | ✗ No commentary layer | ✓ Operator notes in wiki, Explanation Gate rulings |
| L5: Branch Structure | ✗ Single response, no forking | ⚠ Possible but not yet formalized |
| **Score** | **0.5/5** | **4/5** |

---

## III. The Trail Blazer's Protocol

Operational instructions for building trails through the worldtext.

### Step 1: Name the Trail
Every trail has a name. The name is a commitment — it declares what the trail is *about*, what world it opens.

**Example**: "Bateson-to-CRI: How second-order cybernetics became the governor of coherence."

### Step 2: Record the Starting Point
Document the initiating question. Not the refined question — the *original* question, with all its ambiguity and groping.

### Step 3: Build the Trail
For each step:
- Document which source was consulted
- Document *why* this source was chosen (what associative link brought you here)
- Document what was found
- Document what was *not* found (expected but absent)
- Document the decision to proceed or branch

### Step 4: Annotate the Trail
Add marginalia at each node:
- Reservations, objections, excitement
- Connections to other trails
- Questions generated by this node

### Step 5: Close or Branch the Trail
A trail is either:
- **Closed**: it arrives at a conclusion, which is registered in the worldtext (via ritual-ingest or synthesis generation)
- **Branched**: it splits into two or more sub-trails, each pursuing a different implication
- **Suspended**: it has not yet arrived; it remains open, marked for future resumption

### Step 6: File the Trail
The trail is filed in the worldtext as a first-class artifact. It is not discarded after use. It is **the record of thinking** — the most valuable product of the worldtext system.

---

## IV. The Inheritance Problem

Bush's most radical insight: **trails are transmissible.**

> "Wholly new forms of encyclopedias will appear, ready-made with a mesh of associative trails running through them, ready to be dropped into the memex and there amplified."

A worldtext archive is not just the operator's personal workspace. Over time, it becomes an **inheritance** — a set of trails that future operators can follow, contest, fork, and extend.

### Implications for Worldtext Design

1. **Trail literacy**: Operators must be able to read other operators' trails. This requires:
   - Consistent naming conventions
   - Trail metadata (author, date, purpose, status)
   - Commentary that is legible to non-authors

2. **Trail contestation**: Future operators must be able to *disagree* with a trail. This requires:
   - Fork-and-branch capability
   - The ability to annotate an existing trail without modifying it
   - Rival trail coexistence

3. **Trail curation**: Over time, trails accumulate. Some become canonical (ritual-canonization); others become historical; others become obsolete. The worldtext must support trail lifecycle management.

---

## V. The Epistemological Justification for the Tripartite Directory

Bush's architecture provides the *theoretical* justification for the tripartite directory structure already formalized in `causal-worldtext-runtime.md`:

| Layer | Bush | Worldtext |
|-------|------|-----------|
| **The Record** | Everything the owner has encountered | `raw/` — unprocessed source material, original documents, primary evidence |
| **The Index** | The filing system, the catalog, the retrieval mechanism | Schema (`index.md`, `atlas.md`, rituals, distinctions) — the indexical infrastructure |
| **The Trail** | The named, associative paths built through the record | `wiki/` — the compiled knowledge surface, carrying wikilinks, commentary, and synthesis |

The tripartite directory is not arbitrary. It is the physical implementation of Bush's three-layer knowledge architecture: **evidence → index → trail**.

---

## VI. Constitutional Integration

| Existing Component | Connection |
|-------------------|------------|
| `ritual-trail-building` | New ritual, directly derived from Bush |
| `ritual-ingest` | Extended: ingest is *trail-building* when done with provenance awareness |
| `causal-worldtext-runtime.md` | Epistemologically justified: the tripartite directory *is* Bush's architecture |
| `distinction-rag-worldtext` | Quantified: RAG scores 0.5/5 on the Memex Test; Worldtext scores 4/5 |
| `distinction-storage-consultation` | New: the foundational distinction of Bush's theory |
| `distinction-augmentation-substitution` | New: the ethical axis of knowledge system design |
| `conflict-answer-vs-trail` | New: the central conflict between plausibility and provenance |
| `entity-peter-naur` | Connected: Naur's "creative vs. repetitive thought" maps directly to Bush |

---

## VII. Source Documents

- `PAPERS/van.md` — "The Trail as Epistemic Figure: Bush's Memex and the Scholarship Machine"

---

*Synthesis compiled: 2026-04-28. Parent worlds: world-memex-trails. Author: Atlas registration pass.*
