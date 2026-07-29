from dataclasses import dataclass

@dataclass
class ConversationLog:
    question: str
    answer: str
    model: str
    retriever: str
    sources: list[str]
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int
    response_time: float
    feedback: str | None = None
    conversation_id: int | None = None