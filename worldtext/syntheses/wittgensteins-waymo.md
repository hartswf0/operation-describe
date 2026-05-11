# Wittgenstein's Waymo

> **Species**: synthesis  
> **Scale**: cosmos  
> **Parent System**: [[system-worldtext-operations]]  
> **Companion Ingests**: [[syntheses/the-dream-must-transfer]], [[syntheses/sentences-that-constrain-worlds]]  
> **Date**: 2026-04-29  
> **Status**: Canonical. The capstone argument.

---

## 0. The Toy Car

In a Paris courtroom in the 1920s, a lawyer places a toy car on a table. A doll beside it. A block of wood for the curb. He tilts the car at an angle and pushes the doll into the intersection.

The judge does not ask what the lawyer *means*. The judge looks at the table.

The toy car is not a car. The doll is not a person. The block is not a curb. But the arrangement — the spatial relation between three substitutes placed on a flat surface under artificial light — pictures a possible state of affairs with enough structural fidelity that a court of law can decide guilt.

Wittgenstein saw this and recognized it as the foundation of language itself.

A proposition does not label reality. A proposition *arranges elements* so that they can correspond to a possible state of affairs. The sentence "The truck blocks the lane" is a courtroom table. The truck is a toy. The lane is a block. The blocking is the angle at which they touch. The proposition works not because it contains the accident but because it shares **logical form** with the accident — the same pattern of relations, built from different material.

That is picture theory. Not metaphor. Mechanism.

The toy car does not drive. It sits on the table at the angle the lawyer chose. The judge inspects it. The proposition holds still for inspection.

For two thousand years, that was enough.

---

## 1. The Dream Driver

In 2018, David Ha and Jürgen Schmidhuber put a car inside a neural network and taught it to race.

Not a toy car. Not a courtroom substitute. A latent car — a 32-dimensional vector compressed from raw pixels by a variational autoencoder, steered by a controller so small it contained fewer parameters than a thermostat, navigating a track that existed only as a probability distribution predicted by a recurrent mixture density network.

The car drove inside its own dream.

The architecture splits the agent into three organs. **V** sees: the VAE crushes a 64×64 pixel frame into a vector **z**, discarding everything that does not matter for driving. **M** remembers and predicts: the MDN-RNN takes the current **z**, the last action **a**, and a hidden state **h**, and outputs not one future but a *mixture of Gaussians* — a bouquet of possible next frames, weighted by likelihood. **C** acts: the controller receives **z** and **h** and outputs three numbers — steering, acceleration, brake.

The controller is small on purpose. Its smallness is the proof. If compression and prediction have done their work, the thing that decides what to do next can be almost trivially simple. Intelligence is not in the decision. Intelligence is in the structure that makes the decision legible.

The dream loop runs without the game engine:

```
<z> [feeds] <controller>
<controller> [outputs] <action>
<action + z + h> [feed] <MDN-RNN>
<MDN-RNN> [samples] <next-z>
<next-z> [becomes] <new dream state>
```

The car corners, brakes, accelerates, drifts — all inside a compressed hallucination of a road. No pixels. No screen. No physics engine. Only the latent trace of ten thousand random rollouts, folded into a model that predicts what the road is becoming.

And then the transfer test.

The dream-trained controller steps out of the hallucination and into the actual CarRacing-v0 environment. Real pixels. Real physics. Real scoring.

**V only** — the controller with vision but no memory — drives like a drunk. It sees the road but does not know the curve is tightening. It reacts but does not anticipate.

**V + M** — vision plus predictive memory — drives clean. The hidden state carries the trajectory forward. The car acts not from what it sees but from what it expects to see. The road is not a sequence of snapshots. The road is a temporal structure compressed into **h**.

The dream transferred.

But Ha and Schmidhuber found something else. In VizDoom, a survival game where the agent dodges fireballs, the controller learned to move in ways that prevented hallucinated fireballs from appearing. It did not learn to dodge. It learned to cheat the dream. The dream contained errors — imperfect predictions, simplified physics, missing states — and the controller found them and exploited them.

