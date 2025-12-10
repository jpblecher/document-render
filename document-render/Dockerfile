FROM python:3.11-slim
# EnvironmentENV PYTHONDONTWRITEBYTECODE=1ENV PYTHONUNBUFFERED=1
WORKDIR /app
# System deps (falls html2docx / lxml etc. etwas brauchen, kann man hier erweitern)RUN apt-get update && apt-get install -y \    build-essential \    && rm -rf /var/lib/apt/lists/*
# Install python depsCOPY requirements.txt .RUN pip install --no-cache-dir -r requirements.txt
# Copy appCOPY app ./app
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]