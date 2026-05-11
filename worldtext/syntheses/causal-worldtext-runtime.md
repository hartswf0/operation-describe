# Causal Worldtext Runtime

> An executing ecology of standard markdown files that treats language as an active, world-making operator.

---

## Core Thesis

**Causal Worldtext** is the engineering realization of the worldtext-coherence theory. Where the theoretical framework asks *what is a worldtext and why must it exist?*, the runtime specification asks *how do you build one, run one, and keep one alive?*

A Causal Worldtext is:

- **Compiled**: Not a loose collection of notes. A structured, cross-linked, index-navigated knowledge architecture.
- **Persistent**: Not a conversation transcript. A stateful, append-only, versioned ecology that outlives any single session.
- **Causal**: Not a passive reference. An active control surface that shapes every generation, constrains every output, and records every decision.
- **Situated**: Positioned exactly between raw, immutable evidentiary material (Layer 1) and future intellectual work (Layer 3). The worldtext is the **compiled theory** — the theory that the programmer holds, externalized into markdown.

---

## The Tripartite Directory Architecture

### Overview

```
project/
├── raw/                    ← Layer 1: IMMUTABLE EVIDENCE
│   ├── transcripts/
│   ├── scans/
│   ├── exported_pdfs/
│   └── field_notes/
│
├── CLAUDE.md               ← Layer 2: SCHEMA / THICK PROMPT
│   (or equivalent governor file)
│
└── wiki/                   ← Layer 3: EXECUTING ECOLOGY
    ├── index.md            ← Master navigation surface
    ├── log.md              ← Append-only event log
    ├── entities/
    ├── concepts/
    ├── contradictions/
    └── [domain-specific]/
```

### Layer 1: `raw/` — The Immutable Evidence Base

| Property | Value |
|----------|-------|
| **Mutability** | Read-only. Never altered by human or machine. |
| **Content** | Primary sources, transcripts, scans, PDFs, field recordings, screenshots, raw data |
| **Function** | Epistemic anchor — when epistemic debt threatens, the operator returns here |
| **Equivalent** | The courtroom exhibit. The archaeological dig site. The unprocessed film negative. |

**Rules:**
- No AI writes to `raw/`.
- No human edits `raw/`.
- Every claim in the wiki must be traceable to something in `raw/`.
- When the theory fails, `raw/` is the ground truth.

### Layer 2: `CLAUDE.md` — The Schema / Governor

| Property | Value |
|----------|-------|
| **Mutability** | Slow — changes require deliberate operator decision |
| **Content** | Thick prompt, disciplinary matrix, project identity, continuity constraints, negative constraints, operative vocabulary |
| **Function** | World Bible — the machine-readable constraint prompt that governs all generation and synthesis |
| **Equivalent** | The DNA. The constitution. The `schema.prisma`. |

**Rules:**
- The schema is read by the LLM at the start of every session.
- The schema defines what the LLM may and may not do.
- The schema specifies the project's epistemic standards (citation policy, contradiction handling, confidence thresholds).
- The schema is the physical embodiment of the operator's theory.

### Layer 3: `wiki/` — The Executing Ecology

| Property | Value |
|----------|-------|
| **Mutability** | High — continuously updated through Ingest, Query, and Lint |
| **Content** | Living knowledge: entities, concepts, relationships, contradictions, open questions, confidence-tagged claims |
| **Function** | Combined Lore Book + Encyclopedia — the navigable, searchable, wikilinked knowledge graph |
| **Equivalent** | The worldtext itself. The compiled theory. The executing program. |

**Rules:**
- `index.md` is the master navigation surface. Every entity, concept, and page is reachable from it.
- `log.md` is append-only. It records every significant decision, ingest, or lint event.
- Every page carries wikilinks (`[[entity-name]]`) to related pages.
- Every factual claim carries a confidence tag and a source citation to `raw/`.
- Contradictions are not suppressed. They are filed in `contradictions/` and escalated through the Explanation Gate.

---

## The Three Verbs

