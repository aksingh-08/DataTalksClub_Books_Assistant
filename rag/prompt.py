from rag.config import SYSTEM_PROMPT


def build_context(documents):
    context = ""

    for doc in documents:
        context += doc["search_text"] + "\n\n"

    return context


def build_prompt(question, documents):
    context = build_context(documents)

    prompt = f"""
{SYSTEM_PROMPT}

Context:
{context}

Question:
{question}

Answer:
"""

    return prompt