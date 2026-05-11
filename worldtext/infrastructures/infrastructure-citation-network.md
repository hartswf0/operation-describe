# Infrastructure: citation network

> **Species**: infrastructure  
> **Scale**: system  
> **Primary Worlds**: [[world-memex-trail]], [[world-thick-description]]  
> **Last Revision**: 2026-04-28  

---

## Definition

The citation network is the infrastructure of provenance: the system of links that traces every claim in the worldtext back to its source. It is the worldtext's implementation of Bush's trail — the mechanism that lets a reader move from a claim in a synthesis to the entity that made it, to the source paper that contains the original argument.

## Current State

The citation network is partially built. The 178 source pages in `sources/` provide bibliographic records. The 25 entity pages link to primary worlds. The syntheses contain inline references. But the network is incomplete:
- Many syntheses cite concepts without linking to the paper that originated them
- Entity pages reference worlds but not specific syntheses
- The 42 broken links represent gaps in the citation network

## What a Complete Citation Network Would Look Like

Every claim → entity → source → paper → page number.  
Every synthesis → the specific sources that substantiate each section.  
Every entity → the specific passages in the papers where they contribute.  
Every program → the specific papers it draws its operations from.

## Cross-Links

- [[world-memex-trail]] — the citation network IS the memex trail at institutional scale
- [[citation-network]] — the synthesis that describes this infrastructure
