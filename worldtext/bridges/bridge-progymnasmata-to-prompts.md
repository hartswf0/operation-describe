# Bridge: The Progymnasmata Pipeline — Ancient Curriculum → Modern Prompt Pedagogy

> **Species**: bridge  
> **Scale**: bridge  
> **Location**: junction of [[world-classical-ekphrasis]] and [[world-prompt-craft]]  
> **Last Revision**: 2026-04-13  

---

## The Parallel Curricula

### The Ancient Pipeline (Webb 1999, pp. 39-64)

The **Progymnasmata** were 14 graded rhetorical exercises that every educated Greek student performed, attributed to Hermogenes, Aphthonius, and Theon (2nd-4th century CE). The exercises relevant to ekphrasis:

1. **Ethopoeia** (ἠθοποιΐα) — creating a character's speech in a given situation
2. **Ekphrasis** (ἔκφρασις) — vivid description of persons, places, actions, times, events
3. **Encomium** (ἐγκώμιον) — praise of a subject, combining description with evaluation

Webb reports that Theon classified ekphrasis into **six objects**: persons, events, places, times, animals, plants. For each, the student had to master **specific techniques of vivification** — choosing details that convert hearing into seeing.

> "The requirement is that language activate the listener's capacity to form mental images." — Webb 1999, p. 12

### The Modern Pipeline (Liu 2023, Oppenlaender 2024)

Liu (2023) — "Design Guidelines for Prompt Engineering Text-to-Image Generative Models" — studies prompts structured by **subject and style keywords**. Their experimental design:
- 51 **subjects** (abstract and concrete)
- 51 **styles** (abstract and figurative)
- 5,493 generations evaluated for quality

Oppenlaender (2024) finds that participants "lacked style-specific vocabulary necessary for effective prompting" — exactly the deficit the Progymnasmata were designed to remedy.

## The Mapping

| Progymnasmata (Webb) | Prompt Engineering (Liu/Oppenlaender) |
|---------------------|--------------------------------------|
| 6 ekphrastic objects (person, event, place, time, animal, plant) | Subject keywords (51 abstract/concrete categories) |
| Style techniques (vivid detail selection, sensory vocabulary) | Style keywords (51 abstract/figurative categories) |
| Graded difficulty (simple→complex) | Graded complexity (single-concept→multi-concept compositions) |
| Teacher feedback on student's ekphrasis | Model output as feedback on prompt quality |
| Goal: enargeia in the listener | Goal: coherence + aesthetic quality in the output |
| Assessment criterion: "does the audience almost see?" | Assessment criterion: "does the image match the intent?" |
| Vocabulary acquired through practice (years of exercises) | Vocabulary acquired through practice ("a new type of skill that must first be acquired") |

## The Shared Insight

Both curricula discover the same fundamental truth: **verbal-to-visual conversion is a SKILL, not an intuition, and the critical bottleneck is VOCABULARY.**

- The ancient student needed to learn the *vocabulary of vivid detail* — which specific words activate mental images
- The modern prompter needs to learn the *vocabulary of style modifiers* — which specific tokens activate the model's trained representations

Webb quotes Quintilian: the orator must "see for himself" before he can make others see. Oppenlaender quotes participants: "I didn't know what words to use." The problem is the same: a poverty of the verbal that prevents the visual from emerging.

## What the Modern Pipeline LACKS that the Ancient One Had

1. **Ethical framing**: The Progymnasmata embedded ekphrasis within a moral education. The descriptive exercises were preparation for **deliberation** (symbouleutikos) — the civic art of advising. Prompt engineering courses have no ethical substrate.

2. **Oral performance**: Ancient ekphrasis was *spoken*, with the body of the speaker as the medium. Prompt engineering is *typed*, with the keyboard as the interface. (See Bridge 10: Mathieson/Oppenlaender body prompting as the return of orality.)

3. **Genre awareness**: The Progymnasmata taught students to recognize when different types of description were appropriate (ethopoeia for persons, ekphrasis for objects, encomium for praise). Liu (2023) begins to categorize prompt types, but the taxonomy is empirical rather than principled. Louvel's 11 types could serve as the principled framework.

4. **Audience theory**: Ancient rhetoric always began with the audience — who are they, what do they know, what must I make present to them? Prompt engineering has no systematic theory of the "audience" (the model) — prompters learn what works through trial and error rather than through a theory of the model's "cultural memory" (training distribution).

## The Paper That Should Be Written

A comparative study of the Progymnasmata and prompt engineering pedagogy would:
1. Map Webb's 6 ekphrastic objects onto Liu's 51 subject categories
2. Map Louvel's 11 types onto empirically observed prompt strategies
3. Test whether Progymnasmata-trained writers produce better prompts than untrained ones
4. Propose an updated Progymnasmata for the TTI age, incorporating both Quintilian's ethical framework and Oppenlaender's "style-specific vocabulary"

## Cross-References

- [[source-webb-1999-ekphrasis-ancient-modern]] — the Progymnasmata
- [[source-louvel-2018-types-of-ekphrasis]] — the 11 types as principled prompt taxonomy
- [[source-kulkarni-2023-a-word-is-worth-a-thousand-pictures-pro]] — prompts as design material
- [[source-lindley-whitham-2025-prompt-craft]] — craft (not engineering) as the correct framing
- [[synthesis-rosetta-stone]] — Bridge 6 in the master synthesis
- [[world-oral-formulaic-generation]] — Homer's formulas as the oral version of this pipeline
