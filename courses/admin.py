from django.contrib import admin

# Register your models here.
from .models import Institute, Courses

admin.site.register(Institute)
admin.site.register(Courses)
