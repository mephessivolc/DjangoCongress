from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'core'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('listas/', views.ListView.as_view(), name='list'),
]
