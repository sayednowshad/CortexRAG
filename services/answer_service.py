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

from memory.session_memory import (
    SessionMemory
)

from memory.conversation_manager import (
    ConversationManager
)

from memory.topic_tracker import (
    TopicTracker
)

class AnswerService:

    @staticmethod
    def answer_question(
        question: str,
        top_k: int = 5
    ):

        conversation_context = (
            ConversationManager
            .get_context()
        )

        pronouns = [
            "it",
            "this",
            "that",
            "these",
            "those"
        ]

        original_question = question

        if any(
            word in question.lower()
            for word in pronouns
        ):

           current_topic = (
                ConversationManager
                .get_current_topic()
            )

           if current_topic:

                question = (
                    f"{question} "
                    f"regarding "
                    f"{current_topic}"
            )

                print(
                    "Enhanced Question:",
                    question
                )

        enhanced_query = f"""
Conversation History:

{conversation_context}

Current Question:

{question}
"""

        chunks = HybridRetrievalService.search(
            query=enhanced_query,
            top_k=10
        )

        chunks = RerankService.rerank(
            query=enhanced_query,
            chunks=chunks,
            top_k=3
        )

        if not chunks:

            return {
                "question": original_question,
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
CONVERSATION HISTORY:

{conversation_context}

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

Use conversation history
when relevant.

Use memory if it is relevant.

If the answer is not present
in the context, say so.
"""
        print(
            "\nDOCUMENT CONTEXT:\n"
        )

        print(
            document_context[:1500]
        )

        answer = (
            LLMClient.generate(
                prompt
            )
        )
        
        TopicTracker.set_topic(
            original_question
        )

        SessionMemory.add_message(
            original_question,
            answer
        )

        MemoryManager.save_conversation(
            question=original_question,
            answer=answer
        )

        return {
            "question":
                original_question,
            "answer":
                answer,
            "related_concepts":
                related_concepts,
            "memory_hits":
                len(memories),
            "conversation_turns":
                len(
                    SessionMemory
                    .get_history()
                ),
            "sources":
                list(sources)
        }