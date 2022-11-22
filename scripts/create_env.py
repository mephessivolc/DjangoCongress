#!/usr/bin/env python

"""
    Django SECRET_KEY generator.
"""
from django.utils.crypto import get_random_string

chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(_-=+)'

CONFIG_STRING = """
ALLOWED_HOSTS=127.0.0.1, .localhost
DEBUG=False
SECRET_KEY=%s
DATABASES=
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
EMAIL_PORT=
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST =
EMAIL_HOST_USER =
EMAIL_HOST_PASSWORD =
DEFAULT_FROM_EMAIL = 
""".strip()%get_random_string(50, chars)

# Writing our configuration file to ".env"
with open('.env', 'w') as configfiles:
    configfiles.write(CONFIG_STRING)
