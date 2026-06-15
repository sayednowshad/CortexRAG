class SessionMemory:

    history = []

    @classmethod
    def add_message(
        cls,
        question,
        answer
    ):

        cls.history.append(
            {
                "question": question,
                "answer": answer
            }
        )

        cls.history = (
            cls.history[-5:]
        )

    @classmethod
    def get_history(cls):

        return cls.history