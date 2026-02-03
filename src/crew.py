from crewai import Crew, Process
from .agents import MedicalAgents
from .tasks import MedicalTasks

class MedicalCrew:
    def __init__(self, patient_case):
        self.patient_case = patient_case
        self.agents = MedicalAgents()
        self.tasks = MedicalTasks()

    def setup_crew(self) -> Crew:
        # MAS Concept: Hierarchical Organization & Manager Pattern
        # The Coordinator agent acts as a manager, overseeing the specialists.
        
        # Instantiate Agents
        diagnostician = self.agents.diagnostic_reasoning_agent()
        treatment_planner = self.agents.treatment_planning_agent()
        safety_expert = self.agents.medication_safety_agent()
        monitor = self.agents.patient_monitoring_agent()
        ethicist = self.agents.ethics_risk_agent()
        coordinator = self.agents.care_coordinator_agent()

        # Instantiate Tasks
        task_diag = self.tasks.diagnostic_task(diagnostician, self.patient_case)
        task_treat = self.tasks.treatment_planning_task(treatment_planner, self.patient_case)
        task_safety = self.tasks.safety_audit_task(safety_expert)
        task_monitor = self.tasks.monitoring_simulation_task(monitor)
        task_ethics = self.tasks.ethical_review_task(ethicist)
        task_coord = self.tasks.coordination_task(coordinator)

        # Assemble the Crew
        return Crew(
            agents=[diagnostician, treatment_planner, safety_expert, monitor, ethicist, coordinator],
            tasks=[task_diag, task_treat, task_safety, task_monitor, task_ethics, task_coord],
            process=Process.hierarchical,
            manager_agent=coordinator,
            memory=True, # MAS Concept: Shared Memory
            verbose=True
        )

    def run(self):
        crew = self.setup_crew()
        return crew.kickoff()
