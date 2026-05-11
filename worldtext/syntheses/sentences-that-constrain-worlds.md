# Sentences That Constrain Worlds: From Word Models to World Models

> **Species**: synthesis  
> **Scale**: foundational  
> **Parent System**: [[system-worldtext-operations]]  
> **Source**: Wong et al. (2023), "From Word Models to World Models"  
> **Companion**: [[syntheses/the-dream-must-transfer]] (Ha/Schmidhuber ingest)  
> **Date**: 2026-04-29  
> **Status**: Canonical ingest — the language-side bridge that completes the Ha/Schmidhuber agent-side bridge.

---

## 0. What This Document Is

[[syntheses/the-dream-must-transfer|The Dream Must Transfer]] established the agent-side lineage: Wittgenstein's toy car → Ha/Schmidhuber's latent racing car → Waymo's autonomous driving car. That chain showed how a *model* can substitute for the *world* during training.

This document establishes the **language-side** lineage: how *sentences* become operations over possible worlds. Where Ha/Schmidhuber asked "can an agent learn inside a compressed dream?", this ingest asks the complementary question:

> **Can language function as a control surface for a world model — defining entities, constraining relations, posing queries, updating beliefs, and rejecting invalid continuations?**

The answer is the bridge from **word model** to **world model** — and it gives [[concept-worldtext|Worldtext]] its hardest, most grounded definition.

---

## 1. The Core Claim

A sentence does not merely describe a world. A sentence can **operate** on a world model.

```
<sentence> [adds] <condition>
<sentence> [poses] <query>
<sentence> [defines] <concept>
<sentence> [revises] <model>
<sentence> [rejects] <invalid world>
```

Therefore:

> **Worldtext is a symbolic control system in which language defines, constrains, queries, and revises a model of possible states.** (coined here)

Not "worldbuilding." Not "image-text." Not "vibes in latent space." The hard edge: a text becomes world-bearing when it can constrain what counts as a valid continuation, valid object, valid relation, valid action, or valid inference.

---

## 2. The Problem: Fluent Text Without World Constraint

Current generative AI often treats language as a fluent surface. It predicts plausible continuations without maintaining a stable, inspectable model of what must remain true.

```
<word-model> [predicts] <next plausible text>
<world-model> [maintains] <possible states>
<worldtext> [uses language to operate on those states]
```

The difference between a word model and a world model is the difference between:

| Word Model | World Model |
|-----------|-------------|
| Predicts what sounds right | Tracks what must remain true |
| Generates fluent continuation | Maintains entity, relation, and state consistency |
| Outputs plausible text | Supports inference, revision, and rejection |
| Has no memory of commitment | Remembers what has been defined, conditioned, and constrained |

A system can produce endless descriptions of a world without having a world. A world requires: entities, relations, state, memory, constraints, causes, queries, inference, revision, and failure.

---

## 3. The Technical Architecture (Wong et al.)

Wong et al. (2023) provide the technical hinge. Their architecture:

```
<natural-language>
  → <meaning-function>
  → <probabilistic-program>
  → <inference-over-possible-worlds>
```

A sentence like "Josh beat Lio" does not just add prose to a narrative. It becomes:

```scheme
(condition (won-against '(josh) '(lio)))
```

Not because Scheme is sacred. Because **meaning has become operational**. The sentence:
- Updates the model's belief about Josh's strength (posterior inference)
- Changes the probability of future match outcomes (forward prediction)
- Can be queried ("Who is likely to win next?")
- Can be contradicted ("But Lio has never lost" → conflict detection)

### What the Paper Does Capture

- `<sentence>` is not treated as decoration
- `<sentence>` becomes an operation
- `<operation>` constrains or queries a model
- `<model>` samples possible worlds
- `<answer>` is a posterior estimate

### What the Paper Does Not Implement

- LLM-based translation
- General probabilistic programming
- Kinship reasoning
- Visual scene graphs
- Physics simulation
- Agent planning
- World-model construction from scratch
- Language-guided code editing

The gap between what the paper captures and what it doesn't is itself informative. The architecture works for **simple causal-inferential worlds** (sports match predictions). It does not yet work for thick cultural worlds, mythic systems, or multi-agent ecologies. That gap is where the broader [[concept-worldtext|Worldtext]] framework begins.

---

## 4. The Thinker Lineage

Each thinker donates a specific operative rule. Not decorative authority — an extractable function. (This prevents [[syntheses/worldtext-definitive-theory|F4: Theory Without Operation]].)

### Ludwig Wittgenstein (1921/1953)

**Donation**: A proposition has structure. It arranges elements so they can correspond to a possible state of affairs. The early picture theory: `<sentence> [constructs] <testable arrangement>`.

**What this means for the framework**: A meaningful sentence is not a label. It is a model operation. The framework takes Wittgenstein's picture theory and makes it computational: a meaningful sentence arranges constraints over possible worlds.

**Limitation**: Wittgenstein's later work (the *Investigations*) complicates this — meaning is also use-in-context, not only logical structure. Both contributions are needed: the *Tractatus* gives structure, the *Investigations* give situated practice.

