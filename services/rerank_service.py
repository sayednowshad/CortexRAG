from sentence_transformers import (
    CrossEncoder
)


class RerankService:

    _model = None

    @classmethod
    def get_model(cls):

        if cls._model is None:

            cls._model = CrossEncoder(
                "cross-encoder/ms-marco-MiniLM-L-6-v2"
            )

        return cls._model

    @classmethod
    def rerank(
        cls,
        query,
        chunks,
        top_k=3
    ):

        if not chunks:

            return []

        model = cls.get_model()

        pairs = []

        for chunk in chunks:

            pairs.append(
                (
                    query,
                    chunk["content"]
                )
            )

        scores = model.predict(
            pairs
        )

        scored_results = []

        for chunk, score in zip(
            chunks,
            scores
        ):

            chunk["rerank_score"] = (
                float(score)
            )

            scored_results.append(
                chunk
            )

        scored_results.sort(
            key=lambda x:
            x["rerank_score"],
            reverse=True
        )

        return scored_results[:top_k]