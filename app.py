import streamlit as st
import requests
import json

# Page config
st.set_page_config(
    page_title="AI Career Advisor",
    page_icon="🚀",
    layout="centered"
)

# Load API key securely
OPENROUTER_API_KEY = st.secrets["OPENROUTER_API_KEY"]

# OpenRouter endpoint
API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Headers
headers = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json"
}

# UI
st.title("🚀 AI Career Advisor")
st.write("Get career roles and a step-by-step roadmap based on your skills.")

skills = st.text_input("Enter your skills (example: python, sql, machine learning)")

# Button
if st.button("Get Career Advice"):

    if not skills.strip():
        st.warning("Please enter your skills.")
        st.stop()

    with st.spinner("Analyzing your skills..."):

        payload = {
            "model": "openai/gpt-3.5-turbo",
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You are an expert career advisor. "
                        "Give structured output with:\n"
                        "1. Career Roles\n"
                        "2. Required Skills\n"
                        "3. Step-by-step Roadmap\n"
                        "4. Beginner → Intermediate → Advanced path\n"
                        "5. Project ideas\n"
                        "Be clear and structured."
                    )
                },
                {
                    "role": "user",
                    "content": f"My skills: {skills}"
                }
            ],
            "temperature": 0.7,
            "max_tokens": 800
        }

        try:
            response = requests.post(API_URL, headers=headers, json=payload)

            if response.status_code != 200:
                st.error(f"API Error: {response.text}")
                st.stop()

            data = response.json()

            result = data["choices"][0]["message"]["content"]

            st.success("Analysis complete!")

            st.subheader("📊 Career Advice")
            st.write(result)

        except Exception as e:
            st.error(f"Error: {str(e)}")