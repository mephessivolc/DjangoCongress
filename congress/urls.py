from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from .api_rest.viewsets import CongressViewsets, TypeCongressViewsets, SubscriptionsViewsets
from . import views

router = routers.DefaultRouter()
router.register(r'evento', CongressViewsets)
router.register(r'tipo_evento', TypeCongressViewsets)
router.register(r'inscricao', SubscriptionsViewsets)

app_name = 'congress'
pdfpatterns = [
    path('lista_presenca/<slug:slug>', views.ReportPdf.as_view(), name='report_list_pdf'),
]

urlpatterns = [
    path('api_rest/', include(router.urls)),
    path('imagens/', views.ImagesListView.as_view(), name='images_list'),
    path('imagens/<pk>', views.ImagesDetailView.as_view(), name="images_detail"),
    path('pdf/', include(pdfpatterns)),
]
