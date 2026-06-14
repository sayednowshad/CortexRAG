from graph.graph_builder import (
    GraphBuilder
)

from graph.graph_traversal import (
    GraphTraversal
)


class GraphRetrievalService:

    @staticmethod
    def get_related_concepts(
        query: str,
        limit: int = 10
    ):

        graph = GraphBuilder.load_graph()

        related = set()

        for node in graph.nodes:

            if query.lower() in node.lower():

                related.add(node)

                neighbors = (
                    GraphTraversal
                    .get_related_nodes(
                        node,
                        limit=limit
                    )
                )

                related.update(
                    neighbors
                )

        return list(related)