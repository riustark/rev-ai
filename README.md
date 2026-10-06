# REV-AI — AI-Powered Repository Understanding Engine

> **Understand your codebase through natural language.**

REV-AI is an AI-powered repository understanding engine designed to analyze GitHub repositories, index source code, generate semantic embeddings, perform vector-based retrieval, and provide context-aware answers about the codebase using Large Language Models.

Instead of manually navigating through hundreds of files, developers can ask questions such as:

* "How is authentication implemented?"
* "Where is the GitHub repository data fetched?"
* "Explain the repository indexing pipeline."
* "Which service generates embeddings?"
* "How does the RAG pipeline retrieve relevant code?"
* "What does this FastAPI endpoint do?"

REV-AI retrieves the most relevant code context from the repository and uses an LLM to generate an understandable answer.

---

## 🎯 Project Objective

Modern software repositories can contain thousands of files, services, APIs, configurations, and dependencies. Understanding an unfamiliar codebase requires significant manual effort.

REV-AI addresses this problem by creating an **AI-powered semantic layer over source code**.

The core pipeline is:

```text
GitHub Repository
       │
       ▼
Repository API
       │
       ▼
Repository Structure
       │
       ▼
Repository Indexer
       │
       ▼
Code Chunk Generator
       │
       ▼
Embedding Generator
       │
       ▼
Vector Database
       │
       ▼
Semantic Retrieval
       │
       ▼
Prompt Builder
       │
       ▼
Large Language Model
       │
       ▼
AI Code Assistant
```

---

# 🏗️ Architecture

```text
                         ┌─────────────────────┐
                         │   GitHub Repository  │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   GitHub Service    │
                         │ Authentication/API  │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ Repository Service  │
                         │ Structure & Files   │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │    Index Service    │
                         │ File Discovery      │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   Chunk Service     │
                         │ Source Code Chunks  │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ Embedding Service   │
                         │ BGE Small EN v1.5   │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │      Qdrant         │
                         │   Vector Database   │
                         └──────────┬──────────┘
                                    │
                           Semantic Search
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   Search Service    │
                         │ Top-K Retrieval     │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   Prompt Service    │
                         │ Context Construction│
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │    LLM Service      │
                         │   Gemini / LLM       │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │     AI Answer       │
                         └─────────────────────┘
```

---

# 🧠 Core Concept

REV-AI implements a Retrieval-Augmented Generation architecture specifically designed for software repositories.

Instead of sending an entire repository to an LLM, the system:

1. Connects to a GitHub repository.
2. Retrieves repository structure and source files.
3. Filters relevant source files.
4. Splits source code into manageable chunks.
5. Generates vector embeddings for each chunk.
6. Stores embeddings in Qdrant.
7. Converts a developer's question into an embedding.
8. Performs semantic similarity search.
9. Retrieves the most relevant code chunks.
10. Builds an LLM prompt using the retrieved context.
11. Generates a context-aware response.

This allows the LLM to reason over the **relevant parts of the codebase instead of the entire repository**.

---

# 🚀 Key Features

## GitHub Integration

REV-AI integrates with GitHub to retrieve repository information.

Implemented capabilities include:

* GitHub authentication
* Authenticated user retrieval
* Repository listing
* Repository details
* Repository tree retrieval
* Repository file discovery

---

## Repository Indexing

The indexing layer identifies relevant source files while avoiding unnecessary directories and generated content.

The indexing pipeline includes:

```text
Repository
    ↓
File Discovery
    ↓
File Filtering
    ↓
Source File Selection
    ↓
Content Extraction
```

---

## Intelligent Code Chunking

Large source files are divided into smaller semantic units.

This makes the repository suitable for embedding and retrieval while keeping the context supplied to the LLM manageable.

```text
Source File
     │
     ▼
Chunk Generator
     │
     ├── Chunk 1
     ├── Chunk 2
     ├── Chunk 3
     └── Chunk N
```

---

## Semantic Embeddings

REV-AI uses:

**BAAI/bge-small-en-v1.5**

to convert source-code chunks and user questions into numerical vector representations.

Current embedding dimension:

```text
384
```

---

## Vector Search

Qdrant is used as the vector database.

The system stores:

```text
Embedding
+
Repository metadata
+
File information
+
Code content
```

When a developer asks a question, REV-AI performs semantic similarity search and retrieves the most relevant code chunks.

---

## Retrieval-Augmented Generation

