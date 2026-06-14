# test_graph_build.py

from graph.graph_builder import (
    GraphBuilder
)

chunks = [
    "Spring Boot uses Dependency Injection through IoC Container",
    "Spring Boot supports Auto Configuration",
    "Dependency Injection reduces tight coupling"
]

GraphBuilder.add_chunks(
    chunks
)

print("DONE")