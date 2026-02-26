import streamlit as st
import requests

HF_TOKEN = st.secrets.get("HF_TOKEN")

API_URL = "https://router.huggingface.co/hf-inference/models/microsoft/DialoGPT-medium"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

st.title("AI Career Advisor")

skills = st.text_input("Enter your skills:")

if st.button("Get Advice"):

    if not skills:
        st.warning("Please enter skills")
        st.stop()

    prompt = f"""
Suggest:
1. Career roles
2. Required skills
3. Learning roadmap

for these skills: {skills}
"""

    payload = {
        "inputs": prompt
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    result = response.json()

    st.subheader("AI Advice:")
    st.write(result)