# From Imagetext to Worldtext: Generative AI as Operative Ekphrasis

**Watson Hartsoe & Jay David Bolter**

---

## Abstract

Generative AI platforms use prompts to create images, videos, and interactive media. The act of prompting can be understood as a new form of ekphrasis — the ancient literary practice of vivid description. The crucial difference is that unlike traditional ekphrastic poetry and prose, the ekphrasis of prompting is, as Hannes Bajohr has argued, "operative": the text not only describes an image but generates it, collapsing the traditional distinction between the verbal and the visual. Prompt and image together constitute an imagetext, which W.J.T. Mitchell and others have suggested has always been an imagined goal of ekphrasis. Operative ekphrasis is both familiar and radically new in the way that it configures the relationship of word and image and allows us to revisit prior notions of ekphrasis. It offers a new perspective on what Krieger called the "illusion of the natural sign." It offers an alternate paradigm for ekphrastic representation — a paradigm that favors process over finished product. As generative systems are being extended to create entire immersive 3D environments, the imagetext can become a worldtext, which embodies process. We explore operative ekphrasis, imagetext, and worldtext with reference to what is often regarded as the first ekphrasis in Western literature: Homer's Shield of Achilles.

**Keywords**: ekphrasis, generative AI, imagetext, worldtext, thick description, prompt engineering, context engineering

---

## 1. Introduction

Generative AI systems can be used to create a variety of media forms, including text, images, videos, program code, and interactive environments. The interface for these products is typically a prompt provided by a human agent. If we focus on systems that produce visual artifacts — those offered by OpenAI, Google Gemini, Meta, MidJourney, and others — the most common interface remains a text prompt that produces an image or video. Prompting has become a general practice for millions of users, and the art of effective prompting is now known as promptcraft (Lindley and Whitham 2025). The practice has begun to be studied systematically (Oppenlaender et al. 2024; Liu and Chilton 2023), and systems have been developed that embody or improve on existing practices (Almeda et al. 2024; Brade et al. 2023). As has been noted (Bajohr 2024; Meyer 2023; Verdicchio 2024), this movement from text to image corresponds in an almost uncanny way to ekphrasis, the traditional literary practice of vivid description.

The technology of image generation requires training a generative model on millions or billions of captioned images. The captions are a key component because they allow human users to communicate to the model what image they want produced. The text prompt is the natural, indeed obvious, interface to drive the system. When we say obvious, we do not mean to denigrate the remarkable achievements of the computer scientists who developed probabilistic generative systems. We simply mean that once they had developed the insight of tokenizing text and images and building them into a single unified system of weighted matrices, using text prompts became the obvious interface for generating new images.

It seems highly unlikely that any of these computer scientists thought they were developing a new kind of ekphrasis, yet their interface happened to enact a literary practice that predates generative AI by thousands of years. This coincidence invites us to apply literary history and aesthetic theory to one of the most remarkable developments in the history of digital media. Working from a key insight of Hannes Bajohr, we propose a framework for understanding how promptcraft relates to the history of visual and artistic representation — and, reciprocally, how generative AI can serve as a tool for humanistic exploration. As Bajohr points out, Critical AI can undertake not only to apply critical humanistic theory to new digital technological practices but also to enrich humanistic studies. He calls this "thinking with AI" (Bajohr 2024, 77).

---

## 2. Operative Ekphrasis and the Imagetext

### 2.1 The Ancient Definition

For the Greeks, ekphrasis was a rhetorical practice of evoking a vivid visual scene. Rhetoricians, especially in the Greek-speaking parts of the Roman Empire, set ekphrasis as an exercise for their students in a curriculum called the *progymnasmata*. Four textbook authors spanning four centuries — Theon (1st c.), Hermogenes (2nd c.), Aphthonios (4th c.), Nikolaos (5th c.) — define ekphrasis in nearly identical terms: *logos periegematikos*, "a speech that leads one around, bringing the subject matter vividly (*enargōs*) before the eyes." As Ruth Webb recovered and demonstrated, ekphrasis in antiquity was defined not by subject matter but by effect on the audience: it was a technology for making listeners into spectators (Webb 1999; Webb 2016). Nikolaos famously defines the goal of ekphrasis as "turning listeners into spectators," asserting that the description should "almost" (*schedon*) bring about seeing through hearing (Pich and Squire 2026; Webb 2016).

