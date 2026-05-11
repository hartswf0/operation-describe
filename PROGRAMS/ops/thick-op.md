# THICK — Thickness Scanner (Operative)

> **Source theory**: thick.json  
> **Input**: Any .md file  
> **Output**: A thickness profile

## What It Does

THICK measures the descriptive density of any page against Geertz's six-layer model. A thin page has 1-2 layers. A thick page has 4-6. The scanner counts layers, not words.

## Operations

### 1. LAYER_COUNT
For any page, identify which of the 6 layers are present:

| Layer | Name | Detection |
|-------|------|-----------|
| 1 | **Visible act** | Does the page describe what something IS or DOES? (definitions, descriptions) |
| 2 | **Mood/atmosphere** | Does the page carry an emotional or aesthetic register? (metaphors, tone-setting sentences) |
| 3 | **Code** | Does the page invoke a tradition, genre, or disciplinary convention? (citations, theoretical lineage) |
| 4 | **Audience** | Does the page specify who evaluates this and by what standard? (methodology, governance) |
| 5 | **Context** | Does the page situate itself in a larger argument or project? (cross-links, system references) |
| 6 | **Reclassification** | Does the page change the category it belongs to? (claims that revise how we think about the type) |

```bash
TARGET="worldtext/worlds/world-thick-description.md"

L1=$(grep -c "definition\|ontology\|what it\|what this\|describes\|constitutes" "$TARGET")
L2=$(grep -c "atmosphere\|mood\|feel\|tone\|sense of\|air of\|close to\|patient\|dense" "$TARGET")
L3=$(grep -c "Geertz\|Ryle\|Murdoch\|Barad\|tradition\|lineage\|method\|approach" "$TARGET")
L4=$(grep -c "evaluate\|standard\|peer review\|governance\|adequate\|sufficient" "$TARGET")
L5=$(grep -c "\[\[\|cross-link\|cosmos\|system\|connected to\|relates to" "$TARGET")
L6=$(grep -c "however\|but\|not merely\|revise\|transform\|reclassify\|redefine\|challenge" "$TARGET")

echo "THICKNESS PROFILE: $(basename $TARGET)"
echo "  L1 (Act):             $L1"
echo "  L2 (Mood):            $L2"
echo "  L3 (Code):            $L3"
echo "  L4 (Audience):        $L4"
echo "  L5 (Context):         $L5"
echo "  L6 (Reclassification): $L6"
total=$((($L1 > 0) + ($L2 > 0) + ($L3 > 0) + ($L4 > 0) + ($L5 > 0) + ($L6 > 0)))
echo "  LAYERS ACTIVE: $total/6"
```

### 2. THIN_ALERT
Flag any page with fewer than 3 active layers. These are the thin descriptions — pages with definitions but no mood, no tradition, no audience, no reclassification.

### 3. COMPARATIVE_THICKNESS
Run the scanner across all pages in a directory and rank them:

```bash
for f in worldtext/worlds/*.md; do
  layers=0
  [ $(grep -c "ontology\|definition\|what" "$f") -gt 0 ] && layers=$((layers+1))
  [ $(grep -c "atmosphere\|mood\|tone" "$f") -gt 0 ] && layers=$((layers+1))
  [ $(grep -c "Geertz\|Ryle\|tradition\|method" "$f") -gt 0 ] && layers=$((layers+1))
  [ $(grep -c "governance\|evaluate\|standard" "$f") -gt 0 ] && layers=$((layers+1))
  [ $(grep -c "\[\[" "$f") -gt 0 ] && layers=$((layers+1))
  [ $(grep -c "however\|but \|revise\|challenge" "$f") -gt 0 ] && layers=$((layers+1))
  echo "$layers layers → $(basename $f .md)"
done | sort -rn
```

## Report Format

```
THICKNESS REPORT: worldtext/worlds/
===================================
6/6 layers: world-thick-description, world-operative-ekphrasis
5/6 layers: world-embodied-description, world-latent-wrestling
4/6 layers: world-classical-ekphrasis, world-prompt-craft
3/6 layers: world-shield-of-achilles, world-latent-space
2/6 layers: world-world-models, world-digital-poetics ← THIN ALERT
1/6 layers: world-academic-ekphrasis ← CRITICALLY THIN
```
