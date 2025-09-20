import streamlit as st
import PyPDF2
import docx2txt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from sentence_transformers import SentenceTransformer, util
import io

st.set_page_config(page_title="Automated Resume Relevance Check", layout="wide")

st.title("📊 Automated Resume Relevance Check System")

# ----------------------
# Upload Job Description
# ----------------------
st.header("Upload Job Description")
jd_file = st.file_uploader("Upload JD (PDF or DOCX)", type=["pdf", "docx"])

jd_text = ""
if jd_file:
    if jd_file.type == "application/pdf":
        pdf_reader = PyPDF2.PdfReader(jd_file)
        for page in pdf_reader.pages:
            jd_text += page.extract_text()
    elif jd_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        jd_text = docx2txt.process(jd_file)
    st.success("Job Description Uploaded Successfully")

# ----------------------
# Upload Resumes
# ----------------------
st.header("Upload Student Resumes")
resume_files = st.file_uploader("Upload Resumes (PDF or DOCX)", type=["pdf", "docx"], accept_multiple_files=True)

resumes_data = []
for file in resume_files:
    text = ""
    if file.type == "application/pdf":
        pdf_reader = PyPDF2.PdfReader(file)
        for page in pdf_reader.pages:
            text += page.extract_text()
    elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        text = docx2txt.process(file)
    resumes_data.append({"name": file.name, "text": text})

# ----------------------
# Keyword + AI Matching
# ----------------------
st.header("Relevance Analysis")
if jd_text and resumes_data:
    # Load AI model
    model = SentenceTransformer('all-MiniLM-L6-v2')
    jd_embedding = model.encode(jd_text, convert_to_tensor=True)

    # Extract JD keywords
    jd_keywords = set(jd_text.lower().split())
    
    results = []
    for resume in resumes_data:
        # Keyword matching
        resume_keywords = set(resume["text"].lower().split())
        matched = jd_keywords & resume_keywords
        missing = jd_keywords - resume_keywords
        keyword_score = round(len(matched) / max(1, len(jd_keywords)) * 100, 2)
        
        # AI semantic scoring
        resume_embedding = model.encode(resume["text"], convert_to_tensor=True)
        semantic_score = util.cos_sim(jd_embedding, resume_embedding).item() * 100
        
        # Weighted final score
        final_score = round((keyword_score * 0.6 + semantic_score * 0.4), 2)
        
        # Verdict based on final score
        if final_score > 70:
            verdict = "High Fit ✅"
        elif final_score > 40:
            verdict = "Medium Fit ⚠️"
        else:
            verdict = "Low Fit ❌"
        
        results.append({
            "Resume": resume["name"],
            "Keyword Score": keyword_score,
            "Semantic Score": round(semantic_score,2),
            "Final Score": final_score,
            "Verdict": verdict,
            "Matched Keywords": ", ".join(list(matched)[:20]),
            "Missing Keywords": ", ".join(list(missing)[:20])
        })
    
    df = pd.DataFrame(results)
    
    st.subheader("📋 Relevance Scoreboard")
    st.dataframe(df, use_container_width=True)
    
    # ----------------------
    # Charts
    # ----------------------
    st.subheader("📊 Charts")
    fig1 = px.bar(df, x="Resume", y="Final Score", color="Verdict", title="Resume Relevance Scores")
    st.plotly_chart(fig1, use_container_width=True)
    
    fig2, ax = plt.subplots()
    ax.pie(df["Final Score"], labels=df["Resume"], autopct="%1.1f%%")
    ax.set_title("Score Distribution")
    st.pyplot(fig2)
    
    # ----------------------
    # Download report
    # ----------------------
    st.subheader("📥 Download Report")
    output = io.BytesIO()
    df.to_excel(output, index=False, engine='openpyxl')
    output.seek(0)
    st.download_button(label="Download Excel Report", data=output, file_name="resume_relevance_report.xlsx")

st.info("✅ All features work. Keyword and AI-based semantic scoring included!")
