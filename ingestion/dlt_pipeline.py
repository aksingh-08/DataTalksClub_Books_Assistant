from pathlib import Path
import dlt
import frontmatter

BOOKS_PATH = Path('data/raw/datatalksclub/_books')

@dlt.resource(
    name='books',
    write_disposition='replace',
    primary_key='book_id',
)
def books_resource():
    for book_file in BOOKS_PATH.glob('*.md'):
        if book_file.name == '_template.md':
            continue
        book = frontmatter.load(book_file)

        yield {
            'book_id': book_file.stem,
            'title': book.metadata.get('title'),
            'description': book.metadata.get('description'),
            'authors': book.metadata.get('authors', []),
            'content': book.content,
            'start': book.metadata.get('start'),
            'end': book.metadata.get('end'),
            'links': book.metadata.get('links', []),
            'cover': book.metadata.get('cover'),
            'image': book.metadata.get('image'),
            'archive': book.metadata.get('archive'),
            'source_file': book_file.name,
        }

if __name__ == '__main__':
    pipeline = dlt.pipeline(
        pipeline_name='books_pipeline',
        destination='duckdb',
        dataset_name='books_data',
    )
    load_info = pipeline.run(books_resource())
    print(load_info)
    