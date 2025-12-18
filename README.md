# GA03: Research Paper Management & Analysis Intelligence System

## 📌 Overview
This project implements a Research Paper Intelligence System that helps users
ingest academic research papers, generate semantic embeddings, and perform
semantic search using Retrieval-Augmented Generation (RAG) principles.

The system is designed to handle long-form academic PDFs and enable efficient
discovery of relevant content without reading the entire paper.

---

## 🎯 Objectives
- Ingest research paper PDFs
- Split documents into semantic chunks
- Generate embeddings using HuggingFace models
- Index embeddings using FAISS
- Perform semantic search over research papers

---

## 🧱 Project Architecture
PDF
↓
Document Processing
↓
Chunking
↓
HuggingFace Embeddings
↓
FAISS Vector Store
↓
Semantic Search


---

## 🛠 Tech Stack
- Python
- LangChain
- HuggingFace Sentence Transformers
- FAISS
- PyMuPDF
- uv (virtual environment & dependency management)

---

## 📂 Project Structure

GA03-Research-Paper-RAG/
│
├── config/
│ └── settings.py
│
├── core/
│ ├── document_processor.py
│ ├── embeddings.py
│ ├── vector_store.py
│ └── schema.py
│
├── data/
│ ├── papers/
│ └── vectorstore/
│
├── ingest.py
├── main.py
├── requirements.txt
└── README.md


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone <https://github.com/Rishabhjain011>
cd GA03-Research-Paper-RAG

