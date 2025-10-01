from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    # Authentication
    path("login/", auth_views.LoginView.as_view(template_name="blog/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="blog/logout.html"), name="logout"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),

    # Blog Post CRUD
    path("posts/", PostListView.as_view(), name="posts"),                 # List all posts
    path("posts/new/", PostCreateView.as_view(), name="post-create"),     # Create a new post
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),# View a single post
    path("posts/<int:pk>/edit/", PostUpdateView.as_view(), name="post-update"),   # Update a post
    path("posts/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"), # Delete a post
]

