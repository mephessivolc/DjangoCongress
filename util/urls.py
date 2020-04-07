from django.urls import path
from django.conf.urls import include

from . import views
from rest_framework import routers

from .api_rest.viewsets import LuckyNumberViewsets

router = routers.DefaultRouter()
router.register(r'numero_sorte', LuckyNumberViewsets)

app_name = 'util'
urlpatterns = [
    path('api_rest/', include(router.urls)),

]
