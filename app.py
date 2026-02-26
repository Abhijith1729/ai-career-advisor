import streamlit as st
from google import genai
import os

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

st.title("AI Career Advisor")

skills = st.text_input("Enter your skills:")

if st.button("Get Advice"):

    if not skills:
        st.warning("Please enter your skills.")
        st.stop()

    prompt = f"""
Suggest career roles, required skills, and learning roadmap
for these skills: {skills}
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash-exp",
            contents=prompt,
        )

        result = response.text

    except Exception as e:
        result = f"Error: {e}"

    st.subheader("AI Advice:")
    st.write(result)