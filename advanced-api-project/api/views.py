from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter  # Import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .seriealizers import BookSerializer

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]  # Add OrderingFilter here
    filterset_fields = ['title', 'author', 'publication_year']  # Enable filtering by these fields
    search_fields = ['title', 'author']  # Enable search by title and author
    ordering_fields = ['title', 'publication_year']  # Enable ordering by title and publication year

