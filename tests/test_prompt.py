from rag.prompt import build_prompt

documents = [
    {
        "book_title": "Machine Learning Bookcamp",
        "search_text": """
Book: Machine Learning Bookcamp

Question:
How do I test ML code?

Replies:
Alexey: ...
"""
    },
    {
        "book_title": "Designing Machine Learning Systems",
        "search_text": """
Book: Designing Machine Learning Systems

Question:
Testing before deployment

Replies:
Chip Huyen: ...
"""
    }
]

question = "How should I test machine learning models?"

prompt = build_prompt(question, documents)

print(prompt)