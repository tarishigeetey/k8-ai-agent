import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY")
    GROQ_FALLBACK_API_KEY: str = os.getenv("GROQ_FALLBACK_API_KEY")
    GORQ_MODEL = "llama-3.3-70b-versatile"

    QUADRA_API_KEY: str = os.getenv("QUADRA_API_KEY")
    QUDRANT_CLUSTER_ENDPOINT: str = os.getenv("QUDRANT_CLUSTER_ENDPOINT")
    QUDRANT_COLLECTION = "k8_enterprise_rag"

    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY")


settings = Settings()
