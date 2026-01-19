import streamlit as st

from core.resume_parser import extract_resume_text
from core.jd_parser import parse_jd_text
from core.section_extractor import extract_sections
from core.similarity_engine import compute_similarity
from core.gap_analyzer import identify_section_gaps, identify_skill_gaps
from core.skill_extractor import extract_skills
from core.ai_reasoner import generate_ai_feedback


st.set_page_config(page_title="Explainable Resume Intelligence")

st.title("Explainable AI Resume–JD Intelligence")

resume_text = None
jd = None

resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
jd_input = st.text_area("Paste Job Description")

if st.button("Analyze"):

    if not resume_file or not jd_input:
        st.error("Please upload resume and paste job description.")
    else:
        resume_text = extract_resume_text(resume_file)
        jd = parse_jd_text(jd_input)

        # Section analysis
        sections = extract_sections(resume_text)
        section_scores = {
            section: compute_similarity(content, jd)
            for section, content in sections.items()
            if content
        }

        # Skill extraction
        resume_skills = extract_skills(resume_text)
        job_skills = extract_skills(jd)


        missing_skills = identify_skill_gaps(resume_skills, job_skills)

        # UI OUTPUT
        st.subheader("📊 Section Match Scores")
        st.json(section_scores)

        st.subheader("🧠 Detected Resume Skills")
        st.write(resume_skills)

        st.subheader("📌 Required Job Skills")
        st.write(job_skills)

        st.subheader("❌ Missing Skills (Gap)")
        if missing_skills:
            for skill in missing_skills:
                st.error(skill)
        else:
            st.success("No major skill gaps detected 🎉")

        gaps = identify_section_gaps(section_scores)
        st.subheader("⚠ Section-Level Improvements")

        for item in gaps:
            if item.startswith("❌"):
                st.error(item)
            elif item.startswith("⚠"):
                st.warning(item)
            else:
                st.success(item)

        st.subheader("🧠 AI Resume Coach Explanation")

        with st.spinner("AI is analyzing your resume..."):
            ai_feedback = generate_ai_feedback(
                resume_text=resume_text,
                jd_text=jd,
                missing_skills=missing_skills
            )

        st.write(ai_feedback)
