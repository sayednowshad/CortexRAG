from graph.graph_builder import (
    GraphBuilder
)


class GraphTraversal:

    @staticmethod
    def get_related_nodes(
        entity,
        limit=10
    ):

        graph = (
            GraphBuilder.load_graph()
        )

        if entity not in graph:

            return []

        neighbors = list(
            graph.neighbors(entity)
        )

        return neighbors[:limit]