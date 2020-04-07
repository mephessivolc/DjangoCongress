from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

from core.models import Congress

User = get_user_model()

class LuckyNumber(models.Model):
    """
        Numero para eventuais sorteios
    """

    congress = models.ForeignKey(Congress, verbose_name='Evento', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="Usuario", on_delete=models.CASCADE)
    number = models.CharField("Numero da sorte", max_length=3)

    class Meta:
        verbose_name = "Numero da Sorte"
        verbose_name_plural = "Sorteios"

    def __str__(self):
        return "({}) {}".format(self.congress, self.user)
