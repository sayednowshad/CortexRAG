from sentence_transformers import (
    util
)

from memory.memory_store import (
    MemoryStore
)

from memory.memory_embedding_service import (
    MemoryEmbeddingService
)


class MemoryRetriever:

    @staticmethod
    def get_relevant_memories(
        query,
        top_k=3
    ):

        memories = (
            MemoryStore.load_memories()
        )

        if not memories:

            return []

        query_embedding = (
            MemoryEmbeddingService
            .generate_embedding(
                query
            )
        )

        scored_memories = []

        for memory in memories:

            similarity = (
                util.cos_sim(
                    query_embedding,
                    memory["embedding"]
                )
                .item()
            )
            
            print(
                    f"Memory Similarity: "
                    f"{similarity:.4f} | "
                    f"{memory['question']}"
            )
        if similarity > 0.75:
            
            scored_memories.append(
                (
                    similarity,
                    memory
                )
            )

        scored_memories.sort(
            reverse=True,
            key=lambda x: x[0]
        )

        return [
            memory
            for _, memory
            in scored_memories[:top_k]
        ] 