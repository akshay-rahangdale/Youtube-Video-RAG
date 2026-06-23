from fastapi import APIRouter

from youtube_rag.rag.retrieval import RetrievalService
from youtube_rag.rag.vector_store import vector_store
from youtube_rag.rag.chunking import TranscriptChunker
from youtube_rag.schemas.requests import IngestRequest, SearchRequest
from youtube_rag.services.embedding_service import embedding_service
from youtube_rag.services.youtube_service import YoutubeService
from youtube_rag.schemas.requests import ChatRequest
from youtube_rag.services.llm_service import llm_service

router=APIRouter()



@router.post("/ingest")
def ingest(request: IngestRequest):
    
    video_id= YoutubeService.extract_video_id(request.youtube_url)
    
    transcript = YoutubeService.get_transcript(video_id)
    
    chunks= TranscriptChunker.chunk(transcript)
    
    embeddings = [
        embedding_service.embed(chunk)
        for chunk in chunks
    ]
    
    vector_store.add_chunks(
        video_id,
        chunks,
        embeddings
    )
    return {
        "video_id":video_id,
        "chunk_count":len(chunks),
        "sample_chunk":chunks[0]
    }
    

@router.post("/search")
def search(request:SearchRequest):
    
    results = RetrievalService.retrieve(
        request.video_id,
        request.question
    )
    
    return results



@router.post("/chat")
def chat(request: ChatRequest):

    results = RetrievalService.retrieve(
    request.video_id,
    request.question
    )

    context = "\n\n".join(
        results["documents"][0]
    )

    answer = llm_service.generate(
        context=context,
        question=request.question
    )

    return {
        "answer": answer,
        "sources": results["documents"][0]
    }