<h1 align="center"> CortexRAG </h1>

<h3>
  Memory-Augmented Hybrid Retrieval Intelligence Platform
</h3>


<b> 1. Designed and built a Memory-Augmented RAG system using FastAPI and LLMs. </br>
<b> 2. Implemented Hybrid Retrieval (Vector + Keyword Search), Multi-Query Expansion, and Cross-Encoder Reranking. </br>
<b> 3. Developed Knowledge Graph–based Query Expansion and Conversational Topic Tracking. </br>
<b> 4. Built Memory Retrieval, Memory Deduplication, and Context Compression pipelines. </br>
<b> 5. Created Retrieval Analytics Dashboard with latency, source, and retrieval-quality monitoring. </br>
<b> 6.  Integrated Evidence Extraction to optimize token usage and improve answer grounding.  </br>


<br>

<h2 align="center"> Tech Stack </h2>

<br>

| Component            | Technology              | Strategy                       |
| -------------------- | ----------------------- | ------------------------------ |
| PDF Ingestion        | PDFPlumber              | Document Knowledge Extraction  |
| Chunking Engine      | Custom Chunker          | Context Preservation           |
| Embedding Generation | Sentence Transformers   | Semantic Encoding              |
| Vector Database      | FAISS                   | Dense Vector Retrieval         |
| Keyword Search       | BM25                    | Sparse Retrieval               |
| Hybrid Retrieval     | FAISS + BM25            | Retrieval Fusion               |
| Multi Query          | Query Expansion Service | Recall Improvement             |
| Knowledge Graph      | NetworkX                | Semantic Graph Expansion       |
| Reranking            | Cross Encoder           | Relevance Optimization         |
| Evidence Extraction  | Evidence Extractor      | Context Compression            |
| Memory Retrieval     | Memory Engine           | Long-Term Memory               |
| Topic Tracking       | Topic Tracker           | Conversational Context         |
| Memory Deduplication | Deduplicator            | Duplicate Prevention           |
| Context Builder      | Prompt Assembly Engine  | Context Aggregation            |
| Answer Generation    | Phi-3 Mini              | Retrieval-Augmented Generation |
| Analytics Dashboard  | Custom Analytics        | Pipeline Monitoring            |
| Backend Integration  | Spring Boot             | Enterprise API Integration     |
| Testing              | Postman                 | End-to-End Validation          |
| Version Control      | Git & GitHub            | Source Management              |

<br>

## Table of Contents

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
  
<br>
<br>

