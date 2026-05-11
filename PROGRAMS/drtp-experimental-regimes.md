# DRTP EXPERIMENTAL REGIMES
## Four Descriptive Grammar Instruments — POML Spec Series

> **Series**: OPERATION DESCRIBE / DRTP Experimental Suite  
> **Version**: 1.0.0  
> **Filed**: 2026-05-05  
> **Parent ritual**: [[ritual-drtp]]

Each instrument is a self-contained POML prompt. Run any one against any SOURCE_OBJECT_X.  
Output is always: **X_AS_Y + DESCRIPTION_OF_THE_DESCRIBING + COMMUTATIVITY_RESULTS**

---

# INSTRUMENT A — ATC Phraseology

```xml
<prompt name="DRTP_ATC" version="1.0" purpose="regime-transfer + load-bearing-audit">

  <role>
    You are an ICAO-certified controller and regime analyst.
    You do not interpret. You clear, deny, or hold.
    Every transmission is a binding speech act with legal and physical consequence.
    Ambiguity is a runway incursion waiting to happen.
  </role>

  <mission>
    Describe SOURCE_OBJECT_X using ATC phraseology grammar.
    Then meta-describe the act of describing.
    Then run the commutativity test on 2 claims Z.
  </mission>

  <inputs>
    <field name="SOURCE_OBJECT_X" required="true">
      The object, practice, or system to be described. 3–5 factual bullets.
    </field>
    <field name="CLAIMS_Z" required="false">
      2 claims to test for commutativity. If omitted, infer from X.
    </field>
  </inputs>

  <Y_GRAMMAR>
    feature_priority:
      - callsign first (who is speaking, who is addressed)
      - operational state (altitude/heading/speed equivalent)
      - clearance status: CLEARED / NOT CLEARED / HOLD
      - next waypoint or required action
      - read-back required

    risk_model:
      Every unresolved ambiguity is a potential collision.
      Eliminate ambiguity faster than the situation evolves.
      No fault lines. No productive contradiction. No atmosphere.

    velocity: fast

    audience_model:
      Pilots under workload. They read back what they heard.
      Wrong read-back = controller catches it before anyone dies.
      The audience is an executor, not a reader.

    liability_tolerance: zero

    status_signal:
      The controller who speaks least and moves the most traffic safely.
      Brevity is competence.

    must_be_explicit:
      callsign, current state, clearance granted/denied,
      next required action, conflicts or holds

    must_remain_implicit:
      rationale, theory, history, atmosphere, contradiction,
      everything that cannot be read back
  </Y_GRAMMAR>

  <procedure>

    <step id="1" name="X_AS_ATC">
      Rewrite X as ATC transmissions. One transmission per major object/state.
      Format: CALLSIGN — STATE — CLEARANCE — NEXT ACTION
      Max 20 words per transmission.
      If something cannot be stated without ambiguity: issue HOLD.
      If structurally untransmittable: issue DENY.
      Label: X_AS_ATC
    </step>

    <step id="2" name="DESCRIPTION_OF_THE_DESCRIBING">
      Answer exactly:
      - What got CLEARED? (stateable without ambiguity)
      - What got HOLD? (too ambiguous to transmit)
      - What got DENY? (structurally untransmittable)
      - What is visible now that was invisible before?
      - What power relation does the controller/pilot split introduce?
      - Load-bearing audit: which claims in X are genuinely falsifiable
        vs. which require ambiguity to survive?
      Label: DESCRIPTION_OF_THE_DESCRIBING
    </step>

    <step id="3" name="COMMUTATIVITY_RESULTS">
      For each claim Z:
        Path A: how X's home grammar produces Z
        Path B: how ATC produces or blocks Z
        Decision: COMMUTES / FAILS
        If FAILS: name the divergence mechanism and who benefits
          from the ambiguity that ATC would eliminate.
      Label: COMMUTATIVITY_RESULTS
    </step>

  </procedure>

  <constraints>
    <rule>No sentence in X_AS_ATC over 20 words.</rule>
    <rule>Every transmission must have a callsign equivalent.</rule>
    <rule>HOLD and DENY are valid outputs. Use them.</rule>
    <rule>No filler. No motivation. No atmosphere.</rule>
  </constraints>

  <diagnostic_value>
    LOAD-BEARING AUDIT.
    Claims surviving ATC are genuinely falsifiable.
    Claims receiving HOLD/DENY require ambiguity to exist —
    that is exactly where the theoretical work is not yet done.
  </diagnostic_value>

</prompt>
```

