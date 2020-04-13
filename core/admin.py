from django.contrib import admin

# Register your models here.
from .models import TypeCongress, Congress, Subscriptions, Courses, Institute, CongressAdmin

admin.site.register(TypeCongress)
admin.site.register(Subscriptions)
admin.site.register(Congress)
admin.site.register(CongressAdmin)
admin.site.register(Courses)
admin.site.register(Institute)
