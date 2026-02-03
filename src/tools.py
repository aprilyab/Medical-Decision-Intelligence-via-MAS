import random
from langchain.tools import tool
from typing import List, Dict

class MedicalSimulationTools:
    
    @tool("simulate_diagnostic_search")
    def simulate_diagnostic_search(symptoms: List[str]) -> str:
        """Simulates a search in a medical knowledge base for a set of symptoms."""
        # MAS Concept: Decentralized Knowledge
        # Agents use this to gather partial information independently.
        knowledge_base = {
            "dyspnea": ["Congestive Heart Failure", "COPD Exacerbation", "Pneumonia"],
            "edema": ["Heart Failure", "Renal Failure", "Venous Insufficiency"],
            "orthopnea": ["Congestive Heart Failure", "Sleep Apnea"]
        }
        
        results = []
        for symptom in symptoms:
            matches = knowledge_base.get(symptom.lower(), ["Inconclusive condition"])
            results.extend(matches)
        
        unique_results = list(set(results))
        return f"Potential matches found in knowledge base: {', '.join(unique_results)}"

    @tool("check_medication_interactions")
    def check_medication_interactions(new_meds: List[str], current_meds: List[str]) -> str:
        """Simulates a safety check for drug-drug interactions."""
        # MAS Concept: Reactivity & Constraints
        # Safety agent reacts to proposed plans and applies normative constraints.
        conflicts = []
        # Simulate a conflict between Metformin and a hypothetical new drug
        if "Metformin" in current_meds and "Contrast Dye" in new_meds:
            conflicts.append("CRITICAL: Risk of lactic acidosis when Metformin is used with contrast agents.")
        
        if "Lisinopril" in current_meds and "Spironolactone" in new_meds:
            conflicts.append("WARNING: High risk of hyperkalemia.")
            
        if not conflicts:
            return "No interactions detected. Proposed medication plan appears safe."
        return "\n".join(conflicts)

    @tool("calculate_risk_score")
    def calculate_risk_score(patient_age: int, comorbidities: List[str]) -> float:
        """Simulates a clinical risk scoring algorithm (e.g., Charlson Comorbidity Index)."""
        # MAS Concept: Distributed Problem Solving
        # Multiple agents can use this tool to quantify their reasoning.
        base_score = patient_age / 20.0
        comorbidity_weights = {
            "Diabetes": 1.5,
            "COPD": 2.0,
            "Hypertension": 1.0,
            "Heart Failure": 3.0
        }
        
        for condition in comorbidities:
            base_score += comorbidity_weights.get(condition, 0.5)
            
        return round(base_score, 2)
