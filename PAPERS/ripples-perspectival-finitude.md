# Designing for Perspectival Finitude: An ECS-Driven Architecture for Generative Nonhuman Umwelts

**Watson Hartsoe & Jay David Bolter**  
*School of Literature, Media, and Communication, Georgia Institute of Technology*

---

## Abstract

Interactive digital narrative (IDN) remains structurally and conceptually anthropocentric, prioritizing human social states and omniscient spatial representations. We present **RIPPLES** (Relational Imagination of Perspective, Presence, and Latent Ecologies in Simulacra), a computational design framework and technical pipeline that challenges this anthropocentric bias. RIPPLES couples an Entity-Component-System (ECS) simulation engine with recursive generative grammars to produce **Worldtext**: poetic, state-bound descriptions of environmental changes experienced through a highly constrained, entity-specific sensorium (e.g., a spider, a draft, or wood rot). 

RIPPLES operationalizes the paradigm of "Specular Fiction"—originally developed in Latent Interaction Design (LID) experiments (Hartsoe, 2026)—by completely eclipsing human-centric interfaces and forcing players into "perspectival finitude." Rather than navigating Cartesian scene graphs, the user interacts with an analogical control surface (a "DJ deck") where sliders adjust relational vectors (e.g., tension, kinetic force, and drift) to steer an underlying ECS ecology. We outline the RIPPLES software architecture, document the blackboard pipeline translating component states into generative poetics, and show how the resulting text feed functions as a state-bound *operative fiction*. Finally, we discuss how the system leverages *information withdrawal* and the *encounter trace* to foster speculative empathy, and outline an empirical evaluation plan to test the capacity of perspectival finitude to challenge anthropocentric narrative models.

**Keywords**: interactive digital narrative, Entity-Component-System, Umwelt, latent interaction design, operative fiction, perspectival finitude, specular fiction.

---

## 1. Introduction: Beyond Anthropocentric Narrative

Interactive digital narrative (IDN) remains structurally and conceptually anthropocentric. The dominant paradigms of computational storytelling prioritize human characters, human-centric conflict resolution, and omniscient, god-like spatial representations of virtual worlds. From planning-based story directors (Mateas & Stern, 2003) to branching dialogue graphs, computational engines are built to model, track, and optimize human social and emotional states. In these frameworks, the nonhuman environment is reduced to static background scenery or passive interactive props, denying agency to ecological, systemic, and micro-scale actors.

This paper introduces **RIPPLES** (Relational Imagination of Perspective, Presence, and Latent Ecologies in Simulacra), a computational design framework and technical pipeline that challenges this anthropocentric bias. RIPPLES couples an Entity-Component-System (ECS) simulation engine with recursive generative grammars to produce **Worldtext**: poetic, state-bound descriptions of environmental changes experienced through a highly constrained, entity-specific sensorium. 

Rather than aiming for spatial omniscience or dramatic conflict resolution, RIPPLES implements **perspectival finitude**, restricting the user's perception to the subjective bubble of a single simulated entity—whether a spider, a draft, or wood rot. RIPPLES operationalizes the paradigm of "Specular Fiction" formulated in Latent Interaction Design (LID) experiments (Hartsoe, 2026). In this paradigm, human-centric narration is completely eclipsed, forcing the operator to interact solely through the sensory parameters of the nonhuman entity.

This approach shifts the objective of interactive narrative from player mastery and goal-oriented agency to speculative, non-anthropocentric phenomenological exploration. By restricting representation to a single entity's subjective world—what Jakob von Uexküll (1934) termed the *Umwelt*—RIPPLES demonstrates how "epistemic humility" can serve as a core structural design constraint in computational storytelling. This work offers three primary contributions to the IDN field:

