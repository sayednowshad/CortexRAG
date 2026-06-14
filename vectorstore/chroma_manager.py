import chromadb


class ChromaManager:

    COLLECTION_NAME = "knowledge_base"

    _client = None
    _collection = None

    @classmethod
    def get_collection(cls):

        if cls._collection is None:

            cls._client = chromadb.PersistentClient(
                path="data/chroma"
            )

            cls._collection = (
                cls._client.get_or_create_collection(
                    name=cls.COLLECTION_NAME
                )
            )

        return cls._collection

    @classmethod
    def add_chunks(
        cls,
        chunks,
        embeddings,
        source_name
    ):

        collection = cls.get_collection()

        ids = []
        metadatas = []

        for i in range(len(chunks)):

            ids.append(
                f"{source_name}_{i}"
            )

            metadatas.append(
                {
                    "source": source_name,
                    "chunk_index": i,
                    "document_type": "pdf"
                }
            )

        collection.add(
            ids=ids,
            documents=chunks,
            embeddings=embeddings,
            metadatas=metadatas
        )

    @classmethod
    def count(cls):

        collection = cls.get_collection()

        return collection.count()

    @classmethod
    def get_stats(cls):

        collection = cls.get_collection()

        return {
            "collection_name": cls.COLLECTION_NAME,
            "total_vectors": collection.count()
        }

    @classmethod
    def search(
        cls,
        query_embedding,
        top_k=5
    ):

        collection = cls.get_collection()

        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
            include=[
                "documents",
                "metadatas",
                "distances"
            ]
        )

        return results