# Distinction: Fluency / Fidelity

> **Species**: distinction  
> **Scale**: entity  
> **Parent World**: [[world-worldtext-coherence]] ↔ [[world-operative-ekphrasis]]  
> **Source**: worldtext-definitive-corpus-2026-04-28

---

## Poles

| Pole | Definition |
|------|-----------|
| **Fluency** | Surface-plausibility — output that sounds correct, reads smoothly, and appears coherent without constraining future generation or carrying referential weight |
| **Fidelity** | Referential adequacy — output that describes something specific, constrains what can follow, and would break if its nouns were swapped |

## The Distinction

```
<fluency> [hides] <referential-emptiness>
<fidelity> [exposes] <descriptive-adequacy>
```

Fluency is cheap. The generative model is biased toward it because it is the statistical mean of the training distribution. "The village was nestled in a verdant valley" is fluent. It describes nothing. It constrains nothing.

Fidelity is expensive. It requires **descriptive struggle** — the hard work of specifying what is actually the case, what distinguishes this world from all other possible worlds, what will break if you change a detail.

## Operational Test

1. Take a generated passage
2. Swap the key nouns (village → outpost, valley → ridge, cobblestone → gravel)
3. If the passage still works, it is fluent but not faithful
4. If the passage breaks, it possesses fidelity

## Relationship to Cosmos

This distinction is the **governing binary** of the entire Worldtext project. Every diagnostic, every ritual, every synthesis ultimately asks: is this output fluent or faithful? The [[entity-vermeer-problem|Vermeer Problem]] is fluency mistaken for fidelity. The [[syntheses/thick-prompt|Thick Prompt]] is the technique for producing fidelity. The [[syntheses/seven-failure-modes|Seven Failure Modes]] are seven ways fidelity breaks down.

## Cross-References

- [[distinction-thick-thin]] — thick description is the hermeneutic name for fidelity
- [[entity-vermeer-problem]] — fluency without fidelity at the output level
- [[entity-viscosity-trap]] — the process that replaces fidelity with fluency over time
- [[conflict-style-vs-causality]] — style is fluency; causality is fidelity
- [[distinction-rag-worldtext]] — RAG retrieves fluently; Worldtext generates faithfully

## Sources

- `dse.json` (Descriptive Struggle and Descriptive Adequacy)
- worldtext-definitive-corpus-2026-04-28