## Screenshots & Demonstrations
- [AI Layer](#ai-layer)
- [Hugging Face Dashboard](#huggingface)
- [Postman Testing](#postman)
- [Spring Boot Integration](#springboot)
- [RAG Analytics Dashboard](#rag-pipeline)


<a id="project-structure"></a>
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
<br>
<br>

<a id="phase-01---pdf-ingestion"></a>
<h2 align="center"> Phase 01 • Data Ingestion </h2>
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

<br>
<br>

<a id="phase-02---chunking-engine"></a>
<h2 align="center"> Phase 02 • Chunking Engine </h2>
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

<br>
<br>

<a id="phase-03---embedding-generation"></a>
<h2 align="center"> Phase 03 • Embedding Generation </h2>
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
<br>
<br>

<a id="phase-04---vector-database"></a>
<h2 align="center"> Phase 04 • Vector Database </h2>
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
<br>
<br>

<a id="phase-05---dense-retrieval"></a>
<h2 align="center"> Phase 05 • Dense Retrieval </h2>
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
<br>
<br>

<a id="phase-06---bm25-retrieval"></a>
<h2 align="center"> Phase 06 • BM25 Retrieval </h2>
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
<br>
<br>

<a id="phase-07---hybrid-retrieval"></a>
<h2 align="center"> Phase 07 • Hybrid Retrieval </h2>
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

<br>
<br>

<a id="phase-08---cross-encoder-reranking"></a>
<h2 align="center"> Phase 08 • Cross Encoder Reranking </h2>
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
<br>
<br>

<a id="phase-09---evidence-extraction"></a>
<h2 align="center"> Phase 09 • Evidence Extraction </h2>
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
<br>
<br>

<a id="phase-10---memory-system"></a>
<h2 align="center"> Phase 10 • Memory System </h2>
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

<br>
<br>

<a id="phase-11---topic-tracking"></a>
<h2 align="center"> Phase 11 • Topic Tracking </h2>
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

<br>
<br>

<a id="phase-12---multi-query-expansion"></a>
<h2 align="center"> Phase 12 • Multi Query Expansion </h2>
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

<br>
<br>

<a id="phase-13---context-builder"></a>
<h2 align="center"> Phase 13 • Context Builder </h2>
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

<br>
<br>

<a id="phase-14---answer-generation"></a>
<h2 align="center"> Phase 14 • Answer Generation </h2>
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

<br>
<br>

<a id="phase-15---analytics-dashboard"></a>
<h2 align="center"> Phase 15 • Analytics Dashboard </h2>
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

<br>
<br>

<a id="ai-layer"></a>

<table align="center">

  <h2 align="center"> AI Layer • (FastAPI + RAG + LLM) </h2>

<tr>
<td>
<img width="500" src="https://github.com/user-attachments/assets/07b2bc8a-7198-4e83-9a32-9aae304ca2cf">
<br>
<p align="center"><b>Document Ingestion</b></p>
</td>

<td>
<img width="500" src="https://github.com/user-attachments/assets/90a873c9-674a-41ba-9e7b-90dd9aa7dd10">
<br>
<p align="center"><b>Chunks, Vector Storage, Collection Size (Meta Data)</b></p>
</td>
</tr>

<tr>
<td>
<img width="500" src="https://github.com/user-attachments/assets/6533451b-48b2-4339-8a38-c1d38459f8ed">
<br>
<p align="center"><b>Retrieval Pipeline Logs</b></p>
</td>

<td>

<img width="500" src="https://github.com/user-attachments/assets/75d0093b-30f6-493b-b0a4-6eb3ecf9e0c1" />
<br>
<p align="center"><b> Upload, Serach, Chat </b></p>
</td>
</tr>
</table>

<a id="huggingface"></a>
<br>
<br>

<table align="center">

  <h2 align="center"> Hugging Face • (API Dashboard) </h2>

<tr>
<td>
<img width="500" src="https://github.com/user-attachments/assets/5614fb90-d407-4779-b444-95fce0649fb5">
<br>
<p align="center"><b> API Cost • Inference Dashboard </b></p>
</td>

<td>
<img width="500" src="https://github.com/user-attachments/assets/5a835f73-84e2-46e6-8d40-7ac54dd09716">
<br>
<p align="center"><b> Phi-3-mini-4K • 3B+ </b></p>
</td>
</tr>

</table>

<a id="postman"></a>
<br>
<br>

<table align="center">

  <h2 align="center"> PostMan Dashboard • Frontend (Testing) </h2>

<tr>
<td>
<img width="500" src="https://github.com/user-attachments/assets/d1122497-db2f-4a0d-bfae-2ddddd47b2a0">
<br>
<p align="center"><b> /api/Chat 200K </b></p>
</td>

<td>
<img width="500" src="https://github.com/user-attachments/assets/1e139df2-3bb1-4eb6-96c1-56de1aec5381">
<br>
<p align="center"><b> User Query -01  </b></p>
</td>

<td>
<img width="500" src="https://github.com/user-attachments/assets/af2678a0-966e-4ed9-86da-2f732d41301c">
<br>
<p align="center"><b> User Query - 02 </b></p>
</td>

</tr>
</table>

<a id="springboot"></a>

<br>
<br>
<table align="center">

  <h2 align="center"> Backend • (Spring Boot) </h2>

<tr>

<td>
<img width="500" src="https://github.com/user-attachments/assets/ba144b35-3493-438e-af7d-e293fcc38f1e">
<br>
<p align="center"><b> Spring Boot Connection with RAG Pipeline </b></p>
</td>

</tr>
</table>

<a id="rag-pipeline"></a>
<br>
<br>

<table align="center">
  <h2 align="center"> RAG Pipeline • (Metric Analysis Dashboard) </h2>
<tr>

<td>
<img width="500" src="https://github.com/user-attachments/assets/fbca06d7-f3e7-4bf6-b184-ffa02c779e0e">
<br>
<p align="center"> <b> Benchmark Testing, Metric Analysis </b> </p>
</td>

</tr>
</table>

<br>
<br>
