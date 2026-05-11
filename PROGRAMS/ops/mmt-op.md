# MMT — Model Measure Tractatus (Operative)

> **Source theory**: mmt.json  
> **Input**: Any claim in the worldtext  
> **Output**: A contact report measuring whether the claim touches reality

## What It Does

MMT is Wittgenstein's measuring rod. It takes a claim and asks: **does this proposition make contact with the reality it claims to describe?** Contact means: the claim can be laid against something specific and tested for fit or failure.

## Operations

### 1. CONTACT_TEST
For a given claim in a synthesis, find:
- **Source grounding**: Does the claim cite a specific source? Which paper? What page?
- **Entity grounding**: Does the claim reference a named thinker whose position can be verified?
- **World grounding**: Does the claim connect to a world page that has its own evidence base?
- **Repo grounding**: Can the claim be tested against actual files in the repo?

Run:
```bash
# For a specific claim, check if its referenced entities exist
CLAIM="operative ekphrasis requires the six-layer formula"
grep -rl "six-layer\|six layer\|6.*layer" worldtext/syntheses/*.md worldtext/worlds/*.md
# Check if the source paper supports this claim
grep -c "six.*layer\|layer.*six" PAPERS/*.md
```

### 2. MEASURE_CALIBRATION
For each synthesis, count:
- **Calibrated claims**: claims with source citations, page numbers, or direct quotes
- **Uncalibrated claims**: claims presented as facts with no source trail

`calibration_ratio = calibrated / (calibrated + uncalibrated)`

A synthesis with calibration_ratio < 0.3 has lost contact with reality. Its language floats.

### 3. PROJECTION_AUDIT
Check if the synthesis's claims can be **projected back** onto the source papers. For each key term in the synthesis:
- Does the key term appear in the source paper?
- If not, the synthesis has INVENTED a term and attributed it to the source. This is a projection failure — the model does not match the territory.

Run:
```bash
# Check if synthesis terms exist in source papers
SYNTH="worldtext/syntheses/thick-description-of-operative-ekphrasis.md"
SOURCE="PAPERS/geertz.md"
# Extract key terms from synthesis (capitalized multi-word phrases)
grep -oh '[A-Z][a-z]* [A-Z][a-z]*' "$SYNTH" | sort -u | while read term; do
  if ! grep -q "$term" "$SOURCE" 2>/dev/null; then
    echo "PROJECTION FAILURE: '$term' in synthesis but not in source"
  fi
done
```

### 4. FIT_OR_FAILURE
For each claim, declare:
- **FIT**: claim is grounded AND source supports it
- **MISMATCH**: claim is grounded but source says something different
- **FLOAT**: claim has no source contact — it is neither true nor false, just unmoored

## Report Format

```
MMT CONTACT REPORT: thick-description-of-operative-ekphrasis.md
==============================================
Claims found: 23
Calibrated: 14 (61%)
Uncalibrated: 9 (39%)
Projection failures: 3 ("operative cut" not in Geertz, "reclassification cascade" not in Ryle, "wound-sorting" not in any source)
Verdict: PARTIAL CONTACT — synthesis has grounding but has invented 3 terms attributed to sources that don't use them
```
