# MEMEX — Memex Trail Auditor (Operative)

> **Source theory**: memex.json  
> **Input**: The entire worldtext directory  
> **Output**: A trail integrity report

## What It Does

MEMEX is Bush's trail inspector. It checks whether a reader can trace any claim backwards through the worldtext to its origin. The trail: synthesis → entity → source → paper. Every broken link is a broken trail.

## Operations

### 1. TRAIL_TRACE
For a given synthesis, extract all [[wiki-links]] and check:
- Does the target page exist?
- Does the target page link back? (bidirectional trail)
- Can you reach a PAPERS/*.md file within 3 hops?

```bash
# Trace trails from a synthesis
SYNTH="worldtext/syntheses/operative-ethnography.md"
grep -oh '\[\[[^]]*\]\]' "$SYNTH" | sed 's/\[\[//;s/\]\]//' | while read target; do
  # Check if target exists anywhere
  found=$(find worldtext -name "$target.md" 2>/dev/null | head -1)
  if [ -z "$found" ]; then
    echo "BROKEN TRAIL: $target"
  else
    # Check if target links back to this synthesis
    backlink=$(grep -c "$(basename $SYNTH .md)" "$found" 2>/dev/null)
    if [ "$backlink" -eq 0 ]; then
      echo "ONE-WAY TRAIL: $target (no backlink)"
    else
      echo "COMPLETE TRAIL: $target ↔ $(basename $SYNTH)"
    fi
  fi
done
```

### 2. PAPER_DISTANCE
For each synthesis, measure how many hops it takes to reach a source paper (PAPERS/*.md):
- **Distance 0**: synthesis directly quotes or cites a paper by filename
- **Distance 1**: synthesis links to entity, entity has evidence base citing paper
- **Distance 2**: synthesis links to world, world links to entity, entity cites paper  
- **Distance ∞**: no traceable path to any paper

```bash
# Check paper distance
SYNTH="worldtext/syntheses/kiki-or-bouba.md"
# Direct paper references
grep -c "PAPERS/\|\.md.*source\|Evidence Base" "$SYNTH"
# Entity references that might bridge to papers
grep -oh '\[\[entity-[^]]*\]\]' "$SYNTH" | sed 's/\[\[//;s/\]\]//' | while read ent; do
  entfile=$(find worldtext/entities -name "$ent.md" 2>/dev/null | head -1)
  if [ -n "$entfile" ]; then
    paper_refs=$(grep -c "PAPERS/\|Evidence Base\|source" "$entfile")
    echo "  $ent → $paper_refs paper references"
  fi
done
```

### 3. ORPHAN_DETECTION
Find pages that are linked TO by no other page. These are orphans — they exist but nobody points at them.

```bash
# Find pages that nobody links to
for f in worldtext/worlds/*.md worldtext/entities/*.md worldtext/concepts/*.md; do
  name=$(basename "$f" .md)
  refs=$(grep -rl "\[\[$name\]\]" worldtext/ 2>/dev/null | wc -l)
  if [ "$refs" -le 1 ]; then  # Only self-reference or nothing
    echo "ORPHAN: $name ($refs references)"
  fi
done
```

### 4. TRAIL_DENSITY
Score the worldtext's overall trail integrity:

`trail_density = resolved_links / total_links`

We already know: 120 resolved / 131 total = 91.6% trail density (after repairs).

## Report Format

```
MEMEX TRAIL REPORT
==================
Total unique link targets: 131
Resolved: 120 (91.6%)
Broken: 11 (8.4%)
One-way trails: [count]
Complete (bidirectional) trails: [count]
Orphan pages: [count]
Average paper distance: [hops]
```
