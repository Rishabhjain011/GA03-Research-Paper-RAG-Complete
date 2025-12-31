from core.document_processor import DocumentProcessor
from core.vector_store import VectorStoreManager
from core.metadata_extractor import MetadataExtractor
from core.citation_extractor import CitationExtractor

PDF_PATH = "data/papers/project.pdf"

def ingest():
    docs = DocumentProcessor().process_pdf(PDF_PATH)
    VectorStoreManager().create(docs)

    full_text = " ".join(d.page_content for d in docs)
    print(MetadataExtractor().extract(full_text))
    print(CitationExtractor().extract(full_text))

if __name__ == "__main__":
    ingest()
