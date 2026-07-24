# DataTalksClub_Books_Assistant
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
