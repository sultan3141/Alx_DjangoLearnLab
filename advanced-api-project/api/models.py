"""
Models for the API.

- Author: Represents an author with a name field.
- Book: Represents a book with title, publication year, and a foreign key to Author.
  Relationship: One Author → Many Books (ForeignKey with related_name='books').
"""

from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=50)  # allow longer titles
    publication_year = models.IntegerField()  # store only year
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return f"{self.title} ({self.publication_year})"