# Operative Fiction: Narrative as a Control Surface in Generative Worldtexts

**Watson Hartsoe & Jay David Bolter**  
*School of Literature, Media, and Communication, Georgia Institute of Technology*

---

## Abstract

Generative AI platforms have shifted the computational narrative horizon from dialogue generation to neural world models—systems that simulate spatial-temporal environments under the steering force of natural language. Traditional human-computer interaction (HCI) and prompt-engineering paradigms attempt to steer these models using technocratic compilers: system instructions, negative filters, and relational databases. We argue that this compiler paradigm is structurally mismatched with the probabilistic, culturally sedimented nature of latent spaces. Instead, we propose **operative fiction**: the practice of deploying fictional structures, subjective mythologies, and unreliable narratives as high-context computational controls. 

Rather than treating fiction as a passive output of generative systems, we theorize it as the executable software of the *worldtext*—a multi-layered context stack (L0–L6) that spatializes language. We demonstrate that fictional narratives function as semantic compressors, utilizing the model’s pre-trained cultural priors to navigate "latent viscosity" far more efficiently than formal code. By re-reading the ur-worldtext of Homer’s Shield of Achilles and W.H. Auden’s mid-century intervention as competing operative fictions, we outline how subjective lore, contested histories, and mythic motifs steer generative physics. Finally, we formalize design principles for Interactive Digital Narrative (IDN) authors, shifting the authorial role from coding node-graphs to configuring narrative attractors in statistical probability fields.

**Keywords**: operative fiction, worldtext, context engineering, latent viscosity, prompt craft, subcreation, same-worldness.

---

## 1. Introduction: Programming with Dreams

In the field of Interactive Digital Narrative (IDN) and generative storytelling, the typical research vector is *computational*: how can we use large language models (LLMs) to write interactive scripts, generate character dialogues, or compile branching decision trees? In this approach, natural language is treated as an input that produces a narrative artifact, while the underlying control of the narrative engine remains governed by deterministic rules, database variables, or graph-based state machines.

This paper proposes a radical inversion of this paradigm. We introduce the concept of **operative fiction**: the practice of using fictional narratives, unreliable lore, and mythic structures not as the *output* of a system, but as the *executable software* used to program and steer generative world models. 

This inversion is made necessary by a qualitative shift in generative media. The transition from image models (e.g., Midjourney) to neural world models (e.g., DeepMind’s Genie, World Labs’ Marble) means that prompts no longer merely generate static visual surfaces (what Mitchell termed the *imagetext*). Instead, they condition persistent, navigable 3D simulation environments with their own physics, behaviors, and durations (what we define as the *worldtext*). 

However, computer science and HCI have approached the steering of these world models through the "compiler paradigm"—attempting to enforce coherence using sterile system instructions, negative keyword filters, and Cartesian scene graphs. We argue that this approach suffers from two severe failure modes: **technocratic capture** (reducing narrative worlds to sterile usability templates) and **prompt rupture** (the collapse of spatial and temporal logic when the model’s probabilistic defaults override flat text instructions).

```
    Traditional AI Narrative:
    [ deterministic engine ] ──────► generates ──────► [ passive fiction / assets ]

    Operative Fiction (Proposed):
    [ operative fiction / lore ] ──► configures ─────► [ probabilistic world model ]
```

Because neural world models are trained on the cultural sediment of human writing—including millions of novels, mythologies, and descriptions—their internal state-transitions are inherently governed by narrative associations rather than formal logic. Therefore, the most efficient and non-obvious way to steer them is to treat **fiction as a high-context semantic compressor**. A single mythic motif or narrative style acts as a vector anchor, navigating the model's "latent viscosity" and establishing complex physical, material, and social constraints that would require thousands of lines of deterministic code to specify manually.

This paper develops the theory of operative fiction in the worldtext. We formalize the structural stack that enables language to operate as space, define how the "Lore Book" functions as active software, stress-test the theory against the Shield of Achilles, and outline a design methodology for IDN authors.

---

## 2. The Limits of the Compiler Paradigm in Latent Space

To understand why fiction is operative, we must first diagnose why formal coding paradigms fail in latent space. In a traditional game engine or database narrative, the system operates deterministically. A programmer writes:

```typescript
class Room {
  hasRebreatherRequired: boolean = true;
  gravityConstant: number = 9.81;
}
```

The system executes these variables without deviation. However, when an author attempts to build a worldtext within a generative world model, they are writing into a probabilistic, high-dimensional vector space. The model does not execute code; it infers transitions based on statistical proximity. 

