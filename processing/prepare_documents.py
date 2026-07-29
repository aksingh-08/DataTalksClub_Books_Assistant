from pathlib import Path
import duckdb
import json 

DB_PATH = Path('books_pipeline.duckdb')
OUTPUT_PATH = Path('data/processed/retrieval_documents.json')

def save_documents(documents):
    OUTPUT_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )
    with OUTPUT_PATH.open(
        'w',
        encoding='utf-8'
    ) as f:
        json.dump(
            documents,
            f,
            ensure_ascii=False,
            indent=2
        )

def get_connection():
    return duckdb.connect(str(DB_PATH), read_only=True)

def load_books(conn):
    query = '''
    select book_id, title, description, content, source_file
    from books_data.books
    order by book_id
    '''
    return conn.execute(query).fetchall()

def prepare_book_documents(conn):
    rows = load_books(conn)
    documents = []

    for book_id, title, description, content, source_file in rows:
        search_text = f'''
        Book: {title}
        Description:
            {description or ""}
        Content: {content or ""}
        '''.strip()
        documents.append({
            'document_id': f'book::{book_id}',
            'document_type': 'book',
            'book_id': book_id,
            'book_title': title,
            'source_file': source_file,
            'question': '',
            'search_text': search_text,
        })
    return documents

def load_discussions(conn):
    query = '''
    select
    b.book_id,
    b.title,
    a._dlt_id,
    a._dlt_list_idx,
    a.name,
    a.text
    from books_data.books as b
    join books_data.books__archive as a
    on b._dlt_id = a._dlt_parent_id
    order by b.book_id, a._dlt_list_idx
    '''
    return conn.execute(query).fetchall()

def load_all_replies(conn):
    query = '''
    select
    _dlt_parent_id,
    name,
    text,
    _dlt_list_idx
    from books_data.books__archive__replies
    order by _dlt_parent_id, _dlt_list_idx
    '''
    return conn.execute(query).fetchall()

def group_replies_by_discussion(conn):
    rows = load_all_replies(conn)
    replies_by_discussion = {}
    for discussion_id, author, text, _ in rows:
        replies_by_discussion.setdefault(
            discussion_id, []
        ).append({
            'author': author,
            'text': text,
        })
    return replies_by_discussion

def prepare_discussion_documents(conn):
    discussions = load_discussions(conn)
    replies_by_discussion = group_replies_by_discussion(conn)
    documents = []
    for (book_id, book_title, discussion_dlt_id, discussion_index, question_author, question) in discussions:
        replies = replies_by_discussion.get(
            discussion_dlt_id,
            []
        )
        replies_text = '\n\n'.join(
            f'{reply['author']}: {reply['text']}'
            for reply in replies
        )
        search_text = f'''
        Book: {book_title}
        Question by {question_author}: {question}
        Replies: {replies_text if replies_text else 'No replies available.'}
        '''.strip()

        documents.append({
            'document_id': (f'discussion::{book_id}::{discussion_index}'),
            'document_type': 'discussion',
            'book_id': book_id,
            'book_title': book_title,
            'question_author': question_author,
            'question': question or '',
            'reply_count': len(replies),
            'has_replies': len(replies) > 0,
            'search_text': search_text,
        })
    return documents

def prepare_documents():
    conn = get_connection()
    try:
        book_documents = prepare_book_documents(conn)
        discussion_documents = prepare_discussion_documents(conn)
        return book_documents + discussion_documents
    finally:
        conn.close()

if __name__ == '__main__':
    documents = prepare_documents()
    book_count = sum(
        doc['document_type'] == 'book'
        for doc in documents
    )
    discussion_count = sum(
        doc['document_type'] == 'discussion'
        for doc in documents
    )
    print(f'Book documents: {book_count}')
    print(f'Discussion documents: {discussion_count}')
    print(f'Total documents: {len(documents)}')
    save_documents(documents)
    print(f'\nSaved to: {OUTPUT_PATH}')
    # print('\nExample document:\n')
    # print(documents[98]['search_text'])