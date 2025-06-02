# extract_skills.py

import spacy
import re
from docx import Document
import fitz  # PyMuPDF

nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(path):
    text = ""
    with fitz.open(path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def extract_text_from_docx(path):
    doc = Document(path)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_skills_from_text(text, skills_list):
    text = text.lower()
    found_skills = []
    doc = nlp(text)

    for token in doc:
        if token.text in skills_list:
            found_skills.append(token.text)

    # Remove duplicates
    return list(set(found_skills))

def parse_resume(resume_path, skills_list):
    if resume_path.endswith(".pdf"):
        text = extract_text_from_pdf(resume_path)
    elif resume_path.endswith(".docx"):
        text = extract_text_from_docx(resume_path)
    else:
        return []

    return extract_skills_from_text(text, skills_list)
