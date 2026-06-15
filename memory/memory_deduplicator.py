from memory.memory_retriever import (
    MemoryRetriever
)


class MemoryDeduplicator:

    THRESHOLD = 0.95

    @staticmethod
    def should_save(
        question: str
    ):

        memories = (
            MemoryRetriever
            .get_relevant_memories(
                question
            )
        )

        if memories:

            return False

        return True