Critically, the ancient definition was already operative. The orator's speech did not represent a pre-existing visual scene — it *produced* visual experience in the listener's mind. The means were neural (the listener's imagination activated by vivid language) rather than computational (tokens conditioning a denoising process), but the operation was the same: verbal input producing visual output, mediated by a shared representational substrate.

Quintilian explains the mechanism (*Institutio Oratoria* 6.2.29–32): the orator must first conjure the scene in their own mind's eye — must "see it yourself first." Only then will the language "spark a mental impression in the mind of the audience." Webb, drawing on ancient memory theory, explains that the listener's mind is not a blank slate but a "storehouse of images derived from sense perception" — a repository of prior visual experience, organized by cultural convention, that the orator's words activate (Webb 1999, 115). The orator does not transmit images. The orator transmits *coordinates* in the listener's storehouse, and the listener reconstructs the image from local memory.

### 2.2 The Modern Narrowing

In the modern era, the emphasis shifted radically. As rhetorical practice and theory became less culturally important, critics and theorists focused on descriptive passages in poetry and literary prose. In the middle of the twentieth century, the critic Leo Spitzer could simply define ekphrasis without reference to rhetoric at all as "the poetic description of a pictorial or sculptural work of art" (Spitzer 1955). This became the framework for researchers later in the twentieth century, including Murray Krieger (1992), James Heffernan (1993), and W.J.T. Mitchell (1994). A significant body of subsequent literature developed (Clüver 1997; Webb 1999; Elleström 2010; Lindhé 2013; Brosch 2018a, 2018b), some of which addressed the impact of the digital. With the major exception of Webb, this work largely ignored the rhetorical tradition, and until the 2020s none of it took generative AI into account.

The narrowing from "vivid speech that produces seeing" to "verbal representation of visual representation" was a definitional reclassification that concealed the operative core of the ancient practice. Each step — Matz (1867), Bertrand and Bougot (1881), Spitzer (1955), Hagstrum (1958), Heffernan (1993) — subtracted operativity and added representationality. By the time Heffernan defined ekphrasis as "the verbal representation of visual representation," the ancient production-oriented definition had been entirely overwritten.

### 2.3 Bajohr's Operative Ekphrasis

Hannes Bajohr (2024) was among the first literary theorists to note that the prompting of an AI image generator constituted a new form of ekphrasis (see also Meyer 2023; Verdicchio 2024). Bajohr coined the term "operative ekphrasis" to describe the unique capacity that generative AI systems bring to the practice. He distinguishes between traditional computer manipulation of images and the prompting of generative models. These are performative in a new way because the models embed textual encodings derived from captions, descriptions, and metadata associated with images scraped from the web. As Bajohr emphasizes, the process of creating these models collapses in important ways the distinction between text and image, and it is this collapse that makes operative ekphrasis possible.

Bajohr's notion of collapse resonates with W.J.T. Mitchell's essay "Ekphrasis and the Other" in *Picture Theory* (1994, 151–181), written long before machine learning systems were capable of image generation. Mitchell argued that the practice of ekphrasis allows us to understand the complicated and always unstable relationship between text and image. The two were never completely distinct as semiotic systems, and the potential merging of text and image could be seen both as the audacious aspiration of ekphrasis and as its nightmare. The merging would confirm the power of the verbal description to become and therefore control the image it evokes. But at the same time, it would threaten to dissolve the word in the image. What Mitchell calls "imagetext" provokes both "ekphrastic hope" and "ekphrastic fear."

Imagetext is both image and text, which is a fair description of the latent space of an image generation model. In the training process, images and captions are encoded and both contribute to the same large set of weights that constitute the model. When the training is complete, it is impossible to say which particular values constitute the text and which the images; the representations are everywhere in the latent manifold. Prompting can be understood as a process of probing this latent space (Liu and Chilton 2023; Almeda et al. 2024) to tease an image out of all the possible images in the space. The resulting image is almost never an exact replica of any training image; it is an interpolation from among the many similar images the model has absorbed.

Our genealogical evidence suggests that Bajohr is not introducing a new kind of ekphrasis so much as recovering the ancient kind. The ancient definition was already operative — the word produced sight in the listener. The Spitzer narrowing concealed this. Generative AI restores it computationally. The operative turn is a return.

---

## 3. Prompting as Performance and Thick Description

### 3.1 Process over Product

Prompting is a process, even if it involves only a single cycle of word to image. In fact, the process is so simple that users seldom stop after one cycle. They either refine the first prompt or create a different image with a new prompt. While prompting may have the practical goal of producing usable images for commercial or casual purposes, the simplicity of the process vastly expands the number of those who can produce such images. The emphasis shifts to process and participation.

In this way, operative ekphrasis recalls the ancient rhetorical tradition. That tradition emphasized performance. Ekphrases were designed to be part of an oration, to be delivered before an audience and appreciated in the moment. The theory of ekphrasis in the twentieth century, by contrast, emphasized the finished product — the poem, not the process of its making. A well-wrought urn, as critic Cleanth Brooks put it, in a reference to perhaps the most famous English-language ekphrasis, Keats's "Ode on a Grecian Urn." Even before generative AI, digital media theorists were arguing for the multimodality or intermediality of digital ekphrasis (Brosch 2018a) as well as for ekphrasis as performance (Brosch 2018b).

As ekphrastic prompting has developed into a community of practice, prompt craft has become more elaborate. Skilled practitioners do not stop with a single short phrase. They prompt iteratively to refine the result. In multimodal systems, prompters may deploy images to generate other images. Prompts can be data files (in JSON format), scripts, or even code. Metaprompting is already an established term for the practice of writing prompts that generate further prompts (Zhang, Yuan, and Yao 2025). And metaprompting applies not only to text but also to images in two and three dimensions (Zhao et al. 2024; Ceurstemont 2025).

### 3.2 Thick Prompting

We suggest the term "thick prompting" to characterize all of these practices, appealing to the anthropologist Clifford Geertz's concept of "thick description" from the introductory essay to *The Interpretation of Cultures* (Geertz 1993 [1973]). Geertz rejected anthropological theories that reduced cultural complexities to functional formulas. He argued for a process of description that acknowledges the complex structures of meaning behind any cultural practice. That complexity means descriptions need to be "thick": there is always more to say. The process is provisional and potentially endless.

Good prompting is also thick. Both thick description and thick prompting seek to engage with layers of coding. In the case of thick description, these are the layers of cultural coding that overdetermine any practice. In thick prompting, the coding consists of all the semantic layers that have been absorbed into the weights of the model. To prompt is to probe those layers in order to tease out the artifact. Because the models are probabilistic — not the symbolically coded knowledge structures of earlier AI — the process of interrogating them is always approximate, incomplete, and potentially endless. There is no final perfect prompt.

The structural identity between thick description and thick prompting is not merely metaphorical. It can be formalized as a six-layer architecture derived from Geertz's method:

| Layer | Thick Description | Thick Prompt |
|-------|------------------|--------------|
| 1. Visible act | What physically happens | What do you want generated |
| 2. Native meaning | What participants take themselves to be doing | The intended meaning of the output |
| 3. Code | What normative order makes the act intelligible | What style or tradition makes the output legible |
| 4. Audience | Who is watching, recognizing, doubting | Who the output is for and what they expect |
| 5. Stakes | What is really at risk | What is riding on this generation |
| 6. Reclassification | What the act becomes in another setting | How the output will be re-read in a different context |

Layer 6 — reclassification-awareness — is the critical addition. No existing prompt-engineering framework (Liu and Chilton 2023; Oppenlaender 2024; Almeda et al. 2024; Brade et al. 2023) includes it. A thin prompt, like a thin description, reports behavior ("a golden shield with battle scenes"). A thick prompt maps meaning across evaluative frames. Thickness is not verbosity. Thickness is selected context that changes the act's identity across frames.

---

## 4. The Shield of Achilles as Performance and Process

Homer's description of the making of a new shield for Achilles in the *Iliad* (Book 18.478–608) is often invoked as the classical example of literary ekphrasis. We use Homer's text to illustrate how operative ekphrasis follows and diverges from the ekphrastic tradition.

### 4.1 Process, Not Product

As Lessing and later critics pointed out (Lessing 2022 [1766]; Taplin 1980), instead of describing the finished object, Homer describes how the god Hephaestus fashions the shield, scene by scene, as each is located in a different sector. That Homer described the process of making as it unfolds in time was an important point for Lessing, who argued in *Laocoön* that poetry is a temporal medium.

The emphasis on craft and process also makes it tempting to read Homer's description as an allegory for the craft of oral poetry. Just as Hephaestus is crafting a world out of bronze, tin, and gold, so Homer is creating not only Hephaestus's shield but the whole of the *Iliad* from his materials. Homer's materials are the words and formulaic expressions of his oral tradition — expressions developed to suit the requirements of epic verse (dactylic hexameter) while simultaneously capturing essential qualities of the characters and elements of that imagined world (swift-footed Achilles, Hector of the shining helmet, the wine-dark sea).

### 4.2 The Oral-Formulaic System as Generative Model

The oral theory of Homeric composition, proposed by Milman Parry and elaborated by A.B. Lord (Lord 2018 [1960]), demonstrated that Homeric poetry was composed in performance from a repertoire of formulaic expressions — metrical building-blocks honed over generations. The system is probabilistic: no two performances are identical, but all evoke the same world. This is structurally analogous to a generative model: trained on a distribution of prior productions, capable of producing novel outputs that are statistically consistent with the training data but never token-for-token identical.

We propose this analogy (not equivalence): Homeric oral poetry can itself be thought of as a generative system. The system was evolved over generations by poets who fashioned formulaic epithets that suited both metrical constraints and semantic content. A poet trained in the system can then generate a story in the appropriate meter with elements that form the Homeric world. The process was not deterministic, but it was probabilistic. No two tellings of Achilles' wrath would be line-for-line the same, but all would evoke that same world of gods and heroes, combat scenes, and formulaic epithets — bright-eyed Athena and rosy-fingered dawn.

Homer's ekphrasis of the shield was already in this sense produced operatively — generated by a pattern-completing system in real-time performance.

### 4.3 The Shield and the Natural Sign

In the ancient tradition, an ekphrasis is successful if the verbal description can call forth a clear and vivid image in the listener's or reader's mind. As Krieger put it, the verbal description aspires to become a "natural sign," as a picture was assumed to be. He adds: "The narrow, literal doctrine of ekphrasis would seem to require this primitive notion of the pictorial as the naively representational" (Krieger 1992, 12n12). That is, the image called forth would presumably be in a style of pictorial realism.

The generative platforms agree — up to a point. Since pictorial and photographic realism are richly represented in the training data, it is not surprising that an operative ekphrasis can often produce a realistic image of Achilles' shield or the scenes depicted on it. When prompted accordingly, the principal generative AI systems (OpenAI, Gemini, MidJourney) are all capable of a variety of styles, but they default to a small range of popular styles depending on subject matter. For classic ekphrasis, the default is realistic.

As a test, we used Google's Gemini Flash image generator. Our prompt was: "Create the shield described below. Make the image as faithful and detailed as possible," and we included the entire Homeric passage (Book 18, lines 478–608) in the original Greek. The model had no trouble with the Greek. The prompt produced a round bronze shield whose raised figures correspond in general terms, though by no means perfectly, to the scenes described in the passage. Without further instructions, the style defaulted to something between a realistic painted image and a photograph.

Roland Meyer has characterized the common aesthetic of these platforms as "platform realism" — an aesthetic that is fundamentally ekphrastic (depending on the word, containing the trace of the word) and nostalgic in a postmodern way: not so much a longing for the past as for pastness (Meyer 2025). What AI shows us is agonizingly close to the natural sign and yet further than ever. Generative AI produces a result that is an image of images, not a natural sign. We might almost say that what AI shows is the *nostalgia* for the natural sign.

---

## 5. The Shield as Worldtext

As classical scholars have remarked, the shield occupies a position both within and beyond the narrative of the poem. The *Iliad* is a story from the Trojan War that unfolds over weeks in the tenth and final year. The shield does not directly refer to those events; instead, it depicts the whole Homeric world: from the sky and constellations in the center to the Ocean that surrounds the world on the shield's rim. In between are scenes of peace and war, agriculture, a legal dispute, wedding and festive dancing (Taplin 1980). Homer reverses macro- and microcosm: the Trojan War is a moment in the Greek epic universe, but Homer renders that universe on this shield inside that moment.

The description of the shield is ekphrasis. It is imagetext. But we choose it because it also suggests the ekphrastic ambition to encompass a world. We use the shield to gesture toward the concept of the worldtext.

### 5.1 Beyond Two Dimensions

Prior to generative platforms, decades of research in computer graphics, particularly for video games, indicated a cultural desire to move beyond two dimensions. Screen-based games offered 3D game worlds, and virtual reality headsets seemed to fulfill the promise that the player could enter such worlds. But those worlds were created by teams of experts and offered to the player to explore.

Now Google DeepMind with its Genie series and World Labs are offering generative platforms through which a user can bring forth their own 3D world from a text prompt. The ambition is to make the worlds fully interactive and malleable. The imagetext is reimagined as a worldtext. Ekphrastic hope here extends beyond the word as natural sign to something like a neoplatonic faith in the power of the prompt to create a world.

### 5.2 The Context Stack

The worldtext is not merely a bigger imagetext. It is a qualitative shift. The imagetext merges word and image into a single object. The worldtext merges word, image, space, time, interaction, and governance into a single *environment*. The prompt is no longer a description but a **constitution**: it defines not what the image looks like but what the world does, what is possible within it, what constraints apply, what defaults govern.

Even if the user provides only a short verbal prompt, the generator depends on an elaborate set of system prompts that provide context to guide and constrain the model, not to mention sophisticated procedural programming to provide physics and interactivity. Thick prompting is a key aspect of these world model generators.

The shield is the prototype. Homer's shield is not an image — it is a world-specification compressed into five concentric rings. Cosmology at the center. Social order in the middle rings. The Ocean at the rim — the boundary beyond which the world-model has no data. The shield IS a worldtext. It always was. Generative AI makes the worldtext technically executable.

---

## 6. Conclusion

The imagetext has arrived: prompt and image are merged in the latent space of multimodal models. But the imagetext's arrival reveals that the productive tension was never simply between word and image. It was between intent and distribution — between what the describer means and what the substrate defaults to. Without intent the system produces the statistical mean; without distribution the system produces noise. Both forces are required. What varies is the ratio.

And beyond the imagetext, the worldtext waits — not a bigger image but a compiled world, not a description but a constitution, not a prompt but an architecture built from language that does not represent reality but generates it.

Homer already knew. The shield was always a worldtext. We just didn't have the substrate to run it.

---

## References

Almeda, S. G., J. D. Zamfirescu-Pereira, K. W. Kim, P. M. Rathnam, and B. Hartmann. 2024. "Prompting for Discovery: Flexible Sense-Making for AI Art-Making with Dreamsheets." *Proceedings of CHI 2024*, 1–17.

Bajohr, H. 2024. "Operative Ekphrasis: The Collapse of the Text/Image Distinction in Multimodal AI." *Word & Image* 40 (2): 77–90.

Brade, S., B. Wang, M. Sousa, S. Oore, and T. Grossman. 2023. "Promptify: Text-to-Image Generation through Interactive Prompt Exploration with Large Language Models." *UIST 2023*, 1–14.

Brosch, R. 2018a. "Ekphrasis in the Digital Age." *Poetics Today* 39 (2): 225–43.

Brosch, R., ed. 2018b. "Ekphrasis Today." Special issue, *Poetics Today* 39 (2).

Ceurstemont, S. 2025. "Automating Tools for Prompt Engineering." *Communications of the ACM* 68 (05): 15–17.

Clüver, C. 1997. "Ekphrasis Reconsidered." In *Interart Poetics*, edited by U.-B. Lagerroth et al. Rodopi.

Elleström, L., ed. 2010. *Media Borders, Multimodality and Intermediality*. Palgrave Macmillan.

Geertz, C. 1993 [1973]. *The Interpretation of Cultures*. Fontana Press.

Heffernan, J. A. W. 2004 [1993]. *Museum of Words*. University of Chicago Press.

Krieger, M. 1992. *Ekphrasis: The Illusion of the Natural Sign*. Johns Hopkins University Press.

Lessing, G. 2022 [1766]. *Laocoön*. Edited by D. Payne. Random Shack.

Lindhé, C. 2013. "A Visual Sense Is Born in the Fingertips." *Digital Humanities Quarterly* 7 (1).

Lindley, J., and R. Whitham. 2025. "From Prompt Engineering to Prompt Craft." *TEI '25*, 1–12.

Liu, V., and L. B. Chilton. 2023. "Design Guidelines for Prompt Engineering Text-to-Image Generative Models." arXiv:2109.06977.

Lord, A. B. 2018 [1960]. *The Singer of Tales*. 3rd ed. Center for Hellenic Studies.

Meyer, R. 2023. "The New Value of the Archive."

Meyer, R. 2025. "'Platform Realism'." *Transbordeur* 9.

Mitchell, W. J. T. 1994. *Picture Theory*. University of Chicago Press.

Oppenlaender, J. 2024. "A Taxonomy of Prompt Modifiers." *Behaviour & Information Technology* 43 (15): 3763–76.

Oppenlaender, J., R. Linder, and J. Silvennoinen. 2024. "Prompting AI Art." arXiv:2303.13534.

Spitzer, L. 1955. "The 'Ode on a Grecian Urn.'" *Comparative Literature* 7 (3): 203–225.

Steyerl, H. 2023. "Mean Images." *New Left Review*.

Taplin, O. 1980. "The Shield of Achilles Within Homer's Iliad." *Greece and Rome* 27 (1): 1–21.

Verdicchio, M. 2024. "Ekphrasis and Prompt Engineering." *Studi Di Estetica* LII (IV): 59–78.

Webb, R. 1999. "Ekphrasis Ancient and Modern." *Word & Image* 15 (1): 7–18.

Webb, R. 2016. *Ekphrasis, Imagination and Persuasion*. Routledge.

Zhang, Y., Y. Yuan, and A. C.-C. Yao. 2025. "Meta Prompting for AI Systems." arXiv:2311.11482.

Zhao, Y., Y. Shen, S. Petrangeli, M. Gadelha, C. Nguyen, and G. Wu. 2024. "Copiloting Creative 3D Scene Modeling." NeurIPS 2024.