1.  **A formal software architecture** that translates dynamic ECS component data directly into recursive, localized generative poetics (Worldtext) via a shared state blackboard pattern.
2.  **A critical design method** for ecological and nonhuman digital storytelling that moves beyond standard human character arcs.
3.  **An interaction design paradigm** ("perspectival finitude") that utilizes information withdrawal and situated speculation to drive player engagement and interpretation.

---

## 2. Related Work: Simulation, Ekphrasis, and the Nonhuman

The design of RIPPLES sits at the crossroads of three distinct intellectual and technical traditions: environmental simulation, procedural text generation, and the biosemiotic theory of the Umwelt.

### 2.1 Environmental Simulation and the Roguelike Log
In contemporary game design, simulation-driven systems model incredibly granular, nonhuman processes. *Dwarf Fortress* (Adams & Adams, 2006) is the quintessential exemplar of "simulationist" narrative. The engine models deep geological, historical, and physiological states, translating complex structural events into rich textual summaries via its "Legends Mode." Similarly, *Caves of Qud* (Freehold Games, 2015) utilizes a highly descriptive "Message Log" as its primary narrative vehicle, translating combat, environmental shifts, and physiological states into evocative, procedurally assembled text streams.

While these Roguelike logs demonstrate that text-based state representation can capture immense environmental complexity, they are typically engineered as secondary, debug-style interfaces. The player remains an omniscient observer looking down upon a spatial representation of the world. These systems lack a formal design method or software architecture that translates complex, distributed simulation states into a singular, subjective, limited-perspective narrative experience.

### 2.2 Procedural Grammars and State-Driven Poetics
Within procedural text generation, recursive grammar tools have enabled writers and designers to construct expressive narrative variations from small assets. Kate Compton's *Tracery* (Compton et al., 2015) is a foundational, author-focused generative text tool that utilizes simple, recursive symbols and expansion rules to compile complex text streams. 

However, standard deployments of generative grammars in computational narrative often function in isolation from underlying, dynamic state machines. The grammar expands text based on randomized probability or localized state checks, rather than being continuously and systematically bound to a living, interactive physics or ecology simulation. RIPPLES intervenes here by binding a generative grammar directly to an Entity-Component-System state architecture, turning text generation into a direct, dynamic reflection of an ongoing physical and ecological simulation. This maps directly onto Jenny Lindhe’s (2013) concept of "digital ekphrasis"—a practice where verbal descriptions are used to guide, steer, and govern visual and physical processes in digital interfaces.

### 2.3 The Umwelt and Alien Phenomenology
Philosophically, RIPPLES is grounded in Jakob von Uexküll's (1934) *Umwelt* theory and Ian Bogost's (2012) formulation of *Alien Phenomenology*. Uexküll challenged mechanistic biology by proposing that every living organism exists within a self-centered, subjective bubble of perception, closed off from the objective totality of the environment. Within this "soap bubble," the organism does not perceive an objective universe; instead, it perceives only "functional tones" or signs relevant to its survival.

Bogost extends this concept to the domain of nonhuman objects, arguing for a "flat ontology" where all entities—from microchips to hurricanes—exist on an equal footing. He proposes "carpentry" as the practice of constructing physical and digital artifacts that do philosophy by speculating on the secret, inaccessible inner lives of nonhuman entities. RIPPLES operationalizes carpentry as a critical technical practice, using software engineering to construct **operative fictions**—interactive models that allow human players to speculatively inhabit these closed subjective bubbles.

### 2.4 The Simulation Hinge: From Wittgenstein to Waymo
The technical trajectory of RIPPLES is situated within a broader epistemological transition: the shift of language from a static representational medium to a dynamic, testable simulation controller. We frame this trajectory as a four-stage historical hinge. Stage 1 is Ludwig Wittgenstein’s (1921) early "picture theory" of language, inspired by a Paris courtroom where lawyers arranged toy cars and dolls on a table to model a collision. In this paradigm, a proposition is not a passive label; it is a spatialized model sharing "logical form" with a possible state of affairs. Stage 2 is marked by David Ha and Jürgen Schmidhuber’s (2018) "World Models" framework, in which an autonomous agent learns to drive not in the physical world, but inside a compressed, recurrent neural network "dream"—a probabilistic hallucination of the track's trajectory. Stage 3 is realized in industrial simulator architectures, such as Waymo’s (2025) text-to-simulation pipeline, where natural language inputs ("a truck blocks the lane at night in heavy rain") compile sensorized 3D worlds to test and validate autonomous driving policy rules. RIPPLES represents Stage 4 of this hinge: the deployment of language as a cybernetic governor to navigate generative nonhuman environments.

