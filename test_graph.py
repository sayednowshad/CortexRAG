from graph.graph_builder import (
    GraphBuilder
)

graph = (
    GraphBuilder.load_graph()
)

print(
    "Nodes:",
    len(graph.nodes)
)

print(
    "Edges:",
    len(graph.edges)
)

print("\nFirst 30 Nodes:\n")

for node in list(graph.nodes)[:30]:

    print(node)