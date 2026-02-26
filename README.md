# AI Career Advisor using Generative AI

An AI-powered career advisor built using Python and Streamlit that generates career role recommendations, skill requirements, and step-by-step learning roadmaps based on user skills.

This application uses modern Large Language Models via the OpenRouter API to provide intelligent, real-time career guidance.

---

## Features

• Enter your skills (example: Python, SQL, Machine Learning)
• Get AI-generated career role recommendations
• Receive structured learning roadmap (Beginner → Advanced)
• View required skills for each role
• Get project ideas to strengthen your portfolio
• Clean and interactive Streamlit interface
• Deployed on Streamlit Cloud

---

## Live Demo

https://ai-career-advisor.streamlit.app/

---

## Tech Stack

Frontend:
• Streamlit

Backend:
• Python
• Requests library

AI:
• OpenRouter API
• GPT-3.5-Turbo Large Language Model

Deployment:
• Streamlit Cloud

---

## Installation (Run Locally)

### 1. Clone repository

git clone https://github.com/yourusername/ai-career-advisor.git

cd ai-career-advisor

---

### 2. Install dependencies

pip install -r requirements.txt

---

### 3. Set API key

Windows PowerShell:

$env:OPENROUTER_API_KEY="your_api_key_here"

Mac/Linux:

export OPENROUTER_API_KEY="your_api_key_here"

---

### 4. Run application

streamlit run app.py

---

## Project Structure

ai-career-advisor/
│
├── app.py
├── requirements.txt
├── README.md
└── .streamlit/
└── secrets.toml

---

## Example Use Case

Input:
Python, SQL

Output:
• Career roles (Data Analyst, Data Scientist, Backend Developer)
• Required skills
• Step-by-step roadmap
• Project ideas

---

## Why this project is useful

This project helps students and beginners:

• Identify suitable career paths
• Understand skill requirements
• Get structured learning roadmap
• Plan projects for portfolio

---

## Future Improvements

• Chat interface
• Save career plans
• User authentication
• Resume-based career analysis

---

## Author

Abhijith Vyshnava

GitHub: https://github.com/abhijith1729

---

## License

This project is open source and available under the MIT License.
