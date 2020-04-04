from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
Users = get_user_model()

class TypeCongress(models.Model):
    """
        Armazena tipo de congressos, exemplo: Colóquio, Simpósios, Semana de Estudos, entre outros
    """
    type_congress = models.CharField('Tipo de Congresso', max_length=50)

    class Meta:
        verbose_name = 'Tipo de Evento'
        verbose_name_plural = 'Tipos de Evento'

    def __str__(self):
        return self.type_congress

class Congress(models.Model):
    """
        Dados essenciais dos Congressos
    """

    username = models.CharField('Apelido do evento', max_length=20)
    name = models.CharField('Nome do Evento', max_length=100)
    type_congress = models.ForeignKey(TypeCongress, verbose_name='Tipo do evento', on_delete=models.CASCADE)
    date_start_subscription = models.DateTimeField("Data/Hora para iniciar inscrições", auto_now=True)
    date_start_congress = models.DateTimeField("Data/Hora para iniciar primeiro dia", auto_now=True)
    date_close_subscription = models.DateTimeField("Data/Hora para finalizar o recebimento das inscrições", auto_now=True)
    date_close_congress = models.DateTimeField("Data/hora da finalização do evento", auto_now=True)
    date_close_awards = models.DateTimeField("Data/hora finalizar inscrições com premiação", auto_now=True)

    class Meta:
        verbose_name = 'Congresso'
        verbose_name_plural = 'Congressos'

    def __str__(self):
        return self.name

class Subscriptions(models.Model):

    """
        Inscritos
    """
    congress = models.ForeignKey(Congress, verbose_name='Congresso', on_delete=models.CASCADE)
    user = models.ForeignKey(Users, verbose_name='Usuario inscrito', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'

    def __str__(self):
        return "{} ({})".format(self.user.name, self.congress.name)
