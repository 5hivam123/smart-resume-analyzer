# 📄 Smart Resume Analyzer

An ATS-compatible resume analyzer that scores your resume, detects keyword gaps, and gives actionable improvement tips — all powered by NLP.

## 🚀 Features

- **ATS Score (0–100)** with detailed breakdown
- **Keyword Gap Analysis** — matched vs missing skills per job role
- **Section Detection** — checks for Contact, Skills, Experience, Projects, etc.
- **Improvement Tips** — quantification, action verbs, LinkedIn/GitHub, and more
- **10 Job Roles** — SDE, Data Scientist, Frontend, Backend, Full Stack, DevOps, Android, AI/GenAI, Cybersecurity, Data Analyst
- Supports **PDF** and **DOCX** resumes

  Contributing to Smart Resume Analyzer

Thanks for your interest in contributing to Smart Resume Analyzer as part of Elite Coders Summer of Code (ECSoC) 2026! This guide will help you get started, whether it's your first open-source contribution or your fiftieth.


📋 Table of Contents


Getting Started
Project Structure
How to Contribute
Branching & Commit Guidelines
Pull Request Process
ECSoC Labeling Rules
Code Style
Need Help?



🚀 Getting Started


Fork this repository (top-right "Fork" button)
Clone your fork locally:


bash   git clone https://github.com/<your-username>/smart-resume-analyzer.git
   cd smart-resume-analyzer


Create a virtual environment (recommended):


bash   python -m venv venv
   venv\Scripts\activate        # Windows
   # source venv/bin/activate   # Mac/Linux


Install dependencies:


bash   pip install -r requirements.txt


Run the app locally:


bash   streamlit run app.py

The app should open at http://localhost:8501


📁 Project Structure

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


🛠️ How to Contribute


Check the Issues tab for open tasks
Look for issues labeled good first issue if you're new
Comment on the issue to let others know you're working on it — please wait to be assigned before starting, to avoid duplicate work
If you have a new idea or found a bug not yet listed, open a new issue first to discuss it before submitting a PR



🌿 Branching & Commit Guidelines


Never commit directly to main
Create a descriptive branch for your work:


bash  git checkout -b fix/short-description
  # or
  git checkout -b feature/short-description


Keep commits small and focused, with clear messages:


  fix: return empty string on PDF extraction failure
  feat: add DOCX section detection for certifications


🔃 Pull Request Process


Push your branch to your fork:


bash   git push origin fix/short-description


Open a Pull Request against 5hivam123:main
In your PR description, include:

What the change does
How you tested it
Link the related issue (e.g. Fixes #1)



Keep the PR open until it has been reviewed and merged (or you've been asked to close it) — please don't close PRs unilaterally
Respond to review comments by pushing more commits to the same branch — no need to open a new PR
A maintainer will review, request changes if needed, and merge once it's ready



🏷️ ECSoC Labeling Rules

This project participates in Elite Coders Summer of Code (ECSoC) 2026, scored automatically by ECSoC Sentinel.


Every PR that should be scored must carry the ECSoC26 label before or at the time of merging
Difficulty labels (ECSoC26-L1, ECSoC26-L2, ECSoC26-L3) are assigned automatically by Sentinel after merge — contributors and maintainers should not add these manually
Bonus XP labels (good-issue, good-pr, good-ui, good-backend) can only be added by Project Admins for contributions that go beyond the expected scope
PRs without the ECSoC26 label will not be scored, so make sure it's applied before your PR is merged



🎨 Code Style


Follow existing naming conventions and file structure
Keep functions focused and readable
Add comments for non-obvious logic
Test your changes locally before submitting (upload a sample PDF/DOCX and confirm the app behaves as expected)



💬 Need Help?


Open a Discussion or comment on the relevant issue
Join the ECSoC community channels (Discord / WhatsApp) shared in the program onboarding email
Reach out to the maintainer directly:

Discord: shivam_gupta1608
LinkedIn: linkedin.com/in/shivam-gupta-788131288






Every contribution — big or small, code or docs — is welcome and appreciated. Happy coding! 🙌
