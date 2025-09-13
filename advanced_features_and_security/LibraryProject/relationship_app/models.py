from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


# ------------------------------
# Author Model
# ------------------------------
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# ------------------------------
# Book Model with Permissions
# ------------------------------
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return self.title

    class Meta:
        permissions = (
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        )


# ------------------------------
# Library Model
# ------------------------------
class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name="libraries")

    def __str__(self):
        return self.name


# ------------------------------
# Librarian Model
# ------------------------------
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name="librarian")

    def __str__(self):
        return self.name


# ------------------------------
# UserProfile for RBAC
# ------------------------------
class UserProfile(models.Model):
    ROLE_CHOICES = (
        ("Admin", "Admin"),
        ("Librarian", "Librarian"),
        ("Member", "Member"),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        # ✅ Use email instead of username (since username is removed)
        return f"{self.user.email} - {self.role}"


# ------------------------------
# Signal to create UserProfile automatically
# ------------------------------
@receiver(post_save, sender=settings.AUTH_USER_MODEL)  # ✅ point to custom user
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
