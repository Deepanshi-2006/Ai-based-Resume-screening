"""
app.py - Main FastAPI application.
Provides API endpoints for health checking and resume screening.
"""

from fastapi import FastAPI, UploadFile, File, Form, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import os

from backend.validators import validate_file_metadata, validate_job_description
from backend.extractor import extract_text
from backend.preprocessing import normalize_text, extract_candidate_details
from backend.screening import extract_skills_from_text, calculate_match

app = FastAPI(
    title="AI-Based Resume Screening MVP",
    description="Explainable resume-to-job-description skill matching application.",
    version="1.0"
)

# Enable CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
@app.get("/api/health")
def health_check():
    """Health check endpoint to verify backend service status."""
    return {"status": "healthy", "service": "resume-screening-api"}


@app.post("/screen-resume")
@app.post("/api/screen-resume")
async def screen_resume(
    file: UploadFile = File(None),
    job_description: str = Form("")
):
    """
    Main screening endpoint:
    Accepts a PDF or DOCX file and job description text.
    Returns matched skills, missing skills, match percentage, and plain-language explanation.
    """
    if file is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No resume file was uploaded.")

    # 1. Read file contents into memory
    file_bytes = await file.read()
    file_size = len(file_bytes)

    # 2. Input and File Validation (FR-02, FR-04)
    is_valid_file, file_err = validate_file_metadata(file.filename or "", file_size)
    if not is_valid_file:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=file_err)

    is_valid_job, job_err = validate_job_description(job_description)
    if not is_valid_job:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=job_err)

    # 3. Text Extraction (FR-05)
    try:
        raw_resume_text = extract_text(file.filename, file_bytes)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(exc))
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected error occurred during file extraction: {str(exc)}"
        )

    # 4. Text Preprocessing (FR-06)
    normalized_resume = normalize_text(raw_resume_text)
    normalized_job = normalize_text(job_description)

    # 5. Extract Candidate Contact Details (FR-10, Display Only)
    basic_details = extract_candidate_details(raw_resume_text)

    # 6. Skill Identification & Matching (FR-07, FR-08)
    required_skills = extract_skills_from_text(normalized_job)
    resume_skills = extract_skills_from_text(normalized_resume)

    # 7. Score Calculation (FR-09)
    result = calculate_match(resume_skills, required_skills)

    # 8. Return Structured Response (FR-10)
    return {
        "score": result["score"],
        "matched_skills": result["matched_skills"],
        "missing_skills": result["missing_skills"],
        "total_required_skills": result["total_required_skills"],
        "basic_details": basic_details,
        "explanation": result["explanation"]
    }
