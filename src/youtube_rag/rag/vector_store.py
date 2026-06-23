import chromadb

class VectorStore:
    
    def __init__(self):
        self.client = chromadb.PersistentClient(
            path="data/chroma"
        )
    
    def get_collection(self,video_id:str):
        return self.client.get_or_create_collection(
            name=f"video_{video_id}"
        )
        
    def add_chunks(
        self,
        video_id: str,
        chunks: list[str],
        embeddings: list[list[float]]
    ):
    
        collection=self.get_collection(video_id)
        
        collection.add(
            ids=[
                f"{video_id}_{i}"
                for i in range(len(chunks))
            ],
            documents=chunks,
            embeddings=embeddings,
            metadatas=[
                {
                    "video_id":video_id,
                    "chunk_index":i
                }
                for i in range(len(chunks))
            ]
            
        )
        
vector_store = VectorStore()