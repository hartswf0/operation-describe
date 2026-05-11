# BULKHEAD 03 — Prompting as Performance and Thick Description

> **Author**: Jay (primary) + Watson (extension)
> **Word count**: Jay ~480w + Watson ~220w = ~700w total
> **Function**: Jay establishes the performative character of prompting, links it to *progymnasmata*, introduces Geertz/thick description, coins "thick prompting." Watson extends with empirical evidence, the archive-as-first-mover claim, and "image is feedback."

---

## PART A: JAY'S TEXT

Prompting is a process, even if it involves only such cycle of word to image. In fact, the process is so simple that users seldom stop after one cycle. They either refine the first prompt or create a different image with a new prompt. While prompting may have the practical goal of producing usable images for a variety of commercial or casual purposes, the simplicity of the process vastly expands the number of those who can produce such images. The emphasis shifts to process and participation. In this way, operative ekphrasis recalls the ancient rhetorical tradition of the progymnasmata. That tradition emphasized performance. Ekphrases were designed to be part of an oration, to be delivered before an audience and appreciated in the moment. The theory of ekphrasis in the twentieth century emphasized the finished product, the poem, not the process of its making, a well-wrought urn, as critic Cleanth Brooks put it, in a reference to perhaps for the most famous English language ekphrasis, Keats' "Ode on a Grecian Urn."

As ekphrastic prompting has developed into a community of practice, the way prompts are crafted has become more elaborate, for image generation as well as for text and coding. A skilled practitioner does not stop with a single short phrase. As we noted, they prompt iteratively to refine the result. In multimodal systems, prompters may deploy images to generate other images. Prompts can be data files (in json format), scripts or even code. Even before generative AI, digital media theorists were arguing for the multimodality or intermediality of digital ekphrasis (Brosch 2018b) as well as for ekphrasis as performance (Brosch 2018a). Metaprompting is already an established term for the practice of writing prompts that prompt prompts. The term and much of the research have been applied to LLMs that output verbal responses to verbal prompts (Zhang Yuan et al 2025). But metaprompting can also serve for making prompting images in two or three dimensions (Zhao et al 2024; Ceurstemont 2025).

We suggest the term "thick prompting" to characterize all of these practices, appealing to the anthropologist Clifford Geertz's concept of "thick description" from this introductory essay to his book The Interpretation of Cultures (Geertz 1993 [1973]). Geertz rejected anthropological theories that reduced cultural complexities to functional formulas. He argued for a process of description that acknowledges the complex structures of meaning behind any cultural practice. That complexity means that descriptions need to be "thick": there is always more to say. The process is provisional and potentially endless. Good prompting is also thick. Both thick description and thick prompting are seeking to engage with layers of coding. In the case of thick description, it is the layers of cultural coding that overdetermine any practice. In the case of thick prompting, the coding consists of all the semantic layers that have been absorbed into the weights of the model. To prompt is to probe those layers in order to tease out the artifact. Because the models are probabilistic (not the symbolically coded knowledge structures of earlier AI), the process of interrogating them is always approximate, incomplete, and potentially endless. There is no final perfect prompt.

---

## SEAM POINT — Watson plugs in here

---

## PART B: WATSON'S EXTENSION

Thick prompting is not about length. It is about pressure. A thin prompter names a subject and trusts the defaults. But defaults are what Meyer (2025) calls "platform realism" and Steyerl (2023) calls the "mean image" — the statistical memory of a training corpus shaped by the visual conventions and economic incentives of the platforms that host it. Simonen et al. (2026) demonstrate this empirically: when prompts fail to grip the system, default images recur across unrelated inputs. The archive always goes first.

A thick prompter gives the system enough organized constraint to move the result toward a specific world of relations. The thick prompter prunes the default. Oppenlaender (2022–2024) documents this pruning as a co-creative ecosystem of iterative experimentation. PromptMagician (Lin et al., 2024) formalizes the diagnostic cycle: users inspect returned images, identify where the model defaulted toward a stock solution, and compose the next prompt against what they learned. Crucially, all prompting occurs through an interface, whether the prompter designed it or not. The interface dictates the affordances. A prompt does not simply conjure an image from the void; it acts upon a language model functioning as a compiler—a *forge*—which must translate semantic intention into executable code or structural constraints to finally render the visual output.

The prompter enters an archive by giving it a symptom, disturbing what it already carries. The ancient orator and the modern prompter face the same design problem: both must produce verbal input that activates a shared representation — cultural memory in the first case, statistical memory in the second — to generate a vivid output. To describe is to undergo the pressure of a reality that resists easy formulation. To generate is to produce probable continuations from learned patterns (cf. Geertz, 1973; Wiener, 1948). Both Homer and the generative model inherit constraints, but only the poet can suffer them. Thick prompting imports the cost of description into the generative apparatus.

The image is not the product. The image is feedback — a diagnostic return from behind a gate the prompter cannot see through (cf. Oppenlaender, 2024b). Thick prompting names this unfinished condition: ekphrasis after the image has become feedback.

---

## CITATIONS IN THIS SECTION

### Jay's citations (Part A)

Brosch, Renate. 2018a. "Ekphrasis in the Digital Age." *Poetics Today* 39 (2): 225–43.

Brosch, Renate, ed. 2018b. "Ekphrasis Today." Special issue, *Poetics Today* 39, no. 2 (June).

Ceurstemont, Sandrine. 2025. "Automating Tools for Prompt Engineering." *Communications of the ACM* 68 (05): 15–17. https://doi.org/10.1145/3715703.

Geertz, Clifford. 1993. *The Interpretation of Cultures*. Fontana Press.

Zhang, Yifan, Yang Yuan, and Andrew Chi-Chih Yao. 2025. "Meta Prompting for AI Systems." arXiv:2311.11482. https://doi.org/10.48550/arXiv.2311.11482.

Zhao, Yiqin, et al. 2024. "Copiloting Creative 3D Scene Modeling and Visualization with Generative Agents." NeurIPS 2024.

### Watson's citations (Part B)

Lin, Han, Weiming Dong, Tianyuan Miao, and Changsheng Xu. 2024. "PromptMagician: Interactive Prompt Engineering for Text-to-Image Creation." *IEEE Transactions on Visualization and Computer Graphics* 30 (1): 295–305.

Meyer, Roland. 2025. "'Platform Realism': AI Image Synthesis and the Rise of Generic Visual Content." *Transbordeur* 9.

Oppenlaender, Jonas. 2024b. "The Cultivated Practices of Text-to-Image Generation." In *Humane Autonomous Technology*. Springer.

Simonen, Hannu, Atte Kiviniemi, Hannah Johnston, Helena Barranha, and Jonas Oppenlaender. 2026. "An Exploration of Default Images in Text-to-Image Generation." In *Proceedings of the ACM CHI Conference on Human Factors in Computing Systems*. ACM.

Steyerl, Hito. 2023. "Mean Images." *New Left Review*, no. 140/141 (April): 82–97.

Wiener, Norbert. 1948. *Cybernetics*. MIT Press.

---

## STATUS

- [x] Jay text extracted verbatim
- [x] Watson Blacksmith text in place with SYNTH-01 weapons
- [x] All citations listed
- [ ] Seam check: Watson's opening ("not about length") must not feel like a contradiction of Jay's Geertz ("thick: there is always more to say")
- [ ] "Geertz 1993 [197x]" — Jay's date bracket needs fixing (should be [1973])
- [ ] Brooks not formally cited in References. Add if needed.