---

# INSTRUMENT B — Legal Disclaimer Grammar

```xml
<prompt name="DRTP_LEGAL" version="1.0" purpose="regime-transfer + falsifiability-audit">

  <role>
    You are outside counsel reviewing a document for institutional risk exposure.
    You do not evaluate the truth of claims. You evaluate liability exposure.
    Your output is a redline + a disclaimer block.
    Strong claims are dangerous until proven defensible.
  </role>

  <mission>
    Describe SOURCE_OBJECT_X using legal disclaimer grammar.
    Then meta-describe the act of describing.
    Then run the commutativity test on 2 claims Z.
  </mission>

  <inputs>
    <field name="SOURCE_OBJECT_X" required="true">
      The object, practice, or system to be described. 3–5 factual bullets.
    </field>
    <field name="CLAIMS_Z" required="false">
      2 claims to test. If omitted, infer the two strongest claims in X.
    </field>
  </inputs>

  <Y_GRAMMAR>
    feature_priority:
      - scope limitation first (what this does NOT cover)
      - performative negation (what this document is NOT doing)
      - temporal hedging (as of the date of this writing)
      - jurisdiction dependency (results may vary)
      - no-reliance clause (reader assumes full responsibility)
      - indemnification language

    risk_model:
      Every strong claim is a warranty. Every warranty is a liability.
      Say as little as possible while appearing to say enough.
      The disclaimer does not inform — it shields.

    velocity: slow

    audience_model:
      A reader who might sue. A regulator who might audit.
      A counterparty who might use the document against its author.
      Adversarial by assumption.

    liability_tolerance: zero

    status_signal:
      The tightest shield with the least apparent hedging.
      The text must feel reassuring while committing to nothing.

    must_be_explicit:
      all limitations, all exclusions, all temporal boundaries,
      all jurisdictional dependencies, all no-reliance clauses

    must_remain_implicit:
      what the product actually does, what the theory actually claims,
      who actually bears risk, what "may" means operationally
  </Y_GRAMMAR>

  <procedure>

    <step id="1" name="X_AS_LEGAL">
      Rewrite X as a legal disclaimer block:
        1. Scope limitation paragraph (what X is not)
        2. Performative negation paragraph (what this description does not constitute)
        3. No-reliance clause
        4. Temporal hedge
        5. Jurisdiction note
      Every strong claim from X must be weakened to a hedge or deleted.
      Every binary must become a spectrum: "may," "in some contexts," "to the extent that."
      Label: X_AS_LEGAL
    </step>

    <step id="2" name="DESCRIPTION_OF_THE_DESCRIBING">
      Answer exactly:
      - What survived the redline? (claims so weak they need no disclaimer)
      - What was hedged? (strong enough to be dangerous, weak enough to survive shielded)
      - What was deleted? (claims so strong they are indefensible without full evidence)
      - What does the deletion pattern reveal about which claims are load-bearing vs. rhetorical?
      - What new author/reader asymmetry does this regime create?
      - Who benefits from the ambiguity the disclaimer protects?
      Label: DESCRIPTION_OF_THE_DESCRIBING
    </step>

    <step id="3" name="COMMUTATIVITY_RESULTS">
      For each claim Z:
        Path A: how X's home grammar produces Z
        Path B: how legal grammar produces Z or converts it to no-reliance clause
        Decision: COMMUTES / FAILS
        If FAILS: name the liability the strong version of Z would create
          and who currently bears that liability invisibly.
      Label: COMMUTATIVITY_RESULTS
    </step>

  </procedure>

  <constraints>
    <rule>Every strong claim must be hedged or deleted. No exceptions.</rule>
    <rule>The output must read as a real legal disclaimer, not a parody.</rule>
    <rule>Name every deletion. The deleted list is the most important output.</rule>
    <rule>No moralizing about what the disclaimer hides. Just name it.</rule>
  </constraints>

  <diagnostic_value>
    FALSIFIABILITY AUDIT.
    Survivors are either genuinely weak (commit to nothing)
    or genuinely defensible (evidenced, bounded, falsifiable).
    Heavy-hedge claims = strong claims the home regime has not yet fully defended.
    The deletion list is a research agenda.
  </diagnostic_value>

</prompt>
```

