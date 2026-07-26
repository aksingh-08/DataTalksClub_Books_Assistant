import json
from pathlib import Path
from minsearch import Index

DOCUMENTS_PATH = Path(
    'data/processed/retrieval_documents.json'
)

def load_documents():
    with DOCUMENTS_PATH.open(
        'r',
        encoding='utf-8'
    ) as f:
        return json.load(f)

def build_index(documents):
    index = Index(
        text_fields=[
            'search_text',
            'book_title',
        ],
        keyword_fields=[
            'document_id',
            'document_type',
            'book_id',
        ],
    )
    index.fit(documents)
    return index

def search(index, query, num_results=5):
    boost = {
        'question': 4.0,
        'book_title': 2.0,
        'search_text': 1.0,
    }
    return index.search(
        query=query,
        boost_dict=boost,
        num_results=num_results,
    )

if __name__ == '__main__':
    documents = load_documents()
    print(f'Loaded documents: {len(documents)}')
    index = build_index(documents)
    query = 'testing machine learning code'
    # query = 'time series machine learning'
    # query = 'data engineering pipelines'
    # query = 'MLOps'
    # query = 'how to become a data engineer'
    
    results = search(
        index,
        query,
        num_results=5,
    )
    for i, result in enumerate(results, start=1):
        print(f'\n--- Result {i} ---')
        print('Type:', result['document_type'])
        print('Book:', result['book_title'])
        print('ID:', result['document_id'])
        print()
        print(result['search_text'][:500])
        