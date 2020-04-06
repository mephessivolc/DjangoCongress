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
    path('listas/', views.ListView.as_view(), name='list'),
]
