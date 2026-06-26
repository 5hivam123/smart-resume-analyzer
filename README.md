# 📄 Smart Resume Analyzer

An ATS-compatible resume analyzer that scores your resume, detects keyword gaps, and gives actionable improvement tips — all powered by NLP.

## 🚀 Features

- **ATS Score (0–100)** with detailed breakdown
- **Keyword Gap Analysis** — matched vs missing skills per job role
- **Section Detection** — checks for Contact, Skills, Experience, Projects, etc.
- **Improvement Tips** — quantification, action verbs, LinkedIn/GitHub, and more
- **10 Job Roles** — SDE, Data Scientist, Frontend, Backend, Full Stack, DevOps, Android, AI/GenAI, Cybersecurity, Data Analyst
- Supports **PDF** and **DOCX** resumes

## 🛠️ Setup

### 1. Clone / Download
```bash
cd smart-resume-analyzer
```

### 2. Create Virtual Environment (recommended)
```bash
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Mac/Linux
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the App
```bash
streamlit run app.py
```

App opens at → `http://localhost:8501`

## 📁 Project Structure

```
smart-resume-analyzer/
├── app.py                  # Main Streamlit UI
├── requirements.txt
├── README.md
└── utils/
    ├── __init__.py
    ├── parser.py           # PDF & DOCX text extraction
    ├── analyzer.py         # NLP analysis engine
    ├── scorer.py           # ATS scoring logic
    └── job_roles.py        # Keyword database (10 roles)
```

## 🌐 Deploy to Streamlit Cloud (Free)

1. Push code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect repo → set `app.py` as entry point
4. Deploy!

## 📌 Resume Tips Built-in

- Quantification detection (numbers, percentages, scale)
- Power verb vs weak verb analysis
- Contact info completeness (email, phone, LinkedIn, GitHub)
- Word count check (too short / too long)

## 🧑‍💻 Tech Stack

| Layer | Tech |
|-------|------|
| UI | Streamlit |
| PDF Parsing | PyMuPDF (fitz) |
| DOCX Parsing | python-docx |
| NLP / Analysis | Python re, custom NLP logic |
| Scoring | Custom weighted algorithm |