When a user prompts a world model with a thin instruction like `"generate a futuristic room, gravity is normal, but the atmosphere is toxic,"` the system frequently experiences **latent drift**. Because the visual representations of "futuristic rooms" in the model's training distribution are overwhelmingly dominated by clean, unmasked humans breathing normally, the probabilistic gravity of the default distribution (its *viscosity*) overrides the user's text. The model generates a human without a rebreather, violating the world's rules.

The standard computer science repair is to double down on the compiler paradigm: writing increasingly complex, dry negative prompts (`"no humans breathing, no unmasked faces, high detail, 8k"`) or hard-coding Cartesian scene graphs to force compliance. This is what we call the **Vermeer Problem** at the system scale: it produces an output that is fluent and visually polished, but structurally empty of the world's intended logic. It treats the prompt as an isolated command rather than understanding that in latent space, **description is always an inference** over a pre-trained cultural archive.

---

## 3. Operative Fiction as Semantic Compression

We argue that the correct way to steer a probabilistic world model is not to fight its cultural training, but to exploit it. Fictional narratives and genre conventions are not decorative; they are **highly compressed, pre-packaged vector constraint systems**.

In Clifford Geertz's (1973) study of interpretive culture, he argues that symbolic systems function as both *models of* reality (describing what exists) and *models for* reality (prescribing behavior and moods). In the context of a generative worldtext, a fictional narrative does both simultaneously. 

Consider the difference in semantic efficiency between a technocratic prompt and an operative fiction:

*   **Technocratic Prompt**: `"A post-apocalyptic street. Buildings are damaged. There are no plants. The lighting is low. Show debris on the ground. People look tired. The color palette is gray and brown."`
*   **Operative Fiction**: `"A street scene in the immediate aftermath of W.H. Auden's 'The Shield of Achilles' (1952). The leaden sky reflects the industrial wilderness, and the figures exhibit the quiet, post-heroic exhaustion of the barbed-wire era."`

The technocratic prompt attempt to specify the world's *Topos* component by component. It is brittle; if the model misses a single descriptor, the default platform mean (e.g., standard cinematic post-apocalypse assets) bleeds back in. 

The operative fiction, by contrast, deploys a specific literary anchor. By referencing Auden’s poem, the prompt invokes a dense, pre-trained cluster of aesthetic, historical, and philosophical associations in the latent space. The model automatically infers the gray lighting, the lack of vegetation, the specific mid-century military clothing, and the despondent poses of the characters. The fiction acts as a **semantic wedge** that pushes the latent generation far away from the generic platform mean (the "twelve lighthouses" of default generation) into a highly specific, cohesive region of vector space.

This is **operative fiction**: the deliberate use of narrative style, subjective lore, and intertextual frames as the steering logic for generative environments. Meaning is not generated *after* the fact; the fiction is the code that compiles the space.

---

## 4. The Worldtext Stack: Spatializing the Narrative

To implement operative fiction, we must formalize the environment in which it executes: the **worldtext**. A worldtext is not a flat lore file; it is the entire multi-layered context stack (L0–L6) that spatializes language to steer probabilistic distributions.

```
       [ L6: Output Constraints (The Thresholds) ]
                            ▲
        [ L5: User Instruction (The Active Lore) ]
                            ▲
         [ L4: Chronicle (The Temporal Memory) ]
                            ▲
         [ L3: Tool Context (The Ritual Verbs) ]
                            ▲
         [ L2: Knowledge Context (The Lore Book) ]
                            ▲
       [ L1: System Instruction (The World Law) ]
                            ▲
        [ L0: Hardware/Model (The Latent Physics) ]
```

In this stack, the relationship between absolute canon and subjective fiction is divided into two distinct databases:

1.  **The World Bible (L1)**: Holds the structural invariants (e.g., physical constants, primary historical dates) that are treated by the system as absolute truth.
2.  **The Lore Book (L2)**: The repository of subjective, unreliable, and often contradictory narratives generated *within* the world. 

In traditional narrative database design, contradictions are treated as syntax errors that must be resolved. In an operative worldtext, **contradictions in the Lore Book are active features**. A living world is experienced through the biased, limited, and mythic perspectives of its inhabitants. By structuring the Lore Book with explicit metadata tags (e.g., `<canonical/>`, `<disputed/>`, `<false_but_believed/>`), we allow competing fictions to coexist. 

When the model generates a new scene (L5), it queries the Lore Book. The model does not receive a flattened, objective history; it receives a rich, contested narrative field. The resulting generation reflects this subjectivity, producing spatial environments that feel culturally lived-in, haunted by history, and rich with ideological tension. The fiction in the Lore Book directly configures the behavioral rules of the generated space.

---

## 5. Case Study: The Shield of Achilles as Competing Operative Fictions

