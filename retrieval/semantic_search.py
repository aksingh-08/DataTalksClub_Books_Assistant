import json
from pathlib import Path

import numpy as np
from sentence_transformers import SentenceTransformer

DOCUMENTS_PATH = Path('data/processed/retrieval_documents.json')
MODEL_NAME = 'sentence-transformers/all-MiniLM-L6-v2'
EMBEDDINGS_PATH = Path('embeddings/document_embeddings.npy')

def load_documents():
    with DOCUMENTS_PATH.open('r', encoding='utf-8') as f:
        return json.load(f)

def load_model():
    return SentenceTransformer(MODEL_NAME)

def create_embeddings(model, documents):
    texts = [
        document['search_text']
        for document in documents
    ]
    embeddings = model.encode(
        texts,
        show_progress_bar=True,
        normalize_embeddings=True,
    )
    return embeddings

def search(model, documents, document_embeddings, query, num_results=5):
    query_embedding = model.encode(query, normalize_embeddings=True)
    scores = document_embeddings @ query_embedding
    top_indices = np.argsort(scores)[::-1][:num_results]
    results = []
    for index in top_indices:
        result = documents[index].copy()
        result['score'] = float(scores[index])
        results.append(result)
    return results

def save_embeddings(embeddings):
    EMBEDDINGS_PATH.parent.mkdir(parents=True, exist_ok=True)
    np.save(EMBEDDINGS_PATH, embeddings)

def load_embeddings():
    return np.load(EMBEDDINGS_PATH)

def get_embeddings(model, documents):
    if EMBEDDINGS_PATH.exists():
        print('Loading existing embeddings...')
        try:
            embeddings = load_embeddings()
            if len(embeddings) != len(documents):
                print(
                    'Document count changed.'
                    'Regenerating embeddings...'
                )
                embeddings = create_embeddings(model, documents)
                save_embeddings(embeddings)
        except (EOFError, ValueError, OSError):
            print(
                'Embedding file is invalid.'
                'Regenrating embeddings...'
            )
            embeddings = create_embeddings(model, documents)
            save_embeddings(embeddings)
    else:
        print('Creating document embeddings...')
        embeddings = create_embeddings(model, documents)
        save_embeddings(embeddings)
        print(f'Embeddings saved to: {EMBEDDINGS_PATH}')
    return embeddings

if __name__ == '__main__':
    documents = load_documents()
    print(f'Loaded documents: {len(documents)}')
    model = load_model()
    document_embeddings = get_embeddings(model, documents)
    print(f'Embedding shape: {document_embeddings.shape}')
    query = 'testing machine learning code'
    results = search(model, documents, document_embeddings, query, num_results=5)
    for i, result in enumerate(results, start=1):
        print(f'\n--- Result {i} ---')
        print('Score:', round(result['score'], 4))
        print('Type:', result['document_type'])
        print('Book:', result['book_title'])
        print('ID:', result['document_id'])
        print()
        print(result['search_text'][:500])
        