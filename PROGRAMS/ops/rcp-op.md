# RCP — Concept Possession Test (Operative)

> **Source theory**: rcp.json  
> **Input**: Any entity, concept, or distinction page  
> **Output**: A possession report

## What It Does

RCP is Ryle's concept examiner. It asks: **does the page demonstrate mastery of the concept it names, or does it merely define it?** Knowing a concept (Ryle) means being able to use it, apply it, correct errors involving it, recognize instances, distinguish cases, and explain it to someone who doesn't have it.

## Operations

### 1. POSSESSION_TEST
For a concept or entity page, check if it demonstrates:
- **Use**: Is the concept applied to at least one specific case? (not just defined)
- **Negative case**: Does the page show what the concept is NOT? (distinguishing cases)
- **Error correction**: Does the page show what would go wrong if the concept were misused?
- **Transfer**: Does the page show how the concept applies outside its home domain?

```bash
TARGET="worldtext/concepts/concept-viscosity.md"
use=$(grep -c "for example\|such as\|in the case of\|when\|consider" "$TARGET")
negative=$(grep -c "not\|never\|unlike\|contrast\|differ\|opposite\|versus\|vs\." "$TARGET")
error=$(grep -c "fail\|wrong\|mistake\|misuse\|error\|danger\|risk\|problem" "$TARGET")
transfer=$(grep -c "also applies\|extends\|beyond\|other domain\|in .* too\|similarly" "$TARGET")

echo "POSSESSION: use=$use, negative=$negative, error=$error, transfer=$transfer"
total=$((($use > 0) + ($negative > 0) + ($error > 0) + ($transfer > 0)))
echo "MASTERY: $total/4"
```

### 2. PARROT_DETECTOR
A page that only DEFINES a concept (gives its name and a one-line gloss) without using it is a parrot — it can repeat the word but doesn't possess the concept.

Flag any concept/entity page under 150 words with no examples, no cross-links, and no error cases.

## Report Format

```
RCP POSSESSION REPORT: worldtext/concepts/
==========================================
FULL MASTERY (4/4): concept-viscosity, concept-platform-realism
PARTIAL (2-3/4): concept-worldtext, concept-text-as-control-signal
PARROT (0-1/4): concept-operative-ecologies, concept-pictorial-third
```
