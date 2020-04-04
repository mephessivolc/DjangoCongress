from django.contrib.auth import get_user_model
from django.db import models

from core.models import Congress

Users = get_user_model()

class Minicourses(models.Model):
    """
        Modelo de Banco de dados para registros de Minicursos

        name : Nome do minicurso
        description : Descrição do Minicurso
        quantity_places : Quantidade de vagas disponíveis
    """

    congress = models.ForeignKey(Congress, verbose_name='Evento', on_delete=models.CASCADE)
    teacher = models.Foreing(Users, verbose_name='Palestrante', on_delete=models.CASCADE)
    name = models.CharField('Nome', max_length=100, default='')
    description = models.TextField('Descrição', default='')
    quantity_places = models.CharField('Quantidade de Vagas', max_length=2, default='30')

    class Meta:
        verbose_name = "Minicurso"
        verbose_name_plural = "Minicursos"
        ordering = ['name']

    def __str__(self):
        return self.name

class SubscribeMinicourses(models.Model):
    """
        Modelo de Banco de dados para registros de Inscrições

        minicourse : Registro de Minicurso
        users : Usuário do sistema
        presence_in_first_day : presença no primeiro dia
        presence_in_second_day : presença no segundo dia

        obs: será necessário para outros dias inserir registros seguindo o protocolo
            presence_in_<day>_day.
    """

    minicourse = models.ForeignKey(Minicourses, verbose_name='Minicurso', on_delete=models.CASCADE)
    user = models.ForeignKey(Users, verbose_name='Usuario', on_delete=models.CASCADE)
    presence_in_first_day = models.BooleanField('Presenca Primeiro dia', default=False)
    presence_in_second_day = models.BooleanField('Presenca Segundo dia', default=False)

    class Meta:
        verbose_name = "Inscrição em Minicursos"
        verbose_name_plural = "Inscrições em Minicursos"
        ordering = ['minicourse']

    def __str__(self):
        return "{} - {}".format("Nome", self.minicourse)
