from django.db.models.signals import post_save
from django.dispatch import receiver

from . import models

@receiver(post_save, sender=models.Congress)
def create_congress(sender, instance, created, **kwargs):
    if created:
        models.LogoImages.objects.create(congress=instance)
