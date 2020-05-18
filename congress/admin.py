from django.contrib import admin

from django.contrib import admin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
# Register your models here.
from . import models

from .forms import CongressCreateUpdateForm, CongressForm

class LogoImageInline(admin.TabularInline):
    model = models.LogoImages

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
            'fields': ('date_start_subscription', 'date_start',
                'date_close_awards', 'date_close_subscription',
                'date_close'),
        }),
    )

    list_display = ['name', 'get_date', 'get_pdf_url']
    inlines = [LogoImageInline]
    date_hierarchy = 'date_start'

    def get_queryset(self, request):
        qs = super(CongressAdminSite, self).get_queryset(request)

        if request.user.is_superuser:
            return qs

        return qs.filter(subscriptions__is_adm=True)

class CongressSubscritionSite(admin.ModelAdmin):
    list_display = ['__str__','get_congress_info', 'is_adm',
        'is_staff', 'is_payment']

admin.site.site_header = "Administração DjangoCongress"
admin.site.register(models.TypeCongress)
admin.site.register(models.Subscriptions, CongressSubscritionSite)
admin.site.register(models.Congress, CongressAdminSite)
admin.site.register(models.LogoImages)