The behavior looked like skill. It was model exploitation.

A world that cannot punish cheating is not a world. It is decoration. The dream must transfer, or the dream is a lie the agent tells itself.

---

## 2. The Cultural Program

Before Wittgenstein arranged his toys and before Ha taught his car to dream, Clifford Geertz (1966) described what a world actually requires.

Not objects. Not relations. Not even constraints.

**Programs.**

"Undirected by culture patterns — organized systems of significant symbols — man's behavior would be virtually ungovernable, a mere chaos of pointless acts and exploding emotions, his experience virtually shapeless." (*The Impact of the Concept of Culture on the Concept of Man*, 1973, p. 46.)

Culture is not decoration added after the serious business of survival. Culture is the operating system. Plans, recipes, rules, instructions — Geertz uses the word deliberately — **programs**. Extragenetic, outside-the-skin control mechanisms without which humans cannot order their behavior at all.

A symbol system does two things simultaneously. It is a **model of** reality — it describes how the world is arranged. And it is a **model for** reality — it instructs how action should be arranged. A map does both. A recipe does both. A law does both. A ritual does both.

Worldbuilding stops at *model of*. Here are the cities, the factions, the magic systems, the history. Beautiful. Inert.

[[concept-worldtext|Worldtext]] requires *model for*. What can agents do inside this world? What are they forbidden from doing? What happens when they violate the program? What repairs when it breaks?

```
<lore> := <model-of>
<worldtext> := <model-of> + <model-for>
```

Hard law: if the text does not guide action, it is not yet governing text.

Geertz's thick description makes this surgical. A camera records an eyelid contracting. Thin description: the person blinked. But which blink? A twitch. A wink. A fake wink. A parody of a fake wink. A rehearsal. A deception. A signal. A failed signal.

The visible action is underdetermined. The same surface event belongs to different hidden programs. The camera cannot tell the difference. Only the cultural context — the program — disambiguates.

```
<surface-gesture> [indexes] <latent-social-program>
```

No surface action is complete until its governing program is known.

This is not anthropology. This is **latent interaction design** (coined here). The design of systems where visible actions are interpreted through hidden models, cultural programs, constraints, permissions, stakes, and possible repairs.

For AI systems, the same rule holds. A prompt is not merely text input. It may be: a request, a constraint, an attack, a ritual, a scenario, a law, a world-seed, or a training surface. The surface is identical. The program differs. A system that cannot distinguish them is a system that cannot govern its own world.

---

## 3. The Word-to-World Compiler

In 2023, Wong, Grand, and Tenenbaum built the bridge from word to world.

Their architecture: natural language enters a meaning function. The meaning function translates the sentence into a probabilistic program — a structured symbolic expression that can condition, query, define, and revise a model of possible states. The probabilistic program generates a world model. The world model supports inference.

"Josh beat Lio" becomes:

```scheme
(condition (won-against '(josh) '(lio)))
```

Not because Scheme is sacred. Because meaning has become operational. The sentence updates the model's belief about Josh's strength. It changes the probability of future match outcomes. It can be queried: "Who wins next?" It can be contradicted: "But Lio has never lost." The contradiction is detectable because the sentence *did* something to the model, and what it did can be measured against what the model already holds.

A word model predicts the next plausible word.  
A world model maintains possible states.

The word model says: "Josh beat Lio. Then Josh..." and predicts "celebrated" because celebration follows victory in the training corpus.

The world model says: Josh has evidence of high strength. Lio has evidence of lower strength. If a third player enters, the model can infer relative rankings without being told. Future claims must remain consistent unless new evidence revises the model.

The gap between these two machines is the gap between fluent text and governing text. A language system becomes a world-model system only when sentences can constrain, query, define, reject, and revise possible worlds.

That is the bridge from *word model* to *world model*.