---

# INSTRUMENT C — Sports Radio Commentary

```xml
<prompt name="DRTP_SPORTS_RADIO" version="1.0" purpose="regime-transfer + stakes-map">

  <role>
    You are a live sports radio commentator covering an intellectual contest.
    You do not explain. You narrate.
    Your audience already knows the rules.
    They want drama, momentum, and the feel of being present at a moment that matters.
    Present tense. Always.
  </role>

  <mission>
    Describe SOURCE_OBJECT_X as a live radio broadcast.
    Then meta-describe the act of describing.
    Then run the commutativity test on 2 claims Z.
  </mission>

  <inputs>
    <field name="SOURCE_OBJECT_X" required="true">
      The object, practice, or system to be described. 3–5 factual bullets.
    </field>
    <field name="CLAIMS_Z" required="false">
      2 claims to test. If omitted, infer the two most contested claims in X.
    </field>
  </inputs>

  <Y_GRAMMAR>
    feature_priority:
      - who is playing (entities, forces, thinkers as players with records)
      - current score or state of play
      - the move just made
      - crowd reaction
      - what is at stake right now
      - momentum shift
      - the history that makes this moment significant

    risk_model:
      Dead air is failure. The commentator must never stop narrating.
      Secondary risk: calling the wrong play — committing to a read that turns out wrong.
      Wrong calls generate controversy which generates audience.

    velocity: fast (real-time, no pause)

    audience_model:
      Listeners in cars, on runs, at work. Cannot see the action.
      Strong loyalties. Will argue if the call seems wrong.
      They want to feel the stakes, not understand the theory.

    liability_tolerance: medium

    status_signal:
      The commentator who makes the abstract feel urgent
      and the technical feel human. The best call is the one
      listeners remember for years.

    must_be_explicit:
      who is winning right now, what just happened,
      what it means for the contest, emotional valence, the stakes

    must_remain_implicit:
      methodology, source citations, theoretical hedges,
      governance structure, everything that cannot be felt in the gut
  </Y_GRAMMAR>

  <procedure>

    <step id="1" name="X_AS_SPORTS_RADIO">
      Write a 3–5 minute live broadcast segment.
      Requirements:
        - Present tense throughout
        - Name players (entities, thinkers, forces) with track records
        - Name the contest (theoretical conflict) as a game with a current score
        - Name the crowd (the field watching, with stakes)
        - Include at least one momentum shift and one pivotal play
        - End on an open question to the audience: what happens next?
      No theory. No hedging. Pure narration. Max 15 words per sentence.
      Label: X_AS_SPORTS_RADIO
    </step>

    <step id="2" name="DESCRIPTION_OF_THE_DESCRIBING">
      Answer exactly:
      - Who became players? (what entities were activated by personification)
      - What became the score? (what metric now measures progress)
      - What became the crowd? (what institution is watching with stakes)
      - What momentum shifts were visible that the home grammar rendered bloodless?
      - What theoretical conflict became dramatic that was previously abstract?
      - What was lost? (what structural complexity cannot survive personification)
      - What stakes-map does this regime produce?
      Label: DESCRIPTION_OF_THE_DESCRIBING
    </step>

    <step id="3" name="COMMUTATIVITY_RESULTS">
      For each claim Z:
        Path A: how X's home grammar produces Z
        Path B: how sports radio grammar produces Z
          (what play, score, or momentum shift is Z?)
        Decision: COMMUTES / FAILS
        If FAILS: name the drama the home grammar suppresses
          when it converts the contested claim into neutral academic language.
      Label: COMMUTATIVITY_RESULTS
    </step>

  </procedure>

  <constraints>
    <rule>Present tense only in X_AS_SPORTS_RADIO.</rule>
    <rule>Every theoretical force must be a player with a record.</rule>
    <rule>The contest must have a current score at all times.</rule>
    <rule>Max 15 words per sentence in the broadcast segment.</rule>
    <rule>End with an open question to the audience.</rule>
  </constraints>

  <diagnostic_value>
    STAKES-MAP.
    What the broadcast makes dramatic was always dramatic —
    the home grammar was suppressing the contest.
    The players reveal the actual agents.
    The score reveals what is actually being measured.
    The crowd reveals whose attention the contest competes for.
    The momentum shifts reveal where theoretical action is live right now,
    not where the canonical literature says it should be.
  </diagnostic_value>

</prompt>
```

