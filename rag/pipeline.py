import time

from monitoring.logger import logger

from retrieval.factory import get_retriever

from rag.schema import RAGResponse
from rag.config import MODEL_NAME, SEARCH_METHOD, TOP_K
from rag.prompt import build_prompt
from rag.llm import generate_answer


class RAGPipeline:

    def __init__(self, retriever=None):
        self.retriever = get_retriever(SEARCH_METHOD)

    def retrieve(self, question: str):
        return self.retriever.search(
            query=question,
            top_k=TOP_K,
        )

    def ask(self, question: str) -> RAGResponse:
        logger.info(
            'RAG request',
            extra={
                'question': question,
                'retriever': SEARCH_METHOD,
                'top_k': TOP_K
            },
        )
        logger.info(f'Retriever: {SEARCH_METHOD}')
        start = time.perf_counter()
        
        documents = self.retrieve(question)
        logger.info(f'Retrieved {len(documents)} documents')
        prompt = build_prompt(
            question,
            documents
        )
        answer, usage = generate_answer(prompt)
        elapsed = time.perf_counter() - start
        logger.info(f'Response generated in {elapsed:.2f} seconds')
        sources = []
        for doc in documents:
            title = doc['book_title']
            if title not in sources:
                sources.append(title)
        return RAGResponse(
            question=question,
            answer=answer,
            documents=documents,
            sources=sources,
            prompt=prompt,
            model=MODEL_NAME,
            retriever=SEARCH_METHOD,
            response_time=elapsed,
            prompt_tokens=usage['prompt_tokens'],
            completion_tokens=usage['completion_tokens'],
            total_tokens=usage['total_tokens']
        )
        