# The Clean Stack and Artifact Lifecycle

> Canon / Belief / Index — three instruments, not synonyms.

---

## Core Thesis

Every fictional universe requires three fundamentally different instruments. They are not layers of the same thing. They are **ontologically distinct** and must never be collapsed.

---

## The Clean Stack

### 1. WORLD BIBLE (Canon)

**Function**: Governs the world.

The World Bible is the **source of truth** for how the world works. It defines laws, constraints, history, institutions, aesthetics, conflicts, and what is impossible.

| Property | Value |
|----------|-------|
| **Audience** | Writers, designers, directors, collaborators, machines |
| **Tone** | Authoritative, structural, constraint-heavy |
| **Truth status** | Canonical — incontrovertible within the world |
| **Mutability** | Extremely slow — changes require formal canonization |

**Contains**:
- Cosmology: What kind of world is this?
- Laws: What can and cannot happen?
- History: What events shaped the present?
- Institutions: Who holds power?
- Geography: Where does life happen?
- Technology: What tools, systems, machines exist?
- Culture: What do people believe, fear, worship, mock, desire?
- Conflicts: What tensions drive stories?
- Visual language: What does the world look, sound, and feel like?
- Continuity rules: What must remain consistent?

**Best for**: Keeping the whole fictional universe coherent.

---

### 2. LORE BOOK (Belief)

**Function**: Immerses the reader in the world.

The Lore Book is less like a rulebook and more like an **artifact from inside the world**. It can contain myths, legends, propaganda, field notes, sacred fragments, rumors, corrupted records, maps, bestiaries, songs, institutional documents, survivor testimonies.

| Property | Value |
|----------|-------|
| **Audience** | Readers, players, fans, viewers |
| **Tone** | Poetic, archival, fragmentary, atmospheric |
| **Truth status** | Mixed — canonical, disputed, legendary, false_but_believed, obsolete |
| **Mutability** | High — contradictions are features, not bugs |

**Contains**:
- Myths: Origin stories, legends, sacred lies
- Rumors: Contradictory accounts and folk knowledge
- Artifacts: Letters, manuals, diagrams, songs, decrees
- Creatures: Beasts, spirits, machines, anomalies
- Places: Haunted locations, cities, ruins, forbidden zones
- Figures: Saints, villains, heroes, failed gods
- Rituals: Practices, taboos, ceremonies, technologies of belief
- Lost history: What people half-remember or misremember

**Best for**: Giving the world mystery, texture, and emotional gravity.

---

### 3. ENCYCLOPEDIA (Index)

**Function**: Indexes the world.

The Encyclopedia is the **reference layer**. It is modular, searchable, alphabetical or taxonomic. It defines entities cleanly.

| Property | Value |
|----------|-------|
| **Audience** | Writers, readers, designers, researchers |
| **Tone** | Clear, concise, factual |
| **Truth status** | Factual within the world's frame — reports what is known |
| **Mutability** | Medium — updated as canon evolves |

**Contains**:
- Named entries for all indexed entities
- Cross-references between entries
- Disambiguation notes
- Version history
- Status tags (canonical, disputed, legendary, etc.)

**Best for**: Fast retrieval during active world-building.

---

## The Truth-Status Taxonomy

Every piece of world-content carries a truth status:

| Status | Definition | Lives In |
|--------|-----------|----------|
| `canonical` | Incontrovertible fact within the world | World Bible |
| `disputed` | Multiple incompatible accounts exist | Lore Book |
| `legendary` | Widely believed but unverifiable | Lore Book |
| `false_but_believed` | Known to be wrong by the architects, believed by the inhabitants | Lore Book |
| `obsolete` | Once canonical, now superseded | Lore Book archive |

---

## The Artifact Lifecycle

Every generated output enters the system as raw material and must be processed through a formal lifecycle:

```
                    ┌─────────────┐
                    │ RAW FRAGMENT │ ← Uninterpreted exposure
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │  CANDIDATE  │ ← Recognized as potentially belonging
                    │  ARTIFACT   │    to the world
                    └──────┬──────┘
                           │
              ┌────────────┼────────────┐
              │            │            │
       ┌──────▼──────┐ ┌──▼───┐ ┌──────▼──────┐
       │  REJECTED   │ │ LORE │ │ RECOGNIZED  │
       │  ARTIFACT   │ │      │ │  ARTIFACT   │
       └──────┬──────┘ └──┬───┘ └──────┬──────┘
              │            │            │
              ▼            ▼            ▼
         counter-     mythic        candidate
         example     archive       for canon
              │            │            │
              │            │     ┌──────▼──────┐
              │            │     │ CANONIZED   │
              │            │     │  ARTIFACT   │
              │            │     └─────────────┘
              │            │
              ▼            ▼
        teaches         enriches
        negative       the world's
        constraints    felt depth
```

### The Deep Loop

The operator's fundamental work cycle:

```
feed_in → generate → recognize → reject_or_canonize → index → continue
```

This loop never terminates. A world is not built and finished. A world is **maintained** — continuously fed, tested, repaired, and extended.

---

## The Conflict: Canon vs. Lore

The World Bible demands absolute truth. The Lore Book demands productive contradiction.

This tension is not a problem to solve. It is the **engine** of good world-building:

- Too much canon → the world becomes rigid, predictable, and dead.
- Too much lore → the world becomes incoherent, arbitrary, and unnavigable.
- The operator's job is to maintain the **ratio** — enough riverbed to navigate by, enough water to sustain life.

### The Lore Contradiction Limit

How much productive contradiction can a lore book sustain before crossing into accidental coherence failure?

There is no universal answer. But there are diagnostic signs:

| Healthy Contradiction | Pathological Contradiction |
|----------------------|---------------------------|
| Two cultures tell different origin stories | The world has two incompatible physics systems |
| A hero is remembered differently by allies and enemies | A character's age changes between scenes |
| A sacred text has multiple interpretations | The map contradicts itself |
| History is disputed by different factions | The author forgot what they established |

---

## The Executable World Bible

The most radical implication of the Clean Stack: the World Bible should be **machine-readable**.

Not a narrative document. Not a wiki page. A structured constraint prompt:

```yaml
world:
  name: "The Reach"
  physics:
    gravity: "standard terrestrial"
    magic: "none"
    technology_level: "pre-industrial + one anomaly (the Lens)"
  entities:
    - name: "The Lens"
      type: "artifact"
      identity_fields:
        origin: "unknown"
        location: "The Citadel, top floor"
        properties: ["magnifies intent", "cannot be moved by force"]
      state_fields:
        current_holder: "Warden Oss"
        condition: "cracked along the western axis"
  continuity_anchors:
    - "The Lens has always been in the Citadel"
    - "No one alive knows who made it"
  negative_constraints:
    - "The Lens cannot be destroyed"
    - "The Lens does not grant wishes"
    - "Magic does not exist — the Lens is the only anomaly"
```

This YAML is not documentation. It is the **upstream control surface**. Every prompt passes through it. Every generation is tested against it. Every violation is flagged.

---

## Sources

- NATURAL SIGN Doc A: "Worldtext Coherence Theory and Design"
- NATURAL SIGN Doc C: Raw conversation `a.md` — World Bible / Lore Book / Encyclopedia distinction
- NATURAL SIGN Doc B: "Worldtext and Same-Worldness"
- Mark J.P. Wolf, *Building Imaginary Worlds* (2012)

---

*Synthesis compiled: 2026-04-27. Parent world: world-worldtext-coherence. Cross-references: world-subcreation, world-continuity-debt.*
