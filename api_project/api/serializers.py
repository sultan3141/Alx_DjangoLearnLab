from rest_framework import serializers
from .models import Book   # import your Book model

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'   # includes all fields (id, title, author)
