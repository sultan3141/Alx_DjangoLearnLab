from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post, Comment, Like
from rest_framework import serializers
from django.conf import settings

User = get_user_model()

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Comment
        fields = ("id", "post", "author", "content", "created_at", "updated_at")
        read_only_fields = ("id", "author", "created_at", "updated_at")

    def create(self, validated_data):
        request = self.context.get("request")
        return Comment.objects.create(author=request.user, **validated_data)

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ("id", "author", "title", "content", "created_at", "updated_at", "comments")
        read_only_fields = ("id", "author", "created_at", "updated_at", "comments")

    def create(self, validated_data):
        request = self.context.get("request")
        return Post.objects.create(author=request.user, **validated_data)

class FollowSerializer(serializers.Serializer):
    target_user_id = serializers.IntegerField()

class LikeSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Like
        fields = ["id", "user", "post", "created_at"]
        read_only_fields = ["id", "user", "created_at"]

    