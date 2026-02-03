import streamlit as st
import json
import sys
import os

# Add src to path for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.crew import MedicalCrew
from src.config import MEDICAL_DISCLAIMER, APP_NAME

def main():
    st.set_page_config(page_title=APP_NAME, layout="wide")

    st.title(f"🏥 {APP_NAME}")
    st.warning(f"**DISCLAIMER:** {MEDICAL_DISCLAIMER}")

    # Sidebar for Patient Case
    with st.sidebar:
        st.header("📋 Patient Case")
        try:
            with open("data/sample_case.json", "r") as f:
                patient_data = json.load(f)
            
            st.json(patient_data)
        except Exception as e:
            st.error(f"Error loading case: {e}")
            return

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
            st.info("The following pathway emerged from agent collaboration and conflict resolution:")
            st.markdown(st.session_state['simulation_result'])
        else:
            st.write("Run the simulation to see results.")

    # Footer
    st.divider()
    st.caption("Powered by CrewAI & MAS Theory. Designed for Academic Evaluation.")

if __name__ == "__main__":
    main()
