from django.db import models
from django.utils import timezone

class Book(models.Model):
    title = models.CharField(max_length=200)        # short text (required)
    author = models.CharField(max_length=100)       # short text (required)
    published_date = models.DateField(              # a calendar date
        default=timezone.now                        # auto-filled on create
    )

    def __str__(self):
        return f"{self.title} by {self.author}"
