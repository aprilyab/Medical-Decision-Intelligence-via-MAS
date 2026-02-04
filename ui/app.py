import streamlit as st
import json
import sys
import os
import uuid

# Add src to path for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.crew import MedicalCrew
from src.config import MEDICAL_DISCLAIMER, APP_NAME

def main():
    st.set_page_config(page_title=APP_NAME, layout="wide")

    st.title(f"🏥 {APP_NAME}")
  

    # Sidebar for Patient Case
    # Sidebar for Patient Case Input
    with st.sidebar:
        st.header("📋 Patient Case Input")
        
        # Helper to load sample
        if st.checkbox("Load Sample Case Data", value=False):
            try:
                with open("data/sample_case.json", "r") as f:
                    sample = json.load(f)
            except:
                sample = {}
        else:
            sample = {}

        # Common Data Lists
        COMMON_COMPLAINTS = [
            "Chest Pain", "Shortness of Breath", "Abdominal Pain", "Headache", "Fever", 
            "Fatigue", "Dizziness", "Cough", "Palpitations", "Edema", "Nausea/Vomiting"
        ]
        
        COMMON_HISTORY = [
            "Hypertension", "Type 2 Diabetes", "Asthma", "COPD", "Chronic Kidney Disease",
            "Heart Failure", "Coronary Artery Disease", "Stroke", "Obesity", "Smoking History"
        ]
        
        COMMON_MEDS = [
            "Lisinopril", "Metformin", "Atorvastatin", "Amlodipine", "Albuterol", 
            "Furosemide", "Omeprazole", "Levothyroxine", "Losartan", "Hydrochlorothiazide"
        ]
        
        # Dynamic Inputs
        age = st.number_input("Age", min_value=0, max_value=120, value=sample.get("age", 45))
        gender = st.selectbox("Gender", ["Male", "Female", "Other"], index=0 if sample.get("gender") == "Male" else 1)
        
        # Complaint Selection
        complaint_select = st.selectbox("Primary Complaint", ["Select or Type..."] + COMMON_COMPLAINTS, index=0)
        if complaint_select == "Select or Type...":
            primary_complaint = st.text_input("Enter Custom Complaint", value=sample.get("primary_complaint", "Shortness of breath"))
        else:
            primary_complaint = complaint_select
            
        # Medical History
        selected_history = st.multiselect("Medical History (Common)", COMMON_HISTORY, default=[h for h in sample.get("medical_history", []) if h in COMMON_HISTORY])
        custom_history = st.text_input("Additional History (comma separated)", value="")
        final_history = selected_history + ([h.strip() for h in custom_history.split(",")] if custom_history else [])

        # Medications
        selected_meds = st.multiselect("Current Medications (Common)", COMMON_MEDS, default=[m for m in sample.get("current_medications", []) if m in COMMON_MEDS])
        custom_meds = st.text_input("Additional Medications (comma separated)", value="")
        final_meds = selected_meds + ([m.strip() for m in custom_meds.split(",")] if custom_meds else [])

        st.subheader("Vitals")
        col_v1, col_v2 = st.columns(2)
        with col_v1:
            bp = st.text_input("BP (mmHg)", value=sample.get("vitals", {}).get("BP", "120/80"))
            spo2 = st.text_input("SpO2 (%)", value=sample.get("vitals", {}).get("SpO2", "98%"))
        with col_v2:
            hr = st.text_input("HR (bpm)", value=sample.get("vitals", {}).get("HR", "70"))
            temp = st.text_input("Temp (°C)", value=sample.get("vitals", {}).get("Temp", "37.0"))

        # Construct Patient Data Dictionary
        patient_data = {
            "case_id": f"CASE-{uuid.uuid4().hex[:8].upper()}",
            "age": age,
            "gender": gender,
            "primary_complaint": primary_complaint,
            "medical_history": final_history,
            "current_medications": final_meds,
            "symptoms": [{"name": primary_complaint, "severity": "Unknown", "duration": "Unknown"}],
            "vitals": {"BP": bp, "HR": hr, "SpO2": spo2, "Temp": temp}
        }
        
        st.divider()
        st.json(patient_data, expanded=False)

    # Main Area
    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("🕵️ Clinical Reasoning")
        if st.button("Run Clinical Simulation", type="primary"):
            with st.status("Agents are collaborating...", expanded=True) as status:
                st.write("Initializing Medical Team...")
                crew = MedicalCrew(patient_data)
                
                st.write("Specialists are analyzing the case...")
                result = crew.run()
                
                status.update(label="Simulation Complete!", state="complete", expanded=False)
            
            st.session_state['simulation_result'] = result

    with col2:
        st.subheader("🚩 Conflict & Emergent Pathway")
        if 'simulation_result' in st.session_state:
            result = st.session_state['simulation_result']
            st.info("The following pathway emerged from agent collaboration and conflict resolution:")
            
            # Attempt to parse the result
            try:
                # If result is a CrewOutput object, get the raw string
                if hasattr(result, 'raw'):
                    raw_result = result.raw
                else:
                    raw_result = str(result)
                
                # Cleanup potential markdown code blocks if present
                clean_result = raw_result.replace("```json", "").replace("```", "")
                
                import ast
                # safe parsing of python dict string
                data = ast.literal_eval(clean_result)
                
                # Render Executive Summary
                st.markdown("### 📝 Executive Summary")
                st.success(data.get("executive_summary", "No summary available."))
                
                # Detailed Breakdown
                with st.expander("🔍 Detailed Clinical Pathway", expanded=True):
                    st.markdown(f"**Final Diagnosis:** {data.get('final_diagnosis', 'N/A')}")
                    
                    st.markdown("#### 💊 Treatment Plan")
                    for plan in data.get("treatment_plan", []):
                        st.markdown(f"- **{plan.get('name')}**: {plan.get('rationale')}")
                        if plan.get('risks'):
                            st.caption(f"  *Risks: {', '.join(plan.get('risks'))}*")

                    if data.get("safety_notes"):
                        st.markdown("#### ⚠️ Safety Alerts")
                        for note in data.get("safety_notes", []):
                            st.warning(note)
                            
                    if data.get("ethical_summary"):
                         st.markdown("#### ⚖️ Ethical Considerations")
                         st.info(data.get("ethical_summary"))

            except Exception as e:
                st.warning("Could not parse structured output. Showing raw text:")
                st.markdown(result)
        else:
            st.write("Run the simulation to see results.")

    # Footer
    st.divider()


if __name__ == "__main__":
    main()
```
