import streamlit as st
import requests

API_KEY = st.secrets["OPENROUTER_API_KEY"]

API_URL = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "https://your-app.streamlit.app",
    "X-Title": "AI Career Advisor"
}

st.title("AI Career Advisor")

skills = st.text_input("Enter your skills:")

if st.button("Get Advice"):
    if skills:
        payload = {
            "model": "meta-llama/llama-3-8b-instruct",
            "messages": [
                {
                    "role": "user",
                    "content": f"Suggest career roles and roadmap for these skills: {skills}"
                }
            ]
        }

        response = requests.post(API_URL, headers=headers, json=payload)

        if response.status_code == 200:
            result = response.json()["choices"][0]["message"]["content"]
            st.subheader("AI Advice:")
            st.write(result)
        else:
            st.error(response.text)