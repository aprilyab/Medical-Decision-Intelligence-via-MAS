import pytest
import json
import os
from src.crew import MedicalCrew
from src.agents import MedicalAgents
from src.tasks import MedicalTasks

def test_project_structure():
    """Verify essential project files exist."""
    assert os.path.exists("data/sample_case.json")
    assert os.path.exists("src/main.py")
    assert os.path.exists("ui/app.py")

def test_crew_initialization():
    """Verify that the MedicalCrew can be initialized with sample data."""
    with open("data/sample_case.json", "r") as f:
        patient_data = json.load(f)
    
    crew_instance = MedicalCrew(patient_data)
    crew = crew_instance.setup_crew()
    
    assert len(crew.agents) == 6
    assert len(crew.tasks) == 6
    assert crew.process.value == "hierarchical"

def test_agent_specialization():
    """Verify that agents have correct roles and tools."""
    agents = MedicalAgents()
    diag_agent = agents.diagnostic_reasoning_agent()
    
    assert "Diagnostic" in diag_agent.role
    assert len(diag_agent.tools) > 0
