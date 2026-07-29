import json
from pathlib import Path

from retrieval.tfidf_search import (load_documents, build_index, search)

GROUND_TRUTH_PATH = Path('evaluation/ground_truth.json')

def load_ground_truth():
    with GROUND_TRUTH_PATH.open('r', encoding='utf-8') as f:
        return json.load(f)

def hit_rate(relevance_total):
    return sum(any(relevance) for relevance in relevance_total) / len(relevance_total)

def mrr(relevance_total):
    total_score = 0.0
    for relevance in relevance_total:
        for rank, is_relevant in enumerate(relevance, start=1):
            if is_relevant:
                total_score += 1 / rank
                break
    return total_score / len(relevance_total)

def evaluate(ground_truth, documents, vectorizer, document_vectors, num_results=5):
    relevance_total = []
    for item in ground_truth:
        query = item['question']
        relevance_document_id = item['document_id']
        results = search(documents, vectorizer, document_vectors, query, num_results=num_results)
        relevance = [
            result['document_id'] == relevance_document_id
            for result in results
        ]
        relevance_total.append(relevance)
    return relevance_total

if __name__ == '__main__':
    documents = load_documents()
    ground_truth = load_ground_truth()
    print(f'Documents: {len(documents)}')
    print(f'Ground truth: {len(ground_truth)}')
    print('\nBuilding TF_IDF index...')
    vectorizer, document_vectors = build_index(documents)
    print(f'Vocabulary size: {len(vectorizer.vocabulary_)}')
    print(f'Vector shape: {document_vectors.shape}')
    print('\nEvaluating TF_IDF retrieval...')
    relevance_total = evaluate(
        ground_truth, documents, vectorizer, document_vectors, num_results=5
    )
    print('TF_IDF Evaluation')
    print('------------------')
    print(f'Hit@5: {hit_rate(relevance_total):.4f}')
    print(f'MRR: {mrr(relevance_total):.4f}')