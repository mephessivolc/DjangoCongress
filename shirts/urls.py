from django.urls import path
from django.conf.urls import include

from rest_framework import routers

from shirts.api_rest.viewsets import ShirtViewsets

router = routers.DefaultRouter()
router.register(r'camisas', ShirtViewsets)

app_name = 'shirts'
urlpatterns = [
    path('api_rest/', include(router.urls)),

]
