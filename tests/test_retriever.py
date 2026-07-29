from retrieval.factory import get_retriever

retriever = get_retriever("semantic")

results = retriever.search(
    "testing machine learning code",
    top_k=5,
)

print(f"Retrieved {len(results)} documents")

print(results[0]["book_title"])