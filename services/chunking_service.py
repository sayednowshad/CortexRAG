from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)


class ChunkingService:

    @staticmethod
    def create_chunks(text: str):

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=800,
            chunk_overlap=150
        )

        chunks = splitter.split_text(text)

        return chunks