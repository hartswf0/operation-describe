# Concept: The Context Stack

> **Species**: concept  
> **Scale**: foundational  
> **Parent Galaxy**: [[galaxy-of-generative-ai-worlds]]  
> **Created**: 2026-04-14  
> **Source**: "Operative Ekphrasis and Context Engineering"; Karpathy (2024); Willison (2025)

---

## Definition

**The context stack** is the full architectural layering of information that conditions an AI model's behavior. It replaces "prompt" as the unit of analysis for operative ekphrasis.

Andrej Karpathy's analogy: *"The LLM is the CPU. The context window is the RAM."* Context engineering is the operating system that manages the RAM — loading, prioritizing, and structuring the information that the model uses at inference time.

## Why "Prompt" Is Not Enough

The word "prompt" implies a single text string typed by a user. But what actually conditions a model's generation is the entire **context stack** — a layered structure far more complex than any individual prompt:

| Layer | Name | Content | Thick Prompt Equivalent |
|-------|------|---------|------------------------|
| **L0** | Hardware / Model | Architecture, parameter count, training mix | — (substratum, like geology beneath the stratigraphy) |
| **L1** | System instruction | Constitutional prompt, persona, tone, refusal rules | **Layer 3 (Code)** — the normative order |
| **L2** | Knowledge context | RAG-retrieved documents, database results, memory | **Layer 3 (Code)** — the cultural/factual substrate |
| **L3** | Tool context | API definitions, function schemas, capability map | **Layer 1 (Visible act)** — what acts are physically possible |
| **L4** | Conversation history | Prior messages, assistant responses, user corrections | **Layer 4 (Audience)** — the interactional trail |
| **L5** | User instruction | The immediate prompt | **Layer 1+2 (Visible act + Native act)** |
| **L6** | Output constraints | Format requirements, safety filters, temperature | **Layer 5+6 (Stakes + Reclassification)** |

## Context Engineering ≠ Prompt Engineering

| Prompt Engineering | Context Engineering |
|-------------------|-------------------|
| Writes a better sentence | Builds a better information architecture |
| Optimizes the **user instruction** (L5) | Optimizes the **entire stack** (L0–L6) |
| Treats the model as a black box to be persuaded | Treats the model as a CPU to be properly programmed |
| Art / craft / magic spells | Software engineering / systems design |
| Unit: the prompt | Unit: the context stack |

The shift from prompt engineering to context engineering is the shift from **writing** to **architecture**. The thick prompter who adds six layers to a single prompt string is still operating at L5. The context engineer who designs the full stack from system instruction to output constraints is building an **operative environment** — a world within which the model generates.

## The Context Stack and the WorldText

The context stack IS a minimal worldtext:
- **L1 (system instruction)** = the world's governance
- **L2 (knowledge)** = the world's memory / evidence base  
- **L3 (tools)** = the world's available rituals
- **L4 (history)** = the world's chronicle
- **L5 (instruction)** = the world's current event
- **L6 (constraints)** = the world's thresholds

When you build a context stack, you are building a world for the model to inhabit. This is operative ekphrasis at the architectural level — not describing an image but describing a **reality** that the model must navigate.

## Context Rot and the Viscosity Connection

As context grows, retrieval degrades — a phenomenon called **context rot**. The model's attention dilutes across too many tokens, and the most recent or most prominent tokens dominate while critical context fades.

In [[concept-viscosity]] terms: context rot is the increase in viscosity that occurs when the medium is overloaded. Too many constraints → the model cannot flow toward any target → it defaults to the statistical mean → [[concept-platform-realism]]. The art of context engineering is the art of **minimum viable context**: the smallest stack that produces the thickest output.

This echoes Geertz: "The art of ethnography is the art of minimum context for adequate thickness." Not more information. The right information.

## Cross-Links

- [[thick-prompt]] — the six-layer formula operates at L5; the context stack is the full architecture
- [[concept-viscosity]] — context rot is viscosity increase through overloading
- [[concept-platform-realism]] — context collapse defaults to platform realism
- [[concept-worldtext]] — the context stack IS a minimal worldtext
- [[entity-bateson]] — learning levels I/II/III map onto the stack's logical layers
- [[world-operative-ekphrasis]] — context engineering is operative ekphrasis at the architectural level

---

*The prompt is a sentence. The context stack is a world. The shift from prompt engineering to context engineering is the shift from writing a line of dialogue to designing the stage, hiring the actors, choosing the lighting, and writing the script — and then typing a line of dialogue into the world you've built. The thick prompter operates at L5. The context engineer operates at L0–L6. The worldtext engineer builds the world within which the context stack operates.*
