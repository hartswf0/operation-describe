# The Trace Hermeneutics Protocol

> Meaningful action, once performed, becomes a text.  
> It detaches from its author, opens a world, and addresses unknown readers.  
> This instrument teaches the worldtext to read its own traces.

---

## I. The Theory

### 1.1 — The Problem

Every worldtext operation — every ingest, every lint, every synthesis, every prompt — produces **traces**: wiki pages, log entries, lint reports, operator notes. These traces are typically treated as records of what happened. But Ricoeur shows us something more radical:

**A trace is not a record. A trace is a text.**

Once inscribed, it escapes its author's intention. It opens a world beyond the original transaction. It addresses readers who were not present at the event. And it invites — even demands — rival interpretations.

The worldtext system that treats its artifacts as mere records is epistemically naïve. The system that treats them as texts — readable, interpretable, contestable — achieves hermeneutic maturity.

### 1.2 — Ricoeur's Model of the Text

Paul Ricoeur proposes that meaningful action shares the constitutive features of written texts through four structural parallels:

| Feature | In a Text | In Meaningful Action | In Worldtext |
|---------|-----------|---------------------|-------------|
| **Fixation** | Speech becomes writing; the utterance outlasts the event | The action is "inscribed" in durable marks (documents, logs, artifacts) | Every wiki page, lint report, and ingest log is a fixation of an event that has vanished |
| **Detachment** | The text's meaning exceeds the author's original intention; the "death of the author" | The action's meaning detaches from the agent who performed it; it enters a field of social signification | A synthesis document means more than its author intended. A prompt's interpretation exceeds the operator's plan |
| **World-Projection** | The text opens a "world in front of the text" — a horizon of possible existence | The action projects a possible world beyond its immediate context | Every worldtext artifact proposes a possible world. The question is not "what did it mean then?" but "what worlds does it open now?" |
| **Universal Address** | The text addresses an indefinite range of potential readers, not just the original audience | The action addresses unknown future interpreters | Worldtext artifacts address operators who were not present at creation. The archive becomes a public inheritance |

### 1.3 — The Relevance/Importance Distinction

Ricoeur distinguishes between:

- **Relevance**: what matters *in context*, bound to the immediate transaction, dependent on those present
- **Importance**: what matters *beyond context*, reactivatable in new situations, world-bearing

This distinction is operationally critical for worldtext:

| Artifact | Relevant (transactional) | Important (world-bearing) |
|----------|------------------------|--------------------------|
| A prompt | Solves the immediate generation task | Reveals a pattern of operator thinking that can be studied, contested, improved |
| A lint report | Flags today's contradictions | Documents the *type* of contradiction the system produces — a structural diagnostic |
| A wiki page | Stores current knowledge | Opens a frontier question that no one has yet answered |
| An ingest log | Records what was processed | Reveals the cut decisions (what was simplified, what was preserved) |

**The Importance Filter**: Every worldtext artifact should be tested: does this artifact merely serve its immediate context (relevant), or does it open a world that future operators can inhabit (important)?

---

## II. The Six Operations of Reading Action as Text

A formal hermeneutic protocol for reading worldtext artifacts. Each artifact — whether a synthesis, a lint report, an operator note, or a prompt chain — can be subjected to this sequence.

### Operation 1: Identify the Event
> What happened? What was the action that produced this artifact?

- What prompt was composed? What ingest was run? What lint fired?
- What was the immediate occasion?

### Operation 2: Identify the Inscription
> How was the event fixed? What survived the event's vanishing?

