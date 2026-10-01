/**
 * screening_page.js - Coordinates screening page actions, validation, and API flow
 */

import { screenResume } from "../api.js";
import { renderResults } from "../components/results_card.js";

export function initScreeningPage() {
  const fileDropZone = document.getElementById("file-dropzone");
  const fileInput = document.getElementById("resume-file");
  const fileNameDisplay = document.getElementById("selected-file-name");
  const jobDescriptionInput = document.getElementById("job-description");
  const submitBtn = document.getElementById("submit-btn");
  const errorAlert = document.getElementById("error-alert");
  const resultsCard = document.getElementById("results-card");
  const resultsContent = document.getElementById("results-content");

  let selectedFile = null;

  // File selection events
  fileDropZone.addEventListener("click", () => fileInput.click());

  fileInput.addEventListener("change", (e) => {
    if (e.target.files && e.target.files[0]) {
      handleFile(e.target.files[0]);
    }
  });

  // Drag and drop
  fileDropZone.addEventListener("dragover", (e) => {
    e.preventDefault();
    fileDropZone.classList.add("drag-over");
  });

  fileDropZone.addEventListener("dragleave", () => {
    fileDropZone.classList.remove("drag-over");
  });

  fileDropZone.addEventListener("drop", (e) => {
    e.preventDefault();
    fileDropZone.classList.remove("drag-over");
    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      handleFile(e.dataTransfer.files[0]);
    }
  });

  function handleFile(file) {
    const ext = file.name.substring(file.name.lastIndexOf(".")).toLowerCase();
    if (ext !== ".pdf" && ext !== ".docx") {
      showError("Please upload a valid .pdf or .docx file.");
      selectedFile = null;
      fileNameDisplay.textContent = "";
      return;
    }
    if (file.size > 5 * 1024 * 1024) {
      showError("File size exceeds 5MB limit.");
      selectedFile = null;
      fileNameDisplay.textContent = "";
      return;
    }
    clearError();
    selectedFile = file;
    fileNameDisplay.textContent = `Selected: ${file.name} (${(file.size / 1024).toFixed(1)} KB)`;
  }

  function showError(msg) {
    errorAlert.textContent = msg;
    errorAlert.style.display = "block";
  }

  function clearError() {
    errorAlert.textContent = "";
    errorAlert.style.display = "none";
  }

  submitBtn.addEventListener("click", async () => {
    clearError();

    // Required inputs validation
    if (!selectedFile) {
      showError("Please upload a resume file (PDF or DOCX).");
      return;
    }

    const jdText = jobDescriptionInput.value.trim();
    if (!jdText) {
      showError("Please paste or enter a job description.");
      return;
    }

    // Set loading state
    submitBtn.disabled = true;
    submitBtn.innerHTML = '<span class="spinner"></span> Analyzing Resume...';
    resultsCard.classList.remove("active");

    try {
      const data = await screenResume(selectedFile, jdText);
      renderResults(resultsContent, data);
      resultsCard.classList.add("active");
      resultsCard.scrollIntoView({ behavior: "smooth" });
    } catch (err) {
      showError(err.message || "An unexpected error occurred during screening.");
    } finally {
      submitBtn.disabled = false;
      submitBtn.innerHTML = "Screen Resume";
    }
  });
}
