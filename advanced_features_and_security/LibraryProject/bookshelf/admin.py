from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")  # columns in the admin list
    search_fields = ("title", "author")                   # search box fields
    list_filter = ("publication_year",)                  # right-side filter     