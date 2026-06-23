from langchain_google_genai import ChatGoogleGenerativeAI

from youtube_rag.config import settings


class LLMService:

    def __init__(self):
        self.model = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            google_api_key=settings.GEMINI_API_KEY,
            temperature=0
        )

    def generate(self, context: str, question: str) -> str:

        prompt = f"""
You are a helpful assistant.

Answer ONLY using the provided context.

If the answer is not present in the context, say:
"I could not find that information in the video."

CONTEXT:
{context}

QUESTION:
{question}
"""

        response = self.model.invoke(prompt)

        return response.content


llm_service = LLMService()