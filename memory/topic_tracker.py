class TopicTracker:

    current_topic = ""

    @classmethod
    def set_topic(
        cls,
        topic
    ):

        cls.current_topic = topic

    @classmethod
    def get_topic(cls):

        return cls.current_topic