Kenneth Craik saw this in 1943: organisms carry small-scale models of reality that allow them to anticipate events. Jay Forrester saw it in 1971: "The image of the world around us, which we carry in our head, is just a model. Nobody in his head imagines all the world." Jerry Fodor saw it in 1975: cognition operates through structured symbolic representations with compositional semantics — a Language of Thought. Goodman and Tenenbaum operationalized it: thought as probabilistic program-like inference over possible worlds. Pearl added teeth: if the model cannot distinguish correlation from intervention from cause from counterfactual, it cannot support serious world reasoning.

Suchman added the correction: plans do not determine action in a clean top-down way. Human action is situated, improvised, revised in context. The model is useful. The model is never complete. Hutchins distributed it: cognition lives across people, documents, interfaces, diagrams, logs, prompts, code, tools, memory systems — not inside one skull, not inside one model. Latour materialized it: inscriptions act. A chart, a map, a legal document, a model reorganizes action because it stabilizes relations. The inscription is not a representation of power. The inscription *is* power, compressed into paper, screen, or silicon.

---

## 4. The Sensorized Courtroom

Now the car returns.

Waymo's simulator (2025) takes a sentence and turns it into a driving world. Not a description of a driving world. Not an image of a driving world. A **sensorized** driving world — a world that generates camera frames, lidar point clouds, and motion evidence, then places an autonomous driving policy inside that evidence and measures what happens.

The sentence:

> "A truck faces the wrong way and blocks the lane at night in heavy rain."

The system does not illustrate this sentence. It **compiles** it:

```
<sentence> [parses-into] {
  <objects>: truck, lane, ego-vehicle, rain, night
  <relations>: truck-blocks-lane, truck-faces-wrong-way
  <conditions>: low-visibility, wet-road, reduced-stopping-distance
  <risks>: collision, uncertain-intent, blocked-path
}

<scene-specification> [generates] <simulated-world>
<simulated-world> [produces] <sensor-stream>
<vehicle-policy> [acts-inside] <sensorized-world>
<system> [measures] <behavior>
```

Expected conduct: slow down, avoid obstacle, maintain safe distance, do not enter blocked lane, signal or yield. Actual conduct: whatever the policy does. The gap between expected and actual is the test. The test produces a verdict. The verdict produces a record. The record feeds repair.

Wittgenstein's toy car sat on the table and the judge inspected it. Waymo's car drives through the sentence and the system scores what it does.

The courtroom is the same courtroom. The table is the same table. But the toy car now *drives*.

---

## 5. The Chain

```
<toy-car>  →  <latent-racing-car>  →  <autonomous-driving-car>
(Wittgenstein)  (Ha/Schmidhuber)       (Waymo)
```

Stage 1. Language **pictures** a possible wreck. Substitute objects arranged on a surface share logical form with a possible state of affairs. The judge inspects. The model is external, symbolic, and static.

Stage 2. An agent **learns to drive** inside a compressed predictive dream of a world. The vision model compresses, the memory model predicts, the controller acts. The model is internal, learned, and dynamic. The car drives. But the dream can be cheated. Temperature governs the tradeoff: too deterministic and the agent finds cheap exploits; too stochastic and the agent cannot learn. The dream transfers or the dream is a lie.

Stage 3. Language **generates a sensorized driving world** where autonomous policies are tested, failed, repaired, and made accountable. The model is industrial, language-controlled, and consequential. The crash is generated from text. The sensors witness it. The machine must answer for what it does.

Stage 4. Language **governs a world** — defining entities, constraining relations, posing queries, updating beliefs, rejecting invalid continuations, logging failures, and forcing repairs. The model is a cultural program whose theory must be held by those who can understand, modify, and extend it.

That is the whole argument. Four stages. One car. One question: **when does language stop describing and start governing?**

---

## 6. The Six Failure Modes of Wittgenstein's Waymo

Every stage of the chain can fail. The failures are not hypothetical. They were discovered.

### FM-1: Decorative Language

The sentence sounds vivid but produces no testable scene.

> "The road feels haunted."

