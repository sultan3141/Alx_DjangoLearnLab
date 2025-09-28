# api/test_views.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from books.models import Book, Author


class BookAPITests(APITestCase):
    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(username="tester", password="pass123")
        self.client = APIClient()

        # Create author
        self.author = Author.objects.create(name="J.R.R. Tolkien")

        # Create book
        self.book = Book.objects.create(
            title="The Hobbit",
            publication_year=1937,
            author=self.author
        )

        # Endpoints
        self.list_url = reverse("book-list")    # /api/books/
        self.detail_url = reverse("book-detail", args=[self.book.id])  # /api/books/<id>/

    # ---------- Public (Unauthenticated) Tests ----------

    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "The Hobbit")

    def test_retrieve_book(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "The Hobbit")

    def test_cannot_create_book_unauthenticated(self):
        response = self.client.post(self.list_url, {
            "title": "LOTR",
            "publication_year": 1954,
            "author": self.author.id
        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # ---------- Authenticated Tests ----------

    def test_create_book_authenticated(self):
        self.client.login(username="tester", password="pass123")
        response = self.client.post(self.list_url, {
            "title": "LOTR",
            "publication_year": 1954,
            "author": self.author.id
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_update_book_authenticated(self):
        self.client.login(username="tester", password="pass123")
        response = self.client.put(self.detail_url, {
            "title": "The Hobbit Updated",
            "publication_year": 1937,
            "author": self.author.id
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "The Hobbit Updated")

    def test_delete_book_authenticated(self):
        self.client.login(username="tester", password="pass123")
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    # ---------- Filtering / Searching / Ordering ----------

    def test_filter_books_by_title(self):
        response = self.client.get(self.list_url, {"title": "The Hobbit"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books(self):
        response = self.client.get(self.list_url, {"search": "Hobbit"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "The Hobbit")

    def test_order_books_by_year_desc(self):
        # Add another book
        Book.objects.create(title="LOTR", publication_year=1954, author=self.author)
        response = self.client.get(self.list_url, {"ordering": "-publication_year"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "LOTR")  # most recent first
