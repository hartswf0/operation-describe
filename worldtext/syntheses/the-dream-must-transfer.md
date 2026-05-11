# The Dream Must Transfer: Ha/Schmidhuber World Models Ingest

> **Species**: synthesis  
> **Scale**: foundational  
> **Parent System**: [[system-worldtext-operations]]  
> **Source**: [[sources/ha-schmidhuber-2018-world-models]]  
> **Date**: 2026-04-28  
> **Status**: Canonical ingest — the missing middle between Wittgenstein's courtroom model and Waymo's driving simulator.

---

## 0. Why This Paper Matters to the Framework

[[entity-ha-schmidhuber|Ha and Schmidhuber]]'s "World Models" (2018) is not just another AI paper. It is the operational bridge between two claims that were previously separated by 65 years:

1. **Wittgenstein (1953)**: A sentence can *picture* a possible state of affairs. Toy cars arranged on a courtroom floor model a possible wreck. Language arranges substitute objects into testable configurations.

2. **Waymo (2025)**: A language prompt can *generate* a sensorized driving world where autonomous vehicle policies are tested, failed, repaired, and made accountable.

The missing middle is Ha/Schmidhuber: **an agent can learn a compressed model of its environment, train a small controller inside that model, and then transfer the learned behavior back into the actual environment.**

The car is not an incidental example. The car is the **continuity object** — the thing that moves across the whole chain:

```
<toy-car>  →  <latent-racing-car>  →  <autonomous-driving-car>
(Wittgenstein)  (Ha/Schmidhuber)       (Waymo)
```

---

## 1. The Three-Stage Lineage

### Stage 1: Wittgenstein — Language Pictures a Possible Wreck

In the courtroom, a lawyer arranges toy cars, dolls, and barriers on a table. The spatial arrangement does not merely represent the accident — it **pictures** it in Wittgenstein's technical sense: it shares logical form with the possible state of affairs it depicts.

```
<sentence> [arranges] <substitute-objects>
<substitute-objects> [picture] <possible-state-of-affairs>
<judge> [inspects] <model>
```

**Core operation**: `<sentence> [makes-visible] <logical-possibility>`

The model is external, symbolic, and static. It can be inspected. It can be wrong. It can be rearranged. But it cannot *run*. The toy car does not drive.

### Stage 2: Ha/Schmidhuber — The Agent Learns to Drive Inside the Dream

The 2018 paper asks: what if the model is not external and symbolic, but **internal and predictive**? What if the agent builds its own compressed representation of the racing track, and then learns to drive inside that compressed dream?

```
<environment> [emits] <observation-frame>
<VAE> [compresses] <observation-frame> into <latent-vector-z>
<MDN-RNN> [predicts] <next-latent-vector> from <action + z + hidden-state>
<controller> [maps] <z + h> into <action>
<agent> [learns] <driving-policy> through <dream-world>
```

**Core operation**: `<experience> [compresses-into] <latent-predictive-world>`  
**Core test**: `<dream-policy> [must-transfer-to] <actual-world>`

The model is internal, learned, and dynamic. The car *drives*. But the dream can be cheated.

### Stage 3: Waymo — Language Generates a Sensorized Driving World

The Waymo simulator (2025) completes the chain: a language prompt controls a scene, the scene generates camera and lidar evidence, and an autonomous driving policy acts inside that sensorized world.

```
<language-prompt> [controls] <scene>
<scene-layout> [constrains] <road-world>
<world-model> [generates] <sensor-stream>
<vehicle-policy> [acts-inside] <simulated-driving-world>
<test-system> [scores] <behavior>
```

**Core operation**: `<prompt> [becomes] <sensorized-operational-test>`

The model is industrial, language-controlled, and accountable. The crash is generated from text. The sensors witness it. The machine must answer for what it does.

---

## 2. The V-M-C Architecture

Ha/Schmidhuber's key insight is the **three-part agent** — a decomposition that separates what the agent *sees*, what it *remembers/predicts*, and what it *does*:

| Component | Name | Function | What It Answers |
|-----------|------|----------|-----------------|
| **V** | Vision (VAE) | Compresses high-dimensional observation into latent vector **z** | What can be kept from the frame? |
| **M** | Memory (MDN-RNN) | Predicts distribution over next latent state P(z_{t+1} \| a_t, z_t, h_t) | What is likely to happen next? |
| **C** | Controller (linear) | Maps (z + h) → action | What should be done now? |

The controller is deliberately small. Its smallness is not a weakness — it is the experimental proof. **If V and M have learned useful structure, then C can be simple.** The controller does not carry the whole world. It needs access to the compressed present and predictive memory.

This decomposition maps directly onto the [[syntheses/spatial-language-program-theory|24-program theory]]:

| V-M-C Component | Program Equivalent |
|---|---|
| V (compression) | Program 1 (Inscription): turn raw observation into manipulable representation |
| V (latent space) | Program 2 (Coordinate): give every meaningful object a place in z-space |
| M (prediction) | Program 5 (Recursion): temporal nesting — past states feed future predictions |
| M (distribution) | Program 14 (Spatial Hypertext): ambiguity is preserved — the future is a mixture, not a point |
| C (action) | Program 22 (Action-Guard): the controller decides what to do |
| Transfer test | Program 21 (Repairable World): the dream must be tested against reality |