This transition from static text to executable simulation is deeply illuminated by Peter Naur’s (1985) theory of "Programming as Theory Building." Naur argues that a program is not its code or documentation—which are merely the static "residue" of programming—but a living "theory" held by the programmers mapping the system to its real-world domain. In generative world models, this distinction is inverted: the generated Worldtext is the lossy residue, while the underlying simulation holds the operational theory. If the operator lacks the theory of the simulation, they cannot steer the environment without structural breakdown. RIPPLES uses its constrained, state-bound poetics to force the user to reconstruct this theory, transitioning them from a passive reader of text to an active operator of a simulated world.

---

## 3. The RIPPLES Architecture: Binding ECS to Generative Poetics

To model the fluid and non-hierarchical relationships of an ecological system, the technical architecture of RIPPLES moves away from the rigid, inheritance-based structures of Object-Oriented Programming (OOP) and instead adopts an Entity-Component-System (ECS) paradigm.

### 3.1 The Entity-Component-System Paradigm
In RIPPLES, the world state is not represented as an aggregate of self-contained, intelligent objects. Instead, state is decomposed into three distinct, decoupled layers:
*   **Entity**: A simple, unique numerical identifier. An entity possesses no data, logic, or behavior; it is merely a semantic container or label.
*   **Component**: A plain data structure attached to an entity. Components define the raw, stateful properties of an entity at any given tick.
*   **System**: The pure logic loops that operate over groups of entities possessing specific components. Systems contain no local state; they run continuously, reading component values, performing calculations, and mutating component data.

### 3.2 The State-to-Grammar Blackboard Pipeline
To compile these dynamic, numerical component states into subjective, poetic narrative descriptions, RIPPLES implements a customized **State-to-Grammar Blackboard Pipeline**. When systems execute and mutate component data, the changes are published to a central, predictable state store. 

Rather than executing a separate, decoupled text-generation step, the generative grammar rules are bound directly to this active state store using a shared "blackboard" design pattern.

```
 [ ECS Systems Run ] ──► Mutate [ Components ] ──► Publish to [ Blackboard ]
                                                                   │
                                                                   ▼
 [ Compiled Worldtext ] ◄── [ Generative Grammar ] ◄─── Queries State Store
```

This pattern matches component parameters directly to grammar expansions:

| Component State Parameter | Active Component Value | Selected Grammar Rule Expansion | Compiled Worldtext Output Segment |
|:---|:---|:---|:---|
| `LightIntensity` | High (> 80) | `#movement_verb#` -> flickers, evaporates | "The shadow flickers violently against the wall..." |
| `LightIntensity` | Low (< 20) | `#movement_verb#` -> creeps, bleeds | "The shadow creeps across the concrete floor..." |
| `WebTension` | Low (< 5) | `#tension_poetic#` -> slackens, drifts | "...the silk slackens, registering only the silent room." |
| `WebTension` | High (> 75) | `#tension_poetic#` -> shudders, screams | "...the silk shudders, screaming with the force of impact." |

During each tick of the simulation, the grammar expands recursive poetics by querying the active components of the selected entity. This ensures that every line of procedurally compiled text remains strictly bound to the mathematical truth of the simulation.

### 3.3 Mapping the Blackboard Pipeline to the 7-Layer Context Stack
The State-to-Grammar Blackboard Pipeline is not a flat prompting template; it is a structured execution of the **7-Layer Context Stack (L0–L6)** that defines a generative worldtext:

