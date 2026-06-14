from rank_bm25 import BM25Okapi


class BM25Manager:

    bm25 = None

    documents = []

    metadata = []

    @classmethod
    def build_index(
        cls,
        chunks,
        source_name
    ):

        tokenized_docs = []

        for index, chunk in enumerate(chunks):

            tokenized_docs.append(
                chunk.split()
            )

            cls.documents.append(
                chunk
            )

            cls.metadata.append(
                {
                    "source": source_name,
                    "chunk_index": index
                }
            )

        if cls.bm25 is None:

            cls.bm25 = BM25Okapi(
                tokenized_docs
            )

        else:

            all_docs = [
                doc.split()
                for doc in cls.documents
            ]

            cls.bm25 = BM25Okapi(
                all_docs
            )

    @classmethod
    def search(
        cls,
        query,
        top_k=5
    ):

        if cls.bm25 is None:

            return []

        scores = cls.bm25.get_scores(
            query.split()
        )

        ranked_indices = sorted(
            range(len(scores)),
            key=lambda i: scores[i],
            reverse=True
        )[:top_k]

        results = []

        for idx in ranked_indices:

            results.append(
                {
                    "content":
                        cls.documents[idx],
                    "source":
                        cls.metadata[idx]["source"],
                    "chunk_index":
                        cls.metadata[idx]["chunk_index"],
                    "score":
                        float(scores[idx])
                }
            )

        return results