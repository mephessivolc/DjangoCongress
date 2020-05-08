from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Congress, Images

@receiver(post_save, sender=Congress)
def create_congress(sender, instance, created, **kwargs):
    if created:
        Images.objects.create(congress=instance)
