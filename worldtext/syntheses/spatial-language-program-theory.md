# Spatial Language Program Theory: The 24 Programs

> **Species**: synthesis  
> **Scale**: foundational  
> **Parent System**: [[system-worldtext-operations]]  
> **Date**: 2026-04-28  
> **Status**: Canonical reference — originated as operative design document, formalized here.

---

## Core Claim

A system becomes powerful when its ideas can be placed, referenced, inspected, repaired, and regenerated.

**Spatial language** is the program that turns thought into architecture.

It does not treat language as floating description. It treats language as **placed structure**.

```
<intent>
  [becomes] <spatial inscription>

<spatial inscription>
  [occupies] <coordinate>

<coordinate>
  [creates] <relation>

<relation>
  [forms] <syntax>

<syntax>
  [becomes] <parseable structure>

<parseable structure>
  [supports] <reference>

<reference>
  [enables] <recursion>

<recursion>
  [builds] <world>

<world>
  [requires] <canonical source>

<canonical source>
  [generates] <many views>

<many views>
  [reveal] <hidden infrastructure>

<hidden infrastructure>
  [enables] <repair>

<repair>
  [requires] <ownership, provenance, and accountability>
```

---

## The 24 Programs

Each program has: **Purpose**, **Core Operation**, **Refusal** (what it won't accept), **Invariant** (what must hold), and **Failure** (what happens when it breaks).

---

### 1. Inscription Program

**Purpose**: Turn vague thought into a mark that can be seen, moved, named, changed, and traced.

**Operation**:
```
<intent> [externalizes as] <inscription>
<inscription> [occupies] <surface>
<surface> [makes] <thought manipulable>
```

**Examples**: A concept becomes a card. A brick becomes a line of text. A submodel becomes a named block. A pattern becomes a rule of action.

**Refusal**: Hidden intention. Abstract nouns with no operation. Prose that cannot be acted on.

**Invariant**: If it cannot be placed, pointed at, changed, or traced, it is not yet operational.

**Failure**: The system becomes essay fog: impressive language with no working structure.

---

### 2. Coordinate Program

**Purpose**: Give every meaningful object a place.

**Operation**:
```
<object> [receives] <coordinate>
<coordinate> [anchors] <object>
<anchored object> [can be compared with] <other anchored objects>
```

**Forms**: `<word> [has] <x, y>` / `<part> [has] <x, y, z>` / `<submodel> [has] <local origin>` / `<token> [has] <grid position>`

**Refusal**: Floating text. Unlocated concepts. Unsituated claims. Meaning without position.

**Invariant**: Position is not decoration. Position is a semantic operator.

**Failure**: If placement has no consequence, the grid is wallpaper.

---

### 3. Spatial Syntax Program

**Purpose**: Make arrangement carry meaning.

**Operation**:
```
<placement> [encodes] <relation>
<relation> [can be parsed]
<parsed relation> [can guide] <action>
```

**Spatial operators**:

| Operator | Meaning |
|----------|---------|
| `<above>` | priority / authority / origin |
| `<below>` | dependency / consequence / implementation |
| `<left>` | before / source / input |
| `<right>` | after / output / consequence |
| `<inside>` | scope / containment / belonging |
| `<outside>` | exclusion / exception / boundary |
| `<near>` | association / affinity |
| `<far>` | difference / separation |
| `<center>` | hub / attractor / dominant concern |
| `<edge>` | limit / risk / transition |
| `<path>` | sequence / trail / procedure |
| `<cluster>` | emergent category |
| `<empty space>` | absence / unresolved relation / negative evidence |

**Refusal**: Layout as decoration. Lists as the default ontology. Visual design with no semantic force.

**Invariant**: If two things move closer together, their relation has changed.

**Failure**: If spatial change does not change interpretation, the spatial language is fake.

---

### 4. Reference Program

**Purpose**: Replace duplication with callable structure.

**Operation**:
```
<object> [does not contain] <all of itself>
<object> [references] <another object>
<reference> [preserves] <reuse, scale, and coherence>
```

**LDraw form**: `<part> [references] <primitive>` / `<model> [references] <part>` / `<library> [stores] <shared vocabulary>`

**Context form**: `<current task> [references] <purpose, constraints, examples, failure modes, output contract>`

**Refusal**: Copy-paste ontology. Hardcoded repetition. Context dumps.

**Invariant**: Durable systems do not repeat structure. They reference it.

**Failure**: If every object contains its own full copy of meaning, the system bloats, drifts, and becomes unrepairable.

---

### 5. Recursion Program

**Purpose**: Build large worlds from nested callable units.

**Operation**:
```
<whole> [contains] <part>
<part> [contains] <subpart>
<subpart> [contains] <primitive>
<primitive> [supports] <whole>
```

**LDraw/MPD form**: `<main model> [references] <submodel> [references] <part> [references] <primitive>`

**Refusal**: Flat files. Monolithic objects. Final surfaces with no internal grammar.

**Invariant**: A world becomes editable when it is recursively composed.

**Failure**: If the internal levels disappear, the world becomes a dead surface.

---

### 6. Local Dictionary Program

**Purpose**: Let a document define its own vocabulary.

**Operation**:
```
<document> [contains] <named internal units>
<named internal unit> [becomes] <callable word>
<entry point> [assembles] <local vocabulary into world>
```

**MPD form**: `0 FILE main.ldr` / `0 FILE tower.ldr` / `0 FILE gate.ldr`

**Context form**: `0 FILE purpose` / `0 FILE constraints` / `0 FILE examples` / `0 FILE current_task`

**Refusal**: One flat transcript. Undifferentiated prompt sludge. Memory as scrollback.

**Invariant**: A good context behaves like an MPD: many named blocks, one active entry point.

**Failure**: If the document has no scoped internal vocabulary, the system cannot reason over its own parts.

---

### 7. Canonical Artifact Program

**Purpose**: Keep one recoverable source of truth.

**Operation**:
```
<canonical artifact> [generates] <views>
<view> [must be regenerable from] <canonical artifact>
<non-regenerable state> [must become] <explicit saved artifact>
```

**Rule**: If it cannot be regenerated from the source, it is not derived state. It is user-facing state. Save it. Name it. Version it. Make it diffable.

**Refusal**: Silent derived state. Hidden memory. Untracked transformation.

**Invariant**: One truth, many views. Many views, no competing truths.

**Failure**: If a render, skeleton, or output becomes more authoritative than the source, the system has split its reality.

---

### 8. Ownership Graph Program

**Purpose**: Make belonging explicit.

**Operation**:
```
<part> [owns] <stud>
<submodel> [contains] <part>
<artifact> [belongs to] <trail>
<decision> [belongs to] <creator>
<output> [belongs to] <context>
```

**Refusal**: Orphan elements. Null references. Anonymous claims. Detached outputs.

**Invariant**: Nothing important should float ownerless. Ownership is not bureaucracy. Ownership is repairability.

**Failure**: Orphan state creates hallucination, mis-selection, broken edits, and fake authority.

---

### 9. Parse-Don't-Validate Program

**Purpose**: Convert raw material into typed structure before acting on it.

**Operation**:
```
<raw input> [parses into] <typed structure>
<typed structure> [enables] <safe operation>
<parse failure> [blocks] <unsafe transition>
```

**Weak form**: `<validator> [says] "bad"`

**Strong form**: `<parser> [shows] <where, why, and what structure failed>`

**Refusal**: Boolean validation theater. Vague warnings. Accepting broken structure and hoping downstream tools survive.

**Invariant**: The system must know what kind of thing it is handling before it acts.

**Failure**: If illegal state remains representable as normal state, the tool will eventually treat it as real.

---

### 10. Professional Vision Program

**Purpose**: Teach the user what to see.

**Operation**:
```
<raw field> [is marked by] <coding scheme>
<coding scheme> [highlights] <meaningful difference>
<highlighted difference> [enables] <judgment>
```

**Examples**: `<stain in dirt> [becomes] <post mold>` / `<line of text> [becomes] <part reference>` / `<nearby cards> [become] <cluster>` / `<empty cell> [becomes] <negative space>`

**Refusal**: "Just show the data." Neutral seeing. Explanation without training attention.

**Invariant**: The tool must not merely display objects. It must train the user to see operational differences.

**Failure**: If the highlighting is wrong, the tool teaches false perception.

---

### 11. Breakdown-Visibility Program

**Purpose**: Turn failure into evidence.

**Operation**:
```
<transparent tool use> [breaks]
<breakdown> [reveals] <hidden infrastructure>
<visible infrastructure> [enables] <repair>
```

**Examples**: `<selection fails> [reveals] <missing ownership graph>` / `<bad answer> [reveals] <bad context structure>` / `<hallucination> [reveals] <missing grounding>` / `<contradiction> [reveals] <competing source blocks>`

**Refusal**: Silent failure. Fake success. Smoothing over breakdown. Hiding seams until collapse.

**Invariant**: A serious system explains failure in the same language it uses to work.

**Failure**: If repair requires superstition, the system is not inspectable.

---

### 12. Provenance Program

**Purpose**: Keep action tied to actor, time, reason, and consequence.

**Operation**:
```
<actor> [performs] <action>
<action> [changes] <artifact>
<change> [leaves] <trace>
<trace> [supports] <accountability>
```

**Examples**: `<author header> [binds] <file> to <creator>` / `<edit> [binds] <line change> to <session>` / `<claim> [binds] <source>`

**Refusal**: Anonymous transformation. Contextless output. Erased scars. Final-state fetish.

**Invariant**: Every meaningful change must leave a trace.

**Failure**: Without provenance, responsibility dissolves into interface polish.

---

### 13. Gothic Assemblage Program

**Purpose**: Let large structures emerge from local standards, reusable templates, and situated craft.

**Operation**:
```
<local actor> [uses] <template>
<template> [coordinates] <partial knowledge>
<partial knowledge> [assembles into] <larger structure>
```

**Refusal**: Master-plan fantasy. One architect knows all. Centralized theory before action.

**Invariant**: The system grows because local units obey enough shared grammar.

**Failure**: Without local standards, assemblage becomes junk pile. With too much central law, assemblage becomes bureaucracy.

---

### 14. Spatial Hypertext Program

**Purpose**: Let users express uncertain structure before formalizing it.

**Operation**:
```
<user> [places] <items>
<placement> [suggests] <implicit relation>
<implicit relation> [may become] <formal link>
<formal link> [may become] <typed morphism>
```

**Pipeline**: `<loose placement> → <cluster> → <candidate pattern> → <named relation> → <morphism> → <program rule>`

**Refusal**: Premature taxonomy. Requiring links before insight. Treating ambiguity as error.

**Invariant**: A good knowledge tool lets structure emerge before it demands structure.

**Failure**: If the tool requires final categories too early, it kills discovery.

---

### 15. Image-Schema Program

**Purpose**: Use bodily spatial primitives to organize abstract thought.

**Operation**:
```
<body schema> [maps onto] <conceptual relation>
<conceptual relation> [becomes] <spatial operation>
```

**Schemas**: CONTAINER (inside/outside/boundary) / SOURCE-PATH-GOAL (origin/route/destination) / UP-DOWN (authority/dependence) / CENTER-PERIPHERY (importance/marginality) / LINK (association/dependency) / BLOCKAGE (constraint/failure/ethical limit)

**Refusal**: Abstract relations with no bodily handle. Symbolic systems detached from movement.

**Invariant**: Users understand abstract relations faster when those relations borrow from embodied spatial experience.

**Failure**: If the spatial metaphor contradicts bodily expectation, the interface becomes expensive to think with.

---

### 16. Context-as-MPD Program

**Purpose**: Treat AI context as structured scene grammar, not transcript dump.

**Operation**:
```
<context> [is divided into] <named blocks>
<named blocks> [become] <callable semantic units>
<current task> [references] <needed blocks>
<irrelevant blocks> [stay outside] <active frame>
```

**MPD analogy**: `0 FILE purpose` / `0 FILE constraints` / `0 FILE examples` / `0 FILE failure_modes` / `0 FILE output_contract` / `0 FILE current_task`

**Refusal**: Giant prompt blob. Chat history as architecture. Context accumulation as intelligence.

**Invariant**: The context window is scarce space. It must be arranged like a scene.

**Failure**: If everything is included, nothing is foregrounded. If nothing is named, nothing is callable.

---

### 17. Token-as-Stud Program

**Purpose**: Treat small units as reusable attachment points.

**Operation**:
```
<small unit> [supports] <connection>
<connection> [enables] <larger structure>
<larger structure> [remains editable because] <small units stay regular>
```

**Refusal**: Amorphous blocks. Unstable primitives. Attachment without law.

**Invariant**: Small repeated attachment structures make large recombination possible.

**Failure**: If the basic unit is unstable, every higher structure becomes fragile.

---

### 18. Olog Program

**Purpose**: Turn a domain into typed objects and structure-preserving arrows.

**Operation**:
```
<object> [is typed as] <entity>
<relation> [is typed as] <morphism>
<morphism> [preserves] <structure>
<structure> [supports] <translation across domains>
```

**Mapping law**: A real analogy preserves operations, not mood.

**Refusal**: Loose metaphor. Theory by resemblance. Branding as ontology.

**Invariant**: If the relation does not preserve function, it is not a morphism.

**Failure**: Fake morphisms create aesthetic theory with no operational grip.

---

### 19. Library-Governance Program

**Purpose**: Let shared vocabulary survive across many authors.

**Operation**:
```
<new unit> [is proposed]
<community> [reviews] <new unit>
<standard> [accepts or rejects] <new unit>
<accepted unit> [joins] <shared vocabulary>
```

**Refusal**: Anything-goes vocabulary. Private language pretending to be public standard. Unreviewed primitives.

**Invariant**: A shared language requires governance.

**Failure**: Without governance, vocabulary rots. With too much governance, vocabulary freezes.

---

### 20. Worlding Program

**Purpose**: Create a bounded system where action has consequence.

**Operation**:
```
<law> [bounds] <possibility>
<bounded possibility> [becomes] <world>
<actor> [acts inside] <world>
<action> [changes] <world state>
```

**Refusal**: Infinite possibility without consequence. Aesthetic "world" with no laws. Sandbox without memory.

**Invariant**: A world is not a theme. A world is a governed space of possible action.

**Failure**: If actions do not alter state, the world is scenery.

---

### 21. Repairable World Program

**Purpose**: Create systems that can be inspected, repaired, and regenerated after failure.

**Operation**:
```
<world> [is generated from] <canonical source>
<source> [contains] <grammar>
<grammar> [generates] <state>
<state> [can be inspected through] <views>
<views> [reveal] <fault>
<fault> [is repaired at] <source or derived layer>
<repaired source> [regenerates] <world>
```

**Repair ladder**: 1. See the failure. 2. Locate the object. 3. Locate the owner. 4. Locate the source. 5. Locate the violated rule. 6. Change the smallest responsible unit. 7. Regenerate the view. 8. Confirm the postcondition. 9. Leave a trace.

**Refusal**: Dead exports. Opaque render-only worlds. Flattened screenshots.

**Invariant**: A world worth building must be rebuildable.

**Failure**: If the only surviving object is the rendered surface, the world has already died.

---

### 22. Action-Guard Program

**Purpose**: Prevent high-stakes transitions from happening without accountable consent.

**Operation**:
```
<proposed action> [is classified by] <risk>
<risk> [requires] <approval>
<approval> [binds] <human actor> to <consequence>
```

**Refusal**: Automation without consent. Responsibility laundering. Hidden irreversible transitions.

**Invariant**: The more irreversible the action, the more visible the human cut must be.

**Failure**: If high-stakes action happens silently, agency has been stolen.

---

### 23. Memory-Palace Program

**Purpose**: Use place as an indexing engine.

**Operation**:
```
<idea> [is placed in] <locus>
<locus> [anchors] <recall>
<route through loci> [becomes] <memory trail>
```

**Refusal**: Flat lists as default memory. Chronological scroll as only access path.

**Invariant**: Memory improves when ideas have places.

**Failure**: If every item appears in the same undifferentiated list, the system discards spatial intelligence.

---

### 24. Captured Grammar Program

**Purpose**: Turn repeated activity into a formalizable grammar.

**Operation**:
```
<practice> [produces] <repeated moves>
<repeated moves> [become] <grammar>
<grammar> [captures] <future action>
```

**LDraw**: `<building practice> → <part grammar> → <file format> → <captures LEGO assembly>`

**AI**: `<prompting practice> → <context grammar> → <structured prompt system> → <captures model behavior>`

**Refusal**: Improvisation with no memory. Practice with no trace. Prompts as disposable speech.

**Invariant**: A system matures when repeated successful action becomes reusable grammar.

**Failure**: If grammar hardens too early, it kills practice. If grammar never forms, practice cannot scale.

---

## Final Synthesis

The deep program can be written as one chain:

```
<intent> [externalizes into] <spatial inscription>
<spatial inscription> [occupies] <coordinate>
<coordinate> [creates] <semantic relation>
<semantic relation> [forms] <spatial syntax>
<spatial syntax> [becomes] <parseable structure>
<parseable structure> [supports] <reference>
<reference> [enables] <recursion>
<recursion> [enables] <world assembly>
<world assembly> [requires] <canonical artifact>
<canonical artifact> [generates] <views>
<views> [teach] <professional vision>
<professional vision> [reveals] <hidden infrastructure>
<hidden infrastructure> [requires] <seamful exposure>
<seamful exposure> [enables] <repair>
<repair> [requires] <ownership and provenance>
<ownership and provenance> [enable] <accountability>
<accountability> [allows] <governed shared language>
<governed shared language> [allows] <creative civilization>
```

**Final law**:

Do not merely write the system. **Place** it.  
Do not merely describe the object. **Reference** it.  
Do not merely store the output. **Preserve the trail**.  
Do not merely render the world. **Keep the language that can regenerate it.**

---

## Cross-References

- [[syntheses/spatial-language-worldtext-synthesis]] — The morphism table mapping these 24 programs to LDraw and Worldtext
- [[syntheses/hello-worldtext]] — Chapter 01: the circuit test demonstrating programs 7, 9, 11, 12, 20, 21 in action
- [[concept-worldtext]] — The foundational concept
- [[concept-spatial-operator]] — Spatial operators as semantic functions
- [[concept-text-as-control-signal]] — Text as executable constraint
- [[world-theory-building]] — Naur's theory of programming as theory building
