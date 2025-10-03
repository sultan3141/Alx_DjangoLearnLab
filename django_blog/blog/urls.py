from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import post_detail, CommentUpdateView, CommentDeleteView
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
    path("post/new/", PostCreateView.as_view(), name="post-create"),     # Create a new post
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),# View a single post
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),   # Update a post
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"), # Delete a post

    path("posts/<int:pk>/", post_detail, name="post_detail"),
    path("comments/<int:pk>/edit/", CommentUpdateView.as_view(), name="comment_edit"),
    path("comments/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment_delete"),


]

