from django.db import models

# Create your models here.

class Congress(models.Model):

    name = models.CharField("Nome", max_length=200)
    short_name = models.CharField("Sigla", max_length=25)
    first_day = models.DateTimeField("Início em")
    last_day = models.DateTimeField("Término em")

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
        ordering = ['short_name', 'first_day', 'name']

    def __str__(self) -> str:
        return f"{self.name}"