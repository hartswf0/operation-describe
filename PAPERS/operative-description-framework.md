# Operation Describe: Practice-Based Dissertation Framework

This document outlines the master framework, controlled vocabulary, neighbor comparisons, case design, and cockpit metrics for the dissertation.

---

### 1. The Framework in One Sentence

> This dissertation investigates the conditions under which a description becomes operative (the theory), using **thick prompting** (the method) to analyze how these descriptions govern the generation and traversal of moving-image **worldtexts** (the recursive object) through **prompt-output-revision loops** (the mechanism) instrumented via **c2.html** (the prototype).

---

## 2. The Framework Diagram (Uncertain / Testable)

```text
  [ Operative Description ] (Theory under Test)
             │
             ▼
   Does a change in description yield a non-zero generation-space delta (ΔG ≠ 0)?
             │
             ▼
   [ Thick Prompting ] (Methodological Instrument)
             │
             ▼
   Composing repeatable, constraint-rich prompts to produce and classify failures.
             │
             ▼
   [ Prompt-Output-Revision Loop ] (Cineotic Mechanism)
             │
             ▼
   Address (A) ──► Build (B) ──► Cineosis (C) ──► Return (R) ──► Revised Address (A')
             │
             ▼
   [ Worldtext ] (Accumulated Object)
             │
             ▼
   The recursive media environment under test:
   Prompts + Outputs + Revisions + Interfaces + Archives + Interpretations.
             │
             ▼
   [ ABC Cineosis / c2.html ] (Moving-Image Case & Prototype)
             │
             ▼
   Testing whether motion and duration introduce distinct failure modes and return loops.
```

---

## 3. The Core Framework: Five Layers

### Layer 1: Operative Description (Theory Hypothesis)
*   **Hypothesis:** Certain prompts, labels, schemas, and descriptions function as routing infrastructures by altering a system's action-space under finite resource/token constraints.
*   **Unit of Analysis:** The **description/action pair**:
    $$\text{Unit} = \langle D, A_{\text{route}} \rangle$$
    where:
    *   $D$ is the specific descriptive form (a label, prompt, or schema).
    *   $A_{\text{route}}$ is the route (API choice, style shift, or workflow transition) it makes more likely or automatic.
*   **The Delta Metric ($\Delta G$):** A description is operative if and only if changing it yields a non-zero generation-space delta ($\Delta G \neq 0$), modifying:
    *   generated content, visual style, or motion logic
    *   the operator's revision path or interface state
    *   world-state continuity across loops.

### Layer 2: Thick Prompting (Method under Pressure)
*   **Hypothesis:** Composing prompts that specify World-state, Cultural frame, Formal constraint, Operation, Preserve, and Avoid rules creates a repeatable method for producing and analyzing generative failures.
*   **The 6-Layer Context Stack Rubric:**
    1.  **World-state:** What already exists in the target environment?
    2.  **Cultural frame:** What genres, histories, or traditions guide interpretation?
    3.  **Formal constraint:** What medium, structure, or interface limits the output?
    4.  **Operation:** What specific transformation should the system execute?
    5.  **Preserve:** What invariants must remain stable across iteration?
    6.  **Avoid:** What default patterns or failure conditions must be suppressed?

### Layer 3: Prompt-Output-Revision Loop (Cineotic Mechanism)
We do not analyze isolated prompts, but rather the recursive loops of feedback and adjustment, specifically trace-mapped in moving-image settings as:

$$\text{Loop} = \text{Address } (A) \longrightarrow \text{Build } (B) \longrightarrow \text{Cineosis } (C) \longrightarrow \text{Return } (R) \longrightarrow \text{Address' } (A')$$

### Layer 4: Worldtext (The Accumulated Object)
*   **Definition:** Worldtext is the bounded record of a generated world as it accumulates across prompts, outputs, revisions, interfaces, metadata, and interpretations.
*   **Exclusions:** A worldtext is not a storyworld, not an isolated output, and not just the prompt; it is the recursive hanging-together of all these elements.

### Layer 5: ABC Cineosis & c2.html (Moving-Image Case & Prototype)
*   **ABC Cineosis:** The subcase testing whether duration, motion, and cinematic return change the operative-description problem by introducing temporal failure modes.
*   **c2.html:** The physical prototype that instruments this loop by logging and visualizing the three registers of meaning: Descriptive (World), Interpretive (Significance), and Operative (Action-Space).

#### Distinctions Table
| Neighbor Term | Difference | What makes it unnecessary? |
| :--- | :--- | :--- |
| **Speech Act** | Focuses on isolated performative utterances. | If prompts do not alter system routing beyond local output generation. |
| **Thick Description** | Interprets cultural significance on the page. | If thick prompting fails to produce repeatable, analyzable loops. |
| **Prompt Engineering** | Seeks one-shot optimization. | If constraint stacks yield identical results to simple keyword lists. |
| **Storyworld** | The implied fictional universe. | If the worldtext fails to track the physical archive and interface state. |
| **ABC Cineosis** | Moving-image sign-making process. | If motion and duration do not feed back into the prompt revision path. |
| **c2.html** | Prototype workspace interface. | If the tool acts as a simple visual wrapper without logging semiotic state. |
| **Worldtext** | The recursive generated environment. | If outputs can be fully understood without their revision and interface histories. |

