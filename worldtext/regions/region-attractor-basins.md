# Region: Attractor Basins

> **Species**: region  
> **Scale**: region  
> **Parent World**: [[world-latent-space]]

---

## Definition

**Attractor basins** are local clusters in the latent space where specific stylistic, cultural, or entity-linked content pools. They are created by dense concentrations of related training examples — a photographer whose images appear thousands of times, an art movement thoroughly documented online, a named artist cited in millions of captions.

## Examples

| Basin | Training Signal | Effect on Generation |
|-------|-----------------|---------------------|
| **"Lotte Reiniger"** | Her silhouette animations online | Shadow puppet aesthetic, high-contrast, black/white |
| **"Studio Ghibli"** | Millions of Ghibli screenshots + fan art | Watercolor, pastoral, luminous sky, soft edges |
| **"Ansel Adams"** | His photographs + enormous critical apparatus | Black-and-white landscape, zone system tones, deep depth of field |
| **"Art Deco"** | Architectural photography, poster art, pattern libraries | Geometric, gold + black, fan shapes, stepped forms |
| **stock photography** | The platform mean's gravitational core | Generic, sanitized, demographically biased |

## Topology

Each attractor basin has:
- A **center** (highest training density, most stereotypical output)
- A **gradient** (moving away from center, output becomes increasingly uncertain/creative)
- A **boundary** where it meets other basins or the platform mean (here, unexpected hybrid outputs occur — the creative edge)

The thick prompter navigates to a basin by naming it. Combining basins ("Ansel Adams meets Studio Ghibli") forces the generation into the **boundary zone** between basins — a space the training data rarely occupies, where novelty is possible.

## Cross-Links

- [[region-platform-mean]] — the largest basin; the gravitational default
- [[concept-viscosity]] — basins with more training data have higher viscosity (harder to escape)
- [[scene-shadowplay-installation]] — "Lotte Reiniger" as a deliberate basin selection
- [[concept-context-stack]] — the L5 user prompt is the primary basin-selection mechanism
