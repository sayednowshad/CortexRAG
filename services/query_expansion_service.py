from services.graph_retrieval_service import (
    GraphRetrievalService
)


class QueryExpansionService:

    STOP_CONCEPTS = {
        "What",
        "How",
        "Can",
        "This",
        "That",
        "Control",
        "Purpose",
        "Understanding",
        "Defines",
        "Examples",
        "Example",
        "Limitations",
        "Java",
        "Spring"
    }

    @staticmethod
    def score_concept(
        question: str,
        concept: str
    ):

        score = 0

        question_words = set(
            question.lower().split()
        )

        concept_words = set(
            concept.lower().split()
        )

        overlap = len(
            question_words.intersection(
                concept_words
            )
        )

        score += overlap * 10

        if "injection" in concept.lower():
            score += 8

        if "ioc" in concept.lower():
            score += 8

        if "autowired" in concept.lower():
            score += 8

        if len(
            concept.split()
        ) >= 2:
            score += 2

        return score

    @staticmethod
    def get_best_concepts(
        question: str
    ):

        concepts = (
            GraphRetrievalService
            .get_related_concepts(
                question
            )
        )

        scored_concepts = []

        for concept in concepts:

            concept = concept.strip()

            if (
                concept in
                QueryExpansionService
                .STOP_CONCEPTS
            ):
                continue

            if len(
                concept.split()
            ) < 2:
                continue

            score = (
                QueryExpansionService
                .score_concept(
                    question,
                    concept
                )
            )

            scored_concepts.append(
                (
                    concept,
                    score
                )
            )

        scored_concepts.sort(
            key=lambda x: x[1],
            reverse=True
        )

        best_concepts = [
            concept
            for concept, score
            in scored_concepts[:5]
        ]

        best_concepts = list(
            dict.fromkeys(
                best_concepts
            )
        )

        return best_concepts

    @staticmethod
    def expand_query(
        question: str
    ):

        best_concepts = (
            QueryExpansionService
            .get_best_concepts(
                question
            )
        )

        expanded_query = (
            question
            + "\n"
            + "\n".join(
                best_concepts
            )
        )

        print(
            "\nExpanded Query:\n"
        )

        print(
            expanded_query
        )

        print(
            "\nTop Graph Concepts:\n"
        )

        for concept in best_concepts:

            print(
                concept
            )

        return expanded_query