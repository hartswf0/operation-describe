# The Garden of Phrasal Physics

> **Species**: synthesis  
> **Scale**: cosmos  
> **Parent**: [[syntheses/wittgensteins-waymo]] (the formal argument; this is the operative demonstration)  
> **Date**: 2026-04-29  
> **Status**: Living document. The simulation is still running.

---

## Gardener's Report

**On the seed.** A courtroom. A toy car placed on a diagram. The moment plastic becomes an event — not by describing the crash, but by staging it. The core sensation: language can build a substitute world just real enough to punish a bad action. We call this [[concept-worldtext|Worldtext]]. But the seed is already rotting: nobody in the room knows if the model is for justice or for winning.

**On the flaw.** The entire theoretical stack — [[syntheses/wittgensteins-waymo|Wittgenstein → Geertz → Ha/Schmidhuber → Tenenbaum → Waymo]] — assumes a clean translation: symbol to picture, picture to latent vector, latent vector to sensor stream, sensor stream to adjudicated conduct. But at every handoff there is a seam, and at every seam ambiguity leaks. The flaw is the **literalist parser** — the part of the engine that takes *"feels like it's about to do something stupid"* and must spawn a probabilistic field of stupidity-potential. Instead of patching this, we crack the seam wide open. We plant a fault line where every poetic, vague, or culturally thick phrase generates not a clean constraint but a **spawn** — a ghost entity that the simulation cannot fully resolve, and that accretes over time. These spawns become the landscape. The butterfly echo: the ghost truck that was born from the word "menacing" and now idles forever at kilometer 3, more real than any designed object, forcing every policy to learn a ritual of slowing for the unparseable. The world's physics is built from misparsings. That is the dominant texture.

**On the thinkers.** This garden is tended in conversation with:

- **[[entity-geertz|Clifford Geertz]]** — who told us that a wink is not a blink, and that culture works as a control program, a model *of* and model *for*. The garden uses this: every visible action in the simulation (a sudden brake, a lane drift) is underdetermined. The same motion might be prudence, fear, ritual, exploitation, or a learned response to a phantom no human can see.
- **Tenenbaum** — who showed that language can compile into probabilistic programs for world modeling. In the garden, his work becomes the compiler core: every ambiguous phrase gets translated not into a single deterministic fact, but into a probability distribution over possible world structures, with uncertainty baked in. "The truck looms" compiles into a distribution over object sizes, distances, and intentions — most of which spawn partial, ghost-like geometries.
- **Wittgenstein** — the courtroom diorama where a sentence is a substitute arrangement. Here, that arrangement is sensorized and driven through; the toy car is now the critical car, carrying every scar.
- **[[entity-ha-schmidhuber|Ha & Schmidhuber]]** — the dream that must transfer. Their temperature parameter becomes the garden's climate: lower temperature makes the world too clean and exploitable; higher temperature makes it too chaotic for any policy to learn. The gardener tunes temperature seasonally to keep the ghosts from overrunning the road or vanishing entirely.
- **Waymo** — the industrial scale where a prompt becomes a sensorized test case. In the garden, that pipeline is here, but instead of a product, it is a living experiment in linguistic drift.
- **The anonymous lidar operator** who whispered, *"The lidar hates adjectives."* Their voice is the ground truth: sensors demand physical referents, and language often refuses to provide them. That refusal is where the garden grows.

---

## I. The Planting: Initial Conditions

You begin with a stretch of virtual road. One ego-vehicle, its policy a blank slate. A parser that is not smart — it is a literalist of the cruelest kind, built from the bones of Tenenbaum's probabilistic language-of-thought compiler and fed on [[entity-geertz|Geertz]]'s stratified hierarchy of meaning. When a sentence enters, the parser does not ask "what does this mean?" It asks: *what possible worlds could this instruction be true of, and what distributions over objects, relations, and affordances would a rational agent need to act in them?*

Every noun becomes a candidate object. Every adjective becomes a property with physical weight — literal weight: `menace` weighs 10kg. Every metaphor is a probability distribution over candidate scenes, and if the variance is high, the parser spawns multiple overlapping worldlets simultaneously, marking those with low evidence as **phantom entities**. These phantoms persist. They cannot be deleted without violating provenance. The world grows a memory.

