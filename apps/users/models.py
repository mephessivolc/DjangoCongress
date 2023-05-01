from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin

import re
import uuid

from localflavor.br.models import BRCPFField, BRCNPJField

from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.core import validators
from django.db import models

from localflavor.br.models import BRCPFField, BRCNPJField

from .manager import CustomUserManager
# Create your models here.


class Users(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(
            primary_key=True,
            default=uuid.uuid4,
            editable=False,
        )
    name = models.CharField('Nome', max_length=150, default='')
    email = models.EmailField('Email', unique=True)

    is_staff = models.BooleanField('Equipe', default=False)
    is_active = models.BooleanField('Ativo', default=True)

    

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    # def save(self, **kwargs):
    #     if not self.username:
    #         self.username = uuid.uuid4()

    #     super().save(**kwargs)
