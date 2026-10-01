/**
 * results_card.js - Component for rendering the screening results
 */

export function renderResults(container, data) {
  const { score, matched_skills, missing_skills, total_required_skills, basic_details, explanation } = data;

  if (total_required_skills === 0) {
    container.innerHTML = `
      <div class="score-header">
        <div class="score-display">
          <div class="score-circle" style="border-color: var(--warning); color: var(--warning);">ℹ️</div>
          <div>
            <h2>No Skills Identified</h2>
            <p class="explanation-text">${escapeHtml(explanation)}</p>
          </div>
        </div>
      </div>

      <div class="alert alert-info" style="margin-top: 1rem;">
        💡 <strong>Tip for best results:</strong> Paste a complete job description with technical requirements (e.g., <em>Python, FastAPI, SQL, Docker, AWS</em>) rather than only a single job title. You can also try loading sample jobs from the <code>sample_jobs/</code> folder!
      </div>
    `;
    return;
  }

  const matchedHtml = matched_skills.length > 0
    ? matched_skills.map(s => `<span class="pill pill-matched">✓ ${escapeHtml(s)}</span>`).join("")
    : '<span class="pill-none">No required skills matched.</span>';

  const missingHtml = missing_skills.length > 0
    ? missing_skills.map(s => `<span class="pill pill-missing">✕ ${escapeHtml(s)}</span>`).join("")
    : '<span class="pill-none">None! All identified required skills are present.</span>';

  container.innerHTML = `
    <div class="score-header">
      <div class="score-display">
        <div class="score-circle">${score}%</div>
        <div>
          <h2>Match Score</h2>
          <p class="explanation-text">${escapeHtml(explanation)}</p>
        </div>
      </div>
    </div>

    <div class="contact-details">
      <div class="contact-item">
        <div class="label">Candidate Name</div>
        <div class="value">${escapeHtml(basic_details?.name || "Not detected")}</div>
      </div>
      <div class="contact-item">
        <div class="label">Email</div>
        <div class="value">${escapeHtml(basic_details?.email || "Not detected")}</div>
      </div>
      <div class="contact-item">
        <div class="label">Phone</div>
        <div class="value">${escapeHtml(basic_details?.phone || "Not detected")}</div>
      </div>
    </div>

    <div class="skills-group">
      <h3 style="color: var(--success);">Matched Skills (${matched_skills.length})</h3>
      <div class="skills-pills">${matchedHtml}</div>
    </div>

    <div class="skills-group">
      <h3 style="color: var(--danger);">Missing Skills (${missing_skills.length})</h3>
      <div class="skills-pills">${missingHtml}</div>
    </div>
  `;
}

function escapeHtml(str) {
  if (!str) return "";
  return String(str)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}
