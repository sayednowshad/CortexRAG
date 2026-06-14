from embeddings.embedding_model import (
    EmbeddingModel
)


class EmbeddingService:

    @staticmethod
    def generate_embeddings(chunks):

        model = EmbeddingModel.get_model()

        embeddings = model.encode(
            chunks,
            show_progress_bar=False
        )

        return embeddings.tolist()