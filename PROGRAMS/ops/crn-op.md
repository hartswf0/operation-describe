# CRN — Cluster & Ritual Network Mapper (Operative)

> **Source theory**: crn.json  
> **Input**: The worldtext directory  
> **Output**: A network topology report

## What It Does

CRN maps the actual network of the worldtext — which pages connect to which, where the clusters are, where the gaps are. It is the cluster_worlds operation made permanent.

## Operations

### 1. ADJACENCY_MATRIX
Build a co-occurrence matrix: for every pair of worlds, count how many syntheses reference both.

```bash
worlds=$(ls worldtext/worlds/ | sed 's/\.md//')
for w1 in $worlds; do
  for w2 in $worlds; do
    if [ "$w1" != "$w2" ]; then
      co=$(grep -rl "\[\[$w1\]\]" worldtext/syntheses/*.md 2>/dev/null | \
           xargs grep -l "\[\[$w2\]\]" 2>/dev/null | wc -l)
      if [ "$co" -gt 2 ]; then
        echo "$co co-occurrences: $w1 ←→ $w2"
      fi
    fi
  done
done | sort -rn | head -20
```

### 2. HUB_DETECTION
Find the most-connected pages (highest in-degree):

```bash
for f in worldtext/**/*.md; do
  name=$(basename "$f" .md)
  refs=$(grep -rl "\[\[$name\]\]" worldtext/ 2>/dev/null | wc -l)
  echo "$refs refs → $name"
done | sort -rn | head -20
```

### 3. BRIDGE_DETECTION
Find pages that connect otherwise separate clusters. A bridge is a page that links to pages in 2+ different clusters but is the only connection between them.

### 4. RITUAL_MAP
List all ritual pages and check which worlds reference them:

```bash
for r in worldtext/rituals/*.md; do
  name=$(basename "$r" .md)
  worlds=$(grep -rl "\[\[$name\]\]" worldtext/worlds/*.md 2>/dev/null | xargs -I{} basename {} .md | tr '\n' ', ')
  echo "$name → $worlds"
done
```
