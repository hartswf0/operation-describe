# Attention-Tax Semiotics: Cybernetic Operator Pragmatics and the Constellation of Meaning

**Watson Hartsoe**  
*School of Literature, Media, and Communication, Georgia Institute of Technology*

---

## Abstract

This paper formalizes **Cybernetic Operator Pragmatics** (also termed the **Attention-Tax Theory of Meaning**) by constructing a comprehensive constellation of language theories around a single, unified claim: language is not primarily a representational mirror, but an attention-governance system that allows bounded operators (human, machine, biological, or institutional) to maintain an actionable world. We analyze twenty distinct linguistic, semiotic, and computational frameworks—spanning structuralism, deconstruction, information theory, and transformer architectures. We demonstrate that these frameworks are not merely disparate "opinions about words," but localized accounts of what meaning costs, where interpretation occurs, and how description becomes operation. By organizing these frameworks into a single semiotic stack, we outline how signs reorganize operator attention, how attention conditions action-space, and how action feeds back to stabilize or revise meaning. Finally, we formalize the descriptive/interpretive/operative triad and discuss its direct application to prompt engineering and human-computer interface design.

---

## 1. Introduction: Rejecting the Mirror

The foundational error of classical semantics is the "mirror theory of language." This paradigm assumes that a sign is a passive label pointing to an objective referent, and that a sentence is a representation of an external state of affairs:

```text
  [ Word ] ────────────► names ────────────────► [ Object ]
  [ Sentence ] ────────► represents ───────────► [ State of Affairs ]
```

This model treats meaning as a static correspondence. It assumes that reference is costless, that the channel is noise-free, and that the interpreter is an unconstrained, disembodied spectator. 

Cybernetic Operator Pragmatics breaks from this mirror. It argues that language is a regulatory technology. Signs do not reflect an objective world; they actively condition and restrict the salience field of a situated operator:

```text
  [ Sign / Description ]
            │
            ▼
  [ Operator Attention ] ──► Opens / Closes ──► [ Action-Space ]
                                                      │
                                                      ▼
  [ Meaning / Stability ] ◄── Feedback Loop ◄─── [ Action ]
```

Under this framework, **meaning is the operational effect of a description on a situated operator within a feedback-governed system.** Or more sharply: 

> **Meaning is what a sign lets an operator do next.**

This definition serves as the conceptual bridge linking linguistics, cognitive science, cybernetics, and artificial intelligence. To understand how this bridge operates, we must map how different language theories locate, calculate, and govern the costs of interpretation.

---

## 2. The Constellation Matrix

The big map of language theories is not a collection of competing truths, but a matrix of attention allocation. Each theory identifies a unique site where meaning is produced, a specific tax imposed on the operator, and a mechanism by which description becomes operation:

| Theory / Framework | Where Meaning Happens | The Attention Tax (What it Costs) | Operational Transition (How Description Becomes Action) |
|:---|:---|:---|:---|
| **Reference Theory** | In the mapping from word to object | Identification of the referent | Labeling targets for manipulation |
| **Saussurian Structuralism** | In the relational system of difference | Distinguishing contrasts ($langue$) | Classifying state variables |
| **Peircean Semiotics** | In the triadic interpretant relation | Compiling the interpretant | Reorganizing operator response |
| **Formal Semantics** | In model-theoretic truth conditions | Logical parsing and validation | Enforcing schema and constraints |
| **Shannon Information Theory** | In signal transmission over channels | Overcoming noise and entropy | Coding for error-free execution |
| **Wittgensteinian Pragmatics** | In rule-bound language-games | Inferring game rules and context | Executing legal moves in the game |
| **Speech-Act Theory** | In the performance of the utterance | Determining illocutionary force | Direct execution of state changes |
| **Gricean Pragmatics** | In intentional implicature | Calculating cooperative inferences | Decoding implicit goals and intents |
| **Geertzian Anthropology** | In webs of significance | Navigating thick cultural codes | Staging situated ritual behavior |
| **Hermeneutics** | In the fusion of interpretive horizons | Aligning historical/local frames | Adjusting behavior to meet the text |
| **Bakhtinian Dialogism** | In the clash of heteroglossic voices | Disambiguating registers and genres | Selecting the authoritative voice |
| **Deconstruction** | In the trace, deferral, and instability | Locating exclusions and binaries | Exposing system contradictions |
| **Discourse (Foucault)** | In institutional power/knowledge | Maintaining legible classifications | Enforcing subject-positions and rules |
| **Cognitive Linguistics** | In embodied, conceptual metaphors | Mapping physical schemas to abstractions | Channeling thought via spatial cues |
| **Enactivism** | In sensorimotor environmental action | Coordinating bodily affordances | Direct sense-making via movement |
| **Distributional Semantics** | In vector co-occurrence profiles | Resolving high-dimensional proximity | Navigating token neighborhoods |
| **Transformer Architectures** | In contextual token attention weights | Weighting global dependencies | Sampling likely continuations |
| **Programming Semantics** | In runtime abstract machines | Compiling syntax, state, and type | Executing deterministic instructions |
| **Natural Language Ontology** | In implicit linguistic category sorts | Maintaining ontological categories | Structuring database schema |
| **Rylean Cognitive Pragmatics** | In active situated transactions (speech as trade) | Discerning logical grammar; holding the thread | Reorganizing action-space via achievements ($\Delta P$) |
| **Cybernetic Operator Pragmatics** | In the alteration of operator action-space | Managing bounded attention budgets | Directing steering loops under drift |

