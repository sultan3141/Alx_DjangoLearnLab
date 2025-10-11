from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework import filters

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
