# ==========================
# SECTION-LEVEL GAPS
# ==========================
def identify_section_gaps(section_scores):
    feedback = []

    for section, score in section_scores.items():
        if score < 50:
            feedback.append(f"❌ {section.title()} is weak and needs improvement")
        elif score < 70:
            feedback.append(f"⚠ {section.title()} can be strengthened")
        else:
            feedback.append(f"✅ {section.title()} is strong")

    return feedback



# ==========================
# SKILL-LEVEL GAPS
# ==========================
def identify_skill_gaps(resume_skills, job_skills):
    return sorted(set(job_skills) - set(resume_skills))
