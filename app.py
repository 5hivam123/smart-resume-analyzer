import streamlit as st
import os
from utils.parser import extract_text
from utils.analyzer import analyze_resume
from utils.scorer import compute_score
from utils.job_roles import JOB_ROLES

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Smart Resume Analyzer",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

    .main { background: #0f0f1a; color: #e8e8f0; }

    .score-card {
        background: linear-gradient(135deg, #1e1e3a 0%, #2a1a4e 100%);
        border: 1px solid #7c3aed55;
        border-radius: 16px;
        padding: 24px;
        text-align: center;
        margin-bottom: 20px;
    }
    .score-number {
        font-size: 64px;
        font-weight: 700;
        background: linear-gradient(90deg, #7c3aed, #06b6d4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .score-label { color: #a0a0c0; font-size: 14px; margin-top: -8px; }

    .keyword-chip {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 13px;
        margin: 4px;
        font-weight: 500;
    }
    .chip-found  { background: #064e3b; color: #6ee7b7; border: 1px solid #065f46; }
    .chip-missing{ background: #450a0a; color: #fca5a5; border: 1px solid #7f1d1d; }

    .section-card {
        background: #1a1a2e;
        border: 1px solid #2d2d4e;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 16px;
    }
    .section-title {
        font-size: 16px;
        font-weight: 600;
        color: #a78bfa;
        margin-bottom: 12px;
    }

    .tip-item {
        background: #1e2a3a;
        border-left: 3px solid #06b6d4;
        padding: 10px 14px;
        border-radius: 0 8px 8px 0;
        margin-bottom: 8px;
        font-size: 14px;
        color: #cbd5e1;
    }
    .stProgress > div > div > div { background: linear-gradient(90deg, #7c3aed, #06b6d4); }

    div[data-testid="stFileUploadDropzone"] {
        background: #1a1a2e !important;
        border: 2px dashed #7c3aed88 !important;
        border-radius: 12px !important;
    }
</style>
""", unsafe_allow_html=True)

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## ⚙️ Settings")

    # Popular roles shown first
    popular_roles = [
        "Software Developer (SDE)",
        "Frontend Developer",
        "Backend Developer",
        "Data Scientist",
        "Machine Learning Engineer"
    ]

    # Get all roles from JOB_ROLES
    all_roles = sorted(JOB_ROLES.keys())

    # Create final list: Popular roles first, then remaining roles alphabetically
    remaining_roles = [r for r in all_roles if r not in popular_roles]
    role_options = popular_roles + remaining_roles

    # Remember last selected role
    if "selected_role" not in st.session_state:
        st.session_state.selected_role = role_options[0]

    # Ensure saved role exists
    if st.session_state.selected_role not in role_options:
        st.session_state.selected_role = role_options[0]

    job_role = st.selectbox(
        "🎯 Target Job Role",
        role_options,
        index=role_options.index(st.session_state.selected_role),
        placeholder="Search or select a job role..."
    )

    # Save current selection
    st.session_state.selected_role = job_role

    st.markdown("---")
    st.markdown("### 📋 How It Works")
    st.markdown("""
    1. Upload your resume (PDF/DOCX)  
    2. Select a job role  
    3. Get instant ATS score  
    4. See missing keywords  
    5. Follow improvement tips  
    """)
    st.markdown("---")
    st.caption("Built with Python · NLP · Streamlit")

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("# 📄 Smart Resume Analyzer")
st.markdown("*Get ATS score, keyword gaps & actionable improvements for your resume*")

with st.expander("ℹ️ What is an ATS Score?"):
    st.markdown("""
An **Applicant Tracking System (ATS)** is software used by recruiters to automatically scan and rank resumes.

This tool estimates your ATS compatibility by analyzing:

- ✅ Resume keywords
- ✅ Resume sections
- ✅ Skills relevant to your selected job role
- ✅ Overall resume quality

A higher ATS score generally means your resume is better optimized for recruiter screening systems.
""")

st.markdown("---")

# ── Upload ────────────────────────────────────────────────────────────────────
uploaded_file = st.file_uploader(
    "📄 Upload your Resume",
    type=["pdf", "docx"],
    help="""
📋 Upload Requirements

• Supported formats: PDF (.pdf) and DOCX (.docx)
• Maximum file size: 200 MB
• Use a text-based resume for accurate analysis.
• Scanned or password-protected files may not be processed correctly.
• Uploaded resumes are used only for analysis during the current session and are not permanently stored.
""",
)

st.caption(
    "📄 Supported: PDF, DOCX | 📦 Max Size: 200 MB | 🔒 Files are processed only during the current session."
)

if uploaded_file:
    with st.spinner("🔍 Analyzing your resume..."):
        # Extract text
        resume_text = extract_text(uploaded_file)

        if not resume_text.strip():
            st.error("❌ Could not extract text from the file. This may be a scanned or corrupted PDF/DOCX.")
            st.info("Try uploading a text-based PDF or a DOCX resume.")
            st.stop()

        # Analyze
        role_keywords = JOB_ROLES[job_role]
        analysis     = analyze_resume(resume_text, role_keywords)
        score_data   = compute_score(analysis)

    # ── Layout: Score | Keyword Match ────────────────────────────────────────
    col1, col2 = st.columns([1, 2])

    with col1:
        grade_color = (
            "#22c55e" if score_data["total"] >= 75 else
            "#f59e0b" if score_data["total"] >= 50 else
            "#ef4444"
        )
        st.markdown(f"""
        <div class="score-card">
            <div class="score-number">{score_data['total']}</div>
            <div class="score-label">ATS COMPATIBILITY SCORE / 100</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="section-card"><div class="section-title">📊 Score Breakdown</div>', unsafe_allow_html=True)
        for label, val in score_data["breakdown"].items():
            st.markdown(f"**{label}**")
            st.progress(val / 100)
            st.caption(f"{val}/100")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        # Keyword analysis
        st.markdown('<div class="section-card"><div class="section-title">🔑 Keyword Analysis</div>', unsafe_allow_html=True)

        found_html   = "".join(f'<span class="keyword-chip chip-found">✓ {k}</span>'   for k in analysis["found_keywords"])
        missing_html = "".join(f'<span class="keyword-chip chip-missing">✗ {k}</span>' for k in analysis["missing_keywords"])

        if found_html:
            st.markdown(f"**Found in resume:**<br>{found_html}", unsafe_allow_html=True)
        if missing_html:
            st.markdown(f"<br>**Missing keywords:**<br>{missing_html}", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # Match rate
        total_kw  = len(analysis["found_keywords"]) + len(analysis["missing_keywords"])
        match_pct = int(len(analysis["found_keywords"]) / total_kw * 100) if total_kw else 0
        st.metric("Keyword Match Rate", f"{match_pct}%",
                  delta=f"{len(analysis['found_keywords'])} of {total_kw} keywords found")

    st.markdown("---")

    # ── Improvement Tips ─────────────────────────────────────────────────────
    col3, col4 = st.columns(2)

    with col3:
        st.markdown('<div class="section-card"><div class="section-title">💡 Improvement Tips</div>', unsafe_allow_html=True)
        for tip in analysis["tips"]:
            st.markdown(f'<div class="tip-item">• {tip}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col4:
        st.markdown('<div class="section-card"><div class="section-title">📝 Resume Sections Detected</div>', unsafe_allow_html=True)
        sections = analysis["sections_found"]
        all_sections = ["Contact", "Summary", "Skills", "Experience", "Education", "Projects", "Certifications"]
        for sec in all_sections:
            icon = "✅" if sec in sections else "❌"
            st.markdown(f"{icon} **{sec}**")
        st.markdown('</div>', unsafe_allow_html=True)

    # ── Extracted Text Preview ───────────────────────────────────────────────
    with st.expander("🔎 View Extracted Resume Text"):
        st.text_area("Raw Text", resume_text, height=300)

else:
    # Empty state
    st.markdown("""
    <div style="text-align:center; padding: 60px 20px; color: #555580;">
        <div style="font-size: 64px;">📄</div>
        <h3 style="color: #7c7caa;">Upload your resume to get started</h3>
        <p>Supports PDF and DOCX · Instant ATS score · Keyword gap analysis</p>
    </div>
    """, unsafe_allow_html=True)
