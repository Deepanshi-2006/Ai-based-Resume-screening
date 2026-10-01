# Real-World Test Resumes & Job Benchmark Dataset

This directory contains realistic, anonymized test resumes created in accordance with **PRD Section 12 (Data Plan)** and **Section 16 (Safety and Ethical Requirements)**.

All test resumes represent benchmark categories inspired by standard research datasets (such as Kaggle's *Updated Resume Dataset* and Hugging Face's *Resume-Job-Description-Fit*), completely sanitized of personal demographic data.

---

## 📄 Test Resumes Included

| File | Format | Candidate Role | Key Skills Present | Primary Matching Job | Expected Score Range |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `data_scientist_resume.pdf` | **PDF** | Senior Data Scientist | Python, SQL, Machine Learning, Deep Learning, PyTorch, TensorFlow, Scikit-Learn, Pandas, NumPy, NLP, RAG, Power BI | `sample_jobs/data_scientist_job.txt` | **90% - 100%** |
| `devops_cloud_engineer_resume.pdf` | **PDF** | Cloud DevOps Engineer | Kubernetes (k8s), Docker, AWS, Terraform, CI/CD, Linux, Python, Bash, Prometheus, Grafana, Ansible, Git | `sample_jobs/devops_cloud_job.txt` | **90% - 100%** |
| `fullstack_developer_resume.docx` | **DOCX** | Full Stack Engineer | React, TypeScript, JavaScript, HTML, CSS, Next.js, Tailwind CSS, Node.js, Express, FastAPI, Python, PostgreSQL, Redis, Git, Jest | `sample_jobs/fullstack_engineer_job.txt` | **90% - 100%** |
| `cybersecurity_analyst_resume.pdf` | **PDF** | Cybersecurity Analyst | Network Security, Penetration Testing, OWASP, Python, Linux, Cryptography, SIEM, Ethical Hacking, Bash | `sample_jobs/cybersecurity_job.txt` | **90% - 100%** |
| `hr_manager_resume.pdf` | **PDF** | HR Manager (*Negative Control*) | Talent Acquisition, Performance Management, Employee Relations, Payroll, Benefits Administration | Any Tech Job | **0%** (Expected negative test case) |

---

## 🔄 Cross-Domain Testing (Partial & Zero Matches)

To thoroughly validate PRD Section 17 test cases:
1. **Full Match (100%):** Match `data_scientist_resume.pdf` with `data_scientist_job.txt`.
2. **Partial Match (~30%-50%):** Match `data_scientist_resume.pdf` with `python_backend_job.txt` (matches Python & SQL, but flags Docker, FastAPI, and Redis as missing).
3. **Zero Match (0%):** Match `hr_manager_resume.pdf` against `devops_cloud_job.txt` (returns 0% match with clear explanation).

---

## 🛠️ Re-generating Dataset Files
You can re-generate all PDF and DOCX files at any time by running:
```powershell
python sample_resumes/generate_dataset_samples.py
```
