# DataTalksClub_Books_Assistant

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![RAG](https://img.shields.io/badge/RAG-Application-success?style=for-the-badge)
![Groq](https://img.shields.io/badge/LLM-Groq-orange?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red?style=for-the-badge&logo=streamlit)
![Sentence Transformers](https://img.shields.io/badge/Embeddings-SentenceTransformers-green?style=for-the-badge)
![DuckDB](https://img.shields.io/badge/Database-DuckDB-yellow?style=for-the-badge)
![DLT](https://img.shields.io/badge/Ingestion-dlt-purple?style=for-the-badge)


An end-to-end RAG application for discovering, exploring, and asking questions about books featured in the DataTalksClub Book of the Week archive.

The project will focus on building a complete RAG pipeline, including data ingestion, document processing, retrieval, evaluation, monitoring, and a user-friendly interface.

**Future Scope:** Extend the application into an agentic assistant with external tools and planning capabilities.

### Scope
- RAG Pipeline
- Semantic Search
- Book Recommendation
- Question Answering
- Book Comparison
- Evaluation
- Monitoring
- Feedback Collection
- Streamlit UI

### Future Work
- Agent Framework
- Toll Calling
- Web Search
- Memory
- Multi-Agent Workflow

## Technology Stack
**Component**                  |                   **Technology**
-------------------------------|-------------------------------------------
LLM                            |               GitHub Models (openai/gpt-5)
Embedding Model                |               Sentence Transformers (local)
Vector Database                |               Qdrant or Chroma
Data Ingestion                 |               dlt
Backend                        |               Python
Interface                      |               Streamlit
Monitoring                     |               OpenTelemetry + Grafana
Evaluation                     |               Retrieval Metrics + GPT-5 Judge (limited set)
Feedback Storage               |               SQLite