Homer’s description of the Shield of Achilles (*Iliad* XVIII.478–608) is traditionally analyzed as the origin of ekphrasis. We re-read it as the first document of competing operative fictions.

### 5.1 Hephaestus and the Hexameter Compiler
Homer does not describe a static shield; he describes Hephaestus *making* it. The god-smith compiles the world layer by layer, starting with cosmology at the center and ending with the Ocean at the rim. This process is driven by the oral-formulaic system—a probabilistic generative engine in which formulaic epithets act as meteral and semantic constraints. The description is constructive: the hexameter is the compiler, and the metal is the substrate.

```
                       [ Ring 5: Ocean Rim ] (Boundary Condition)
                     [ Ring 4: Dance / Ritual ] (Social Ethos)
                   [ Ring 3: Agriculture / Harvest ] (Topos Cycles)
                 [ Ring 2: Cities of War and Peace ] (Civic Mythos)
                       [ Center: Cosmology ] (Invariants)
```

The shield constitutes a world because it balances Mark J.P. Wolf's (2012) three criteria:
*   **Invention**: It alters the default assumption of the Iliad's war-world by embedding an entire civil, agricultural, and festive cosmos.
*   **Completeness**: The surrounding ring of the Ocean river acts as a boundary condition, implying that the world continues infinitely beyond the metal surface.
*   **Consistency**: The elements are bound by a shared social and physical logic, where agricultural time and civic adjudication balance the violence of the outer rings.

### 5.2 Auden's Reclassification: The Battle of Distributions
In 1952, W.H. Auden wrote "The Shield of Achilles," which acts as a literal demonstration of Layer 6 (Reclassification) in prompting. Auden uses the same prompt—"forge a shield for Achilles"—but feeds it through a different cultural distribution: the mid-twentieth century. 

Thetis expects the Homeric output: olive trees, well-governed cities, and ritual dances. But Hephaestus's forge is now conditioned by a high-viscosity post-war distribution. The output is a leaden sky, barbed wire, and bored officials. 

Auden’s poem demonstrates that **the prompt is not sovereign; it is subject to the viscosity of the epoch's training distribution**. Thetis is the originary disappointed prompt-user, discovering that her intent has been crushed by the statistical inertia of the machine. The clash between Homer’s bronze world and Auden’s leaden world is a clash between two operative fictions competing to condition the same generative space.

---

## 6. Design Principles for IDN Authors: Programming the Umwelt

To move from theoretical critique to design practice, we translate the theory of operative fiction into four core design principles for Interactive Digital Narrative creators building with generative world models.

### 6.1 Shift from Cartesian to Semantic Navigation
In traditional game design, traversal is Cartesian: the player moves their avatar across x, y, and z coordinates in a scene graph. In a generative worldtext, traversal is **semantic**. The author must design interfaces where the player's actions are translated into narrative modifications of the active context stack. 

For example, in a speculative exploration game, typing a description of a room's history ("This room was abandoned during the flood") does not merely update a text log; it modifies the L2 Lore Book, forcing the world model to physically generate watermarks, rotting floorboards, and silt deposits when the player turns the camera. Traversal is achieved by rewriting the world's history in real time.

This shift is concretely realized in the RIPPLES attic simulation framework (Hartsoe & Bolter, 2026). In RIPPLES, Cartesian coordinates are completely bypassed. Instead, the player interacts with an analogical control surface (a "DJ deck") where sliders adjust abstract relational vectors like tension, kinetic force, and decay velocity. Mutating these levers does not move a physical avatar through a 3D grid; instead, it directly updates the underlying Entity-Component-System (ECS) database, which serves as a dynamic L2 Knowledge Context. Traversal is achieved not by locomotion but by mutating the ecological vectors of the space, compiling a persistent Worldtext feed that the player must read to speculatively reconstruct the hidden states.

### 6.2 Cultivate Attractor Tokens to Fight Viscosity
Authors must identify and map the "attractor tokens" of the model they are utilizing. An attractor token is a highly specific semantic term (e.g., a named artist, a precise historical style, or a localized cultural ritual) that has high vector weight in the model's latent space. 

Instead of writing long, descriptive prompts that dilute the signal, the author builds a "glossary of attractors" within the L1 System Instructions. When the player enters a new region, the system injects the appropriate attractor token into the context window, snapping the generation from the generic platform mean to the specific narrative world.

### 6.3 Use the Six-Layer Thick Prompt Rubric
Every interactive state transition must be authored using the six-layer thick prompt rubric. Authors must explicitly define:
1.  **Visible Act**: The raw assets to be generated.
2.  **Native Meaning**: The immediate narrative context.
3.  **Code**: The genre, style, and constraints that make the asset legible.
4.  **Audience**: The perspective of the player or observing agent.
5.  **Stakes**: What is at risk in the current scene.
6.  **Reclassification**: How the assets must morph when the scene's evaluative frame changes (e.g., transitioning from a safe haven to a hostile combat zone).

