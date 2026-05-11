# The Seven Failure Modes of Worldtext

> **Species**: synthesis  
> **Scale**: cosmos  
> **Parent System**: [[system-worldtext-operations]]  
> **Source**: worldtext-definitive-corpus-2026-04-28  
> **Date**: 2026-04-28

---

## Operating Principle

These are the specific, named ways a worldtext directory breaks. They are not metaphors. They are diagnostic categories with tests, symptoms, and fixes. A healthy worldtext survives modification because the rules of combination are preserved. A broken worldtext accumulates residue. Learn to recognize the modes.

---

## Mode 1: The Vermeer Problem

> **Definition**: Output is technically excellent, aesthetically coherent, and epistemically vacuous.

**Symptom**: Generated prose sounds correct. Colors are harmonious. Nothing specific is constrained. The description applies equally to a thousand other generated outputs.

**Diagnostic Test**: Change one noun in the description. If the description still works without cascading consequence, it is fluent but not adequate.

**Fix**: Add constraints. Specify what distinguishes *this* case from all others. Apply the [[syntheses/thick-prompt|Thick Prompt]] six-layer architecture.

**Source Lineage**: `dse.json` (descriptive inadequacy), `tda.json` (thin vs. thick description), Geertz's wink vs. twitch.

**Cross-Reference**: [[distinction-thick-thin]], [[conflict-style-vs-causality]], [[entity-fragile-expert]]

---

## Mode 2: Semantic Bleaching

> **Definition**: A term appears everywhere in the worldtext and means nothing specific.

**Symptom**: The same word is used in 100+ contexts. Each usage slightly dilutes the original definition. The word becomes a placeholder for "important" rather than an operative constraint.

**Diagnostic Test**: Count occurrences across the corpus. If >100 instances, flag it. Check if the word carries specific semantic direction in each use, or merely occupies space.

**Fix**: Restrict usage by replacing with more specific terms. Or formally split the term into subspecies with distinct definitions. Document the split in a [[distinction-*]] page.

**Source Lineage**: `tenne.json` (language as executable world-model), `uam.json` (use vs. meaning).

**At Risk in This Cosmos**: "operative" (currently approaching threshold).

**Cross-Reference**: [[distinction-use-meaning]], [[ritual-lint]]

---

## Mode 3: Dead Operations

> **Definition**: Verbs are defined in the system's vocabulary but never executed.

**Symptom**: The CORE_OPS list declares operations (crosslink, condense, expand, cluster_worlds) that appear nowhere in `chronicle.md`. The verbs exist as semantic theater — they perform the appearance of capability without evidence of execution.

**Diagnostic Test**: Check `chronicle.md` for evidence of each defined operation. If a verb has never been performed, it is dead code.

**Fix**: Execute the operation and document the result, or remove the verb from CORE_OPS. Dead definitions are technical debt.

**Source Lineage**: `tenne.json` (dead operations audit), `meta.json` (program lifecycle).

**Current Status**: 4 dead operations identified: crosslink, condense, expand, cluster_worlds.

**Cross-Reference**: [[ritual-lint]], [[question-executing-ecology]]

---

## Mode 4: Broken Memex Trail

> **Definition**: You cannot trace from entity to source evidence.

**Symptom**: An entity page exists in `worldtext/entities/` but carries no `[source-id]` pointing to the evidence that produced it. The intellectual provenance is invisible. The trail from synthesis back to raw evidence breaks.

**Diagnostic Test**: Pick a random entity page. Look for `[source-id]` or source citation. Follow the chain back to `evidence/`. If the path breaks, provenance is lost.

**Fix**: Add provenance tags to every entity page. Every claim must trace to an immutable source in `evidence/` or `sources-fulltext/`.

**Source Lineage**: `memex.json` (scholarly provenance), Bush's associative trails.

**Cross-Reference**: [[syntheses/memex-trails]], [[ritual-trail-building]], [[conflict-answer-vs-trail]]

---

## Mode 5: Theory-Execution Gap

