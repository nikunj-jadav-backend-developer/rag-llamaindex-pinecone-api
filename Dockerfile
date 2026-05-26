FROM python:3.11-slim

WORKDIR /app/rag-llamaindex-pinecone

# Prevent Python from creating .pyc files and __pycache__ folders
# Keeps Docker container clean
ENV PYTHONUNBUFFERED=1 

# Force Python to show logs/output immediately
# Useful for Docker logs and debugging FastAPI/Uvicorn
ENV PYTHONDONTWRITEBYTECODE=1

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]