The RAG pipeline follows:

```text
User Question
      │
      ▼
Question Embedding
      │
      ▼
Vector Search
      │
      ▼
Top-K Relevant Code Chunks
      │
      ▼
Context Builder
      │
      ▼
Prompt
      │
      ▼
LLM
      │
      ▼
Context-Aware Answer
```

---

# 🛠️ Technology Stack

| Layer                  | Technology             |
| ---------------------- | ---------------------- |
| Backend                | Python                 |
| API Framework          | FastAPI                |
| API Server             | Uvicorn                |
| Repository Integration | GitHub API             |
| Embedding Model        | BAAI/bge-small-en-v1.5 |
| Vector Database        | Qdrant                 |
| LLM                    | Google Gemini          |
| Containerization       | Docker                 |
| API Documentation      | Swagger / OpenAPI      |
| Version Control        | Git / GitHub           |

---

# 📁 Project Structure

```text
rev-ai/
│
├── backend/
│   │
│   ├── app/
│   │   ├── api/
│   │   │   ├── router.py
│   │   │   └── routes/
│   │   │       └── github.py
│   │   │
│   │   ├── core/
│   │   │   └── config.py
│   │   │
│   │   ├── schemas/
│   │   │   ├── answer_schema.py
│   │   │   ├── ask_schema.py
│   │   │   └── search_schema.py
│   │   │
│   │   ├── services/
│   │   │   ├── chunk_service.py
│   │   │   ├── embedding_service.py
│   │   │   ├── file_service.py
│   │   │   ├── github_service.py
│   │   │   ├── index_service.py
│   │   │   ├── llm_service.py
│   │   │   ├── prompt_service.py
│   │   │   ├── rag_service.py
│   │   │   ├── repository_service.py
│   │   │   ├── search_service.py
│   │   │   └── vector_service.py
│   │   │
│   │   └── main.py
│   │
│   ├── test_embedding.py
│   ├── test_llm.py
│   ├── test_prompt.py
│   ├── test_qdrant.py
│   └── test_rag.py
│
├── docker/
│
├── docs/
│   └── learning-journal.md
│
├── frontend/
│
├── scripts/
│
├── tests/
│
├── .gitignore
├── README.md
└── docker-compose.yml
```

---

# ⚙️ Backend Services

REV-AI follows a service-oriented backend structure.

### GitHub Service

Responsible for GitHub communication and repository operations.

```text
github_service.py
```

Responsibilities include:

* Authentication
* User information
* Repository retrieval
* Repository metadata
* Repository tree

---

### Repository Service

Responsible for repository-level operations and coordinating repository data.

```text
repository_service.py
```

---

### File Service

Responsible for source-file retrieval and file-level processing.

```text
file_service.py
```

---

### Index Service

Responsible for discovering and filtering files that should be indexed.

```text
index_service.py
```

---

### Chunk Service

Responsible for converting source files into chunks suitable for embedding.

```text
chunk_service.py
```

---

### Embedding Service

Responsible for generating vector representations of source code and queries.

```text
embedding_service.py
```

Model:

```text
BAAI/bge-small-en-v1.5
```

---

### Vector Service

Provides the interface between the application and Qdrant.

```text
vector_service.py
```

---

### Search Service

Converts a user question into an embedding and retrieves the most relevant repository chunks.

```text
search_service.py
```

---

### Prompt Service

Builds the context-aware prompt supplied to the LLM.

```text
prompt_service.py
```

---

### LLM Service

Handles communication with the configured Large Language Model.

```text
llm_service.py
```

---

### RAG Service

Coordinates the retrieval and generation workflow.

```text
rag_service.py
```

---

# 🔌 API Layer

REV-AI exposes its backend functionality through FastAPI.

The API layer is organized into:

```text
app/
└── api/
    ├── router.py
    └── routes/
        └── github.py
```

Interactive API documentation is available through FastAPI's Swagger UI when the application is running.

```text
/swagger
```

---

# 🧪 Current Capabilities

The current implementation supports the core repository-understanding pipeline:

* [x] GitHub authentication
* [x] Fetch authenticated GitHub user
* [x] Fetch repositories
* [x] Fetch repository details
* [x] Fetch repository tree
* [x] Repository file indexing
* [x] Source-code chunking
* [x] Embedding generation
* [x] Qdrant vector collection
* [x] Semantic vector search
* [x] Prompt construction
* [x] LLM integration
* [x] RAG-based repository questions
* [x] FastAPI API layer
* [x] Swagger API testing

