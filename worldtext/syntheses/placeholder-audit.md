# Placeholder & Duplicate Audit

> **Species**: synthesis  
> **Scale**: cosmos  
> **Filed**: 2026-04-13  

---

## Findings

### Corpus Composition

| Category | Count | % |
|----------|-------|---|
| **Total entries** | 708 | 100% |
| Entries with real authors | 245 | 34.6% |
| Entries without real authors | 463 | 65.4% |
| Entries with no author field | 6 | 0.8% |
| **Exact title duplicates** | 25 | 3.5% |

### Duplicate Entries Identified (25)

| Index | Duplicate Of | Title |
|-------|-------------|-------|
| 9 | 0 | Museum of Words (Heffernan) |
| 143 | 69 | Empty title "2026," |
| 144 | 78 | Operative ekphrasis (Bajohr) |
| 163 | 83 | Memory of the multitude |
| 198 | 173 | collapse of text/image distinction |
| 324 | 203 | Engineering Models / Wittgenstein |
| 400 | 142 | Thick Evaluations of Cultural Representation |
| 427 | 364 | Virtually Shamans |
| 434 | 69 | Empty title "2026," |
| 453 | 450 | Semiotics-based prompt engineering |
| 488 | 203 | Engineering Models / Wittgenstein |
| 507 | 492 | Singer of Tales in LLM Era |
| 527 | 69 | Empty title "2026," |
| 564 | 69 | Empty title "2026," |
| 573 | 558 | CAMEL Communicative Agents |
| 578 | 420 | LatentPrompt |
| 598 | 131 | Daily Papers / Hugging Face |
| 613 | 173 | collapse of text/image distinction |
| 626 | 438 | AI Generative Art as Algorithmic Remediation |
| 649 | 217 | Hallucinations in LLMs |
| 665 | 495 | Dreamsheets |
| 684 | 319 | Ethnography and AI |
| 698 | 697 | MetaTool |
| 700 | 699 | Artworks Reimagined |
| 707 | 706 | Adversarial Versification |

### Effective Corpus After Deduplication

| Category | Count |
|----------|-------|
| Unique entries | 683 |
| Unique with real authors | ~232 |
| Unique with abstracts > 100 chars | ~150 |
| Formally-typed (book/article/conference/chapter) | 85 |

### Classification of 463 Authorless Entries

These are primarily **Zotero web-page auto-captures** (type: "document"). The "author" field contains auto-extracted keywords from the page title rather than actual author names. Many are:
- Blog posts and news articles about AI
- Documentation pages (Hugging Face, arXiv, GitHub)
- YouTube video descriptions
- Wikipedia/encyclopedia entries
- Marketing content about AI tools

**Verdict**: These entries are **legitimate research bookmarks** but not **scholarly sources**. They represent the researcher's browsing trail — evidence of research interest, not primary evidence. They should be reclassified as `evidence_grade: bookmark` rather than treated as full sources.

### Recommendation

1. **Do not delete** the 463 bookmark entries — they are evidence of research interest patterns
2. **Flag** them as `grade: bookmark` in source processing
3. **Remove** the 25 exact duplicates (mark as superseded)
4. **Process individually** only the ~232 unique entries with real authors
5. **Revise** the cosmos's source count claims from "708" to "683 unique entries (232 attributed, 451 bookmarks)"

---

*This audit was triggered by the Dark Matter Guardian Grader finding. Filed into the WorldText stratum.*
