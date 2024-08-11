# CRUD Operations Documentation

## Create Operation

**Command:**
```python
from bookshelf.models import Book
from datetime import date

# Creating a new book
new_book = Book.objects.create(
    title='The Great Gatsby',
    author='George Orwell',
    published_date=date(1925, 4, 10),
    isbn='9780743273565',
    pages=180,
    cover='https://example.com/gatsby.jpg'
)

# Output
print(f'Created Book: {new_book}')
Created Book: The Great Gatsby by George Orwell

# Retrieve all books
all_books = Book.objects.all()
print("All Books:", list(all_books))

# Retrieve a specific book by ID
book = Book.objects.get(id=1)  # Replace with the actual ID of the book
print("Book by ID:", book)

# Retrieve books by specific attributes
books_by_author = Book.objects.filter(author='George Orwell')
print("Books by Author:", list(books_by_author))
All Books: [<Book: The Great Gatsby by George Orwell>]
Book by ID: The Great Gatsby by F. Scott Fitzgerald
Books by Author: [<Book: The Great Gatsby by George Orwell >]

# Update an existing book
book = Book.objects.get(id=1)  # Replace with the actual ID of the book
book.title = 'The Great Gatsby (Updated)'
book.save()

# Output
print(f'Updated Book: {book}')
Updated Book: The Great Gatsby (Updated) by George Orwell


# Delete a specific book
book = Book.objects.get(id=1)  # Replace with the actual ID of the book
book.delete()

# Output
print(f'Deleted Book with ID 1')
Deleted Book with ID 1
