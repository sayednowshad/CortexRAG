from memory.memory_store import (
    MemoryStore
)


class MemoryManager:

    @staticmethod
    def save_conversation(
        question,
        answer
    ):

        memory = {
            "question": question,
            "answer": answer
        }

        MemoryStore.save_memory(
            memory
        )