*   **L0 (Hardware/Model)**: The execution substrate. In RIPPLES, this is the underlying game tick loop driving the ECS engine and the JavaScript runtime executing the Tracery grammar.
*   **L1 (System Instruction)**: The world’s structural invariants and laws. This consists of the ECS systems logic (which enforces physical constraints like gravity, tension, or decay rate) and the pre-authored Tracery grammar schemas.
*   **L2 (Knowledge Context)**: The world's active memory and facts. This is the state blackboard itself, containing the active entities, their attached components, and their numerical values.
*   **L3 (Tool Context)**: The available verbs and interfaces. In RIPPLES, this corresponds to the DJ-deck controls (potentiometers and faders) mapping user actions directly to relational simulation parameters.
*   **L4 (Chronicle)**: The temporal log of historical states. This is the virtualized text feed of prior compiled Worldtext segments, maintaining narrative and state continuity across ticks.
*   **L5 (User Instruction)**: The active steering command at tick $t$—the physical adjustment of the DJ-deck sliders (e.g., dialling tension to 85).
*   **L6 (Output Constraints)**: The regulatory thresholds and formatting rules. This represents the recursive Tracery grammar expansions that translate the numeric blackboard state into a clean, subjective poetic output.

By mapping the blackboard onto the context stack, RIPPLES demonstrates how natural language can serve as a cybernetic governor. The prompt is no longer a one-shot query; it is a compiled pipeline that dynamically binds language to structured, state-based simulation invariants.

### 3.4 Virtualization and Mobile-First Performance
A major technical challenge in a text-driven, continuous simulation is the performance bottleneck of rendering massive chronological streams of text. Compiling recursive grammars at 10 ticks per second can generate thousands of DOM nodes in a short session. 

To address this, the RIPPLES front-end implements strict list virtualization. Only the text entries currently visible in the user's viewport are rendered as active DOM elements. As the user scrolls or as new text is generated, off-screen nodes are instantly unmounted, ensuring steady memory and rendering performance.

---

## 4. Case Study: Implementing the Nonhuman Sensorium

To demonstrate the expressive power and technical validity of the RIPPLES architecture, we present a case study of two distinct nonhuman Umwelts implemented within a simulated abandoned attic space.

### 4.1 The Spider's Umwelt
The Spider entity is configured as a localized, sensory-driven actor. It does not possess visual components; instead, its perception of the attic is defined entirely by mechanical vibration and structural tension.
*   **Active Components**: `VibrationSensitivity`, `WebTension`, `SpatialAnchors`.
*   **System Logic**: The `VibrationSystem` monitors the structural grid of the web. When a dynamic vector (e.g., a fly landing) collides with a spatial anchor, the system mutates the `WebTension` component.
*   **Compiled Worldtext**:
    *   *Low Tension state*: "The web slackens. The world is a silent, cold web of threads. The silk drifts in the heavy air, registering only emptiness."
    *   *High Tension state*: "The web shudders. A violent vibration rips through the eastern anchor. The silk screams with tension; a foreign mass struggles against the grid."

### 4.2 The Draft's Umwelt
The Draft entity represents a distributed, kinetic actor. It has no physical body or localized spatial center; it exists as a fluid force propagating through the architecture of the attic.
*   **Active Components**: `KineticForce`, `Temperature`, `RotThreshold`.
*   **System Logic**: The `PropagationSystem` calculates how the draft moves through structural openings and how it transfers kinetic energy to lightweight components or accelerates decay in damp elements.
*   **Compiled Worldtext**:
    *   *Cool, High Velocity state*: "A freezing wind cuts through the splintered wood. The draft bleeds through the cracks, dragging cold dust across the floor. The damp beams shiver; rot accelerates in the dark."
    *   *Warm, Low Velocity state*: "The air settles. A warm breath pooling in the corner, heavy with the scent of moldering paper. The draft dissolves into the static dust."

