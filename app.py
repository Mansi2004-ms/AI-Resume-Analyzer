
import streamlit as st
import pandas as pd
import numpy as np
import pdfplumber
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# --- Helper Functions ---

def clean_text(text):
    """Cleans text by converting to lowercase and removing non-alphabetic characters."""
    text = text.lower()
    text = re.sub("[^a-zA-Z ]", " ", text)
    return text

def extract_skills(text, skill_list):
    """Extracts skills from text based on a predefined skill list."""
    found_skills = []
    for skill in skill_list:
        if skill.lower() in text:
            found_skills.append(skill)
    return found_skills

# --- Streamlit Application ---
st.title("Resume-Job Description Matcher")
st.write("Upload your resume (PDF) and a job description (TXT) to get an ATS score and identify missing skills.")

# Load skills data
try:
    df_skills = pd.read_csv("skills.csv")
    skill_list = df_skills["Skills"].tolist()
except FileNotFoundError:
    st.error("Error: 'skills.csv' not found. Please ensure the file is in the same directory as this app.")
    st.stop()

# Input: Resume Upload
resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
resume_text = ""
if resume_file:
    with pdfplumber.open(resume_file) as pdf:
        for page in pdf.pages:
            resume_text += page.extract_text()
    st.success("Resume uploaded and text extracted!")

# Input: Job Description Upload
jd_file = st.file_uploader("Upload Job Description (TXT)", type=["txt"])
jd_text = ""
if jd_file:
    jd_text = jd_file.read().decode("utf-8")
    st.success("Job Description uploaded and text extracted!")

# Perform Analysis if both files are uploaded
if resume_text and jd_text:
    st.subheader("Analysis Results")

    # Clean texts
    cleaned_resume = clean_text(resume_text)
    cleaned_jd = clean_text(jd_text)

    # Extract skills
    resume_skills = extract_skills(cleaned_resume, skill_list)
    jd_skills = extract_skills(cleaned_jd, skill_list)

    # Find missing skills
    missing_skills = list(set(jd_skills) - set(resume_skills))

    # Calculate ATS score using TF-IDF and Cosine Similarity
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform([cleaned_resume, cleaned_jd])
    cosine_sim_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    ats_score = round(cosine_sim_score * 100, 2)

    # Display ATS Score
    st.metric(label="ATS Score", value=f"{ats_score}%")

    # Provide feedback based on ATS score
    if ats_score < 50:
        st.error("Poor Resume Match: Your resume needs significant improvement for this job.")
    elif ats_score < 70:
        st.warning("Average Resume Match: Good, but there's room for improvement.")
    else:
        st.success("Excellent Resume Match: Your resume aligns well with the job description!")

    st.markdown("---")

    # Display Resume Skills
    st.subheader("Skills in Your Resume")
    if resume_skills:
        st.write(", ".join(resume_skills))
    else:
        st.write("No relevant skills found in your resume based on the provided list.")

    st.markdown("---")

    # Display Missing Skills
    st.subheader("Missing Skills (from Job Description)")
    if missing_skills:
        st.write(", ".join(missing_skills))
    else:
        st.success("You have all the listed skills from the job description!")

else:
    st.info("Please upload both your resume (PDF) and the job description (TXT) to get started.")
