import streamlit as st
import requests

HF_TOKEN = st.secrets.get("HF_TOKEN")

if not HF_TOKEN:
    st.error("HF_TOKEN not found in Streamlit Secrets.")
    st.stop()

API_URL = "https://router.huggingface.co/hf-inference/models/HuggingFaceH4/zephyr-7b-beta"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

st.title("AI Career Advisor")

skills = st.text_input("Enter your skills:")

if st.button("Get Advice"):

    if not skills:
        st.warning("Please enter skills.")
        st.stop()

    prompt = f"""
Suggest:
1. Career roles
2. Required skills
3. Learning roadmap

for skills: {skills}
"""

    payload = {
    "inputs": f"<|user|>\n{prompt}\n<|assistant|>",
    "parameters": {
        "max_new_tokens": 300,
        "temperature": 0.7
    }
}

    try:
        with st.spinner("Generating advice..."):
            response = requests.post(API_URL, headers=headers, json=payload)

            # If HF returns error page instead of JSON
            if response.status_code != 200:
                st.error(f"HF Error: {response.text}")
                st.stop()

            result = response.json()

            if isinstance(result, list):
                output = result[0]["generated_text"]
            else:
                output = str(result)

        st.subheader("AI Advice:")
        st.write(output)

    except Exception as e:
        st.error(f"Error: {e}")