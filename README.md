# 🧠 AI Research Assistant

An agentic AI application that searches academic research papers from [arXiv](https://arxiv.org), downloads the PDF, extracts content, and summarizes it using OpenAI GPT-3.5 Turbo — all in one click.


![Python](https://img.shields.io/badge/Python-3.10-blue)
![Streamlit](https://img.shields.io/badge/Built%20With-Streamlit-red)
![License](https://img.shields.io/badge/License-MIT-green)

## 🚀 Features
- 🔍 Enter any research topic (e.g., “Bayesian Optimization”)
- 📚 Fetch top papers from **arXiv**
- 📄 Extract content from PDF (using PyMuPDF)
- 🤖 Summarize the paper using **GPT-3.5 Turbo**
- 🧠 Agentic flow: autonomous search → retrieval → summarization
- 📥 Download summaries as `.txt`
- 🧼 No hardcoded API keys — users enter their own key securely
- 🎨 Clean UI with expandable summaries

## 📦 Tech Stack
- Python
- Streamlit
- OpenAI API
- arXiv API
- PyMuPDF (fitz)
- Requests

## 🔐 Setup Instructions

1. Clone the repo
2. Create and activate a virtual environment:
   
   python -m venv aiagent_env
   aiagent_env\Scripts\activate  # Windows

## Install dependencies:
- pip install -r requirements.txt



## Run the app:

- streamlit run app.py

![Demo](image.png)

## OpenAI Key Security
- No keys are hardcoded.

- Users must enter their own OpenAI API key in the sidebar.

- This ensures the app is safe for deployment and usage without billing the developer.

## 📄 License
- This project is licensed under the MIT License.

## 💡 Built By
- Avinash Mynampati


## 🚀 Live Demo

Try it here: [ai-research-assistant.streamlit.app](https://ai-research-assistant7.streamlit.app)

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ai-research-assistant7.streamlit.app)
