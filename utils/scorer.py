from typing import Dict


def compute_score(analysis: Dict) -> Dict:
    """
    Compute an ATS compatibility score (0–100) with a detailed breakdown.

    Breakdown weights:
    - Keyword Match      : 40 pts
    - Sections Present   : 25 pts
    - Quantification     : 15 pts
    - Action Verbs       : 10 pts
    - Contact Info       : 10 pts
    """

    # 1. Keyword score (40 pts)
    total_kw = len(analysis["found_keywords"]) + len(analysis["missing_keywords"])
    kw_score = 0
    if total_kw > 0:
        match_ratio = len(analysis["found_keywords"]) / total_kw
        kw_score    = int(match_ratio * 40)

    # 2. Section score (25 pts)
    important_sections = ["Contact", "Skills", "Experience", "Education", "Projects"]
    bonus_sections     = ["Summary", "Certifications"]
    found = analysis["sections_found"]

    section_score = sum(5 for s in important_sections if s in found)       # 5 pts each → 25
    section_score += sum(2 for s in bonus_sections     if s in found)       # 2 pts each → bonus
    section_score  = min(section_score, 25)

    # 3. Quantification (15 pts)
    quant_score = 15 if analysis["has_numbers"] else 0

    # 4. Action verbs (10 pts)
    verb_score = min(analysis["has_power_verbs"] * 2, 10)

    # 5. Contact info (10 pts)
    contact_score  = 0
    contact_score += 4 if analysis["has_email"]    else 0
    contact_score += 3 if analysis["has_phone"]    else 0
    contact_score += 2 if analysis["has_linkedin"] else 0
    contact_score += 1 if analysis["has_github"]   else 0

    total = kw_score + section_score + quant_score + verb_score + contact_score
    total = min(total, 100)

    return {
        "total": total,
        "breakdown": {
            "🔑 Keyword Match":    int(kw_score      / 40  * 100),
            "📋 Sections":         int(section_score  / 25  * 100),
            "📈 Quantification":   int(quant_score    / 15  * 100),
            "⚡ Action Verbs":     int(verb_score     / 10  * 100),
            "📞 Contact Info":     int(contact_score  / 10  * 100),
        }
    }
