"""
Ingestion Script
================
GA03 – Part I & Part II

This script:
1. Loads a research paper PDF
2. Splits it into semantic chunks
3. Builds a FAISS vector index using HuggingFace embeddings
4. Saves the vector store locally

Run:
uv run python ingest.py
"""

from pathlib import Path

from core.document_processor import DocumentProcessor
from core.vector_store import VectorStoreManager
from core.schema import ResearchPaper, PaperSection


def ingest_paper(pdf_path: Path):
    """
    End-to-end ingestion pipeline for a single research paper
    """

    # -----------------------------
    # Step 1: Process PDF
    # -----------------------------
    processor = DocumentProcessor()
    documents = processor.process_pdf(str(pdf_path))

    # -----------------------------
    # Step 2: Create ResearchPaper schema (Part I)
    # -----------------------------
    paper = ResearchPaper(
        paper_id=pdf_path.stem,
        title=None,
        authors=None,
        abstract=None,
        year=None
    )

    for doc in documents:
        section = PaperSection(
            section_name=f"Page_{doc.metadata.get('page', 0)}",
            content=doc.page_content
        )
        paper.sections.append(section)

    paper.full_text = "\n".join(section.content for section in paper.sections)

    # -----------------------------
    # Step 3: Build FAISS Vector Store (Part II)
    # -----------------------------
    vector_store = VectorStoreManager()
    vector_store.build(documents)
    vector_store.save()

    print("✅ Ingestion completed successfully")
    print(f"📄 Paper ID: {paper.paper_id}")
    print(f"📦 Total Chunks Indexed: {len(documents)}")


if __name__ == "__main__":
    # -----------------------------
    # Define PDF path safely
    # -----------------------------
    BASE_DIR = Path(__file__).resolve().parent
    PDF_PATH = BASE_DIR / "data" / "papers" / "project.pdf"

    if not PDF_PATH.exists():
        raise FileNotFoundError(f"❌ PDF not found at {PDF_PATH}")

    ingest_paper(PDF_PATH)
