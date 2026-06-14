from graph.graph_builder import GraphBuilder

graph = GraphBuilder.load_graph()

print("Nodes:", len(graph.nodes))
print("Edges:", len(graph.edges))

print(list(graph.nodes)[:20])