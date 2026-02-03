import os
from dotenv import load_dotenv

load_dotenv()

# System constants
APP_NAME = "Clinical Decision Support Simulation System (CDSS-MAS)"
UI_THEME = "dark"

# Simulation settings
DEFAULT_CONFIDENCE_THRESHOLD = 0.7
MAX_ITERATIONS = 5

# Safety Disclaimer
MEDICAL_DISCLAIMER = (
    "simulation-only; "
    "NOT real medical advice; "
    "for educational/evaluation purposes only"
)
