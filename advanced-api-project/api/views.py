# api/views.py

from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .seriealizers import BookSerializer

# ListView and CreateView combined
class BookListCreateView(generics.ListCreateAPIView):
    """
    get:
    Return a list of all existing books.

    post:
    Create a new book instance. Requires authentication.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """
        Optionally customize the creation of a Book instance.
        For example, you can associate the book with the logged-in user.
        """
        serializer.save()

# DetailView, UpdateView, and DeleteView combined
class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    get:
    Retrieve a single book by its ID.

    put:
    Update an existing book. Requires authentication.

    delete:
    Delete a book. Requires authentication.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        """
        Optionally customize the update of a Book instance.
        """
        serializer.save()

    def perform_destroy(self, instance):
        """
        Optionally customize the deletion of a Book instance.
        """
        instance.delete()
