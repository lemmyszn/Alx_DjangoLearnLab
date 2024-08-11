# CRUD Operations Documentation

## Create Operation

**Command:**
```python
from bookshelf.models import Book
from datetime import date

# Creating a new book
new_book = Book.objects.create(
    title='1984',
    author='George Orwell',
    published_date=date(1949, 6, 8),
    isbn='9780451524935',
    pages=328,
    cover='https://example.com/cover.jpg'
)

# Output
print(f'Created Book: {new_book}')
Created Book: 1984

# Retrieve all books
all_books = Book.objects.all()
print("All Books:", list(all_books))

# Retrieve a specific book by ID
book = Book.objects.get(id=1)  # Replace with the actual ID of the book
print("Book by ID:", book)

# Retrieve books by specific attributes
books_by_author = Book.objects.filter(author='George Orwell')
print("Books by Author:", list(books_by_author))
All Books: [<Book: 1984 by George Orwell>]
Book by ID: 1984 by F. Scott Fitzgerald
Books by Author: [<Book:1984  by George Orwell >]

# Update an existing book
book = Book.objects.get(id=1)  # Replace with the actual ID of the book
book.title = '1984 (Updated)'
book.save()

# Output
print(f'Updated Book: {book}')
Updated Book: 1984 (Updated) by George Orwell


# Delete a specific book
book = Book.objects.get(id=1)  # Replace with the actual ID of the book
book.delete()

# Output
print(f'Deleted Book with ID 1')
Deleted Book with ID 1
