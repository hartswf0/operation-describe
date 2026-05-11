# DSE — Descriptive Struggle Engine (Operative)

> **Source theory**: dse.json  
> **Input**: Any .md file in the worldtext  
> **Output**: A struggle report classifying each section of the file

## What It Does

DSE reads a file and asks Murdoch's question of every paragraph: **did this language cost the author something?**

## Operations

### 1. PRESSURE_SCAN
Read the target file. For each section (delimited by ##), count:
- **Revision markers**: words like "however," "but," "not quite," "more precisely," "rather," "instead," "actually," "upon closer inspection" — evidence the writer corrected themselves
- **Hedging markers**: "perhaps," "might," "seems," "arguably" — evidence of uncertainty (which is honest) vs. "is," "clearly," "obviously" (which may be false confidence)
- **Specific referents**: proper nouns, page numbers, direct quotes — evidence of contact with source material
- **Generic abstractions**: "the system," "the process," "the phenomenon," "the operation" — evidence of floating above the material

Score each section: `specificity_ratio = specific_referents / (specific_referents + generic_abstractions)`

### 2. MURDOCH_TEST
For each section, classify:
- **S6: Accountable** — high specificity, revision markers present, sources cited
- **S3: Candidate** — has force but lacks grounding (expressive but no sources)
- **S1: Partial** — generic language, no revision evidence
- **S0: Unformed** — pure abstraction, no contact with any specific thing

### 3. CLICHÉ_DETECTOR
Flag any phrase that appears in 3+ syntheses verbatim. If the same string appears across multiple files, it has become a cliché — its descriptive force is dead.

Run: `grep -c "PHRASE" worldtext/syntheses/*.md`

### 4. FLUENCY_TRAP
Flag sections where word count exceeds 500 but specificity_ratio < 0.1. These are high-volume, low-contact sections: the language is fluent but not touching anything.

## Execution

```bash
# Run DSE on a target file
TARGET="worldtext/syntheses/thick-description-of-operative-ekphrasis.md"

# PRESSURE_SCAN
echo "=== REVISION MARKERS ==="
grep -c -i "however\|but \|not quite\|more precisely\|rather,\|instead,\|actually,\|upon closer" "$TARGET"

echo "=== SPECIFIC REFERENTS ==="
grep -c "[A-Z][a-z]* [0-9]\{4\}\|p\.\|pp\.\|§\|\[\[entity-" "$TARGET"

echo "=== GENERIC ABSTRACTIONS ==="
grep -c "the system\|the process\|the phenomenon\|the operation\|the mechanism\|the apparatus" "$TARGET"

echo "=== CLICHÉ CHECK ==="
# Find phrases that appear in 3+ files
grep -oh '"[^"]*"' "$TARGET" | while read phrase; do
  count=$(grep -rl "$phrase" worldtext/syntheses/*.md | wc -l)
  if [ "$count" -ge 3 ]; then echo "CLICHÉ ($count files): $phrase"; fi
done
```

## What the Report Looks Like

```
DSE REPORT: thick-description-of-operative-ekphrasis.md
================================================
Section 1 "The Six Layers": S6 (Accountable) — specificity 0.73, 4 revision markers, Geertz 1973 cited
Section 2 "Layer Analysis": S3 (Candidate) — specificity 0.41, 1 revision marker, no direct quotes
Section 3 "Reclassification": S1 (Partial) — specificity 0.12, 0 revision markers, 8 generic abstractions
CLICHÉS FOUND: "material-discursive" (5 files), "operative cut" (4 files)
FLUENCY TRAP: Section 3 — 620 words, specificity 0.12
```
