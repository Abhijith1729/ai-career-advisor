import streamlit as st
import requests

HF_TOKEN = st.secrets["HF_TOKEN"]

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-base"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "Content-Type": "application/json"
}

st.title("AI Career Advisor")

skills = st.text_input("Enter your skills:")

if st.button("Get Advice"):
    if skills:
        payload = {
            "inputs": f"Suggest career roles and roadmap for these skills: {skills}"
        }

        response = requests.post(API_URL, headers=headers, json=payload)

        if response.status_code == 200:
            result = response.json()[0]["generated_text"]
            st.subheader("AI Advice:")
            st.write(result)
        else:
            st.error(response.text)