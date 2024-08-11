# Updating a Book in the Database

To update an existing book in the database, you can retrieve the book using `Book.objects.get()` and then modify its attributes. Below is an example of how to update the book with the title "1984":

```python
from bookshelf.models import Book

# Retrieve the book with the title "1984"
try:
    book = Book.objects.get(title='1984')

    # Update attributes of the book
    book.author = 'George Orwell'
    book.published_date = '1949-06-08'
    book.isbn = '9780451524935'
    book.pages = 328
    book.cover = 'https://example.com/new_cover.jpg'  # Example new cover URL

    # Save the changes
    book.save()

    # Print the updated details
    print(f"Updated Title: {book.title}")
    print(f"Updated Author: {book.author}")
    print(f"Updated Published Date: {book.published_date}")
    print(f"Updated ISBN: {book.isbn}")
    print(f"Updated Pages: {book.pages}")
    print(f"Updated Cover URL: {book.cover}")
except Book.DoesNotExist:
    print("The book with title '1984' does not exist.")
