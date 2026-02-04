import sys
import os
import json
import uuid

# Add the parent directory to sys.path to allow absolute imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.crew import MedicalCrew
from src.config import MEDICAL_DISCLAIMER, APP_NAME

def get_patient_details():
    """Prompts the user for patient details dynamically."""
    print("\n--- Enter Patient Details (Press Enter to skip and use sample case) ---")
    
    primary_complaint = input("Primary Complaint: ").strip()
    if not primary_complaint:
        return None  # Signal to use sample case

    age = input("Age: ").strip()
    gender = input("Gender: ").strip()
    history_input = input("Medical History (comma separated): ").strip()
    history = [h.strip() for h in history_input.split(",")] if history_input else []
    
    meds_input = input("Current Medications (comma separated): ").strip()
    meds = [m.strip() for m in meds_input.split(",")] if meds_input else []

    vitals = {}
    print("--- Enter Vitals (Optional) ---")
    vals = ["BP", "HR", "SpO2", "Temp"]
    for v in vals:
        val = input(f"{v}: ").strip()
        if val:
            vitals[v] = val

    return {
        "case_id": f"CASE-{uuid.uuid4().hex[:8].upper()}",
        "age": int(age) if age.isdigit() else 45, # Default if invalid
        "gender": gender or "Unknown",
        "primary_complaint": primary_complaint,
        "medical_history": history,
        "current_medications": meds,
        "symptoms": [{"name": primary_complaint, "severity": "Unknown", "duration": "Unknown"}], # Simplified for CLI
        "vitals": vitals
    }

def main():
    print("="*60)
    print(f" {APP_NAME} ")
    print("="*60)
    print("-"*60)

    # Dynamic Input
    patient_case = get_patient_details()

    if not patient_case:
        print("\nUsing Default Sample Case...")
        # Load sample patient case
        try:
            case_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "sample_case.json")
            with open(case_path, "r") as f:
                patient_case = json.load(f)
        except FileNotFoundError:
            print("Error: data/sample_case.json not found. Please ensure the project structure is intact.")
            return

    print(f"\nLoading Patient Case: {patient_case['case_id']}")
    print(f"Primary Complaint: {patient_case['primary_complaint']}")
    print("-"*60)
    print("Initializing Multi-Agent Clinical Team Simulation...")
    
    # Initialize and run the crew
    crew_instance = MedicalCrew(patient_case)
    result = crew_instance.run()

    print("\n" + "="*60)
    print(" FINAL EMERGENT CARE PATHWAY ")
    print("="*60)
    print(result)
    print("="*60)
    print("Simulation Complete.")

if __name__ == "__main__":
    main()
