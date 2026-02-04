# Medical Decision Intelligence via MAS
##  Project Overview

**Medical Decision Intelligence via MAS** is a clinical decision support simulation driven by a **Multi-Agent System (MAS)** architecture. Instead of relying on a single AI model, this system orchestrates a team of specialized autonomous agents—representing a Diagnostician, Treatment Planner, Safety Auditor, and Ethics Reviewer—to collaborate on complex patient cases.

By simulating the distributed reasoning of a human medical board, the system achieves:
*   **Reduced Bias**: Through diverse agent perspectives and role-playing.
*   **Enhanced Safety**: Dedicated agents expressly verify drug interactions and contraindications.
*   **Comprehensive Care**: Integrated ethical reviews and long-term monitoring simulations.

##  Features

- **Multi-Agent Collaboration**: Autonomous agents representing Diagnostic, Treatment, Safety, and Ethics specialists.
- **Dynamic Patient Input**: Interactive interfaces for entering patient data via Terminal or Web UI.
- **Concise Reporting**: Generates executive-level clinical summaries with strict brevity.
- **Conflict Resolution**: Advanced coordination logic to resolve disagreements between specialists.
- **API Reliability**: Robust error handling with automatic API key rotation.
- **Secure Design**: Privacy-first architecture suitable for simulated medical data.

## 🛠️ Installation

### Prerequisites
- Python 3.10 or higher
- Git

### Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/aprilyab/Medical-Decision-Intelligence-via-MAS.git
   cd Medical-Decision-Intelligence-via-MAS
   ```

2. **Create a Virtual Environment**
   ```bash
   python3 -m venv mvenv
   source mvenv/bin/activate  
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configuration**
   Copy the example environment file and configure your API keys:
   ```bash
   cp .env.example .env
   ```
   Edit `.env` to add your Google Gemini API keys.

##  Usage

### Terminal Mode (CLI)
Run the simulation directly in your terminal for a text-based experience:
```bash
python src/main.py
```
Follow the prompts to enter patient details or press Enter to use a sample case.

### Web Interface (Streamlit)
Launch the interactive dashboard for a visual experience:
```bash
streamlit run ui/app.py
```
Access the app at `http://localhost:8501`. Use the sidebar to input patient data via smart dropdowns.

##  Project Structure

```
├── data/               # Sample patient cases
├── src/                # Source code
│   ├── agents.py       # Agent definitions and logic
│   ├── crew.py         # Crew orchestration
│   ├── tasks.py        # Task definitions
│   ├── tools.py        # Custom tools
│   ├── main.py         # CLI entry point
│   └── config.py       # Configuration settings
├── ui/                 # User Interface logic
│   └── app.py          # Streamlit application
├── tests/              # Automated tests
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```

