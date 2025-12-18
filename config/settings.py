import os
from dataclasses import dataclass
from typing import Optional
from pathlib import Path

from dotenv import load_dotenv


# Load .env from project root
ENV_PATH = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=ENV_PATH)


def get_int(name: str, default: int) -> int:
    try:
        return int(os.getenv(name, default))
    except ValueError:
        return default


def get_float(name: str, default: float) -> float:
    try:
        return float(os.getenv(name, default))
    except ValueError:
        return default


@dataclass
class Settings:
    """
    Centralized application configuration.
    Loaded from environment variables.
    """

    # API Keys
    GROQ_API_KEY: Optional[str] = os.getenv("GROQ_API_KEY")
    HF_API_KEY: Optional[str] = os.getenv("HF_API_KEY")

    # LLM Configuration
    LLM_MODEL: str = os.getenv("LLM_MODEL", "llama3-70b-8192")
    LLM_TEMPERATURE: float = get_float("LLM_TEMPERATURE", 0.1)

    # Embedding Configuration (NO TORCH)
    EMBEDDING_MODEL: str = os.getenv(
        "EMBEDDING_MODEL",
        "sentence-transformers/all-MiniLM-L6-v2"
    )

    # Chunking
    CHUNK_SIZE: int = get_int("CHUNK_SIZE", 1000)
    CHUNK_OVERLAP: int = get_int("CHUNK_OVERLAP", 200)

    # Vector Store
    FAISS_INDEX_PATH: str = os.getenv(
        "FAISS_INDEX_PATH",
        "data/vectorstore/faiss"
    )

    # Retrieval
    TOP_K_RESULTS: int = get_int("TOP_K_RESULTS", 1)

    def validate(self) -> None:
        """Validate mandatory environment variables."""
        if not self.GROQ_API_KEY:
            raise ValueError("❌ GROQ_API_KEY is missing in .env")
        if not self.HF_API_KEY:
            raise ValueError("❌ HF_API_KEY is missing in .env")


# Singleton settings object
settings = Settings()
settings.validate()
