import re
from typing import Dict, List


# ── Section header patterns ───────────────────────────────────────────────────
SECTION_PATTERNS = {
    "Contact":       r"\b(contact|email|phone|linkedin|github|mobile)\b",
    "Summary":       r"\b(summary|objective|profile|about me|career objective)\b",
    "Skills":        r"\b(skills|technical skills|core competencies|technologies)\b",
    "Experience":    r"\b(experience|work experience|employment|internship|intern)\b",
    "Education":     r"\b(education|academic|qualification|degree|university|college|b\.?tech)\b",
    "Projects":      r"\b(projects|personal projects|academic projects|portfolio)\b",
    "Certifications":r"\b(certification|certificate|courses|training|udemy|coursera)\b",
}

# ── Weak action verbs that should be replaced ─────────────────────────────────
WEAK_VERBS = ["worked on", "helped with", "assisted in", "did", "made", "used"]

# ── Strong power verbs ────────────────────────────────────────────────────────
POWER_VERBS = [
    "developed", "implemented", "designed", "optimized", "built",
    "led", "architected", "deployed", "automated", "engineered",
    "improved", "reduced", "increased", "launched", "collaborated",
]


def analyze_resume(resume_text: str, role_keywords: List[str]) -> Dict:
    """
    Full NLP analysis of a resume against a target job role.
    Returns found/missing keywords, section detection, tips, and metrics.
    """
    text_lower = resume_text.lower()

    # 1. Keyword matching (case-insensitive, whole-word-ish)
    found_keywords   = []
    missing_keywords = []
    for kw in role_keywords:
        pattern = re.escape(kw.lower())
        if re.search(pattern, text_lower):
            found_keywords.append(kw)
        else:
            missing_keywords.append(kw)

    # 2. Section detection
    sections_found = [
        sec for sec, pat in SECTION_PATTERNS.items()
        if re.search(pat, text_lower, re.IGNORECASE)
    ]

    # 3. Quantification check
    has_numbers = bool(re.search(r"\d+\s?(%|x\b|percent|million|lakh|users|projects|hours|days|months)", text_lower))

    # 4. Action verb check
    has_power_verbs = sum(1 for v in POWER_VERBS if v in text_lower)
    has_weak_verbs  = [v for v in WEAK_VERBS if v in text_lower]

    # 5. Length check
    word_count = len(resume_text.split())

    # 6. Contact info check
    has_email    = bool(re.search(r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}", resume_text))
    has_linkedin = bool(re.search(r"linkedin\.com/in/", text_lower))
    has_github   = bool(re.search(r"github\.com/", text_lower))
    has_phone    = bool(re.search(r"(\+91[\-\s]?)?\d{10}", resume_text))

    # 7. Generate tips
    tips = _generate_tips(
        missing_keywords=missing_keywords,
        sections_found=sections_found,
        has_numbers=has_numbers,
        has_power_verbs=has_power_verbs,
        has_weak_verbs=has_weak_verbs,
        word_count=word_count,
        has_email=has_email,
        has_linkedin=has_linkedin,
        has_github=has_github,
    )

    return {
        "found_keywords":   found_keywords,
        "missing_keywords": missing_keywords,
        "sections_found":   sections_found,
        "has_numbers":      has_numbers,
        "has_power_verbs":  has_power_verbs,
        "has_weak_verbs":   has_weak_verbs,
        "word_count":       word_count,
        "has_email":        has_email,
        "has_linkedin":     has_linkedin,
        "has_github":       has_github,
        "has_phone":        has_phone,
        "tips":             tips,
    }


def _generate_tips(
    missing_keywords, sections_found, has_numbers,
    has_power_verbs, has_weak_verbs, word_count,
    has_email, has_linkedin, has_github
) -> List[str]:
    tips = []

    if missing_keywords:
        sample = ", ".join(missing_keywords[:4])
        tips.append(f"Add missing keywords to your Skills/Projects section: **{sample}**{'...' if len(missing_keywords) > 4 else ''}.")

    if not has_numbers:
        tips.append("Quantify your achievements — e.g. 'Reduced load time by 40%' or 'Built for 500+ users'.")

    if has_power_verbs < 3:
        tips.append("Use strong action verbs like *developed, implemented, optimized, deployed* in experience bullets.")

    if has_weak_verbs:
        weak = ", ".join(f'"{v}"' for v in has_weak_verbs[:3])
        tips.append(f"Replace weak phrases ({weak}) with impact-driven verbs.")

    if "Projects" not in sections_found:
        tips.append("Add a **Projects** section — it's critical for freshers and open-source contributors.")

    if "Certifications" not in sections_found:
        tips.append("Include certifications (Coursera, NPTEL, etc.) to boost credibility.")

    if not has_linkedin:
        tips.append("Add your LinkedIn profile URL for recruiter visibility.")

    if not has_github:
        tips.append("Include your GitHub link — especially important for CSE/Dev roles.")

    if word_count < 300:
        tips.append("Your resume seems too short. Aim for 400–600 words (1 page).")
    elif word_count > 900:
        tips.append("Resume may be too lengthy for ATS — try to keep it under 1 page (~600 words).")

    if "Summary" not in sections_found:
        tips.append("Add a 2–3 line professional summary at the top targeting your specific role.")

    if not tips:
        tips.append("Great resume! Consider tailoring the summary for each specific job application.")

    return tips
