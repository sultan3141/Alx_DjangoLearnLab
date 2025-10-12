# notifications/utils.py
from django.contrib.contenttypes.models import ContentType
from .models import Notification

def create_notification(recipient, actor, verb, target=None):
    """
    Create a notification. `target` can be any model instance (post, comment, etc.)
    """
    target_content_type = None
    target_object_id = None
    if target is not None:
        target_content_type = ContentType.objects.get_for_model(target.__class__)
        target_object_id = getattr(target, "pk", None)

    # Avoid creating a notification if actor == recipient (optional)
    if recipient == actor:
        return None

    notification = Notification.objects.create(
        recipient=recipient,
        actor=actor,
        verb=verb,
        target_content_type=target_content_type,
        target_object_id=str(target_object_id) if target_object_id is not None else None,
    )
    return notification