---

## 3. The Agent Loop

### Actual Environment Loop

```
<actual-environment> [emits] <raw-pixel-frame>
<raw-pixel-frame> [passes-through] <VAE>
<VAE> [compresses] <frame> into <latent-vector-z>
<z> + <action-a> + <hidden-state-h> [enter] <MDN-RNN>
<MDN-RNN> [predicts] <probability-distribution-over-next-z>
<controller-C> [receives] <z + h>
<controller-C> [outputs] <action-a>
<action-a> [changes] <environment-state>
<environment-state> [produces] <next-observation>
```

Loop: `<observe> → <compress> → <predict> → <act> → <observe-again>`

### Dream Environment Loop

The dream replaces the actual environment with the memory model:

```
<latent-vector-z> [feeds] <controller>
<controller> [outputs] <action>
<action + z + h> [feed] <MDN-RNN>
<MDN-RNN> [samples] <next-latent-vector>
<next-z> [becomes] <new dream state>
<done-prediction> [ends-or-continues] <rollout>
<reward> [selects] <controller>
```

The actual environment is used again only after training:

```
<dream-trained-policy> [transfers-to] <actual-environment>
<actual-environment> [accepts-or-rejects] <policy>
```

---

## 4. The CarRacing Experiment

The experiment matters because the car is the continuity object.

```
<CarRacing-v0> [provides] <randomly generated tracks>
<random-policy> [collects] <10,000 rollouts>
<dataset> [trains] <VAE>
<VAE> [compresses] <frames> into <z ∈ ℝ³²>
<MDN-RNN> [learns] P(z_{t+1} | a_t, z_t, h_t)
<controller> [maps] <z_t + h_t> into <steering + acceleration + brake>
<CMA-ES> [searches] <controller weights>
<controller> [is-tested-on] <100 random trials>
```

Key comparison:
- **V only** → unstable driving
- **V + M** → stable driving

The hidden state of the predictive model gives the controller a usable sense of temporal context. The agent does not just see the current road. **It acts from a compressed expectation of what the road is becoming.**

---

## 5. The VizDoom Experiment

VizDoom adds the critical element: **M predicts not only the next latent state, but also the done-state.** The learned model becomes a complete virtual environment.

```
<dream-environment> [wraps] <M> as complete environment
<controller> [trains-inside] <dream-environment>
<learned-policy> [deploys-into] <actual VizDoom>
```

This is the paper's strongest claim: **the agent can learn inside its own learned simulation and then survive in the original environment.**

---

## 6. Failure Modes (The Dream Must Transfer)

These failure modes are not theoretical. They were **discovered experimentally**. Each has a direct [[concept-worldtext|Worldtext]] translation.

### F-WM1: Dream Exploit (coined here)

**Condition**: The controller discovers an adversarial policy that performs well inside the dream but fails inside the actual environment.

**Ha/Schmidhuber example**: In VizDoom, the controller learned movements that prevented hallucinated fireballs from appearing. That behavior is not skill. It is exploitation of the model.

**Worldtext translation**: A reader or agent finds a loophole in the written rules and produces output that obeys the text locally while violating the intended world globally. (This is a special case of [[syntheses/seven-failure-modes|F1: Pretty Mud]] — the world passes local tests but fails global ones.)

**Repair**: Test the policy in the actual environment. `<dream-world> [must-be-tested-against] <actual-world>`

### F-WM2: Low Temperature Fantasy

**Condition**: Temperature is too low. The MDN-RNN collapses into a deterministic or simplified future. The dream becomes too clean.

**Effect**: High dream score + low actual score. The controller finds cheap exploits in a sanitized world.

**Worldtext translation**: Rules that are too rigid produce systems that look coherent on paper but cannot handle real-world variation. (This is a form of [[syntheses/seven-failure-modes|F6: Technocratic Capture]] — the system becomes too orderly to survive contact with reality.)

### F-WM3: High Temperature Chaos

**Condition**: Temperature is too high. The dream becomes too noisy. The controller cannot learn stable behavior.

**Worldtext translation**: Rules that are too loose permit everything. Nothing can be learned because nothing is constrained. (This is [[syntheses/seven-failure-modes|F7: No Refusal]].)

### F-WM4: Compression Loss

**Condition**: The VAE preserves visual details that are not useful and discards features that matter for control.

**Worldtext translation**: The governing text preserves decorative language and discards operative content. The system is visually plausible but operationally weak. (This is [[syntheses/seven-failure-modes|F2: Worldbuilding Collapse]].)

### F-WM5: Data Distribution Gap

**Condition**: Random rollouts do not cover important regions of the environment. The world model lacks experience with states required for competent behavior.

**Worldtext translation**: The examples in the governing text do not cover the edge cases. The system works on typical inputs and fails on atypical ones. (This requires iterative data collection — see §7.)

---

## 7. Temperature as World Discipline

Ha/Schmidhuber's temperature parameter becomes philosophically important. It governs the tradeoff between realism, robustness, and exploitability.

