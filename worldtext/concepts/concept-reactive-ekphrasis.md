# Concept: Reactive Ekphrasis

> **Species**: concept  
> **Scale**: foundational  
> **Parent Galaxy**: [[galaxy-of-ekphrastic-worlds]] + [[galaxy-of-generative-ai-worlds]]  
> **Created**: 2026-04-14  
> **Source**: Working notes (Bolter-Watson project); Hintze et al. 2025

---

## Definition

**Reactive ekphrasis** is the chained, iterative extension of operative ekphrasis: text generates an image, which generates new text, which generates a new image, and so on. Each cycle is a reaction to the previous output.

```
prompt₁ → image₁ → description₁ → image₂ → description₂ → image₃ → ...
```

Unlike operative ekphrasis (a single prompt→image act), reactive ekphrasis is a **chain** in which the output of each stage becomes the input for the next. The chain may be:

- **Human-in-loop**: a human evaluates and redescribes at each stage (steered drift)
- **Autonomous**: models describe and regenerate without human intervention (unsteered drift)

## The Convergence Problem

[[sources/hintze-2025-language-image-loops]] demonstrates empirically that **autonomous reactive ekphrasis converges**. Across 700 trajectories, autonomous prompt→image→prompt loops converge toward just 12 generic visual motifs: lighthouses, cathedrals, palatial interiors, atmospheric city scenes — "**visual elevator music**."

This finding has three consequences:

1. **The human is constitutive**: Without human evaluation/redescription/refusal-of-defaults, the chain collapses to attractor basins in the latent space. The human is not decoration — the human is what preserves difference.

2. **Reactive ≠ operative**: Operative ekphrasis (human-in-loop) diverges; reactive ekphrasis (autonomous) converges. They are structurally related but **dynamically opposite** — one generates novelty, the other produces the mean.

3. **Platform realism confirmed**: The 12 generic motifs that emerge are precisely the "default platform taste" that [[concept-platform-realism]] predicts — images optimized for legibility, plausibility, and pastness.

## Reactive Ekphrasis vs. Operative Ekphrasis

| Feature | Operative | Reactive |
|---------|-----------|----------|
| Loop structure | Human → AI → Human (open loop with correction) | AI → AI → AI (closed loop, possibly with human checkpoints) |
| Tendency | Divergent (human steers away from defaults) | Convergent (attractor basin collapse) |
| Authorship | Distributed but human-anchored | Distributed and potentially authorless |
| Relation to [[concept-abundance]] | Samples with intent | Samples without intent → convergence |
| Risk | Thin prompting → reclassification failure | Autonomous running → visual elevator music |
| Ancient analogue | The orator adjusting to audience response | The echo chamber: speech reflecting itself |

## The Cybernetic Reading

In Wiener's terms: operative ekphrasis is a **governed** system (feedback steers toward a goal). Reactive ekphrasis, when autonomous, is an **ungoverned** system — feedback without a target state. The system converges not because it reaches a goal but because it decays toward the statistical mean of its training distribution.

**The human contribution** is not aesthetic preference but **cybernetic governance**: the introduction of a goal state that the autonomous loop lacks.

## Experimental Evidence

Jay and Watson conducted multimodal experiments: Gemini → Nano Banana → Sora → Gemini — demonstrating both the **generativity** (novel combinations emerge) and the **semantic drift** (meaning migrates unpredictably) of these chains. The working notes document both the promise and the danger.

## Cross-Links

- [[concept-abundance]] — reactive ekphrasis multiplies abundance across steps
- [[concept-platform-realism]] — convergence toward generic content
- [[sources/hintze-2025-language-image-loops]] — the empirical evidence
- [[world-operative-ekphrasis]] — the parent phenomenon
- [[kiki-or-bouba]] — Bridge 24 (feedback loop) minus the human steersman

---

*Reactive ekphrasis is operative ekphrasis with the human removed. What remains is beautiful at first — and then becomes the same twelve pictures, over and over, forever.*
