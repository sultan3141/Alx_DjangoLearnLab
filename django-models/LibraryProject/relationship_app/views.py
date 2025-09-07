from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Book, Library

# Function-based view
def list_books(request):
    books = Book.objects.all()  # Get all Book objects
    return render(request, 'list_books.html', {'books': books})

from django.views.generic import DetailView
from .models import Library

# Class-based view
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
