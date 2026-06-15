from memory.session_memory import (
    SessionMemory
)
from memory.topic_tracker import (
    TopicTracker
)

class ConversationManager:

    @staticmethod
    def get_context():

        history = (
            SessionMemory
            .get_history()
        )

        if not history:

            return ""

        context = []

        for item in history:

            context.append(
                f"User: {item['question']}"
            )

            context.append(
                f"Assistant: {item['answer']}"
            )

        return "\n".join(
            context
        )
        
    @staticmethod
    def get_current_topic():

        return (
            TopicTracker
            .get_topic()
        )

    @staticmethod
    def get_last_topic():

        history = (
            SessionMemory
            .get_history()
        )

        if not history:

            return ""

        return history[-1][
            "question"
        ]