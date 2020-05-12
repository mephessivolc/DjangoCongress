from django.contrib import admin

from django.contrib import admin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
# Register your models here.
from .models import (TypeCongress, Congress, Subscriptions,
    Courses, Institute, Images
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
            'fields': ('slug', 'username', 'name', 'type_congress', 'workload'),
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

    list_display = ['name', 'get_date', 'get_pdf_url']

class CongressSubscritionSite(admin.ModelAdmin):
    list_display = ['__str__', 'is_adm',
        'is_staff', 'is_payment']

admin.site.site_header = "Administração DjangoCongress"
admin.site.register(TypeCongress)
admin.site.register(Subscriptions, CongressSubscritionSite)
admin.site.register(Congress, CongressAdminSite)
admin.site.register(Courses)
admin.site.register(Institute)
admin.site.register(Images)
