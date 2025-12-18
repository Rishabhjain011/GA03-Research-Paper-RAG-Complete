from langchain_huggingface import HuggingFaceEmbeddings
from config import settings


class EmbeddingManager:
    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings(
            model_name=settings.EMBEDDING_MODEL,
            encode_kwargs={"normalize_embeddings": True}
        )


__all__ = ["EmbeddingManager"]