---

# 🔧 Local Development

## Prerequisites

Make sure the following are installed:

* Python 3.12+
* Git
* Docker
* Docker Compose
* GitHub account
* Google Gemini API access

---

## 1. Clone the Repository

```bash
git clone https://github.com/riustark/rev-ai.git
cd rev-ai
```

---

## 2. Create a Virtual Environment

Windows:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\activate
```

Linux/macOS:

```bash
python -m venv .venv
source .venv/bin/activate
```

---

## 3. Install Dependencies

If a requirements file is available:

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file:

```env
GITHUB_TOKEN=your_github_token
GEMINI_API_KEY=your_gemini_api_key
```

Never commit `.env` to GitHub.

Use `.env.example` for sharing required configuration names.

---

# 🐳 Running Qdrant

REV-AI uses Qdrant for vector storage.

Start the infrastructure using Docker Compose:

```bash
docker compose up -d
```

Verify the running containers:

```bash
docker ps
```

---

# ▶️ Running the Backend

From the project root:

```bash
uvicorn backend.app.main:app --reload
```

Depending on the configured Python module path, the application can also be started from the backend directory.

Once running, access the FastAPI documentation through:

```text
http://localhost:8000/docs
```

---

# 🔎 Example RAG Workflow

A typical request follows this flow:

```text
Developer
   │
   │ "How does repository indexing work?"
   ▼
FastAPI
   │
   ▼
RAG Service
   │
   ▼
Embedding Service
   │
   ▼
Qdrant
   │
   │ Top-K relevant chunks
   ▼
Prompt Service
   │
   ▼
Gemini / LLM
   │
   ▼
Generated Explanation
```

Example response conceptually:

```text
Repository indexing is handled by the IndexService.

The service discovers source files, filters ignored
directories and unsupported extensions, and passes
the resulting files to the chunking pipeline...
```

The important aspect is that the answer is generated using **retrieved repository context**, rather than relying solely on the LLM's general knowledge.

---

# 🧠 Design Principles

REV-AI is designed around several engineering principles:

### Separation of Concerns

Each major responsibility is isolated into its own service.

```text
GitHub → Repository → Index → Chunk → Embed → Search → RAG → LLM
```

### Modularity

Individual services can be replaced or upgraded independently.

For example:

```text
Embedding Model
      ↓
BGE
      ↓
Future Model
```

or:

```text
Vector Database
      ↓
Qdrant
      ↓
Future Vector Store
```

### Scalability

The architecture is designed so that repository ingestion, embedding generation, vector retrieval, and LLM generation can eventually be separated into independent workers or services.

### Context-Aware Generation

The LLM should receive relevant repository context rather than unnecessary source files.

---



# 🔐 Security Considerations

REV-AI interacts with source-code repositories and external APIs.

Production deployments should implement:

* Secure secret management
* GitHub OAuth instead of manually managed tokens where appropriate
* Token encryption
* Repository-level authorization
* API authentication
* Rate limiting
* Input validation
* Audit logging
* Secure vector metadata handling
* PII and secret detection before indexing
* HTTPS/TLS
* Environment-specific configuration

**Never commit API keys, GitHub tokens, passwords, or `.env` files to the repository.**

---

# 📊 Engineering Vision

REV-AI is intended to evolve from a repository Q&A system into a broader **AI Software Engineering Intelligence Platform**.

The long-term vision is:

```text
                    REV-AI
                       │
        ┌──────────────┼──────────────┐
        │              │              │
        ▼              ▼              ▼
 Repository        Code          Architecture
 Understanding    Intelligence    Intelligence
        │              │              │
        └──────────────┼──────────────┘
                       │
                       ▼
              AI Software Engineer
```

The goal is not simply to "chat with code."

The goal is to build an intelligent system capable of understanding:

* Repository structure
* Source code
* Dependencies
* Architecture
* APIs
* Business logic
* Code relationships
* Changes over time

and eventually assist developers throughout the software-development lifecycle.

---

# 📜 License

License information will be added as the project moves toward public distribution.

---

# 👨‍💻 Project

**REV-AI — AI-Powered Repository Understanding Engine**

Built with:

```text
Python
FastAPI
GitHub API
Qdrant
Sentence Transformers
Google Gemini
Docker
```

**Repository:**
https://github.com/riustark/rev-ai
