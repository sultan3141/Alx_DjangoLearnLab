# posts/tests.py
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from django.contrib.auth import get_user_model
from posts.models import Post, Like
from notifications.models import Notification

User = get_user_model()

class LikeNotificationTests(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username="user1", password="pass123")
        self.user2 = User.objects.create_user(username="user2", password="pass123")
        # Create a Post (adjust according to your Post model fields)
        self.post = Post.objects.create(author=self.user2, content="Hello world")
        self.client1 = APIClient()
        self.client1.force_authenticate(self.user1)

    def test_like_creates_like_and_notification(self):
        url = reverse("post-like", args=[self.post.pk])
        resp = self.client1.post(url)
        self.assertEqual(resp.status_code, 201)
        self.assertTrue(Like.objects.filter(user=self.user1, post=self.post).exists())

        # Check notification created
        notif = Notification.objects.filter(recipient=self.user2, actor=self.user1, verb__icontains="liked").first()
        self.assertIsNotNone(notif)

    def test_unlike_removes_like(self):
        # like first
        Like.objects.create(user=self.user1, post=self.post)
        url = reverse("post-unlike", args=[self.post.pk])
        resp = self.client1.post(url)
        self.assertEqual(resp.status_code, 200)
        self.assertFalse(Like.objects.filter(user=self.user1, post=self.post).exists())
