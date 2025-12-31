import os
from langchain_community.vectorstores import FAISS
from core.embeddings import EmbeddingManager
from config.settings import settings


class VectorStoreManager:
    def __init__(self):
        self.embedder = EmbeddingManager().get_embeddings()
        self.index_path = settings.FAISS_INDEX_PATH
        self.vectorstore = None

    def create(self, documents):
        """
        Create and save FAISS index.
        """
        self.vectorstore = FAISS.from_documents(documents, self.embedder)
        self.vectorstore.save_local(self.index_path)

    def load(self):
        """
        Load FAISS index from disk.
        """
        if not os.path.exists(self.index_path):
            raise FileNotFoundError(
                "FAISS index not found. Run ingest.py first."
            )

        self.vectorstore = FAISS.load_local(
            self.index_path,
            self.embedder,
            allow_dangerous_deserialization=True
        )

    def search(self, query: str, k: int):
        if not self.vectorstore:
            raise RuntimeError("Vector store not loaded")

        return self.vectorstore.similarity_search(query, k=k)
