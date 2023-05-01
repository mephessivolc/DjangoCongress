# -*- coding: utf-8 -*-

from django.contrib.auth.backends import ModelBackend as DjangoModelBackend
from django.contrib.auth import get_user_model
from django.contrib import messages

class EmailAuthBackend(DjangoModelBackend):

    def authenticate(self, request, username=None, password=None):
        if not username is None:
            UserModel = get_user_model()
            try:
                user = UserModel.objects.get(email=username)

                if user.check_password(password):
                    return user

            except UserModel.DoesNotExist:
                return None
