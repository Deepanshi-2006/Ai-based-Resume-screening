"""
skills_data.py - Real-world tech skill catalog and synonym dictionary.
Maintains curated technical skills and acronym/alias mappings across major domains:
Programming Languages, Frontend, Backend, Databases, Cloud/DevOps, AI/ML, Testing, and Security.
"""

# Curated catalog of canonical technical skills
DEFAULT_SKILLS = [
    # 1. Programming Languages
    "python", "java", "c++", "c#", "c", "javascript", "typescript", "ruby", "php",
    "swift", "kotlin", "go", "rust", "r", "dart", "scala", "perl", "bash", "shell",
    "powershell", "lua", "haskell", "clojure", "elixir", "matlab", "vba", "cobol",

    # 2. Frontend Development
    "html", "css", "react", "angular", "vue", "next.js", "nuxt.js", "svelte",
    "tailwind css", "bootstrap", "sass", "less", "webpack", "vite", "redux", "mobx",
    "jquery", "figma", "storybook", "webgl", "three.js", "remix", "astro",

    # 3. Backend Development & APIs
    "node.js", "express", "django", "flask", "fastapi", "spring boot", "spring",
    "ruby on rails", "asp.net", "laravel", "graphql", "rest api", "grpc", "microservices",
    "websockets", "celery", "kafka", "rabbitmq", "nestjs", "gin", "fiber", "tornado",

    # 4. Databases & Caching
    "sql", "mysql", "postgresql", "mongodb", "redis", "sqlite", "oracle", "cassandra",
    "elasticsearch", "dynamodb", "firebase", "mariadb", "neo4j", "couchbase", "supabase",
    "clickhouse", "snowflake", "bigquery", "prisma", "hibernate", "sqlalchemy",

    # 5. Cloud Platforms & DevOps
    "docker", "kubernetes", "aws", "azure", "google cloud", "git", "github", "gitlab",
    "bitbucket", "ci/cd", "terraform", "ansible", "jenkins", "prometheus", "grafana",
    "nginx", "linux", "unix", "helm", "argo cd", "cloudformation", "serverless",
    "openstack", "vagrant", "splunk", "datadog",

    # 6. Artificial Intelligence & Data Science
    "machine learning", "deep learning", "data science", "natural language processing",
    "computer vision", "generative ai", "large language models", "llm", "rag",
    "tensorflow", "pytorch", "keras", "scikit-learn", "pandas", "numpy", "scipy",
    "opencv", "hugging face", "langchain", "llama-index", "data analysis",
    "data engineering", "power bi", "tableau", "spark", "hadoop", "airflow", "dbt",

    # 7. Quality Assurance & Testing
    "pytest", "unittest", "jest", "mocha", "cypress", "selenium", "playwright",
    "junit", "postman", "jmeter", "test automation", "unit testing", "integration testing",

    # 8. Mobile Development
    "android", "ios", "react native", "flutter", "xamarin", "swiftui", "jetpack compose",

    # 9. Cybersecurity & Networking
    "penetration testing", "cryptography", "owasp", "ethical hacking", "siem",
    "soc", "network security", "information security", "vulnerability assessment",

    # 10. Technical Roles & Specializations
    "backend developer", "backend development", "backend",
    "frontend developer", "frontend development", "frontend",
    "full stack developer", "full stack development", "full stack",
    "data scientist", "data analyst", "machine learning engineer",
    "devops engineer", "devops", "cloud engineer", "cloud architect",
    "mobile developer", "ios developer", "android developer",
    "software engineer", "software developer", "qa engineer",
    "security engineer", "cybersecurity analyst", "web developer",
    "web development", "api development"
]

# Aliases and acronyms mapping to canonical skill names
SKILL_ALIASES = {
    # Programming languages
    "js": "javascript",
    "ts": "typescript",
    "py": "python",
    "golang": "go",
    "c sharp": "c#",
    "c-sharp": "c#",
    "cpp": "c++",
    "c plus plus": "c++",
    "dotnet": ".net",
    ".net core": ".net",
    "dot net": ".net",
    "ror": "ruby on rails",
    "rails": "ruby on rails",

    # Web & Frontend
    "html5": "html",
    "css3": "css",
    "reactjs": "react",
    "react.js": "react",
    "vuejs": "vue",
    "vue.js": "vue",
    "angularjs": "angular",
    "nextjs": "next.js",
    "nuxtjs": "nuxt.js",
    "tailwind": "tailwind css",
    "tailwindcss": "tailwind css",

    # Backend
    "nodejs": "node.js",
    "node": "node.js",
    "rest": "rest api",
    "restful": "rest api",
    "restful api": "rest api",
    "restful apis": "rest api",
    "rest apis": "rest api",
    "micro-services": "microservices",
    "micro services": "microservices",

    # Databases
    "postgres": "postgresql",
    "mongo": "mongodb",
    "ms sql": "sql",
    "mssql": "sql",
    "relational database": "sql",
    "rdbms": "sql",
    "elastic search": "elasticsearch",

    # Cloud & DevOps
    "k8s": "kubernetes",
    "kube": "kubernetes",
    "gcp": "google cloud",
    "google cloud platform": "google cloud",
    "amazon web services": "aws",
    "amazon aws": "aws",
    "microsoft azure": "azure",
    "cicd": "ci/cd",
    "continuous integration": "ci/cd",
    "continuous deployment": "ci/cd",

    # AI / ML
    "ml": "machine learning",
    "dl": "deep learning",
    "nlp": "natural language processing",
    "cv": "computer vision",
    "genai": "generative ai",
    "gen ai": "generative ai",
    "llms": "llm",
    "large language model": "llm",
    "large language models": "llm",
    "sklearn": "scikit-learn",
    "tf": "tensorflow",
    "powerbi": "power bi",
    "huggingface": "hugging face",
    "retrieval augmented generation": "rag",

    # Mobile
    "rn": "react native",

    # Roles and Specializations
    "backend dev": "backend developer",
    "backend engineer": "backend developer",
    "backend engineering": "backend development",
    "frontend dev": "frontend developer",
    "frontend engineer": "frontend developer",
    "frontend engineering": "frontend development",
    "fullstack developer": "full stack developer",
    "fullstack": "full stack",
    "full-stack": "full stack",
    "full stack dev": "full stack developer",
    "software dev": "software developer",
    "swe": "software engineer",
    "sde": "software engineer",
    "ml engineer": "machine learning engineer",
    "ai engineer": "machine learning engineer",
    "data science engineer": "data scientist",
    "cloud devops": "devops engineer"
}
