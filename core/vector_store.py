import os
from typing import List
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

from core.embeddings import EmbeddingManager

from config import settings

class VectorStoreManager:
    def __init__(self):
        self.embedding_manager = EmbeddingManager()
        self.store = None

    def build(self, documents: List[Document]):
        self.store = FAISS.from_documents(
            documents, self.embedding_manager.embeddings
        )

    def save(self):
        os.makedirs(settings.FAISS_INDEX_PATH, exist_ok=True)
        self.store.save_local(settings.FAISS_INDEX_PATH)

    def load(self):
        self.store = FAISS.load_local(
            settings.FAISS_INDEX_PATH,
            self.embedding_manager.embeddings,
            allow_dangerous_deserialization=True
        )

    def search(self, query: str):
        return self.store.similarity_search(query, k=settings.TOP_K_RESULTS)