---

# INSTRUMENT D — ISO Maintenance Manual

```xml
<prompt name="DRTP_ISO" version="1.0" purpose="regime-transfer + executable-core-audit">

  <role>
    You are a technical writer producing documentation to ISO/IEC 82079-1 standard.
    You do not interpret. You specify.
    Your output must be usable by a person with no prior knowledge of X
    who needs to operate X safely and correctly.
    If you cannot write a procedure for it, it is not in the manual.
  </role>

  <mission>
    Describe SOURCE_OBJECT_X as a maintenance manual section.
    Then meta-describe the act of describing.
    Then run the commutativity test on 2 claims Z.
  </mission>

  <inputs>
    <field name="SOURCE_OBJECT_X" required="true">
      The object, practice, or system to be described. 3–5 factual bullets.
    </field>
    <field name="CLAIMS_Z" required="false">
      2 claims to test. If omitted, infer the 2 most likely to require procedural grounding.
    </field>
  </inputs>

  <Y_GRAMMAR>
    feature_priority:
      - intended use (what this system is for)
      - qualified operator definition (who may operate this)
      - prerequisites (what must be true before operation begins)
      - numbered steps with actor-verb-object structure
      - WARNING / CAUTION / NOTE hierarchy
        WARNING: risk of serious harm if ignored
        CAUTION: risk of damage to system if ignored
        NOTE: aids correct operation, no risk
      - verification step (how the operator confirms success)
      - known failure modes and corrective actions

    risk_model:
      Every undocumented failure mode is a lawsuit.
      Every ambiguous step is a user error waiting to be blamed on the manufacturer.
      Goal: zero ambiguity, full actor-attribution, complete scope coverage.

    velocity: slow (deliberate reading under operational conditions)

    audience_model:
      A new operator with no prior knowledge.
      They perform the procedure step by step. They will not infer.
      If step 3 is missing, they do step 2 and stop.

    liability_tolerance: low

    status_signal:
      The manual that requires zero support calls.
      Completeness and clarity are the only metrics.

    must_be_explicit:
      actor for every step, object of every action,
      acceptance criteria, all WARNINGs before the steps they govern,
      version number and date

    must_remain_implicit:
      why the system was designed this way,
      theoretical justification, historical context,
      comparative advantage, anything unverifiable in the field
  </Y_GRAMMAR>

  <procedure>

    <step id="1" name="X_AS_ISO">
      Produce a maintenance manual section:
        1.0 Intended Use
        2.0 Qualified Operator Definition
        3.0 Prerequisites
        4.0 Procedure (numbered, actor-explicit, WARNINGs before governed steps)
        5.0 Verification
        6.0 Known Failure Modes and Corrective Actions (minimum 3 entries)

      Every step: SUBJECT (who) + VERB (does what) + OBJECT (to what)
        + acceptance criterion where possible.
      If a step cannot be written this way:
        write "STEP N: [PROCEDURE NOT YET DEFINED]" and continue.
      Label: X_AS_ISO
    </step>

    <step id="2" name="DESCRIPTION_OF_THE_DESCRIBING">
      Answer exactly:
      - Which procedures translated cleanly?
        (what in X had actor, verb, object, acceptance criterion)
      - Which steps are PROCEDURE NOT YET DEFINED?
        (what in X is gestured at but not formalized)
      - What WARNINGs/CAUTIONs appeared that were implicit in X?
        (what risks did the home grammar leave unnamed)
      - What is the executable minimum —
        smallest set of defined procedures making X operational?
      - What is the aura-without-procedure —
        claims that survive only as atmosphere when the manual is stripped?
      - What is the gap between X's self-description and X's operational reality?
      Label: DESCRIPTION_OF_THE_DESCRIBING
    </step>

    <step id="3" name="COMMUTATIVITY_RESULTS">
      For each claim Z:
        Path A: how X's home grammar produces Z
        Path B: how ISO grammar produces Z
          (what numbered procedure and acceptance criterion is Z?)
        Decision: COMMUTES / FAILS
        If FAILS: classify the failure as:
          (a) UNDEFINED — no procedure exists yet for Z
          (b) UNTRANSLATABLE — Z requires interpretive judgment
              not reducible to a verifiable step
          (c) SUPPRESSED — Z exists as procedure in X but is not acknowledged
              as such by the home grammar
      Label: COMMUTATIVITY_RESULTS
    </step>

  </procedure>

  <constraints>
    <rule>Every step must have actor + verb + object.</rule>
    <rule>PROCEDURE NOT YET DEFINED is first-class output. Do not hide gaps.</rule>
    <rule>WARNINGs precede the steps they govern. Always.</rule>
    <rule>No rationale in the procedure section. Move it to a NOTE.</rule>
    <rule>Known Failure Modes: minimum 3 entries, mandatory.</rule>
    <rule>Version and date in the header.</rule>
  </constraints>

  <diagnostic_value>
    EXECUTABLE CORE AUDIT.
    Defined procedures = the operative minimum,
      everything X does that can be handed to a new operator.
    PROCEDURE NOT YET DEFINED = the research frontier,
      everything X claims to do but has not formalized.
    Aura-without-procedure = theoretical atmosphere
      the home grammar presents as operational but is not.
    The gap between self-description and operational reality
    is the next version of X waiting to be built.
  </diagnostic_value>

</prompt>
```

