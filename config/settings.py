import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Settings:
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY")
    HF_API_KEY: str = os.getenv("HF_API_KEY")

    LLM_MODEL: str = os.getenv("LLM_MODEL", "llama3-70b-8192")
    LLM_TEMPERATURE: float = float(os.getenv("LLM_TEMPERATURE", 0.1))

    EMBEDDING_MODEL: str = os.getenv(
        "EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2"
    )

    CHUNK_SIZE: int = int(os.getenv("CHUNK_SIZE", 1000))
    CHUNK_OVERLAP: int = int(os.getenv("CHUNK_OVERLAP", 200))

    FAISS_INDEX_PATH: str = os.getenv("FAISS_INDEX_PATH", "data/vectorstore/faiss")
    TOP_K_RESULTS: int = int(os.getenv("TOP_K_RESULTS", 5))

    def validate(self):
        if not self.GROQ_API_KEY:
            raise ValueError("Missing GROQ_API_KEY")
        if not self.HF_API_KEY:
            raise ValueError("Missing HF_API_KEY")

settings = Settings()
settings.validate()
