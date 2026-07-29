from dataclasses import dataclass
# from typing import Any

@dataclass
class RAGResponse:
    question: str
    answer: str
    documents: list[str]
    sources: list[str]
    prompt: str
    model: str
    retriever: str
    response_time: float
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int
    conversation_id: int | None = None