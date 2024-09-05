from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
# models.py
# Author: Represents an author with a one-to-many relationship to books.
# Book: Represents a book with a title, publication year, and a foreign key to the author.

# serializers.py
# BookSerializer: Handles serialization and validation of the Book model.
# AuthorSerializer: Serializes the Author model and includes a nested serializer for related books.
