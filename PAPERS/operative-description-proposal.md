# PhD Proposal: Operative Description
## How Labels, Prompts, and Schemas Route Action

**Watson Hartsoe**  
*School of Literature, Media, and Communication, Georgia Institute of Technology*

---

## One-Sentence Thesis

This project investigates the conditions under which a description ceases to be decorative and becomes operative—hypothesizing that certain prompts, labels, schemas, and descriptions function as routing infrastructures by measurably altering ($\Delta G \neq 0$) a system's action-space.

---

## Abstract

This dissertation tests the hypothesis that descriptive language functions as a routing infrastructure in contemporary human-machine systems. Rather than asserting "operative description" as an already-proven fact, this project frames the concept as a testable class of descriptive acts: descriptions (such as labels, prompts, and schemas) that do not merely represent state variables, but measurably steer subsequent action.

Drawing on Wittgenstein’s account of language-games, Austin’s speech-act theory, Geertz’s thick description, and Bowker and Star’s classification theory, we investigate this suspicion at three computational scales. First, we examine **Prompting as Operative Ekphrasis** in text-to-image and text-to-video models, testing whether text tokens function as reliable steering signals under the gravity of "latent viscosity." Second, we study **Thick Prompting and Context Engineering**, testing whether layering Geertzian cultural codes prevents latent drift across system boundaries (the reclassification test). Third, we study **Narrative Control in Generative Worldtexts**, exploring how schemas, tool descriptions, and Lore Books configure the simulated physics and actions of neural world models and autonomous LLM workflows. The dissertation contributes a testable, practice-based framework for analyzing prompt-output-revision loops and steering-based design in digital media studies, philosophy of language, and human-computer interaction.

---

## Core Idea: From Mirror to Lever (A Testable Suspicion)

Some descriptions sit on the page. Other descriptions appear to move things:

*   `bug` is suspected to route a software issue toward repair.
*   `toxic` is suspected to route a comment toward warning, hiding, or moderation queues.
*   `ESI Level 2` is suspected to route a patient toward urgent care.
*   `issue_refund(order_id)` is suspected to route an LLM agent toward API execution.
*   *“A post-war leaden sky...”* is suspected to route a diffusion model away from generic slop into a specific latent valley.

These represent candidate **operative descriptions**. We trace whether they alter the action-space of a situated operator.

Following Gregory Bateson's formulation of information as a "difference that makes a difference," we formulate a mathematical test: a description is operative only when it yields a non-zero **generation-space delta ($\Delta G \neq 0$)**. That is, a change in description must produce a measurable change in:
1.  Generated content, style, or motion logic.
2.  The operator's revision path or interface state.
3.  The system's subsequent routing and consequence.

If $\Delta G = 0$, the description is decorative, not operative.

---

## Theoretical Spine

The framework anchors itself in three humanistic lineages, translating them into computational mechanics:

### 1. Wittgenstein: Language as Use
Wittgenstein establishes that the meaning of a word is its use inside a rule-bound language-game ([Stanford Encyclopedia of Philosophy][1]).
*   *Translation:* A prompt or system instruction compiles a temporary language-game for an LLM operator, establishing what moves are legal, cheap, or impossible.

### 2. Austin: Speech-Acts as Doing
Austin shows that performative utterances do not describe reality, but execute state changes directly ([Stanford Encyclopedia of Philosophy][2]).
*   *Translation:* Operative description extends performativity to descriptive classifications. Naming a post "toxic" or a user a "churn risk" instantly opens and closes code-level and human-level action paths.

### 3. Geertz: Thick Description as Context
Geertz shows that description is not passive surface observation, but the reconstruction of the webs of significance that make an action intelligible ([UCSC People][3]).
*   *Translation:* "Thick Prompting" is the practice of context engineering. It builds multi-layered prompts that specify the rules, codes, and stakes of a generation to survive transport across probabilistic vector spaces without collapsing into default averages.

---

## The Case Studies

The dissertation examines three cases where description functions as routing infrastructure:

```
                  [ HIGH-DIMENSIONAL REALITY / INTENT ]
                                     │
                                     ▼
                      [ OPERATIVE DESCRIPTION D ]
                                     │
            ┌────────────────────────┼────────────────────────┐
            ▼                        ▼                        ▼
     [ Case 1: Prompt ]       [ Case 2: Thick ]       [ Case 3: Worldtext ]
     Multimodal Diffusion     Context Engineering      World Models & Schemas
            │                        │                        │
            ▼                        ▼                        ▼
    Visual Generation        Latent Compliance        Executable Agency & Physics
```

