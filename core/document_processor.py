from pathlib import Path
from typing import List
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from config import settings


class DocumentProcessor:
    def __init__(self):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=settings.CHUNK_SIZE,
            chunk_overlap=settings.CHUNK_OVERLAP
        )

    def process_pdf(self, path: str) -> List[Document]:
        loader = PyPDFLoader(path)
        docs = loader.load()

        for i, doc in enumerate(docs):
            doc.metadata["source"] = Path(path).name
            doc.metadata["page"] = i

        return self.splitter.split_documents(docs)


__all__ = ["DocumentProcessor"]
