# Changelog

All notable changes to this project will be documented in this file.
The format follows Keep a Changelog and this project adheres to
Semantic Versioning.

## [0.1.0] – 2026-02-03

### Added
- Initial public release of Explainable AI Resume–Job Description Intelligence
- Resume and job description semantic similarity analysis
- Section-level similarity scoring for:
  - Summary
  - Skills
  - Experience
  - Projects
  - Education
- Sentence embedding–based similarity using Hugging Face models
- Skill extraction from resume and job description
- Skill gap detection (missing required skills)
- Explainable AI feedback including:
  - Resume weaknesses
  - Missing skill explanations
  - Suggested resume bullet improvements
  - 30-day learning roadmap
- Local LLM reasoning via Ollama
- Optional OpenAI-based reasoning fallback
- Streamlit-based interactive UI

### Changed


### Fixed


### Technical Details
- Embedding model: `all-MiniLM-L6-v2` (Hugging Face)
- Similarity metric: cosine similarity
- Local reasoning model: `phi3:mini` via Ollama
- Resume parsing using PDF text extraction
- Modular, provider-agnostic AI reasoning layer

### Known Limitations
- Skill extraction is rule-based and limited to predefined skills
- Section extraction relies on heuristic patterns
- Resume parsing quality depends on PDF structure
- No persistence or user history
- No multi-resume ranking support
