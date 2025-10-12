from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from rest_framework import filters
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from notifications.utils import create_notification
from django.conf import settings

class IsOwnerOrReadOnly:
    """
    Custom permission: only the owner can edit or delete.
    """
    def has_object_permission(self, request, view, obj):
        # Safe methods (GET, HEAD, OPTIONS) allowed
        if request.method in ("GET", "HEAD", "OPTIONS"):
            return True
        # For edits, must be owner
        return obj.author == request.user

class PostViewSet(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["title", "content"]
    ordering_fields = ["created_at", "updated_at"]
    ordering = ["-created_at"]
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        # For update/destroy ensure only authors can
        if self.action in ("update", "partial_update", "destroy"):
            return [IsAuthenticated(), IsOwnerOrReadOnly()]
        return super().get_permissions()

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by("created_at")
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        qs = super().get_queryset()
        post_id = self.request.query_params.get("post")
        if post_id is not None:
            qs = qs.filter(post__id=post_id)
        return qs

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        if self.action in ("update", "partial_update", "destroy"):
            return [IsAuthenticated(), IsOwnerOrReadOnly()]
        return super().get_permissions()


class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # users this user follows
        following_users = user.following.all()
        # posts authored by those users
        qs = Post.objects.filter(author__in=following_users).order_by("-created_at")
        return qs

class LikePostView(generics.GenericAPIView):
    """
    POST to like a post. Requires authentication.
    """
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        user = request.user
        post = get_object_or_404(Post, pk=pk)

        # Prevent liking twice
        like_exists = Like.objects.filter(user=user, post=post).exists()
        if like_exists:
            return Response({"detail": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        like = Like.objects.create(user=user, post=post)
        # Create notification: recipient is the post owner
        create_notification(recipient=post.author, actor=user, verb="liked your post", target=post)
        return Response(LikeSerializer(like).data, status=status.HTTP_201_CREATED)

class UnlikePostView(generics.GenericAPIView):
    """
    POST to unlike a post. Requires authentication.
    """
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        user = request.user
        post = get_object_or_404(Post, pk=pk)
        like_qs = Like.objects.filter(user=user, post=post)
        if not like_qs.exists():
            return Response({"detail": "Like does not exist."}, status=status.HTTP_400_BAD_REQUEST)
        like_qs.delete()
        # Optionally, remove related notifications or mark them read — here we keep notifications as history.
        return Response({"detail": "Unliked"}, status=status.HTTP_200_OK)

