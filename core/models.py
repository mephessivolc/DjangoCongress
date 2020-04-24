import os
import uuid

from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

from .utils import UploadToPathAndRename
# Create your models here.
Users = get_user_model()

modal_choices = (
    ('B', 'Bacharelado'),
    ('L', 'Licenciatura'),
    ('PS', 'Pós-Graduação Mestrado'),
    ('PD', 'Pós-Graduação Doutorado'),
    ('PP', 'Pós-Graduação Pós-Doutorado'),
    ('PL', 'Pós-Graduação Lato Sensu'),
    ('TL', 'Tecnólogo'),
    ('T', 'Técnico'),
)

# def path_and_rename(path):
#     def wrapper(instance, filename):
#         # ext = filename.split('.')[-1]
#         ext = os.path.splitext(filename)[1]
#         filename = "{}.{}".format(uuid.uuid4(), ext)
#         return os.path.join(path, filename)
#
#     return wrapper

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

class Institute(models.Model):
    username = models.CharField('Sigla da Unidade de Ensino', max_length=15)
    name = models.CharField('Nome da Unidade de Ensino', max_length=100)

    class Meta:
        verbose_name = 'Instituição de Ensino'
        verbose_name_plural = 'Instituições de Ensino'

    def __str__(self):
        return self.name

class Courses(models.Model):
    name = models.CharField('Curso', max_length=30)
    modal = models.CharField('Modalidade', max_length=10, choices=modal_choices, default='L')
    institute = models.ForeignKey(Institute, verbose_name='Unidade de Ensino', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def get_readable_choices(self):
        return dict(modal_choices)[self.modal]

    def __str__(self):
        return "{} - {} ({})".format(self.name, self.modal, self.institute.username)

class Congress(models.Model):
    """
        Dados essenciais dos Congressos
    """

    username = models.CharField('Apelido do evento', max_length=20, blank=True, null=True)
    slug = models.SlugField('Referencia', max_length=100, blank=True, null=True, default="")
    name = models.CharField('Nome do Evento', max_length=100)
    type_congress = models.ForeignKey(TypeCongress, verbose_name='Tipo do evento', on_delete=models.CASCADE)
    date_start_subscription = models.DateTimeField("Iniciar Inscrições", auto_now=False, auto_now_add=False, default=timezone.now)
    date_start_congress = models.DateTimeField("Primeiro dia", auto_now=False, auto_now_add=False, default=timezone.now)
    date_close_subscription = models.DateTimeField("Encerrar Recebimento de Inscrições", auto_now=False, auto_now_add=False, default=timezone.now)
    date_close_congress = models.DateTimeField("Finalização do evento", auto_now=False, auto_now_add=False, default=timezone.now)
    date_close_awards = models.DateTimeField("Finalizar Inscrições com Premiação", auto_now=False, auto_now_add=False, default=timezone.now)

    is_closed = models.BooleanField('Está fechado?', default=False)

    class Meta:
        verbose_name = 'Congresso'
        verbose_name_plural = 'Congressos'

    def __str__(self):
        return self.name

class AdminCongress(models.Model):
    """
        Cadastro de Sub-Administradores do Congresso. Sub-Administradores sao usuarios que podem atualizar dados do
        congresso enquanto este permanece em periodo ativo.
    """

    user = models.ForeignKey(Users, verbose_name='Administrador do Evento', on_delete=models.DO_NOTHING)
    congress = models.ForeignKey(Congress, verbose_name='Congresso', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Administrador do Evento'
        verbose_name_plural = "Administradores do Evento"
        permissions = [('core.congress.change_congress', "Can Change Congress")]

    def __str__(self):
        return "({}/{}) {}".format(self.congress.username, self.congress.date_close_congress.strftime("%Y"), self.user)


class Subscriptions(models.Model):

    """
        Inscritos
    """
    congress = models.ForeignKey(Congress, verbose_name='Congresso', on_delete=models.CASCADE)
    user = models.ForeignKey(Users, verbose_name='Usuario inscrito', on_delete=models.CASCADE)
    is_staff = models.BooleanField('Monitor', default=False)
    is_payment = models.BooleanField('Pagamento', default=False)

    class Meta:
        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'

    def __str__(self):
        return "{} ({})".format(self.user.name, self.congress.name)

class ImagesCongress(models.Model):
    congress = models.OneToOneField(Congress, on_delete=models.CASCADE)
    image = models.ImageField("Logo", default="media/default.png", upload_to=UploadToPathAndRename('congress/logo/'))

    class Meta:
        verbose_name = 'Logo'
        verbose_name_plural = 'Logos'

    def __str__(self):
        return "{} ({})".format(self.congress.username, self.congress.date_start_congress.strftime("%m/%Y"))

class LuckyNumber(models.Model):
    """
        Numero para eventuais sorteios
    """

    congress = models.ForeignKey(Congress, verbose_name='Evento', on_delete=models.CASCADE)
    user = models.ForeignKey(Users, verbose_name="Usuario", on_delete=models.CASCADE)
    number = models.CharField("Numero da sorte", max_length=3)

    class Meta:
        verbose_name = "Numero da Sorte"
        verbose_name_plural = "Sorteios"

    def __str__(self):
        return "({}) {}".format(self.congress, self.user)
