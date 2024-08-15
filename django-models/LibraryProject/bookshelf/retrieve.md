### Retrieve Operation

To retrieve and display all attributes of the book you just created, use the following commands in the Django shell:

**Command:**

```python
from bookshelf.models import Book

# Retrieve all books
books = Book.objects.all()
for book in books:
    print(f"Title: {book.title}, Author: {book.author}, Publication Year: {book.publication_year}")

# Retrieving a Book from the Database

To retrieve a book from the database, you can use Django's `Book.objects.get()` method. Here’s how to retrieve a book with the title "1984":

```python
from bookshelf.models import Book

# Retrieve the book with the title "1984"
try:
    book = Book.objects.get(title='1984')
    print(f"Title: {book.title}")
    print(f"Author: {book.author}")
    print(f"Published Date: {book.published_date}")
    print(f"ISBN: {book.isbn}")
    print(f"Pages: {book.pages}")
    print(f"Cover URL: {book.cover}")  # This will show the URL of the cover image
except Book.DoesNotExist:
    print("The book with title '1984' does not exist.")
