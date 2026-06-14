from memory.memory_store import (
    MemoryStore
)


class MemoryRetriever:

    @staticmethod
    def get_relevant_memories(
        query
    ):

        memories = (
            MemoryStore.load_memories()
        )

        query = query.lower()

        results = []

        for memory in memories:

            question = (
                memory["question"]
                .lower()
            )

            if any(
                word in question
                for word in query.split()
            ):

                results.append(
                    memory
                )

        return results[-5:]