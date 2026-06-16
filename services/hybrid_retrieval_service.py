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

        print("\n==============================")
        print("DENSE RESULTS")
        print("==============================")

        for result in dense_results:

            print(
                f"\nSOURCE: {result['source']}"
            )

            print(
                result["content"][:300]
            )

        print("\n==============================")
        print("BM25 RESULTS")
        print("==============================")

        for result in bm25_results:

            print(
                f"\nSOURCE: {result['source']}"
            )

            print(
                result["content"][:300]
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

        final_results = list(
            merged.values()
        )

        print("\n==============================")
        print("HYBRID MERGED RESULTS")
        print("==============================")

        print(
            f"Dense Results : {len(dense_results)}"
        )

        print(
            f"BM25 Results  : {len(bm25_results)}"
        )
        
        print(
            f"Merged Results: {len(final_results)}"
        )

        return final_results