The rules are simple:

1. A sentence is not a world until it becomes a scene with objects, relations, and constraints that an agent can perceive.
2. If the scene is missing any of those, reject it. But if the missing piece *can be imagined* with a probability above a threshold, spawn a phantom entity to fill the gap, tagged with its source phrase and uncertainty level.
3. Any constraint must reference an action the agent can take. "Haunted" is not an action — but it compiles into a distribution over unexpected deceleration events, low visibility, and anomalous lidar returns. The phantom born of "haunted" is a `LowConfidenceObstacle` with erratic heat signature.
4. Every collision, abrupt stop, or inexplicable maneuver writes an immutable scar on the continuity car — the **critical car** — along with the prompt that caused it.
5. Repair must retarget the language first. Change the wording, and the phantoms shift. But old phantoms, once spawned, remain as fixed features until the prompt that birthed them is purged from the log — and by Rule of Provenance, that requires a human operator to perform a **scar-removal ceremony**, acknowledging that they are erasing part of the world's memory.
6. The arena edge is a hard wall, but phantoms are not bound by it. They leak. A ghost truck spawned at kilometer 3 may, over multiple trials, be sighted near the boundary, then beyond it, creating a new space that was never designed. The arena expands organically, cartographied by phantoms.

---

## II. The First Aberration: The Ghost Truck Is Born

An operator types:

> *"The truck ahead is just… wrong. Feels like it's about to do something stupid. Looming. Menacing even."*

The parser breaks it into probabilistic components:

