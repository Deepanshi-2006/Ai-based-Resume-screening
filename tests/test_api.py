"""
test_api.py - Integration tests for the FastAPI backend endpoints.
Validates FR-01 through FR-11 and integration testing criteria.
"""

from fastapi.testclient import TestClient
from backend.app import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["service"] == "resume-screening-api"


def test_screen_resume_missing_file():
    response = client.post("/screen-resume", data={"job_description": "We need Python and SQL"})
    assert response.status_code == 400
    assert "No resume file was uploaded" in response.json()["detail"]


def test_screen_resume_invalid_extension():
    files = {"file": ("resume.txt", b"plain text content", "text/plain")}
    response = client.post(
        "/screen-resume",
        data={"job_description": "We need Python and SQL"},
        files=files
    )
    assert response.status_code == 400
    assert "Unsupported file format" in response.json()["detail"]


def test_screen_resume_empty_job_description():
    files = {"file": ("resume.pdf", b"%PDF-1.4 mock content", "application/pdf")}
    response = client.post(
        "/screen-resume",
        data={"job_description": ""},
        files=files
    )
    assert response.status_code == 400
    assert "Job description cannot be empty" in response.json()["detail"]
