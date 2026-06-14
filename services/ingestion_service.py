import os

from loaders.pdf_loader import PDFLoader

from services.chunking_service import (
    ChunkingService
)

from services.embedding_service import (
    EmbeddingService
)

from vectorstore.chroma_manager import (
    ChromaManager
)

from vectorstore.bm25_manager import (
    BM25Manager
)
from graph.graph_builder import (
    GraphBuilder
)

class IngestionService:

    PROCESSED_DIR = "data/processed"

    @classmethod
    def process_pdf(
        cls,
        file_path,
        file_name
    ):

        extracted_text = (
            PDFLoader.extract_text(
                file_path
            )
        )

        txt_file_name = (
            file_name.replace(
                ".pdf",
                ".txt"
            )
        )

        processed_path = os.path.join(
            cls.PROCESSED_DIR,
            txt_file_name
        )

        with open(
            processed_path,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(
                extracted_text
            )

        chunks = (
            ChunkingService.create_chunks(
                extracted_text
            )
        )

        embeddings = (
            EmbeddingService.generate_embeddings(
                chunks
            )
        )

        ChromaManager.add_chunks(
            chunks=chunks,
            embeddings=embeddings,
            source_name=file_name
        )

        BM25Manager.build_index(
            chunks,
            file_name
        )

        GraphBuilder.add_chunks(
            chunks
        )

        return {
            "pdf_name": file_name,
            "text_file": txt_file_name,
            "characters_extracted":
                len(extracted_text),
            "chunks_created":
                len(chunks),
            "vectors_stored":
                len(chunks),
            "total_collection_size":
                ChromaManager.count()
        }