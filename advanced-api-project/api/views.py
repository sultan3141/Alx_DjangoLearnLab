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

from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.utils import timezone
from rest_framework.response import Response
from rest_framework import status

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Retrieve a single book by ID (GET) → open to everyone
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# Create a new book (POST) → only authenticated users

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        year = serializer.validated_data.get("publication_year")
        if year > timezone.now().year:
            return Response(
                {"error": "Publication year cannot be in the future."},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer.save()


class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        year = serializer.validated_data.get("publication_year")
        if year > timezone.now().year:
            return Response(
                {"error": "Publication year cannot be in the future."},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer.save()

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]