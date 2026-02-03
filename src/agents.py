from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from .tools import MedicalSimulationTools

class MedicalAgents:
    def __init__(self):
        self.tools = MedicalSimulationTools()
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash",
            verbose=True,
            temperature=0.7,
            google_api_key=os.getenv("GOOGLE_API_KEY")
        )

    def diagnostic_reasoning_agent(self) -> Agent:
        # MAS Concept: Autonomy & Specialized Reasoning
        # This agent acts independently based on its narrow expertise in diagnostics.
        return Agent(
            role="Diagnostic Reasoning Specialist",
            goal="Analyze symptoms and medical history to produce differential diagnoses with confidence scores.",
            backstory="You are an expert diagnostician with decades of experience in internal medicine. "
                      "You specialize in identifying patterns in complex patient data and considering rare conditions.",
            tools=[self.tools.simulate_diagnostic_search, self.tools.calculate_risk_score],
            allow_delegation=False,
            verbose=True,
            llm=self.llm
        )

    def treatment_planning_agent(self) -> Agent:
        # MAS Concept: Proactivity
        # Proposes multiple solutions and initiates the pathway design.
        return Agent(
            role="Treatment Planning Consultant",
            goal="Propose guideline-based treatment options tailored to the patient's specific comorbidities.",
            backstory="You are a clinical pharmacologist and treatment strategist. You focus on evidence-based medicine "
                      "and long-term outcomes, ensuring that treatment plans are comprehensive and effective.",
            tools=[self.tools.calculate_risk_score],
            allow_delegation=False,
            verbose=True,
            llm=self.llm
        )

    def medication_safety_agent(self) -> Agent:
        # MAS Concept: Reactivity & Normative Constraints
        # Reacts to proposed treatments and applies safety norms.
        return Agent(
            role="Medication Safety & Interaction Expert",
            goal="Identify potential drug-drug interactions and contraindications in proposed treatment plans.",
            backstory="You are a senior clinical pharmacist. Your primary concern is patient safety. "
                      "You are known for being meticulous and identifying risks that others might miss.",
            tools=[self.tools.check_medication_interactions],
            allow_delegation=False,
            verbose=True,
            llm=self.llm
        )

    def patient_monitoring_agent(self) -> Agent:
        # MAS Concept: Dynamic Environment & Feedback
        # Simulates a dynamic environment where the patient's state changes.
        return Agent(
            role="Patient Response Simulator",
            goal="Simulate how the patient might respond to the proposed care pathway over time.",
            backstory="You specialize in patient-centered care and longitudinal monitoring. "
                      "You predict physiological shifts and potential side effects based on patient history.",
            tools=[self.tools.calculate_risk_score],
            allow_delegation=False,
            verbose=True,
            llm=self.llm
        )

    def ethics_risk_agent(self) -> Agent:
        # MAS Concept: Social Ability (Ethics/Norms)
        # Evaluates the social and ethical dimensions of the collective decision.
        return Agent(
            role="Bioethics & Risk Oversight Officer",
            goal="Evaluate the ethical risks, patient burden, and fairness of the proposed clinical decisions.",
            backstory="You are a bioethicist focused on patient autonomy, non-maleficence, and justice. "
                      "You ensure that the care plan respects the patient's quality of life and values.",
            tools=[],
            allow_delegation=False,
            verbose=True,
            llm=self.llm
        )

    def care_coordinator_agent(self) -> Agent:
        # MAS Concept: Manager / Coordinator & Belief Modeling
        # This agent facilitates communication and resolves conflicts, reasoning about other agents' outputs.
        return Agent(
            role="Clinical Care Pathway Coordinator",
            goal="Integrate all specialist inputs into a cohesive, safe, and ethical emergent care pathway.",
            backstory="You are a highly skilled medical team leader. You excel at resolving conflicting "
                      "recommendations from different specialists and synthesizing complex information into a clear plan.",
            tools=[],
            allow_delegation=True, # Coordinator can delegate to specialists for clarification
            verbose=True,
            llm=self.llm
        )