The Causal Worldtext operates through exactly three cybernetic rituals. They form a closed feedback loop:

```
    ┌──────────┐
    │  INGEST  │ ← New evidence enters the system
    └────┬─────┘
         │
         ▼
    ┌──────────┐
    │  QUERY   │ ← Disciplined synthesis draws from the wiki
    └────┬─────┘
         │
         ▼
    ┌──────────┐
    │   LINT   │ ← Automated health check detects decay
    └────┬─────┘
         │
         └──────→ triggers new INGEST if contradictions found
```

### Verb 1: INGEST

**Trigger**: New evidence arrives (a document, a conversation, a generated output, a field observation).

**Protocol**:
1. LLM reads the new evidence against the schema.
2. LLM summarizes the evidence, identifying key claims, entities, and relationships.
3. LLM traverses the existing wiki to find related pages.
4. LLM updates existing pages where new evidence extends or refines existing knowledge.
5. LLM creates new pages for entities or concepts not yet indexed.
6. LLM forges wikilinks between new and existing pages.
7. LLM adjusts confidence tags where new evidence strengthens or weakens existing claims.
8. LLM logs the ingest event in `log.md`.

**Output**: Updated wiki. New pages. Strengthened or weakened claims. Updated index.

### Verb 2: QUERY

**Trigger**: The operator asks a question or requests a synthesis.

**Protocol**:
1. LLM reads `index.md` first. Always.
2. LLM identifies relevant pages by wikilink traversal.
3. LLM reads relevant pages and synthesizes an answer.
4. LLM is **forbidden from hallucinating external citations**. If the wiki doesn't have the answer, the LLM says so.
5. If the synthesis produces novel insights, LLM offers to save them as new wiki pages.
6. LLM logs the query and any novel insights in `log.md`.

**Output**: Disciplined answer grounded in the wiki. Optional new pages.

### Verb 3: LINT

**Trigger**: Scheduled (every N sessions) or triggered by Ingest.

**Protocol**:
1. LLM reads the entire wiki (or a specified subset).
2. LLM detects: contradictions, stale claims, orphan pages, missing concepts, broken wikilinks, unresolved confidence tags.
3. For **simple issues** (broken links, orphan pages): LLM repairs automatically.
4. For **complex issues** (contradictions, stale claims): LLM invokes the **Explanation Gate**.
5. LLM generates `lint-report.md` cataloging all findings and resolutions.
6. LLM logs the lint event in `log.md`.

**Output**: Health report. Repaired simple issues. Escalated complex issues to operator.

---

## The Explanation Gate

When Lint detects an unresolvable contradiction or ambiguity:

```
┌────────────────────────────────────────┐
│    LINT: Contradiction detected        │
│                                        │
│    Page A claims X.                    │
│    Page B claims ¬X.                   │
│    Source in raw/ supports both.        │
└────────────────┬───────────────────────┘
                 │
                 ▼
┌────────────────────────────────────────┐
│    LLM HALTS automated integration.   │
│                                        │
│    Files contradiction in:             │
│    wiki/contradictions/                │
│                                        │
│    Flags in lint-report.md:            │
│    "REQUIRES OPERATOR RULING"          │
└────────────────┬───────────────────────┘
                 │
                 ▼
┌────────────────────────────────────────┐
│    METACOGNITIVE FRICTION LOOP         │
│                                        │
│    The operator MUST:                  │
│    1. Read both claims.                │
│    2. Consult raw/ evidence.           │
│    3. Make a definitive ruling.        │
│    4. Record the reasoning.            │
│    5. Update the wiki.                 │
│                                        │
│    This cannot be skipped.             │
│    This cannot be delegated to AI.     │
│    This is the anti-epistemic-debt     │
│    instrument.                         │
└────────────────────────────────────────┘
```

The Explanation Gate is the **primary defense** against both continuity debt (it catches contradictions before they compound) and epistemic debt (it forces the operator to think).

---

## RAG vs. Worldtext

