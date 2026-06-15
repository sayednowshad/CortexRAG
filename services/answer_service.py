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

from memory.topic_extractor import (
    TopicExtractor
)

from services.query_expansion_service import (
    QueryExpansionService
)

from services.multi_query_service import (
    MultiQueryService
)

from memory.memory_deduplicator import (
    MemoryDeduplicator
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

        current_topic = None

        if any(
            word in question.lower()
            for word in pronouns
        ):

           current_topic = (
                ConversationManager
                .get_current_topic()
            )

           if not current_topic:

                                    return {
            "question": original_question,
            "answer":
            (
                "I need more context. "
                "What does 'it' refer to?"
            ),
            "sources": []
        }

        question = (
        f"{question} "
        f"regarding "
        f"{current_topic}"
        )

        print(
        "Enhanced Question:",
        question
        )
        
        # wait....
        queries = (
            MultiQueryService
            .generate_queries(
                question
            )
        )

        all_chunks = []

        for query in queries:

            enhanced_query = f"""
Conversation History:

{conversation_context}

Current Question:

{query}
"""

            results = (
                HybridRetrievalService
                .search(
                    query=enhanced_query,
                    top_k=5
                )
            )

            all_chunks.extend(
                results
            )

        unique_chunks = {}

        for chunk in all_chunks:

            unique_chunks[
                chunk["content"]
            ] = chunk

        chunks = list(
            unique_chunks.values()
        )

        print(
            f"\nRetrieved Chunks: {len(chunks)}"
        )

        chunks = (
            RerankService
            .rerank(
                query=question,
                chunks=chunks,
                top_k=3
            )
        )
        
        print(
            "\nFINAL CHUNKS AFTER RERANK:\n"
        )

        for chunk in chunks:

            print(
                chunk["source"]
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
            QueryExpansionService
            .get_best_concepts(
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

        print("\nPROMPT:\n")
        print(prompt[:4000])

        answer = (
            LLMClient.generate(
                prompt
            )
        )

        topic = (
            TopicExtractor
            .extract(
                original_question
            )
        )

        if topic:

            print(
                "Current Topic:",
                topic
            )

            TopicTracker.set_topic(
                topic
            )

        SessionMemory.add_message(
            original_question,
            answer
        )

        if (
    "I could not find the answer"
    not in answer
    ):

         if (
            MemoryDeduplicator
            .should_save(
            original_question
        )
    ):

             MemoryManager.save_conversation(
            question=original_question,
            answer=answer
        )

        else:
             print(
            "Duplicate memory skipped."
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