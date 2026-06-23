# YouTube Video RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot that allows users to chat with YouTube videos using transcript-based semantic search and Google's Gemini models.

## Overview

This project ingests a YouTube video, extracts its transcript, chunks the content, generates vector embeddings, stores them in ChromaDB, and answers user questions using Retrieval-Augmented Generation (RAG).

### Architecture

```text
YouTube URL
      ↓
Transcript Extraction
      ↓
Text Chunking
      ↓
Embeddings (BGE Small)
      ↓
ChromaDB Vector Store
      ↓
Question
      ↓
Similarity Search
      ↓
Relevant Chunks
      ↓
Gemini
      ↓
Answer
```

---

## Tech Stack

* Python 3.13
* FastAPI
* ChromaDB
* Sentence Transformers
* LangChain Google Gemini
* youtube-transcript-api
* uv

---

## Features

* Extract transcripts from YouTube videos
* Support English and Hindi transcripts
* Chunk large transcripts
* Generate semantic embeddings
* Store embeddings in ChromaDB
* Retrieve relevant chunks using vector similarity
* Generate answers using Gemini
* REST APIs for ingestion, retrieval, and chat

---

## Project Structure

```text
youtube-video-rag/

data/
├── chroma/
└── transcripts/

src/
└── youtube_rag/
    ├── api/
    │   └── routes.py
    │
    ├── rag/
    │   ├── chunking.py
    │   ├── retrieval.py
    │   └── vector_store.py
    │
    ├── schemas/
    │   └── requests.py
    │
    ├── services/
    │   ├── youtube_service.py
    │   ├── embedding_service.py
    │   └── llm_service.py
    │
    ├── config.py
    └── main.py
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/<your-username>/youtube-video-rag.git

cd youtube-video-rag
```

### Create Virtual Environment

```bash
uv venv
```

### Install Dependencies

```bash
uv sync
```

---

## Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_gemini_api_key
```

---

## Run Application

```bash
uv run uvicorn youtube_rag.main:app --reload
```

Swagger UI:

```text
http://localhost:8000/docs
```

---

# API Documentation

## 1. Ingest Video

### Endpoint

```http
POST /ingest
```

### Request

```json
{
  "youtube_url": "https://www.youtube.com/watch?v=VIDEO_ID"
}
```

### Flow

```text
URL
 ↓
Video ID
 ↓
Transcript
 ↓
Chunking
 ↓
Embeddings
 ↓
ChromaDB
```

### Response

```json
{
  "video_id": "VIDEO_ID",
  "chunk_count": 11,
  "sample_chunk": "..."
}
```

---

## 2. Search Chunks

### Endpoint

```http
POST /search
```

### Request

```json
{
  "video_id": "VIDEO_ID",
  "question": "Why was the person late?"
}
```

### Response

```json
{
  "top_chunks": [
    "...",
    "...",
    "..."
  ]
}
```

---

## 3. Chat With Video

### Endpoint

```http
POST /chat
```

### Request

```json
{
  "video_id": "VIDEO_ID",
  "question": "Why was the person late for work?"
}
```

### Response

```json
{
  "answer": "The person was late because he missed the train and later got stuck in an elevator."
}
```

---

# How RAG Works

### Step 1: Transcript Extraction

Extract transcript from YouTube.

```python
transcript = api.fetch(video_id)
```

---

### Step 2: Chunking

Split transcript into overlapping chunks.

```python
RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
```

---

### Step 3: Embeddings

Convert text into vectors.

```python
SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
)
```

Output:

```text
384-dimensional vector
```

---

### Step 4: Storage

Store chunks and embeddings inside ChromaDB.

```python
collection.add(...)
```

Stored data:

```text
Chunk ID
Document
Embedding
Metadata
```

---

### Step 5: Retrieval

User question:

```text
Why was the person late?
```

Question embedding generated:

```text
384-dimensional vector
```

Similarity search performed:

```python
collection.query(...)
```

Top K chunks retrieved.

---

### Step 6: Answer Generation

Prompt sent to Gemini:

```text
Context:
[Retrieved Chunks]

Question:
[User Question]
```

Gemini generates the final answer.

---

## Sample Workflow

### Step 1

Ingest:

```json
{
  "youtube_url": "https://www.youtube.com/watch?v=4RVGipmXvHs"
}
```

### Step 2

Ask:

```json
{
  "video_id": "4RVGipmXvHs",
  "question": "Why was the person late?"
}
```

### Step 3

System retrieves relevant transcript chunks.

### Step 4

Gemini generates answer using retrieved context.

---

## Current Status

### Completed

* Transcript Extraction
* Chunking
* Embedding Generation
* ChromaDB Storage
* Semantic Retrieval
* Gemini Integration
* Chat Endpoint

### Planned Improvements

* Timestamp Support
* Source Citation
* Conversation Memory
* Hybrid Search
* Reranking
* Docker Support
* Cloud Deployment
* Evaluation Metrics
* Multi-Video Search

---

## Future Enhancements

### Timestamp Citations

```text
Answer:
This topic is discussed around 02:35 in the video.
```

### Multi-Video Search

Search across multiple videos simultaneously.

### Streaming Responses

Stream Gemini responses to frontend in real-time.

---

## License

MIT License

---

## Author

Akshay Rahangdale

Software Engineer | Backend | AI Engineering | RAG Systems
