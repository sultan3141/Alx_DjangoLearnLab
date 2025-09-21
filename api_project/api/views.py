from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()         # fetch all Book records
    serializer_class = BookSerializer     # use the serializer we defined