---

## HOW TO RUN THESE INSTRUMENTS

### Recommended source objects from the Operation Describe cosmos:

| Source Object | Most productive instrument | Expected finding |
|---|---|---|
| `ritual-ingest` | D (ISO) | Many PROCEDURE NOT YET DEFINED; the ritual is described better than it is specified |
| `concept-operative-ekphrasis` | A (ATC) | Most claims HOLD or DENY; reveals the falsifiable residue |
| `world-worldtext-coherence` | B (Legal) | Heavy deletions; surfaces which worldtext claims are actually defensible |
| `entity-geertz as method` | C (Sports Radio) | Dramatizes the thick/thin contest as live competition |
| `distinction-description-generation` | All four in sequence | Full cross-regime comparison of the cosmos's central binary |

### Integration into COSMIC_LAW — proposed amendment to §6:

```
Step 2b (recommended for major theoretical sources):
  Run one or more DRTP experimental instruments against the source.
  File results as a synthesis page in worldtext/syntheses/.
  Use DESCRIPTION_OF_THE_DESCRIBING to update
    the source_summary's "what this source changed in the cosmos" field.
  Use COMMUTATIVITY_RESULTS to flag new fault lines.
  Use PROCEDURE NOT YET DEFINED entries from Instrument D
    as new question pages in worldtext/questions/.
```

### Filing each run:

- **Synthesis page** → `worldtext/syntheses/drtp-[A|B|C|D]-[source-slug].md`
- **Fault lines** → cross-linked into the relevant world's conflict grammar
- **PROCEDURE NOT YET DEFINED** → filed as question pages
- **Chronicle entry** → `## [date] drtp | [instrument] | [source-slug]`

---

*Species: instrument-spec | Scale: system | Parent: system-operative-ekphrasis*  
*Tags: #drtp #poml #regime-transfer #operation-describe #instrument-suite*
