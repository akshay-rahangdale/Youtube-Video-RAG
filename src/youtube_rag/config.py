from dotenv import load_dotenv

import os

load_dotenv()


class Settings:
    GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")
    
settings=Settings()

if not settings.GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is missing")

