books=Book.objects.get(id=1)
books.delete()
books=books.objects.all()
print(books)