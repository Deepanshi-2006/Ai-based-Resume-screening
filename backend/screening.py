"""
screening.py - Skill matching and scoring engine.
Implements FR-08, FR-09, and FR-10 with alias and acronym resolution.
"""

import re
from backend.skills_data import DEFAULT_SKILLS, SKILL_ALIASES


def get_skill_regex(term: str) -> re.Pattern:
    """
    Compiles a robust regex pattern for matching a skill name or alias,
    handling edge cases like 'c', 'c++', 'c#', '.net', and multi-word phrases.
    """
    escaped = re.escape(term)

    if term.lower() in {"c", "r"}:
        # Single-letter languages: must not be followed by +, #, or alphanumeric chars
        return re.compile(rf"\b{escaped}(?![+#\w])", re.IGNORECASE)

    # Prefix boundary: word boundary if starts with alphanumeric, else non-word lookbehind
    prefix = r"\b" if re.match(r"^\w", term) else r"(?<!\w)"
    # Suffix boundary: word boundary if ends with alphanumeric, else non-word lookahead
    suffix = r"\b" if re.match(r".*\w$", term) else r"(?!\w)"

    return re.compile(prefix + escaped + suffix, re.IGNORECASE)


def extract_skills_from_text(
    normalized_text: str,
    skill_vocabulary: list[str] | None = None,
    aliases: dict[str, str] | None = None
) -> list[str]:
    """
    Finds which skills from the vocabulary appear in the normalized text.
    Also searches for known aliases/acronyms and maps them to canonical skill names.
    Returns sorted list of unique detected canonical skills.
    """
    if not normalized_text:
        return []

    vocab = skill_vocabulary if skill_vocabulary is not None else DEFAULT_SKILLS
    alias_dict = aliases if aliases is not None else SKILL_ALIASES

    # Build search list: tuples of (search_term, canonical_name)
    all_terms = [(skill, skill) for skill in vocab]
    for alias_term, canonical in alias_dict.items():
        all_terms.append((alias_term, canonical))

    # Sort search terms by length descending so longer compound phrases match first
    all_terms.sort(key=lambda x: len(x[0]), reverse=True)

    detected = set()
    for term, canonical in all_terms:
        pattern = get_skill_regex(term)
        if pattern.search(normalized_text):
            detected.add(canonical.lower())

    return sorted(list(detected))


def calculate_match(
    resume_skills: list[str],
    required_skills: list[str]
) -> dict:
    """
    Calculates the skill match score:
    skill-match score = (matched required skills / total required skills) * 100
    Generates matched_skills, missing_skills, score, and plain-language explanation.
    """
    total_required = len(required_skills)

    if total_required == 0:
        return {
            "score": 0,
            "matched_skills": [],
            "missing_skills": [],
            "total_required_skills": 0,
            "explanation": "No configured skills were identified in the job description to match against."
        }

    resume_set = set(resume_skills)
    matched = [s for s in required_skills if s in resume_set]
    missing = [s for s in required_skills if s not in resume_set]

    matched_count = len(matched)
    score = round((matched_count / total_required) * 100)

    explanation = f"{matched_count} of {total_required} required skills were found in the resume."

    return {
        "score": score,
        "matched_skills": matched,
        "missing_skills": missing,
        "total_required_skills": total_required,
        "explanation": explanation
    }
