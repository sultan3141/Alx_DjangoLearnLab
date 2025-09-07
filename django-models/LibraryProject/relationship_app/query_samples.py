import os
import django

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)  # <- Filter books by author
        return books
    except Author.DoesNotExist:
        return []

# 2. List all books in a library
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return []

# 3. Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)  # <- This line explicitly uses objects.get(library=...)
        return librarian
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None

# Example usage (for testing)
if __name__ == "__main__":
    print(get_books_by_author("Author 1"))
    print(get_books_in_library("Central Library"))
    print(get_librarian_for_library("Central Library"))
