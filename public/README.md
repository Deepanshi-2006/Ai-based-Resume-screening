# Frontend - AI-Based Resume Screening MVP

This is the client-side interface for the AI-Based Resume Screening application.

## Structure
- `index.html`: Main HTML entry point containing the upload interface, job description input, and results view.
- `src/styles.css`: Modern, responsive styling with clean cards, badges, and progress bars.
- `src/api.js`: Handles communication with the backend API via the standard `fetch()` API.
- `src/components/`: Modular UI helper functions for rendering skill badges, status banners, and candidate cards.
- `src/pages/`: Page rendering logic for home, screening, results, and error states.

## Running the Frontend
Simply open `index.html` in any modern web browser or serve it using a local static server (e.g. `python -m http.server 3000`).
Make sure the backend is running at `http://127.0.0.1:8000`.
