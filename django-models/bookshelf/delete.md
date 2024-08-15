# Deleting a Book from the Database

To delete a book from the database, use Django's `Book.objects.get()` to retrieve the book, and then call the `delete()` method on the retrieved object. Below is an example of how to delete a book with the title "Nineteen Eighty-Four":

```python
from bookshelf.models import Book

# Retrieve the book with the title "Nineteen Eighty-Four"
try:
    book = Book.objects.get(title='Nineteen Eighty-Four')

    # Delete the book
    book.delete()

    print("The book with title 'Nineteen Eighty-Four' has been deleted.")
except Book.DoesNotExist:
    print("The book with title 'Nineteen Eighty-Four' does not exist.")
