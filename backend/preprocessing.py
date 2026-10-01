"""
preprocessing.py - Text normalization and basic detail extraction.
Implements FR-06: normalizes case, spacing, and basic punctuation.
Also extracts basic contact information (email, phone, candidate name).
"""

import re


def normalize_text(text: str) -> str:
    """
    Normalizes text for consistent comparison:
    - Converts to lowercase
    - Normalizes unicode quotation marks/apostrophes
    - Replaces multiple whitespace with a single space
    """
    if not text:
        return ""

    # Convert to lowercase
    normalized = text.lower()

    # Normalize special dashes and quotes
    normalized = re.sub(r"[–—]", "-", normalized)
    normalized = re.sub(r"[''´`]", "'", normalized)
    normalized = re.sub(r'[""“”]', '"', normalized)

    # Normalize multiple whitespace, tabs, and newlines to a single space
    normalized = re.sub(r"\s+", " ", normalized).strip()
    return normalized


def extract_email(text: str) -> str:
    """Extract candidate email using regular expressions."""
    email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"
    match = re.search(email_pattern, text)
    return match.group(0) if match else "Not detected"


def extract_phone(text: str) -> str:
    """Extract candidate phone number using regular expressions."""
    # Matches common international and domestic formats like +1 234 567 8900, +91 9876543210, (123) 456-7890
    phone_pattern = r"(\+?\d{1,3}[\s-]?)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}\b"
    match = re.search(phone_pattern, text)
    return match.group(0).strip() if match else "Not detected"


def extract_name(text: str) -> str:
    """
    Extract candidate name heuristically:
    Takes the first non-empty line of the resume, cleaning out common headers,
    section labels, honorifics, and contact formatting.
    """
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if not lines:
        return "Not detected"

    disallowed_keywords = {
        "resume", "curriculum vitae", "cv", "summary", "profile", "objective",
        "experience", "education", "skills", "projects", "contact", "professional"
    }

    for line in lines[:8]:
        # Filter out lines that look like emails, URLs, or phone numbers
        if "@" in line or "http" in line.lower() or "www." in line.lower() or any(char.isdigit() for char in line):
            continue

        lower_line = line.lower()
        if any(keyword in lower_line for keyword in disallowed_keywords):
            continue

        # Strip titles/honorifics or trailing punctuation for validation
        clean_words = [re.sub(r"[^\w]", "", w) for w in line.split() if w.strip()]
        if 1 <= len(clean_words) <= 4 and all(w.isalpha() for w in clean_words):
            return line

    return "Not detected"


def extract_candidate_details(raw_text: str) -> dict:
    """Extracts basic contact fields (name, email, phone) without using sensitive personal attributes."""
    return {
        "name": extract_name(raw_text),
        "email": extract_email(raw_text),
        "phone": extract_phone(raw_text)
    }
