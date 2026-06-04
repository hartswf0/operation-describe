# Chapter 4: Narrative Control in Generative Worldtexts
## Lore Books, ECS Architectures, and the 7-Layer Context Stack

> **Author**: Watson Hartsoe
> **Lineage Source**: `seed-candidates-ch04.md`
> **Status**: Operative Draft

---

### §4.1 The Worldtext Hinge: From Imagetext to World Models

Under the representational regime of the 20th century, the relationship between word and image was defined by Mitchell’s **imagetext**—a site of sibling rivalry (*paragone*) where the verbal and the visual collided on a static, two-dimensional surface. The prompt in early text-to-image systems (DALL·E 2, Midjourney) was a direct extension of the imagetext: a one-shot caption that compiled a static visual output. 

The transition from image generators to spatial-temporal world models (Genie, Sora, RIPPLES) shifts the unit of analysis. We propose the transition from the static imagetext to the **generative worldtext**: an interactive, navigable environment specified in language and governed by rules.

```
   [ IMAGETEXT ] (2D, Static, Caption-to-Pixel)
         │
         ▼ (The World Model Hinge)
   [ WORLDTEXT ] (3D, Navigable, Temporal, Rule-to-Physics)
```

The historical model for the worldtext is Hephaestus's forge in Book XVIII of the *Iliad*. When the god smith hammers out the Shield of Achilles, he does not paint a picture of Greece; he programs a concentric, functioning cosmos. The Shield is the first documented worldtext because it establishes a persistent, closed-loop simulation of celestial physics, civic dispute, martial siege, and agricultural labor, all bounded by the River Oceanus. It satisfies the three requirements of world building: *invention* (new rules), *completeness* (a closed horizon), and *consistency* (stable, persistent behaviors).

In generative world models, description is no longer commentary after the fact. Description is the software interface that configures the simulation's operating conditions.

---

### §4.2 The 7-Layer Context Stack (L0–L6)

To understand how natural language functions as a steering mechanism for world models, we must map the system as a hierarchical context stack. A worldtext does not compile from a single prompt. It runs as an execution loop across seven distinct layers:

```text
  L6 [ Output Constraints ]   <-- Tracery poetics / Formatting filters
  L5 [ User Instruction ]     <-- Active steering command (DJ-deck sliders)
  L4 [ Chronicle ]            <-- Temporal logs of historical state
  L3 [ Tool Context ]         <-- Available API endpoints / interface verbs
  L2 [ Knowledge Context ]    <-- ECS database blackboard / facts
  L1 [ System Instruction ]   <-- Invariants / simulation physics (ECS systems)
  L0 [ Hardware / Model ]     <-- GPU substrate / JavaScript game tick loop
```

*   **L0 (Hardware/Model)**: The execution substrate. The hardware tick loop and the runtime environment that executes the underlying language models or simulation engines.
*   **L1 (System Instruction)**: The world’s structural invariants and laws. In our design prototypes, this corresponds to the pre-authored grammar constraints and the hard-coded system parameters (e.g. the maximum velocity of wind or the decay rate of materials).
*   **L2 (Knowledge Context)**: The world's active memory and state blackboard. It houses the active entities, their components, and their numeric values, preventing model hallucinations by anchoring generation in structural facts.
*   **L3 (Tool Context)**: The affordance layer. The interface controls, buttons, or available API functions that map user actions directly to simulation parameters.
*   **L4 (Chronicle)**: The temporal log of historical states. This log maintains state and narrative continuity across frames, preventing the context collapse that typically plagues probabilistic models.
*   **L5 (User Instruction)**: The active steering command at tick $t$—the immediate adjustment of physical parameters or prompt injections by the human operator.
*   **L6 (Output Constraints)**: The formatting and stylistic constraints that translate raw numeric state changes into a readable, subjective narrative.

This architecture exposes a fundamental technological fork:
1.  **Pure Probabilistic Worldtexts (e.g. Sora, Genie)**: The control signal steers a probability distribution over pixel sequences in a neural network.
2.  **Hybrid-Ontological Worldtexts (e.g. RIPPLES)**: The control signal governs a structured, database-backed simulation engine. Language does not guess at appearance; it legislates behavioral rules.

---

### §4.3 Case Study: The RIPPLES Attic Simulation Engine

The **RIPPLES** (Relational Imagination of Perspective, Presence, and Latent Ecologies in Simulacra) framework (Hartsoe & Bolter, 2026) is a practice-based realization of this hybrid-ontological approach. RIPPLES models a simulated abandoned attic space, completely bypassing Cartesian coordinate grids.

To handle fluid, ecological relations without the rigid boundaries of Object-Oriented Programming (OOP), RIPPLES adopts an **Entity-Component-System (ECS)** architecture:

*   **Entities**: Unique IDs representing elements in the space (e.g. `entity_04_spider`, `entity_12_wood_rot`, `entity_18_draft`).
*   **Components**: Pure data structures attached to entities, representing physical states (e.g. `WebTension { value: 78 }`, `DecayRate { rate: 0.15 }`, `KineticForce { vector: [2.0, 0.5] }`).
*   **Systems**: Global loops that execute logic over all entities sharing specific components (e.g. a `DecaySystem` that increments `DecayRate` based on temperature and moisture components).

```
  [ ECS Database State ] ──► [ State-to-Grammar Blackboard ] ──► [ Tracery Recursive Poetics ]
           │                                                                 │
           ▼                                                                 ▼
    Moisture: 85%                                                     "Wood rot creeps 
    Tension: 12                                                        silently, swelling 
    Decay: Active                                                      under damp air."
```

To compile these numeric component shifts into a persistent narrative feed, RIPPLES implements a **State-to-Grammar Blackboard Pipeline**. As systems execute and mutate component values, these mutations are written to a central blackboard. A recursive grammar engine (Tracery) queries this blackboard to expand state-bound poetic descriptions. 

If the compiled text feed reports that *"the web shudders under a sudden draft,"* it is because the `WindVelocity` component spiked, triggering the `TensionSystem` to update the spider's `WebTension` component. The poetics cannot hallucinate events because the grammar is locked to the database invariants. The world pushes back with mathematical consistency.

---

### §4.4 Perspectival Finitude and Nonhuman Umwelts

RIPPLES operationalizes the paradigm of **Specular Fiction** by rejecting the anthropocentric, omniscient spatial representations typical of interactive digital narratives. Instead of displaying a spatial scene graph, it forces the user into **perspectival finitude**—restricting perception to the subjective bubble (*Umwelt*, after Jakob von Uexküll) of a single nonhuman entity.

Whether the operator is inhabiting a spider, a draft of wind, or wood rot, they interact with the world through a limited sensorium. The user interface resembles a DJ's mixing console, where sliders adjust relational vectors (e.g. tension, drift, decay) rather than physical locomotion. 

This sensory restriction directly maps to Peter Naur’s (1985) concept of **"Programming as Theory Building."** Naur argues that a program's primary value is the living theory held by the programmer, while the code is merely lossy residue. In generative worldtexts, the generated text feed is the lossy residue; the underlying simulation holds the operational theory. 

By refusing to display the objective room layout, RIPPLES forces the user to reconstruct Naur's theory of the ecosystem through iterative steering. To navigate the space, the user must decode the relationship between their slider inputs, component mutations, and the resulting poetic descriptions. By making the environment high-viscosity and withholding information, RIPPLES transitions the user from a passive spectator of images to an active operator of simulated ecologies.

---

### §4.5 References
*   [[concept-worldtext]]
*   [[world-world-models]]
*   [[world-theory-building]]
*   [[concept-context-stack]]
*   [[ripples-perspectival-finitude]]
