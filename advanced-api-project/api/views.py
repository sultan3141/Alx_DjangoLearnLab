"""
Views for Book model using Django REST Framework Generic Views.

- BookListView: Retrieve all books (open to everyone).
- BookDetailView: Retrieve a single book by ID (open to everyone).
- BookCreateView: Create a new book (authenticated users only).
- BookUpdateView: Update an existing book (authenticated users only).
- BookDeleteView: Delete a book (authenticated users only).

Permissions:
- List and Detail → AllowAny
- Create, Update, Delete → IsAuthenticated

Customizations:
- Added publication_year validation in create & update.
"""
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer


# Anyone can list books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# Anyone can read details
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# Only authenticated users can create
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# Only authenticated users can update
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# Only authenticated users can delete
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
