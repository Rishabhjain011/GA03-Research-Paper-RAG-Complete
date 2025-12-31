from core.vector_store import VectorStoreManager
from core.rag_chain import RAGChain
from config.settings import settings

vs = VectorStoreManager()
vs.load()
rag = RAGChain()

while True:
    q = input("Ask: ")
    if q == "exit":
        break
    docs = vs.search(q, settings.TOP_K_RESULTS)
    print(rag.generate(docs, q))