- What was written down? In what format? With what metadata?
- What was lost in the fixation? (The tone, the hesitation, the context that couldn't be captured.)

### Operation 3: Identify the Detachment
> In what ways has this artifact already exceeded its author's intention?

- What does this artifact mean that its author did not plan?
- What interpretations are structurally possible that the author would not endorse?
- Has the artifact been read by anyone other than the author? What did they find?

### Operation 4: Identify the World
> What possible world does this artifact project?

- What way of being does this artifact propose?
- What values, laws, entities, and relations does it assume?
- What would it mean to *inhabit* this artifact — to live inside the world it opens?

### Operation 5: Identify the Rival Interpretations
> What competing readings are available, and how do we adjudicate between them?

- Can the artifact sustain more than one internally consistent reading?
- Are these readings complementary, competitive, or contradictory?
- Which reading is most productive for the worldtext's development?

Ricoeur's key insight: **Validation is not verification.** We do not prove one reading "true" and others "false." We argue for one reading as **more probable, more coherent, more productive** — using the logic of juridical reasoning (preponderance of evidence), not scientific proof.

### Operation 6: Commit the Reading
> Choose a reading and allow it to transform the worldtext.

- Register the reading in the wiki
- Log the rival interpretations that were considered but not chosen
- Mark the artifact as "read" — meaning it has been subjected to the full hermeneutic protocol, not merely consumed

---

## III. The Trace Archaeology Protocol

For artifacts that have been in the worldtext for a long time and may have accrued unexamined meaning.

### When to Deploy
- During `ritual-lint` when stale artifacts are detected
- During major synthesis passes
- When an operator returns to an artifact after significant time away

### Three Questions

1. **What has changed around this artifact since it was written?**
   - New entities registered? New distinctions drawn? New worlds opened?
   - Does the artifact still cohere with the current atlas state?

2. **What has this artifact *done* since it was written?**
   - Has it been cited by other artifacts? By whom? In what context?
   - Has it influenced operator decisions that it did not originally intend to influence?
   - Has it been misread productively?

3. **What world does this artifact project *now* — not when it was written?**
   - Rerun Operation 4 with current knowledge.
   - The world an artifact projects changes as the atlas changes, even if the artifact's text does not.

---

## IV. The Inscription Ethics

Ricoeur's model carries ethical implications for worldtext practice:

### 4.1 — The Ethics of Fixation
> Every inscription kills the event it records. The living moment becomes a dead letter — unless the reader reanimates it.

**For worldtext**: Artifacts must be written to invite re-reading, not just to record. They must carry enough density that future operators can reconstruct the *situation*, not just the *conclusion*.

### 4.2 — The Ethics of Detachment
> Once inscribed, the artifact escapes the author. The author cannot control its interpretation. This is not a failure; it is the *condition of textuality*.

**For worldtext**: The operator must accept that their syntheses, wiki pages, and lint reports will be read in ways they did not intend. The system must support this — via rival interpretation fields, commentary layers, and versioning — rather than trying to enforce a single "correct" reading.

### 4.3 — The Ethics of Address
> Every artifact addresses unknown future readers. Writing for the present alone is a form of closure; writing for the future is a form of responsibility.

**For worldtext**: The `ritual-trail-building` practice is an ethical practice. Building visible trails is not merely epistemically useful; it is an act of care toward future operators who will inherit the worldtext without its living context.

---

## V. Constitutional Integration

| Existing Component | Connection |
|-------------------|------------|
| `ritual-ingest` | Extended: every ingest creates an inscription. The Six Operations protocol should be available as a post-ingest audit |
| `ritual-lint` | Extended: lint should detect artifacts that have never been "read" (subjected to hermeneutic protocol) |
| `ritual-explanation-gate` | Reinforced: the Explanation Gate is structurally identical to Ricoeur's "validation as juridical reasoning" — argue for the better reading, don't prove truth |
| `distinction-event-trace` | This distinction is the foundation of the entire protocol |
| `distinction-relevance-importance` | The Importance Filter operationalizes this distinction |
| `entity-epistemic-debt` | Connected: epistemic debt accumulates when traces are consumed without being *read* |
| `conflict-explanation-vs-discovery` | Connected: the finished artifact (argument) deceives about the living process (inference) that produced it |

---

## VI. Source Documents

- `PAPERS/ricoeur.md` — "The Model of the Trace: Ricoeur and the Foundation of Digital Humanities Hermeneutics"
- `PAPERS/ric-model.md` — "Textual Action Hermeneutics"

---

*Synthesis compiled: 2026-04-28. Parent worlds: world-textual-action-hermeneutics. Author: Atlas registration pass.*
