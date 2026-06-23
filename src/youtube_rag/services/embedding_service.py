from sentence_transformers import SentenceTransformer

class EmbeddingService:
    
    def __init__(self):
        print("Loading BGE model...")
        self.model=SentenceTransformer(
            "BAAI/bge-small-en-v1.5"
        )
        
    def embed(self,text):
        return self.model.encode(text)
    
embedding_service = EmbeddingService()