import json
from pathlib import Path

DOCUMENTS_PATH = Path('data/processed/retrieval_documents.json')

OUTPUT_PATH = Path('evaluation/ground_truth.json')

def load_documents():
    with DOCUMENTS_PATH.open('r', encoding='utf-8') as f:
        return json.load(f)

def create_ground_truth(documents):
    ground_truth = []
    for document in documents:
        if document['document_type'] != 'discussion':
            continue
        question = document.get('question', '').strip()
        if not question:
            continue
        ground_truth.append({
            'question': question,
            'document_id': document['document_id'],
            'book_id': document['book_id'],
            'book_title': document['book_title'],
        })
    return ground_truth

def save_ground_truth(ground_truth):
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_PATH.open('w', encoding='utf-8') as f:
        json.dump(ground_truth, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    documents = load_documents()
    ground_truth = create_ground_truth(documents)
    save_ground_truth(ground_truth)
    print(f'Ground truth questions: {len(ground_truth)}')
    print(f'Saved to: {OUTPUT_PATH}')
    # print('\nExample:')
    # print(ground_truth[0])
    if ground_truth:
        print('\nExample:')
        print(ground_truth[0])
    else:
        print('\nNo ground-truth records were created.')

    