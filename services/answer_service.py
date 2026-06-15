from services.hybrid_retrieval_service import (
    HybridRetrievalService
)

from services.rerank_service import (
    RerankService
)

from services.graph_retrieval_service import (
    GraphRetrievalService
)

from llm.llm_client import (
    LLMClient
)

from memory.memory_manager import (
    MemoryManager
)

from memory.memory_retriever import (
    MemoryRetriever
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

        related_concepts = (
            GraphRetrievalService
            .get_related_concepts(
                question
            )
        )
        print(
            "Related Concepts:",
            related_concepts
        )

        memories = (
            MemoryRetriever
            .get_relevant_memories(
                question
            )
        )

        context_parts = []

        sources = set()

        for chunk in chunks:

            context_parts.append(
                chunk["content"]
            )

            sources.add(
                chunk["source"]
            )

        graph_context = "\n".join(
            related_concepts
        )

        document_context = "\n\n".join(
            context_parts
        )

        memory_context = "\n\n".join(
            [
                (
                    f"Q: {memory['question']}\n"
                    f"A: {memory['answer']}"
                )
                for memory in memories
            ]
        )

        context = f"""
MEMORY:

{memory_context}

RELATED CONCEPTS:

{graph_context}

DOCUMENT CONTEXT:

{document_context}
"""

        prompt = f"""
Answer the question using ONLY
the context below.

CONTEXT:

{context}

QUESTION:

{question}

Use memory if it is relevant.

If the answer is not present
in the context, say so.
"""

        answer = (
            LLMClient.generate(
                prompt
            )
        )

        MemoryManager.save_conversation(
            question=question,
            answer=answer
        )

        return {
            "question": question,
            "answer": answer,
            "related_concepts":
                related_concepts,
            "memory_hits":
                len(memories),
            "sources":
                list(sources)
        }