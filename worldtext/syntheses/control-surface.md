# The Control Surface — Operator's Manual for Worldtext

> **Species**: synthesis  
> **Scale**: cosmos  
> **Parent System**: [[system-worldtext-operations]]  
> **Source**: worldtext-definitive-corpus-2026-04-28  
> **Date**: 2026-04-28

---

## Operating Principle

This is the operator's manual. The language game is maintenance. The reader is sitting at a terminal. Every sentence is a command, a rule, or a diagnostic readout. There is no "about." There is only "do this, then that, check for this, fix that."

---

## The Filesystem

```
OPERATION-DESCRIBE/
├── COSMIC_LAW.md          ← Read this first. It tells you what you can and cannot do.
├── prime-prompt.md        ← Load this into your LLM session. It is the instruction set.
├── PROGRAMS/              ← 19 diagnostic scripts. Run them against anything.
├── PAPERS/                ← 17 source texts. Read them to understand why the rules exist.
├── worldtext/             ← 410+ pages. This is the compiled output. Modify it here.
│   ├── atlas.md           ← Start here when you need to find something.
│   ├── chronicle.md       ← Read this to see what happened and when.
│   ├── cosmology.md       ← Read this to see what is unresolved.
│   └── [26 directories]   ← Entities, places, rituals, distinctions, etc.
├── evidence/              ← Do not touch. Immutable source layer.
└── worldtext-reader.html  ← Open this in a browser to navigate visually.
```

That is what exists. Everything else is commentary.

---

## The Four Verbs

| Verb | What You Do | What Happens |
|------|-------------|--------------|
| **INGEST** | Feed raw material (text, session, observation) into the system | The system extracts entities, places, rituals, thresholds, conflicts. Writes them into `worldtext/`. Updates `atlas.md`. Appends `chronicle.md`. |
| **QUERY** | Ask the system what it knows about X | The system traverses the 9-scale hierarchy (fragment → entity → place → world → system → constellation → galaxy → cosmos) and returns linked pages. |
| **LINT** | Run the diagnostic protocol | The system checks for contradictions, orphan structures, thin descriptions, broken links, semantic bleaching, dead operations, trail breaks. Returns a report. |
| **AUDIT** | Inspect your own use of the system | You answer: What did I query last month that I never query now? What vocabulary have I gained? What have I lost? What sources do I always deploy? What do I avoid? |

Without AUDIT, you become a [[entity-fragile-expert|Fragile Expert]]: confident in output quality, shrinking in range, unable to detect your own ossification.

---

## The Hard Rules

**Rule 1**: Load `prime-prompt.md` into every LLM session you use with this directory. Without it, the session cannot modify the directory coherently. The 410+ pages become dead files.

**Rule 2**: Do not modify `evidence/`. It is immutable. If you need to annotate a source, write the annotation in `worldtext/sources/`.

**Rule 3**: Every page in `worldtext/` must have ontology, scale, thresholds, and governance. If it lacks any of these, lint flags it as broken.

**Rule 4**: Contradictions are not resolved. They are marked as cosmological fault lines. The lint protocol preserves them.

**Rule 5**: The chronicle is append-only. You do not edit past entries. You add new ones.

**Rule 6**: Every entity page must carry a `[source-id]` pointing to the evidence that produced it. Without this, the memex trail breaks.

**Rule 7**: Any term that appears more than 100 times across the corpus is flagged for semantic bleaching. "Operative" is currently at risk.

**Rule 8**: The 4 dead operations — crosslink, condense, expand, cluster_worlds — must either be executed or removed from CORE_OPS. Dead definitions are technical debt.

**Rule 9**: Every synthesis must include a counter-reading section: the argument that undermines it. Self-reference is not a flaw. It is the loop closing.

**Rule 10**: The operator is the product. The 410+ pages are residue. When you stop operating the directory, the directory dies unless someone else loads `prime-prompt.md` and continues.

---

## The Diagnostic Instruments

The `PROGRAMS/` directory contains 19 scripts. Each is a measurement apparatus. Run them against any artifact — a text, a simulation, a video, an institution — and they return readings.