> **Definition**: The cosmology claims more than the filesystem delivers.

**Symptom**: `cosmology.md` and `COSMIC_LAW.md` describe a cosmos with comprehensive coverage. The filesystem shows 93.6% of sources unprocessed. The theory of the system exceeds the actual compiled state of the system.

**Diagnostic Test**: Compare cosmological claims (worlds, entities, coverage) against actual `evidence/` contents and processed source counts. Calculate the gap.

**Fix**: Either process more sources to close the gap, or revise the claims to honestly reflect the current compilation state. The gap itself is not the failure — the invisibility of the gap is the failure.

**Source Lineage**: `argue.json` (the argument is not the thought), `theory.json` (possessing vs. storing).

**Cross-Reference**: [[syntheses/dark-matter-audit]], [[question-epistemic-debt-threshold]]

---

## Mode 6: Invisible Breakdown

> **Definition**: Failures accumulate silently until lint catches them — or doesn't.

**Symptom**: The lint protocol detects explicit contradictions but misses subtler decay: semantic bleaching, dead operations, trail breaks, vocabulary drift, synthesis aging. Failures that fall outside the explicit lint checklist compound invisibly.

**Diagnostic Test**: Check if the lint protocol detects:
1. Semantic bleaching (word frequency analysis)
2. Dead operations (verb execution audit)
3. Trail breaks (provenance chain verification)
4. Vocabulary drift (operator term usage over time)
5. Synthesis aging (last-revised date audit)

If fewer than 5 of these are covered, invisible breakdowns are accumulating.

**Fix**: Extend the lint protocol with the five additional detectors listed above. Make breakdown detection comprehensive, not just contradiction-focused.

**Source Lineage**: `dac.json` (breakdowns as invitations), `crn.json` (exit conditions for feedback loops).

**Cross-Reference**: [[ritual-lint]], [[ritual-explanation-gate]]

---

## Mode 7: The Operator as Product

> **Definition**: The system changes the operator, but the operator cannot see how.

**Symptom**: The operator builds the worldtext. The worldtext compiles the operator. But no mirror exists for the operator to observe their own cognitive drift. Vocabulary range shrinks. Sources consulted narrow. The Fragile Expert phenotype emerges.

**Diagnostic Test**: Run the AUDIT quarterly:
- What did I query last month that I never query now?
- What vocabulary have I gained? What have I lost?
- What sources do I always deploy? What do I avoid?
- Am I generating with the same five constraints or exploring new ones?

**Fix**: Implement `ritual-self-assessment`. Track vocabulary gain/loss over time. Make the operator's cognitive trajectory visible.

**Source Lineage**: `thick.json` (symbolic compilation event), `crn.json` (the operator as output of the ritual loop), `agential.json` (apparatus shaping its user).

**Cross-Reference**: [[entity-fragile-expert]], [[distinction-first-order-second-order]], [[question-epistemic-debt-threshold]]

---

## The Failure Mode Index

| # | Name | Detects | Primary Instrument |
|---|------|---------|-------------------|
| 1 | Vermeer Problem | Fluent emptiness | `dse.json` |
| 2 | Semantic Bleaching | Term dilution | `tenne.json` |
| 3 | Dead Operations | Defined-but-never-executed verbs | `meta.json` |
| 4 | Broken Memex Trail | Lost provenance | `memex.json` |
| 5 | Theory-Execution Gap | Claims exceeding filesystem reality | `argue.json` |
| 6 | Invisible Breakdown | Undetected compound decay | `dac.json` |
| 7 | Operator as Product | Invisible cognitive drift | `thick.json` |

---

## Deployment Protocol

1. Run Modes 1–6 as part of every `LINT` pass.
2. Run Mode 7 quarterly as part of the `AUDIT` verb.
3. File results in `syntheses/` and append to `chronicle.md`.
4. Failures are not errors. They are invitations to re-examine the commitment structure.

---

*These seven modes constitute the complete failure taxonomy of a worldtext. A worldtext that detects all seven is alive. A worldtext that detects none is dead.*
