from retrieval.semantic_search import SemanticRetriever
from retrieval.text_search import TextSearchRetriever
from retrieval.tfidf_search import TFIDFRetriever


RETRIEVERS = {
    "semantic": SemanticRetriever,
    "tfidf": TFIDFRetriever,
    "text": TextSearchRetriever,
}


def get_retriever(name: str):
    try:
        return RETRIEVERS[name]()
    except KeyError:
        raise ValueError(f"Unknown retriever: {name}")