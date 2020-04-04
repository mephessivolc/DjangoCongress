from django.contrib import admin
from .models import TypeCongress, Congress, Subscriptions

# Register your models here.
admin.site.register(TypeCongress)
admin.site.register(Congress)
admin.site.register(Subscriptions)
