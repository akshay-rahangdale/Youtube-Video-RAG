## System Architecture & Technical Deep-Dive

This system is built as a stateless, decoupled asynchronous-ready RAG (Retrieval-Augmented Generation) pipeline using FastAPI. It maps sequential, audio-derived video text transcripts into localized vector spaces for sub-second semantic retrieval.

```mermaid
graph TD
    %% Styling
    classDef processing fill:#f9f,stroke:#333,stroke-width:2px;
    classDef storage fill:#bbf,stroke:#333,stroke-width:2px;
    classDef external fill:#fbf,stroke:#333,stroke-width:2px;

    %% Ingestion Flow
    subgraph Ingestion_Pipeline [1. Ingestion Pipeline]
        A[POST /ingest] -->|Extracts Video ID| B(youtube-transcript-api)
        B -->|Fetch Raw Captions| C[Raw Transcript Text]
        C -->|RecursiveCharacterTextSplitter| D[Text Chunks <br> size: 1000, overlap: 200]
        D -->|Batch Text Input| E(SentenceTransformers <br> BAAI/bge-small-en-v1.5)
        E -->|Generate 384-Dim Vectors| F[(ChromaDB Vector Store)]
    end

    %% Chat/Retrieval Flow
    subgraph Query_and_Generation [2. Retrieval & Generation Pipeline]
        G[POST /chat] -->|User Question| H(SentenceTransformers <br> BAAI/bge-small-en-v1.5)
        H -->|Query Vector| I[Similarity Search <br> Cosine / L2 Metric]
        F .->|Filters by video_id| I
        I -->|Top-K Relevant Chunks| J[Prompt Engineering Context Builder]
        G -->|Isolate Question| J
        J -->|Context + Query Payload| K(Google Gemini API)
        K -->|Synthesized Response| L[JSON Answer Output]
    end

    %% Class assignments
    class B,D,E,H,I,J processing;
    class F storage;
    class K external;
