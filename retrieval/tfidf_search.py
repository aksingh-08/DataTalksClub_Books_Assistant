import json
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

DOCUMENTS_PATH = Path(
    'data/processed/retrieval_documents.json'
)

def load_documents():
    with DOCUMENTS_PATH.open('r', encoding='utf-8') as f:
        return json.load(f)

def build_index(documents):
    texts = [
        document['search_text']
        for document in documents
    ]
    vectorizer = TfidfVectorizer(stop_words='english')
    document_vectors = vectorizer.fit_transform(texts)
    return vectorizer, document_vectors

def search(documents, vectorizer, document_vectors, query, num_results=5):
    query_vector = vectorizer.transform([query])
    scores = cosine_similarity(query_vector, document_vectors).flatten()
    top_indices = scores.argsort()[::-1][:num_results]
    results = []
    for index in top_indices:
        result = documents[index].copy()
        result['score'] = float(scores[index])
        results.append(result)
    return results

if __name__ == '__main__':
    documents = load_documents()
    print(f'Loaded documents: {len(documents)}')
    vectorizer, document_vectors = build_index(documents)
    print(f'Vocabulary size: {len(vectorizer.vocabulary_)}')
    print(f'Vector shape: {document_vectors.shape}')
    query = 'testing machinelearning code'
    results = search(documents, vectorizer, document_vectors, query, num_results=5)
    for i, result in enumerate(results, start=1):
        print(f'\n--- Result {i} ---')
        print('Score:', round(result['score'], 4))
        print('Type:', result['document_type'])
        print('Book:', result['book_title'])
        print('ID:', result['document_id'])
        print()
        print(result['search_text'][:500])
        