### Case 1: Prompting as Operative Ekphrasis (The Imagetext Case)
*   **The System:** Text-to-image and text-to-video diffusion models (e.g., Stable Diffusion, Midjourney, Sora).
*   **The Description ($D$):** Text prompts detailing visual content, style, and camera behaviors.
*   **The Operator ($O$):** The multimodal diffusion model.
*   **The Route:** Sampling pathways in the latent vector space.
*   **The Action:** The generation of visual surfaces (Mitchell's *imagetext*).
*   **The Argument:** Prompting recovers the ancient rhetorical practice of **ekphrasis** (making the absent visible through words). In diffusion models, description and generation collapse: writing a description acts as the direct compilation of an image. We trace how natural language functions as a visual compiler under the constraints of "latent viscosity."

### Case 2: Thick Prompting and Context Engineering (The Cultural/Social Case)
*   **The System:** Professional prompt architectures and context-engineering pipelines.
*   **The Description ($D$):** Multi-layered prompts structured using Geertz's six layers: visible act, native act, code, audience, stakes, and reclassification.
*   **The Operator ($O$):** Large language models and multimodal generators.
*   **The Route:** Navigation through high-viscosity probability fields.
*   **The Action:** The preservation of world coherence and resistance to default platform slop.
*   **The Argument:** A thin prompt (e.g., "a golden shield") is vulnerable to **latent drift**—the model's statistical defaults override the user's intent. By engineering **thick prompts** that specify style codes, stakes, and reclassification thresholds, developers build semantic constraints that maintain world consistency across different model versions.

### Case 3: Narrative Control in Generative Worldtexts (The Worldtext Case)
*   **The System:** Autonomous LLM agent frameworks (function calling) and neural world models (Genie, RIPPLES).
*   **The Description ($D$):** Function descriptions, JSON schemas, and narrative "Lore Books."
*   **The Operator ($O$):** LLM agents and simulation compilers.
*   **The Route:** API selection, database queries, and simulated physical interactions.
*   **The Action:** Executable program calls and persistent spatial-temporal simulation updates (the *worldtext*).
*   **The Argument:** In agentic workflows and world models, text descriptions function as the direct steering logic for execution. A tool description (e.g., "issue refund") or a Lore Book entry does not merely describe the world; it configures the physical constants, behavioral rules, and permissions of the simulation.

---

## Methodology: Routing Analysis

For each case, we apply a consistent six-question diagnostic framework to map the lifecycle of the description:

1.  **What is the description?** (The label, prompt, or schema)
2.  **What object does it classify or frame?** (The raw user input, code, or coordinate)
3.  **Who or what reads the description?** (The operator: human developer, LLM agent, or diffusion engine)
4.  **What action does it route?** (The visual compilation, API selection, or workflow transition)
5.  **What does it compress or ignore?** (The context, cultural register, or alternative pathways)
6.  **What feedback loop confirms, contests, or revises the route?** (Errors, user corrections, or model retries)

---

## Chapter Plan

### Chapter 1: Description as Routing (The Core Theory)
*   **Aims:** Define the theoretical paradigm of operative description. Dismantle the "mirror theory of language" (representational semantics) and establish descriptions as routing mechanisms inside feedback-governed systems.
*   **Theoretical Lineage:** Wittgenstein (meaning as use in language-games), Austin (speech acts and the performative dimension of descriptive language), and Geertz (thick description and translation of symbolic frames).
*   **Key Concepts:**
    *   *The Register Triad:* Descriptive (rendering state) $\to$ Interpretive (mapping significance) $\to$ Operative (routing action).
    *   *The Unit of Analysis:* The **description/generation-route pair** $\langle D, G_{\text{route}} \rangle$, mapping descriptive tokens to changes in generated states, constraints, or styles.
    *   *The Generation-Space Delta:* Mathematical formulation of operativity, measuring the change in output distribution ($\Delta G \neq 0$).
*   **Explanatory Objective:** Distinguish operative description from traditional classification systems, pure metadata, and speech acts, framing it as substrate-agnostic processing.

### Chapter 2: Prompting as Operative Ekphrasis: The Imagetext
*   **Aims:** Analyze text-to-image and text-to-video diffusion models as systems of **operative ekphrasis**—where the act of description collapses directly into the act of visual generation.
*   **Theoretical Lineage:** Classical ekphrasis theory (Homer, Quintilian's *phantasia* and *enargeia*, Spitzer's 1955 redefinition), Mitchell’s *imagetext* (verbal/visual relations), and Harun Farocki's *operational images* (images that perform actions).
*   **Key Concepts:**
    *   *Natural Language as a Routing Layer:* Text prompts functioning as visual compilers in latent space.
    *   *Latent Viscosity:* The statistical density and inertia of the model's pre-trained distribution.
    *   *Latent Bricolage:* The practice of scavenging and recombining semantic fragments to bypass default platform averages.
*   **Evidence & Archive:** Controlled prompts, generated image/video outputs, and latent space trajectory logs.

### Chapter 3: Thick Prompting and Context Engineering
*   **Aims:** Formulate **Thick Prompting** as a repeatable methodological framework for context engineering in generative models.
*   **Theoretical Lineage:** Clifford Geertz’s (1973) thick description methodology, and Lucy Suchman’s plans and situated actions.
*   **Key Concepts:**
    *   *The 6-Layer Thick Prompt Rubric:* World-state (existing content), Cultural frame (histories/genres), Formal constraint (medium/structure), Operation (transformation), Preserve (stability rules), and Avoid (failure conditions).
    *   *The Warning of the Cohen Case:* How thin prompts experience **latent drift** or context collapse when transported across systems (analogous to Cohen's mezrag covenant failing under French colonial law).
    *   *Reclassification:* The transfer test of prompt durability across different platforms and evaluation settings.
*   **Evidence & Archive:** Structured archives of prompt-output-revision loops demonstrating world consistency and default resistance.

### Chapter 4: Narrative Control in Generative Worldtexts
*   **Aims:** Study how schemas, tool descriptions, and prompt-based "Lore Books" act as control surfaces that compile simulated physics and executable agent actions.
*   **Theoretical Lineage:** Hephaestus's forge and the Shield of Achilles as the ur-worldtext (*invention*, *completeness*, *consistency*), Bowker and Star's infrastructure studies, and Edwin Hutchins's distributed cognition.
*   **Key Concepts:**
    *   *The Context Stack (L0–L6):* The multi-layered framework of simulation (hardware, system law, Lore Book, tools, timeline, user instructions, output thresholds).
    *   *The Lore Book as Active Software:* How contradictory narrative archives, subjective histories, and disputed lore configure the behavior and physics of navigable environments.
*   **Design Prototype:** The RIPPLES attic simulation engine (Hartsoe & Bolter, 2026), demonstrating how Entity-Component-System (ECS) relational databases compile a persistent, speculative Worldtext feed.

### Chapter 5: The Politics of the Threshold
*   **Aims:** Compare the cases to trace the political, ethical, and design dynamics of operative description routing systems.
*   **Theoretical Lineage:** Michel Foucault (discourse, power/knowledge, and institutional discipline), Geoffrey Bowker and Susan Leigh Star (the politics of classification infrastructures), and Tarleton Gillespie & Sarah T. Roberts (platform governance, moderation labor, and queue asymmetry).
*   **Key Concepts:**
    *   *Jurisdictional Asymmetry:* Who controls the schemas, who writes the world bibles, and who must obey the automated routes.
    *   *The Cost of Error:* How marginalized subjects pay the price of misrouting (e.g., false-positive moderation blocks, under-triaged care, or denied database privileges).
    *   *Design Criteria for Accountable Steering:* Outlining guidelines for transparent, contestable, and reversible description interfaces that support human override and provenance documentation.

---

## Significance and Contribution

This dissertation unifies digital media theory, STS, and AI engineering. Rather than treating prompt craft as a modern folklore or engineering anomaly, it establishes prompting as the contemporary manifestation of a 2,500-year-old rhetorical lineage. By formalizing the **description/action pair** under finite attention and token budgets, the project provides a materialist, semiotic vocabulary suited to systems in which natural language has been upgraded to executable infrastructure.

---

[1]: https://plato.stanford.edu/archives/win2006/entries/wittgenstein/ "Ludwig Wittgenstein (Stanford Encyclopedia of Philosophy/Winter 2006)"
[2]: https://plato.stanford.edu/entries/speech-acts/ "Speech Acts (Stanford Encyclopedia of Philosophy)"
[3]: https://people.ucsc.edu/~ktellez/geertz1973.pdf "Thick Description"
