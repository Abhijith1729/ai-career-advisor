import streamlit as st
import requests
import os

# Get HuggingFace token from Streamlit secrets
HF_TOKEN = st.secrets["HF_TOKEN"]

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

st.title("AI Career Advisor")

skills = st.text_input("Enter your skills:")

if st.button("Get Advice"):

    if not skills:
        st.warning("Please enter your skills.")
        st.stop()

    prompt = f"""
Suggest:

1. Career roles
2. Required skills
3. Learning roadmap

for these skills: {skills}
"""

    payload = {
        "inputs": prompt,
        "max_length": 500
    }

    try:
        with st.spinner("Generating advice..."):
            response = requests.post(API_URL, headers=headers, json=payload)

            result = response.json()

            if isinstance(result, list):
                output = result[0]["generated_text"]
            else:
                output = str(result)

        st.subheader("AI Advice:")
        st.write(output)

    except Exception as e:
        st.error(f"Error: {e}")