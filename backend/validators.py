"""
validators.py - File and input validation module.
Enforces file format, size limits, and required field checks according to FR-02 and FR-04.
"""

# Maximum file size allowed: 5 MB
MAX_FILE_SIZE = 5 * 1024 * 1024
ALLOWED_EXTENSIONS = {".pdf", ".docx"}


def validate_file_metadata(filename: str, file_size: int) -> tuple[bool, str]:
    """Validates the uploaded file extension and size."""
    if not filename:
        return False, "No file provided."

    lower_name = filename.lower()
    has_valid_ext = any(lower_name.endswith(ext) for ext in ALLOWED_EXTENSIONS)
    if not has_valid_ext:
        return False, "Unsupported file format. Please upload a PDF or DOCX file."

    if file_size <= 0:
        return False, "Uploaded file is empty."

    if file_size > MAX_FILE_SIZE:
        return False, "File size exceeds the 5MB limit."

    return True, ""


def validate_job_description(job_description: str) -> tuple[bool, str]:
    """Validates that a non-empty job description has been provided."""
    if not job_description or not job_description.strip():
        return False, "Job description cannot be empty."

    if len(job_description.strip()) < 10:
        return False, "Job description is too short. Please provide a meaningful job description."

    return True, ""
