import re
import uuid

from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.core import validators
from django.db import models

from localflavor.br.models import BRCPFField, BRCNPJField

from .manager import CustomUserManager

# Create your models here.

ie_choices = (
        ('UEMASUL', 'UEMASUL'),
        ('UEMA', 'UEMA'),
        ('IFMA', 'IFMA'),
        ('OUTRO', 'OUTROS'),
    )

curse_choices = (
        ('MAT', "Licenciatura em Matemática"),
        ('FIS', "Licenciatura em Física"),
        ('OUT', "Outro"),
    )

nivel_choices = (
        ('GRAD', "Estudante de Graduação"),
        ('POS', "Estudante de Pós-Graduação"),
        ('PROF', "Professor de Ensino Básico"),
        ("PRSUP", "Professor de Ensino Superior"),
    )

tshirt_choices = (
        ('PP Fem', 'PP Fem'),
        ('P Fem', 'P Fem'),
        ('M Fem', 'M Fem'),
        ('G Fem', 'G Fem'),
        ('GG Fem', 'GG Fem'),
        ('PP Masc', 'PP Masc'),
        ('P Masc', 'P Masc'),
        ('M Masc', 'M Masc'),
        ('G Masc', 'G Masc'),
        ('GG Masc', 'GG Masc'),
    )


class Users(AbstractBaseUser, PermissionsMixin):

    """

    """

    username = models.CharField(
        'Usuário / E-mail', max_length=37, unique=True, validators=[
            validators.RegexValidator(
                re.compile('^[\w.@+-]+$'),
                'Informe um nome de usuário válido. '
                'Este valor deve conter apenas letras, números '
                'e os caracteres: @/./+/-/_ .'
                , 'invalid'
            )
        ], help_text='Um nome curto que será usado para identificá-lo de forma única na plataforma',
        default='',
    )
    name = models.CharField('Nome', max_length=150, default='')
    email = models.EmailField('Email', unique=True)

    is_staff = models.BooleanField('Equipe', default=False)
    is_student = models.BooleanField('Estudante', default=True)
    is_active = models.BooleanField('Ativo', default=True)
    is_payment = models.BooleanField('Pagamento', default=False)

    cpf = BRCPFField('CPF', unique=True, help_text='Somente Números')
    ie = models.CharField('Instituição de Ensino', max_length=7, choices=ie_choices, default='UEMASUL')
    course = models.CharField('Curso', max_length=3, choices=curse_choices, default='MAT')
    nivel = models.CharField('Atuação', max_length=5, choices=nivel_choices, default='GRAD')
    tshirt = models.CharField('Tamanho Camisa', max_length=8, choices=tshirt_choices,
        blank=True, null=True, default=''
    )

    monitor = models.CharField('Monitor', max_length=150, default="", blank=True, null=True)
    date_joined = models.DateTimeField("Data de Entrada", auto_now_add=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'email']

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Conta'
        verbose_name_plural = "Contas"
        ordering = ['name']

    def __str__(self):
        return self.name or self.email

    def get_short_name(self):
        return "{}".format(self.name.split()[0] or self.username)

    def save(self, **kwargs):
        if not self.username:
            self.username = uuid.uuid4()

        super().save(**kwargs)
