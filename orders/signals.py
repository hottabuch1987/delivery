from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order
from .tasks import send_password_email

@receiver(post_save, sender=Order)
def trigger_password_email(sender, instance, **kwargs):
    if instance.viewed and not kwargs.get('created', False):
        # Вызов задачи Celery
        send_password_email.delay(instance.id)