# THEORY — Theory Death Detector (Operative)

> **Source theory**: theory.json  
> **Input**: The entire PROGRAMS/ and worldtext/ directory  
> **Output**: A theory-life report

## What It Does

THEORY is Naur's mortician. It asks: **is the theory still alive in the people who work on this, or has it died into documentation?** A living theory means the operators can modify the system coherently without breaking it. A dead theory means the operators can only patch, duplicate, and work around.

## Operations

### 1. COHERENCE_TEST
Check if recent additions to the worldtext are coherent with existing structure:

```bash
# Find the 10 most recently modified files
ls -t worldtext/**/*.md | head -10

# For each, check if it follows the established format
for f in $(ls -t worldtext/**/*.md | head -10); do
  species=$(grep -m1 'Species' "$f" | head -1)
  scale=$(grep -m1 'Scale' "$f" | head -1)
  revision=$(grep -m1 'Revision' "$f" | head -1)
  has_crosslinks=$(grep -c '\[\[' "$f")
  if [ -z "$species" ] || [ -z "$scale" ]; then
    echo "FORMAT VIOLATION: $f (missing Species or Scale)"
  fi
  if [ "$has_crosslinks" -eq 0 ]; then
    echo "ISOLATION: $f (no cross-links — not connected to cosmos)"
  fi
done
```

### 2. THEORY_HOLDER_TEST
Can a new operator (someone who has never seen this repo) make a coherent modification?

Test: Pick a random world page. Read only that page and the prime-prompt. Try to write a new entity page that belongs to that world. Check:
- Did the new page use the correct format?
- Did it link to the right worlds?
- Did it cite sources from the evidence base?
- Did it avoid contradicting existing pages?

If yes: theory is alive in the documentation.  
If no: theory lives only in the original builder's head. **This is Naur's death warning.**

### 3. PATCH_DETECTION
Find evidence of patching rather than coherent modification:
- Files that duplicate content from other files (the 3 imagetext→worldtext duplicates)
- Files that contradict other files without acknowledging the contradiction
- Files that use vocabulary not defined anywhere in the cosmos (invented terms)

```bash
# Detect duplicated content blocks (100+ char strings appearing in 2+ files)
for f in worldtext/syntheses/*.md; do
  grep -oh '.\{100,\}' "$f" | while read block; do
    matches=$(grep -rl "$block" worldtext/syntheses/*.md 2>/dev/null | wc -l)
    if [ "$matches" -gt 1 ]; then
      echo "DUPLICATION: $(echo $block | cut -c1-60)... ($matches files)"
    fi
  done
done
```

### 4. DEATH_AUDIT
Final question: if the original builder disappeared tomorrow, what would break?

```
ALIVE: pages that are self-explanatory (format + content + cross-links sufficient)
DYING: pages that reference unwritten context (broken links, unexplained terms)
DEAD:  pages that only the builder understands (no format, no links, no evidence base)
```

## Report Format

```
THEORY LIFE REPORT
==================
Files checked: 280
Format-compliant: 243 (87%)
Format-violating: 37 (13%)
Isolated (no cross-links): 12
Duplicate content blocks: 3
Invented terms (no definition page): 8
DEATH RISK: MEDIUM — format is strong but 37 files don't follow it, and 12 pages have no connections
```
