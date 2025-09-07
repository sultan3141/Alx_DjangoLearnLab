from django.db import models
from django.utils import timezone

class Book(models.Model):
    title = models.CharField(max_length=200)        # short text (required)
    author = models.CharField(max_length=100)       # short text (required)
    publication_year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} by {self.author}"
    