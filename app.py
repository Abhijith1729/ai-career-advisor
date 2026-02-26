import streamlit as st
import requests

HF_TOKEN = st.secrets["HF_TOKEN"]

API_URL = "https://router.huggingface.co/hf-inference/models/google/flan-t5-base"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "Content-Type": "application/json"
}

st.title("AI Career Advisor")

skills = st.text_input("Enter your skills:")

if st.button("Get Advice"):
    if skills:
        payload = {
            "inputs": f"Suggest career roles and roadmap for these skills: {skills}",
            "parameters": {
                "max_new_tokens": 200,
                "temperature": 0.7
            }
        }

        response = requests.post(API_URL, headers=headers, json=payload)

        if response.status_code == 200:
            data = response.json()

            if isinstance(data, list):
                result = data[0].get("generated_text", str(data))
            else:
                result = str(data)

            st.subheader("AI Advice:")
            st.write(result)

        else:
            st.error(response.text)