# Scene: The Carrot Uprising

> **Species**: scene  
> **Scale**: scene  
> **Parent World**: [[world-operative-ekphrasis]]  
> **Source**: "Operative Ekphrasis: Thick Prompting and the Ritual of the Latent Space" (Paper A)

---

## The Scene

A designer (Watson Hartsoe) sits at a workstation. The task: use the humble carrot (*Daucus carota*) as an architectural unit in a generative workflow. Not "generate an image of a carrot." Build a civilization from carrots.

**The thick prompt stack:**
1. **LDraw code** — The LLM is not asked for a pixel image but for LDraw file syntax: `1 4 0 0 0 1 0 0 0 1 3001.dat`. The text becomes geometric primitives. The prompt writes CAD instructions.
2. **POML orchestration** — The LDraw modules are organized using Prompt Orchestration Markup Language. POML acts as the worldtext container, defining spatial relationships between the generated "carrot-bricks."
3. **Intermedial compiling** — The LDraw/POML code is rendered into a visual representation, which is then fed into an image-to-video model (LumaLabs Ray3).
4. **The residue** — The final output is not just the video. It is the chain of text, code, and geometry that produced it. The thick prompt IS the artwork as much as the image.

**The atmosphere**: Ritualistic. Each step transforms the medium. Text → code → geometry → render → video. The "Carrot Uprising" is not an image; it is a **multi-stage compiling event**.

**The reclassification threshold**: A simple prompt ("make a Lego carrot") would produce platform realism — a generic, slightly-cute LEGO brick. The thick prompt stack forces the model through four compiling stages, each adding semantic density. The carrot ceases to be a vegetable and becomes an architectural morpheme.

## What This Scene Contains

- **Infrastructure**: The two-compiler architecture (LDraw = discrete geometry; LEGOS = continuous diffusion)
- **Flow**: Text → LDraw instructions → geometric primitives → POML orchestration → render → image-to-video model → final output
- **Memory trace**: LEGO as a cultural artifact; the carrot as a biological form; LDraw as an open standard since 1995
- **Fragment within**: The "blunt sword" — this process solves the paragone by dissolving it. Text IS the image. Code IS the geometry. The word/image distinction has no purchase.

## Cross-Links

- [[fragment-blunt-sword]] — this is the blunt sword in action
- [[concept-context-stack]] — the LDraw/POML/render chain IS a full context stack
- [[concept-viscosity]] — each compiling stage reduces viscosity toward the intended region
- [[distinction-intent-distribution]] — maximum intent (4 layers of specification) against distribution's default
- [[concept-worldtext]] — POML is a literal worldtext: a textual specification of a spatial world
