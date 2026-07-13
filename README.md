📄 AI Resume Analyzer using NLP and Streamlit

## 📌 Project Overview

AI Resume Analyzer is a web application that helps job seekers evaluate how well their resume matches a specific job description. The application extracts text from a PDF resume, identifies technical skills, compares the resume with the job description using Natural Language Processing (NLP), calculates an ATS (Applicant Tracking System) match score, and provides suggestions to improve the resume.

---

## 🎯 Objective

The objective of this project is to assist users in optimizing their resumes for job applications by identifying relevant skills, highlighting missing keywords, and estimating the resume's compatibility with a target job description.

---

## ✨ Features

* Upload Resume in PDF format
* Paste or upload a Job Description
* Extract text from the uploaded resume
* Identify technical skills from the resume
* Calculate ATS Match Score using NLP
* Detect missing skills based on the job description
* Provide resume improvement suggestions
* Interactive and user-friendly Streamlit interface

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Pandas
* NumPy
* Scikit-learn
* PyPDF2
* pdfplumber
* NLTK
* Regular Expressions (Regex)

---

## 📂 Project Structure

```text
AI-Resume-Analyzer/
│── app.py
│── notebook.ipynb
│── skills.csv
│── requirements.txt
│── README.md
│── .gitignore
```

---

## 📊 Input

### Resume

* PDF (.pdf)

### Job Description

* Text pasted into the application or uploaded as a text/PDF file

---

## ⚙️ Project Workflow

1. Upload Resume
2. Extract Resume Text
3. Clean and Preprocess Text
4. Upload or Paste Job Description
5. Extract Technical Skills
6. Calculate ATS Match Score using TF-IDF and Cosine Similarity
7. Identify Missing Skills
8. Generate Resume Improvement Suggestions
9. Display Results in the Streamlit Dashboard

---

## 🤖 AI & NLP Techniques

* PDF Text Extraction
* Text Cleaning
* Skill Extraction
* TF-IDF Vectorization
* Cosine Similarity
* Keyword Matching
* ATS Score Calculation

---

## 📈 Output

The application provides:

* ATS Match Score (%)
* Skills Found
* Missing Skills
* Resume Improvement Suggestions

---

## 💻 Example

### Resume Skills

* Python
* SQL
* Machine Learning
* Git
* Power BI

### Job Description Skills

* Python
* SQL
* Docker
* AWS
* Git

### Output

```text
ATS Match Score : 86%

Skills Found
✔ Python
✔ SQL
✔ Git

Missing Skills
✘ Docker
✘ AWS

Suggestions
• Add Docker experience if applicable.
• Mention cloud-related projects.
• Include relevant certifications.
```

---

## 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/AI-Resume-Analyzer.git
```

### Navigate to the Project Folder

```bash
cd AI-Resume-Analyzer
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

---

## 📈 Future Enhancements

* Support DOCX resume uploads
* Semantic similarity using transformer-based embeddings
* AI-generated resume improvement suggestions
* Resume section detection (Education, Skills, Projects, Experience)
* Downloadable PDF analysis report
* Dashboard with visual skill match charts

---

## 🎓 Learning Outcomes

Through this project, I gained practical experience in:

* Natural Language Processing (NLP)
* PDF Text Extraction
* Text Preprocessing
* TF-IDF Vectorization
* Cosine Similarity
* Skill Extraction
* ATS Score Calculation
* Streamlit Application Development
* GitHub Project Management

---

## ⚠️ Disclaimer

This project is intended for educational and demonstration purposes. The ATS match score is an estimate based on text similarity and keyword matching and should not be considered equivalent to the evaluation performed by commercial Applicant Tracking Systems.

---

## 👩‍💻 Author

**Mansi Suryawanshi**

B.Tech in Electronics and Telecommunication Engineering
Government College of Engineering, Nagpur

