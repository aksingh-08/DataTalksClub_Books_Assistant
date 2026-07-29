from rag.pipeline import RAGPipeline

rag = RAGPipeline()

result = rag.ask(
    "How can I become a machine learning engineer?"
)
print(result.answer)
print("\nBooks used:")

# for doc in result["documents"]:
#     print("-", doc["book_title"])
for source in result.sources:
    print('-', source)

print('\nMetadata:')
print(f'Model: {result.model}')
print(f'Retriever: {result.retriever}')
print(f'Response Time: {result.response_time:.2f} sec')

print('\nToken Usage')
print(f"Prompt Tokens: {result.prompt_tokens}")
print(f"Completion Tokens: {result.completion_tokens}")
print(f"Total Tokens: {result.total_tokens}")
