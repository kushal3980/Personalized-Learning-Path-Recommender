import streamlit as st
import os
import tempfile
import json

from recommender import recommend_path
from extract_skills import parse_resume

# Load master skill list
with open("data/skills_master.txt", "r") as f:
    master_skills = [line.strip().lower() for line in f.readlines()]

# Load role-to-skills mapping
with open("data/roles.json", "r") as f:
    roles_dict = json.load(f)

st.set_page_config(page_title="Personalized Learning Path Recommender")

st.title("📘 Personalized Learning Path Recommender")
st.write("Upload your resume and choose a target role to get a personalized upskilling path.")

# Resume upload
uploaded_file = st.file_uploader("📄 Upload your resume (.pdf or .docx)", type=["pdf", "docx"])
target_role = st.selectbox("🎯 Select Target Job Role", list(roles_dict.keys()))

if st.button("🔍 Recommend Learning Path"):
    if not target_role:
        st.warning("Please select a target role.")
    else:
        if uploaded_file:
            # Save to temp file
            with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[-1]) as tmp_file:
                tmp_file.write(uploaded_file.read())
                resume_path = tmp_file.name

            user_skills = parse_resume(resume_path, master_skills)
            os.remove(resume_path)

            st.subheader("🧠 Skills Extracted From Resume")
            st.write(", ".join(user_skills) if user_skills else "No recognizable skills found.")

        else:
            st.info("No resume uploaded. Please input your known skills manually.")
            user_input = st.text_input("🔧 Enter your known skills (comma-separated)")
            user_skills = [skill.strip().lower() for skill in user_input.split(",") if skill]

        required_skills = roles_dict[target_role]
        missing_skills = list(set(required_skills) - set(user_skills))

        st.subheader("🚧 Skill Gap")
        if missing_skills:
            st.write("You need to learn the following skills:")
            st.write(", ".join(missing_skills))
        else:
            st.success("🎉 You already have all skills required for this role!")

        # Recommend learning path
        st.subheader("📚 Recommended Learning Path")
        if missing_skills:
            target_skill = missing_skills[-1]
            path = recommend_path(user_skills, target_skill)
            st.code(" → ".join(path))
