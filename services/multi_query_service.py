from services.query_expansion_service import (
    QueryExpansionService
)


class MultiQueryService:

    @staticmethod
    def generate_queries(
        question: str
    ):

        queries = [question]

        concepts = (
            QueryExpansionService
            .get_best_concepts(
                question
            )
        )

        for concept in concepts:

            if concept.strip():

                queries.append(
                    concept
                )

        queries = list(
            dict.fromkeys(
                queries
            )
        )

        print(
            "\nGenerated Queries:\n"
        )

        for query in queries:

            print(
                f"- {query}"
            )

        return queries