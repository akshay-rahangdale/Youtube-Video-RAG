from langchain_text_splitters import RecursiveCharacterTextSplitter

class TranscriptChunker:
    
    @staticmethod
    def chunk(text: str) -> list[str]:
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        
        return splitter.split_text(text)