---

## 3. Structural and Relational Fields

### 3.1 Saussure: Language as Difference
Ferdinand de Saussure (1916) established that language is not an aggregate of labels, but a closed system of differences. As summarized in the *Stanford Encyclopedia of Philosophy*, Saussure distinguishes between **langue** (the abstract system of linguistic conventions) and **parole** (individual acts of speaking). In structuralism, a sign carries no intrinsic essence; it exists only by virtue of what it is *not*. 

Under Cybernetic Operator Pragmatics, this is formulated as:

$$\text{Language} \text{ does not describe by mirroring a } \text{World}; \text{ it describes by installing a } \text{Difference-System}.$$

Every language-game taxes operator attention toward binary or n-ary contrasts:
$$\text{human / nonhuman}, \quad \text{legal / illegal}, \quad \text{sacred / profane}, \quad \text{bug / feature}, \quad \text{signal / noise}$$

For machine operators, this structural difference-field is materialized directly in the vector space:

$$\text{Embedding Space} \text{ is not a dictionary; it is a learned field of topological differences}.$$

A token carries weight not because it maps to an external object, but because of its relative coordinates within a high-dimensional manifold of other tokens.

### 3.2 Distributional Semantics: Proximity and Context
Distributional semantics operationalizes Saussure's relational view through John Rupert Firth's (1957) maxim: "You shall know a word by the company it keeps." Modern NLP models learn distributed representations (e.g., word2vec) where semantic similarity corresponds to spatial proximity in a vector neighborhood.

In our system:
$$\text{The model does not begin with definitions; it begins with statistical neighborhoods}.$$

A word is a node in a vast, relational gravity well. The word "bank" has no fixed definition; its local neighborhood is warped by surrounding context tokens (e.g., "river, mud" vs. "money, vault"). Thus:

$$\text{Prompting} = \text{Shaping the neighborhood of likely continuations}.$$

By injecting specific style tokens ("Write like a memo" vs. "Write like scripture"), the prompt engineer adjusts the semantic gravity of the latent space, forcing the model operator's output vector to land in a highly specific basin of attraction.

---

## 4. Triadic Mediation and Semiosis in Feedback

Charles Sanders Peirce (1931) rejected the dyadic sign-referent model, proposing instead a triadic relation: the **Sign** (the representation), the **Object** (the referent), and the **Interpretant** (the mental effect or further sign produced by the relation).

```text
       [ Object ]
         /    \
        /      \
  [ Sign ] ──► [ Interpretant ] ──► Reorganizes [ Operator Action ]
```

In our framework:
$$\text{The Sign does not jump directly to the Object; it produces an Interpretant}.$$

Meaning is not in the sign itself; it occurs when the interpretant reorganizes the operator's potential action. Smoke does not "contain" fire; it is a sign that compiles an interpretant within the operator, shifting their action space from stasis to flight or investigation.

For AI systems:
$$\text{Prompt (Sign)} \;\; \longrightarrow \;\; \text{Model Response (Interpretant)} \;\; \longrightarrow \;\; \text{User Reaction (Next Interpretant)}$$

Meaning is not established in a single execution pass. It is a continuous, recursive chain of interpretants: a process of **semiosis in feedback**.

---

## 5. Precision and Transmission under Noise

