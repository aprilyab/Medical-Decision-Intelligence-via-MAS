from pydantic import BaseModel, Field
from typing import List, Optional, Dict

class Symptom(BaseModel):
    name: str
    severity: str # e.g., "mild", "moderate", "severe"
    duration: str

class PatientCase(BaseModel):
    case_id: str
    age: int
    gender: str
    primary_complaint: str
    symptoms: List[Symptom]
    medical_history: List[str]
    current_medications: List[str]
    vitals: Dict[str, str]

class DiagnosticHypothesis(BaseModel):
    condition: str
    confidence_score: float = Field(..., ge=0, le=1)
    reasoning: str

class TreatmentOption(BaseModel):
    name: str
    dosage: Optional[str] = None
    rationale: str
    risks: List[str]

class MedicationSafetyReport(BaseModel):
    is_safe: bool
    contraindications: List[str]
    suggested_alternatives: List[str]
    safety_score: float

class EthicsRiskEvaluation(BaseModel):
    ethical_concerns: List[str]
    burden_on_patient: str
    fairness_assessment: str
    recommendation: str

class CarePathway(BaseModel):
    case_id: str
    final_diagnosis: str
    treatment_plan: List[TreatmentOption]
    safety_notes: List[str]
    ethical_summary: str
    coordinator_notes: str
