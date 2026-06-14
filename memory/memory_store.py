import json
import os


class MemoryStore:

    MEMORY_FILE = (
        "data/memory/memories.json"
    )

    @classmethod
    def load_memories(cls):

        os.makedirs(
            "data/memory",
            exist_ok=True
        )

        if not os.path.exists(
            cls.MEMORY_FILE
        ):

            return []

        try:

            with open(
                cls.MEMORY_FILE,
                "r",
                encoding="utf-8"
            ) as file:

                content = (
                    file.read()
                    .strip()
                )

                if not content:

                    return []

                return json.loads(
                    content
                )

        except Exception:

            return []

    @classmethod
    def save_memory(
        cls,
        memory
    ):

        memories = (
            cls.load_memories()
        )

        memories.append(
            memory
        )

        os.makedirs(
            "data/memory",
            exist_ok=True
        )

        with open(
            cls.MEMORY_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                memories,
                file,
                indent=4,
                ensure_ascii=False
            )