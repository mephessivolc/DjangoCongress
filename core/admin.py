from django.contrib import admin

# Register your models here.
from .models import TypeCongress, Congress, Subscriptions

admin.site.register(TypeCongress)
admin.site.register(Subscriptions)
admin.site.register(Congress)
