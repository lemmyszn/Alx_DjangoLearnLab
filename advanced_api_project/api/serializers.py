from datetime import timezone
from rest_framework import serializers
from .models import Book, Author

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        if value > timezone.now().year:
            raise serializers.ValidationError("The publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
# models.py
# Author: Represents an author with a one-to-many relationship to books.
# Book: Represents a book with a title, publication year, and a foreign key to the author.

# serializers.py
# BookSerializer: Handles serialization and validation of the Book model.
# AuthorSerializer: Serializes the Author model and includes a nested serializer for related books.
