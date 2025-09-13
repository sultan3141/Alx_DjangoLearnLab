from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from relationship_app.models import Book, Author

# ------------------------------
# View to list all books
# ------------------------------
@permission_required('relationship_app.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()  # Fetch all books
    return render(request, "bookshelf/book_list.html", {"books": books})

# ------------------------------
# View to create a new book
# ------------------------------
@permission_required('relationship_app.can_create', raise_exception=True)
def create_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author_id = request.POST.get("author")
        Book.objects.create(title=title, author_id=author_id)
        return redirect("book_list")
    authors = Author.objects.all()
    return render(request, "bookshelf/create_book.html", {"authors": authors})

# ------------------------------
# View to edit a book
# ------------------------------
@permission_required('relationship_app.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.title = request.POST.get("title")
        book.save()
        return redirect("book_list")
    return render(request, "bookshelf/edit_book.html", {"book": book})

# ------------------------------
# View to delete a book
# ------------------------------
@permission_required('relationship_app.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect("book_list")