### Peter Naur (1985)

**Donation**: The program is not the code. The real program is the theory held by those who can understand, modify, and extend it. Code is residue. Theory is the living possession.

**What this means**: A world exists only when there is a theory that tells us: what can happen, what cannot happen, what follows from what, what breaks the system, what must be revised. The framework is [[entity-dead-program|Naurian]] because it treats text as part of a living theory, not as decorative output.

### Kenneth Craik (1943)

**Donation**: Organisms carry "small-scale models" of reality that allow them to anticipate events.

**What this means**: Language is not merely expressive. It can alter the internal model used for prediction. "Josh is rarely lazy" does not just add prose — it changes future inference. `<language> [updates] <world-model>`.

**Connection to Ha/Schmidhuber**: Craik's small-scale model is the conceptual ancestor of the VAE + MDN-RNN architecture. Ha/Schmidhuber operationalized Craik's insight as compressed latent dynamics.

### Jay Forrester (1971)

**Donation**: "The image of the world around us, which we carry in our head, is just a model. Nobody in his head imagines all the world."

**What this means**: The mind carries a *selected* model, not the whole world. Language is one way of updating the control model through which action becomes possible. `<mental-model> [guides] <action>` / `<sentence> [modifies] <mental-model>`.

### Jerry Fodor (1975)

**Donation**: The Language of Thought — cognition operates through structured symbolic representations with compositional semantics.

**What Wong et al. add**: They modify Fodor by adding **uncertainty, sampling, and probabilistic inference**. The result is a *Probabilistic* Language of Thought (PLoT):

```
<symbolic-thought> + <probability> = <reasoning-under-uncertainty>
```

**What this means**: Natural language can be translated into structured expressions that support inference. "Josh beat Lio" becomes a conditioning operation in a probabilistic program.

### Noah Goodman & Joshua Tenenbaum (2006–present)

**Donation**: Thought as probabilistic program-like inference over possible worlds. The technical grounding for the whole architecture.

**What this means**: A world is not just a setting. A world is a **generative structure** that can produce possible states and reject inconsistent ones.

```
<world> [is represented as] <generative model>
<belief> [is updated by] <conditioning>
<question> [is answered by] <posterior inference>
```

This is the most grounded technical basis the framework has.

### Judea Pearl (2000)

**Donation**: Causality, not just association. If a world model cannot distinguish correlation from intervention from cause from counterfactual, it cannot support serious world reasoning.

**What this means**:

```
<event> [changes] <state>
<intervention> [modifies] <causal structure>
<counterfactual> [tests] <alternate world>
```

This prevents the framework from becoming mere "semantic mood." **A governing text must support causal reasoning, not only statistical association.**

### Lucy Suchman (1987)

**Donation**: Plans do not determine action in a clean top-down way. Human action is situated, improvised, and revised in context.

**What this means**: `<plan> [guides but does not exhaust] <situated-action>`. A world model is useful, but it is never complete. Language operates inside actual contexts of use.

**This prevents**: The framework from becoming rigid formalism. It is the Suchman guard against [[syntheses/worldtext-definitive-theory|F6: Technocratic Capture]].

### Edwin Hutchins (1995)

**Donation**: Distributed cognition. Meaning is not only in the model. It is in the whole working arrangement — people, documents, interfaces, diagrams, logs, prompts, code, tools, memory systems.

**What this means**: `<cognition> [is distributed across] <symbolic-environment>`. The framework should not be treated as something inside one mind or one model. It is a property of the entire sociotechnical system.

### Bruno Latour (1986)

**Donation**: Inscriptions act. A chart, a map, a legal document, a lab report, or a model can reorganize action because it stabilizes relations.

**What this means**: `<inscription> [stabilizes] <relation>` / `<relation> [enables] <action>`. The framework is not "text as metaphor." It is **text as an actor in a sociotechnical system**.

---

## 5. The Minimal Conditions

A symbolic system counts as a governing text only if it supports at least some of the following:

| Operation | What It Does | Example |
|-----------|-------------|---------|
| `[define]` | Creates an entity or concept | "The Candle Quarter has no electric light" |
| `[relate]` | Connects entities | "The blacksmith serves the temple" |
| `[condition]` | Constrains possible worlds | "INVARIANT: Salt water is profane" |
| `[query]` | Asks what follows | "If the river floods, what changes?" |
| `[infer]` | Derives unseen variables | "Josh beat Lio → Josh is probably strong" |
| `[revise]` | Updates definitions | "INVARIANT_05 (REVISED): The dead are NOT stored in walls" |
| `[reject]` | Blocks invalid continuations | "FATAL: A sailor dipped his hand in the sea" |
| `[explain]` | Traces failure to source | "The violation traces back to INVARIANT_06" |

**No enforcement, no governing text.** A text that permits every continuation governs nothing.

---

## 6. Against Pretty Mud

"Pretty mud" (coined in [[syntheses/hello-worldtext|Chapter 01]]) means unconstrained generative output: fluent, visual, evocative, but not structurally accountable.

**Grounded definition**: A generative system produces "pretty mud" when it generates plausible surfaces without preserving inspectable constraints over entities, relations, and state transitions.

