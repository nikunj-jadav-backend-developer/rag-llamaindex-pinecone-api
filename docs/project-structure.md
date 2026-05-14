## Project Structure

This project follows a layered FastAPI architecture to keep the codebase clean, scalable, and maintainable.

```text
app/
├── api/              # API route definitions and versioned endpoints
├── core/             # Application configuration, logging, and exception handling
├── services/         # Business logic and orchestration layer
├── repositories/     # Data access and storage-related logic
├── schemas/          # Request and response validation models
├── utils/            # Reusable helper functions
└── main.py           # FastAPI application entry point

tests/                # Unit and integration tests
docs/                 # Project documentation


## Directory Responsibilities

### `app/`

Contains the main application source code. All backend logic related to APIs, services, configuration, schemas, repositories, and utilities is placed inside this directory.

### `app/main.py`

Application entry point. It initializes the FastAPI application, registers API routers, middleware, exception handlers, and application-level settings.

### `app/api/`

Contains all API-related code. This layer is responsible for handling HTTP requests and responses.

### `app/api/v1/`

Contains versioned API routes for version 1 of the application. API versioning helps maintain backward compatibility when future API changes are introduced.

### `app/api/v1/routes.py`

Central router file for API version 1. It includes and combines all individual route modules such as health routes, document routes, and RAG routes.

### `app/api/v1/health_routes.py`

Contains health check endpoints. These endpoints are used to verify whether the application is running properly.

### `app/core/`

Contains core application-level configuration and setup files. This includes configuration management, logging setup, exception handling, and security-related settings.

### `app/core/config.py`

Centralized configuration file. It loads environment variables from `.env`, validates configuration values, and exposes application settings such as app name, environment, API keys, Pinecone settings, upload limits, and model configuration.

### `app/core/logging.py`

Contains logging configuration for the application. It defines log format, log level, and logging behavior used across the project.

### `app/core/exceptions.py`

Contains global exception handlers. It ensures that unexpected errors return consistent and safe API responses.

### `app/services/`

Contains business logic and orchestration code. Services coordinate between API routes, repositories, external services, and third-party integrations.

### `app/services/document_service.py`

Handles document-related business logic such as file validation, file upload processing, and triggering document ingestion.

### `app/services/rag_service.py`

Handles RAG-related business logic such as receiving user questions, calling the retrieval pipeline, and returning generated answers.

### `app/services/llamaindex_service.py`

Handles LlamaIndex integration. It is responsible for loading documents, creating chunks, generating embeddings, storing vectors, and querying indexed data.

### `app/services/pinecone_service.py`

Handles Pinecone-related operations such as connecting to Pinecone, accessing indexes, and managing vector database interactions.

### `app/repositories/`

Contains data access and storage-related logic. Repositories abstract how and where data is stored.

### `app/repositories/file_repository.py`

Handles local file storage operations such as saving uploaded files to the storage directory.

### `app/schemas/`

Contains request and response validation models using Pydantic. Schemas define the structure of API inputs and outputs.

### `app/schemas/document_schema.py`

Contains request and response models related to document upload and document processing APIs.

### `app/schemas/rag_schema.py`

Contains request and response models related to RAG query APIs.

### `app/utils/`

Contains reusable helper functions that are not directly tied to a specific business feature.

### `app/utils/response_utils.py`

Contains helper functions for creating consistent API responses.

### `app/utils/file_utils.py`

Contains reusable file-related helper functions such as checking file extensions, file size, or file names.

### `tests/`

Contains unit and integration tests for the application.

### `tests/test_health.py`

Contains test cases for the health check endpoint.

### `docs/`

Contains project documentation such as architecture explanation, folder structure details, deployment steps, and development guidelines.

### `docs/project-structure.md`

Contains detailed documentation explaining the project folder structure and responsibility of each directory and file.

### `storage/`

Contains locally stored uploaded files. This directory is mainly used in local development or simple deployments.

### `storage/uploads/`

Contains uploaded documents such as PDF or TXT files before or after processing.

### `.env.example`

Sample environment configuration file. It documents all required environment variables without exposing real secret values.

### `.env`

Local environment configuration file. It contains actual secret values such as API keys. This file must not be committed to Git.

### `.gitignore`

Defines files and folders that should not be tracked by Git, such as `.env`, virtual environments, cache files, and uploaded files.

### `requirements.txt`

Contains the list of Python dependencies required to run the application.

### `Dockerfile`

Defines how to build the Docker image for the application.

### `docker-compose.yml`

Defines how to run the application container locally or on a server using Docker Compose.

### `README.md`

Main project documentation file. It provides project overview, setup instructions, usage guide, API information, and links to detailed documentation.

### `Makefile`

Contains shortcut commands for common development tasks such as running the app, running tests, building Docker images, and starting Docker Compose.