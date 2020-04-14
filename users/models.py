import re
import unicodedata
import uuid

from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.core import validators
from django.db import models
from django.urls import reverse

from localflavor.br.models import BRCPFField, BRCNPJField

from .manager import CustomUserManager
# Create your models here.

class Users(AbstractBaseUser, PermissionsMixin):

    """
        Usuarios do sistema
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

    name = models.CharField('Nome', max_length=150, default='', validators=[
        validators.RegexValidator(re.compile('[^\W\d_]+$', re.UNICODE),
        'Digite um nome válido (somente letras)',
        'invalido')
    ])
    email = models.EmailField('Email', unique=True)

    is_staff = models.BooleanField('Equipe', default=False)
    is_active = models.BooleanField('Ativo', default=True)

    cpf = BRCPFField('CPF', unique=True, help_text='Somente Números')

    date_joined = models.DateTimeField("Data de Entrada", auto_now_add=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'email', 'cpf']

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Conta'
        verbose_name_plural = "Contas"
        ordering = ['name']

    def __str__(self):
        return self.name or self.email

    def get_short_name(self):
        return "{}".format(self.name.split()[0] or self.username)

    def get_create_url(self):
        return reverse('users:create')

    def get_update_url(self):
        return reverse('users:update', kwargs={'slug': self.username})

    def get_unicode_name(self):
        # Unicode normalize transforma um caracter em seu equivalente em latin.
        nfkd = unicodedata.normalize('NFKD', self.name)
        title_unicode = u"".join([c for c in nfkd if not unicodedata.combining(c)])

        # Usa expressão regular para retornar a palavra apenas com números, letras e espaço
        title_unicode = re.sub('[^a-zA-Z0-9 \\\]', '', title_unicode)
        # title_unicode = title_unicode.replace(' ', '_')
        return title_unicode

    def save(self, **kwargs):
        if not self.username:
            self.username = uuid.uuid4()

        super().save(**kwargs)
