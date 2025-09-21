from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=20)
    author=models.CharField(max_length=15)
    
    def __str__(self):
     return self.title