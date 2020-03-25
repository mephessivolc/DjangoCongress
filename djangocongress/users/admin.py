from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from .models import Users

class UserAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Users, UserAdmin)
