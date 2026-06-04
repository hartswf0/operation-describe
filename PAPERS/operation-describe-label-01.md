# Due-Diligence Answers: Operative Description

This document provides the formal answers to the due-diligence boundary and defense questions compiled in [operation-describe-label-00.md](file:///Users/gaia/OPERATION-DESCRIBE/PAPERS/operation-describe-label-00.md).

---

### **0. The Non-Operative Boundary**
> Language is non-operative when it has no systemic consequences. A text string on an unread backup tape has an action delta of zero ($\Delta P = 0$). It is merely decorative. The moment that string branches execution, it becomes infrastructure. We do not study the passive storage of symbols; we study symbols acting as routing valves.

### **1. Boundaries: Symbolic Valves**
> Descriptions are symbolic frames. A door is a physical barrier; the label `restricted` is a description. It is operative because it alters the probability of entry. If a sign does not shift the probability of subsequent action, it is not a description—it is noise.

### **2. The Defense: Not Total Novelty, But Recombination**
> We do not claim language is a new phenomenon. We claim that *short descriptive forms* (labels, prompts, schemas) have been upgraded to *routing infrastructure*. Speech-act theory tells us language performs; workflow automation builds the pipes. Operative description is the valve: it is the symbolic coordinate that routes action across human-machine systems.

### **3. Causality: Holding the Input Constant**
> Causality is proven by holding the input constant and varying only the description. If the exact same user prompt and function signature produce different tool calls when we vary the JSON schema's `description` field, the description is the causal driver. The counterfactual is the unlabeled or baseline state.

### **4. Evidence: Logged State Transitions**
> Routing is not a vibe; it is a logged event. We track timestamped label applications, API parameters, warning prompts, and tool-invocation traces. The data is empirical, public (GitHub), or experimentally generated (LLM API logs). Where platform moderation logs are proprietary, we run simulated pipelines using public toxicity APIs.

### **5. Unit of Analysis: The Description/Action Pair**
> We do not analyze words in isolation. The unit of analysis is the **description/action pair** $\langle D, A_{\text{route}} \rangle$: a specific descriptive token and the route it makes more likely, legitimate, or automatic.

### **6. The Operator: Substrate-Agnostic Processors**
> An operator is simply: *the thing that reads the description and acts on it.* It can be a tired nurse, an LLM agent, or a cron job. Conscious human understanding is irrelevant; routing requires only that the description be processed in a way that shifts the action-space.

### **7. Authority: Asymmetric Platform Power**
> Descriptions only route when backed by systemic authority. Maintainers label issues; platform policies enforce toxicity queues; developers define schemas. The political question is: **who controls the categories that route action, and who is routed by them?**

### **8. Error: Infrastructure Made Visible**
> Error is where the system becomes visible. A `good first issue` that is too hard, a satirical comment flagged as `toxic`, or an LLM calling a refund tool prematurely are not just mistakes; they are diagnostic events that expose the routing rules.

### **9. Compression: The Low-Dimensional Interface**
> Operative descriptions are compression interfaces. They collapse high-dimensional, complex realities (e.g., tone, context, history) into low-dimensional, actionable symbols (`bug`, `toxic`, `ESI Level 2`).

### **10. Feedback: The Cybernetic Loop**
> Feedback prevents "cybernetics" from becoming a loose metaphor. It is the downstream event (appeals, PR merges, API errors) that returns to modify the description, adjust the threshold, or mutate the next prompt context.

### **11. The Cases: Labor, Speech, and Execution**
> The case studies form a coherent register of contemporary systems:
> *   *GitHub labels* route human labor.
> *   *Toxicity thresholds* route platform speech.
> *   *LLM schemas* route machine execution.

### **12. Scope: The Leanest Core**
> This is a single dissertation focused on a shared mechanism. The primary case is the LLM tool description (cleanest experimental control); the secondary case is GitHub labels (public scale). Toxicity is the political governance case; emergency triage is kept only as an introductory analogy.

### **13. Method: Mixed-Methods Routing Analysis**
> We combine public data scraping (GitHub), API simulations on public datasets (toxicity moderation), and controlled experimental sweeps (LLM prompts). Each method measures the action-space delta ($\Delta P$) produced by varying the description.

### **14. Ethics: Sandboxed Agency**
> Human data is anonymized. Toxicity datasets are simulated. LLM tool calls are sandboxed to mock functions, ensuring no real-world actions (e.g., refunds or emails) are executed.

### **15. Power: Asymmetric Discipline**
> Operative descriptions reduce complexity for platform controllers while restricting agency for categorized subjects. The efficiency of the system is paid for in the compliance and routing of its users.

### **16. Design: The Qualities of Good Routing**
> Effective routing requires clear category boundaries, transparent authority, visible confidence levels, and easy contestability or reversibility. Speed is not the only value; a fast route can be a bad route.

### **17. Disproof: Falsification Metrics**
> The theory is falsified if experimentally varying LLM tool description text fails to change tool call rates under identical prompts, or if adding GitHub issue labels has no statistical effect on issue resolution times.

### **18. Home Field: Media Theory**
> The home field is digital media theory, supported by philosophy of language and platform/AI studies.

### **19. Why Now: Natural Language as Compiler**
> In modern software and LLM architectures, natural language is no longer just a medium for human communication; it is directly compiled into executable machine action.

### **20. The Defense: The Three-Sentence Defense**
> We do not study labels as names, but as routing valves. We do not study speech acts as isolated utterances, but as classifications coupled to platform workflows. We study the description/action pair through routing analysis.

---

## The Final Checklist

### 1. What is operative description?
An operative description is a symbolic classification coupled to an infrastructure that routes subsequent action.

### 2. What is not operative description?
An unread description stored in an inactive archive is not operative because its action-space delta is zero.

### 3. What is your primary case?
The primary case study is LLM tool descriptions.

### 4. What is your unit of analysis?
The unit of analysis is the description/action pair.

### 5. What route does each case show?
GitHub routes software labor, moderation routes platform speech, and LLM schemas route machine execution.

### 6. What evidence proves routing?
System database timestamps, moderator queue logs, and API call JSON records prove routing.

### 7. What is your counterfactual?
The counterfactual is the behavior of identical inputs without the label or with altered schema descriptions.

### 8. What data can you actually access?
We access open GitHub repository logs, public toxicity datasets, and developer API transaction logs.

### 9. What would disprove or weaken your claim?
If varying LLM schema descriptions fails to alter model invocation rates, the claim is weakened.

### 10. Why is this not just speech-act theory?
Speech-act theory focuses on isolated performative utterances, whereas we focus on classifications embedded in multi-step platform workflows.

### 11. Why is this not just classification?
Classification merely sorts objects into categories, whereas operative description unifies the sort with the instructions that route the operator.

### 12. Who controls the descriptions?
Platform architects, software developers, and institutional administrators control the descriptions.

### 13. Who can contest them?
Operators can contest descriptions through system feedback loops such as appeals, relabeling, and retry protocols.

### 14. Who pays when they are wrong?
The categorized subjects (silenced users, denied customers, under-triaged patients) pay when they are wrong.

### 15. Why does this matter now?
It matters now because natural language is no longer passive representation; it is directly executed as system code.
