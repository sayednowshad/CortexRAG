from services.hybrid_retrieval_service import (
    HybridRetrievalService
)

from services.rerank_service import (
    RerankService
)

# from services.graph_retrieval_service import (
#     GraphRetrievalService
# )

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

from services.evidence_extractor import (
    EvidenceExtractor
)

import time

from services.analytics_service import (
    AnalyticsService
)
class AnswerService:

    @staticmethod
    def answer_question(
        question: str,
        top_k: int = 5
    ):
        start_time = time.time()
        
        conversation_context = (
            ConversationManager
            .get_context()
        )
        
        import re
        
        pronouns = [
            "it",
            "its",
            "this",
            "that",
            "these",
            "those",
            "they",
            "them",
            "their"
        ]

        original_question = question

        current_topic = None
        
        question_words = re.findall(
            r"\b\w+\b",
            question.lower()
        )
        
        print(
            "Question Words:",
             question_words
        )
        
        if any(
            word in pronouns
            for word in question_words
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

        retrieval_start = time.time()
        
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
                    top_k=top_k
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
        retrieval_time = (
            time.time()
            - retrieval_start
        )

        print(
            f"\nRetrieved Chunks: {len(chunks)}"
        )
        
        # added timing for retrieval and reranking
        rerank_start = time.time()
        
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
            
        print(
            "\nRETRIEVED CONTENT:\n"
        )
        
        rerank_time = (
            time.time()
            - rerank_start
        )

        for chunk in chunks:

            print("=" * 50)

            print(
            chunk["content"][:500]
            )

        if not chunks:

            AnalyticsService.print_failure(
                "NO_CHUNKS"
            )

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

        sources = set()

        for chunk in chunks:

            sources.add(
                chunk["source"]
            )

        graph_context = "\n".join(
            related_concepts
        )

        # TEMPORARY DEBUG MODE
        # Disable EvidenceExtractor

        document_context = "\n\n".join(
            [
                chunk["content"]
                for chunk in chunks
            ]
        )

        print(
            "\nRAW DOCUMENT CONTEXT:\n"
        )

        print(
                document_context[:5000]
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
        
        llm_start = time.time()

        answer = (
            LLMClient.generate(
                prompt
            )
        )
        
        llm_time = (
            time.time()
            - llm_start
        )
        
        if "LLM Error" in answer:

            AnalyticsService.print_failure(
            "LLM_ERROR"
        )
        if (
            "I could not find"
            in answer
    ):
            AnalyticsService.print_failure(
            "NO_ANSWER"
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

        # ==========================
        # ANALYTICS
        # ==========================

        total_time = (
            time.time()
            - start_time
        )

        analytics = {

            "question":
                original_question,

            "queries":
                len(queries),

            "retrieved_chunks":
                len(all_chunks),

            "final_chunks":
                len(chunks),

            "memory_hits":
                len(memories),

            "sources_names":
                list(sources),

            "answer_length":
                len(answer),

            "retrieval_time":
                round(
                    retrieval_time,
                    3
                ),

            "rerank_time":
                round(
                    rerank_time,
                    3
                ),

            "llm_time":
                round(
                    llm_time,
                    3
                ),

            "total_time":
                round(
                    total_time,
                    3
                )
        }

        AnalyticsService.print_dashboard(
            analytics
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