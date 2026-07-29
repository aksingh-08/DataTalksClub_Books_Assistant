from abc import ABC, abstractmethod

class BaseRetriever(ABC):
    @abstractmethod
    def search(self, query: str, top_k: int):
        '''
        Return the top_k most relevant documents.
        '''
        pass