### 5.1 Formal Semantics: The Precision Tax
Formal semantics (Montague, 1970) treats natural language with the mathematical rigor of formal logic. As the *Stanford Encyclopedia of Philosophy* notes, Richard Montague argued that there is no important theoretical difference between natural languages and the artificial languages of logicians.

Formal semantics defines the meaning of a sentence as its truth conditions: under what model configurations is the statement true?

In our framework, this represents a specific, upfront attention tax:

$$\text{Formal Semantics} = \text{The attention tax paid for structural precision}.$$

In machine environments, this corresponds to schemas, JSON validation, typed variables, and constraint satisfaction. It is the compiler that prevents semantic drift. A vague prompt (`"Extract info"`) pays no upfront tax but suffers high output ambiguity. A structured prompt (`"Return JSON with keys: name, amount, source"`) pays a heavy upfront tax to make validation cheap.

### 5.2 Shannon: Transmission and Bandwidth
Claude Shannon (1948) modeled communication as the transmission of messages through a noisy channel, focusing on entropy, redundancy, and channel capacity, while intentionally bracketing semantic meaning.

In our terms, Shannon's channel equations represent a fundamental physical constraint on all operators:

$$\text{Token Burn} = \text{Machine cost of maintaining signal through noisy context}.$$
$$\text{Cognitive Load} = \text{Human cost of maintaining signal through noisy situation}.$$

If the channel (a prompt, a user interface, a corporate procedure) is filled with noise (conflicting rules, layout clutter, redundant paperwork), the operator must spend its scarce attention budget on error correction rather than constructive action.

---

## 6. Use, Games, and Speech Acts

### 6.1 Wittgenstein: Language-Games
Ludwig Wittgenstein (1953) shifted the study of meaning from representation to use. A word's meaning is its function inside a rule-bound language-game. 

In our system:
$$\text{Meaning} = \text{Move} \text{ inside } \text{Game}.$$

An command like `"Run it"` is semantically empty until the active game is declared: is it a code compiler, a theatrical performance, a political campaign, or a physical sprint?

For generative models, this is the primary mechanism of steering:

$$\text{A prompt compiles a temporary language-game for a machine operator}.$$

By prompting a model with a specific persona ("Act as a code debugger"), the author does not retrieve a static answer; they construct a temporary game with its own legal moves, success criteria, and interpretive rules.

### 6.2 Austin: Utterance as Action
John Langshaw Austin (1962) and John Searle (1969) broke the boundary between saying and doing through speech-act theory, demonstrating that performative utterances ("I promise," "I declare war") do not describe a state of affairs, but execute one.

Our framework radicalizes this claim:

$$\text{All description is inherently performative and operative}.$$

Descriptions do not merely report data; they construct the subject positions through which future operations are justified:

```text
  "Patient" ─────────► permits ─────────► [ diagnosis, treatment, billing ]
  "Suspect" ─────────► permits ─────────► [ surveillance, arrest, interrogation ]
  "User" ────────────► permits ─────────► [ behavioral tracking, metric optimization ]
  "Bug" ─────────────► permits ─────────► [ debugging, code patch ]
```

Every description alters the operator's permitted action-space. The line between saying and doing is a illusion of scale.

---

## 7. Inference, Context, and Cultural Thickness

### 7.1 Grice: Implicature and cooperative principles
Paul Grice (1975) demonstrated that human communication depends on cooperative implicature: hearing what is *not* said by calculating the speaker's intent. 

In our terms:
$$\text{Meaning} = \text{Literal Content} + \text{Inferred Operation}.$$

If a human asks an AI, `"Can you write this?"`, the literal semantic query is about capability. The pragmatic, Gricean interpretation is a request for generation. Weak prompt engineering imposes a heavy Gricean tax on the model, forcing it to guess the user's implicit constraints. Effective prompts represent **implicature debt reduction**—specifying goals, formats, and limitations explicitly to save the model's scarce processing resources.

### 7.2 Geertz: The Salience Web
Clifford Geertz (1973) formulated culture as a semiotic web of significance. His classic distinction between a blink (physiological twitch) and a wink (communicative signal) shows that interpretation requires reconstructing the latent social code.

In our system:

$$\text{Thick Description} = \text{The reconstruction of the attention-tax system required for use}.$$

