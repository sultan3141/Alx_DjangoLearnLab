from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to="profile_pics/", blank=True, null=True)
    # ManyToMany to itself: a user follows other users
    following = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="followers",
        symmetrical=False,
        blank=True,
    )

    def __str__(self):
        return self.username
