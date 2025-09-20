# 📊 Automated Resume Relevance Check System  

## 🚀 Problem Statement  
At Innomatics Research Labs, resume evaluation is currently **manual, inconsistent, and time-consuming**. Placement teams handle 18–20 job requirements every week, with **thousands of resumes** to review.  

This leads to:  
- ⏳ Delays in shortlisting candidates  
- ❌ Inconsistent evaluations  
- 📉 Heavy workload on placement staff  

---

## 🎯 Objective  
The **Automated Resume Relevance Check System** solves these problems by:  
- Automatically evaluating resumes against job descriptions (JD)  
- Generating a **Relevance Score (0–100)**  
- Providing a **Fit Verdict** (High / Medium / Low)  
- Highlighting **missing keywords/skills**  
- Offering **AI-powered improvement suggestions**  
- Enabling recruiters to **download reports** and analyze via dashboard  

---

## 🛠️ Tech Stack  
- **Frontend/Interface**: [Streamlit](https://streamlit.io)  
- **Backend**: Python  
- **Libraries**:  
  - `PyPDF2`, `docx2txt` → Resume & JD parsing  
  - `pandas`, `numpy` → Data analysis  
  - `matplotlib`, `plotly` → Charts & visualizations  
  - `sentence-transformers` → AI-powered semantic similarity  
- **Export**: Excel report download  

---

## 📌 Features  
✅ Upload **Job Description (PDF/DOCX)**  
✅ Upload **Multiple Resumes (PDF/DOCX)**  
✅ Extract & analyze resume content  
✅ **Relevance Score** & **Verdict (High/Medium/Low)**  
✅ **Matched vs Missing Keywords**  
✅ **Interactive Charts** (bar chart, pie chart)  
✅ **Downloadable Excel Report**  
✅ AI-powered **semantic matching** (not just keyword-based)  

---

## ⚙️ Workflow  
1. **Upload JD**  
2. **Upload Resumes**  
3. **System extracts text & analyzes**  
4. **Keyword Match + AI Semantic Similarity**  
5. **Relevance Score + Verdict generated**  
6. **Results shown in dashboard with charts**  
7. **Download report**  

---



## 🚀 Deployment  
The project is deployed on **Streamlit Cloud**.  
👉 [Live Demo Link](https://your-deployed-app.streamlit.app) *(replace with your link)*  

---

## 📥 Installation (Run Locally)  
1. Clone repo:  
   ```bash
   git clone https://github.com/your-username/resume-relevance-check.git
   cd resume-relevance-check
