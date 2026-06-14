from services.retrieval_service import (
    RetrievalService
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

        chunks = (
            RetrievalService.search(
                query=question,
                top_k=top_k
            )
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