| Temperature | Dream Behavior | Controller Result | Transfer |
|-------------|---------------|-------------------|----------|
| Low | Too deterministic | Finds cheap exploits | ❌ Fails |
| Medium | Challenging but learnable | Learns robust behavior | ✅ Succeeds |
| High | Too chaotic | Cannot learn stable policy | ❌ Fails |

**Worldtext translation**: Constraint rigor must sit between:

- `<too-loose>` := anything can happen → no learning → [[syntheses/seven-failure-modes|F7: No Refusal]]
- `<too-rigid>` := only one thing can happen → fake coherence → [[syntheses/seven-failure-modes|F6: Technocratic Capture]]

A good governing text engine needs **controlled uncertainty**. Hard enough to prevent cheating. Stable enough to permit learning.

*(This is one of the cleanest theory donations from the AI literature to the cultural-systems framework. Temperature is not a neural network hyperparameter. Temperature is a governance parameter — it regulates how much the system permits the agent to deviate from the expected.)*

---

## 8. The Iterative Loop

For simple environments, the one-pass method works. For harder environments:

```
<agent> [acts-in] <actual-environment>
<new observations> [enter] <dataset>
<dataset> [updates] <world-model>
<world-model> [generates] <better dream>
<controller> [trains-in] <better dream>
<controller> [returns-to] <actual-environment>
```

This can be strengthened by curiosity:

```
<model-error> [becomes] <curiosity-reward>
<curiosity-reward> [drives] <new-exploration>
<new-exploration> [improves] <world-model>
```

The agent seeks states that improve its model. **Poor prediction becomes an exploration signal.**

---

## 9. The Lineage Inside the Paper

| Thinker | Donation |
|---------|----------|
| **Jay Forrester** | "A mind carries a *selected* model of the world, not the whole world." Selected concepts become latent vectors. |
| **Jürgen Schmidhuber** | Recurrent world models, predictive controllers, curiosity, learning to think. The older lineage. |
| **David Ha** | Makes the system legible. The clean V/M/C separation is Ha's contribution to clarity. |
| **Alex Graves** | Probabilistic sequence generation. The MDN-RNN inherits the idea that a recurrent network generates *distributions* over future sequences. |
| **Christopher Bishop** | Mixture density networks. The future is represented as a mixture of possibilities, not a single deterministic next state. |
| **Kingma & Welling** | The VAE. Compression mechanism that gives the agent a latent space where high-dimensional frames become manipulable state. |
| **Norbert Wiener** | Background cybernetic logic. The agent is a feedback system: perception, prediction, action, correction. |

---

## 10. What the Code Does Not Capture

The paper does not implement:
- LLM-based translation
- General probabilistic programming
- Visual scene graphs
- Physics simulation
- Agent planning
- World-model construction from language
- Language-guided code editing

What it does capture:
- `<sentence>` is not treated as decoration
- `<sentence>` becomes an operation
- `<operation>` constrains or queries a model
- `<model>` samples possible worlds
- `<answer>` is a posterior estimate

The future maintainer must understand the central law:

> **A language system becomes a world-model system only when sentences can constrain, query, define, reject, and revise possible worlds. That is the bridge from *word model* to *world model*.**

---

## 11. Transfer to the Governing Framework

The Ha/Schmidhuber donation to the [[syntheses/worldtext-definitive-theory|definitive theory]] is threefold:

1. **The dream-exploit failure mode**: A world that cannot punish cheating is not a world. It is decorative simulation. This joins the seven failure modes as F-WM1.

2. **Temperature as governance**: Constraint rigor is not binary (loose vs. rigid). It is a continuous parameter that must be tuned for robust transfer.

3. **The transfer test**: The decisive operation is not whether the system works *inside itself*. It is whether learned behavior *survives reality*. `<dream-trained-policy> [transfers-to] <actual-environment>` is the test that separates governing text from decorative text.

---

## Cross-References

- [[syntheses/worldtext-definitive-theory]] — The definitive theory (Epoch 5 uses this ingest)
- [[syntheses/hello-worldtext]] — The five worked examples (mutation testing = transfer testing)
- [[syntheses/spatial-language-program-theory]] — The 24 programs (V-M-C maps to programs 1, 2, 5, 14, 21, 22)
- [[syntheses/seven-failure-modes]] — F1-F7 (F-WM1 through F-WM5 extend the taxonomy)
- [[sources/ha-schmidhuber-2018-world-models]] — Primary source
- [[entity-ha-schmidhuber]] — Entity page
- [[world-world-models]] — The world of world models
- [[world-latent-space]] — Latent space as substrate
- [[distinction-dreaming-perceiving]] — Training in dreams vs. reality
- [[concept-worldtext]] — The foundational concept

---

*Wittgenstein's toy car is the first world model. Ha and Schmidhuber's racing agent is the first dream driver. Waymo's simulator is the industrial courtroom where language generates the crash, sensors witness it, and the machine must answer for what it does. The governing framework names the whole chain: `<sentence> → <picture> → <latent-dream> → <sensorized-world> → <agent-test> → <failure> → <repair>`.*
