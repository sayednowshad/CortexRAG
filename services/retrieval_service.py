from embeddings.embedding_model import (
    EmbeddingModel
)

from vectorstore.chroma_manager import (
    ChromaManager
)


class RetrievalService:

    SIMILARITY_THRESHOLD = 0.80

    @staticmethod
    def search(
        query: str,
        top_k: int = 5
    ):

        model = EmbeddingModel.get_model()

        query_embedding = model.encode(
            query
        ).tolist()

        results = ChromaManager.search(
            query_embedding=query_embedding,
            top_k=top_k
        )

        formatted_results = []

        documents = results["documents"][0]
        metadatas = results["metadatas"][0]
        distances = results["distances"][0]

        for document, metadata, distance in zip(
            documents,
            metadatas,
            distances
        ):

            # Guardrail: Ignore low-quality retrievals
            if distance <= RetrievalService.SIMILARITY_THRESHOLD:

                formatted_results.append(
                    {
                        "content": document,
                        "source": metadata["source"],
                        "chunk_index": metadata["chunk_index"],
                        "distance": round(distance, 4)
                    }
                )

        return formatted_results