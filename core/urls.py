from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from .api_rest.viewsets import CongressViewsets, TypeCongressViewsets, SubscriptionsViewsets
from . import views

router = routers.DefaultRouter()
router.register(r'evento', CongressViewsets)
router.register(r'tipo_evento', TypeCongressViewsets)
router.register(r'inscricao', SubscriptionsViewsets)

app_name = 'core'
urlpatterns = [
    path('api_rest/', include(router.urls)),
    path('', views.Index.as_view(), name='index'),
    path('evento/', views.CongressCreateView.as_view(), name='create_congress'),
    path('tipo_evento/', views.TypeCongressCreateView.as_view(), name='create_type_congress'),
]
