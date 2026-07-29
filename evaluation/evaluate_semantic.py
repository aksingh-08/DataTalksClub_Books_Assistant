import json
from pathlib import Path

from retrieval.semantic_search import (
    load_documents,
    load_model,
    get_embeddings,
    search
)

GROUND_TRUTH_PATH = Path('evaluation/ground_truth.json')

def load_ground_truth():
    with GROUND_TRUTH_PATH.open('r', encoding='utf-8') as f:
        return json.load(f)

def hit_rate(relevance_total):
    return sum(
        any(relevance)
        for relevance in relevance_total
    ) / len(relevance_total)

def mrr(relevance_total):
    total_score = 0.0
    for relevance in relevance_total:
        for rank, is_relevant in enumerate(relevance, start=1):
            if is_relevant:
                total_score += 1 / rank
                break
    return total_score / len(relevance_total)

def evaluate(
    ground_truth, documents, model, document_embeddings, num_results=5
):
    relevance_total = []
    for i, item in enumerate(ground_truth, start=1):
        query = item['question']
        relevance_document_id = item['document_id']
        results = search(
            model, documents, document_embeddings, query, num_results=num_results
        )
        relevance = [
            result['document_id'] == relevance_document_id
            for result in results
        ]
        relevance_total.append(relevance)
        if i % 100 == 0:
            print(f'Processed {i}/{len(ground_truth)} questions')
    return relevance_total

if __name__ == '__main__':
    documents = load_documents()
    ground_truth = load_ground_truth()
    print(f'documents: {len(documents)}')
    print(f'ground truth: {len(ground_truth)}')
    print('\nloading semantic model...')
    model = load_model()
    print('\nloading document embeddings...')
    document_embeddings = get_embeddings(model, documents)
    print(f'embedding shape: {document_embeddings.shape}')
    print('\nevaluating semantic retrieval...')
    relevance_total = evaluate(
        ground_truth, documents, model, document_embeddings, num_results=5
    )
    print('\nSemantic search evaluation')
    print('------------------------------')
    print(f'Hit@5: {hit_rate(relevance_total):.4f}')
    print(f'MRR: {mrr(relevance_total):.4f}')
    