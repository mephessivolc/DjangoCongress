from django.db import models

from django.utils import timezone
# Create your models here.

class CoreModels(models.Model):

    """
        Modelo de Banco de dados para as datas principais do sistema

        date_start_subscription : Data para iniciar as inscrições no sistema
        data_start_event : Data que irá iniciar o evento
        data_end_subscription : Ultimo dia para fazer inscrições com kits de inscrição
        data_end_event : Data final do evento e inicio do recebimento dos certificados
        data_end_all : Data final de recebimento de certificados e finalização do sistema

        data_end_minicourse : Data e hora para finalização de inscrições em minicursos
    """

    date_start_subscription = models.DateField('Data início inscrição', default=timezone.now)
    data_start_event = models.DateField('Data inicio evento', default=timezone.now)
    data_end_subscription = models.DateField('Data finalização inscrição', default=timezone.now)
    data_end_event = models.DateField('Data final do evento', default=timezone.now)
    data_end_all = models.DateField('Data final do sistema', default=timezone.now)

    data_end_minicourse = models.DateTimeField('Data finalização para Minicurso', default=timezone.now)

    class Meta:
        verbose_name = 'Principal'
        verbose_name_plural = 'Principais'
