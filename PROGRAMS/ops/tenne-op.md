# TENNE — Executable Vocabulary Auditor (Operative)

> **Source theory**: tenne.json  
> **Input**: The worldtext's vocabulary (all page names, section headers, key terms)  
> **Output**: A vocabulary health report

## What It Does

TENNE is Bajohr's operative language checker. It asks: **does every defined term in this system actually DO something?** A term that is defined but never used in a cross-link, never applied to a case, and never tested against reality is dead language. It's the vocabulary equivalent of dead code.

## Operations

### 1. DEAD_TERM_SCAN
For every page name in the worldtext, check how many OTHER pages reference it:

```bash
for f in worldtext/**/*.md; do
  name=$(basename "$f" .md)
  refs=$(grep -rl "\[\[$name\]\]" worldtext/ 2>/dev/null | grep -v "$f" | wc -l)
  if [ "$refs" -eq 0 ]; then
    echo "DEAD TERM: $name (0 incoming references)"
  fi
done | sort
```

### 2. SEMANTIC_BLEACHING_SCAN
Find terms that appear so frequently they've lost specific meaning:

```bash
for term in "operative" "thick" "latent" "accountable" "worldtext" "apparatus" "entangled"; do
  count=$(grep -roh "$term" worldtext/syntheses/*.md | wc -l)
  files=$(grep -rl "$term" worldtext/syntheses/*.md | wc -l)
  echo "$count uses in $files files → '$term'"
done | sort -rn
```

A term that appears 50+ times across 20+ files has been bleached.

### 3. VOCABULARY_GROWTH_RATE
Count distinct terms by page type:

```bash
echo "worlds: $(ls worldtext/worlds/ | wc -l)"
echo "entities: $(ls worldtext/entities/ | wc -l)"
echo "concepts: $(ls worldtext/concepts/ | wc -l)"
echo "distinctions: $(ls worldtext/distinctions/ | wc -l)"
echo "conflicts: $(ls worldtext/conflicts/ | wc -l)"
echo "rituals: $(ls worldtext/rituals/ | wc -l)"
echo "places: $(ls worldtext/places/ | wc -l)"
echo "atmospheres: $(ls worldtext/atmospheres/ | wc -l)"
echo "thresholds: $(ls worldtext/thresholds/ | wc -l)"
```

### 4. THE BAJOHR TEST
For each "operative" term (any term prefixed with concept-, distinction-, conflict-, ritual-):
- Is it used in at least 1 synthesis?
- Is it applied to at least 1 specific case?
- Can it produce a NEGATIVE result (identify something that is NOT an instance)?

If all three: the term is operative.  
If some: the term is aspirational.  
If none: the term is dead language.