To read a wink, the operator must pay an attention tax, monitoring variables like intent, audience, and relationship. A thin prompt produces default, low-context output (the platform mean). A thick prompt specifies the cultural, stylistic, and normative frame required to guide the model away from generic defaults into precise, meaningful operations.

---

## 8. Horizons, Voices, and Instabilities

### 8.1 Hermeneutics: Horizon Fusion
Contemporary hermeneutics (Gadamer, 1960) treats understanding not as the decoding of a sender's objective signal, but as a "fusion of horizons" ($Horizontverschmelzung$) between the interpreter and the text.

In our framework:
$$\text{Interpretation} = \text{The collision of the Operator Horizon and the Sign Horizon}.$$

The machine's horizon is defined by its training distribution, system prompt, active context window, and tools. The human's horizon is defined by their cognitive capacity, culture, stakes, and goals. Prompting is the deliberate attempt to align these horizons using a limited budget of tokens:

```text
  [ User Horizon: Desire/Stakes ] ──► [ Prompt Alignment ] ◄── [ Model Horizon: Data/Prior ]
```

### 8.2 Bakhtin: Heteroglossia
Mikhail Bakhtin (1934) argued that language is never a single, unified medium; it is a polyphonic field of social voices, classes, and historical registers (heteroglossia). 

Large Language Models are inherently Bakhtinian engines:

$$\text{Model Output} = \text{Statistical heteroglossia constrained by prompt context}.$$

A model response is a braid of multiple social registers (corporate, academic, legal, therapeutic). A prompt acts as an editor of these voices, explicitly silencing certain registers to isolate the authoritative voice required for the game:

```text
  "Do not use startup optimism. Do not use therapy-speak. Use precise systems-theory prose."
```

### 8.3 Derrida: Deferral and the Seam
Jacques Derrida (1967) attacked the "metaphysics of presence," showing that meaning is never fully stable or present; it is constantly deferred ($différance$), relying on traces, absences, and exclusions.

In our terms:
$$\text{No prompt contains its full interpretation; no output contains its full meaning}.$$

fluency is often a mask for interpretive instability. Deconstruction is the diagnostic practice of locating the seams—the suppressed contradictions, default assumptions, and binary exclusions (e.g., what voices are erased when a model is prompted to be "neutral" or "objective"?).

---

## 9. Discourse, Metaphor, and Embodiment

### 9.1 Foucault: Discourse and Power
Michel Foucault (1972) demonstrated that discourse does not merely report objects; it actively produces subjects and institutional realities (power/knowledge).

In our system:
$$\text{Description} = \text{Subject-Position Production}.$$

When an AI system classifies a user as a "churn risk," or an employee as "noncompliant," it is not reporting a natural state. It is executing an institutional discourse that authorizes specific actions (surveillance, denial of service, intervention). Under Foucault's lens, the attention tax becomes an instrument of governance:

$$\text{Attention Tax} = \text{Systemic Discipline}.$$

### 9.2 Cognitive Linguistics: Embodied Metaphor
George Lakoff and Mark Johnson (1980) proved that human conceptual systems are structured metaphorically by mapping bodily experiences onto abstract concepts (e.g., "Argument is War," "Time is Money").

In our terms:
$$\text{Metaphors are soft control surfaces that orient operator attention}.$$

When a prompt instructs a model to "sharpen the argument" or "build a foundation," it is not using decorative language. It is utilizing embodied metaphors to warp the statistical probability field of the model, routing attention along pathways derived from physical blades or buildings.

### 9.3 Enactivism: Sense-Making in Action
Enactivism (Varela, Thompson, & Rosch, 1991) asserts that cognition is not an internal representation of an external world, but the emergence of meaning through sensorimotor interaction between organism and environment (sense-making).

In our system:
$$\text{Meaning is tool-relative and action-bounded}.$$

A door handle means "pull" because of the operator's hand shape and physical habits. For an AI agent, its "body" is its toolset (APIs, browser, interpreter). The prompt `"Book the flight"` is semantically vacant to a raw LLM. It becomes meaningful only when coupled with the sensorimotor affordances of a browser tool and payment permissions.

---

## 10. Computation, Ontologies, and Execution

### 10.1 Transformers: Computational Selection
The Transformer architecture (Vaswani et al., 2017) formalized attention mathematically as a scaled dot-product between queries, keys, and values.

Our framework builds a structural bridge between this mathematical mechanism and cognitive semiotics:

$$\text{All operators (human or machine) must select relevance under attention constraint}.$$

