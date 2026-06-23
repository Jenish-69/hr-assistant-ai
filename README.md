# HR Assistant AI & HR Portal

## Overview

HR Assistant AI is an intelligent HR support system developed using FastAPI, Angular, LangChain, LangGraph, FAISS, and Groq LLM. The application provides employees with HR self-service capabilities while enabling natural language interaction through an AI-powered HR Assistant.

The system combines traditional HR portal functionalities with Retrieval-Augmented Generation (RAG) to answer employee queries based on Zoho People documentation.

---

## Project Objectives

* Provide employee self-service functionalities
* Automate HR-related query resolution
* Reduce dependency on HR personnel for common requests
* Enable intelligent document retrieval from HR knowledge sources
* Demonstrate modern AI integration within enterprise applications

---

## Features

### HR Portal

* Attendance Dashboard
* Leave Application Management
* Attendance Regularization Requests
* Employee Self-Service Interface

### AI HR Assistant

* Natural Language Question Answering
* Retrieval-Augmented Generation (RAG)
* Context-Aware Responses
* LangGraph Memory Integration
* HR Documentation Search
* Leave & Attendance Knowledge Support

---

## Technology Stack

### Frontend

* Angular
* TypeScript
* HTML
* CSS
* HttpClient
* FormsModule

### Backend

* FastAPI
* Python
* Uvicorn

### AI & Machine Learning

* LangChain
* LangGraph
* Groq LLM
* HuggingFace Embeddings
* FAISS Vector Database
* Sentence Transformers

### Knowledge Base

* Zoho People Leave Documentation
* Zoho People Attendance Documentation

---

## System Architecture

Employee

↓

Angular Frontend

↓

FastAPI Backend

↓

LangGraph Workflow

↓

Retriever Tool

↓

FAISS Vector Database

↓

Zoho HR Documentation

↓

Groq LLM

↓

AI Generated Response

---

## Project Structure

```text
hr-assistant-ai/

│
├── backend/
│   ├── main.py
│   ├── hr_graph_rag.py
│   ├── hr_graph.py
│   ├── retriever_tool.py
│   ├── create_vector_db.py
│   ├── chunk_data.py
│   ├── database.py
│   ├── schemas.py
│   ├── website_context.txt
│   └── faiss_index/
│
├── hr-portal/
│   ├── src/
│   ├── app/
│   └── assets/
│
└── README.md
```

## API Endpoints

### Home

```http
GET /
```

Response:

```json
{
  "message": "HR Assistant API Running"
}
```

### Attendance Dashboard

```http
GET /attendance
```

Returns employee attendance information.

### Apply Leave

```http
POST /apply-leave
```

Submits employee leave requests.

### Attendance Regularization

```http
POST /regularize
```

Submits attendance correction requests.

### View Leave Requests

```http
GET /leave-requests
```

Returns submitted leave records.

### View Regularization Requests

```http
GET /regularization-requests
```

Returns submitted regularization records.

### AI HR Assistant

```http
POST /ask
```

Accepts employee questions and returns AI-generated responses.

---

## Retrieval-Augmented Generation (RAG)

The HR Assistant uses Retrieval-Augmented Generation to provide accurate responses.

### Workflow

1. User submits a question
2. Question is sent to FastAPI backend
3. Retriever searches FAISS vector database
4. Relevant HR documentation chunks are retrieved
5. Context is passed to Groq LLM
6. AI generates an informed response
7. Response is returned to the user

---

## LangGraph Agent Workflow

The AI Assistant follows a structured workflow:

### Classify

Determines the category of the employee query.

### Retrieve

Searches HR knowledge documents.

### Generate Response

Uses Groq LLM to formulate the final answer.

### Memory Management

LangGraph MemorySaver stores conversational context using thread-based memory.

---

## Embedding Model

Model:

```text
sentence-transformers/all-MiniLM-L6-v2
```

Purpose:

* Convert HR documents into vector embeddings
* Enable semantic similarity search
* Improve retrieval accuracy

---

## Vector Database

FAISS (Facebook AI Similarity Search)

Purpose:

* Store document embeddings
* Perform similarity search
* Retrieve relevant HR content efficiently

---

## Knowledge Sources

The assistant is trained using content extracted from:

* Zoho People Leave Documentation
* Zoho People Attendance Documentation

The documentation is scraped, cleaned, chunked, embedded, and stored in the FAISS vector database.

---

## Testing

Successfully tested:

* Attendance Dashboard API
* Leave Submission API
* Regularization API
* HR Assistant Endpoint
* LangGraph Memory Functionality
* Retrieval Accuracy
* Frontend Integration

---

## Future Enhancements

* Zoho People API Integration
* Employee Authentication
* Role-Based Access Control
* Email Notifications
* Multi-Document Knowledge Base
* Chat Session History
* Analytics Dashboard
* Employee Profile Management

---

## Learning Outcomes

Through this project, the following concepts were implemented and explored:

* FastAPI Development
* Angular Frontend Development
* REST API Design
* LangChain
* LangGraph
* Retrieval-Augmented Generation
* FAISS Vector Search
* HuggingFace Embeddings
* Groq LLM Integration
* AI Agent Workflows
* HR Process Automation

---

## Author

Jenish Jebaraj

Computer Science Engineering

Sathyabama Institute of Science and Technology

Internship Project – HR Assistant AI & HR Portal
