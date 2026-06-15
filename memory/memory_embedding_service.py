from embeddings.embedding_model import (
    EmbeddingModel
)


class MemoryEmbeddingService:

    @staticmethod
    def generate_embedding(
        text
    ):

        model = (
            EmbeddingModel
            .get_model()
        )

        return (
            model.encode(text)
            .tolist()
        )