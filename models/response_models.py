from pydantic import BaseModel
from typing import List


class RetrievedChunk(BaseModel):
    content: str
    source: str
    chunk_index: int


class SearchResponse(BaseModel):
    query: str
    results: List[RetrievedChunk]