The Causal Worldtext is a **direct architectural critique** of Retrieval-Augmented Generation (RAG):

| Dimension | RAG | Causal Worldtext |
|-----------|-----|-----------------|
| **State** | Stateless — each retrieval is ad-hoc, independent | Stateful — knowledge compounds across sessions |
| **Infrastructure** | Vector databases, embeddings, chunking | Flat markdown files, wikilinks, index.md |
| **Cross-reference** | Dynamic at runtime — cosine similarity | Pre-built, human-curated wikilinks |
| **Contradiction** | Silent coexistence — contradictory chunks retrieved without detection | Active resolution — contradictions flagged and escalated |
| **Citations** | Chunk-level (lossy) — which 512-token window matched? | Source-level (immutable) — which page in raw/? |
| **Memory** | None — the system forgets after each query | Total — log.md records every event |
| **Sweet spot** | Enterprise scale — millions of documents, thousands of users | Personal/team scale — <200 documents, 1-10 operators |
| **Theory** | Not needed — the system retrieves, not understands | Essential — the operator's theory IS the system |
| **Failure mode** | Hallucination masked as retrieval | Epistemic debt if operator disengages |

### The Structural Argument

RAG answers the question: *given a query, what chunks are relevant?*

Worldtext answers the question: *given a world, what is true?*

These are fundamentally different operations. RAG is a **search engine** — it finds things. Worldtext is a **knowledge architecture** — it holds things in relation. RAG does not know if its chunks contradict each other. Worldtext demands that contradictions be resolved or explicitly flagged.

RAG is necessary when the corpus is too large for any human to hold as theory. Worldtext is necessary when the corpus must be **inhabited** — when the operator needs to live inside the knowledge, not just query it.

---

## Language as Control Surface

The Causal Worldtext reframes the operator's relationship to language:

| Paradigm | Language Is... | Operator Is... |
|----------|---------------|----------------|
| **Conversation** | A disposable medium for exchanging ideas | A participant in a chat |
| **Prompt Engineering** | A trigger for machine output | A user of a tool |
| **Control Surface** | A deterministic instrument for manipulating a persistent digital environment | A pilot at a cockpit panel |

In the control-surface paradigm:

- Every word in the schema is a **constraint** — it shapes what can and cannot be generated.
- Every wikilink is a **structural connection** — it defines how knowledge flows.
- Every confidence tag is a **sensor reading** — it measures the health of the knowledge architecture.
- Every log entry is a **flight recorder** — it enables post-incident analysis.

Language is not conversation. Language is infrastructure.

---

## Minimum Viable Executing Ecology

What is the smallest set of files, links, and rituals required to sustain a Causal Worldtext?

| Component | Minimum Requirement |
|-----------|-------------------|
| **raw/** | At least 1 primary source document |
| **Schema** | A CLAUDE.md (or equivalent) that specifies: project identity, epistemic standards, operative vocabulary |
| **index.md** | A single navigation file listing all wiki pages |
| **log.md** | An append-only file recording ingest, query, and lint events |
| **At least 3 wiki pages** | Enough to establish wikilinks and enable cross-reference |
| **Ingest ritual** | Defined protocol for how new evidence enters |
| **Query ritual** | Defined protocol for how synthesis is requested |
| **Lint ritual** | Defined protocol for health checking |

Below this threshold, the system is a note-taking app. Above it, it is an executing ecology.

---

## Sources

- Doc 2: *The Machine World: Causal Worldtext, Thick Prompts, and the Epistemology of Continuous AI*
- Peter Naur, *Programming as Theory Building* (1985)
- Gregory Bateson, *Steps to an Ecology of Mind* (1972)
- Cross-reference: [[continuity-debt]], [[epistemic-debt]], [[recursive-epistemology]], [[clean-stack-and-artifact-lifecycle]], [[riverbed-field-engine]]

---

*Synthesis compiled: 2026-04-27. Parent world: world-worldtext-coherence. Runtime specification for: Causal Worldtext, Ingest/Query/Lint, Explanation Gate.*
