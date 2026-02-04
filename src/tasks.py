from crewai import Task
from src.schemas import DiagnosticReport, TreatmentReport, MedicationSafetyReport, EthicsRiskEvaluation, CarePathway

class MedicalTasks:
    def diagnostic_task(self, agent, patient_case) -> Task:
        # MAS Concept: Distributed Problem Solving
        return Task(
            description=f"Analyze the patient case: {patient_case}. "
                        "Identify the most likely diagnoses and provide confidence scores for each. "
                        "**Format:** Use concise bullet points.",
            expected_output="A list of 3 hypotheses with reasoning (bullet points).",
            agent=agent,
            output_json=DiagnosticReport
        )

    def treatment_planning_task(self, agent, patient_case) -> Task:
        # MAS Concept: Proactivity & Goal-Directed Behavior
        return Task(
            description=f"Based on the patient case: {patient_case}, propose a non-biased, "
                        "guideline-based treatment plan. Consider the patient's existing medications. "
                        "**Format:** concise bullet points only.",
            expected_output="A treatment list with rationale and risks (bullet points).",
            agent=agent,
            output_json=TreatmentReport
        )

    def safety_audit_task(self, agent) -> Task:
        # MAS Concept: Reactivity & Constraint Satisfaction
        return Task(
            description="Review the proposed treatment plan for any drug-drug interactions, "
                        "contraindications, or safety concerns given the patient's history. "
                        "**Format:** concise bullet points.",
            expected_output="A safety report with risks and alternatives (bullet points).",
            agent=agent,
            output_json=MedicationSafetyReport
        )

    def monitoring_simulation_task(self, agent) -> Task:
        # MAS Concept: Dynamic Feedback Loop
        return Task(
            description="Simulate the patient's physiological response to the proposed treatment over a 30-day period. "
                        "**Format:** concise bullet points.",
            expected_output="A simulation report (bullet points).",
            agent=agent
        )

    def ethical_review_task(self, agent) -> Task:
        # MAS Concept: Social Ability & Value Alignment
        return Task(
            description="Evaluate the proposed care pathway for ethical implications, including patient burden and fairness. "
                        "**Format:** concise bullet points.",
            expected_output="An ethical evaluation report (bullet points).",
            agent=agent,
            output_json=EthicsRiskEvaluation
        )

    def coordination_task(self, agent) -> Task:
        # MAS Concept: Conflict Resolution & Emergent Consensus
        return Task(
            description="Integrate all specialist findings into a single, unified Care Pathway. "
                        "**CRITICAL: Brevity is mandatory.** Focus only on the most critical actions, "
                        "primary diagnosis, and top 2-3 risks. Avoid long technical justifications. "
                        "Produce a clean, executive-level summary using **BULLET POINTS ONLY**. "
                        "Do not use dense paragraphs.",
            expected_output="A concise final care pathway JSON with bulleted summaries.",
            agent=agent,
            output_json=CarePathway
        )