---

## 4. The Engine

$$\text{THE ENGINE} = \text{OD} \longrightarrow \text{TP} \longrightarrow \text{PORL} \longrightarrow \text{WT}$$

*   **Operative Description** ($OD$) produces **Thick Prompting** ($TP$), which structures **Prompt-Output-Revision Loops** ($PORL$), which accumulate into **Worldtext** ($WT$).
*   **The Operational Diagnostics (5 Questions):**
    1.  What description is doing work?
    2.  What route does it create in the generative process?
    3.  What output appears because of that route?
    4.  What revision confirms, rejects, or redirects it?
    5.  What part of the worldtext changes?

---

## 5. Boundary and Validation

### Generation-Space Delta ($\Delta G$)
*   A description is **non-operative** when it does not change the generation, selection, revision, interpretation, or archival status of an output ($\Delta G = 0$).
*   A description is **operative** when it produces an observable generation-space delta ($\Delta G \neq 0$), changing style, structure, continuity, medium, revision path, or archive status.

### Boundary & Validation Rubric
1.  **Definition test:** Can the committee define operative description in one sentence?
2.  **Method test:** Can another researcher use thick prompting on a different project?
3.  **Object test:** Is worldtext clearly distinguishable from prompt, output, storyworld, interface, and archive?
4.  **Archive test:** Is the case archive bounded by project, date, model/tool, revision cycle, and artifact type?
5.  **Loop test:** Does each case show prompt-output-revision loops, not isolated outputs?
6.  **Delta test:** Can you point to where a description changed the generated world?
7.  **Negative-case test:** Do you include examples where a prompt phrase failed to matter ($\Delta G = 0$)?
8.  **Transfer test:** Could an artist, scholar, or designer adopt the framework?

---

## 6. The Minimum Data Structure for Your Archive

Each entry in the research archive must follow this YAML structure:

```yaml
entry_id: SOA_001
project: Shield of Achilles
date: 2026-06-04
model_tool: Midjourney v6
input_material: Iliad Book XVIII (translated by Fagles)
operative_description: "late geometric period Greek metalwork"
thick_prompt_components:
  world_state: "Ring 2: City at peace"
  cultural_frame: "Homeric geometric iconography"
  formal_constraint: "horror vacui, flat perspective, no shadows"
  operation: "emboss concentric bronze reliefs"
  preserve: "cosmological center balance"
  avoid: "cinematic fantasy bloom or modern CGI shine"
  output_format: "bronze relief detail"
output_summary: "concentric geometric warriors with flat perspective and verdigris patina"
revision_decision: accept / reject / revise / fork
generation_delta:
  style: "Greek geometric"
  world_state: "Ring 2 populated"
  interface: "none"
  narrative: "classical"
  image_text_relation: "strict correspondence"
  archive_status: "stabilized"
failure_mode: "none"
next_prompt: "SOA_002"
theoretical_note: "Geometric style coordinates act as a high-viscosity vector anchor, successfully bypassing standard fantasy-game visual priors."
```

---

## 7. The Case-Study Framework

### Case 1: Shield of Achilles (The Mythic/Ekphrastic Case)
*   **Role:** Translates inherited cultural forms into generated world structures.
*   **Core Question:** How does thick prompting transform an inherited object, image, or myth into a recursive generated worldtext?
*   **Evidence:** Prompt logs, image/text outputs, revision chains, annotations, world-state changes, failed prompts.

### Case 2: WAG Prototype (The System/Interface Case)
*   **Role:** Proves that worldtext is shaped by interface, interaction, and revision structures.
*   **Core Question:** How does a prototype system make operative description into a repeatable design practice?
*   **Evidence:** Interface states, prompt controls, user actions, generated outputs, revision logs, diagrams, design notes.

### Case 3: Comparative Mini-Case (The Negative Case)
*   **Role:** Serves as a contrast case to establish falsifiability.
*   **Examples:** A decorative prompt phrase that had no effect ($\Delta G = 0$), a generic prompt that flattened worldtext, or an output that broke continuity despite thick prompting.

---

## 8. The Framework Terms as a Controlled Vocabulary

