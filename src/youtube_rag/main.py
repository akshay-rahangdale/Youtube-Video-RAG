from fastapi import FastAPI

from youtube_rag.api.routes import router

app=FastAPI(
    title="Youtube RAG"
)

app.include_router(router)

@app.get("/")
def health():
    return {"status":"Good and Running"}

