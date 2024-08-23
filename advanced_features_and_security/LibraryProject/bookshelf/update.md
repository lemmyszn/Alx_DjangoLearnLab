# Updating a Book in the Database

To update an existing book in the database, such as changing its title, follow these steps. Below is an example of updating a book's title from "1984" to "Nineteen Eighty-Four":

```python
from bookshelf.models import Book

# Retrieve the book with the title "1984"
try:
    book = Book.objects.get(title='1984')

    # Update the title of the book
    book.title = 'Nineteen Eighty-Four'
    book.save()

    # Print the updated details
    print(f"Updated Title: {book.title}")
    print(f"Author: {book.author}")
    print(f"Published Date: {book.published_date}")
    print(f"ISBN: {book.isbn}")
    print(f"Pages: {book.pages}")
    print(f"Cover URL: {book.cover}")
except Book.DoesNotExist:
    print("The book with title '1984' does not exist.")
