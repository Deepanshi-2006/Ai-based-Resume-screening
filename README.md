# AI-Based Resume Screening MVP

An explainable, transparent, rule-based resume-to-job-description skill matching application built as a B.Tech 3rd-year academic project.

---

## 🎯 Project Overview
This project allows a user to upload a resume (PDF or DOCX) and paste a job description. The system extracts text from the document, identifies required and candidate skills using a transparent vocabulary, calculates a deterministic match score, and highlights both matched and missing skills.

Unlike opaque "black-box" models or external paid APIs, this system focuses on **transparency, privacy, and explainability**, ensuring the user understands exactly how the match score was derived.

> **Ethical Note:** This tool is designed strictly as an assistance prototype for human review. It does not make automated hiring or rejection decisions, and does not evaluate personal demographic attributes.

---

## 📁 Project Structure

```
AI-Based Resume Screening/
├── backend/
│   ├── app.py              # FastAPI entry point & API endpoints
│   ├── extractor.py        # PDF (pypdf) & DOCX (python-docx) text extraction
│   ├── preprocessing.py    # Text normalization & regex detail extraction
│   ├── screening.py        # Skill extraction, matching & scoring logic
│   ├── skills_data.py      # Configurable skill catalog
│   ├── validators.py       # File size, extension, & input validation
│   ├── requirements.txt    # Backend Python dependencies
│   └── uploads/            # Temporary storage (git ignored)
├── frontend/
│   ├── index.html          # Main web application UI
│   ├── README.md           # Frontend guide
│   └── src/
│       ├── api.js          # Fetch client for backend communication
│       ├── styles.css      # Modern responsive UI styles
│       ├── components/     # UI rendering components (results card)
│       └── pages/          # Page event and interaction handlers
├── sample_resumes/         # Anonymized / fictional test resumes
├── sample_jobs/            # Sample job descriptions for testing
├── tests/
│   ├── test_extractor.py   # Validation and extraction tests
│   ├── test_screening.py   # Skill matching and scoring unit tests
│   └── test_api.py         # FastAPI endpoint integration tests
├── .gitignore              # Ignored files (venv, uploads, cache)
├── LICENSE                 # MIT License
└── README.md               # Project documentation
```

---

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.10+ (tested on Python 3.14)
- Modern web browser (Chrome, Edge, Firefox)

### 1. Backend Setup
1. Navigate to the project root directory in your terminal:
   ```bash
   cd "AI-Based Resume Screening"
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. Install dependencies:
   ```bash
   pip install -r backend/requirements.txt
   ```

4. Start the FastAPI backend server:
   ```bash
   uvicorn backend.app:app --reload --port 8000
   ```
   *The API will be available at `http://127.0.0.1:8000` and interactive API docs at `http://127.0.0.1:8000/docs`.*

### 2. Frontend Setup
1. Open `frontend/index.html` directly in your browser:
   - Or run a local HTTP server:
     ```bash
     cd frontend
     python -m http.server 3000
     ```
2. Navigate to `http://127.0.0.1:3000` in your web browser.

---

## 🧪 Running Automated Tests

Run the test suite using `pytest`:
```bash
pytest tests/ -v
```

---

## 📊 Scoring Formula
$$\text{Skill-Match Score} = \left(\frac{\text{Matched Required Skills}}{\text{Total Required Skills}}\right) \times 100$$

If no configured skills are detected in the job description, the system provides an informative message to prevent division by zero or misleading zero scores.

---

## 🛡️ Safety & Ethical Requirements
1. **Human-in-the-Loop:** System provides assist metrics only; human evaluation is required.
2. **Exclusion of Sensitive Attributes:** Names, ages, gender, photos, addresses, and demographic details are strictly excluded from score calculation.
3. **Data Privacy:** Files are processed temporarily in memory without persistent retention or transmission to third-party AI services.
