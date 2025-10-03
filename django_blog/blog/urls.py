from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    add_comment,
    PostByTagListView,
    CommentUpdateView,
    CommentDeleteView,
    search,
)

urlpatterns = [
    # Authentication
    path("login/", auth_views.LoginView.as_view(template_name="blog/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="blog/logout.html"), name="logout"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),

    # Blog Post CRUD
    path("posts/", PostListView.as_view(), name="posts"),                 
    path("post/new/", PostCreateView.as_view(), name="post-create"),     
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),

    # Comments
    path("post/<int:pk>/comments/new/", add_comment, name="add_comment"),
    path("comment/<int:pk>/update/", CommentUpdateView.as_view(), name="comment_edit"),
    path("comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment_delete"),

    # Tag filtering (checker requirement)
    path("tags/<slug:tag_slug>/", PostByTagListView.as_view(), name="tag_posts"),

    # Search
    path("search/", search, name="search"),
]
