# Bridge: Misrepresentation = Hallucination — The Deepest Structural Identity

> **Species**: bridge  
> **Scale**: bridge (CRITICAL)  
> **Location**: junction of [[galaxy-of-ekphrastic-worlds]] and [[galaxy-of-generative-ai-worlds]]  
> **Last Revision**: 2026-04-13  

---

## The Claim

Ekphrastic **misrepresentation** (Kafalenos 2018) and AI **hallucination** are the same structural phenomenon at different scales. Both are inevitable consequences of converting between two fundamentally dissimilar representational systems. And both are not defects but **constitutive features** of the system they inhabit.

---

## The Evidence

### 1. Polysemy → Multimodal Ambiguity

Barthes (1964, via Kafalenos): **"All images are polysemous."** The image supports multiple readings; the describer selects one.

CLIP (via Bajohr 2024): The embedding space maps texts and images to nearby vectors, but the mapping is many-to-many. Multiple prompts map to overlapping visual regions. The model samples one possible image from a distribution of valid responses.

**In both cases**: the input (image / prompt) is *richer* than any single output (description / generated image) can capture. Selection from abundance is the basic operation.

### 2. Medium Dissimilarity → Modality Gap

Foucault (1966, via Kafalenos): **"It is in vain that we say what we see; what we see never resides in what we say."** Words and images are different media with different expressive capacities; neither can be reduced to the other's terms.

Liang et al. (2022, "Mind the Gap"): The **modality gap** in CLIP shows that text and image embeddings occupy geometrically distinct regions of the shared space. Even when a text and image are semantically identical, their vectors are separated by a systematic offset. Translation between modalities is always approximate.

**In both cases**: the conversion between representational systems is structurally lossy. Perfect fidelity is not just hard — it is impossible. The gap is not a bug; it is an architectural feature.

### 3. Perspectival Montage → Training Bias

Sternberg (1982, via Kafalenos): Quotation always involves a **"perspectival montage"** — the quoting subject's perspective is inevitably superimposed on the quoted subject's. The two cannot be fully separated.

AI alignment research (Bommasani et al. 2021, etc.): Model outputs inevitably reflect the **training distribution's biases**. The model's "perspective" (learned statistical patterns) is superimposed on the user's intent. The two cannot be fully separated.

**In both cases**: there is no neutral position from which to describe/generate. Every output carries the trace of the system that produced it — whether that system is a human mind shaped by culture or a neural network shaped by training data.

### 4. Spence's Drift → Autoregressive Hallucination

Spence (1982, via Kafalenos): **"Once a particular term is chosen... this term will arouse its own network of associations and these, if they are sufficiently compelling, will tend to supplant the image."**

Autoregressive generation (GPT, etc.): Once a token is generated, it enters the context window and conditions all subsequent tokens. If the initial token is slightly off-target, the subsequent tokens follow its associative trajectory rather than the original prompt's intent. **The associations supplant the image.**

**This is the most precise structural identity in the cosmos.** Spence described the mechanism of autoregressive drift — one modality (language) gradually replacing another (visual memory/intent) through cascading associations — 40 years before anyone built a model that does it computationally.

---

## Why Both Are Constitutive, Not Defective

Here is the non-obvious conclusion that connects to the cosmos's deepest thesis:

If misrepresentation/hallucination is **inevitable** (as both Kafalenos and AI researchers agree), then the question is not "how do we eliminate it?" but **"what does it produce?"**

### What Misrepresentation Produces (Ekphrasis Side)

- **Louvel's pictorial third**: the surplus that arises from the gap between word and image. If ekphrasis perfectly represented the image, there would be no pictorial third — no new meaning, no surprise, no discovery.
- **Krieger's miracle/mirage**: the "illusion" of the natural sign is productive precisely because it is an illusion. If words could literally become images, the miracle would vanish.
- **Thick description**: Geertz's thick description works because it re-describes what is already visible, adding interpretive layers that were not "in" the original. Thick description IS misrepresentation — the addition of significance that the "thin" description did not contain.

### What Hallucination Produces (AI Side)

- **Creative serendipity**: the moments when a generated image exceeds the prompt's literal specification — capturing a mood, suggesting a composition, discovering a visual solution the user hadn't imagined.
- **Training distribution exposure**: hallucinations reveal the model's biases, which is itself valuable information (the Rorschach function Kafalenos identifies).
- **The prompt-output gap**: the space where prompt craft becomes creative practice (Lindley & Whitham 2025).

### The Shared Truth

**The gap between input and output is where meaning forms.** If the system were perfectly faithful, it would be a photocopier — producing exact copies with no interpretation, no surplus, no discovery. Misrepresentation and hallucination are the system's *creativity* — the difference between copying and generating, between thin description and thick description.

This is the answer to the question posed in the Four Strata synthesis: **What does ekphrasis become in Stratum IV (dissolution)?** It becomes the art of navigating the productive gap between prompt and output — the art of misrepresentation as creative practice.

---

## The Cortázar Test

Kafalenos's analysis of Cortázar's "Graffiti" provides a test case for the bridge:

In the story, a man interprets chalk marks as meaningful messages from a woman. At the end, we learn the woman invented him — there was no communication, no image, no ekphrasis. The "misrepresentation" is total: the described images never existed.

**The AI equivalent**: generating an image of a concept that has no visual referent (e.g., "the feeling of justice" or "the smell of time"). The generated image is a response to something that was never visual in the first place. It is a misrepresentation of a non-existent original — an ekphrasis without an image to describe.

This is what Krieger called **notional ekphrasis**: description of an artwork that exists only in the text. And it is what AI does every time it generates an image from a text prompt — it creates the image that the text describes, even though that image never existed before the description.

**Notional ekphrasis is the default mode of AI generation.**

---

## Cross-References

- [[source-kafalenos-2018-ekphrasis-misrepresentation]] — founding document
- [[source-bajohr-2024-operative-ekphrasis]] — CLIP as the machine substrate for polysemy
- [[concept-pictorial-third]] — the productive gap between input and output
- [[bridge-paragone-to-alignment]] — misrepresentation as the failure mode that alignment tries to prevent (but shouldn't eliminate entirely)
- [[synthesis-rosetta-stone]] — Bridge 13 (this extends the original 12)
- [[world-thick-description]] — thick description IS productive misrepresentation
