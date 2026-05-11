# Synthesis: The Prompter's Archive

> **Species**: synthesis  
> **Scale**: section-weight  
> **Primary Worlds**: [[world-operative-ekphrasis]], [[world-prompt-craft]]  
> **Source Ore**: deep-research-report (15), deep-research-report (16)  
> **Last Revision**: 2026-05-10  

---

## Thesis

Every generative image begins twice: once in the prompter's words and once in the archive's habits. The archive always goes first. Thick prompting is the labor of making the archive go second.

---

## The Argument

Geertz (1973) divides description into thin and thick. A thin description records a contraction of an eyelid. A thick description reconstructs the layered codes — intention, convention, social recognition, parody, rehearsal of parody — that make the contraction legible as a wink rather than a twitch. The thickness is not more words. It is more frames.

Generative AI inherits this problem at the level of infrastructure. When a prompter types "a castle at night," the system does not begin from an empty canvas. It begins from what Steyerl (2023) calls the "mean image" and Meyer (2025) calls "platform realism": the statistical memory of a training corpus optimized for legibility, plausibility, ratings, and consumer expectation. Simonen et al. (2025) demonstrate empirically that "default images" — closely resembling outputs — recur across unrelated prompts when the prompt fails to grip the system. The archive has a center of mass. Thin prompting orbits that center. Thick prompting tries to escape it.

The escape is iterative, not declarative. Oppenlaender (2022–2024) documents prompt engineering as a "co-creative online ecosystem" built from modifiers, experimentation, and community knowledge. PromptMagician (Lin et al. 2024) formalizes the loop: users inspect returned images, identify where the archive bent toward a stock solution, and compose the next prompt against what they learned. PRIP treats the user-preferred image as a "pivot between user language and system language" — an intermediary that translates between what the prompter means and what the model can operationalize. In all these cases, the image is not the terminal product. It is a reply. The image is diagnostic before it is definitive.

Parry's concept of the formula — "an expression regularly used under the same metrical conditions to express a given essential idea" — and Lord's stronger claim that the singer composes in performance through a grammar internalized as habit give this practice an unexpected genealogy. Lord (1960) insists that the oral poet does not move mechanically within formulaic language; comparative oral-poetry scholarship confirms that formulaic style can make each performance distinctive rather than repetitive. The analogy holds at exactly one level: in both Homeric song and generative AI, output emerges through constrained recombination inside a patterned system of inheritance. The archive — whether oral tradition or training corpus — furnishes the grammar. The practitioner — whether singer or prompter — introduces the variation.

The analogy must be controlled. It should not erase the difference between an embodied singer embedded in a living tradition and a stochastic model trained on scraped corpora. Its value lies elsewhere: it reframes generation as variable, world-consistent, and non-identical from instance to instance, rather than as either total freedom or brute repetition. The prompter does not merely request an image. The prompter sets the terms under which a latent visual archive will answer.

Bajohr (2024) names the structural condition. In multimodal AI, text and image are encoded within the same mathematical representation space. The semiotic "otherness" that Mitchell (1994) described — ekphrastic hope as the desire to cross from word to image, ekphrastic fear as the anxiety that the image might consume the word — is mathematically annihilated. Operative ekphrasis names cases in which text no longer merely represents an image but helps execute one. But Bajohr also warns: there is "no outside-model." The prompter operates inside proprietary interfaces, factory settings, and corpora whose composition is never fully disclosed.

Webb (2009) provides the historical anchor. Ancient ekphrasis was not a quiet verbal label attached to a static artwork. It was a rhetorical event: vivid speech whose aim was to bring absent scenes before the eyes of listeners. Ekphrasis was performative from the start — an event in language, addressed to an audience, judged by what it called forth. Prompting revives that logic under computational conditions. The prompter performs for the model as the orator performed for the audience.

Thick prompting, then, is not a metaphorical flourish. It is a defensible synthetic term for a practice that Geertz's method makes legible and that HCI research empirically validates. A thick prompt adds the kinds of determinations that alter what the model can plausibly return: relation instead of isolated object, medium instead of generic look, exclusion instead of passive acceptance, social frame instead of free-floating icon, correction instead of one-shot issuance. A thick prompt does not ask for more. It narrows the field of acceptable inheritance.

The image is feedback. Thick prompting names this unfinished condition: ekphrasis after the image has become a diagnostic return from the prompter's archive.

---

## Entity Index

| Entity | Work | Year | Role |
|--------|------|------|------|
| Clifford Geertz | *The Interpretation of Cultures* | 1973 | Thick description: layered codes, not volume |
| Milman Parry | Formulaic studies | 1930s | Formula as metrically conditioned expression |
| Albert Bates Lord | *The Singer of Tales* | 1960 | Composition in performance; non-mechanical formulaic style |
| Jonas Oppenlaender | Prompt engineering studies | 2022–2024 | Prompting as iterative, community-shaped craft |
| Lin et al. | PromptMagician | 2024 | Interactive visual prompt refinement |
| — | PRIP model | 2024 | Image as pivot between user and system language |
| Hannu Simonen et al. | "Default images" study | 2025 | Empirical proof of default-image recurrence |
| Hito Steyerl | "Mean Image" essays | 2023 | Statistical aesthetics converging toward averages |
| Roland Meyer | "Platform Realism" | 2025 | Generic visuality optimized for platform capitalism |
| Hannes Bajohr | "Operative Ekphrasis" | 2024 | Text/image collapse in multimodal systems; "no outside-model" |
| Renate Brosch | Ekphrasis as literary response | 2018 | Performance over mimesis in digital media |
| Ruth Webb | *Ekphrasis, Imagination and Persuasion* | 2009 | Ancient ekphrasis as vivid speech event, not art-object description |
| W. J. T. Mitchell | *Picture Theory* | 1994 | Ekphrastic hope/fear/indifference |
| Murray Krieger | *Ekphrasis: The Illusion of the Natural Sign* | 1992 | The natural sign as impossible horizon |

---

## Cross-Links

- [[concept-thick-prompting]] — the concept this synthesis expands
- [[concept-platform-realism]] — what thin prompting surrenders to
- [[concept-viscosity]] — thickness as deliberately introduced viscosity
- [[threshold-generation-gate]] — the gate the diagnostic return comes through
- [[entity-geertz]] — methodological source
- [[entity-ha-schmidhuber]] — the world-model architecture that follows in SYNTH-02
- [[distinction-thick-thin]] — the structural distinction this synthesis operationalizes

---

## What This Synthesis Does for the Paper

This synthesis replaces Watson's current 222-word thick-prompting section with a ground-up build that:
1. Opens on the archive's priority over the prompter (not on a definition)
2. Grounds the thin/thick distinction in Geertz's actual method (twitch/wink)
3. Provides three empirical anchors: Simonen (defaults), PromptMagician (refinement loops), PRIP (image-as-pivot)
4. Introduces the Parry/Lord analogy as a genealogy of constrained variation
5. Terminates on "the image is feedback" — handing off to the shield section

**Word count**: ~680. **Named sources**: 14. **Citations per 100 words**: 2.06.
