# Explainable AI Resume–Job Description Intelligence

An AI-powered application that analyzes a resume against a job description and provides **explainable, actionable feedback** instead of black-box scores.

This project focuses on **clarity**, **reasoning**, and **real-world usefulness**.

---

## 🚀 Features

- Resume vs Job Description semantic matching
- Section-level similarity scoring (Summary, Skills, Experience)
- Technical skill extraction from resume and JD
- Skill gap detection (missing required skills)
- Explainable AI feedback with improvement suggestions
- Local LLM support using Ollama (cost-free development)
- Easy switch to OpenAI for production use

---

## 🧠 Architecture Overview

- **UI**: Streamlit
- **Core Logic**: Modular Python engine
- **Similarity**: Sentence embeddings + cosine similarity
- **Skill Analysis**: Deterministic + AI fallback
- **AI Reasoning**: Provider-agnostic (Local / Cloud)

The system is designed to be **explainable**, **modular**, and **production-ready**.

---

## 🖥️ How to Run Locally

### 1️⃣ Clone the repository
```bash
git clone <your-repo-url>
cd ai_resume_intelligence
```
### 2️⃣ Create virtual environment
```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```
### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
### 4️⃣ Run Ollama (Local AI)

Make sure Ollama is installed and running.

Pull a lightweight model in one terminal:
```
ollama pull phi3:mini
ollama serve
```
### 5️⃣ Run the app
```bash in another terminal
Copy code
streamlit run app.py
```
### 🔁 Switching to OpenAI (Optional)₹
In core/ai_reasoner.py:

```python

USE_LOCAL_LLM = False
```
Set API key:

```bash

export OPENAI_API_KEY=your_api_key_here
```
---

## 🎯 Why This Project Is Different

Most resume analysis tools provide scores without explanation.
This project focuses on **explainable AI**, showing *why* a resume matches a job description and *how* it can be improved.

---

## 📌 Use Cases

- Resume optimization for job seekers  
- AI-powered career coaching tools  
- HR-tech prototypes  
- Portfolio demonstration of applied AI engineering  

---

## 📄 License

This project is intended for educational and portfolio purposes.

## 📄 CHANGELOG.md 
For release history and planned improvements.
