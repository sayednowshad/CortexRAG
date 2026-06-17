<h1> Knowledge Intelligence Engine (KIE) </h1>

<h3>
  Advanced Retrieval-Augmented Generation Platform
</h3>


<b> 1. Designed and built a Memory-Augmented RAG system using FastAPI and LLMs. </br>
<b> 2. Implemented Hybrid Retrieval (Vector + Keyword Search), Multi-Query Expansion, and Cross-Encoder Reranking. </br>
<b> 3. Developed Knowledge Graph–based Query Expansion and Conversational Topic Tracking. </br>
<b> 4. Built Memory Retrieval, Memory Deduplication, and Context Compression pipelines. </br>
<b> 5. Created Retrieval Analytics Dashboard with latency, source, and retrieval-quality monitoring. </br>
<b> 6.  Integrated Evidence Extraction to optimize token usage and improve answer grounding.  </br>


## Table of Contents

- [Project Overview](#project-overview)
- [System Architecture](#system-architecture)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Phase 01 - PDF Ingestion](#phase-01---pdf-ingestion)
- [Phase 02 - Chunking Engine](#phase-02---chunking-engine)
- [Phase 03 - Embedding Generation](#phase-03---embedding-generation)
- [Phase 04 - Vector Database](#phase-04---vector-database)
- [Phase 05 - Dense Retrieval](#phase-05---dense-retrieval)
- [Phase 06 - BM25 Retrieval](#phase-06---bm25-retrieval)
- [Phase 07 - Hybrid Retrieval](#phase-07---hybrid-retrieval)
- [Phase 08 - Cross Encoder Reranking](#phase-08---cross-encoder-reranking)
- [Phase 09 - Evidence Extraction](#phase-09---evidence-extraction)
- [Phase 10 - Memory System](#phase-10---memory-system)
- [Phase 11 - Topic Tracking](#phase-11---topic-tracking)
- [Phase 12 - Multi Query Expansion](#phase-12---multi-query-expansion)
- [Phase 13 - Context Builder](#phase-13---context-builder)
- [Phase 14 - Answer Generation](#phase-14---answer-generation)
- [Phase 15 - Analytics Dashboard](#phase-15---analytics-dashboard)
- [Backend Screenshots](#backend-screenshots)
- [Testing Results](#testing-results)
- [Future Improvements](#future-improvements)


<h2 align="center"> Complete RAG Architecture </h2>

```mermaid
flowchart TB

User[User]

subgraph Offline Pipeline
    PDF[PDF Files]
    Loader[PDF Loader]
    Chunker[Chunking]
    Embedder[Embeddings]
    VectorDB[(Vector DB)]
    BM25[(BM25 Index)]

    PDF --> Loader
    Loader --> Chunker
    Chunker --> Embedder
    Embedder --> VectorDB

    Chunker --> BM25
end

subgraph Online Pipeline
    Query[Question]
    MQ[Multi Query]

    Dense[Dense Search]
    Sparse[BM25 Search]

    Hybrid[Hybrid Retrieval]
    Rerank[Reranker]

    Memory[Memory]
    Topic[Topic Tracker]

    Context[Context Builder]
    LLM[LLM]

    Query --> MQ

    MQ --> Dense
    MQ --> Sparse

    VectorDB --> Dense
    BM25 --> Sparse

    Dense --> Hybrid
    Sparse --> Hybrid

    Hybrid --> Rerank

    Memory --> Context
    Topic --> Context

    Rerank --> Context

    Context --> LLM
end

User --> Query

LLM --> Analytics[Analytics Dashboard]

Analytics --> Answer[Response]
```

<a id="phase-02---chunking-engine"></a>
<h2 align="center"> Phase 02 • Chunking Engine </h2>
<p align="center"> <b> Purpose: </b> "Convert uploaded PDFs into raw textual knowledge." </p>

```mermaid
flowchart LR

A[PDF Files]
-->
B[PDF Loader]

B
-->
C[Extract Raw Text]

C
-->
D[Store Documents]

D
-->
E[Knowledge Base]
```

<h2 align="center"> Phase: 02 (Chunking Engine) </h2>
<p align="center"> <b> Purpose: </b> "Break large documents into searchable chunks" </p>

```mermaid
flowchart LR

A[Raw Document]
-->
B[Chunking Service]

B
-->
C[Chunk 1]

B
-->
D[Chunk 2]

B
-->
E[Chunk N]

C --> F[Chunk Store]
D --> F
E --> F
```

<h2 align="center"> Phase: 03 (Embedding Generation) </h2>
<p align="center"> <b> Purpose: </b> "Convert text into vector representations." </p>

```mermaid
flowchart LR

A[Chunks]

-->
B[Sentence Transformer]

-->
C[Embeddings]

-->
D[Vector Store]
```


<h2 align="center"> Phase: 04 (Vector Database) </h2>
<p align="center"> <b> Purpose: </b> "Store semantic representations for retrieval." </p>

```mermaid
flowchart LR

A[Chunk]

-->
B[Embedding]

-->
C[FAISS / Chroma]

-->
D[Persistent Storage]
```


<h2 align="center"> Phase: 05 (Dense Retrieval) </h2>
<p align="center"> <b> Purpose: </b> "Semantic similarity search." </p>

```mermaid
flowchart LR

A[User Query]

-->
B[Embedding Model]

-->
C[Query Vector]

-->
D[Vector Search]

-->
E[Top K Chunks]
```


<h2 align="center"> Phase: 06 (BM25 Retrieval) </h2>
<p align="center"> <b> Purpose: </b> "Exact keyword retrieval." </p>

```mermaid
flowchart LR

A[User Query]

-->
B[BM25 Engine]

-->
C[Keyword Matching]

-->
D[Top K Results]
```

<h2 align="center"> Phase: 07 (Hybrid Retrieval) </h2>
<p align="center"> <b> Purpose: </b> "Combine semantic and keyword search." </p>

```mermaid
flowchart TD

A[Query]

B[Dense Search]

C[BM25 Search]

D[Merge Results]

E[Hybrid Results]

A --> B
A --> C

B --> D
C --> D

D --> E
```

<h2 align="center"> Phase: 08 (Cross Encoder Reranking) </h2>
<p align="center"> <b> Purpose: </b> "Improve retrieval precision." </p>

```mermaid
flowchart LR

A[Hybrid Results]

-->
B[Cross Encoder]

-->
C[Relevance Scores]

-->
D[Top Ranked Chunks]
```


<h2 align="center"> Phase: 09 (Evidence Extraction) </h2>
<p align="center"> <b> Purpose: </b> "Reduce unnecessary tokens." </p>

```mermaid
flowchart LR

A[Top Chunks]

-->
B[Sentence Scoring]

-->
C[Important Sentences]

-->
D[Compressed Context]
```

<h2 align="center"> Phase: 10 (Memory System) </h2>
<p align="center"> <b> Purpose: </b> "Maintain long-term conversation context." </p>

```mermaid
flowchart TD

A[User Question]

-->
B[Memory Retriever]

-->
C[Previous Conversations]

-->
D[Relevant Memories]
```

<h2 align="center"> Phase: 11 (Topic Tracking) </h2>
<p align="center"> <b> Purpose: </b> "Resolve follow-up questions like:
"Explain it?"
"Compare them?"" </p>

```mermaid
flowchart LR

A[Question]

-->
B[Topic Extractor]

-->
C[Current Topic]

-->
D[Topic Tracker]
```


<h2 align="center"> Phase: 12 (Multi Query Expansion) </h2>
<p align="center"> <b> Purpose: </b> "Improve recall by generating multiple search queries." </p>

```mermaid
flowchart TD

A[Original Question]

-->
B[Query Generator]

B --> C[Variant 1]

B --> D[Variant 2]

B --> E[Variant 3]

C --> F[Retrieval]
D --> F
E --> F
```

<h2 align="center"> Phase: 13 (Context Builder) </h2>
<p align="center"> <b> Purpose: </b> "Assemble everything before LLM generation." </p>

```mermaid
flowchart TD

A[Retrieved Chunks]

B[Memory]

C[Topic]

D[Evidence]

A --> E[Context Builder]
B --> E
C --> E
D --> E

E --> F[Final Prompt Context]
```

<h2 align="center"> Phase: 14 (Answer Generation) </h2>
<p align="center"> <b> Purpose: </b> "Generate grounded responses from retrieved knowledge." </p>

```mermaid
flowchart LR

A[Prompt]

-->
B[LLM]

-->
C[Generated Answer]

-->
D[Response Formatter]
```

<h2 align="center"> Phase: 15 (Analytics Dashboard) </h2>
<p align="center"> <b> Purpose: </b> "Observe and evaluate RAG pipeline performance." </p>

```mermaid
flowchart TD

A[Question]

-->
B[Analytics Service]

B --> C[Retrieval Time]

B --> D[Rerank Time]

B --> E[LLM Time]

B --> F[Memory Hits]

B --> G[Sources]

B --> H[Dashboard Output]
```

