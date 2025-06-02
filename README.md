# Personalized-Learning-Path-Recommender
Personalized Learning Path Recommender uses NLP and skill graphs to analyze resumes, identify skill gaps, and generate tailored learning paths for target job roles. Built with Streamlit and NetworkX, it helps professionals and organizations optimize upskilling and career growth efficiently.

---

## Features

- **Resume Parsing:** Extracts skills from PDF or DOCX resumes using NLP techniques.
- **Role-Based Skill Mapping:** Supports multiple job roles, each mapped to essential skills.
- **Skill Gap Analysis:** Compares current skills with target role requirements.
- **Learning Path Recommendation:** Generates step-by-step learning paths via directed skill graphs.
- **Interactive Web UI:** User-friendly interface built with Streamlit.

---

## Installation

1. Clone the repo:

   ```bash
   git clone https://github.com/kushal3980/skillpath-recommender.git
   cd skillpath-recommender
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3. Install dependencies:

  ```bash
      pip install -r requirements.txt
  ```

4. Download required spaCy model:

  ```bash
      python -m spacy download en_core_web_sm
  ```

## Project Structure

- `app.py` — Main Streamlit application.

- `recommender.py` — Logic for skill path recommendation using NetworkX.

- `skill_graph.py` — Defines the skill dependency graph.

- `extract_skills.py` — Resume parsing and skill extraction using spaCy and PyMuPDF.

- `data/roles.json` — Role-to-skills mapping file.

- `data/skills_master.txt` — Master list of recognized skills.

## License

MIT License

---

## Author

Kushal Barot
