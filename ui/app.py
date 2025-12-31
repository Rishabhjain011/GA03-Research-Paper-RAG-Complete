import sys
import os

# -------------------------------------------------
# Fix Python path so Streamlit can find core modules
# -------------------------------------------------
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# -------------------------------------------------
# Imports
# -------------------------------------------------
import streamlit as st

from core.vector_store import VectorStoreManager
from core.rag_chain import RAGChain
from config.settings import settings

# -------------------------------------------------
# Streamlit Page Config
# -------------------------------------------------
st.set_page_config(
    page_title="Research Paper Intelligence System",
    page_icon="📄",
    layout="wide"
)

# -------------------------------------------------
# UI Header
# -------------------------------------------------
st.title("📄 Research Paper Management & Analysis Intelligence System")
st.write(
    "Ask natural language questions and get AI-powered answers "
    "directly from research papers using RAG."
)

# -------------------------------------------------
# Load Vector Store & RAG Chain (cached)
# -------------------------------------------------
@st.cache_resource
def load_system():
    vector_store = VectorStoreManager()
    vector_store.load()

    rag_chain = RAGChain()
    return vector_store, rag_chain


vector_store, rag_chain = load_system()

# -------------------------------------------------
# User Input
# -------------------------------------------------
query = st.text_input(
    "🔍 Enter your question about the research paper:",
    placeholder="e.g. What problem does the paper address?"
)

# -------------------------------------------------
# Run Query
# -------------------------------------------------
if query:
    with st.spinner("Searching and generating answer..."):
        docs = vector_store.search(query, settings.TOP_K_RESULTS)
        answer = rag_chain.generate(docs, query)

    # -------------------------------------------------
    # Display Answer
    # -------------------------------------------------
    st.subheader("🧠 Answer")
    st.write(answer)

    # -------------------------------------------------
    # Show Retrieved Context
    # -------------------------------------------------
    with st.expander("📚 Retrieved Context (Source Chunks)"):
        for i, doc in enumerate(docs, start=1):
            st.markdown(
                f"**Chunk {i} | Page {doc.metadata.get('page', 'N/A')}**"
            )
            st.write(doc.page_content)
            st.markdown("---")
