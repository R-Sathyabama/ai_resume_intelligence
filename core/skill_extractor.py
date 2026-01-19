import re

COMMON_SKILLS = {
    "python", "java", "c++", "javascript", "typescript",
    "react", "node", "django", "flask", "fastapi",
    "sql", "mysql", "postgresql", "mongodb",
    "aws", "azure", "gcp", "docker", "kubernetes",
    "git", "github", "ci/cd",
    "machine learning", "deep learning", "nlp",
    "pandas", "numpy", "scikit-learn",
    "rest api", "graphql",
    "linux", "bash"
}

def extract_skills(text: str):
    if not text:
        return []

    text = text.lower()
    found = set()

    for skill in COMMON_SKILLS:
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, text):
            found.add(skill)

    return sorted(found)
