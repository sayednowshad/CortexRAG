from memory.memory_store import (
    MemoryStore
)

from memory.memory_embedding_service import (
    MemoryEmbeddingService
)


class MemoryManager:

    @staticmethod
    def save_conversation(
        question,
        answer
    ):

        embedding = (
            MemoryEmbeddingService
            .generate_embedding(
                question
            )
        )

        memory = {
            "question": question,
            "answer": answer,
            "embedding": embedding
        }

        MemoryStore.save_memory(
            memory
        )