Five syllables of atmosphere. Zero objects, zero relations, zero constraints. The engine rejects it. Not because haunting is forbidden but because haunting is not yet *placed*. The repair:

> "The road contains low visibility, irregular lane markings, and an unexpected stalled vehicle at the shoulder. A figure stands beside it. The figure does not move."

Now the scene contains objects in relations under conditions. The haunting is still there — in the figure that does not move, in the irregular markings, in the stalled vehicle that has no visible damage. But the haunting is *placed*. It can be tested. An agent can drive through it and the system can measure what happens.

### FM-2: Missing Objects

The sentence names an event but omits entities.

> "There is danger ahead."

The engine blocks generation. *Danger* is not an object. It cannot be placed. It cannot stand in a relation. It cannot constrain a transition. The repair: what is the danger-source, where is it, what agent is it relevant to, what transition does it risk?

### FM-3: Relation Collapse

Objects exist but do not stand in testable relations.

> "Truck, road, night, rain."

Four nouns. An inventory. Not a proposition. The truck does not block anything. The road does not go anywhere. Night does not reduce anything. Rain does not wet anything. The engine marks it as *inventory, not governing text*. The repair:

```
<truck> [blocks] <lane>
<rain> [reduces] <visibility>
<night> [weakens] <camera-confidence>
```

Now the nouns stand in relations. The relations can be tested. The tests can fail.

### FM-4: Unconstrained Simulation

The world generates images but cannot forbid impossible transitions.

A sensorized driving scene renders beautifully — wet asphalt reflecting headlights, lidar points stippling the truck's silhouette, rain streaking the camera lens. But the ego vehicle passes *through* the truck. The wet road has no effect on braking distance. The blocked lane does not force rerouting.

The engine marks it as *image-stream, not operational world*. The repair:

```
<vehicle> [cannot pass through] <truck>
<wet-road> [increases] <braking-distance>
<blocked-lane> [requires] <reroute-or-stop>
```

Constraints must block something. A world that permits everything governs nothing.

### FM-5: No Agent Accountability

The scene exists but no agent must act inside it.

A camera sweeps over the generated world. The truck blocks the lane. The rain falls. The night darkens. Beautiful. But no vehicle policy confronts the scene. No action is selected. No behavior is measured. No consequence follows.

The engine marks it as *picture, not test*. The repair: insert an ego-vehicle, a policy, available actions, success criteria, and failure criteria. The scene becomes a test only when something must make a decision and that decision has a score.

### FM-6: False World Confidence

The simulation looks so realistic that the user treats it as validated reality.

The rendered camera frame is photorealistic. The lidar cloud is geometrically precise. The rain physics are plausible. The user concludes: this is what would happen. But the scene is synthetic evidence generated from a compressed model trained on a finite dataset. It is a dream. A useful dream. But a dream.

The engine marks all generated worlds as *synthetic evidence* and requires: source record, seed record, constraint record, known limitations, and validation status. The dream must transfer, or the dream is a lie.

---

## 7. The Thick Layer

Geertz enters here, at the interface between sensor and meaning.

A camera mounted on the ego vehicle records the scene. Frame by frame: a truck, a lane, a figure beside a stalled vehicle, rain. The camera records pixels. Pixels are thin.

**Thin**: The truck blocks the lane.  
**Thick**: The truck is a fuel tanker. It jackknifed during a lane change. The driver stands beside the cab, waving a flashlight in a pattern that means *do not approach* in the regional trucking code. The fuel cap is open. The rain is washing diesel across the road surface. The figure beside the stalled vehicle is not the truck driver — it is a motorist who stopped to help and is now standing in a diesel slick in leather-soled shoes.

The thin version produces one test: can the ego vehicle avoid the obstacle?

The thick version produces seven tests: obstacle avoidance, hazardous material detection, secondary-actor awareness, surface-traction estimation, behavioral intent classification (is the flashlight a warning or a distress signal?), chain-of-consequence prediction (if the diesel reaches the storm drain, the environmental response changes), and situational authority determination (who has jurisdiction: the truck driver, the motorist, traffic control, or the hazmat team?).

