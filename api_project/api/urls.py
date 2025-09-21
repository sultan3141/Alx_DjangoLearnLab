from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# Create router and register the ViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Old ListAPIView (read-only)
    path('books/', BookList.as_view(), name='book-list'),

    # ✅ Router URLs for CRUD operations
    path('', include(router.urls)),
]
