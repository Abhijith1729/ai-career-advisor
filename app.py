import streamlit as st
import google.generativeai as genai
import os

# Configure Gemini API key (read from environment variable)
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

st.title("AI Career Advisor")

skills = st.text_input("Enter your skills:")

if st.button("Get Advice"):

    if skills:

        prompt = f"Suggest career roles and a learning roadmap for these skills: {skills}"

        try:
            response = model.generate_content(prompt)
            result = response.text
        except Exception as e:
            result = f"Error generating response: {e}"

        st.subheader("AI Advice:")
        st.write(result)