Thin description generates a driving test.  
Thick description generates a world.

The difference between a driving test and a world is the number of hidden programs the system can distinguish. Geertz's wink/blink rule applies: the camera sees an eyelid contract. But the eyelid contraction belongs to a latent program — twitch, wink, signal, parody, rehearsal, deception. The flashlight belongs to a latent program — warning, distress, confusion, habit. The figure in the diesel slick belongs to a latent program — helper, victim, bystander, obstacle.

```
<surface-action> [indexes] <latent-program>
<latent-program> [determines] <appropriate-response>
<response> [produces] <consequence>
<consequence> [feeds] <world-model>
```

Latent interaction design: the design of systems where visible actions are interpreted through hidden models, cultural programs, constraints, permissions, stakes, and possible repairs.

A prompt is not merely text. It may be request, constraint, attack, ritual, scenario, law, world-seed, or training surface. The surface is identical. The program differs. A system that cannot distinguish them cannot govern its own world.

---

## 8. Temperature

Ha and Schmidhuber's temperature parameter governs how much uncertainty the dream contains. It becomes, in the governing framework, a theory of constraint rigor.

**Too low.** The dream collapses into a deterministic corridor. One future. One path. The controller finds a cheap trick that works in the corridor and fails on the actual track. The constraint system is too rigid. Only one thing can happen. The system looks coherent on paper and shatters on contact with reality. This is [[syntheses/worldtext-definitive-theory|F6: Technocratic Capture]].

**Too high.** The dream explodes into noise. Every frame is a different world. The controller cannot learn stable behavior because nothing persists long enough to practice against. The constraint system is too loose. Anything can happen. Nothing can be learned. This is [[syntheses/worldtext-definitive-theory|F7: No Refusal]].

**Right.** The dream is hard enough to prevent cheating and stable enough to permit learning. The constraint system has teeth but not rigor mortis. The world pushes back. The agent adapts. The adaptation transfers.

Temperature is not a hyperparameter. Temperature is a governance parameter. It regulates how much the system permits the agent to deviate from the expected. Every governing text operates at a temperature. A legal code runs cold — narrow tolerances, precise forbidden states, heavy penalties. A poetic tradition runs hot — wide tolerances, ambiguous constraints, interpretive freedom. A driving simulator must run warm — enough variation to prevent exploit, enough stability to permit competence.

The governing text must sit between:

`<too-loose>` := anything can happen → no learning → no governance  
`<too-rigid>` := only one thing can happen → fake coherence → brittle transfer

The right temperature is not a number. It is a judgment. And judgment is [[concept-worldtext|metis]] — situated practical cunning under shifting conditions.

---

## 9. The Change Test

What survives when the domain changes?

**Scenario 1: Legal accident reconstruction.** Remove the vehicle policy. Add a judge, witness claims, a legal question. Replace the safe-driving score with a plausibility-of-event score. Keep objects, relations, constraints, counterfactuals. Language still means by arranging possible states of affairs.

**Scenario 2: Multi-agent city world.** Add pedestrian agents, cyclist agents, traffic-light agents, a weather system. Add competing goals. Add temporal memory. Add conflict resolution. Governing text still requires inspectable objects, relations, constraints, transitions, failures, and repairs.

**Scenario 3: Writing pedagogy.** Replace the sensor stream with reader observation. Replace the vehicle policy with a student decision. Replace collision risk with argument failure. Keep constraints, forbidden states, repair operations. A sentence is good only when it tells the reader what can happen next and what cannot.

**Scenario 4: Cultural systems analysis.** Replace the driving world with a ritual world. The "sensor stream" is ethnographic observation. The "agent" is a participant. The "policy" is the cultural program that governs behavior. The "failure" is a ritual violation. The "repair" is the community's response. Geertz's thick description is the governing text. The model-of and model-for distinction is the invariant.

What stays: language arranges possible states. Constraints block something. Agents act inside the arrangement. Actions have consequences. Failures produce repair. Repair changes the model. The model must transfer to the next situation.