By specifying all six layers, the prompt carries enough contextual density to survive transport across different state transitions without collapsing into generic defaults.

### 6.4 Implement the Same-Worldness Audit
When integrating user-generated prompts or stochastic variations into a persistent narrative, the engine must run an automated same-worldness audit. Every candidate generation (L5 output) must be validated against the world bible’s *Mythos*, *Topos*, and *Ethos*. 

If a generation violates a material invariant (e.g., introducing a technology that violates the Topos) or a social norm (violating the Ethos), the engine must reject the artifact. Crucially, the rejected output is not discarded; it is stored as a `<counterexample/>` in the L2 database, dynamically updating the negative constraints to refine the model's future steering.

---

## 7. Conclusion: The Steersman of Latent Space

The rise of generative world models marks the death of the compiler paradigm in digital storytelling. We can no longer treat the creation of interactive worlds as a task of explicit, Cartesian asset construction. In the probabilistic medium of latent space, we do not compile; we steer.

Operative fiction is the theoretical and practical framework for this new era. It acknowledges that fictional narrative is not a passive product to be displayed, but the most efficient, high-context software for configuring neural simulation environments. By structuring the context stack, indexing subjective lore, and deploying narrative attractors, the IDN author ceases to be a programmer of code and becomes the steersman (*kybernetes*) of latent space.

Homer already knew the secret: description is not representation, but constitution. The Shield of Achilles was the first executable worldtext. We have finally built the substrate to run it, and our code is fiction.

---

## References

*   Auden, W. H. (1955). *The Shield of Achilles*. Random House.
*   Bajohr, H. (2024). Operative ekphrasis: The collapse of the text/image distinction in multimodal AI. *Word & Image*, 40(2), 77–90.
*   Bateson, G. (1972). *Steps to an ecology of mind*. Ballantine Books.
*   Bolter, J. D., & Grusin, R. (1999). *Remediation: Understanding new media*. MIT Press.
*   Geertz, C. (1973). Thick description: Toward an interpretive theory of culture. In *The interpretation of cultures* (pp. 3–30). Basic Books.
*   Ha, D., & Schmidhuber, J. (2018). Recurrent world models facilitate policy evolution. *Advances in Neural Information Processing Systems (NeurIPS)*, 2450–2462.
*   Hartsoe, W., & Bolter, J. D. (2026). Designing for Perspectival Finitude: An ECS-Driven Architecture for Generative Nonhuman Umwelts. *Proceedings of the International Conference on Interactive Digital Storytelling (ICIDS)*.
*   Heffernan, J. A. W. (1993). *Museum of words: The poetics of ekphrasis from Homer to Ashbery*. University of Chicago Press.
*   Hintze, L., Proschinger Åström, T., & Schossau, M. (2026). Language-image loops: Convergence and divergence in autonomous multimodal cycles. *Computational Linguistics*.
*   Homer. (ca. 730 BCE). *Iliad*.
*   Karpathy, A. (2024). Context engineering. Keynote, AI Engineer World's Fair.
*   Krieger, M. (1992). *Ekphrasis: The illusion of the natural sign*. Johns Hopkins University Press.
*   Lord, A. B. (1960). *The singer of tales*. Harvard University Press.
*   Meyer, R. (2025). Platform realism and the visual economy of AI-generated images. *New Media & Society*.
*   Mitchell, W. J. T. (1994). *Picture theory: Essays on verbal and visual representation*. University of Chicago Press.
*   Naur, P. (1985). Programming as theory building. *Microprocessing and Microprogramming*, 15(5), 253–261.
*   Pavel, T. G. (1986). *Fictional worlds*. Harvard University Press.
*   Steyerl, H. (2023). Mean images. *New Left Review*.
*   Tosca, S., & Klastrup, L. (2020). *Transmedial worlds in everyday life: Networked reception, social media and fictional worlds*. Routledge.
*   Webb, R. (1999). Ekphrasis ancient and modern: The invention of a genre. *Word & Image*, 15(1), 7–18.
*   Wolf, M. J. P. (2012). *Building imaginary worlds: The theory and history of subcreation*. Routledge.
*   Wong, L., Grand, G., Lew, A. K., Goodman, N. D., Mansinghka, V. K., & Tenenbaum, J. B. (2023). From word models to world models: Natural language as a programming language for generative simulations. *arXiv preprint arXiv:2306.12672*.
