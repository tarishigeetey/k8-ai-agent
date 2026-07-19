from openai import OpenAI
from langchain_openai import ChatOpenAI

from app.config import settings

GROQ_BASE_URL = "https://api.groq.com/openai/v1"

# NOTE: Portkey isn't set up on this account (no 'rag'/'brag' provider slugs, and inline
# config is rejected on this plan). Bypassing the gateway — calling Groq's own
# OpenAI-compatible endpoint directly with GROQ_API_KEY. No fallback/retry/cache/dashboard
# logging until Portkey is configured; swap base_url/api_key back to Portkey's then.
portkey_client = OpenAI(api_key=settings.GROQ_API_KEY, base_url=GROQ_BASE_URL)


def get_langchain_llm(feature: str = "rag") -> ChatOpenAI:
    """
    Returns a ChatOpenAI pointed at Groq's OpenAI-compatible endpoint.

    Why ChatOpenAI and not ChatGroq:
      `langchain-groq` isn't installed. ChatOpenAI supports a `base_url` param, and
      Groq's API speaks the OpenAI format, so pointing ChatOpenAI at Groq's address
      works as a drop-in without adding a new dependency.
    """
    return ChatOpenAI(
        api_key=settings.GROQ_API_KEY,
        base_url=GROQ_BASE_URL,
        model=settings.GROQ_MODEL,
        temperature=0,
    )


def extract_cache_status(response) -> str:
    """
    Placeholder for when Portkey is reintroduced — Groq direct calls have no cache layer.
    """
    return "MISS"
