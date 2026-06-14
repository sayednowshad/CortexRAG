from services.retrieval_service import (
    RetrievalService
)

from vectorstore.bm25_manager import (
    BM25Manager
)


class HybridRetrievalService:

    @staticmethod
    def search(
        query: str,
        top_k: int = 5
    ):

        dense_results = (
            RetrievalService.search(
                query=query,
                top_k=top_k
            )
        )

        bm25_results = (
            BM25Manager.search(
                query=query,
                top_k=top_k
            )
        )

        merged = {}

        for result in dense_results:

            key = (
                result["source"],
                result["chunk_index"]
            )

            merged[key] = result

        for result in bm25_results:

            key = (
                result["source"],
                result["chunk_index"]
            )

            if key not in merged:

                merged[key] = result

        return list(
            merged.values()
        )[:top_k]