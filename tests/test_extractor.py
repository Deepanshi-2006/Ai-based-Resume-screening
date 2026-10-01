"""
test_extractor.py - Unit tests for file extraction and validator functions.
Validates FR-02 and FR-05.
"""

from backend.validators import validate_file_metadata, validate_job_description
from backend.extractor import extract_text


def test_validate_file_metadata_valid():
    ok, err = validate_file_metadata("resume.pdf", 1024 * 100)
    assert ok is True
    assert err == ""

    ok_docx, _ = validate_file_metadata("resume.docx", 2048)
    assert ok_docx is True


def test_validate_file_metadata_invalid_extension():
    ok, err = validate_file_metadata("resume.png", 1024)
    assert ok is False
    assert "Unsupported file format" in err


def test_validate_file_metadata_empty_file():
    ok, err = validate_file_metadata("resume.pdf", 0)
    assert ok is False
    assert "empty" in err


def test_validate_file_metadata_oversized():
    ok, err = validate_file_metadata("resume.pdf", 6 * 1024 * 1024)
    assert ok is False
    assert "exceeds" in err


def test_validate_job_description():
    ok, _ = validate_job_description("Looking for Python and SQL developer with 2 years experience.")
    assert ok is True

    empty_ok, empty_err = validate_job_description("")
    assert empty_ok is False
    assert "empty" in empty_err

    short_ok, short_err = validate_job_description("dev")
    assert short_ok is False
    assert "too short" in short_err
