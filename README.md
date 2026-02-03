# Clinical Decision Support Simulation System (CDSS-MAS)

> [!IMPORTANT]
> **ETHICAL DISCLAIMER:** This system is a **simulation-only** educational tool designed for academic evaluation. It does **NOT** provide real medical advice, diagnoses, or prescriptions. All clinical data and agent outputs are hypothetical.

## Project Overview
CDSS-MAS is a high-fidelity **Multi-Agent System (MAS)** built with **CrewAI** to simulate a multidisciplinary clinical team collaborating on complex patient cases. It demonstrates how autonomous agents can resolve conflicts, model beliefs, and produce emergent care pathways.

## Why this is a Multi-Agent System (MAS)
Unlike monolithic AI systems, CDSS-MAS is composed of multiple **autonomous**, **reactive**, and **proactive** entities that interact in a shared environment.

### Mapping to MAS Theory
| MAS Concept | CDSS-MAS Realization |
| :--- | :--- |
| **Autonomy** | Each agent (Diagnostic, Treatment, Safety) operates with its own goal and backstory, independent of others. |
| **Reactivity** | The Safety Agent reacts to proposed plans, and the Monitoring Agent reacts to physiological simulations. |
| **Proactivity** | The Treatment Planning Agent initiates path creation based on diagnostic hypotheses. |
| **Social Ability** | Agents communicate via structured tasks and shared memory within the CrewAI environment. |
| **Decentralized Decision-Making** | Reasoning is distributed across specialists; no single agent has the full solution initially. |
| **Emergent Behavior** | The final care pathway is an emergent property of the negotiation between treatment efficacy and safety constraints. |
| **Belief Modeling** | The Manager Agent (Coordinator) reasons about the confidence levels and potential biases of specialized agents. |

## CrewAI Architecture
The system utilizes a **Hierarchical Process**:
- **Manager Agent**: `Clinical Care Pathway Coordinator`
- **Specialists**: Diagnostic, Treatment, Safety, Monitoring, and Ethics agents.
- **Shared Memory**: Enabled to allow agents to "remember" previous interactions and context.

## How to Run

### 1. Environment Setup
```bash
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY
pip install -r requirements.txt
```

### 2. Terminal Demonstration
```bash
python src/main.py
```
This will run the full simulation and print agent reasoning directly to the console.

### 3. Streamlit UI Demonstration
```bash
streamlit run ui/app.py
```
This opens a dashboard to visualize agent collaboration, patient data, and the final decision pathway.

## Documentation
- [ARCHITECTURE.md](ARCHITECTURE.md): Detailed system design and Mermaid diagrams.
- [CONTRIBUTING.md](CONTRIBUTING.md): Guidelines for developers.
