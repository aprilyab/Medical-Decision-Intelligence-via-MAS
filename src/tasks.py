from crewai import Task
from .schemas import DiagnosticHypothesis, TreatmentOption, MedicationSafetyReport, EthicsRiskEvaluation, CarePathway

class MedicalTasks:
    def diagnostic_task(self, agent, patient_case) -> Task:
        # MAS Concept: Distributed Problem Solving
        return Task(
            description=f"Analyze the patient case: {patient_case}. "
                        "Identify the most likely diagnoses and provide confidence scores for each.",
            expected_output="A list of at least 3 clinical hypotheses with reasoning and confidence scores.",
            agent=agent,
            output_json=DiagnosticHypothesis
        )

    def treatment_planning_task(self, agent, patient_case) -> Task:
        # MAS Concept: Proactivity & Goal-Directed Behavior
        return Task(
            description=f"Based on the patient case: {patient_case}, propose a non-biased, "
                        "guideline-based treatment plan. Consider the patient's existing medications.",
            expected_output="A set of treatment options including rationale and potential risks.",
            agent=agent,
            output_json=TreatmentOption
        )

    def safety_audit_task(self, agent) -> Task:
        # MAS Concept: Reactivity & Constraint Satisfaction
        return Task(
            description="Review the proposed treatment plan for any drug-drug interactions, "
                        "contraindications, or safety concerns given the patient's history.",
            expected_output="A safety report detailing risks, contraindications, and suggested alternatives.",
            agent=agent,
            output_json=MedicationSafetyReport
        )

    def monitoring_simulation_task(self, agent) -> Task:
        # MAS Concept: Dynamic Feedback Loop
        return Task(
            description="Simulate the patient's physiological response to the proposed treatment over a 30-day period.",
            expected_output="A simulation report predicting patient stability and potential adverse reactions.",
            agent=agent
        )

    def ethical_review_task(self, agent) -> Task:
        # MAS Concept: Social Ability & Value Alignment
        return Task(
            description="Evaluate the proposed care pathway for ethical implications, including patient burden and fairness.",
            expected_output="An ethical evaluation report with a final recommendation on path viability.",
            agent=agent,
            output_json=EthicsRiskEvaluation
        )

    def coordination_task(self, agent) -> Task:
        # MAS Concept: Conflict Resolution & Emergent Consensus
        return Task(
            description="Integrate all specialist findings (diagnostic, treatment, safety, ethics, and monitoring) "
                        "into a single, unified Care Pathway. Resolve any conflicting recommendations.",
            expected_output="A final, integrated Clinical Care Pathway report.",
            agent=agent,
            output_json=CarePathway
        )