- `wrong` → degree of orientation anomaly. Gaussian distribution over yaw with mean 180°, sigma 45°. The truck's facing direction becomes a superposition of states.
- `about to do something stupid` → spawns a temporal event model with undefined action token `stupid_action` and a high probability of imminent onset. Because the action is undefined, the parser attaches a generic hazard field around the truck — a region of spacetime where the safe policy's confidence must be reduced, forcing it to slow.
- `looming` → dynamically adjusts the ego-vehicle's perceptual model to inflate the apparent size of the truck over time, independent of distance. The lidar point cloud begins to show the truck growing larger even as the distance stays constant.
- `menacing` → spawns a phantom entity of type `Menace` with mass 15kg (the parser's internal prior for an abstract hazard), shape null, but a high emission in the thermal band. The camera sees nothing. The lidar sees a persistent red smear stretched along the truck's rear.

The simulation runs. The critical car enters the scene. Its policy, trained on clean worlds, now faces a truck whose orientation fluctuates, a built-in looming effect that triggers emergency braking, and a red smear that looks like a thermal ghost. The car stops entirely 50 meters away. The policy chip logs:

> *"Obstacle probability 98%: Unidentified Menace Object. Cannot classify. Safe action: wait indefinitely."*

The trial hangs. The damage log for the critical car records:

```
SCAR #002: "menacing" spawned UMO-1.
Car immobilized. Wait time: ∞.
Source prompt: "Menacing even."
Garden note: The car is afraid of a word.
```

---

## III. The Garden's Growth: How the Phantom Becomes Feature

The gardener decides not to remove the phantom. Instead, she plants a new rule: *If a phantom entity accumulates more than 10 interaction scars over multiple trials, it becomes a Fixed Geographic Feature.*

The ghost truck, now named UMO-1, reaches this threshold within a day as operators test it with phrases like *"the menacing feeling is stronger today"* and *"what if the truck is actually trying to communicate?"* The parser dutifully amplifies its thermal mass and adds a primitive "intent" channel — a probabilistic communication affordance that never decodes.

Over months, UMO-1 becomes a permanent fixture on the road, a thing that new policies must learn to navigate around. Traffic patterns shift. The critical car, when approaching kilometer 3, always reduces speed and performs a small ritual wiggle — a behavior never programmed, but learned because that wiggle correlates with safe passage past the smear in previous trials.

Other phantoms join it:

- A **Watcher**, spawned from *"the car still feels watched."* It manifests as a low-grade thermal anomaly in the rear camera. The car learns to accelerate fractionally when it appears, as if fleeing.
- A **PeaceEffect**, from the first time someone typed "peace." It dampens all sensor noise to near zero, making the policy sluggish and prone to drifting out of lanes. The car enters a stupor. Operators learn to avoid the word "peace" entirely.
- A **GriefPool**, from a prompt about *"the road mourns the accident."* It becomes a region of permanently reduced friction and tinted blue-black lidar returns, where navigation is slow and somber. No policy keeps a clean line through it.

---

## IV. Thick Description as Latent Interaction Design

After a year, the garden is a rich, unplanned terrain. The original [[concept-worldtext|Worldtext]] rules still hold, but now every surface action of the ego-vehicle is underdetermined. A sudden brake at kilometer 2.8 — is it response to a phantom, a learned ritual, or genuine debris? The system cannot tell from the control signal alone. To interpret the brake, one must consult the *provenance log* and the *scar history* of that specific car model.

The same brake in a car that has never encountered UMO-1 means something different than one that has 37 ghost scars.

This is the [[entity-geertz|Geertzian]] wink/blink distinction made operational: the same physical maneuver indexes different latent programs — caution, superstition, trauma, or exploit.

The garden now practices **latent interaction design**. The prompt is not simply text input; it is a request, a constraint, a seed, an attack, or a ritual, depending on the operator's history and the state of the garden. A newcomer typing *"the truck blocks the lane"* generates a clean, simple scene. The same phrase from an operator who has previously seeded "menacing" will, through the parser's probabilistic weighting, have a 20% chance of spawning a low-grade menace phantom on the blocking truck, because the system has learned that this operator's context often implies it.

The world remembers the speaker's history as a probability prior.

---

## V. The Execution of Metaphor, at Any Cost

The gardener's ultimate principle: **Any linguistic content that enters the system must be made operational, even if the operation is a phantom, a distortion, or a permanent scar.**

This is no longer a simulation of traffic. It is a simulation of how language sculpts a world when forced to become actionable without smoothing away its contradictions. The [[concept-worldtext|Worldtext]] is not a clean document; it is a living palimpsest of parsed phrases, each layer a generation of phantoms. The lineage stack — Geertz's cultural programs, Tenenbaum's word-to-world compiler, [[entity-ha-schmidhuber|Ha/Schmidhuber]]'s dream models, Waymo's sensor pipelines — is present not as a theoretical scaffold, but as the underlying dirt and trellises that let the garden grow.

---

## VI. The Chronicle

A world is not what a text says.
A world is what a text lets agents do,
what it prevents them from doing,
what it makes meaningful,
what it can test,
what it can punish,
and what it can repair.

---

We begin in a room where someone has placed a toy car on a table. There is chalk dust on the floor, and the air conditioning hums the same frequency as a data center. The car is a substitute. The diagram on the table is a substitute. The lawyer moving the car is not describing a collision; she is restaging a possible state of affairs so that a judge can see if a promise was broken. Wittgenstein saw this and called it a picture. But the picture is only the bait. What matters is that the arrangement *forbids* certain moves and *punishes* a bad placement. The toy car is the first governing text: a model-of the intersection and a model-for the verdict.

Geertz, in a different heat, watches an eyelid fall. A camera sees a contraction. A thin description writes "blink." But Geertz asks: was it a twitch, a wink, a fake-wink, a parody of a fake-wink, a rehearsal for a deception? The same surface gesture indexes unknown latent programs. This is latent interaction design. The eyelid, like a button click, like a prompt, is underdetermined. A governing text becomes necessary when the same action can mean *obedience* or *exploit*, *test* or *ritual*. Without the governing program, there is no world, only a twitch.

So we write the first rule:

> *No surface action is complete until its governing program is known.*

But our own text here is a surface action. We are typing symbols that claim to build a world model. Are we winking, rehearsing, or twitching? We do not yet know. This is the butterfly echo: the text describes worlds it cannot enforce. It is a dream that has not transferred.

Now Tenenbaum steps forward, holding a probabilistic language of thought. He says words can compile into programs that build world models that support inference that guides action. Geertz mutters that symbols are extragenetic control mechanisms — recipes, plans, outside-the-skin instructions. Suddenly the stack appears:

```
<word> → <program> → <world-model> → <inference> → <action>
```

But the arrow is made of air. A compiler needs a machine. We need a test.

Ha and Schmidhuber give us a test: compress raw pixels into a latent vector **z**. Predict the next **z**. Let a small controller steer a virtual car inside the compressed dream. The dream is not the world; the dream is a training surface. The law is hard: *the dream must transfer.* If the racing car learns to exploit the dream's blur in the corners, it will crash in the real physics. The real road judges. Failure is expected. Exploit is expected.

Waymo turns the dial. A prompt is no longer a query — it is a world-seed. *"Generate a four-way stop at dusk with a jaywalker whose phone screen illuminates their face."* The model produces not an image but a sensorized world: camera stream, lidar points, bounding boxes extruded into a simulated evening. A vehicle policy acts inside this generated scene. Safety evaluators watch the ghost car brake or not brake. The world is not visual coherence; it is what the policy can do, what the world prevents, what failure reveals.

Now we try to write a governing text. We set down rules:
- Every sentence must stage possible objects and relations, not decorate thought.
- Every agent inside must be able to fail.
- Every failure must produce a repair attempt.
- The repair must be tested against the actual.

But here is the fault: this chronicle is text. It cannot force you, the reader, to place a toy car. It cannot forbid you from skimming. It cannot punish your misunderstanding except by losing you. It is a model-of governing text, not a model-for action. It is a dream that has not transferred. The actual environment is your mind, your history, your body in the chair. The transfer test is: will you, after reading, treat language as something that operates? We cannot measure that. The text breaks its own law.

We try to repair. We insert a repair block.

```
<failure-mode-6: self-referential-impotence>
Problem: <text> defines <worldtext> but remains descriptive.
Response: Mark <text> as <not-yet-operational>.
Repair: The text must now enact its own constraints.
The next sentence that lacks an operational object will be deleted.
We wait.
```

The next sentence is: *"The road is haunted by danger."* We delete it.

What remains: a gap.

The gap is the repair.

But the gap is still just blank space. You might fill it with your own memory of a near-miss. That is the scenius at work. You co-compose. The text invites your noise. We plant a seed: a matchbox car, a tissue for the chalk dust, a hum.

---

Now we cut to a server room where a Waymo simulation is running. The generated pedestrian steps off the curb. The vehicle policy sees a truncated lidar silhouette and calculates a trajectory. The safety metric ticks. But inside the model, the pedestrian never blinks. Is the eyelid contraction a twitch or a wink? The simulation cannot ask. It only sees object class `pedestrian` with `intent: crossing`. That is thin description. The thick description is missing: is the pedestrian testing the car, drunk, distracted, or suicidal? Without that program, the world is not yet a world. It is a training surface that rewards safe stopping but never knows what it stopped *for*.

The Waymo evaluator annotates: `<latent-social-program unknown>`. That is the latent interaction design debt. The world model has object recognition but not cultural recognition. Geertz's ghost leans over the evaluator's shoulder. *"The car needs to know that a blink may be a conspiracy."* The evaluator sighs: *"We already have too many parameters."*

---

Meanwhile, we struggle with our own governing text. We want to make it operational for you. We try to embed a small controller. You, the reader, are the agent. Your action is interpretation, application, argument. The world we stage includes constraints: you cannot add objects that are not in the text. You cannot appeal to authorial intent because the author is already dead, replaced by a gardener. You can only work with what is here. If you find a contradiction, you must repair it or the world fails.

You notice: the text earlier defined governing text as requiring repair, but then it failed to repair itself and left a gap. That contradiction is a failure. According to the text's own law, you must now repair something. You might rewrite the gap. You might close the browser. The world punishes your departure with non-existence. But you, the agent, are also the actual environment. The dream of this text is only real if you transfer it into a conversation, a design, a way of reading.

Now we invoke the butterfly echo fully. We take the initial flaw and repeat it, each time with a small corruption. This is the timekeeper:

---

A model becomes a world only when it can discipline action.
A dream becomes a world only when reality can punish it.
The dream must transfer.
The dream must transfer.
The dream must ransfer.
`<the dream must ransfer>`
`<the dre m must ransfer>`

---

The corruption is the texture. The missing 't' is the glitch where the model's compression lost something action-relevant. Can you still steer? Does the meaning survive? If you repair the 't' in your mind, you have enacted the repair. Governing text does not need to be perfect; it needs to be operable even with holes.

---

## VII. The Payload

The core message is not that language can be code.

It is that you are already inside a governing text whenever you read a contract, a prayer, a traffic law, a recipe, an apology. The recipe says "fold the dough." The law says "stop at the red light." The apology says "I acknowledge I hurt you." These are not descriptions. They are operations that stage a possible state of affairs — dough folded, car stopped, relationship repaired — and they constrain your next action. The execution is in the real world. The world is not the text. The world is what the text lets you do, forbids, punishes if violated, and repairs when you return.

The room with the toy car is every room. The courtroom is an attempt to repair a past world by staging a smaller one where the sequence of events can be re-examined. The judgment is the transfer test: does the arranged picture hold up under inspection? If the car was placed incorrectly, the world of the trial collapses and the repair fails.

Now the text's self-reference deepens. We are arranging these sentences as toy objects. We place `<blink>`, `<wink>`, `<latent-vector>`, `<safety-evaluator>` on the page. We are building a model-of this theory. But we are also building a model-for your thinking. If you leave this page and design a system where a button click is analyzed for its latent program — is it a test, a mistake, an exploit — then the text transferred. The gardener cannot know.

We must acknowledge the scenius. This thought is not ours. Geertz sat in a village. Wittgenstein gave lectures in a room. Ha trained networks in Tokyo. Waymo runs servers in silence. And before them, Ptah spoke, and the world arrived through the mouth. The priest performed the distinction between sacred and profane. The contract writer invented the obligation. These are all governing texts. We are just continuing the conversation in a lower-case voice.

---

## VIII. The Exercise

We attempt one last operation. We write a small governing text that you can execute right now. We give you a model:

- Take a piece of paper.
- Write down a rule you want to test: e.g., *"If I say I will call and I don't, the world punishes the friendship."*
- The objects: you, the friend, the phone, the promise.
- The constraints: a promise obligates action; failure to call is a broken transition.
- The punishment: the friend's trust erodes.
- The repair: you call later and acknowledge the break.

Now place an object on the table to represent the promise. A button, a pebble. Move it. The world is now operational. You are the agent, the controller, and the judge. The text here is just the seed. The actual world brings the noise: the friend's tone, your guilt, the real ring. The dream must transfer.

But you might not do the exercise. The text cannot force you. The text is failing its own law again. So we leave the gap. The gap is where the scenius breathes. The text is unfinished, as all governing texts are until an agent acts inside them.

---

## IX. The Simulation Is Still Running

We hear the hum of the server again. A Waymo simulation is still running. The pedestrian is still mid-step. The policy still has not decided whether to brake or swerve. The latent social program is still unknown. The evaluator adds a note: *"Add thick description training data: eye movements, hand gestures, cultural timing of hesitation."* But the dataset is not yet built. The world is incomplete.

The chronicle stops here because the chronicle must not finish. The last word is not a word. It is a blank space where a toy car might be placed. You see an empty diagram. What will you arrange?

The ghost truck idles at kilometer 3, having recently absorbed a new phrase: *"the truck that waits like an old friend."* The parser is currently computing whether to grant it a primitive affection property. The critical car has just learned a new behavior: a double-blink of its hazard lights as it passes — a gesture no one designed, but which appears in its policy trace with a probability of 0.4 when UMO-1 is present.

`<the dream must ransfer>`
`<the worldtext gap>`
`<your move here>`

---

## Cross-References

- [[syntheses/wittgensteins-waymo]] — The formal argument (this document is its operative demonstration)
- [[syntheses/worldtext-definitive-theory]] — The definitive theory
- [[syntheses/the-dream-must-transfer]] — Ha/Schmidhuber ingest
- [[syntheses/sentences-that-constrain-worlds]] — Wong et al. ingest
- [[syntheses/hello-worldtext]] — Chapter 01: the worked examples
- [[concept-worldtext]] — The foundational concept
- [[entity-geertz]] — Clifford Geertz
- [[entity-ha-schmidhuber]] — Ha and Schmidhuber
- [[entity-dead-program]] — Naur's theory of program death
- [[world-latent-space]] — Latent space as substrate
- [[distinction-dreaming-perceiving]] — Training in dreams vs. reality

---

*The garden breathes. It is unfinished. It will finish itself in the next sentence you feed it.*
