from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

# Previous ListAPIView (still here)
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# ✅ New ViewSet for full CRUD
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
