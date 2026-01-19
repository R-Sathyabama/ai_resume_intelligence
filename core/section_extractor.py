import re

SECTIONS = ["summary", "skills", "experience", "projects", "education"]

def extract_sections(text):
    sections = {}
    lower_text = text.lower()

    for section in SECTIONS:
        pattern = rf"{section}.*?(?=\n[A-Z][a-z]+|\Z)"
        match = re.search(pattern, lower_text, re.DOTALL)
        sections[section] = match.group(0) if match else ""
    
    return sections