*   **Human**: cognitive load (measured in working memory limits).
*   **Model**: context pressure (measured in token budget and latency).
*   **Culture**: common sense (measured in default salience rules).
*   **Interface**: visual hierarchy (measured in screen space and layout).

### 10.2 Programming Semantics: Operational Execution
In computer science, operational semantics defines a program's meaning by the state transitions it executes on an abstract machine.

We map this execution model across three scales of language:

$$\begin{aligned}
  \text{Code} &= \text{Maximally operative language for deterministic machines.} \\
  \text{Prompt} &= \text{Semi-operative language for probabilistic interpreters.} \\
  \text{Natural Language} &= \text{Culturally operative language for embodied operators.}
\end{aligned}$$

Code taxes syntax and type; prompts tax context and ambiguity; human language taxes social codes and relational history. All three are executable instructions that run on different substrates.

### 10.3 Natural-Language Ontology: Smuggling Worlds
Natural-language ontology (Bach, 1986) studies the ontological commitments implicit in our grammar (e.g., how language distinguishes objects from events).

In our terms:
$$\text{Every taxonomy is a legislated world-model}.$$

When a database schema classifies entities, or a prompt instructs: `"Classify tickets by urgency and sentiment"`, it does not report a neutral reality. It smuggles a complete ontology into the system, enforcing what kinds of things are permitted to exist for the operator.

---

## 11. Rylean Cognitive Pragmatics: Weights, Generation, and Achievements

Gilbert Ryle’s philosophy of mind and language provides a critical corrective to both intellectualist "inner logic" myths and behaviorist "fluency-equals-thought" reductionism. By framing language as an active, situated performance governed by public criteria, Ryle maps directly to the trade-offs of modern transformer architectures.

### 11.1 Capital vs. Trade: Language vs. Speech
To dismantle the intellectualist fallacy, Ryle (1961) establishes a fundamental distinction between language and speech:
*   **Language is Capital:** A language is a stock, fund, or treasury of words, constructions, idioms, and intonations. It is a set of learned, reusable, and teachable instruments.
*   **Speech is Trade:** Speech is the active, situated transaction of using that capital to say something on a particular occasion.

In the regime of generative AI, this economic analogy maps directly to the system's architecture:
*   **The Model Weights are Capital:** The trained parameters, token embeddings, and attention weights represent the accumulated stock of language. They are stored, static, and reusable.
*   **Token Generation is Trade:** The runtime activation, token-by-token decoding, and tick-by-tick traversal represent speech. The model does not store sentences; it generates them dynamically as transactions under the pressure of the prompt.

### 11.2 Ordinary vs. Logical Grammar: Language-Faults vs. Speech-Faults
By separating the instrument (capital) from the act (trade), Ryle identifies two different ways language can fail:
*   **Language-Faults:** Grammatical solecisms, spelling errors, and unidiomatic constructions. These are failures of instrument mastery. A language instructor corrects them.
*   **Speech-Faults:** Absurdities, circularity, category mistakes, and invalid inferences. These are failures in the act of saying. A logician or philosopher corrects them.

This distinction exposes the gap between **ordinary grammar** (governing syntax and acceptable construction) and **logical grammar** (governing the possible sense of what is said):
*   *Large Language Models* have mastered language as capital: they rarely commit language-faults.
*   However, lacking a situated orientation in a persistent world, they are highly vulnerable to speech-faults. A model can generate a grammatically flawless paragraph that is completely circular, logically absurd, or commits category mistakes, showing that syntax is not a guarantor of operational sense.

### 11.3 Inference as an Achievement ($\Delta P$)
Ryle's grammar of mind is built on the achievement-word. Drawing an inference is not a process parallel to searching or arguing; it is the terminus: a discrete state transition that reorganizes the operator's attention allocation and shifts their action-space:

