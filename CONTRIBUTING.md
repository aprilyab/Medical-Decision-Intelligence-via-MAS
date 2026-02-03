# Contributing to CDSS-MAS

We welcome contributions that enhance the academic quality and MAS demonstration capabilities of this project.

## Development Guidelines
- **Atomicity**: Ensure every commit is atomic and descriptive.
- **MAS Focus**: When adding features, explicitly state which MAS concept (autonomy, proactivity, etc.) is being reinforced.
- **Ethics First**: Never implement features that imply real-world medical reliability. This is a simulation ONLY.

## Git Commit Format
- `feat:` for new agents/tools
- `docs:` for documentation updates
- `test:` for verification scripts
- `refactor:` for code improvements without logic changes

## Setup
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Create a `.env` file from `.env.example`.
4. Run tests before submitting: `pytest tests/`.
