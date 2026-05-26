# AI RAG Application with FastAPI, LlamaIndex, Pinecone, Terraform & Ansible

Production-ready Retrieval-Augmented Generation (RAG) application built using FastAPI, LlamaIndex, Pinecone, HuggingFace embeddings, Docker, Terraform, and Ansible.

---

# Features

- FastAPI backend
- LlamaIndex RAG pipeline
- Pinecone vector database
- HuggingFace embeddings
- Dockerized deployment
- Terraform infrastructure provisioning
- Ansible automated deployment
- Poetry dependency management
- AWS EC2 deployment

---

# Tech Stack

- Python
- FastAPI
- LlamaIndex
- Pinecone
- HuggingFace
- Docker
- Terraform
- Ansible
- Poetry
- AWS EC2

---

# Project Structure

```bash
project/
│
├── ansible/
├── terraform/
├── backend/
├── frontend/
│
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
├── poetry.lock
├── README.md
```

---

# Clone Repository

```bash
git clone YOUR_GITHUB_REPO_URL
cd YOUR_PROJECT_NAME
```

---

# Setup Poetry

## Install Poetry

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Add Poetry to PATH:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

Verify:

```bash
poetry --version
```

---

# Install Dependencies

```bash
poetry install
```

Activate shell:

```bash
poetry shell
```

---

# Run Application Locally

## Using Poetry

```bash
poetry run uvicorn main:app --reload
```

OR:

```bash
uvicorn main:app --reload
```

---

# Run Docker Application

## Build Docker Image

```bash
docker compose build
```

## Start Containers

```bash
docker compose up
```

## Run in Detached Mode

```bash
docker compose up -d
```

---

# Stop Containers

```bash
docker compose down
```

---

# Access Application

```text
http://localhost:8000
```

FastAPI Swagger Docs:

```text
http://localhost:8000/docs
```

---

# Terraform Deployment

## Initialize Terraform

```bash
cd terraform

terraform init
```

## Validate

```bash
terraform validate
```

## Deploy Infrastructure

```bash
terraform apply
```

This creates:

- EC2 Instance
- Security Groups
- SSH Access

---

# Ansible Deployment

## Test Connection

```bash
cd ansible

ansible -i inventory.ini rag_servers -m ping
```

## Deploy Application

```bash
ansible-playbook -i inventory.ini deploy.yml
```

This automatically:

- Installs Docker
- Clones latest repository
- Builds Docker image
- Starts containers

---

# Molecule Testing

## Run Ansible Tests Locally

```bash
cd ansible

molecule test
```

This validates Ansible playbooks locally before EC2 deployment.

---

# Environment Variables

Create `.env` file:

```env
PINECONE_API_KEY=your_key
OPENAI_API_KEY=your_key
```

---

# AWS Deployment Flow

```text
Terraform
    ↓
AWS EC2
    ↓
Ansible
    ↓
Docker Deployment
    ↓
FastAPI RAG Application
```

---

# Future Improvements

- CI/CD using GitHub Actions
- HTTPS with Nginx
- Custom domain
- Monitoring & logging

---

# Author

Nikunj Jadav