$$\text{Inference}(O) : P_{\text{before}}(O, S, A) \to P_{\text{after}}(O, S', A)$$

The meaning of the inference is the operational delta:

$$\Delta P = P_{\text{after}} - P_{\text{before}}$$

By contrast, the retrospectively written **argument** is a low-operativity trace ($\Delta P \to 0$ for the thinker). The thinker cannot "re-infer" the conclusion if they already achieved it. The subsequent recitation of the proof is a decorative performance, a compliance trace, or a pedagogical interface—not the original movement of thought. This delta-transition is demonstrated in two cases:
*   **The Paris Tea Party:** The guests hear that the priest's first penitent was a murderer, and that the nobleman was the priest's first penitent. They instantly infer the nobleman's guilt. They do not perform three silent internal acts of "premising" and "concluding"; they simply grasp the state transition.
*   **The Detective's Report:** The detective spends weeks collecting chaotic, unclassified details (ash, bank statements, timestamps). Only after the discovery does he write the report, cleaning up false starts and arranging clues into a clean, deductive sequence. The report justifies the conclusion to a court, but it is a retrospective artifact, not a transcript of the search.

### 11.4 Holding the Thread: The Latent Attention Buffer
The deepest challenge Ryle leaves unresolved is the mechanics of cognitive integration: how a thinker holds multiple considerations together without consciously reciting them. When following a story, you attend to the sentence currently being read, yet you also "hold the thread." You do not run through the previous chapters at every second, yet you are instantly ready to notice if a plot rule is broken. 

In our framework, this "thread" is the **latent attention buffer**. It corresponds directly to:
*   **The KV-Cache / Attention Matrix:** In transformer architectures, the model does not recalculate the entire preceding sequence from scratch at every token generation. It maintains a latent history—a compressed attention state that constrains the probability of the next token.
*   **The Structural Invariant:** The "unsaid" acts as a computational anchor, forcing the current description to remain answerable to the prior state without paying the cognitive or computational tax of explicit recitation.

### 11.5 Chain-of-Thought as a UI Artifact
The Rylean critique of the "inner blackboard" applies with devastating force to contemporary AI interpretability—specifically the fiction of **Chain-of-Thought (CoT) prompting**. 

When an LLM outputs a step-by-step reasoning trace ("Let's think step by step..."), AI researchers routinely commit the intellectualist category mistake by treating the generated text as a transparent transcript of the model's inner reasoning. Ryle exposes this as an interpretability illusion:
1.  **CoT is not the computation:** The printed tokens are expressive residues, not the underlying mechanical inference. The actual transition occurs in the high-dimensional latent space—the mathematical execution of attention weights across layers.
2.  **CoT is a Post-hoc Rationale:** The step-by-step text is a decorative user-interface artifact designed to satisfy the human operator's demand for legibility, and an operational conditioning layer that biases subsequent token probabilities.

---

## 12. The Descriptive / Interpretive / Operative Triad

To design and analyze attention-tax systems, we formalize language into three operational registers:

```text
  [ DESCRIPTIVE ]  Renders a world.
        │
        ▼
  [ INTERPRETIVE ] Maps significance inside a cultural/local schema.
        │
        ▼
  [ OPERATIVE ]    Alters the operator's action-space.
```

Consider the utterance:
```text
  "The silk thread is vibrating."
```

*   **Descriptive**: Reports the physical state of a thread.
*   **Interpretive**: Within the spider's *Umwelt*, this vibration signifies "prey captured" rather than "wind draft."
*   **Operative**: Mutates the spider's action-space from rest to attack.

For an AI system:
*   **Descriptive**: "User input contains key phrase 'I want to cancel'."
*   **Interpretive**: Maps phrase to "churn risk" within the business ontology.
*   **Operative**: Mutates the system's action-space to trigger retention discounts, flag account managers, and restrict exit links.

Meaning is never a property of the descriptive register alone:

$$\text{Meaning} = \text{Description} + \text{Interpretive Frame} + \text{Operative Consequence}$$

---

## 13. Application: Prompting and Interface Design

This framework unifies prompt engineering and human-computer interface design under a single cybernetic law:

$$\text{Interface Design} = \text{Prompting for human operators.}$$
$$\text{Prompt Design} = \text{Interface design for machine operators.}$$

```text
  [ Human Interface ] ──► Routes human attention ──► Prevents cognitive overload
  [ Machine Prompt ]  ──► Routes model attention ──► Prevents context collapse
```

A prompt is not a text string; it is a temporary salience architecture designed to control the attention of a probabilistic processor. An interface is not a set of buttons; it is a salience architecture designed to control the attention of a biological processor. Both are attention-routing systems engineered to steer operators through drift.

---

## 14. The Formal Model and The Dialectical Ladder

### The Mathematical Model
Let $O = \langle A, M, P, R, G, \text{Act}, F \rangle$ be an operator, and $S$ be the environment state. A description $D$ is a transformation:

$$D : S \to S'$$

where $S'$ is the environment state as rendered for action.

The **Meaning** of description $D$ is the operational shift in $O$'s action-space:

$$M(D, O, S) = \text{Act}_{\text{after}}(D, O, R, A) - \text{Act}_{\text{before}}(D, O, R, A)$$

The **Attention Tax** ($\text{Tax}$) is the resources spent by $O$ to parse $D$:

$$\text{Tax}(D, O) = \text{Resources required for } O \text{ to parse } D \text{ without error}$$

System failure occurs immediately when the tax exceeds the operator's budget:

$$\text{Tax}(D, O) > A(O)$$

*   **Human Overload**: Cognitive exhaustion, misreading, action collapse.
*   **Machine Overload**: Context loss, hallucination, tool thrashing, instruction drift.

---

### The Dialectical Ladder of Language

We compile the entire semiotic stack into a single evolutionary ladder:

```text
  [ 7. Cybernetic Operator Pragmatics ]  Meaning is attention-costed action in feedback.
                    ▲
  [ 6. Computational Attention ]         Self-attention and context window constraints.
                    ▲
  [ 5. Discursive Governance ]           Foucault/power-knowledge and subject positions.
                    ▲
  [ 4. Thick Interpretation ]            Geertzian webs of significance and context.
                    ▲
  [ 3. Pragmatics / Speech-Acts ]        Wittgensteinian use and performative doing.
                    ▲
  [ 2. Relational Difference ]           Saussurian difference and vector spaces.
                    ▲
  [ 1. Representational Reference ]      Language as a passive mirror of objects.
```

---

## 15. Conclusion: The Attention-Tax Theory of Meaning

Every theory of language identifies a different site where meaning is produced:

*   **Reference Theory**: In the mapping between word and world.
*   **Structuralism**: In the relational differences between signs.
*   **Semiotics**: In the triadic interpretant relation.
*   **Pragmatics**: In rule-bound use.
*   **Speech-Act Theory**: In the performed act.
*   **Anthropology**: In the thickness of the cultural web.
*   **Foucault**: In discursive power and subject formation.
*   **Cognitive Linguistics**: In embodied metaphor.
*   **AI**: In statistical-contextual continuation.
*   **Cybernetics**: In feedback and control.

Our theory synthesizes these frameworks: **meaning happens wherever a bounded operator spends attention to maintain an actionable world.**

The final formula of meaning is operational change:

$$M(D, O, S) = \Delta \text{Action-Space}(O) \text{ produced by } D \text{ inside } S \text{ under attention constraint } A \text{ through feedback } F$$

The meaning of a description is not its reference, but its consequence: the change it produces in what an operator can notice, infer, justify, and do next.

---

### Performed Intentionality and the Descriptive Struggle

To resolve the tension between the public behavior of language and its private understanding, Ryle’s discipline must be integrated with the insights of Iris Murdoch and A. C. Lloyd (from the 1951 *Thinking and Language* symposium). This yields a threefold model of **descriptive adequacy**:

```text
               [ Lloyd's Factual Depth ] (Institutional/Social Fact)
                           ▲
                           │
  [ Murdoch's Inward Adequacy ] ◄───► [ Ryle's Public Criteria ]
      (Descriptive Struggle)              (Conduct Acid Bath)
```

1.  **Murdoch's Inward Adequacy:** Murdoch recovers the "descriptive struggle"—the lived effort to make words answer to the pressure of what is meant, felt, or remembered. Metaphor is not decoration; it is conceptual work performed when literal concepts fail. Thinking is not symbol manipulation, but the search for the description that does not betray the experience.
2.  **Lloyd's Factual Depth:** Lloyd historicizes description, insisting that natural language has historical depth. Classifications (e.g., *shell-shock*) are not static tags; they are dynamic, sedimented instruments shaped by institutional struggle, observation, and revision.
3.  **Ryle's Public Criteria:** Ryle provides the necessary "acid bath," preventing the recovery of inwardness from sliding into private-theatre mysticism. There is no inner glow. The attribution of thought to any operator (human or machine) must be disciplined by public competence, self-correction, and practical conduct.

#### The Synthesis: Performed Intentionality
By bringing these three perspectives together, we define thinking as **descriptive struggle constrained by public criteria**. 

Meaning is not a ghost inside the machine, nor is it a behavioral habit of output generation. It is **performed intentionality**: speech enacted through public instruments (capital) that remains accountable to a remembered pressure, a historical fact, and an active environmental feedback loop. 

Generative AI produces description without need, metaphor without inward pressure, and classification without institutional belonging. The machine is philosophically critical because, by eerie subtraction, it shows us what human thought was doing all along: language becomes thinking only when it is bound to the difficult, answerable labor of descriptive adequacy.

---

### The Core Theses

#### The Dissertation Thesis
> Against representational theories of language, **Cybernetic Operator Pragmatics** argues that signs do not primarily mirror states of affairs but organize attention for situated operators. Extending Wittgenstein’s account of meaning as use within language-games and Geertz’s account of culture as webs of significance, this framework treats description as an operational act: a culturally thick, rule-bound intervention that alters what an operator can notice, ignore, remember, and do within a feedback system. In human systems this cost appears as cognitive load; in AI systems it appears as token burn, context pressure, and tool-use overhead. The problem is formally identical across substrates: every bounded operator must spend attention to maintain a world coherent enough for action.

#### The Knife Thesis
> Wittgenstein tells us: **Meaning is a move.**  
> Saussure tells us: **The move is differential.**  
> Peirce tells us: **The move is mediated.**  
> Geertz tells us: **The move is culturally thick.**  
> Foucault tells us: **The move is disciplined by power.**  
> Cybernetics tells us: **The move feeds back.**  
> AI tells us: **The move costs tokens.**  
> Cognitive load theory tells us: **The move costs mind.**  
> Attention-Tax Semiotics says: **These are the same problem dressed in different skins.**

$$\text{Language} = \text{Culturally inherited attention architecture designed to train operators to make moves inside feedback systems.}$$

---

## References

*   Austin, J. L. (1962). *How to do things with words*. Oxford University Press.
*   Bach, E. (1986). The algebra of events. *Linguistics and Philosophy*, 9(1), 5–16.
*   Bakhtin, M. M. (1981). *The dialogic imagination: Four essays*. University of Texas Press.
*   Derrida, J. (1976). *Of grammatology*. Johns Hopkins University Press.
*   Firth, J. R. (1957). *Papers in linguistics 1934–1951*. Oxford University Press.
*   Foucault, M. (1972). *The archaeology of knowledge*. Tavistock Publications.
*   Gadamer, H.-G. (1989). *Truth and method*. Crossroad.
*   Geertz, C. (1973). *The interpretation of cultures*. Basic Books.
*   Grice, H. P. (1975). Logic and conversation. *Syntax and Semantics*, 3, 41–58.
*   Ha, D., & Schmidhuber, J. (2018). Recurrent world models facilitate policy evolution. *Advances in Neural Information Processing Systems (NeurIPS)*, 2450–2462.
*   Lakoff, G., & Johnson, M. (1980). *Metaphors we live by*. University of Chicago Press.
*   Montague, R. (1970). English as a formal language. *Linguisti di Oggi*, 189–224.
*   Murdoch, Iris, A. C. Lloyd, and Gilbert Ryle. (1951). Thinking and language. *Proceedings of the Aristotelian Society, Supplementary Volumes*, 25, 25-110.
*   Peirce, C. S. (1931). *Collected papers of Charles Sanders Peirce*. Harvard University Press.
*   Ryle, Gilbert. (1954). Thinking and inferring. In *Dilemmas*. Cambridge University Press.
*   Ryle, Gilbert. (1961). Use, usage and meaning. *Proceedings of the Aristotelian Society*, 62, 223–230.
*   Saussure, F. de. (1916). *Course in general linguistics*. Philosophical Library.
*   Shannon, C. E. (1948). A mathematical theory of communication. *Bell System Technical Journal*, 27(3), 379–423.
*   Sweller, J. (1988). Cognitive load during problem solving: Effects on learning. *Cognitive Science*, 12(2), 257-285.
*   Varela, F. J., Thompson, E., & Rosch, E. (1991). *The embodied mind: Cognitive science and human experience*. MIT Press.
*   Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). Attention is all you need. *Advances in Neural Information Processing Systems (NeurIPS)*, 5998–6008.
*   Wittgenstein, L. (1953). *Philosophical Investigations*. Blackwell.
*   Wong, L., Grand, G., Lew, A. K., Goodman, N. D., Mansinghka, V. K., & Tenenbaum, J. B. (2023). From word models to world models: Natural language as a programming language for generative simulations. *arXiv preprint arXiv:2306.12672*.
