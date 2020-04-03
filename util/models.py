from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class LuckyNumber(models.Model):
    """
        Numero para eventuais sorteios
    """

    user = models.OneToOneField(User, verbose_name="Usuario", on_delete=models.CASCADE)
    number = models.CharField("Numero da sorte", max_length=3)

    class Meta:
        verbose_name = "Numero da Sorte"
        verbose_name_plural = "Sorteios"

    def __str__(self):
        return "{}".format(user.name)
