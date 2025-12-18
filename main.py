"""
Semantic Search Demo
====================
GA03 – Part II

This script:
1. Loads the FAISS vector store
2. Accepts a user query
3. Retrieves top-k relevant chunks

Run:
uv run python main.py
"""

from core.vector_store import VectorStoreManager


def main():
    store = VectorStoreManager()
    store.load()

    print("\n🔍 Research Paper Semantic Search")
    print("Type 'exit' to quit\n")

    while True:
        query = input("Ask a question: ")

        if query.lower() == "exit":
            break

        results = store.search(query)

        print("\n📄 Top Results:\n")
        for i, doc in enumerate(results, start=1):
            print(f"Result {i}:")
            print(doc.page_content[:500])
            print("-" * 80)


if __name__ == "__main__":
    main()
