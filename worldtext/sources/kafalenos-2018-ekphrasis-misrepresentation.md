# Source: Kafalenos 2018 — Ekphrasis as Misrepresentation

> **Species**: source  
> **Scale**: source  
> **Evidence Grade**: A (epistemology of ekphrasis + misrepresentation thesis)  
> **Parent Galaxy**: [[galaxy-of-ekphrastic-worlds]]  
> **Full Text**: Yes — 33,275 characters extracted  
> **Last Revision**: 2026-04-13  

---

## Citation

Kafalenos, Emma. "Ekphrasis as Misrepresentation: From Balzac's *Sarrasine* to Cortázar's 'Graffiti.'" *Poetics Today* 39, no. 2 (2018): 287–297.

## Core Argument

Ekphrasis **unavoidably misrepresents** the image it describes, for three structural reasons:

### 1. The Polysemy of the Image
Images are polysemous — they support multiple readings. Barthes (1964): "all images are polysemous; they imply, underlying their signifiers, a 'floating chain' of signifieds, the reader able to choose some and ignore others." Any ekphrasis selects one reading from the floating chain and presents it as definitive. The others are lost.

### 2. The Dissimilarity of Images and Words
Foucault (on *Las Meninas*): "the relation of language to painting is an infinite relation. It is not that words are imperfect, or that, when confronted by the visible, they prove insuperably inadequate. Neither can be reduced to the other's terms: it is in vain that we say what we see; what we see never resides in what we say."

Spence (1982) adds: "words will invariably misrepresent the image" because "any descriptive term will place an image into a category to which it only partly belongs." Crucially: "once a particular term is chosen... this term will arouse its own network of associations and these... will tend to supplant the image."

### 3. The Perspectival Montage
Ekphrasis is a quotation — and all quotations involve a "perspectival montage" (Sternberg 1982) where the quoting subject's perspective is superimposed on the quoted subject's. The two perspectives cannot finally be separated.

### The Cortázar Case: Graffiti as Failed Ekphrasis
In Cortázar's "Graffiti," a man interprets a woman's chalk marks as meaningful communication. At the story's end, we learn the man exists only in the woman's imagination — there was never a second perspective, never an image to describe, never an ekphrasis. The story works because readers *know* ekphrasis misrepresents, and the false-ekphrasis reveals the depth of political repression.

## THE CRITICAL BRIDGE: Misrepresentation = Hallucination

Kafalenos's three reasons ekphrasis misrepresents are **structurally identical** to the three reasons AI systems hallucinate:

| Kafalenos (Ekphrasis) | AI (Generation) |
|----------------------|-----------------|
| **Polysemy of the image**: multiple valid readings; ekphrasis selects one | **Multimodality of latent space**: multiple valid decodings; the model samples one |
| **Dissimilarity of media**: words cannot capture what eyes see; "neither can be reduced to the other's terms" | **Modality gap**: text embeddings and image embeddings do not perfectly overlap; reconstruction is always lossy |
| **Perspectival montage**: the describer's bias is superimposed on the image-maker's intent | **Training bias**: the model's learned distribution is superimposed on the user's intent |

### And Spence's Deadly Insight Maps Exactly

Spence (1982): "once a particular term is chosen... this term will arouse its own network of associations and these... will tend to supplant the image."

This is **exactly how AI hallucination works**: once a token is generated, it activates its own network of associations in the autoregressive model, and these associations can "supplant" the original prompt intent. The token that replaces the intended image is the hallucination. Spence described autoregressive drift in 1982, 40 years before GPT.

### The "Rorschach Test" Connection

Kafalenos: "what a narrativizer chooses to add [to an image] can be interpreted like a Rorschach test." This is exactly what prompting a generative model reveals — the model's "Rorschach response" to a prompt exposes its training distribution's biases, blind spots, and associative habits.

## Cross-References

- **Bajohr** → "artificial semantics" = Barthes' "polysemy" in a machine substrate
- **Foucault** → "the relation of language to painting is an infinite relation" — the foundational impossibility that drives both ekphrasis and AI research
- **Spence** → autoregressive drift described 40 years before GPT
- **Sternberg** → perspectival montage = training bias layered on user intent
- **Louvel** → the pictorial third emerges FROM the misrepresentation — it is the surplus of the gap, not the failure of the translation

## World Effects

- **[[world-operative-ekphrasis]]**: misrepresentation is not a defect but the constitutive condition
- **[[world-classical-ekphrasis]]**: all ekphrasis is misrepresentation — this is the tradition's deepest truth
- **[[bridge-misrepresentation-to-hallucination]]**: NEW bridge — the most powerful connection
- **[[distinction-misrepresentation-hallucination]]**: the ekphrastic and AI names for the same structural feature
- **[[entity-kafalenos]]**: key entity

---

*Kafalenos is the epistemologist of the cosmos. She asks: what does it mean to describe an image in words? And her answer — that misrepresentation is inevitable — is precisely the answer AI researchers are giving to the question: what does it mean for a model to generate an image from a prompt?*
