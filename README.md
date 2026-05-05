# RAG Assistant

A Retrieval-Augmented Generation (RAG) based assistant that answers queries from an Operating Systems lab manual using local LLM inference with Ollama (Phi-3) and ChromaDB for semantic retrieval.

---

## Overview

This project implements a context-aware AI assistant that retrieves relevant sections from an OS lab manual and generates precise, grounded responses.

Unlike naive LLM chat systems, this assistant:
- Retrieves relevant context chunks from a vector database  
- Feeds them into a local LLM (Phi-3 via Ollama)  
- Produces factually grounded answers  

---

## Components

### astAPI Backend
- Handles user queries via REST API  
- Manages the RAG pipeline  
- Integrates retrieval + generation  

### ChromaDB
- Stores embeddings of OS lab manual  
- Performs semantic similarity search  
- Returns top-k relevant chunks  

### Ollama (Phi-3)
- Local LLM for inference  
- Generates answers using retrieved context  
- Ensures privacy (no external API calls)  

---

## Data Source

- Operating Systems Lab Manual  
- Preprocessed into text chunks  
- Embedded and stored in ChromaDB  

---

## Workflow

1. User sends query to FastAPI  
2. Query is embedded and matched in ChromaDB  
3. Top-k relevant chunks are retrieved  
4. Context is passed to Phi-3 via Ollama  
5. LLM generates a grounded response  

---

## Features

- Retrieval-Augmented Generation (RAG) pipeline  
- Semantic search using vector embeddings  
- Fully local LLM (Ollama Phi-3)  
- Fast API-based interaction  
- Domain-specific QA (OS lab manual)  

---

## Tech Stack

- Backend: FastAPI  
- LLM: Phi-3 (via Ollama)  
- Vector DB: ChromaDB  
- Embeddings: Sentence Transformers / Ollama embeddings  
- Language: Python  

---

## Getting Started

### 1. Clone the Repository
bash id="z9f3r1" git clone https://github.com/yourusername/rag-assistant.git cd rag-assistant 

### 2. Install Dependencies
bash id="d2l8xp" pip install -r requirements.txt 

### 3. Start Ollama (Phi-3)
bash id="6c2mzk" ollama run phi3 

### 4. Run FastAPI Server
bash id="d91kqf" uvicorn main:app --reload 

### 5. Access API Docs
id="x7v9al" http://localhost:8000/docs

---

## 🧪 Example Query

id="n3k2pq" "What is deadlock and how can it be prevented?"

👉 The system retrieves relevant sections and generates a context-aware answer.
