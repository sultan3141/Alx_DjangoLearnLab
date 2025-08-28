book = Book.objects.get(id=1)
book.title = "123"   # ✅ correct field name
book.save()          # ✅ don’t forget to save changes to the database
print(book.title)
