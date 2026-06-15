\# HR Assistant AI



\## Overview



HR Assistant AI is an intelligent HR support system built using Angular, FastAPI, LangGraph, FAISS, and Groq LLM.



The system allows employees to view attendance, apply for leave, submit attendance regularization requests, and ask HR-related questions through an AI assistant.



The AI Assistant uses Retrieval-Augmented Generation (RAG) to retrieve information from Zoho HR documentation and generate relevant answers.



\## Features



\- Attendance Dashboard

\- Leave Application

\- Attendance Regularization

\- AI HR Assistant Chatbot

\- RAG-based Question Answering

\- Zoho HR Documentation Knowledge Base

\- Angular Frontend

\- FastAPI Backend



\## Tech Stack



\- Angular

\- FastAPI

\- Python

\- LangChain

\- LangGraph

\- FAISS

\- HuggingFace Embeddings

\- Groq LLM



\## Project Structure



```text

hr-assistant/

├── backend/

└── hr-portal/



\## Architecture



Employee

↓

Angular Frontend

↓

FastAPI Backend

↓

LangGraph Agent

↓

Retriever Tool

↓

FAISS Vector Database

↓

Zoho HR Documentation

↓

Groq LLM

↓

AI Response



\## How It Works



1\. The user interacts with the HR Portal through the Angular frontend.

2\. The frontend sends requests to the FastAPI backend.

3\. The backend handles attendance, leave, regularization, and AI assistant requests.

4\. HR documentation from Zoho is scraped and converted into text chunks.

5\. The text chunks are converted into embeddings using HuggingFace Embeddings.

6\. The embeddings are stored in a FAISS vector database.

7\. When the user asks a question, the retriever searches the FAISS database for relevant HR content.

8\. LangGraph manages the AI workflow.

9\. Groq LLM generates the final response using the retrieved context.

10\. The answer is returned to the user through the frontend.



\## Screenshots



\### Dashboard



(Add screenshot here)



\### Attendance Dashboard



(Add screenshot here)



\### Leave Application



(Add screenshot here)



\### Regularization Form



(Add screenshot here)



\### AI HR Assistant



(Add screenshot here)



\## Future Enhancements



\- Persistent user memory

\- Multi-user authentication

\- Leave approval workflow

\- Manager dashboard

\- Real-time attendance integration

\- Database integration (MySQL/PostgreSQL)

\- Role-based access control

\- Advanced HR analytics and reporting



\## Setup Instructions



\### Backend



```bash

cd backend



python -m venv venv



venv\\Scripts\\activate



pip install -r requirements.txt



uvicorn main:app --reload

```



\### Frontend



```bash

cd hr-portal



npm install



ng serve

```



\### Access Application



Frontend:



```text

http://localhost:4200

```



Backend:



```text

http://127.0.0.1:8000

```



\## Author



\*\*Jenish Jebaraj\*\*



Computer Science Engineering Student



Sathyabama Institute of Science and Technology



GitHub: https://github.com/Jenish-69



Project: HR Assistant AI

