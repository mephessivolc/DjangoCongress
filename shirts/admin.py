from django.contrib import admin

# Register your models here.
from .models import Shirts, ColorShirts, SizeShirts, TypeShirts, RequestShirts

admin.site.register(ColorShirts)
admin.site.register(SizeShirts)
admin.site.register(TypeShirts)
admin.site.register(RequestShirts)
admin.site.register(Shirts)
