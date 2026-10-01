/**
 * api.js - Frontend API client module.
 * Communicates with the backend /screen-resume and /health endpoints via Fetch API.
 */

const API_BASE_URL = "http://127.0.0.1:8000";

/**
 * Checks backend health status.
 */
export async function checkBackendHealth() {
  try {
    const response = await fetch(`${API_BASE_URL}/health`);
    return response.ok;
  } catch (error) {
    console.warn("Backend health check failed:", error);
    return false;
  }
}

/**
 * Submits the resume file and job description to the backend.
 * @param {File} resumeFile 
 * @param {string} jobDescription 
 * @returns {Promise<Object>} Screening result JSON
 */
export async function screenResume(resumeFile, jobDescription) {
  const formData = new FormData();
  formData.append("file", resumeFile);
  formData.append("job_description", jobDescription);

  try {
    const response = await fetch(`${API_BASE_URL}/screen-resume`, {
      method: "POST",
      body: formData,
    });

    const data = await response.json();

    if (!response.ok) {
      const errorMsg = data.detail || "An error occurred while screening the resume.";
      throw new Error(errorMsg);
    }

    return data;
  } catch (error) {
    if (error.name === "TypeError" && error.message.includes("fetch")) {
      throw new Error("Unable to connect to the backend server. Please verify the Python API is running on http://127.0.0.1:8000.");
    }
    throw error;
  }
}