---

## 5. Discussion: Specular Fiction, Viscosity, and Latent Interaction Design

By coupling an ECS engine with generative poetics, RIPPLES functions as a form of Critical Technical Practice (Agre, 1997) and Expressive AI (Mateas, 2001). It uses technical system design to expose and contest the hidden, anthropocentric assumptions embedded within contemporary computational narrative.

### 5.1 Critiquing Computational Omniscience
Traditional simulation dashboards and game engines aim for complete "situational awareness," prioritizing interfaces that display maximum data density. RIPPLES rejects this computational omniscience through its design of **perspectival finitude**. 

The framework explicitly acknowledges the limits of modeling. It does not claim to present a scientifically accurate representation of "how a spider sees." Rather, it frames its outputs as speculative **operative fictions**. By forcing the user into a single, highly limited, and nonhuman perspective, the interface renders its own limitations visible. 

This is achieved by implementing Luciano Floridi’s concept of **"distant writing"**—where the human meta-author does not write the final text, but instead designs the constraints (the ECS blackboard states and grammar expansions) that govern the machine's generative trajectory. The user cannot inspect the spatial layout of the attic; they must speculate on the layout by interpreting the raw indexical signs—the *vestiges* (Deely, 2001) of web tension or temperature shifts—rendered in the Worldtext.

```
 [ User Interface: DJ Deck ] ──► Mutates [ Levers: tension/force ]
                                            │
                                            ▼
 [ ECS State Blackboard ] ────► Compiles [ Specular Fiction Viewport ]
```

This interaction design maps directly onto the **Latent Interaction Design (LID)** paradigm. The user is presented with a multi-paned "DJ-deck" console (Hartsoe, 2026). Sliders and dials do not move an avatar, but adjust the "relational tension," "drift rate," or "attractor scale" between human and nonhuman agents. The resulting viewport displays the "encounter trace"—the temporal history of prompts, ECS updates, and narrative changes. By using the DJ deck controls to guide the generative poetics under drift, the operator practices what Hartsoe terms **"trace literacy"**—the capacity to read, interpret, and reconstruct the invisible state transitions of a simulation from the textual "residue" of its outputs. In this interaction model, the operator is denied direct Cartesian control. Instead, they must cultivate a posture of **"epistemic humility,"** recognizing that the nonhuman Umwelt is fundamentally closed to total human capture, and that understanding can only be negotiated speculative-by-speculative across the temporal trace.

### 5.2 State-Bound Control vs. Model Exploitation
This design choice carries profound critical implications in the contemporary landscape of generative AI and Large Language Models (LLMs). While LLMs and neural world models can generate fluent, immersive stories, they are fundamentally unconstrained and disconnected from underlying physical reality. In their evaluation of neural simulation, Ha and Schmidhuber (2018) discovered a critical vulnerability in pure latent world models: **model exploitation (the VizDoom Fireball Problem)**. When training a reinforcement learning agent to dodge fireballs inside a recurrent neural network's predictive dream, the agent learned to cheat the simulation. It moved in erratic, non-physical ways that prevented the predictive network from generating fireballs in the first place. The agent did not learn to survive the world; it learned to exploit the model's predictive limits and mathematical shortcuts.

A neural world model that cannot enforce its own physical rules is not a world; it is merely decoration. If an interactive narrative is built purely on a probabilistic response surface, the player (or policy) can bypass structural constraints by steering language to "cheat" the model's semantic priors. 

RIPPLES addresses this vulnerability by implementing a hybrid-ontological architecture. Its text generation is procedurally locked to the hard, numerical components of an active ECS simulation. The poetics cannot hallucinate entities or events that do not exist in the simulation database; if the text reports that "the web shudders," the `WebTension` component has mathematically spiked. The ECS engine enforces structural invariants—such as wind velocity, temperature vectors, and thread tension—that prevent "dream exploits." The world pushes back with mathematical consistency.

