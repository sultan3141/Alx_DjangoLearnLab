# posts/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Like
from notifications.utils import create_notification

@receiver(post_save, sender=Like)
def notify_on_like(sender, instance, created, **kwargs):
    if created:
        post = instance.post
        actor = instance.user
        recipient = post.author
        create_notification(recipient=recipient, actor=actor, verb="liked your post", target=post)
