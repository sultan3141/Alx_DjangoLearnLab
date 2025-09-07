from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Book, Library
from django.views.generic import DetailView
# Function-based view
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # match folder structure
    context_object_name = 'library''
