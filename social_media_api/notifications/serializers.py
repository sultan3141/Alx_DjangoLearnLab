# notifications/serializers.py
from rest_framework import serializers
from .models import Notification
from django.contrib.contenttypes.models import ContentType

class NotificationSerializer(serializers.ModelSerializer):
    actor_username = serializers.CharField(source="actor.username", read_only=True)
    target_repr = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = ["id", "actor", "actor_username", "verb", "target_repr", "timestamp", "unread"]

    def get_target_repr(self, obj):
        if obj.target is None:
            return None
        try:
            return str(obj.target)
        except Exception:
            return {"id": obj.target_object_id, "type": obj.target_content_type.model}
