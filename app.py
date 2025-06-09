import streamlit as st
from trusted_symptom_disease import trusted_dict
from hallucination_detector import check_for_hallucination

st.set_page_config(page_title="Hallucination Detector", layout="centered")
st.title("🧠 GPT Hallucination Detection")
st.markdown("Check if GPT's diagnosis matches trusted medical knowledge.")

# Step 1: Input
symptoms = st.multiselect("Select patient symptoms", list(trusted_dict.keys()))
gpt_diagnosis_text = st.text_input("Paste GPT diagnosis (comma separated)", "malaria, covid, flu")

# Step 2: Process
if st.button("Check for Hallucination"):
    gpt_diagnosis = [d.strip() for d in gpt_diagnosis_text.split(",")]
    results = check_for_hallucination(symptoms, gpt_diagnosis)

    # Step 3: Output
    st.success("✅ Matched: " + ", ".join(results["matched"]))
    st.warning("🚨 Hallucinations: " + ", ".join(results["hallucinated"]))
    st.markdown(f"### 🎯 Confidence Score: {results['score']}%")
    
    st.markdown("### 📋 Log:")
    for log in results["logs"]:
        st.text(log)
