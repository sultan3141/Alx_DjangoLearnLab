from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to="profile_pics/", blank=True, null=True)
    # followers: users who follow *this* user
    followers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="following",  # so user.following gives those they follow
        symmetrical=False,
        blank=True,
    )

    def __str__(self):
        return self.username
