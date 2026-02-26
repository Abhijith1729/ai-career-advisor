import streamlit as st
import requests

HF_TOKEN = st.secrets["HF_TOKEN"]

API_URL = "https://router.huggingface.co/hf-inference/models/mistralai/Mistral-7B-Instruct-v0.2"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "Content-Type": "application/json"
}

st.title("AI Career Advisor")

skills = st.text_input("Enter your skills:")

if st.button("Get Advice"):

    prompt = f"Suggest career paths and roadmap for someone with skills: {skills}"

    payload = {
        "inputs": prompt
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code != 200:
        st.error(f"HF Error: {response.text}")
    else:
        result = response.json()
        st.write(result[0]["generated_text"])