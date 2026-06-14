from services.graph_retrieval_service import (
    GraphRetrievalService
)

results = (
    GraphRetrievalService
    .get_related_concepts(
        "Java Collections"
    )
)

print(
    "Graph Concepts:"
)

for concept in results:

    print(concept)