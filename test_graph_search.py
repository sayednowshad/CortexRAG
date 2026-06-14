from services.graph_retrieval_service import (
    GraphRetrievalService
)

results = (
    GraphRetrievalService
    .get_related_concepts(
        "Java"
    )
)

print(results)