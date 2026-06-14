from services.hybrid_retrieval_service import (
    HybridRetrievalService
)
from services.rerank_service import (
    RerankService
)
from llm.llm_client import (
    LLMClient
)


class AnswerService:

    @staticmethod
    def answer_question(
        question: str,
        top_k: int = 5
    ):

        chunks = HybridRetrievalService.search(
            query=question,
            top_k=10
        )

        chunks = RerankService.rerank(
            query=question,
            chunks=chunks,
            top_k=3
        )
        
        if not chunks:

            return {
                "question": question,
                "answer":
                (
                    "I could not find "
                    "relevant information "
                    "in the knowledge base."
                ),
                "sources": []
            }

        context_parts = []

        sources = set()

        for chunk in chunks:

            context_parts.append(
                chunk["content"]
            )

            sources.add(
                chunk["source"]
            )

        context = "\n\n".join(
            context_parts
        )

        prompt = f"""
Answer the question using ONLY
the context below.

CONTEXT:

{context}

QUESTION:

{question}
"""

        answer = (
            LLMClient.generate(
                prompt
            )
        )

        return {
            "question": question,
            "answer": answer,
            "sources": list(
                sources
            )
        }