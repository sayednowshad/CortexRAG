import os
import re
import pickle

import networkx as nx


class GraphBuilder:

    GRAPH_PATH = (
        "data/graph/knowledge_graph.pkl"
    )

    STOP_WORDS = {
    word.lower()
    for word in {
         "Purpose",
            "Defines",
            "Cannot",
            "Understanding",
            "Limitations",
            "Examples",
            "Example",
            "Page",
            "Pages",
            "Copyright",
            "This",
            "These",
            "Those",
            "What",
            "When",
            "One",
            "Two",
            "Three",
            "Java",
    }
}

    _graph = nx.Graph()

    @classmethod
    def extract_entities(
        cls,
        text
    ):

        entities = re.findall(
            r'\b(?:[A-Z][A-Za-z0-9@._-]*)(?:\s+[A-Z][A-Za-z0-9@._-]*)*\b',
            text
        )

        entities = list(
            set(
                entity.strip()
                for entity in entities
                if (
                    len(entity.strip()) > 2
                    and entity.strip().lower()
                    not in cls.STOP_WORDS
                )
            )
        )

        return entities

    @classmethod
    def add_chunks(
        cls,
        chunks
    ):

        for chunk in chunks:

            entities = cls.extract_entities(
                chunk
            )

            for entity in entities:

                cls._graph.add_node(
                    entity
                )

            for i in range(
                len(entities)
            ):

                for j in range(
                    i + 1,
                    len(entities)
                ):

                    cls._graph.add_edge(
                        entities[i],
                        entities[j]
                    )

        cls.save_graph()

    @classmethod
    def save_graph(cls):

        os.makedirs(
            "data/graph",
            exist_ok=True
        )

        with open(
            cls.GRAPH_PATH,
            "wb"
        ) as file:

            pickle.dump(
                cls._graph,
                file
            )

    @classmethod
    def load_graph(cls):

        if os.path.exists(
            cls.GRAPH_PATH
        ):

            try:

                with open(
                    cls.GRAPH_PATH,
                    "rb"
                ) as file:

                    cls._graph = (
                        pickle.load(file)
                    )

            except Exception:

                cls._graph = nx.Graph()

        return cls._graph