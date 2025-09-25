"""
Serializers for API.

- BookSerializer: Converts Book model instances to JSON and validates data.
  Includes custom validation to prevent future publication years.
- AuthorSerializer: Converts Author model instances to JSON.
  Includes nested BookSerializer to display each author's related books dynamically.
"""

from rest_framework import serializers
from django.utils import timezone
from .models import Author, Book


# BookSerializer: serializes all fields of Book
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

    # Custom validation: publication year cannot be in the future
    def validate_publication_year(self, value):
        current_year = timezone.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


# AuthorSerializer: serializes Author + their related books
class AuthorSerializer(serializers.ModelSerializer):
    # Nested serialization of books
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ["id", "name", "books"]