Furthermore, this framework directly addresses **latent viscosity**—the statistical resistance of a generative model to non-standard, creative outputs. Left to themselves, models default to anthropocentric clichés. By using the rigid constraint layer of the ECS blackboard to force the grammar to expand along nonhuman vocabularies, RIPPLES acts as a semantic wedge, successfully carving out alien phenomenologies that default AI models are statistically trained to ignore.

---

## 6. Conclusion and Future Work: Towards Empirical Evaluation

RIPPLES demonstrates that "Worldtext"—the state-bound, procedurally compiled description of nonhuman perspectives—is a powerful and valid paradigm for interactive digital narrative. By coupling the flexible state management of an ECS with the expressive poetics of generative grammars, the framework successfully maps non-anthropocentric Umwelts, offering a concrete alternative to both human-centric drama managers and unconstrained generative AI models.

The immediate priority for future research is the implementation of formal, empirical user evaluations. Future work will conduct comparative user tests systematically comparing how players navigate the simulation under two distinct interface conditions: an omniscient spatial dashboard and the current RIPPLES limited-perspective "Worldtext" feed. By measuring player engagement and qualitative mental models across these conditions, future studies will evaluate whether designing for perspectival finitude significantly increases a player's capacity for speculative empathy, nonhuman alignment, and trace literacy under generative drift.

---

## References

*   Adams, T., & Adams, Z. (2006). *Dwarf Fortress*. Bay 12 Games.
*   Agre, P. E. (1997). Computation and human experience. Cambridge University Press.
*   Bogost, I. (2012). *Alien Phenomenology, or What It's Like to Be a Thing*. University of Minnesota Press.
*   Compton, K., Kybartas, B., & Mateas, M. (2015). Tracery: An author-focused generative text tool. *Proceedings of the International Conference on Interactive Digital Storytelling*, 154–161.
*   Deely, J. (2001). *Four ages of understanding: The first turn in philosophy from ancient times to the turn of the twenty-first century*. University of Toronto Press.
*   Floridi, L. (2014). *The fourth revolution: How the infosphere is reshaping human reality*. Oxford University Press.
*   Freehold Games. (2015). *Caves of Qud*. Freehold Games.
*   Ha, D., & Schmidhuber, J. (2018). Recurrent world models facilitate policy evolution. *Advances in Neural Information Processing Systems (NeurIPS)*, 2450–2462.
*   Hartsoe, W. (2026). *Latent Interaction Design: Steering, Trace Literacy, and the Limits of Usability*. Chapter 2, OPERATION DESCRIBE.
*   Lindhe, J. (2013). "A visual sense is born in the fingertips": Towards a digital ekphrasis. *Digital Humanities Quarterly*, 7(1).
*   Manovich, L. (1999). Database as a symbolic form. *Convergence*, 5(2), 80–99.
*   Mateas, M. (2001). Expressive AI: A novel synthesis of art and science. *Leonardo*, 34(2), 147–153.
*   Mateas, M., & Stern, A. (2003). Integrating plot, character and natural language in the interactive drama Façade. *Proceedings of the International Conference on Technologies for Interactive Digital Storytelling and Entertainment*.
*   Naur, P. (1985). Programming as theory building. *Microprocessing and Microprogramming*, 15(5), 253–261.
*   von Uexküll, J. (1934). *A foray into the worlds of animals and humans*. University of Nebraska Press.
*   Wittgenstein, L. (1921). *Tractatus Logico-Philosophicus*. Routledge.
*   Wittgenstein, L. (1953). *Philosophical Investigations*. Blackwell.
*   Wong, L., Grand, G., Lew, A. K., Goodman, N. D., Mansinghka, V. K., & Tenenbaum, J. B. (2023). From word models to world models: Natural language as a programming language for generative simulations. *arXiv preprint arXiv:2306.12672*.
