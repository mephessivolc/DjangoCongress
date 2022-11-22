from django.contrib import admin


# Register your models here.
from .models import Congress

@admin.register(Congress)
class CongressAdmin(admin.ModelAdmin):
    list_display = ['short_name', 'name', 'first_day']