import streamlit as st
import google.generativeai as genai
import os

# configure API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# use correct model
model = genai.GenerativeModel("gemini-1.5-flash")

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
        response = model.generate_content(prompt)
        st.subheader("AI Advice:")
        st.write(response.text)

    except Exception as e:
        st.error(str(e))