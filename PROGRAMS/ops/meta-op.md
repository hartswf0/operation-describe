# META-OP — Master Diagnostician

> **Source theory**: meta.json  
> **Input**: The entire OPERATION-DESCRIBE repository  
> **Output**: A full system health report

## What It Does

META-OP runs all 9 operative programs against the repo and produces a single diagnostic.

## The 9 Programs

| Program | Named After | What It Measures | Command |
|---------|------------|-----------------|---------|
| **DSE** | Murdoch/Ryle | Descriptive struggle — did the language cost something? | Pressure scan, cliché detection |
| **MMT** | Wittgenstein | Contact — does the claim touch its source? | Citation audit, projection test |
| **MEMEX** | Bush | Trail integrity — can you trace any claim to its origin? | Link resolution, orphan detection |
| **ARGUE** | Ryle | Process preservation — is this a report or an investigation? | Discovery ratio, dead-end count |
| **HAUNTED** | Calvino | Ghost detection — does the text exceed its template? | Content ratio, surplus scan |
| **THEORY** | Naur | Theory life — can a newcomer modify this coherently? | Format compliance, coherence test |
| **DAC** | Winograd/Flores | Breakdown mapping — where is the system broken? | Breakdown list, repair queue |
| **THICK** | Geertz | Thickness — how many layers does this description carry? | Layer count per page |
| **RCP** | Ryle | Concept mastery — is the concept used or just defined? | Possession test per concept |
| **TENNE** | Bajohr | Vocabulary health — is the term operative or dead? | Dead term scan, bleaching check |
| **CRN** | Calvino/Geertz | Network topology — what connects to what? | Adjacency matrix, hub detection |

## Full System Run

```bash
#!/bin/bash
# META-OP: Run all diagnostics

REPO="/Users/gaia/OPERATION-DESCRIBE"
WT="$REPO/worldtext"

echo "================================================"
echo "META-OP DIAGNOSTIC — $(date)"
echo "================================================"

# 1. INVENTORY
echo ""
echo "=== INVENTORY ==="
for dir in $WT/*/; do
  count=$(ls "$dir" 2>/dev/null | grep -c '.md$')
  echo "  $count pages → $(basename $dir)"
done
total=$(find $WT -name "*.md" | wc -l)
echo "  TOTAL: $total pages"

# 2. MEMEX — Trail integrity
echo ""
echo "=== MEMEX: TRAIL INTEGRITY ==="
broken=0
resolved=0
for target in $(grep -roh '\[\[[^]]*\]\]' $WT/syntheses/*.md | sed 's/\[\[//;s/\]\]//;s/|.*//' | sort -u); do
  found=0
  for dir in $WT/*/; do
    [ -f "$dir$target.md" ] && found=1 && break
  done
  [ "$found" -eq 1 ] && resolved=$((resolved+1)) || broken=$((broken+1))
done
echo "  Resolved: $resolved"
echo "  Broken: $broken"
pct=$((resolved * 100 / (resolved + broken)))
echo "  Trail density: ${pct}%"

# 3. TENNE — Vocabulary health
echo ""
echo "=== TENNE: VOCABULARY ==="
dead=0
for f in $WT/concepts/*.md $WT/distinctions/*.md; do
  name=$(basename "$f" .md)
  refs=$(grep -rl "\[\[$name\]\]" $WT/ 2>/dev/null | grep -v "$f" | wc -l)
  [ "$refs" -eq 0 ] && dead=$((dead+1)) && echo "  DEAD: $name"
done
echo "  Dead terms: $dead"

# 4. THICK — World thickness
echo ""
echo "=== THICK: WORLD THICKNESS ==="
for f in $WT/worlds/*.md; do
  wc=$(wc -w < "$f" | tr -d ' ')
  name=$(basename "$f" .md)
  if [ "$wc" -lt 300 ]; then
    echo "  THIN ($wc words): $name"
  fi
done

# 5. DAC — Orphan detection
echo ""
echo "=== DAC: ORPHANS ==="
for f in $WT/worlds/*.md; do
  name=$(basename "$f" .md)
  refs=$(grep -rl "\[\[$name\]\]" $WT/syntheses/*.md 2>/dev/null | wc -l | tr -d ' ')
  [ "$refs" -eq 0 ] && echo "  ORPHAN WORLD: $name"
done

echo ""
echo "================================================"
echo "META-OP COMPLETE"
echo "================================================"
```

## How to Run

```bash
bash PROGRAMS/ops/meta-run.sh
```

## What Each Program Does to the Repo

| Program | READS | WRITES | JUDGES |
|---------|-------|--------|--------|
| DSE | syntheses | struggle report | was this language forced? |
| MMT | syntheses + papers | contact report | does this claim touch its source? |
| MEMEX | all wiki-links | trail report | can you trace this? |
| ARGUE | syntheses | process report | is this a report or an investigation? |
| HAUNTED | any page | ghost report | does this exceed its template? |
| THEORY | all pages | life report | can a newcomer extend this? |
| DAC | all pages | breakdown report | where is the system broken? |
| THICK | any page | thickness profile | how many layers? |
| RCP | concepts/entities | possession report | is this concept used or just defined? |
| TENNE | all page names | vocabulary report | is this term alive or dead? |
| CRN | all pages | network report | what connects to what? |