This is not an insult. It is a diagnostic. The governing framework exists specifically because:

```
<fluency> ≠ <world model>
<description> ≠ <constraint>
<continuation> ≠ <inference>
```

Most AI-generated worlds are pretty mud. They sound right. They do not hold together.

---

## 7. The Bridge from Word Model to World Model

The central law the future maintainer must understand:

> **A language system becomes a world-model system only when sentences can constrain, query, define, reject, and revise possible worlds.**

This is the bridge from `<word model>` to `<world model>`.

It completes the two-sided architecture:

| Side | Paper | Question | Answer |
|------|-------|----------|--------|
| **Agent** | Ha/Schmidhuber (2018) | Can an agent learn inside a compressed dream? | Yes, if the dream transfers to reality |
| **Language** | Wong et al. (2023) | Can language operate on a world model? | Yes, if sentences constrain possible states |
| **Framework** | This synthesis | Can language govern a dream that transfers? | That is the open problem |

The framework names the convergence: **language as the control surface for world models that agents act inside.**

---

## 8. Limits

The theory must remain honest about what it does not claim:

- ❌ All language is code
- ❌ All meaning is computation
- ❌ All worlds are formal systems
- ❌ All ambiguity should be eliminated

Instead:

- ✅ *Some* uses of language become more powerful when made operational
- ✅ *Some* worlds require ambiguity (see [[syntheses/worldtext-definitive-theory|§8: The Metis Principle]])
- ✅ *Some* models must remain revisable
- ✅ *Some* meaning remains situated (Suchman)
- ✅ *Some* cognition is distributed (Hutchins)
- ✅ *Some* inscriptions act without being formalized (Latour)

This is where the thinker lineage prevents the theory from becoming rigid. Wittgenstein gives structure. Suchman gives situated practice. Hutchins gives distribution. Latour gives material agency. Pearl gives causality. Together they prevent any single axis from dominating.

---

## 9. The Academic Frame

For those who need the formal argument:

**Abstract**: This synthesis argues that language becomes world-bearing only when it operates on an explicit or implicit model of possible worlds. Drawing on Wittgenstein's picture theory, Naur's account of programming as theory building, Fodor's language of thought, and contemporary probabilistic cognitive science (Goodman, Tenenbaum, Wong et al.), it defines the governing framework as a symbolic system in which utterances can condition, query, define, and revise structured world models. Against accounts of generative AI as mere fluent continuation, it distinguishes between text that predicts plausible surfaces and text that constrains possible states. The central claim: a world is not produced by description alone; it emerges when symbolic operations enforce consistency, support inference, expose contradiction, and make revision possible.

**One paragraph**: The framework names language that operates on a model of possible worlds. It begins from a simple distinction: a word model predicts plausible continuations, while a world model maintains entities, relations, constraints, uncertainty, and state. Drawing on Wittgenstein, Naur, Fodor, Goodman, Tenenbaum, and the probabilistic language-of-thought tradition, it treats sentences as operations: they define concepts, condition beliefs, pose queries, revise assumptions, and reject invalid continuations. The point is not that all language is code. The point is that some language becomes world-bearing only when it can constrain what follows.

---

## 10. Transfer to the Governing Framework

The Wong et al. donation to the [[syntheses/worldtext-definitive-theory|definitive theory]] is fourfold:

1. **The word-model/world-model distinction**: The sharpest diagnostic the framework has. Does the system predict plausible text, or does it maintain possible states?

2. **The probabilistic grounding**: The framework is not just metaphor. Sentences can literally become conditioning operations in a probabilistic program. Goodman and Tenenbaum proved this.

3. **The thinker lineage expansion**: Craik, Fodor, Pearl, Suchman, Hutchins, and Latour join the framework's intellectual ancestry — each donating a specific operative rule, not a decorative citation.

4. **The hardest definition**: "Worldtext is a symbolic control system in which language defines, constrains, queries, and revises a model of possible states." This is harder than anything in the existing documents.

---

## Cross-References

- [[syntheses/worldtext-definitive-theory]] — The definitive theory (this ingest strengthens §1 and §3)
- [[syntheses/the-dream-must-transfer]] — The agent-side companion (Ha/Schmidhuber)
- [[syntheses/hello-worldtext]] — Chapter 01 (the worked examples are tests of this thesis)
- [[syntheses/spatial-language-program-theory]] — The 24 programs
- [[syntheses/seven-failure-modes]] — F1 (Pretty Mud) is the diagnostic this paper grounds
- [[concept-worldtext]] — The foundational concept
- [[entity-dead-program]] — Naur's theory of program death
- [[entity-geertz]] — Geertz's cultural control programs (parallel to probabilistic programs)
- [[world-latent-space]] — Latent space as the substrate where word models approximate world models
- [[distinction-fluency-fidelity]] — The fluency/fidelity gap this paper makes precise

---

*A world begins when language has consequences inside a model. Not emotional consequences only. Operational consequences. A sentence must be able to change what is possible. That is where prose gains enforcement. That is where description becomes governing text.*
