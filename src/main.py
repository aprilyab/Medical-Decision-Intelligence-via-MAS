import json
from .crew import MedicalCrew
from .config import MEDICAL_DISCLAIMER, APP_NAME

def main():
    print("="*60)
    print(f" {APP_NAME} ")
    print("="*60)
    print(f"DISCLAIMER: {MEDICAL_DISCLAIMER}")
    print("-"*60)

    # Load sample patient case
    try:
        with open("data/sample_case.json", "r") as f:
            patient_case = json.load(f)
    except FileNotFoundError:
        print("Error: data/sample_case.json not found. Please ensure the project structure is intact.")
        return

    print(f"Loading Patient Case: {patient_case['case_id']}")
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