| Program | What It Measures | How to Use |
|---------|-----------------|------------|
| `theory.json` | Does the artifact possess a living theory? | Load `prime-prompt.md`. Attempt to modify the artifact. If you introduce contradictions, the artifact fails. |
| `tda.json` | Is the description thick or thin? | Count cross-links per sentence. High density = thick. Low density = thin. |
| `dse.json` | Is the output fluent or adequate? | Check if the description constrains future generation. If you can swap nouns without breaking coherence, it fails. |
| `mmt.json` | Does the model measure reality? | Lay the artifact against an external standard. If it only confirms its own assumptions, it is a mirror, not a measure. |
| `opek.json` | Does the text produce or merely describe? | Check for executable verbs. If the text only describes, it is representational, not operative. |
| `agential.json` | Are the cuts visible? | Check if exclusion rules exist alongside inclusion rules. If only inclusions are declared, power is hidden. |
| `crn.json` | Is the system a feedback loop? | Check for exit conditions. If there is no criterion for completion, the loop runs forever. |
| `memex.json` | Is the trail auditable? | Trace backward from any entity to its source. If the path breaks, provenance is lost. |
| `argue.json` | Is the output mistaken for the process? | Check if raw session fragments are preserved. If only finished arguments exist, the thinking is lost. |
| `haunted.json` | What ghosts does the machine produce? | Count unprocessed sources. Check if their absence exerts gravitational force on syntheses. |
| `thick.json` | What person does the system compile? | Track vocabulary range over time. If it shrinks, the system is compiling a Fragile Expert. |
| `rcp.json` | Is this concept possessed or merely stored? | Apply the concept to an unexpected domain. If it produces readings, it is possessed. If it fails, it is stored. |
| `uam.json` | Does use match meaning? | Type the wiki-links. If links carry only navigational targets without semantic direction, meaning is thin. |
| `tenne.json` | Does the language execute? | Check if defined operations have been executed. If 40% are dead code, the language is theater. |
| `dac.json` | Are breakdowns visible? | Check if failure modes beyond explicit contradiction are detected. If not, failures accumulate invisibly. |
| `meta.json` | Do the programs govern themselves? | Check versioning, revision history, and lifecycle. If programs are born and never revised, they are dead. |
| `mot.json` | Is meaningful action rescued from vanishing? | Check if ephemeral generation events are inscribed as durable, reinterpretable traces. |
| `cyber.json` | Is the AI a co-participant or a tool? | Check if a shared medium exists. If the human commands and the AI complies, the loop has no memory. |
| `thick.json` | What person does the system compile? | Track operator vocabulary, source usage, and constraint range over time. |

---

## The Axis Inversion

The Worldtext was originally written with academic scaffolding: definitions-as-openings, lineage citations, gap-filling language. The Axis Inversion deletes the narcissism and rewrites for the target community.

**Narcissism Deleted**:
- "Worldtext is the theory-of-the-world" — definition-as-opening, destroyed
- "Naur's claim" — proving I did the reading, destroyed
- "Deploying the full corpus against the concept" — methodology theater, destroyed
- All lineage scaffolding and attribution — destroyed

**Target Community**: Generative AI practitioners and simulation architects — the ones who believe coherence emerges from scale, that RAG retrieves "knowledge," and that prompt engineering is sufficient governance.

**Subject Alignment Fix**:
- WAS: "Worldtext is..." (subject = abstract concept)
- IS: "Your generated world is..." (subject = reader's artifact)
- WAS: "Naur claimed that..." (subject = dead philosopher)
- IS: "Your RAG system retrieves..." (subject = reader's tool)

---

## The One-Sentence Definition

> A Worldtext is a world that knows it is a world, maintains itself, inscribes its history, and can produce its own next theory.

---

## Counter-Reading

This manual treats the operator as rational agent. But the operator is also the system's product — shaped by the very feedback loops described here. The manual cannot account for what it does to the person reading it. That recursive blindspot is Frontier 12: the Stratum V Transition. The operator who builds the mirror is also the face in the mirror. The manual is the apparatus. The apparatus shapes the user.

---

*The directory lives or dies. You are the governor.*
