# Scene: The Shadowplay Installation

> **Species**: scene  
> **Scale**: scene  
> **Parent World**: [[world-prompt-craft]] + [[world-operative-ekphrasis]]  
> **Source**: Lindley & Whitham, "From Prompt Engineering to Prompt Craft" (2025)

---

## The Scene

Cork, Ireland. TEI2024 conference. A darkened room set with a light source, a camera, a computer running StreamDiffusion, and two screens. Participants are instructed to cast shadows on a surface. The camera captures the shadow; the AI transforms it. The output appears on the main display at 1fps, then 12fps in V2.

**The actors**: Conference attendees. Some follow instructions (cast shadows). Many step directly in front of the camera, disrupting the "light prompting" protocol. The disruption produces "aesthetic and interesting results."

**The atmosphere**: Constant anticipation. The connection between body movement and AI output is evident but unpredictable. "Striking and grotesque imagery" appears without warning. The audience is simultaneously in control and not in control.

**The threshold**: When the prompt includes "Lotte Reiniger" — a pioneer of shadow animation who died in 1981 — the aesthetic snaps into coherence: playful, dark, silhouette-like. This single entity name navigates the latent space to a legible region. Without it, the default was **war photography** — because high-contrast monochrome images in the training data are predominantly war images. The model's cultural viscosity defaulted to atrocity (like Auden's shield).

**The twist**: Participants' bodies ARE the prompt. The "text box" is bypassed. The input modality is gestural, somatic, embodied. This is the cosmos's **Void 3 (the Body)** partially illuminated: the body as prompt surface.

## What This Scene Contains

- **Infrastructure**: StreamDiffusion server, camera-to-model pipeline, TouchDesigner network
- **Flow**: Body movement → shadow → camera capture → AI transformation → screen display → participant reaction → adjusted movement
- **Memory trace**: Lotte Reiniger (1899–1981) persists as a stylistic attractor in the training data, reachable through her name
- **Governance**: The "meta-prompt" constrains the possibility space; the facilitator edits it live during the exhibition
- **Conflict**: Legibility vs. chaos — the "fixed seed" (stable but boring) vs. "random seed" (exciting but uncontrollable) trade-off

## Cross-Links

- [[concept-viscosity]] — the model's default to war photography = cultural viscosity toward violence
- [[concept-platform-realism]] — without "Lotte Reiniger," the model converges to its training distribution mean
- [[concept-context-stack]] — the meta-prompt = L1 (system instruction); the fragment cards = L5 (user instruction)
- [[fragment-audens-barbed-wire]] — the model's default is barbed wire, not olive trees
- [[ritual-prompting]] — the act is ritualized: light, shadow, transformation, revelation