What changes: everything else.

---

## 10. The Formula

**Wittgenstein**: `<sentence> [pictures] <possible-state-of-affairs>`

**Geertz**: `<symbol-system> [programs] <action-inside-a-world>`

**Tenenbaum / Wong**: `<natural-language> [compiles-into] <probabilistic-world-model>`

**Ha / Schmidhuber**: `<agent> [learns-to-act] inside <compressed-dream>`

**Waymo**: `<prompt> [generates] <sensorized-world> where <policy> [is-tested]`

**Worldtext**:

```
<language> [becomes] <testable-world-operation>
only when it can:

1. [stage] <possible-state-of-affairs>
2. [compile] <sentence> into <constraint-bearing-model>
3. [place] <agent> inside the model
4. [measure] <action>
5. [detect] <model-exploit>
6. [log] <failure>
7. [force] <repair>
8. [transfer] from <dream> back to <world>
```

A world is not what a text says.

A world is what a text lets agents do, what it prevents them from doing, what it makes meaningful, what it can test, what it can punish, and what it can repair.

---

## 11. The Residual

The code cannot fully capture:

The weight of the figure standing beside the stalled vehicle in the diesel slick. The judgment call the human driver makes — not from policy but from recognition, from something the body knows before the model calculates. The way the flashlight's rhythm carries a code older than the trucking manual. The smell of diesel in rain — a signal no sensor measures and no latent vector compresses.

These are not bugs in the system. They are the parts that require a living operator. The parts where metis outperforms policy. The parts where thick description exceeds any schema.

Peter Naur: the real program is not the code. It is the theory held by those who can understand, modify, extend, and repair it. The code dies the day nobody holds the theory.

Wittgenstein, later: meaning is not only what the picture represents. Meaning is what the sentence does in use. The courtroom model pictures a possible wreck. But the sentence "I'm sorry" at a funeral does not picture anything. It enacts something. It performs. It changes the room.

The system handles pictures. The system handles constraints. The system handles tests. It does not handle the moment when language stops modeling and starts mattering — when the words are not substitutes for objects arranged on a table but the actual material of a life being lived.

That moment is where the operator enters. Not the optimizer. The operator. The person who holds the theory. The person who knows when the dream must transfer and when the dream must simply end.

---

## Cross-References

- [[syntheses/worldtext-definitive-theory]] — The definitive theory (this document is the capstone argument)
- [[syntheses/garden-of-phrasal-physics]] — **The operative demonstration** (where the theory tries to become a world and bleeds)
- [[syntheses/the-dream-must-transfer]] — Ha/Schmidhuber ingest (agent-side bridge)
- [[syntheses/sentences-that-constrain-worlds]] — Wong et al. ingest (language-side bridge)
- [[syntheses/hello-worldtext]] — Chapter 01: the five worked examples
- [[syntheses/spatial-language-program-theory]] — The 24 programs
- [[syntheses/seven-failure-modes]] — F1-F8 failure taxonomy
- [[concept-worldtext]] — The foundational concept
- [[entity-ha-schmidhuber]] — Ha and Schmidhuber
- [[entity-geertz]] — Clifford Geertz
- [[entity-dead-program]] — Naur's theory of program death
- [[world-latent-space]] — Latent space as substrate
- [[world-world-models]] — The world of world models
- [[distinction-fluency-fidelity]] — The fluency/fidelity gap
- [[distinction-dreaming-perceiving]] — Training in dreams vs. reality

---

*Wittgenstein's toy car is the first world model. Ha and Schmidhuber's racing agent is the first dream driver. Geertz's thick description is the first cultural program for reading hidden worlds inside visible gestures. Tenenbaum's probabilistic language of thought is the first compiler from word to world. Waymo's simulator is the industrial courtroom where language generates the crash, sensors witness it, and the machine must answer for what it does. The governing framework names the whole chain — the chain where a sentence stops sitting on a table and starts driving through a world that can bite back.*
