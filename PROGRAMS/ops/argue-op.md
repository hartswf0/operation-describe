# ARGUE — Argument vs. Thought Detector (Operative)

> **Source theory**: argue.json  
> **Input**: Any synthesis .md file  
> **Output**: A process-vs-product report

## What It Does

ARGUE is Ryle's detective. It asks: **is this synthesis a report or an investigation?** A report presents clean conclusions in logical order. An investigation shows the mess: false starts, shifts of attention, re-framings, dead ends. The report deceives us about the activity that produced it.

## Operations

### 1. RETROSPECTIVE_DETECTOR
Scan for language that reconstructs rather than discovers:
- **Retrospective markers**: "as we saw," "as established above," "it follows that," "therefore," "thus," "consequently," "clearly" — language that presents a chain of reasoning as if it were the process of reasoning
- **Discovery markers**: "surprisingly," "this suggests," "unexpectedly," "on closer reading," "we initially thought... but," "the first attempt showed" — language that preserves the struggle

`discovery_ratio = discovery_markers / (discovery_markers + retrospective_markers)`

A synthesis with discovery_ratio < 0.2 is a **polished report disguised as thinking**. Ryle would say: the argument is not the thought.

### 2. DEAD_END_PRESERVATION
Check if the synthesis contains any of these signs of preserved process:
- **Contradictions acknowledged**: "this seems to contradict..."
- **Failed approaches mentioned**: "the initial approach was to..."
- **Questions left open**: "what remains unclear is..."
- **Alternative paths noted**: "another possibility would be..."

Count: `preserved_process = contradictions + failed_approaches + open_questions + alternatives`

If `preserved_process == 0`, the synthesis has erased all evidence of thought. It is pure report.

### 3. VERSION_AUDIT
Check if earlier versions of the same synthesis exist (like our three imagetext→worldtext documents):

```bash
# Find version pairs
for f in worldtext/syntheses/*.md; do
  base=$(basename "$f" .md | sed 's/-v[0-9]*$//')
  matches=$(ls worldtext/syntheses/${base}*.md 2>/dev/null | wc -l)
  if [ "$matches" -gt 1 ]; then
    echo "VERSION SET: $base ($matches versions)"
    ls worldtext/syntheses/${base}*.md
  fi
done
```

If versions exist, the PROCESS is accidentally preserved. The argue.json theory says this is valuable — the versions ARE the thought that the final report conceals.

### 4. THE RYLE FLAG
For any section that begins with "It is clear that..." or "Obviously..." or "As we have shown..." — flag it. This is the retrospective voice at its most confident. At these exact points, the real thinking has been most thoroughly hidden.

## Report Format

```
ARGUE REPORT: operative-ethnography.md
=====================================
Discovery ratio: 0.31 (marginal — some process preserved)
Retrospective markers: 14
Discovery markers: 6
Dead ends preserved: 2 ("the initial framing as 'fieldwork'...")
Open questions: 3
Contradictions acknowledged: 1
RYLE FLAGS: 4 ("It is clear that...", "Obviously...", "As established...")
VERSION SETS: none found
VERDICT: MIXED — synthesis preserves some struggle but defaults to report voice in sections 3, 5, 7
```