### Core Terms
*   **Operative description:** A description that changes generation, revision, selection, or stabilization.
*   **Thick prompting:** A repeatable method for composing constraint-rich prompts and studying their effects.
*   **Worldtext:** The recursive media environment accumulated across prompts, outputs, revisions, interfaces, archives, and interpretations.
*   **Prompt-output-revision loop:** The mechanism through which worldtext changes.
*   **Generation-space delta:** The observable difference a description makes in the generated world ($\Delta G$).
*   **Operative ekphrasis:** A subcase where description of an image/object does not merely represent it but generates or revises a media world around it.
*   **Steering:** The ethical/design problem of guiding generative systems without pretending to fully control them.

### Banned or Limited Terms
*   *Banned/Limited:* cybernetic, operator, worlding, recursive cultural system, executable description, compiler.
*   *Replacement:* Replace *"natural language as compiler"* with **"natural language as a routing layer for generative systems"**.

---

## 9. Contribution Architecture

```text
  CORE CONTRIBUTION ────► Operative description as a theory of generative steering.
  METHOD CONTRIBUTION ──► Thick prompting as a repeatable practice-based method.
  OBJECT CONTRIBUTION ──► Worldtext as the recursive media environment produced by loops.
  ANALYTIC CONTRIB. ────► Prompt-output-revision analysis.
  PRACTICE CONTRIB. ────► Bounded archive and prototype case studies.
  ETHICAL CONTRIB. ─────► Steering generated worlds through contestability & provenance.
```

---

## 10. The Dashboard Pages

### ⚡ The Engine
*   **Purpose:** Explain the $OD \to TP \to PORL \to WT$ model.
*   **Must include:** diagram, definitions, unit of analysis, example loop, generation-space delta, failure mode.

### ⚖ Boundary & Validation
*   **Purpose:** Prevent bloat.
*   **Must include:** what the dissertation is/is not, operative/non-operative distinction, worldtext distinction table, validation metrics, kill criteria.

### 📅 Milestones
*   **Purpose:** Convert concept into proposal.
*   **Milestones:**
    1.  Contribution contract
    2.  Term definitions
    3.  Archive schema
    4.  Case selection
    5.  Literature map
    6.  Method chapter draft
    7.  Case sample analysis
    8.  Prospectus draft
    9.  Committee packet

### 🗓 Weekly Planner
*   **Monday:** Define / revise one concept.
*   **Tuesday:** Annotate 2 sources.
*   **Wednesday:** Process archive entries.
*   **Thursday:** Write 500-1000 dissertation words.
*   **Friday:** Update diagrams and dashboard.
*   **Weekend:** Review, cut, plan next loop.

### 🛠 Ask Packet Form
*   **Purpose:** Make advisor meetings efficient.
*   **Must include:** what I changed, what decision I need, what evidence I have, what I am cutting, what I am uncertain about, one page of text for review.

### 🏁 Day 1-7 Board
*   **Purpose:** Start immediately with scope lock.
*   **Rhythm:**
    *   *Day 1:* One-sentence contribution locked.
    *   *Day 2:* Definitions of operative description, thick prompting, worldtext.
    *   *Day 3:* Archive schema built.
    *   *Day 4:* Shield of Achilles sample entry.
    *   *Day 5:* WAG sample entry.
    *   *Day 6:* Boundary/validation page revised.
    *   *Day 7:* 2-page dissertation contract exported.

### 🎓 Defense & Citations
*   **Purpose:** Prepare committee-facing legitimacy.
*   **Must include:** one-sentence defense, three-sentence defense, field contribution, neighbor concept comparison, core citations, possible objections, answers to objections.

---

## 11. The Neighbor-Concept Defense

| Concept | What It Does | Why Yours is Different |
| :--- | :--- | :--- |
| **Speech Act** | Shows language performs actions. | Operative description studies recursive generative steering across prompts, outputs, and revisions. |
| **Thick Description** | Interprets cultural meaning. | Thick prompting operationalizes cultural density as a prompt method. |
| **Prompt Engineering** | Optimizes model outputs. | Thick prompting studies prompt practice as cultural research, not just optimization. |
| **Storyworld** | Names a fictional world. | Worldtext includes prompts, revisions, metadata, interface states, and archive logic. |
| **Imagetext** | Studies image/text relations. | Worldtext includes image-text relations but also generative process and revision loops. |
| **Interface** | Mediates interaction. | Worldtext includes interface conditions but is not reducible to interface. |
| **Archive** | Stores materials. | Worldtext is produced through archival accumulation, but includes generative and interpretive dynamics. |

---

## 12. The Dissertation Contract

> This dissertation does not study all prompting, all AI storytelling, or all generative AI.
> 
> It studies selected **prompt-output-revision loops** in which **operative descriptions** steer the formation of **worldtexts**.
> 
> Its contribution is a theory-method pair: **operative description** names the steering function of descriptive language, and **thick prompting** provides a repeatable method for composing, observing, and revising that function.
> 
> The dissertation is validated if **worldtext** is clearly defined, the **archive** is bounded, the **method** is repeatable, and the **case studies** show how descriptions change generated worlds across revision cycles.
