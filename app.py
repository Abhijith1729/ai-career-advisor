import streamlit as st
from google import genai
import os

# create client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

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

for skills: {skills}
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        st.subheader("AI Advice:")
        st.write(response.text)

    except Exception as e:
        st.error(str(e))