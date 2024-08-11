### Retrieve Operation

To retrieve and display all attributes of the book you just created, use the following commands in the Django shell:

**Command:**

```python
from bookshelf.models import Book

# Retrieve all books
books = Book.objects.all()
for book in books:
    print(f"Title: {book.title}, Author: {book.author}, Publication Year: {book.publication_year}")

