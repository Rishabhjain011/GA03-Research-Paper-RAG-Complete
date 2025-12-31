from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.documents import Document

from config.settings import settings


class RAGChain:
    """
    Handles Retrieval-Augmented Generation using Groq LLM.
    """

    def __init__(self):
        self.llm = ChatGroq(
            groq_api_key=settings.GROQ_API_KEY,
            model=settings.LLM_MODEL,
            temperature=settings.LLM_TEMPERATURE
        )

        self.prompt = PromptTemplate(
            input_variables=["context", "question"],
            template="""
You are an AI research assistant.
Answer ONLY using the context below.
If the answer is not present, say so clearly.

Context:
{context}

Question:
{question}

Answer:
"""
        )

    def generate(self, docs: list[Document], question: str) -> str:
        """
        Generate grounded answer using retrieved chunks.
        """
        context = "\n\n".join(doc.page_content for doc in docs)

        prompt = self.prompt.format(
            context=context,
            question=question
        )

        response = self.llm.invoke(prompt)
        return response.content
