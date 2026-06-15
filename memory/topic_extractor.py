import re


class TopicExtractor:

    @staticmethod
    def extract(
        question
    ):

        question = (
            question.strip()
        )

        patterns = [

            r"What is (.+?)\??$",

            r"Explain (.+?)\??$",

            r"Tell me about (.+?)\??$",

            r"Describe (.+?)\??$"
        ]

        for pattern in patterns:

            match = re.search(
                pattern,
                question,
                re.IGNORECASE
            )

            if match:

                return (
                    match
                    .group(1)
                    .strip()
                )

        return None