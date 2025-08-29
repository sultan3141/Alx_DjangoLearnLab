from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_date")  # columns in the admin list
    search_fields = ("title", "author")                   # search box fields
    list_filter = ("published_date",)                     # right-side filter
