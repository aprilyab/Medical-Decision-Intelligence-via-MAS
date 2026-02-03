# Architecture: Clinical Decision Support Simulation System (CDSS-MAS)

## System Overview
The CDSS-MAS is a hierarchical Multi-Agent System designed to simulate complex clinical decision-making. It leverages CrewAI for agent orchestration and Streamlit for visualization.

## Architecture Diagram (Mermaid)
```mermaid
graph TD
    subgraph "Agents"
        C[Care Pathway Coordinator - Manager]
        D[Diagnostic Reasoning Agent]
        T[Treatment Planning Agent]
        S[Medication Safety Agent]
        M[Patient Monitoring Agent]
        E[Ethics & Risk Officer]
    end

    subgraph "Tools & Data"
        TB[Medical Knowledge Base Tool]
        TS[Safety Interaction Tool]
        TR[Risk Scoring Tool]
        PC[Sample Patient Case - JSON]
    end

    PC --> C
    C --> D
    C --> T
    C --> S
    C --> M
    C --> E

    D --> TB
    D --> TR
    S --> TS
    T --> TR
    M --> TR

    D -.-> |Conflicting Recommendation| T
    D -.-> |Conflicting Recommendation| S
    T -.-> |New Medication| S
    S -.-> |Safety Warning| C
    C -.-> |Resolved Plan| Result[Emergent Care Pathway]
```

## Agent Interaction Flow
1. **Coordination Initiated**: The Manager Agent (Coordinator) receives the patient case.
2. **Distributed Analysis**:
   - **Diagnostic Reasoning Agent** evaluates symptoms to produce hypotheses.
   - **Treatment Planning Agent** proposes guideline-based options.
3. **Reactive Safety Audit**: 
   - **Medication Safety Agent** reacts to proposed treatments using safety tools.
4. **Dynamic Feedback**:
   - **Patient Monitoring Agent** simulates temporal responses.
5. **Normative Evaluation**:
   - **Ethics Agent** applies ethical constraints and burden assessment.
6. **Consensus & Emergence**:
   - The **Coordinator** resolves conflicts (e.g., safety vs. efficacy) and synthesizes the final Pathway.

## Task Dependencies
- `diagnostic_task` (None)
- `treatment_planning_task` (None)
- `safety_audit_task` (treatment_planning_task)
- `monitoring_simulation_task` (treatment_planning_task, diagnostic_task)
- `ethical_review_task` (coordination_task)
- `coordination_task` (All specialists)
