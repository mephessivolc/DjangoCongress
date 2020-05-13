from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Courses)
admin.site.register(models.Institute)
