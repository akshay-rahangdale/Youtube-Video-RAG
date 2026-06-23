from youtube_rag.services.embedding_service import embedding_service
from youtube_rag.rag.vector_store import vector_store
    


class RetrievalService:
    
    @staticmethod
    def retrieve(video_id: str,question: str,k:int = 3):
         
        query_embedding= embedding_service.embed(question)
        
         
        collection = vector_store.get_collection(video_id)
        
         
        results = collection.query(
             query_embeddings=[query_embedding.tolist()],
             n_results=k
        )
         
        return results