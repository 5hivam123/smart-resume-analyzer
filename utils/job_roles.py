"""
Keyword database for various job roles.
Each role maps to a list of ATS-critical keywords.
"""

JOB_ROLES = {
    "Software Developer (SDE)": [
        "Python", "Java", "C++", "JavaScript", "TypeScript",
        "REST API", "Microservices", "Docker", "Git", "GitHub",
        "Data Structures", "Algorithms", "SQL", "NoSQL",
        "System Design", "OOP", "CI/CD", "Linux", "Agile", "Scrum",
    ],
    "Data Scientist / ML Engineer": [
        "Python", "Machine Learning", "Deep Learning", "NLP",
        "TensorFlow", "PyTorch", "Scikit-learn", "Pandas", "NumPy",
        "Data Analysis", "Feature Engineering", "SQL", "Statistics",
        "Model Deployment", "Computer Vision", "Jupyter", "Matplotlib",
        "Seaborn", "Hugging Face", "LLM", "RAG",
    ],
    "Frontend Developer": [
        "HTML", "CSS", "JavaScript", "React", "Next.js", "TypeScript",
        "Tailwind CSS", "Redux", "REST API", "Git", "Responsive Design",
        "UI/UX", "Figma", "Webpack", "Performance Optimization",
        "Accessibility", "Testing", "Jest", "Storybook",
    ],
    "Backend Developer": [
        "Python", "Node.js", "Express", "FastAPI", "Django",
        "REST API", "GraphQL", "PostgreSQL", "MongoDB", "Redis",
        "Docker", "Kubernetes", "AWS", "Authentication", "JWT",
        "Microservices", "CI/CD", "Linux", "Git", "System Design",
    ],
    "Full Stack Developer": [
        "React", "Node.js", "Python", "JavaScript", "TypeScript",
        "REST API", "MongoDB", "PostgreSQL", "Docker", "Git",
        "HTML", "CSS", "Tailwind CSS", "Redux", "Express",
        "Next.js", "Authentication", "Deployment", "Agile", "CI/CD",
    ],
    "Data Analyst": [
        "SQL", "Python", "Excel", "Power BI", "Tableau",
        "Data Cleaning", "Data Visualization", "Statistics",
        "Pandas", "NumPy", "Business Intelligence", "ETL",
        "Google Sheets", "Reporting", "Dashboard", "Forecasting",
    ],
    "DevOps / Cloud Engineer": [
        "Docker", "Kubernetes", "AWS", "Azure", "GCP",
        "CI/CD", "Jenkins", "Terraform", "Ansible", "Linux",
        "Bash", "Python", "Git", "Monitoring", "Prometheus",
        "Grafana", "Nginx", "Infrastructure as Code", "Security",
    ],
    "Android Developer": [
        "Kotlin", "Java", "Android SDK", "Jetpack Compose",
        "MVVM", "Retrofit", "Room Database", "Firebase",
        "REST API", "Git", "Google Play", "Coroutines",
        "LiveData", "ViewModel", "Material Design", "Testing",
    ],
    "AI / GenAI Engineer": [
        "Python", "LLM", "Prompt Engineering", "LangChain",
        "RAG", "Hugging Face", "OpenAI API", "Fine-tuning",
        "Vector Database", "Embeddings", "FastAPI", "Docker",
        "NLP", "Machine Learning", "MLOps", "Model Deployment",
        "PyTorch", "TensorFlow", "Transformers",
    ],
    "Cybersecurity Analyst": [
        "Network Security", "SIEM", "Penetration Testing",
        "Ethical Hacking", "Kali Linux", "Wireshark", "Firewall",
        "Vulnerability Assessment", "Incident Response",
        "Python", "Bash", "OWASP", "Cryptography", "SOC",
        "Threat Intelligence", "Compliance", "CEH", "CISSP",
    ],
}
