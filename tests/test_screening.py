"""
test_screening.py - Unit tests for skill extraction, normalization, and scoring logic.
Validates FR-06, FR-07, FR-08, FR-09, and PRD Section 17 test cases.
"""

from backend.preprocessing import normalize_text, extract_candidate_details
from backend.screening import extract_skills_from_text, calculate_match


def test_normalize_text():
    raw = "  Python Developer   with   Docker,  and SQL! \n\n "
    normalized = normalize_text(raw)
    assert "  " not in normalized
    assert normalized == "python developer with docker, and sql!"


def test_skill_extraction_simple():
    text = "Proficient in Python, SQL, and Docker with some experience in HTML."
    skills = extract_skills_from_text(text)
    assert "python" in skills
    assert "sql" in skills
    assert "docker" in skills
    assert "html" in skills


def test_skill_extraction_edge_cases():
    # Test C vs C++ vs C#
    text = "Skilled in C++ and C# but not fluent in C."
    skills = extract_skills_from_text(text)
    assert "c++" in skills
    assert "c#" in skills
    assert "c" in skills

    text_cpp_only = "I only program in C++ every day."
    skills_cpp = extract_skills_from_text(text_cpp_only)
    assert "c++" in skills_cpp
    assert "c" not in skills_cpp  # C should NOT trigger from C++


def test_skill_aliases():
    text = "Experience with k8s, js, postgres, and ml pipelines."
    skills = extract_skills_from_text(text)
    assert "kubernetes" in skills
    assert "javascript" in skills
    assert "postgresql" in skills
    assert "machine learning" in skills


def test_score_calculation_100_percent():
    required = ["python", "sql", "docker"]
    resume = ["python", "sql", "docker", "git"]
    result = calculate_match(resume, required)
    assert result["score"] == 100
    assert len(result["missing_skills"]) == 0
    assert len(result["matched_skills"]) == 3


def test_score_calculation_0_percent():
    required = ["docker", "kubernetes", "aws"]
    resume = ["html", "css", "javascript"]
    result = calculate_match(resume, required)
    assert result["score"] == 0
    assert len(result["matched_skills"]) == 0
    assert len(result["missing_skills"]) == 3


def test_score_calculation_partial():
    required = ["python", "sql", "docker", "aws"]
    resume = ["python", "sql"]
    result = calculate_match(resume, required)
    assert result["score"] == 50
    assert result["matched_skills"] == ["python", "sql"]
    assert result["missing_skills"] == ["docker", "aws"]


def test_no_required_skills_found():
    required = []
    resume = ["python", "sql"]
    result = calculate_match(resume, required)
    assert result["score"] == 0
    assert "No configured skills were identified" in result["explanation"]


def test_candidate_details_extraction():
    sample_text = (
        "Alex Rivera\n"
        "Email: alex.rivera@example.com | Phone: +1-555-123-4567\n"
        "Experienced software developer..."
    )
    details = extract_candidate_details(sample_text)
    assert details["name"] == "Alex Rivera"
    assert details["email"] == "alex.rivera@example.com"
    assert "555-123-4567" in details["phone"]
