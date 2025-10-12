from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Notification(models.Model):
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="notifications")
    actor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="acted_notifications")
    verb = models.CharField(max_length=255)  # e.g., "liked", "followed", "commented"
    timestamp = models.DateTimeField(auto_now_add=True)
    unread = models.BooleanField(default=True)

    # Generic relation to target object (post, comment, user, etc.)
    target_content_type = models.ForeignKey(ContentType, null=True, blank=True, on_delete=models.CASCADE)
    target_object_id = models.CharField(max_length=255, null=True, blank=True)
    target = GenericForeignKey("target_content_type", "target_object_id")

    class Meta:
        ordering = ["-timestamp"]

    def __str__(self):
        return f"Notification(to={self.recipient}, actor={self.actor}, verb={self.verb})"
