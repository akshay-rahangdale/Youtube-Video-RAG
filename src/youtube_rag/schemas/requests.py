from pydantic import BaseModel
class IngestRequest(BaseModel):
    youtube_url: str
    
class SearchRequest(BaseModel):
    video_id: str
    question: str
    
class ChatRequest(BaseModel):
    video_id: str
    question: str