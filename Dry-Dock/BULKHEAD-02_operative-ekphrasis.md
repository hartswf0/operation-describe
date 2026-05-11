# BULKHEAD 02 — Operative Ekphrasis and the Imagetext

> **Author**: Jay
> **Word count**: ~590w
> **Function**: Historical genealogy of ekphrasis (ancient → modern narrowing → Bajohr recovery). Introduces operative ekphrasis, text/image collapse in latent space, Mitchell imagetext, ekphrastic hope/fear. Establishes prompting as process.

---

## TEXT

For the Greeks, ekphrasis was a rhetorical practice of describing a vivid visual scene. Rhetoricians, especially in the Greek-speaking parts of the Roman empire, set ekphrasis as an exercise for their students. Ekphrasis was also a generic element in their own rhetorical performances, when public speaking became a significant form of artistic performance. Authors of rhetorical treatises from the Empire period, including Theon (1st century), Hermogenes (2nd), Aphthonios (4th), and Nikolaos (5th), treat ekphrasis as the art of enargeia (Webb, 1999; Webb 2016). In the modern era, the emphasis shifted radically. As rhetorical practice and theory became less culturally important, critics and theorists focused on descriptive passages in poetry and in literary prose. In the middle of the twentieth century, the critic Leo Spitzer could simply define ekphrasis without reference to rhetoric at all as "the poetic description of a pictorial or sculptural work of art." (Webb 1999, 10) This became the aesthetic framework for researchers later in the twentieth century, including Murray Krieger (1992), James Heffernan (2004[1993]), and W.J.T. Mitchell (1994). Since that time, a significant body of literature has developed (e.g. Clüver 1997; Webb 1999; Elleström 2010; Lindhé 2013; Webb 2016; Brosch 2018b), some of which has addressed the impact of the digital, including a special issue of Poetics Today edited by Renate Brosch (2018b). With the major exception of Webb, this work largely ignored that rhetorical tradition of ekphrasis, and until the 2020s, none of it took generative AI into account.

Hannes Bajohr was among the first literary theorists to note that the prompting of an AI image generator constituted a new form of ekphrasis. (Bajohr 2024; see also Meyer 2023) Bajohr coined the term "operative ekphrasis" to describe the unique capacity that gen AI systems bring to the practice. He distinguishes between the traditional computer manipulation of images and the prompting of generative models. These are performative in a new way because the models embed textual encodings into the model. These encodings are derived from text captions, descriptions, metadata associated with the image scraped from the web or elsewhere. As Bajohr emphasizes, the process of creating these models collapses in important ways the distinction between text and image, and it is this collapse that makes operative ekphrasis possible. Bajohr's notion of collapse resonates with the essay of W. J. T. Mitchell "Ekphrasis and the Other" in Picture Theory (1994, 151-181), long before machine learning systems were capable of image generation. Mitchell argued that the practice of ekphrasis allows us to understand the complicated and always unstable relationship between text and image. The two were never completely distinct as semiotic systems, and the potential merging of text and image could be seen both as the audacious aspiration of ekphrasis and as its nightmare. The merging would confirm the power of the verbal description to become and therefore to control the image it evokes. But, at the same time, it would threaten to dissolve the word in the image. The image would make the word unnecessary. What Mitchell calls "imagetext" provokes both "ekphrastic hope" and "ekphrastic fear."

Imagetext as both image and text is an appropriate description of the latent space of an image generation model. In the training process, images and captions (or textual descriptions) are encoded and both contribute to the same large set of weights that constitute the model. When the training is complete, it is impossible to say which particular values constitute the text and which the images; the representations of text and images are everywhere in the latent manifold. Prompting can be understood as a process of probing the latent space (Liu and Chilton 2023; Almeda et al. 2024) to tease an image out of all the possible images in the space. The resulting image is almost never an exact replica of any of the millions or billions of images that were fed in during training; it is instead an interpolation from among the many similar images that the model has absorbed. The probabilistic nature of the process means that even the computer specialists who have created these images cannot determine exactly how any given image was created. Nevertheless, the process itself (in current systems, usually diffusion) is deterministic: a series of steps in which the system repeatedly refines the image out of an initial pattern of noise.

In generative systems, ekphrasis is a well-defined procedure. The transformation from word to image is a process. Prompting itself is often a repeated process. The prompter creates one prompt and receives one or more images. The first results are often not what the prompter wants, so they repeat the process.

---

## CITATIONS IN THIS SECTION

Almeda et al. 2024. (See BULKHEAD-01 for full citation.)

Bajohr, Hannes. 2024. (See BULKHEAD-01.)

Brosch, Renate. 2018a. "Ekphrasis in the Digital Age." In "Ekphrasis Today," edited by Renate Brosch. *Poetics Today* 39 (2): 225–43. https://doi.org/10.1215/03335372-4324420.

Brosch, Renate, ed. 2018b. "Ekphrasis Today." Special issue, *Poetics Today* 39, no. 2 (June).

Clüver, Claus. 1997. "Ekphrasis Reconsidered: On Verbal Representations of Non-Verbal Texts." In *Interart Poetics*, edited by Ulla-Britta Lagerroth, Hans Lund, and Erik Hedling. Rodopi.

Elleström, L., ed. 2010. *Media Borders, Multimodality and Intermediality*. Palgrave Macmillan.

Heffernan, James A. W. 2004. *Museum of Words: The Poetics of Ekphrasis from Homer to Ashbery*. University of Chicago Press.

Krieger, Murray. 1992. *Ekphrasis: The Illusion of the Natural Sign*. Johns Hopkins University Press. https://doi.org/10.1353/book.68495.

Lindhé, Cecilia. 2013. "A Visual Sense Is Born in the Fingertips: Towards a Digital Ekphrasis." *Digital Humanities Quarterly* 007 (1).

Liu and Chilton 2023. (See BULKHEAD-01.)

Meyer, Roland. 2023. (See BULKHEAD-01.)

Mitchell, W. J. T. 1994. *Picture Theory: Essays on Verbal and Visual Representation*. University of Chicago Press.

Webb, Ruth. 1999. "Ekphrasis Ancient and Modern: The Invention of a Genre." *Word & Image* 15 (1): 7–18. https://doi.org/10.1080/02666286.1999.10443970.

Webb, Ruth. 2016. *Ekphrasis, Imagination and Persuasion in Ancient Rhetorical Theory and Practice*. Routledge.

---

## STATUS

- [x] Text extracted verbatim
- [x] Citations extracted (14 sources)
- [ ] "prompting of an AI image generated" — grammatical error in original. Should be "image generator."
- [ ] Jay's Spitzer reference is via Webb (1999, 10) — no separate Spitzer citation in references. Verify.
