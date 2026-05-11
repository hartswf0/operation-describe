# DAC — Breakdown & Commitment Detector (Operative)

> **Source theory**: dac.json  
> **Input**: The worldtext directory  
> **Output**: A breakdown report and commitment audit

## What It Does

DAC is Winograd & Flores's repair crew. It asks: **where has the system broken down, and who is responsible for the repair?** Every broken link, every contradiction, every undefined term is a breakdown. The question is whether the breakdown is visible (good — it reveals structure) or invisible (bad — it corrodes silently).

## Operations

### 1. BREAKDOWN_MAP
List all visible breakdowns in the worldtext:
- **Broken links**: `[[targets]]` with no page (11 remaining)
- **Contradictions**: claims in one synthesis that conflict with claims in another
- **Format violations**: pages missing Species, Scale, or Last Revision
- **Orphan pages**: pages that no other page links to
- **Dead worlds**: worlds with 0 synthesis references

```bash
# Run full breakdown scan
echo "=== BROKEN LINKS ===" 
# (use the crosslink script from above)

echo "=== FORMAT VIOLATIONS ==="
for f in worldtext/**/*.md; do
  if ! grep -q 'Species\|Scale' "$f" 2>/dev/null; then
    echo "  FORMAT: $(basename $f)"
  fi
done

echo "=== ORPHAN PAGES ==="
for f in worldtext/worlds/*.md worldtext/entities/*.md worldtext/concepts/*.md; do
  name=$(basename "$f" .md)
  refs=$(grep -rl "\[\[$name\]\]" worldtext/ 2>/dev/null | grep -v "$f" | wc -l)
  if [ "$refs" -eq 0 ]; then
    echo "  ORPHAN: $name"
  fi
done
```

### 2. COMMITMENT_AUDIT
For each synthesis, check:
- **Who committed?** Does the synthesis declare its author or session?
- **What was promised?** Does it state what it will demonstrate?
- **Was it fulfilled?** Does the conclusion match the stated goal?
- **Who repairs?** If the synthesis has broken links, is there a responsible party?

### 3. REPAIR_QUEUE
Generate a prioritized repair list:
1. **Critical**: Broken links referenced by 3+ other pages
2. **High**: Orphan pages (exist but disconnected)
3. **Medium**: Format violations
4. **Low**: One-way trails (linked but no backlink)

### 4. HAMMER_TEST (Heideggerian)
Pick a random page. "Break" it by removing one section. Does the breakage reveal the structure?
- What pages link to this page?
- What pages does this page link to?
- What would become orphaned if this page disappeared?

This test reveals the structural importance of each page. A page whose removal would orphan many others is load-bearing. A page whose removal would orphan nothing is cosmetic.

## Report Format

```
DAC BREAKDOWN REPORT
====================
Broken links: 11
Format violations: [count]
Orphan pages: [count]
Dead worlds: 1 (world-academic-ekphrasis)
Total breakdowns: [sum]
Visible breakdowns (already flagged in syntheses): [count]
Invisible breakdowns (discovered only by audit): [count]

REPAIR QUEUE:
  CRITICAL: [[concept-thick-prompting]] — now resolved
  HIGH: world-academic-ekphrasis — 0 references, absorb into world-classical-ekphrasis
  MEDIUM: 37 format-violating pages
  LOW: 45 one-way trails
```
