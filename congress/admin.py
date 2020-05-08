from django.contrib import admin

from django.contrib import admin
# Register your models here.
from .models import (TypeCongress, Congress, Subscriptions,
    Courses, Institute, AdminCongress, Images
)

from .forms import CongressCreateUpdateForm, CongressForm

class CongressAdminSite(admin.ModelAdmin):
    add_form = CongressCreateUpdateForm
    add_fieldsets = (
        (None, {
            'fields': ('username', 'name', 'type_congress', 'workload'),
        }),
    )

    form = CongressForm
    fieldsets = (
        (None, {
            'fields': ('username', 'name', 'type_congress', 'workload'),
        }),
        ("Informações", {
            'fields': ('is_closed',),
        }),
        ('Datas/Hora', {
            'fields': ('date_start_subscription', 'date_start_congress',
                'date_close_awards', 'date_close_subscription',
                'date_close_congress'),
        }),
    )

admin.site.site_header = "Administração DjangoCongress"
admin.site.register(TypeCongress)
admin.site.register(Subscriptions)
admin.site.register(Congress, CongressAdminSite)
admin.site.register(AdminCongress)
admin.site.register(Courses)
admin.site.register(Institute)
admin.site.register(Images)
