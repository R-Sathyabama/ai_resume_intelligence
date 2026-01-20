import os
import requests

# ==========================
# CONFIGURATION SWITCH
# ==========================
# True  -> Use local Ollama
# False -> Use OpenAI API
USE_LOCAL_LLM = True


# ==========================
# OLLAMA CONFIG (LOCAL)
# ==========================
OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "phi3:mini"


# ==========================
# OPENAI CONFIG (CLOUD)
# ==========================
OPENAI_MODEL = "gpt-4o-mini"


# ==========================
# MAIN PUBLIC FUNCTION
# (app.py calls ONLY this)
# ==========================
def generate_ai_feedback(resume_text, jd_text, missing_skills):
    if USE_LOCAL_LLM:
        return _ollama_response(resume_text, jd_text, missing_skills)
    else:
        return _openai_response(resume_text, jd_text, missing_skills)


# ==========================
# PROMPT (SHARED)
# ==========================
def _build_prompt(resume_text, jd_text, missing_skills):
    return f"""
You are an expert technical recruiter.

TASK:
Analyze the resume against the job description.

RULES:
- Be concise
- Be specific
- No generic advice
- Use bullet points

OUTPUT FORMAT:
1. Why the resume is weak
2. Missing skills explanation
3. Suggested resume bullet improvements
4. 30-day learning roadmap

Missing Skills:
{', '.join(missing_skills) if missing_skills else 'None'}

Resume:
{resume_text}

Job Description:
{jd_text}
"""


# ==========================
# OLLAMA IMPLEMENTATION
# ==========================
def _ollama_response(resume_text, jd_text, missing_skills):
    prompt = _build_prompt(resume_text, jd_text, missing_skills)

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": OLLAMA_MODEL,
                "prompt": prompt,
                "stream": False
            },
            timeout=120
        )
        response.raise_for_status()
        return response.json().get("response", "No response from Ollama.")

    except requests.exceptions.ConnectionError:
        return "⚠️ AI engine is not running. Start it using: `ollama serve`"

    except requests.exceptions.Timeout:
        return "⚠️ AI engine took too long to respond. Try again."

    except requests.exceptions.RequestException as e:
        return f"⚠️ AI request failed: {str(e)}"

     


# ==========================
# OPENAI IMPLEMENTATION
# (only used when switch=False)
# ==========================
def _openai_response(resume_text, jd_text, missing_skills):
    try:
        from openai import OpenAI
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        prompt = _build_prompt(resume_text, jd_text, missing_skills)

        response = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"❌ OpenAI error: {str(e)}"
